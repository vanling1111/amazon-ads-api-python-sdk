"""
Sponsored Brands - Campaigns API (异步版本)
SB广告系列管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SBCampaignsAPI(BaseAdsClient):
    """SB Campaigns API (全异步)"""

    # ============ Campaigns ============

    async def list_campaigns(
        self,
        state_filter: str | None = None,
        name_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取SB Campaign列表
        
        Args:
            state_filter: enabled, paused, archived
            name_filter: 名称过滤
            max_results: 最大结果数
            next_token: 分页token
        """
        params: JSONData = {"maxResults": max_results}
        if state_filter:
            params["stateFilter"] = state_filter
        if name_filter:
            params["nameFilter"] = name_filter
        if next_token:
            params["nextToken"] = next_token

        result = await self.post("/sb/v4/campaigns/list", json_data=params)
        return result if isinstance(result, dict) else {"campaigns": []}

    async def get_campaign(self, campaign_id: str) -> JSONData:
        """获取单个SB Campaign详情"""
        result = await self.get(f"/sb/v4/campaigns/{campaign_id}")
        return result if isinstance(result, dict) else {}

    async def create_campaigns(self, campaigns: JSONList) -> JSONData:
        """
        批量创建SB Campaign
        
        Args:
            campaigns: [
                {
                    "name": "My SB Campaign",
                    "state": "enabled",
                    "budget": 100.0,
                    "budgetType": "DAILY",
                    "startDate": "2024-01-01",
                    "bidOptimization": true,
                    "bidMultiplier": 1.0
                }
            ]
        """
        result = await self.post("/sb/v4/campaigns", json_data={"campaigns": campaigns})
        return result if isinstance(result, dict) else {"campaigns": {"success": [], "error": []}}

    async def update_campaigns(self, campaigns: JSONList) -> JSONData:
        """
        批量更新SB Campaign
        
        Args:
            campaigns: [{"campaignId": "xxx", "state": "paused", "budget": 200.0}]
        """
        result = await self.put("/sb/v4/campaigns", json_data={"campaigns": campaigns})
        return result if isinstance(result, dict) else {"campaigns": {"success": [], "error": []}}

    async def delete_campaign(self, campaign_id: str) -> JSONData:
        """归档SB Campaign"""
        return await self.delete(f"/sb/v4/campaigns/{campaign_id}")

    # ============ Ad Groups ============

    async def list_ad_groups(
        self,
        campaign_id: str | None = None,
        state_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取SB Ad Group列表"""
        params: JSONData = {"maxResults": max_results}
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]
        if state_filter:
            params["stateFilter"] = state_filter
        if next_token:
            params["nextToken"] = next_token

        result = await self.post("/sb/v4/adGroups/list", json_data=params)
        return result if isinstance(result, dict) else {"adGroups": []}

    async def get_ad_group(self, ad_group_id: str) -> JSONData:
        """获取单个SB Ad Group详情"""
        result = await self.get(f"/sb/v4/adGroups/{ad_group_id}")
        return result if isinstance(result, dict) else {}

    async def create_ad_groups(self, ad_groups: JSONList) -> JSONData:
        """批量创建SB Ad Group"""
        result = await self.post("/sb/v4/adGroups", json_data={"adGroups": ad_groups})
        return result if isinstance(result, dict) else {"adGroups": {"success": [], "error": []}}

    async def update_ad_groups(self, ad_groups: JSONList) -> JSONData:
        """批量更新SB Ad Group"""
        result = await self.put("/sb/v4/adGroups", json_data={"adGroups": ad_groups})
        return result if isinstance(result, dict) else {"adGroups": {"success": [], "error": []}}

    # ============ Budget Rules ============

    async def list_budget_rules(self, campaign_id: str | None = None) -> JSONList:
        """获取SB Budget Rule列表"""
        params = {}
        if campaign_id:
            params["campaignIdFilter"] = campaign_id
        result = await self.get("/sb/budgetRules", params=params or None)
        return result if isinstance(result, list) else []

    async def create_budget_rules(self, rules: JSONList) -> JSONList:
        """批量创建SB Budget Rule"""
        result = await self.post("/sb/budgetRules", json_data=rules)
        return result if isinstance(result, list) else []

    async def update_budget_rules(self, rules: JSONList) -> JSONList:
        """批量更新SB Budget Rule"""
        result = await self.put("/sb/budgetRules", json_data=rules)
        return result if isinstance(result, list) else []

    async def delete_budget_rule(self, rule_id: str) -> JSONData:
        """删除SB Budget Rule"""
        return await self.delete(f"/sb/budgetRules/{rule_id}")

    # ============ Insights ============

    async def get_campaign_insights(
        self,
        campaign_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取Campaign洞察数据"""
        result = await self.get(f"/sb/v4/campaigns/{campaign_id}/insights", params={
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def pause_campaign(self, campaign_id: str) -> JSONData:
        """暂停Campaign"""
        return await self.update_campaigns([{"campaignId": campaign_id, "state": "paused"}])

    async def enable_campaign(self, campaign_id: str) -> JSONData:
        """启用Campaign"""
        return await self.update_campaigns([{"campaignId": campaign_id, "state": "enabled"}])

    async def update_budget(self, campaign_id: str, budget: float) -> JSONData:
        """更新Campaign预算"""
        return await self.update_campaigns([{"campaignId": campaign_id, "budget": budget}])

    async def list_all_campaigns(self, state_filter: str | None = None) -> JSONList:
        """获取所有Campaign（自动分页）"""
        all_campaigns = []
        next_token = None

        while True:
            result = await self.list_campaigns(
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
