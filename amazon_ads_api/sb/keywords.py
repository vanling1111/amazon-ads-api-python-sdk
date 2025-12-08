"""
Sponsored Brands - Keywords API (异步版本)
SB关键词管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SBKeywordsAPI(BaseAdsClient):
    """SB Keywords API (全异步)"""

    # ============ Keywords ============

    async def list_keywords(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        state_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取SB Keyword列表"""
        params: JSONData = {"maxResults": max_results}
        if ad_group_id:
            params["adGroupIdFilter"] = [ad_group_id]
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]
        if state_filter:
            params["stateFilter"] = state_filter
        if next_token:
            params["nextToken"] = next_token

        result = await self.post("/sb/keywords/list", json_data=params)
        return result if isinstance(result, dict) else {"keywords": []}

    async def get_keyword(self, keyword_id: str) -> JSONData:
        """获取单个Keyword详情"""
        result = await self.get(f"/sb/keywords/{keyword_id}")
        return result if isinstance(result, dict) else {}

    async def create_keywords(self, keywords: JSONList) -> JSONData:
        """
        批量创建SB Keyword
        
        Args:
            keywords: [
                {
                    "campaignId": "xxx",
                    "adGroupId": "xxx",
                    "state": "enabled",
                    "keywordText": "running shoes",
                    "matchType": "BROAD",  # BROAD | PHRASE | EXACT
                    "bid": 1.0
                }
            ]
        """
        result = await self.post("/sb/keywords", json_data=keywords)
        return result if isinstance(result, dict) else {"keywords": {"success": [], "error": []}}

    async def update_keywords(self, keywords: JSONList) -> JSONData:
        """批量更新SB Keyword"""
        result = await self.put("/sb/keywords", json_data=keywords)
        return result if isinstance(result, dict) else {"keywords": {"success": [], "error": []}}

    async def delete_keyword(self, keyword_id: str) -> JSONData:
        """归档Keyword"""
        return await self.delete(f"/sb/keywords/{keyword_id}")

    # ============ Negative Keywords ============

    async def list_negative_keywords(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        max_results: int = 100,
    ) -> JSONData:
        """获取SB Negative Keyword列表"""
        params: JSONData = {"maxResults": max_results}
        if ad_group_id:
            params["adGroupIdFilter"] = [ad_group_id]
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]

        result = await self.post("/sb/negativeKeywords/list", json_data=params)
        return result if isinstance(result, dict) else {"negativeKeywords": []}

    async def create_negative_keywords(self, keywords: JSONList) -> JSONData:
        """批量创建SB Negative Keyword"""
        result = await self.post("/sb/negativeKeywords", json_data=keywords)
        return result if isinstance(result, dict) else {"negativeKeywords": {"success": [], "error": []}}

    async def delete_negative_keyword(self, keyword_id: str) -> JSONData:
        """删除Negative Keyword"""
        return await self.delete(f"/sb/negativeKeywords/{keyword_id}")

    # ============ Product Targeting ============

    async def list_targets(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        state_filter: str | None = None,
        max_results: int = 100,
    ) -> JSONData:
        """获取SB Target列表"""
        params: JSONData = {"maxResults": max_results}
        if ad_group_id:
            params["adGroupIdFilter"] = [ad_group_id]
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]
        if state_filter:
            params["stateFilter"] = state_filter

        result = await self.post("/sb/targets/list", json_data=params)
        return result if isinstance(result, dict) else {"targets": []}

    async def create_targets(self, targets: JSONList) -> JSONData:
        """
        批量创建SB Target
        
        Args:
            targets: [
                {
                    "campaignId": "xxx",
                    "adGroupId": "xxx",
                    "state": "enabled",
                    "expressions": [
                        {"type": "asinSameAs", "value": "B00XXXX"}
                    ],
                    "bid": 1.0
                }
            ]
        """
        result = await self.post("/sb/targets", json_data=targets)
        return result if isinstance(result, dict) else {"targets": {"success": [], "error": []}}

    async def update_targets(self, targets: JSONList) -> JSONData:
        """批量更新SB Target"""
        result = await self.put("/sb/targets", json_data=targets)
        return result if isinstance(result, dict) else {"targets": {"success": [], "error": []}}

    async def delete_target(self, target_id: str) -> JSONData:
        """归档Target"""
        return await self.delete(f"/sb/targets/{target_id}")

    # ============ Negative Targets ============

    async def list_negative_targets(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        max_results: int = 100,
    ) -> JSONData:
        """获取SB Negative Target列表"""
        params: JSONData = {"maxResults": max_results}
        if ad_group_id:
            params["adGroupIdFilter"] = [ad_group_id]
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]

        result = await self.post("/sb/negativeTargets/list", json_data=params)
        return result if isinstance(result, dict) else {"negativeTargets": []}

    async def create_negative_targets(self, targets: JSONList) -> JSONData:
        """批量创建SB Negative Target"""
        result = await self.post("/sb/negativeTargets", json_data=targets)
        return result if isinstance(result, dict) else {"negativeTargets": {"success": [], "error": []}}

    # ============ Recommendations ============

    async def get_keyword_recommendations(
        self,
        ad_group_id: str | None = None,
        asins: list[str] | None = None,
        max_recommendations: int = 100,
    ) -> JSONData:
        """获取关键词建议"""
        body: JSONData = {"maxRecommendations": max_recommendations}
        if ad_group_id:
            body["adGroupId"] = ad_group_id
        if asins:
            body["asins"] = asins

        result = await self.post("/sb/recommendations/keyword", json_data=body)
        return result if isinstance(result, dict) else {"recommendations": []}

    async def get_targeting_recommendations(
        self,
        ad_group_id: str | None = None,
        asins: list[str] | None = None,
        max_recommendations: int = 100,
    ) -> JSONData:
        """获取定向建议"""
        body: JSONData = {"maxRecommendations": max_recommendations}
        if ad_group_id:
            body["adGroupId"] = ad_group_id
        if asins:
            body["asins"] = asins

        result = await self.post("/sb/recommendations/targets", json_data=body)
        return result if isinstance(result, dict) else {"recommendations": []}

    async def get_bid_recommendations(
        self,
        ad_group_id: str,
        keywords: list[dict] | None = None,
        targets: list[dict] | None = None,
    ) -> JSONData:
        """获取竞价建议"""
        body: JSONData = {"adGroupId": ad_group_id}
        if keywords:
            body["keywords"] = keywords
        if targets:
            body["targets"] = targets

        result = await self.post("/sb/recommendations/bids", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ Category Targeting ============

    async def get_targeting_categories(
        self,
        asins: list[str] | None = None,
    ) -> JSONData:
        """
        获取可用的定向品类
        
        SB支持按品类定向
        """
        body: JSONData = {}
        if asins:
            body["asins"] = asins

        result = await self.post("/sb/targets/categories", json_data=body)
        return result if isinstance(result, dict) else {"categories": []}

    # ============ 便捷方法 ============

    async def pause_keyword(self, keyword_id: str) -> JSONData:
        """暂停Keyword"""
        return await self.update_keywords([{"keywordId": keyword_id, "state": "paused"}])

    async def update_bid(self, keyword_id: str, bid: float) -> JSONData:
        """更新Keyword竞价"""
        return await self.update_keywords([{"keywordId": keyword_id, "bid": bid}])

    async def list_all_keywords(
        self,
        campaign_id: str | None = None,
        state_filter: str | None = None,
    ) -> JSONList:
        """获取所有Keyword（自动分页）"""
        all_keywords = []
        next_token = None

        while True:
            result = await self.list_keywords(
                campaign_id=campaign_id,
                state_filter=state_filter,
                max_results=100,
                next_token=next_token,
            )
            keywords = result.get("keywords", [])
            all_keywords.extend(keywords)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_keywords
