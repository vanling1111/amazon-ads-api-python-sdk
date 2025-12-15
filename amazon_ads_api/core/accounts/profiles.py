"""
Profiles & Manager Accounts API (异步版本)

官方文档:
- Profiles: https://advertising.amazon.com/API/docs/en-us/reference/2/profiles
- Manager Accounts: https://advertising.amazon.com/API/docs/en-us/guides/account-management/authorization/manager-accounts

广告账户 Profile 和 Manager Account 管理
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


# Content-Type 常量
MANAGER_ACCOUNT_V1 = "application/vnd.manageraccount.v1+json"
CREATE_MANAGER_ACCOUNT_V1 = "application/vnd.createmanageraccountrequest.v1+json"
GET_MANAGER_ACCOUNTS_V1 = "application/vnd.getmanageraccountsresponse.v1+json"
UPDATE_ACCOUNTS_REQUEST_V1 = "application/vnd.updateadvertisingaccountsinmanageraccountrequest.v1+json"
UPDATE_ACCOUNTS_RESPONSE_V1 = "application/vnd.updateadvertisingaccountsinmanageraccountresponse.v1+json"


class ProfilesAPI(BaseAdsClient):
    """
    Profiles & Manager Accounts API (全异步)
    
    Profiles API (v2):
    - GET /v2/profiles
    - PUT /v2/profiles
    
    Manager Accounts API (v3):
    - GET /managerAccounts
    - POST /managerAccounts
    - POST /managerAccounts/{id}/associate
    - POST /managerAccounts/{id}/disassociate
    """

    # ============ Profiles (v2) ============

    async def list_profiles(
        self,
        api_program: str | None = None,
        access_level: str | None = None,
        profile_type_filter: str | None = None,
        valid_payment_method_filter: str | None = None,
    ) -> JSONList:
        """
        获取所有广告 Profile
        
        GET /v2/profiles
        
        Profile 代表一个市场的广告账户
        每个市场（US, UK, DE等）有独立的 Profile
        
        Args:
            api_program: 过滤有特定权限的 Profile
                - billing
                - campaign (默认)
                - paymentMethod
                - store
                - report
                - account
                - posts
            access_level: 过滤访问级别
                - edit (默认)
                - view
            profile_type_filter: 过滤账户类型（逗号分隔）
                - seller
                - vendor
                - agency
            valid_payment_method_filter: 过滤有效支付方式
                - true
                - false
        
        Returns:
            [
                {
                    "profileId": 123,
                    "countryCode": "US",
                    "currencyCode": "USD",
                    "dailyBudget": 1000.0,
                    "timezone": "America/Los_Angeles",
                    "accountInfo": {
                        "marketplaceStringId": "ATVPDKIKX0DER",
                        "id": "ENTITY...",
                        "type": "seller" | "vendor" | "agency",
                        "name": "My Account",
                        "validPaymentMethod": true
                    }
                }
            ]
        """
        params: JSONData = {}
        
        if api_program:
            params["apiProgram"] = api_program
        if access_level:
            params["accessLevel"] = access_level
        if profile_type_filter:
            params["profileTypeFilter"] = profile_type_filter
        if valid_payment_method_filter:
            params["validPaymentMethodFilter"] = valid_payment_method_filter
        
        result = await self.get("/v2/profiles", params=params if params else None)
        return result if isinstance(result, list) else []

    async def get_profile(self, profile_id: str) -> JSONData:
        """
        获取单个 Profile 详情
        
        官方端点: GET /v2/profiles/{profileId}
        官方文档: Profiles_v3.yaml
        
        Args:
            profile_id: Profile ID
        """
        result = await self.get(f"/v2/profiles/{profile_id}")
        return result if isinstance(result, dict) else {}

    async def update_profiles(self, profiles: JSONList) -> JSONList:
        """
        批量更新 Profile
        
        PUT /v2/profiles
        
        注意：此操作仅适用于使用 Sponsored Products 的卖家
        不适用于 vendor 类型账户
        
        Args:
            profiles: [
                {
                    "profileId": 123,
                    "dailyBudget": 1000.0
                }
            ]
        
        Returns:
            更新后的 Profile 列表
        """
        result = await self.put("/v2/profiles", json_data=profiles)
        return result if isinstance(result, list) else []

    async def update_profile(self, profile_id: str, daily_budget: float) -> JSONData:
        """更新单个 Profile 的每日预算"""
        result = await self.update_profiles([{
            "profileId": int(profile_id),
            "dailyBudget": daily_budget,
        }])
        return result[0] if result else {}

    # ============ Manager Accounts (v3) ============

    async def list_manager_accounts(self) -> JSONData:
        """
        获取 Manager Accounts 列表
        
        GET /managerAccounts
        
        Manager Account 可以管理多个 Profile
        返回最多 50 个关联的账户
        
        Returns:
            {
                "managerAccounts": [
                    {
                        "managerAccountId": "xxx",
                        "managerAccountName": "My Manager Account",
                        "linkedAccounts": [
                            {
                                "accountId": "xxx",
                                "accountName": "...",
                                "accountType": "SELLER" | "VENDOR" | "DSP_ADVERTISING_ACCOUNT" | "MARKETING_CLOUD",
                                "marketplaceId": "ATVPDKIKX0DER",
                                "profileId": "123",
                                "dspAdvertiserId": "..."
                            }
                        ]
                    }
                ]
            }
        """
        result = await self.get(
            "/managerAccounts",
            accept=GET_MANAGER_ACCOUNTS_V1
        )
        return result if isinstance(result, dict) else {"managerAccounts": []}

    async def create_manager_account(
        self,
        name: str,
        account_type: str = "Advertiser",
    ) -> JSONData:
        """
        创建 Manager Account
        
        POST /managerAccounts
        
        Args:
            name: Manager Account 名称
            account_type: 账户类型
                - Advertiser: 管理自己的产品和服务
                - Agency: 代理管理客户账户
        
        Returns:
            {
                "managerAccountId": "xxx",
                "managerAccountName": "...",
                "linkedAccounts": []
            }
        """
        body = {
            "managerAccountName": name,
            "managerAccountType": account_type,
        }
        result = await self.post(
            "/managerAccounts",
            json_data=body,
            content_type=CREATE_MANAGER_ACCOUNT_V1,
            accept=MANAGER_ACCOUNT_V1
        )
        return result if isinstance(result, dict) else {}

    async def associate_accounts(
        self,
        manager_account_id: str,
        accounts: list[dict],
    ) -> JSONData:
        """
        将广告账户关联到 Manager Account
        
        POST /managerAccounts/{managerAccountId}/associate
        
        Args:
            manager_account_id: Manager Account ID
            accounts: 要关联的账户列表（最多 20 个）
                [
                    {
                        "id": "ENTITY..." | "DSP_ADVERTISER_ID",
                        "type": "ACCOUNT_ID" | "DSP_ADVERTISER_ID",
                        "roles": ["ENTITY_USER"]  # 可选
                    }
                ]
        
        Returns:
            {
                "succeedAccounts": [...],
                "failedAccounts": [...]
            }
        """
        body = {"accounts": accounts}
        result = await self.post(
            f"/managerAccounts/{manager_account_id}/associate",
            json_data=body,
            content_type=UPDATE_ACCOUNTS_REQUEST_V1,
            accept=UPDATE_ACCOUNTS_RESPONSE_V1
        )
        return result if isinstance(result, dict) else {}

    async def disassociate_accounts(
        self,
        manager_account_id: str,
        accounts: list[dict],
    ) -> JSONData:
        """
        解除广告账户与 Manager Account 的关联
        
        POST /managerAccounts/{managerAccountId}/disassociate
        
        Args:
            manager_account_id: Manager Account ID
            accounts: 要解除关联的账户列表（最多 20 个）
                [
                    {
                        "id": "ENTITY...",
                        "type": "ACCOUNT_ID"
                    }
                ]
        
        Returns:
            {
                "succeedAccounts": [...],
                "failedAccounts": [...]
            }
        """
        body = {"accounts": accounts}
        result = await self.post(
            f"/managerAccounts/{manager_account_id}/disassociate",
            json_data=body,
            content_type=UPDATE_ACCOUNTS_REQUEST_V1,
            accept=UPDATE_ACCOUNTS_RESPONSE_V1
        )
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def get_profile_by_marketplace(self, marketplace: str) -> JSONData | None:
        """
        根据市场获取 Profile
        
        Args:
            marketplace: US, CA, UK, DE, FR, IT, ES, JP, AU, AE, SA, ...
        """
        profiles = await self.list_profiles()
        for profile in profiles:
            if profile.get("countryCode") == marketplace:
                return profile
        return None

    async def get_seller_profiles(self) -> JSONList:
        """获取所有 Seller Profile"""
        profiles = await self.list_profiles(profile_type_filter="seller")
        return profiles

    async def get_vendor_profiles(self) -> JSONList:
        """获取所有 Vendor Profile"""
        profiles = await self.list_profiles(profile_type_filter="vendor")
        return profiles

    async def get_profile_daily_budget(self, profile_id: str) -> float:
        """获取 Profile 每日预算"""
        profile = await self.get_profile(profile_id)
        return profile.get("dailyBudget", 0.0)

    async def set_profile_daily_budget(self, profile_id: str, daily_budget: float) -> JSONData:
        """设置 Profile 每日预算"""
        return await self.update_profile(profile_id, daily_budget)

    async def link_account_to_manager(
        self,
        manager_account_id: str,
        account_id: str,
        account_type: str = "ACCOUNT_ID",
    ) -> JSONData:
        """
        将单个账户关联到 Manager Account
        
        Args:
            manager_account_id: Manager Account ID
            account_id: 账户 ID（ENTITY... 或 DSP Advertiser ID）
            account_type: ACCOUNT_ID 或 DSP_ADVERTISER_ID
        """
        return await self.associate_accounts(
            manager_account_id,
            [{"id": account_id, "type": account_type}]
        )

    async def unlink_account_from_manager(
        self,
        manager_account_id: str,
        account_id: str,
        account_type: str = "ACCOUNT_ID",
    ) -> JSONData:
        """
        解除单个账户与 Manager Account 的关联
        """
        return await self.disassociate_accounts(
            manager_account_id,
            [{"id": account_id, "type": account_type}]
        )
