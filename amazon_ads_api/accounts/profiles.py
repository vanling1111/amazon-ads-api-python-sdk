"""
Profiles API
广告账户Profile管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class ProfilesAPI(BaseAdsClient):
    """Profiles API"""

    # ============ Profiles ============

    def list_profiles(self) -> JSONList:
        """
        获取所有广告Profile
        
        Profile代表一个市场的广告账户
        每个市场（US, UK, DE等）有独立的Profile
        """
        result = self.get("/v2/profiles")
        return result if isinstance(result, list) else []

    def get_profile(self, profile_id: str) -> JSONData:
        """获取单个Profile详情"""
        result = self.get(f"/v2/profiles/{profile_id}")
        return result if isinstance(result, dict) else {}

    def update_profile(self, profile_id: str, updates: JSONData) -> JSONData:
        """
        更新Profile
        
        Args:
            updates: {
                "dailyBudget": 1000.0,  # 每日预算上限
            }
        """
        result = self.put(f"/v2/profiles/{profile_id}", json_data=updates)
        return result if isinstance(result, dict) else {}

    # ============ Manager Accounts ============

    def list_manager_accounts(self) -> JSONList:
        """
        获取Manager Accounts列表
        
        Manager Account可以管理多个Profile
        """
        result = self.get("/managerAccounts")
        return result if isinstance(result, list) else []

    def create_manager_account(
        self,
        name: str,
        email: str,
    ) -> JSONData:
        """创建Manager Account"""
        result = self.post("/managerAccounts", json_data={
            "name": name,
            "email": email,
        })
        return result if isinstance(result, dict) else {}

    # ============ Account Associations ============

    def list_account_associations(self, manager_account_id: str) -> JSONList:
        """获取Manager Account关联的广告账户"""
        result = self.get(f"/managerAccounts/{manager_account_id}/associations")
        return result if isinstance(result, list) else []

    def create_account_association(
        self,
        manager_account_id: str,
        profile_id: str,
    ) -> JSONData:
        """将Profile关联到Manager Account"""
        result = self.post(f"/managerAccounts/{manager_account_id}/associations", json_data={
            "profileId": profile_id,
        })
        return result if isinstance(result, dict) else {}

    def delete_account_association(
        self,
        manager_account_id: str,
        profile_id: str,
    ) -> JSONData:
        """解除Profile与Manager Account的关联"""
        return self.delete(f"/managerAccounts/{manager_account_id}/associations/{profile_id}")

    # ============ API Tokens ============

    def get_token_info(self) -> JSONData:
        """获取当前Token信息"""
        result = self.get("/v2/token/info")
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    def get_profile_by_marketplace(self, marketplace: str) -> JSONData | None:
        """
        根据市场获取Profile
        
        Args:
            marketplace: US, CA, UK, DE, FR, IT, ES, JP, AU, AE, SA, ...
        """
        profiles = self.list_profiles()
        for profile in profiles:
            if profile.get("countryCode") == marketplace:
                return profile
        return None

    def get_seller_profiles(self) -> JSONList:
        """获取所有Seller Profile"""
        profiles = self.list_profiles()
        return [p for p in profiles if p.get("accountInfo", {}).get("type") == "seller"]

    def get_vendor_profiles(self) -> JSONList:
        """获取所有Vendor Profile"""
        profiles = self.list_profiles()
        return [p for p in profiles if p.get("accountInfo", {}).get("type") == "vendor"]

    def get_profile_daily_budget(self, profile_id: str) -> float:
        """获取Profile每日预算"""
        profile = self.get_profile(profile_id)
        return profile.get("dailyBudget", 0.0)

    def set_profile_daily_budget(self, profile_id: str, daily_budget: float) -> JSONData:
        """设置Profile每日预算"""
        return self.update_profile(profile_id, {"dailyBudget": daily_budget})

