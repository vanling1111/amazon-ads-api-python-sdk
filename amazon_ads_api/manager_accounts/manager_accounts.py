"""
Amazon Ads Manager Accounts API (异步版本)
"""

from typing import Any
from ..base import BaseAdsClient, JSONData


class ManagerAccountsAPI(BaseAdsClient):
    """Manager Accounts API (全异步)"""

    async def create_manager_account(
        self,
        name: str,
        *,
        description: str | None = None,
    ) -> JSONData:
        """创建新的Manager Account"""
        request_body: dict[str, Any] = {"name": name}
        if description:
            request_body["description"] = description

        result = await self.post("/managerAccounts", json_data=request_body)
        return result if isinstance(result, dict) else {}

    async def get_manager_accounts(self) -> JSONData:
        """获取当前用户有权访问的所有Manager Accounts"""
        result = await self.get("/managerAccounts")
        return result if isinstance(result, dict) else {"managerAccounts": []}

    async def link_accounts(
        self,
        manager_account_id: str,
        accounts: list[dict[str, Any]],
    ) -> JSONData:
        """将广告账户关联到Manager Account"""
        result = await self.post(
            f"/managerAccounts/{manager_account_id}/associate",
            json_data={"accounts": accounts},
        )
        return result if isinstance(result, dict) else {}

    async def unlink_accounts(
        self,
        manager_account_id: str,
        accounts: list[dict[str, Any]],
    ) -> JSONData:
        """取消广告账户与Manager Account的关联"""
        result = await self.post(
            f"/managerAccounts/{manager_account_id}/disassociate",
            json_data={"accounts": accounts},
        )
        return result if isinstance(result, dict) else {}
