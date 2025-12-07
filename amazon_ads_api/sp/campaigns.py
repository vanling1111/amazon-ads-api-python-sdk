"""
Sponsored Products - Campaigns API
SP广告系列管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SPCampaignsAPI(BaseAdsClient):
    """SP Campaigns API"""

    def list_campaigns(
        self,
        state_filter: str | None = None,
        name_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取Campaign列表
        
        Args:
            state_filter: enabled, paused, archived
            name_filter: 名称过滤
            max_results: 最大结果数(1-100)
            next_token: 分页token
            
        Returns:
            {"campaigns": [...], "nextToken": "..."}
        """
        params: JSONData = {"maxResults": max_results}
        if state_filter:
            params["stateFilter"] = state_filter
        if name_filter:
            params["name"] = name_filter
        if next_token:
            params["nextToken"] = next_token

        result = self.post("/sp/campaigns/list", json_data=params)
        return result if isinstance(result, dict) else {"campaigns": []}

    def get_campaign(self, campaign_id: str) -> JSONData:
        """获取单个Campaign详情"""
        result = self.get(f"/sp/campaigns/{campaign_id}")
        return result if isinstance(result, dict) else {}

    def create_campaigns(self, campaigns: JSONList) -> JSONData:
        """
        批量创建Campaign
        
        Args:
            campaigns: Campaign列表
            [
                {
                    "name": "My Campaign",
                    "targetingType": "MANUAL",  # MANUAL | AUTO
                    "state": "enabled",
                    "dailyBudget": 10.0,
                    "startDate": "20240101",
                    "bidding": {
                        "strategy": "LEGACY_FOR_SALES"
                    }
                }
            ]
        """
        result = self.post("/sp/campaigns", json_data={"campaigns": campaigns})
        return result if isinstance(result, dict) else {"campaigns": {"success": [], "error": []}}

    def update_campaigns(self, campaigns: JSONList) -> JSONData:
        """
        批量更新Campaign
        
        Args:
            campaigns: 包含campaignId的更新数据
            [{"campaignId": "xxx", "state": "paused", "dailyBudget": 20.0}]
        """
        result = self.put("/sp/campaigns", json_data={"campaigns": campaigns})
        return result if isinstance(result, dict) else {"campaigns": {"success": [], "error": []}}

    def delete_campaign(self, campaign_id: str) -> JSONData:
        """归档Campaign"""
        return self.delete(f"/sp/campaigns/{campaign_id}")

    # ============ 便捷方法 ============

    def pause_campaign(self, campaign_id: str) -> JSONData:
        """暂停Campaign"""
        return self.update_campaigns([{"campaignId": campaign_id, "state": "paused"}])

    def enable_campaign(self, campaign_id: str) -> JSONData:
        """启用Campaign"""
        return self.update_campaigns([{"campaignId": campaign_id, "state": "enabled"}])

    def update_budget(self, campaign_id: str, daily_budget: float) -> JSONData:
        """更新Campaign日预算"""
        return self.update_campaigns([{
            "campaignId": campaign_id,
            "dailyBudget": daily_budget
        }])

    def update_bidding_strategy(self, campaign_id: str, strategy: str) -> JSONData:
        """
        更新竞价策略
        
        Args:
            strategy: LEGACY_FOR_SALES | AUTO_FOR_SALES | MANUAL
        """
        return self.update_campaigns([{
            "campaignId": campaign_id,
            "bidding": {"strategy": strategy}
        }])

    # ============ 批量获取所有Campaign ============

    def list_all_campaigns(
        self,
        state_filter: str | None = None,
    ) -> JSONList:
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

