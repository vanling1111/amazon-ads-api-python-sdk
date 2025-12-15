"""
Sponsored Display - Campaigns API (异步版本)
SD广告系列管理
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SDCampaignsAPI(BaseAdsClient):
    """SD Campaigns API (全异步)"""

    # ============ Campaigns ============

    async def list_campaigns(
        self,
        state_filter: str | None = None,
        name_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取SD Campaign列表
        
        SD API 使用 GET 请求，与 SP 不同
        
        Args:
            state_filter: enabled, paused, archived
            name_filter: 名称过滤
            max_results: 最大结果数
        """
        params: JSONData = {}
        if state_filter:
            params["stateFilter"] = state_filter.upper()
        if max_results:
            params["count"] = max_results
        if next_token:
            params["startIndex"] = next_token

        result = await self.get("/sd/campaigns", params=params)
        
        # SD API 直接返回数组，不是对象
        if isinstance(result, list):
            return {"campaigns": result, "totalResults": len(result)}
        return result if isinstance(result, dict) else {"campaigns": []}

    async def get_campaign(self, campaign_id: str) -> JSONData:
        """获取单个SD Campaign详情"""
        result = await self.get(f"/sd/campaigns/{campaign_id}")
        return result if isinstance(result, dict) else {}

    async def create_campaigns(self, campaigns: JSONList) -> JSONData:
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
        result = await self.post("/sd/campaigns", json_data=campaigns)
        return result if isinstance(result, dict) else {"campaigns": {"success": [], "error": []}}

    async def update_campaigns(self, campaigns: JSONList) -> JSONData:
        """批量更新SD Campaign"""
        result = await self.put("/sd/campaigns", json_data=campaigns)
        return result if isinstance(result, dict) else {"campaigns": {"success": [], "error": []}}

    async def delete_campaign(self, campaign_id: str) -> JSONData:
        """归档SD Campaign"""
        return await self.delete(f"/sd/campaigns/{campaign_id}")

    async def get_campaign_extended(self, campaign_id: str) -> JSONData:
        """获取Campaign扩展信息（包含更多指标）"""
        result = await self.get(f"/sd/campaigns/extended/{campaign_id}")
        return result if isinstance(result, dict) else {}

    async def list_campaigns_extended(
        self,
        state_filter: str | None = None,
        max_results: int = 100,
    ) -> JSONList:
        """获取所有Campaign扩展信息"""
        params: JSONData = {}
        if state_filter:
            params["stateFilter"] = state_filter
        if max_results:
            params["count"] = max_results

        result = await self.get("/sd/campaigns/extended", params=params or None)
        return result if isinstance(result, list) else []

    # ============ Budget Rules ============

    async def list_budget_rules(self) -> JSONData:
        """获取Budget Rule列表"""
        result = await self.get("/sd/budgetRules")
        return result if isinstance(result, dict) else {"budgetRules": []}

    async def get_budget_rule(self, budget_rule_id: str) -> JSONData:
        """获取单个Budget Rule详情"""
        result = await self.get(f"/sd/budgetRules/{budget_rule_id}")
        return result if isinstance(result, dict) else {}

    async def get_budget_rule_campaigns(self, budget_rule_id: str) -> JSONData:
        """获取与Budget Rule关联的Campaign列表"""
        result = await self.get(f"/sd/budgetRules/{budget_rule_id}/campaigns")
        return result if isinstance(result, dict) else {"campaigns": []}

    async def list_campaign_budget_rules(self, campaign_id: str) -> JSONData:
        """获取Campaign关联的Budget Rule列表"""
        result = await self.get(f"/sd/campaigns/{campaign_id}/budgetRules")
        return result if isinstance(result, dict) else {"budgetRules": []}

    async def create_budget_rules(self, rules: JSONList) -> JSONData:
        """批量创建Budget Rule"""
        result = await self.post("/sd/budgetRules", json_data={"budgetRules": rules})
        return result if isinstance(result, dict) else {"budgetRules": {"success": [], "error": []}}

    async def update_budget_rules(self, rules: JSONList) -> JSONData:
        """批量更新Budget Rule"""
        result = await self.put("/sd/budgetRules", json_data={"budgetRules": rules})
        return result if isinstance(result, dict) else {"budgetRules": {"success": [], "error": []}}

    async def create_campaign_budget_rules(
        self, 
        campaign_id: str, 
        budget_rule_ids: list[str]
    ) -> JSONData:
        """将Budget Rule关联到Campaign"""
        result = await self.post(
            f"/sd/campaigns/{campaign_id}/budgetRules",
            json_data={"budgetRuleIds": budget_rule_ids}
        )
        return result if isinstance(result, dict) else {"success": [], "error": []}

    async def delete_campaign_budget_rule(
        self, 
        campaign_id: str, 
        budget_rule_id: str
    ) -> JSONData:
        """从Campaign移除Budget Rule关联"""
        return await self.delete(f"/sd/campaigns/{campaign_id}/budgetRules/{budget_rule_id}")

    async def get_budget_recommendations(
        self, 
        campaign_ids: list[str]
    ) -> JSONData:
        """获取Campaign预算建议"""
        result = await self.post(
            "/sd/campaigns/budgetRecommendations",
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
            "/sd/campaigns/budget/usage",
            json_data={
                "campaignIds": campaign_ids,
                "startDate": start_date,
                "endDate": end_date
            }
        )
        return result if isinstance(result, dict) else {"budgetUsage": []}

    # ============ Ad Groups ============

    async def list_ad_groups(
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

        result = await self.post("/sd/adGroups/list", json_data=params)
        return result if isinstance(result, dict) else {"adGroups": []}

    async def get_ad_groups(
        self,
        campaign_id: str | None = None,
        state_filter: str | None = None,
        start_index: int = 0,
        count: int = 100,
    ) -> JSONList:
        """获取SD Ad Group列表（v2 GET 方式）"""
        params: JSONData = {"startIndex": start_index, "count": count}
        if campaign_id:
            params["campaignIdFilter"] = campaign_id
        if state_filter:
            params["stateFilter"] = state_filter

        result = await self.get("/sd/adGroups", params=params)
        return result if isinstance(result, list) else []

    async def get_ad_group(self, ad_group_id: str) -> JSONData:
        """获取单个SD Ad Group详情"""
        result = await self.get(f"/sd/adGroups/{ad_group_id}")
        return result if isinstance(result, dict) else {}

    async def get_ad_groups_extended(
        self,
        campaign_id: str | None = None,
        state_filter: str | None = None,
        start_index: int = 0,
        count: int = 100,
    ) -> JSONList:
        """获取Ad Group扩展信息列表"""
        params: JSONData = {"startIndex": start_index, "count": count}
        if campaign_id:
            params["campaignIdFilter"] = campaign_id
        if state_filter:
            params["stateFilter"] = state_filter

        result = await self.get("/sd/adGroups/extended", params=params)
        return result if isinstance(result, list) else []

    async def get_ad_group_extended(self, ad_group_id: str) -> JSONData:
        """获取单个Ad Group扩展信息"""
        result = await self.get(f"/sd/adGroups/extended/{ad_group_id}")
        return result if isinstance(result, dict) else {}

    async def create_ad_groups(self, ad_groups: JSONList) -> JSONData:
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
        result = await self.post("/sd/adGroups", json_data=ad_groups)
        return result if isinstance(result, dict) else {"adGroups": {"success": [], "error": []}}

    async def update_ad_groups(self, ad_groups: JSONList) -> JSONData:
        """批量更新SD Ad Group"""
        result = await self.put("/sd/adGroups", json_data=ad_groups)
        return result if isinstance(result, dict) else {"adGroups": {"success": [], "error": []}}

    async def delete_ad_group(self, ad_group_id: str) -> JSONData:
        """归档SD Ad Group"""
        return await self.delete(f"/sd/adGroups/{ad_group_id}")

    # ============ Product Ads ============

    async def get_product_ads(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        state_filter: str | None = None,
        start_index: int = 0,
        count: int = 100,
    ) -> JSONList:
        """获取SD Product Ad列表（v2 GET 方式）"""
        params: JSONData = {"startIndex": start_index, "count": count}
        if ad_group_id:
            params["adGroupIdFilter"] = ad_group_id
        if campaign_id:
            params["campaignIdFilter"] = campaign_id
        if state_filter:
            params["stateFilter"] = state_filter

        result = await self.get("/sd/productAds", params=params)
        return result if isinstance(result, list) else []

    async def get_product_ad(self, ad_id: str) -> JSONData:
        """获取单个Product Ad详情"""
        result = await self.get(f"/sd/productAds/{ad_id}")
        return result if isinstance(result, dict) else {}

    async def get_product_ads_extended(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        start_index: int = 0,
        count: int = 100,
    ) -> JSONList:
        """获取Product Ad扩展信息列表"""
        params: JSONData = {"startIndex": start_index, "count": count}
        if ad_group_id:
            params["adGroupIdFilter"] = ad_group_id
        if campaign_id:
            params["campaignIdFilter"] = campaign_id

        result = await self.get("/sd/productAds/extended", params=params)
        return result if isinstance(result, list) else []

    async def get_product_ad_extended(self, ad_id: str) -> JSONData:
        """获取单个Product Ad扩展信息"""
        result = await self.get(f"/sd/productAds/extended/{ad_id}")
        return result if isinstance(result, dict) else {}

    async def list_product_ads(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        state_filter: str | None = None,
        max_results: int = 100,
    ) -> JSONData:
        """获取SD Product Ad列表（POST list 方式）"""
        params: JSONData = {"maxResults": max_results}
        if ad_group_id:
            params["adGroupIdFilter"] = [ad_group_id]
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]
        if state_filter:
            params["stateFilter"] = state_filter

        result = await self.post("/sd/productAds/list", json_data=params)
        return result if isinstance(result, dict) else {"productAds": []}

    async def create_product_ads(self, product_ads: JSONList) -> JSONData:
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
        result = await self.post("/sd/productAds", json_data=product_ads)
        return result if isinstance(result, dict) else {"productAds": {"success": [], "error": []}}

    async def update_product_ads(self, product_ads: JSONList) -> JSONData:
        """批量更新SD Product Ad"""
        result = await self.put("/sd/productAds", json_data=product_ads)
        return result if isinstance(result, dict) else {"productAds": {"success": [], "error": []}}

    async def delete_product_ad(self, ad_id: str) -> JSONData:
        """归档SD Product Ad"""
        return await self.delete(f"/sd/productAds/{ad_id}")

    # ============ Forecasts ============

    async def get_campaign_forecast(
        self,
        tactic: str,
        targeting: list[dict],
        daily_budget: float,
    ) -> JSONData:
        """
        获取Campaign预测
        
        预测给定设置下的Impressions、Clicks等
        """
        result = await self.post("/sd/forecasts", json_data={
            "tactic": tactic,
            "targeting": targeting,
            "dailyBudget": daily_budget,
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

    async def create_audience_campaign(
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
        return await self.create_campaigns(campaigns)

    async def create_contextual_campaign(
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
        return await self.create_campaigns(campaigns)
