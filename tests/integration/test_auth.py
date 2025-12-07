"""
Integration tests for authentication
Note: These tests require valid credentials set as environment variables:
  - AMAZON_ADS_CLIENT_ID
  - AMAZON_ADS_CLIENT_SECRET
  - AMAZON_ADS_REFRESH_TOKEN
  - AMAZON_ADS_PROFILE_ID (optional)
"""
import os
import pytest
from amazon_ads_api import AmazonAdsClient, AdsRegion
from amazon_ads_api.base import AmazonAdsError


# Skip integration tests if no credentials
def has_valid_credentials():
    """Check if valid credentials are available"""
    client_id = os.environ.get("AMAZON_ADS_CLIENT_ID", "")
    return client_id and client_id != "test_client_id"


requires_credentials = pytest.mark.skipif(
    not has_valid_credentials(),
    reason="Requires valid Amazon Ads API credentials"
)


class TestOAuth2Authentication:
    """Test OAuth2 authentication flow"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_token_refresh_with_valid_credentials(self):
        """Test that token can be refreshed with valid credentials"""
        client = AmazonAdsClient(
            client_id=os.environ["AMAZON_ADS_CLIENT_ID"],
            client_secret=os.environ["AMAZON_ADS_CLIENT_SECRET"],
            refresh_token=os.environ["AMAZON_ADS_REFRESH_TOKEN"],
            region=AdsRegion.NA,
        )
        
        # Force token refresh
        token = client._refresh_access_token()
        
        assert token is not None
        assert len(token) > 0
        assert client._access_token == token
        assert client._token_expires_at is not None
    
    @requires_credentials
    @pytest.mark.integration
    def test_token_caching(self):
        """Test that token is cached and reused"""
        client = AmazonAdsClient(
            client_id=os.environ["AMAZON_ADS_CLIENT_ID"],
            client_secret=os.environ["AMAZON_ADS_CLIENT_SECRET"],
            refresh_token=os.environ["AMAZON_ADS_REFRESH_TOKEN"],
            region=AdsRegion.NA,
        )
        
        # First call should refresh token
        token1 = client._get_access_token()
        # Second call should return cached token
        token2 = client._get_access_token()
        
        assert token1 == token2
    
    @pytest.mark.integration
    def test_invalid_credentials(self):
        """Test authentication fails with invalid credentials"""
        client = AmazonAdsClient(
            client_id="invalid_client_id",
            client_secret="invalid_client_secret",
            refresh_token="invalid_refresh_token",
            region=AdsRegion.NA,
        )
        
        with pytest.raises(AmazonAdsError) as exc_info:
            client._refresh_access_token()
        
        # Should be 400 or 401
        assert exc_info.value.status_code in [400, 401]


class TestProfilesAPI:
    """Test Profiles API - most basic API call"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_profiles(self):
        """Test getting profiles list"""
        client = AmazonAdsClient(
            client_id=os.environ["AMAZON_ADS_CLIENT_ID"],
            client_secret=os.environ["AMAZON_ADS_CLIENT_SECRET"],
            refresh_token=os.environ["AMAZON_ADS_REFRESH_TOKEN"],
            region=AdsRegion.NA,
        )
        
        profiles = client.accounts.profiles.list_profiles()
        
        assert isinstance(profiles, list)
        # If we have profiles, verify structure
        if len(profiles) > 0:
            profile = profiles[0]
            assert "profileId" in profile
            assert "countryCode" in profile
    
    @requires_credentials
    @pytest.mark.integration
    def test_get_profile(self):
        """Test getting a specific profile"""
        profile_id = os.environ.get("AMAZON_ADS_PROFILE_ID")
        if not profile_id:
            pytest.skip("AMAZON_ADS_PROFILE_ID not set")
        
        client = AmazonAdsClient(
            client_id=os.environ["AMAZON_ADS_CLIENT_ID"],
            client_secret=os.environ["AMAZON_ADS_CLIENT_SECRET"],
            refresh_token=os.environ["AMAZON_ADS_REFRESH_TOKEN"],
            region=AdsRegion.NA,
        )
        
        profile = client.accounts.profiles.get_profile(profile_id)
        
        assert profile is not None
        assert str(profile.get("profileId")) == profile_id


