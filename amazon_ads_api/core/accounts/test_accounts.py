"""
Amazon Ads Test Accounts API (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/guides/account-management/test-accounts/overview
OpenAPI Spec: AdvertisingTestAccount_prod_3p.json

测试账户管理
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class TestAccountsAPI(BaseAdsClient):
    """
    Test Accounts API (全异步)
    
    官方端点 (共2个):
    - GET /testAccounts - 获取测试账户信息
    - POST /testAccounts - 创建测试账户
    
    注意:
    - 每个市场只能创建 1 个测试账户
    - 支持的账户类型: AUTHOR, VENDOR
    - 测试账户用于 API 集成测试，不产生实际费用
    """

    async def get_test_accounts(
        self,
        request_id: str | None = None,
    ) -> JSONList:
        """
        获取测试账户信息
        
        GET /testAccounts
        
        Args:
            request_id: 可选，按请求 ID 过滤
        
        Returns:
            [
                {
                    "id": "ENTITY012345678910",
                    "accountType": "AUTHOR" | "VENDOR",
                    "countryCode": "US",
                    "status": "COMPLETED" | "IN_PROGRESS" | "FAILED",
                    "asins": ["B0123456789", "B0123456789", "B0123456789"]  # AUTHOR 账户有 3 个 ASIN
                }
            ]
        """
        params = {}
        if request_id:
            params["requestId"] = request_id
        
        result = await self.get(
            "/testAccounts",
            params=params if params else None
        )
        return result if isinstance(result, list) else []

    async def create_test_account(
        self,
        account_type: str,
        country_code: str,
        vendor_code: str | None = None,
    ) -> JSONData:
        """
        创建测试账户
        
        POST /testAccounts
        
        Args:
            account_type: 账户类型
                - "AUTHOR": 作者账户（用于图书广告）
                - "VENDOR": 供应商账户（用于品牌广告）
            country_code: 国家代码
                - 支持: AE, AU, BE, BR, CA, DE, EG, ES, FR, IT, JP, MX, NL, PL, SA, SE, SG, TR, UK, US
            vendor_code: 供应商代码（仅 VENDOR 类型需要）
        
        Returns:
            {
                "requestId": "A7BCDGCEVXQ1CJJ4301V"
            }
            
        注意:
            - 每个市场只能创建 1 个同类型的测试账户
            - 创建是异步的，使用返回的 requestId 查询状态
            - 创建完成后，测试账户将包含 3 个预设的 ASIN
        """
        body: JSONData = {
            "accountType": account_type,
            "countryCode": country_code,
        }
        
        if vendor_code:
            body["accountMetaData"] = {"vendorCode": vendor_code}
        
        result = await self.post("/testAccounts", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def create_author_account(self, country_code: str) -> JSONData:
        """
        创建 Author 测试账户
        
        用于图书广告测试
        """
        return await self.create_test_account(
            account_type="AUTHOR",
            country_code=country_code
        )

    async def create_vendor_account(
        self,
        country_code: str,
        vendor_code: str,
    ) -> JSONData:
        """
        创建 Vendor 测试账户
        
        用于品牌广告测试
        """
        return await self.create_test_account(
            account_type="VENDOR",
            country_code=country_code,
            vendor_code=vendor_code
        )

    async def get_account_by_country(
        self,
        country_code: str,
    ) -> JSONData | None:
        """根据国家代码获取测试账户"""
        accounts = await self.get_test_accounts()
        for account in accounts:
            if account.get("countryCode") == country_code:
                return account
        return None

    async def check_creation_status(self, request_id: str) -> str:
        """
        检查测试账户创建状态
        
        Returns:
            "COMPLETED" | "IN_PROGRESS" | "FAILED"
        """
        accounts = await self.get_test_accounts(request_id=request_id)
        if accounts and len(accounts) > 0:
            return accounts[0].get("status", "UNKNOWN")
        return "NOT_FOUND"

    async def get_completed_accounts(self) -> JSONList:
        """获取所有已完成创建的测试账户"""
        accounts = await self.get_test_accounts()
        return [a for a in accounts if a.get("status") == "COMPLETED"]
