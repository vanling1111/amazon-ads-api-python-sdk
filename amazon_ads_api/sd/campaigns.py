"""
Sponsored Display - Campaigns API
SD广告系列管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SDCampaignsAPI(BaseAdsClient):
    """SD Campaigns API"""

    # ============ Campaigns ============

    def list_campaigns(
        self,
        state_filter: str | None = None,
        name_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取SD Campaign列表
        
        Args:
            state_filter: enabled, paused, archived
            name_filter: 名称过滤
            max_results: 最大结果数
        """
        params: JSONData = {"maxResults": max_results}
        if state_filter:
            params["stateFilter"] = state_filter
        if name_filter:
            params["nameFilter"] = name_filter
        if next_token:
            params["nextToken"] = next_token

        result = self.post("/sd/campaigns/list", json_data=params)
        return result if isinstance(result, dict) else {"campaigns": []}

    def get_campaign(self, campaign_id: str) -> JSONData:
        """获取单个SD Campaign详情"""
        result = self.get(f"/sd/campaigns/{campaign_id}")
        return result if isinstance(result, dict) else {}

    def create_campaigns(self, campaigns: JSONList) -> JSONData:
        """
        批量创建SD Campaign
        
        Args:
            campaigns: [
                {
                    "name": "My SD Campaign",
                    "state": "enabled",
                    "budget": 100.0,
                    "budgetType": "daily",
                    "startDate": "20240101",
                    "tactic": "T00020",  # 受众定向
                    "costType": "cpc"
                }
            ]
        
        Tactics:
        - T00020: 受众(Views)
        - T00030: 受众(Purchases)
        - T00001: 上下文定向
        """
        result = self.post("/sd/campaigns", json_data=campaigns)
        return result if isinstance(result, dict) else {"campaigns": {"success": [], "error": []}}

    def update_campaigns(self, campaigns: JSONList) -> JSONData:
        """批量更新SD Campaign"""
        result = self.put("/sd/campaigns", json_data=campaigns)
        return result if isinstance(result, dict) else {"campaigns": {"success": [], "error": []}}

    def delete_campaign(self, campaign_id: str) -> JSONData:
        """归档SD Campaign"""
        return self.delete(f"/sd/campaigns/{campaign_id}")

    # ============ Ad Groups ============

    def list_ad_groups(
        self,
        campaign_id: str | None = None,
        state_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取SD Ad Group列表"""
        params: JSONData = {"maxResults": max_results}
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]
        if state_filter:
            params["stateFilter"] = state_filter
        if next_token:
            params["nextToken"] = next_token

        result = self.post("/sd/adGroups/list", json_data=params)
        return result if isinstance(result, dict) else {"adGroups": []}

    def get_ad_group(self, ad_group_id: str) -> JSONData:
        """获取单个SD Ad Group详情"""
        result = self.get(f"/sd/adGroups/{ad_group_id}")
        return result if isinstance(result, dict) else {}

    def create_ad_groups(self, ad_groups: JSONList) -> JSONData:
        """
        批量创建SD Ad Group
        
        Args:
            ad_groups: [
                {
                    "campaignId": "xxx",
                    "name": "My Ad Group",
                    "state": "enabled",
                    "defaultBid": 1.0,
                    "bidOptimization": "reach"  # reach | pageVisits | conversions
                }
            ]
        """
        result = self.post("/sd/adGroups", json_data=ad_groups)
        return result if isinstance(result, dict) else {"adGroups": {"success": [], "error": []}}

    def update_ad_groups(self, ad_groups: JSONList) -> JSONData:
        """批量更新SD Ad Group"""
        result = self.put("/sd/adGroups", json_data=ad_groups)
        return result if isinstance(result, dict) else {"adGroups": {"success": [], "error": []}}

    def delete_ad_group(self, ad_group_id: str) -> JSONData:
        """归档SD Ad Group"""
        return self.delete(f"/sd/adGroups/{ad_group_id}")

    # ============ Product Ads ============

    def list_product_ads(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        state_filter: str | None = None,
        max_results: int = 100,
    ) -> JSONData:
        """获取SD Product Ad列表"""
        params: JSONData = {"maxResults": max_results}
        if ad_group_id:
            params["adGroupIdFilter"] = [ad_group_id]
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]
        if state_filter:
            params["stateFilter"] = state_filter

        result = self.post("/sd/productAds/list", json_data=params)
        return result if isinstance(result, dict) else {"productAds": []}

    def create_product_ads(self, product_ads: JSONList) -> JSONData:
        """
        批量创建SD Product Ad
        
        Args:
            product_ads: [
                {
                    "campaignId": "xxx",
                    "adGroupId": "xxx",
                    "state": "enabled",
                    "asin": "B00XXXX"
                }
            ]
        """
        result = self.post("/sd/productAds", json_data=product_ads)
        return result if isinstance(result, dict) else {"productAds": {"success": [], "error": []}}

    def update_product_ads(self, product_ads: JSONList) -> JSONData:
        """批量更新SD Product Ad"""
        result = self.put("/sd/productAds", json_data=product_ads)
        return result if isinstance(result, dict) else {"productAds": {"success": [], "error": []}}

    def delete_product_ad(self, ad_id: str) -> JSONData:
        """归档SD Product Ad"""
        return self.delete(f"/sd/productAds/{ad_id}")

    # ============ Forecasts ============

    def get_campaign_forecast(
        self,
        tactic: str,
        targeting: list[dict],
        daily_budget: float,
    ) -> JSONData:
        """
        获取Campaign预测
        
        预测给定设置下的Impressions、Clicks等
        """
        result = self.post("/sd/forecasts", json_data={
            "tactic": tactic,
            "targeting": targeting,
            "dailyBudget": daily_budget,
        })
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    def pause_campaign(self, campaign_id: str) -> JSONData:
        """暂停Campaign"""
        return self.update_campaigns([{"campaignId": campaign_id, "state": "paused"}])

    def enable_campaign(self, campaign_id: str) -> JSONData:
        """启用Campaign"""
        return self.update_campaigns([{"campaignId": campaign_id, "state": "enabled"}])

    def update_budget(self, campaign_id: str, budget: float) -> JSONData:
        """更新Campaign预算"""
        return self.update_campaigns([{"campaignId": campaign_id, "budget": budget}])

    def list_all_campaigns(self, state_filter: str | None = None) -> JSONList:
        """获取所有Campaign（自动分页）"""
        all_campaigns = []
        next_token = None

        while True:
            result = self.list_campaigns(
                state_filter=state_filter,
                max_results=100,
                next_token=next_token,
            )
            campaigns = result.get("campaigns", [])
            all_campaigns.extend(campaigns)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_campaigns

    def create_audience_campaign(
        self,
        name: str,
        daily_budget: float,
        tactic: str = "T00020",
    ) -> JSONData:
        """
        快速创建受众定向Campaign
        
        Args:
            name: Campaign名称
            daily_budget: 日预算
            tactic: T00020(Views) | T00030(Purchases)
        """
        campaigns = [{
            "name": name,
            "state": "enabled",
            "budget": daily_budget,
            "budgetType": "daily",
            "tactic": tactic,
            "costType": "cpc",
        }]
        return self.create_campaigns(campaigns)

    def create_contextual_campaign(
        self,
        name: str,
        daily_budget: float,
    ) -> JSONData:
        """
        快速创建上下文定向Campaign
        
        Args:
            name: Campaign名称
            daily_budget: 日预算
        """
        campaigns = [{
            "name": name,
            "state": "enabled",
            "budget": daily_budget,
            "budgetType": "daily",
            "tactic": "T00001",  # Contextual targeting
            "costType": "cpc",
        }]
        return self.create_campaigns(campaigns)

