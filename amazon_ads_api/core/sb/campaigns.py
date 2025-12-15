"""
Sponsored Brands - Campaigns API (异步版本)
SB广告系列管理
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


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
        
        SB API v4 使用 POST 请求到 /sb/v4/campaigns/list
        需要特殊的 Content-Type: application/vnd.sbcampaignresource.v4+json
        
        Args:
            state_filter: enabled, paused, archived
            name_filter: 名称过滤
            max_results: 最大结果数
            next_token: 分页token
        """
        body: JSONData = {"maxResults": min(max_results, 100)}
        
        if state_filter:
            body["stateFilter"] = {"include": [state_filter.upper()]}
        if name_filter:
            body["nameFilter"] = {"include": [name_filter]}
        if next_token:
            body["nextToken"] = next_token

        # SB v4 API 需要特殊的 Content-Type
        result = await self.post(
            "/sb/v4/campaigns/list", 
            json_data=body, 
            content_type="application/vnd.sbcampaignresource.v4+json"
        )
        
        if isinstance(result, dict):
            return result
        return {"campaigns": [], "totalResults": 0}

    async def get_campaign(self, campaign_id: str) -> JSONData:
        """获取单个SB Campaign详情"""
        result = await self.get(f"/sb/v4/campaigns/{campaign_id}")
        return result if isinstance(result, dict) else {}

    # SB v4 Content-Types
    SB_CAMPAIGN_V4_CONTENT_TYPE = "application/vnd.sbcampaignresource.v4+json"
    SB_AD_GROUP_V4_CONTENT_TYPE = "application/vnd.sbadgroupresource.v4+json"

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
        result = await self.post(
            "/sb/v4/campaigns", 
            json_data={"campaigns": campaigns},
            content_type=self.SB_CAMPAIGN_V4_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"campaigns": {"success": [], "error": []}}

    async def update_campaigns(self, campaigns: JSONList) -> JSONData:
        """
        批量更新SB Campaign
        
        Args:
            campaigns: [{"campaignId": "xxx", "state": "paused", "budget": 200.0}]
        """
        result = await self.put(
            "/sb/v4/campaigns", 
            json_data={"campaigns": campaigns},
            content_type=self.SB_CAMPAIGN_V4_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"campaigns": {"success": [], "error": []}}

    async def delete_campaign(self, campaign_id: str) -> JSONData:
        """归档SB Campaign"""
        return await self.delete(f"/sb/v4/campaigns/{campaign_id}")

    # ============ Ad Groups ============

    async def list_ad_groups(
        self,
        campaign_id: str | None = None,
        ad_group_ids: list[str] | None = None,
        state_filter: list[str] | str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取SB Ad Group列表
        
        Args:
            campaign_id: Campaign ID过滤
            ad_group_ids: Ad Group ID过滤
            state_filter: 状态过滤 ["ENABLED", "PAUSED", "ARCHIVED"]
            max_results: 最大结果数
            next_token: 分页token
        """
        params: JSONData = {"maxResults": max_results}
        
        # ID过滤 - 官方格式: {"include": [...]}
        if campaign_id:
            params["campaignIdFilter"] = {"include": [campaign_id]}
        if ad_group_ids:
            params["adGroupIdFilter"] = {"include": ad_group_ids}
        
        # 状态过滤
        if state_filter:
            states = [state_filter] if isinstance(state_filter, str) else state_filter
            params["stateFilter"] = {"include": [s.upper() for s in states]}
        
        if next_token:
            params["nextToken"] = next_token

        result = await self.post(
            "/sb/v4/adGroups/list", 
            json_data=params,
            content_type="application/vnd.sbadgroupresource.v4+json"
        )
        return result if isinstance(result, dict) else {"adGroups": []}

    async def get_ad_group(self, ad_group_id: str) -> JSONData:
        """获取单个SB Ad Group详情"""
        result = await self.get(f"/sb/v4/adGroups/{ad_group_id}")
        return result if isinstance(result, dict) else {}

    async def create_ad_groups(self, ad_groups: JSONList) -> JSONData:
        """批量创建SB Ad Group"""
        result = await self.post(
            "/sb/v4/adGroups", 
            json_data={"adGroups": ad_groups},
            content_type=self.SB_AD_GROUP_V4_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"adGroups": {"success": [], "error": []}}

    async def update_ad_groups(self, ad_groups: JSONList) -> JSONData:
        """批量更新SB Ad Group"""
        result = await self.put(
            "/sb/v4/adGroups", 
            json_data={"adGroups": ad_groups},
            content_type=self.SB_AD_GROUP_V4_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"adGroups": {"success": [], "error": []}}

    # ============ Ad Groups Delete (v4) ============

    async def delete_ad_groups(self, ad_group_ids: list[str]) -> JSONData:
        """
        批量归档SB Ad Group（官方 v4 /delete 端点）
        
        注意：Amazon Ads 不支持真正删除，此操作将 Ad Group 状态设置为 "archived"。
        官方请求格式: {"adGroupIdFilter": {"include": [...]}}
        """
        result = await self.post(
            "/sb/v4/adGroups/delete",
            json_data={"adGroupIdFilter": {"include": ad_group_ids}}
        )
        return result if isinstance(result, dict) else {"adGroups": {"success": [], "error": []}}

    async def delete_ad_group(self, ad_group_id: str) -> JSONData:
        """归档单个SB Ad Group"""
        return await self.delete_ad_groups([ad_group_id])

    # ============ Campaigns Delete (v4) ============

    async def delete_campaigns(self, campaign_ids: list[str]) -> JSONData:
        """
        批量归档SB Campaign（官方 v4 /delete 端点）
        
        注意：Amazon Ads 不支持真正删除，此操作将 Campaign 状态设置为 "archived"。
        官方请求格式: {"campaignIdFilter": {"include": [...]}}
        """
        result = await self.post(
            "/sb/v4/campaigns/delete",
            json_data={"campaignIdFilter": {"include": campaign_ids}}
        )
        return result if isinstance(result, dict) else {"campaigns": {"success": [], "error": []}}

    # ============ Budget Rules ============

    async def get_budget_rule(self, budget_rule_id: str) -> JSONData:
        """获取单个Budget Rule详情"""
        result = await self.get(f"/sb/budgetRules/{budget_rule_id}")
        return result if isinstance(result, dict) else {}

    async def get_budget_rule_campaigns(self, budget_rule_id: str) -> JSONData:
        """获取与Budget Rule关联的Campaign列表"""
        result = await self.get(f"/sb/budgetRules/{budget_rule_id}/campaigns")
        return result if isinstance(result, dict) else {"campaigns": []}

    async def list_campaign_budget_rules(self, campaign_id: str) -> JSONData:
        """获取Campaign关联的Budget Rule列表"""
        result = await self.get(f"/sb/campaigns/{campaign_id}/budgetRules")
        return result if isinstance(result, dict) else {"budgetRules": []}

    async def create_campaign_budget_rules(
        self, 
        campaign_id: str, 
        budget_rule_ids: list[str]
    ) -> JSONData:
        """将Budget Rule关联到Campaign"""
        result = await self.post(
            f"/sb/campaigns/{campaign_id}/budgetRules",
            json_data={"budgetRuleIds": budget_rule_ids}
        )
        return result if isinstance(result, dict) else {"success": [], "error": []}

    async def delete_campaign_budget_rule(
        self, 
        campaign_id: str, 
        budget_rule_id: str
    ) -> JSONData:
        """从Campaign移除Budget Rule关联"""
        return await self.delete(f"/sb/campaigns/{campaign_id}/budgetRules/{budget_rule_id}")

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

    # ============ Budget Recommendations ============

    async def get_budget_rules_recommendations(
        self, 
        campaign_id: str,
    ) -> JSONData:
        """
        获取 Campaign 的特殊事件预算规则推荐
        
        官方端点: POST /sb/campaigns/budgetRules/recommendations
        官方文档: SponsoredBrands_v3.yaml
        
        Args:
            campaign_id: Campaign ID
            
        Returns:
            包含推荐的特殊事件和建议预算增加
        """
        result = await self.post(
            "/sb/campaigns/budgetRules/recommendations",
            json_data={"campaignId": campaign_id}
        )
        return result if isinstance(result, dict) else {"recommendations": []}

    async def get_budget_recommendations(
        self, 
        campaign_ids: list[str]
    ) -> JSONData:
        """获取Campaign预算建议"""
        result = await self.post(
            "/sb/campaigns/budgetRecommendations",
            json_data={"campaignIds": campaign_ids}
        )
        return result if isinstance(result, dict) else {"recommendations": []}

    async def get_budget_usage(
        self, 
        campaign_ids: list[str],
        start_date: str,
        end_date: str
    ) -> JSONData:
        """获取Campaign预算使用情况"""
        result = await self.post(
            "/sb/campaigns/budget/usage",
            json_data={
                "campaignIds": campaign_ids,
                "startDate": start_date,
                "endDate": end_date
            }
        )
        return result if isinstance(result, dict) else {"budgetUsage": []}

    # ============ Campaign Insights ============

    async def get_campaigns_insights(self, request: JSONData) -> JSONData:
        """批量获取Campaign洞察数据"""
        result = await self.post("/sb/campaigns/insights", json_data=request)
        return result if isinstance(result, dict) else {"insights": []}

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
