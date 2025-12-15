"""
Amazon Ads Advertising Accounts API (异步版本)

官方 Spec: AdvertisingAccounts.json
验证日期: 2024-12-15

官方端点数: 5
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class AdvertisingAccountsAPI(BaseAdsClient):
    """
    Advertising Accounts API (全异步)
    
    API Tier: L1
    Source: OpenAPI
    OpenAPI_SPEC: AdvertisingAccounts.json
    Stability: 高
    
    管理广告账户，包括创建、查询和条款接受。
    官方验证: 5个端点
    """

    # ==================== Accounts ====================

    async def create_account(
        self,
        account_data: dict[str, Any],
    ) -> JSONData:
        """
        创建广告账户
        
        官方端点: POST /adsAccounts
        
        Args:
            account_data: 账户创建数据，包含:
                - name: 账户名称
                - countryCode: 国家代码
                - currencyCode: 货币代码
                - timezone: 时区
                - type: 账户类型 (seller, vendor, agency)
        """
        result = await self.post("/adsAccounts", json_data=account_data)
        return result if isinstance(result, dict) else {}

    async def list_accounts(
        self,
        filters: dict[str, Any] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取广告账户列表
        
        官方端点: POST /adsAccounts/list
        
        Args:
            filters: 过滤条件
            max_results: 每页数量
            next_token: 分页令牌
            
        Returns:
            {
                "adsAccounts": [...],
                "nextToken": "..."
            }
        """
        body: dict[str, Any] = {"maxResults": max_results}
        
        if filters:
            body["filters"] = filters
        if next_token:
            body["nextToken"] = next_token
        
        result = await self.post("/adsAccounts/list", json_data=body)
        return result if isinstance(result, dict) else {"adsAccounts": []}

    async def get_account(
        self,
        advertising_account_id: str,
    ) -> JSONData:
        """
        获取广告账户详情
        
        官方端点: GET /adsAccounts/{advertisingAccountId}
        
        Args:
            advertising_account_id: 广告账户 ID
        """
        result = await self.get(f"/adsAccounts/{advertising_account_id}")
        return result if isinstance(result, dict) else {}

    # ==================== Terms Tokens ====================

    async def create_terms_token(
        self,
        token_data: dict[str, Any],
    ) -> JSONData:
        """
        创建条款令牌
        
        官方端点: POST /termsTokens
        
        用于记录用户接受服务条款的令牌
        
        Args:
            token_data: 令牌数据，包含:
                - termsType: 条款类型
                - accepted: 是否接受
        """
        result = await self.post("/termsTokens", json_data=token_data)
        return result if isinstance(result, dict) else {}

    async def get_terms_token(
        self,
        terms_token: str,
    ) -> JSONData:
        """
        获取条款令牌状态
        
        官方端点: GET /termsTokens/{termsToken}
        
        Args:
            terms_token: 条款令牌
        """
        result = await self.get(f"/termsTokens/{terms_token}")
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def list_all_accounts(self) -> JSONList:
        """获取所有广告账户（自动分页）"""
        all_accounts: JSONList = []
        next_token = None
        
        while True:
            result = await self.list_accounts(
                max_results=100,
                next_token=next_token,
            )
            accounts = result.get("adsAccounts", [])
            all_accounts.extend(accounts)
            
            next_token = result.get("nextToken")
            if not next_token:
                break
        
        return all_accounts

    async def accept_terms(self, terms_type: str) -> JSONData:
        """接受服务条款"""
        return await self.create_terms_token({
            "termsType": terms_type,
            "accepted": True,
        })

