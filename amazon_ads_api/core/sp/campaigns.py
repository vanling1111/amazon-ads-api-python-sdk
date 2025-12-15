"""
Sponsored Products - Campaigns API (异步版本)
SP广告系列管理
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

# API v3 Content-Type
CONTENT_TYPE_CAMPAIGN = "application/vnd.spCampaign.v3+json"


class SPCampaignsAPI(BaseAdsClient):
    """SP Campaigns API (全异步)"""

    async def list_campaigns(
        self,
        state_filter: list[str] | str | None = None,
        name_filter: str | None = None,
        campaign_ids: list[str] | None = None,
        portfolio_ids: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
        include_extended_data: bool = False,
    ) -> JSONData:
        """
        获取Campaign列表
        
        Args:
            state_filter: 状态过滤 ["ENABLED", "PAUSED", "ARCHIVED"]
            name_filter: 名称过滤（模糊匹配）
            campaign_ids: Campaign ID过滤
            portfolio_ids: Portfolio ID过滤
            max_results: 最大结果数(1-100)
            next_token: 分页token
            include_extended_data: 是否包含扩展字段
            
        Returns:
            {"campaigns": [...], "nextToken": "..."}
        """
        params: JSONData = {"maxResults": max_results}
        
        # 状态过滤 - 官方格式: {"include": [...]}
        if state_filter:
            states = [state_filter] if isinstance(state_filter, str) else state_filter
            params["stateFilter"] = {"include": [s.upper() for s in states]}
        
        # 名称过滤 - 官方格式: {"queryTermMatchType": "BROAD_MATCH", "include": [...]}
        if name_filter:
            params["nameFilter"] = {
                "queryTermMatchType": "BROAD_MATCH",
                "include": [name_filter]
            }
        
        # Campaign ID过滤
        if campaign_ids:
            params["campaignIdFilter"] = {"include": campaign_ids}
        
        # Portfolio ID过滤
        if portfolio_ids:
            params["portfolioIdFilter"] = {"include": portfolio_ids}
        
        if next_token:
            params["nextToken"] = next_token
        
        if include_extended_data:
            params["includeExtendedDataFields"] = True

        result = await self.post("/sp/campaigns/list", json_data=params, content_type=CONTENT_TYPE_CAMPAIGN)
        return result if isinstance(result, dict) else {"campaigns": []}

    async def get_campaign(self, campaign_id: str) -> JSONData:
        """获取单个Campaign详情"""
        result = await self.get(f"/sp/campaigns/{campaign_id}", content_type=CONTENT_TYPE_CAMPAIGN)
        return result if isinstance(result, dict) else {}

    async def create_campaigns(self, campaigns: JSONList) -> JSONData:
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
        result = await self.post("/sp/campaigns", json_data={"campaigns": campaigns}, content_type=CONTENT_TYPE_CAMPAIGN)
        return result if isinstance(result, dict) else {"campaigns": {"success": [], "error": []}}

    async def update_campaigns(self, campaigns: JSONList) -> JSONData:
        """
        批量更新Campaign
        
        Args:
            campaigns: 包含campaignId的更新数据
            [{"campaignId": "xxx", "state": "paused", "dailyBudget": 20.0}]
        """
        result = await self.put("/sp/campaigns", json_data={"campaigns": campaigns}, content_type=CONTENT_TYPE_CAMPAIGN)
        return result if isinstance(result, dict) else {"campaigns": {"success": [], "error": []}}

    async def delete_campaigns(self, campaign_ids: list[str]) -> JSONData:
        """
        批量归档Campaign（官方 v3 /delete 端点）
        
        注意：Amazon Ads 不支持真正删除广告实体，此操作将 Campaign 状态设置为 "archived"。
        归档后的 Campaign 仍可在报告中查询，但无法恢复为 enabled/paused。
        
        官方请求格式: {"campaignIdFilter": {"include": [...]}}
        
        Args:
            campaign_ids: Campaign ID列表
            
        Returns:
            {"campaigns": {"success": [...], "error": [...]}}
        """
        body = {"campaignIdFilter": {"include": campaign_ids}}
        result = await self.post("/sp/campaigns/delete", json_data=body, content_type=CONTENT_TYPE_CAMPAIGN)
        return result if isinstance(result, dict) else {"campaigns": {"success": [], "error": []}}

    async def delete_campaign(self, campaign_id: str) -> JSONData:
        """归档单个Campaign（状态变为 archived）"""
        return await self.delete_campaigns([campaign_id])
    
    # archive_campaign 是 delete_campaign 的别名
    async def archive_campaign(self, campaign_id: str) -> JSONData:
        """归档Campaign（等同于 delete_campaign）"""
        return await self.delete_campaign(campaign_id)

    # ============ 便捷方法 ============

    async def pause_campaign(self, campaign_id: str) -> JSONData:
        """暂停Campaign"""
        return await self.update_campaigns([{"campaignId": campaign_id, "state": "paused"}])

    async def enable_campaign(self, campaign_id: str) -> JSONData:
        """启用Campaign"""
        return await self.update_campaigns([{"campaignId": campaign_id, "state": "enabled"}])

    async def update_budget(self, campaign_id: str, daily_budget: float) -> JSONData:
        """更新Campaign日预算"""
        return await self.update_campaigns([{
            "campaignId": campaign_id,
            "dailyBudget": daily_budget
        }])

    async def update_bidding_strategy(self, campaign_id: str, strategy: str) -> JSONData:
        """
        更新竞价策略
        
        Args:
            strategy: LEGACY_FOR_SALES | AUTO_FOR_SALES | MANUAL
        """
        return await self.update_campaigns([{
            "campaignId": campaign_id,
            "bidding": {"strategy": strategy}
        }])

    # ============ 批量获取所有Campaign ============

    async def list_all_campaigns(
        self,
        state_filter: str | None = None,
    ) -> JSONList:
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

    async def get_campaigns_batch(self, campaign_ids: list[str]) -> JSONList:
        """
        并行批量获取Campaign详情
        
        Args:
            campaign_ids: Campaign ID列表
            
        Returns:
            Campaign详情列表
        """
        tasks = [self.get_campaign(cid) for cid in campaign_ids]
        results = await self.parallel_execute(tasks, max_concurrent=10)
        return [r for r in results if r and not isinstance(r, Exception)]

    async def list_campaigns_summary(self, state_filter: str | None = None) -> JSONData:
        """
        获取Campaign汇总统计（快速）
        
        Returns:
            {
                "total": 100,
                "enabled": 50,
                "paused": 30,
                "archived": 20,
                "total_budget": 5000.0
            }
        """
        campaigns = await self.list_all_campaigns(state_filter=state_filter)
        
        summary = {
            "total": len(campaigns),
            "enabled": 0,
            "paused": 0,
            "archived": 0,
            "total_budget": 0.0,
        }
        
        for c in campaigns:
            state = c.get("state", "").lower()
            if state in summary:
                summary[state] += 1
            
            budget = c.get("budget", {})
            if isinstance(budget, dict):
                summary["total_budget"] += budget.get("budget", 0) or 0
            elif isinstance(budget, (int, float)):
                summary["total_budget"] += budget
        
        return summary

    # ============ Campaign Recommendations ============

    async def get_campaign_recommendations(
        self,
        campaign_ids: list[str] | None = None,
        max_results: int = 100,
    ) -> JSONData:
        """
        获取Campaign推荐
        
        官方端点: GET /sp/campaign/recommendations
        
        返回Campaign级别的优化建议。
        """
        params: JSONData = {"maxResults": max_results}
        if campaign_ids:
            params["campaignIdFilter"] = ",".join(campaign_ids)

        result = await self.get("/sp/campaign/recommendations", params=params)
        return result if isinstance(result, dict) else {"recommendations": []}

    async def list_campaign_recommendations(
        self,
        campaign_ids: list[str] | None = None,
        recommendation_types: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取Campaign推荐列表（POST版本）
        
        官方端点: POST /sp/campaign/recommendations
        
        Args:
            campaign_ids: Campaign ID过滤
            recommendation_types: 推荐类型过滤
            max_results: 最大结果数
            next_token: 分页Token
        """
        body: JSONData = {"maxResults": max_results}
        if campaign_ids:
            body["campaignIdFilter"] = campaign_ids
        if recommendation_types:
            body["recommendationTypeFilter"] = recommendation_types
        if next_token:
            body["nextToken"] = next_token

        result = await self.post("/sp/campaign/recommendations", json_data=body)
        return result if isinstance(result, dict) else {"recommendations": []}
