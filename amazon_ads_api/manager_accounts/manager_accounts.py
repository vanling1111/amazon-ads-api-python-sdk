"""
Manager Accounts API

端点前缀: /managerAccounts
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class ManagerAccountsAPI(BaseAdsClient):
    """Manager Accounts管理 - 管理一组Amazon广告账户"""
    
    async def create_manager_account(
        self,
        name: str,
        *,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """创建新的Manager Account"""
        request_body: Dict[str, Any] = {"name": name}
        if description:
            request_body["description"] = description
            
        return await self._request(
            "POST",
            "/managerAccounts",
            json=request_body
        )
    
    async def get_manager_accounts(self) -> Dict[str, Any]:
        """获取当前用户有权访问的所有Manager Accounts"""
        return await self._request("GET", "/managerAccounts")
    
    async def link_accounts(
        self,
        manager_account_id: str,
        accounts: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        将广告账户关联到Manager Account
        
        Args:
            manager_account_id: Manager Account ID
            accounts: 要关联的账户列表，每个账户包含:
                - accountId: 账户ID
                - accountType: 账户类型 (SELLER, VENDOR, ADVERTISER等)
                - role: 关系角色 (OWNER, VIEWER等)
        """
        return await self._request(
            "POST",
            f"/managerAccounts/{manager_account_id}/associate",
            json={"accounts": accounts}
        )
    
    async def unlink_accounts(
        self,
        manager_account_id: str,
        accounts: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        取消广告账户与Manager Account的关联
        
        Args:
            manager_account_id: Manager Account ID
            accounts: 要取消关联的账户列表
        """
        return await self._request(
            "POST",
            f"/managerAccounts/{manager_account_id}/disassociate",
            json={"accounts": accounts}
        )

