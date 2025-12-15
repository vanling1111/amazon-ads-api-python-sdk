"""
Sponsored Display - Targeting API (异步版本)
SD定向管理（受众定向 + 上下文定向）
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SDTargetingAPI(BaseAdsClient):
    """SD Targeting API (全异步)"""

    # ============ Targets ============

    async def list_targets(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        state_filter: str | None = None,
        start_index: int = 0,
        count: int = 100,
    ) -> JSONList:
        """获取SD Target列表 (v2 API - 使用 GET)"""
        params: JSONData = {"startIndex": start_index, "count": count}
        if ad_group_id:
            params["adGroupIdFilter"] = ad_group_id
        if campaign_id:
            params["campaignIdFilter"] = campaign_id
        if state_filter:
            params["stateFilter"] = state_filter

        result = await self.get("/sd/targets", params=params)
        return result if isinstance(result, list) else []

    async def get_target(self, target_id: str) -> JSONData:
        """获取单个Target详情"""
        result = await self.get(f"/sd/targets/{target_id}")
        return result if isinstance(result, dict) else {}

    async def create_targets(self, targets: JSONList) -> JSONData:
        """
        批量创建SD Target
        
        受众定向示例:
        {
            "adGroupId": "xxx",
            "state": "enabled",
            "expression": [
                {"type": "audienceCategory", "value": "in-market"}
            ],
            "bid": 1.0
        }
        
        上下文定向示例:
        {
            "adGroupId": "xxx",
            "state": "enabled",
            "expression": [
                {"type": "asinSameAs", "value": "B00XXXX"}
            ],
            "bid": 1.0
        }
        """
        result = await self.post("/sd/targets", json_data=targets)
        return result if isinstance(result, dict) else {"targets": {"success": [], "error": []}}

    async def update_targets(self, targets: JSONList) -> JSONData:
        """批量更新SD Target"""
        result = await self.put("/sd/targets", json_data=targets)
        return result if isinstance(result, dict) else {"targets": {"success": [], "error": []}}

    async def delete_target(self, target_id: str) -> JSONData:
        """归档Target"""
        return await self.delete(f"/sd/targets/{target_id}")

    # ============ Negative Targets ============

    async def list_negative_targets(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        start_index: int = 0,
        count: int = 100,
    ) -> JSONList:
        """获取SD Negative Target列表 (v2 API - 使用 GET)"""
        params: JSONData = {"startIndex": start_index, "count": count}
        if ad_group_id:
            params["adGroupIdFilter"] = ad_group_id
        if campaign_id:
            params["campaignIdFilter"] = campaign_id

        result = await self.get("/sd/negativeTargets", params=params)
        return result if isinstance(result, list) else []

    async def create_negative_targets(self, targets: JSONList) -> JSONData:
        """批量创建SD Negative Target"""
        result = await self.post("/sd/negativeTargets", json_data=targets)
        return result if isinstance(result, dict) else {"negativeTargets": {"success": [], "error": []}}

    async def get_negative_target(self, target_id: str) -> JSONData:
        """获取单个Negative Target详情"""
        result = await self.get(f"/sd/negativeTargets/{target_id}")
        return result if isinstance(result, dict) else {}

    async def update_negative_targets(self, targets: JSONList) -> JSONData:
        """批量更新Negative Target"""
        result = await self.put("/sd/negativeTargets", json_data=targets)
        return result if isinstance(result, dict) else {"negativeTargets": {"success": [], "error": []}}

    async def delete_negative_target(self, target_id: str) -> JSONData:
        """删除Negative Target"""
        return await self.delete(f"/sd/negativeTargets/{target_id}")

    # ============ Extended Data ============

    async def list_targets_extended(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        start_index: int = 0,
        count: int = 100,
    ) -> JSONList:
        """获取Target扩展信息（包含更多指标）"""
        params: JSONData = {"startIndex": start_index, "count": count}
        if ad_group_id:
            params["adGroupIdFilter"] = ad_group_id
        if campaign_id:
            params["campaignIdFilter"] = campaign_id

        result = await self.get("/sd/targets/extended", params=params)
        return result if isinstance(result, list) else []

    async def get_target_extended(self, target_id: str) -> JSONData:
        """获取单个Target扩展信息"""
        result = await self.get(f"/sd/targets/extended/{target_id}")
        return result if isinstance(result, dict) else {}

    async def list_negative_targets_extended(
        self,
        ad_group_id: str | None = None,
        start_index: int = 0,
        count: int = 100,
    ) -> JSONList:
        """获取Negative Target扩展信息"""
        params: JSONData = {"startIndex": start_index, "count": count}
        if ad_group_id:
            params["adGroupIdFilter"] = ad_group_id

        result = await self.get("/sd/negativeTargets/extended", params=params)
        return result if isinstance(result, list) else []

    async def get_negative_target_extended(self, target_id: str) -> JSONData:
        """获取单个Negative Target扩展信息"""
        result = await self.get(f"/sd/negativeTargets/extended/{target_id}")
        return result if isinstance(result, dict) else {}

    # ============ Targeting Recommendations ============

    async def get_targeting_recommendations(
        self,
        ad_group_id: str | None = None,
        asins: list[str] | None = None,
        tactic: str | None = None,
        max_recommendations: int = 100,
    ) -> JSONData:
        """
        获取定向建议
        
        Args:
            ad_group_id: 广告组ID
            asins: 基于这些ASIN推荐
            tactic: T00020 | T00030 | T00001
        """
        body: JSONData = {"maxRecommendations": max_recommendations}
        if ad_group_id:
            body["adGroupId"] = ad_group_id
        if asins:
            body["asins"] = asins
        if tactic:
            body["tactic"] = tactic

        result = await self.post("/sd/targets/recommendations", json_data=body)
        return result if isinstance(result, dict) else {"recommendations": []}

    async def get_bid_recommendations(
        self,
        ad_group_id: str,
        targets: list[dict],
    ) -> JSONData:
        """获取竞价建议"""
        result = await self.post("/sd/targets/bid/recommendations", json_data={
            "adGroupId": ad_group_id,
            "targets": targets,
        })
        return result if isinstance(result, dict) else {}

    # ============ Audiences ============

    async def list_audiences(self) -> JSONList:
        """
        获取可用的受众列表
        
        包括In-Market、Lifestyle等受众类型
        """
        result = await self.get("/sd/audiences")
        return result if isinstance(result, list) else []

    async def get_audience_categories(self) -> JSONData:
        """
        获取受众类别树
        
        用于受众定向选择
        """
        result = await self.get("/sd/audiences/categories")
        return result if isinstance(result, dict) else {"categories": []}

    # ============ Brand Safety ============

    async def get_brand_safety_list(self, ad_group_id: str) -> JSONData:
        """
        获取品牌安全列表
        
        排除不想展示广告的位置
        """
        result = await self.get(f"/sd/adGroups/{ad_group_id}/brandSafetyList")
        return result if isinstance(result, dict) else {}

    async def update_brand_safety_list(
        self,
        ad_group_id: str,
        domains: list[str] | None = None,
        apps: list[str] | None = None,
    ) -> JSONData:
        """
        更新品牌安全列表
        
        Args:
            domains: 要排除的网站域名
            apps: 要排除的App
        """
        body: JSONData = {}
        if domains:
            body["domains"] = domains
        if apps:
            body["apps"] = apps

        result = await self.put(f"/sd/adGroups/{ad_group_id}/brandSafetyList", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def update_bid(self, target_id: str, bid: float) -> JSONData:
        """更新Target竞价"""
        return await self.update_targets([{"targetId": target_id, "bid": bid}])

    async def batch_update_bids(self, bid_updates: list[dict]) -> JSONData:
        """批量更新竞价"""
        return await self.update_targets(bid_updates)

    async def create_audience_target(
        self,
        ad_group_id: str,
        audience_type: str,
        audience_value: str,
        bid: float,
    ) -> JSONData:
        """
        创建受众定向
        
        Args:
            audience_type: audienceCategory, lifestyle, inMarket等
            audience_value: 具体值
        """
        targets = [{
            "adGroupId": ad_group_id,
            "state": "enabled",
            "expression": [{"type": audience_type, "value": audience_value}],
            "bid": bid,
        }]
        return await self.create_targets(targets)

    async def create_asin_target(
        self,
        ad_group_id: str,
        asin: str,
        bid: float,
    ) -> JSONData:
        """创建ASIN定向"""
        targets = [{
            "adGroupId": ad_group_id,
            "state": "enabled",
            "expression": [{"type": "asinSameAs", "value": asin}],
            "bid": bid,
        }]
        return await self.create_targets(targets)

    async def create_category_target(
        self,
        ad_group_id: str,
        category_id: str,
        bid: float,
    ) -> JSONData:
        """创建品类定向"""
        targets = [{
            "adGroupId": ad_group_id,
            "state": "enabled",
            "expression": [{"type": "asinCategorySameAs", "value": category_id}],
            "bid": bid,
        }]
        return await self.create_targets(targets)
