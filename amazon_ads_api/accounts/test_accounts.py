"""
Amazon Ads Test Accounts API (异步版本)
测试账户管理
"""

from typing import Any
from ..base import BaseAdsClient, JSONData, JSONList


class TestAccountsAPI(BaseAdsClient):
    """Test Accounts API - 测试账户管理 (全异步)"""

    # ==================== 测试账户管理 ====================

    async def list_test_accounts(self) -> JSONList:
        """获取所有测试账户列表"""
        response = await self.get("/testAccounts")
        if isinstance(response, dict):
            return response.get("testAccounts", [])
        return []

    async def create_test_account(
        self,
        name: str,
        country_code: str,
        account_type: str = "seller",
        timezone: str | None = None,
    ) -> JSONData:
        """创建测试账户"""
        data: dict[str, Any] = {
            "name": name,
            "countryCode": country_code,
            "accountType": account_type,
        }
        if timezone:
            data["timezone"] = timezone

        result = await self.post("/testAccounts", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_test_account(self, test_account_id: str) -> JSONData:
        """获取测试账户详情"""
        result = await self.get(f"/testAccounts/{test_account_id}")
        return result if isinstance(result, dict) else {}

    async def delete_test_account(self, test_account_id: str) -> JSONData:
        """删除测试账户"""
        result = await self.delete(f"/testAccounts/{test_account_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 测试数据管理 ====================

    async def generate_test_data(
        self,
        test_account_id: str,
        data_type: str,
        config: dict[str, Any] | None = None,
    ) -> JSONData:
        """为测试账户生成测试数据"""
        data: dict[str, Any] = {"dataType": data_type}
        if config:
            data["config"] = config

        result = await self.post(
            f"/testAccounts/{test_account_id}/data", json_data=data
        )
        return result if isinstance(result, dict) else {}

    async def reset_test_account(self, test_account_id: str) -> JSONData:
        """重置测试账户数据"""
        result = await self.post(f"/testAccounts/{test_account_id}/reset")
        return result if isinstance(result, dict) else {}

    # ==================== 测试账户授权 ====================

    async def get_test_account_credentials(self, test_account_id: str) -> JSONData:
        """获取测试账户API凭证"""
        result = await self.get(f"/testAccounts/{test_account_id}/credentials")
        return result if isinstance(result, dict) else {}

    async def refresh_test_account_credentials(
        self, test_account_id: str
    ) -> JSONData:
        """刷新测试账户API凭证"""
        result = await self.post(
            f"/testAccounts/{test_account_id}/credentials/refresh"
        )
        return result if isinstance(result, dict) else {}