class TestRegions:
    """Test different regions"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_na_region_endpoint(self):
        """Test North America region endpoint"""
        client = AmazonAdsClient(
            client_id=os.environ["AMAZON_ADS_CLIENT_ID"],
            client_secret=os.environ["AMAZON_ADS_CLIENT_SECRET"],
            refresh_token=os.environ["AMAZON_ADS_REFRESH_TOKEN"],
            region=AdsRegion.NA,
        )
        
        assert client.base_url == "https://advertising-api.amazon.com"
        
        # Try to list profiles - should work if credentials are for NA
        try:
            profiles = client.accounts.profiles.list_profiles()
            assert isinstance(profiles, list)
        except AmazonAdsError as e:
            # 403 is expected if credentials are not for NA region
            if e.status_code != 403:
                raise
    
    @pytest.mark.integration
    def test_eu_region_endpoint(self):
        """Test Europe region endpoint"""
        client = AmazonAdsClient(
            client_id=os.environ.get("AMAZON_ADS_CLIENT_ID", "test"),
            client_secret=os.environ.get("AMAZON_ADS_CLIENT_SECRET", "test"),
            refresh_token=os.environ.get("AMAZON_ADS_REFRESH_TOKEN", "test"),
            region=AdsRegion.EU,
        )
        
        assert client.base_url == "https://advertising-api-eu.amazon.com"
    
    @pytest.mark.integration
    def test_fe_region_endpoint(self):
        """Test Far East region endpoint"""
        client = AmazonAdsClient(
            client_id=os.environ.get("AMAZON_ADS_CLIENT_ID", "test"),
            client_secret=os.environ.get("AMAZON_ADS_CLIENT_SECRET", "test"),
            refresh_token=os.environ.get("AMAZON_ADS_REFRESH_TOKEN", "test"),
            region=AdsRegion.FE,
        )
        
        assert client.base_url == "https://advertising-api-fe.amazon.com"


class TestHeadersInRequests:
    """Test that correct headers are sent with requests"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_authorization_header(self):
        """Test Authorization header is sent"""
        client = AmazonAdsClient(
            client_id=os.environ["AMAZON_ADS_CLIENT_ID"],
            client_secret=os.environ["AMAZON_ADS_CLIENT_SECRET"],
            refresh_token=os.environ["AMAZON_ADS_REFRESH_TOKEN"],
            region=AdsRegion.NA,
        )
        
        headers = client._get_headers()
        
        assert "Authorization" in headers
        assert headers["Authorization"].startswith("Bearer ")
        assert "Amazon-Advertising-API-ClientId" in headers
        assert headers["Amazon-Advertising-API-ClientId"] == os.environ["AMAZON_ADS_CLIENT_ID"]
    
    @requires_credentials
    @pytest.mark.integration
    def test_profile_scope_header(self):
        """Test Amazon-Advertising-API-Scope header is sent when profile is set"""
        profile_id = os.environ.get("AMAZON_ADS_PROFILE_ID")
        if not profile_id:
            pytest.skip("AMAZON_ADS_PROFILE_ID not set")
        
        client = AmazonAdsClient(
            client_id=os.environ["AMAZON_ADS_CLIENT_ID"],
            client_secret=os.environ["AMAZON_ADS_CLIENT_SECRET"],
            refresh_token=os.environ["AMAZON_ADS_REFRESH_TOKEN"],
            region=AdsRegion.NA,
        )
        client.with_profile(profile_id)
        
        headers = client._get_headers()
        
        assert "Amazon-Advertising-API-Scope" in headers
        assert headers["Amazon-Advertising-API-Scope"] == profile_id
