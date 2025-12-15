"""
Amazon Ads API SDK - SaaS Multi-Tenant Integration Example

This example demonstrates how to properly integrate the SDK
in a multi-tenant SaaS application with multiple users and Amazon Ads accounts.

Architecture:
- SDK Layer: Handles Amazon Ads API communication (this SDK)
- Service Layer: Manages users, accounts, and client pooling (your application)
- API Layer: FastAPI endpoints for your users (your application)

Key Concepts:
1. SDK is multi-account capable (concurrent safe)
2. SaaS layer manages tenant boundaries
3. Each profile gets its own client instance
4. Permission checks happen before SDK calls
"""

import asyncio
from typing import Dict, Optional
from datetime import datetime

# Third-party (your SaaS dependencies)
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from fastapi import APIRouter, Depends, HTTPException

# This SDK
from amazon_ads_api import AmazonAdsClient, AdsRegion


# ============================================================
# 1. Database Models (Your SaaS)
# ============================================================

Base = declarative_base()


class Tenant(Base):
    """Multi-tenant SaaS: Tenant (Company/Organization)"""
    __tablename__ = 'tenants'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class User(Base):
    """SaaS Users"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, ForeignKey('tenants.id'), nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String)  # 'admin', 'member', 'viewer'


class AmazonAccount(Base):
    """
    Amazon Ads Accounts (one tenant can have multiple accounts)
    
    Note: client_secret and refresh_token should be encrypted in production!
    """
    __tablename__ = 'amazon_accounts'
    
    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, ForeignKey('tenants.id'), nullable=False)  # 🔑 Tenant boundary
    
    # Amazon OAuth credentials
    client_id = Column(String, nullable=False)
    client_secret = Column(String, nullable=False)  # ⚠️ Encrypt in production!
    
    # Account info
    account_name = Column(String)  # User-defined, e.g., "US Main Account"
    region = Column(String, nullable=False)  # 'NA', 'EU', 'FE'
    
    created_at = Column(DateTime, default=datetime.utcnow)


class AmazonProfile(Base):
    """
    Amazon Ads Profiles/Stores (one account can have multiple profiles)
    
    Each profile has its own refresh_token
    """
    __tablename__ = 'amazon_profiles'
    
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('amazon_accounts.id'), nullable=False)
    
    # Profile info
    profile_id = Column(String, unique=True, nullable=False)  # Amazon Profile ID
    profile_name = Column(String)  # User-defined, e.g., "Store A"
    marketplace = Column(String)  # 'US', 'CA', 'UK', etc.
    
    # OAuth token (per profile)
    refresh_token = Column(String, nullable=False)  # ⚠️ Encrypt in production!
    access_token = Column(String)
    token_expires_at = Column(DateTime)
    
    # Status
    is_active = Column(Boolean, default=True)
    last_synced_at = Column(DateTime)


# ============================================================
# 2. Service Layer (Your SaaS Business Logic)
# ============================================================

class AdsClientService:
    """
    Service Layer: Manages multi-tenant Amazon Ads clients
    
    Responsibilities:
    - Validate user permissions (prevent cross-tenant access)
    - Create one SDK client per profile
    - Manage client caching
    - Handle token refresh persistence
    """
    
    def __init__(self, db: Session):
        self.db = db
        self._client_cache: Dict[str, AmazonAdsClient] = {}  # {profile_id: client}
        self._lock = asyncio.Lock()
    
    async def get_client_for_user(
        self, 
        user_id: int, 
        profile_id: str
    ) -> AmazonAdsClient:
        """
        Get SDK client for a specific user and profile
        
        🔒 Security: Validates user has access to this profile
        
        Args:
            user_id: Your SaaS user ID
            profile_id: Amazon Profile ID
            
        Returns:
            AmazonAdsClient instance
            
        Raises:
            PermissionError: User doesn't have access to this profile
        """
        # 1. Get user and tenant
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError(f"User {user_id} not found")
        
        # 2. 🔒 Validate profile belongs to user's tenant (critical!)
        profile = self.db.query(AmazonProfile).join(
            AmazonAccount
        ).filter(
            AmazonProfile.profile_id == profile_id,
            AmazonAccount.tenant_id == user.tenant_id  # 🔑 Tenant boundary check
        ).first()
        
        if not profile:
            raise PermissionError(
                f"User {user_id} (tenant {user.tenant_id}) "
                f"does not have access to profile {profile_id}"
            )
        
        # 3. Get Amazon Account
        account = self.db.query(AmazonAccount).filter(
            AmazonAccount.id == profile.account_id
        ).first()
        
        # 4. Create or reuse SDK client
        if profile_id not in self._client_cache:
            async with self._lock:
                if profile_id not in self._client_cache:
                    self._client_cache[profile_id] = AmazonAdsClient(
                        client_id=account.client_id,
                        client_secret=account.client_secret,
                        refresh_token=profile.refresh_token,
                        profile_id=profile.profile_id,
                        region=AdsRegion(account.region)
                    )
        
        return self._client_cache[profile_id]
    
    async def get_all_tenant_clients(
        self, 
        tenant_id: int
    ) -> Dict[str, AmazonAdsClient]:
        """
        Get SDK clients for all profiles of a tenant
        
        Used for batch operations
        
        Args:
            tenant_id: Your SaaS tenant ID
            
        Returns:
            Dict mapping profile_id to AmazonAdsClient
        """
        # Get all active profiles for this tenant
        profiles = self.db.query(AmazonProfile).join(
            AmazonAccount
        ).filter(
            AmazonAccount.tenant_id == tenant_id,
            AmazonProfile.is_active == True
        ).all()
        
        clients = {}
        for profile in profiles:
            if profile.profile_id not in self._client_cache:
                account = profile.account
                self._client_cache[profile.profile_id] = AmazonAdsClient(
                    client_id=account.client_id,
                    client_secret=account.client_secret,
                    refresh_token=profile.refresh_token,
                    profile_id=profile.profile_id,
                    region=AdsRegion(account.region)
                )
            clients[profile.profile_id] = self._client_cache[profile.profile_id]
        
        return clients
    
    async def batch_fetch_campaigns(
        self, 
        user_id: int, 
        profile_ids: list[str]
    ) -> Dict[str, dict]:
        """
        Batch fetch campaigns for multiple profiles (concurrent)
        
        Leverages SDK's multi-account capability
        """
        # Get clients for all profiles (with permission checks)
        clients = [
            await self.get_client_for_user(user_id, pid) 
            for pid in profile_ids
        ]
        
        # SDK guarantees concurrent safety!
        results = await asyncio.gather(*[
            client.sp.campaigns.list_campaigns() 
            for client in clients
        ])
        
        return dict(zip(profile_ids, results))


# ============================================================
# 3. API Layer (Your SaaS FastAPI Endpoints)
# ============================================================

router = APIRouter()


def get_current_user() -> User:
    """FastAPI dependency: Get current user from JWT token"""
    # Your JWT validation logic here
    # For demo purposes, returning a mock user
    pass


def get_db() -> Session:
    """FastAPI dependency: Get database session"""
    # Your database session logic here
    pass


def get_client_service(db: Session = Depends(get_db)) -> AdsClientService:
    """FastAPI dependency: Get AdsClientService instance"""
    return AdsClientService(db)


@router.get("/campaigns")
async def get_campaigns(
    profile_id: str,
    current_user: User = Depends(get_current_user),
    client_service: AdsClientService = Depends(get_client_service)
):
    """
    API Endpoint: Get campaigns for a specific profile
    
    Flow:
    1. FastAPI validates JWT token → current_user
    2. Service layer validates user has access to profile
    3. Service layer gets SDK client
    4. SDK layer calls Amazon Ads API
    
    Returns:
        Campaign data from Amazon Ads API
    """
    try:
        # Service layer handles permission check
        client = await client_service.get_client_for_user(
            current_user.id, 
            profile_id
        )
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    
    # SDK layer handles Amazon Ads API call
    campaigns = await client.sp.campaigns.list_campaigns()
    
    return campaigns


@router.get("/all-campaigns")
async def get_all_user_campaigns(
    current_user: User = Depends(get_current_user),
    client_service: AdsClientService = Depends(get_client_service),
    db: Session = Depends(get_db)
):
    """
    API Endpoint: Batch get campaigns for all user's profiles
    
    Demonstrates concurrent multi-profile fetching
    
    Returns:
        Dict mapping profile_id to campaign data
    """
    # 1. Get all profiles for user's tenant (SaaS layer)
    profiles = db.query(AmazonProfile).join(
        AmazonAccount
    ).filter(
        AmazonAccount.tenant_id == current_user.tenant_id,
        AmazonProfile.is_active == True
    ).all()
    
    profile_ids = [p.profile_id for p in profiles]
    
    # 2. Batch fetch (SDK guarantees concurrent safety)
    results = await client_service.batch_fetch_campaigns(
        current_user.id, 
        profile_ids
    )
    
    return results


# ============================================================
# 4. Usage Example
# ============================================================

async def main():
    """
    Example: How a SaaS application uses the SDK
    """
    # Simulate database setup
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    
    engine = create_engine('sqlite:///example.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    db = Session()
    
    # Create service
    client_service = AdsClientService(db)
    
    # Example 1: Single profile access
    try:
        client = await client_service.get_client_for_user(
            user_id=1, 
            profile_id='profile-123'
        )
        campaigns = await client.sp.campaigns.list_campaigns()
        print(f"Campaigns: {campaigns}")
    except PermissionError as e:
        print(f"Access denied: {e}")
    
    # Example 2: Batch access (concurrent)
    profile_ids = ['profile-123', 'profile-456', 'profile-789']
    results = await client_service.batch_fetch_campaigns(
        user_id=1, 
        profile_ids=profile_ids
    )
    print(f"Batch results: {results}")
    
    # Example 3: All tenant profiles
    tenant_clients = await client_service.get_all_tenant_clients(tenant_id=1)
    all_campaigns = await asyncio.gather(*[
        client.sp.campaigns.list_campaigns() 
        for client in tenant_clients.values()
    ])
    print(f"All tenant campaigns: {all_campaigns}")


if __name__ == "__main__":
    asyncio.run(main())

