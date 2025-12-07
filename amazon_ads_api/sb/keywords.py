"""
Sponsored Brands - Keywords API
SB关键词管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SBKeywordsAPI(BaseAdsClient):
    """SB Keywords API"""

    # ============ Keywords ============

    def list_keywords(
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

        result = self.post("/sb/keywords/list", json_data=params)
        return result if isinstance(result, dict) else {"keywords": []}

    def get_keyword(self, keyword_id: str) -> JSONData:
        """获取单个Keyword详情"""
        result = self.get(f"/sb/keywords/{keyword_id}")
        return result if isinstance(result, dict) else {}

    def create_keywords(self, keywords: JSONList) -> JSONData:
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
        result = self.post("/sb/keywords", json_data=keywords)
        return result if isinstance(result, dict) else {"keywords": {"success": [], "error": []}}

    def update_keywords(self, keywords: JSONList) -> JSONData:
        """批量更新SB Keyword"""
        result = self.put("/sb/keywords", json_data=keywords)
        return result if isinstance(result, dict) else {"keywords": {"success": [], "error": []}}

    def delete_keyword(self, keyword_id: str) -> JSONData:
        """归档Keyword"""
        return self.delete(f"/sb/keywords/{keyword_id}")

    # ============ Negative Keywords ============

    def list_negative_keywords(
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

        result = self.post("/sb/negativeKeywords/list", json_data=params)
        return result if isinstance(result, dict) else {"negativeKeywords": []}

    def create_negative_keywords(self, keywords: JSONList) -> JSONData:
        """批量创建SB Negative Keyword"""
        result = self.post("/sb/negativeKeywords", json_data=keywords)
        return result if isinstance(result, dict) else {"negativeKeywords": {"success": [], "error": []}}

    def delete_negative_keyword(self, keyword_id: str) -> JSONData:
        """删除Negative Keyword"""
        return self.delete(f"/sb/negativeKeywords/{keyword_id}")

    # ============ Product Targeting ============

    def list_targets(
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

        result = self.post("/sb/targets/list", json_data=params)
        return result if isinstance(result, dict) else {"targets": []}

    def create_targets(self, targets: JSONList) -> JSONData:
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
        result = self.post("/sb/targets", json_data=targets)
        return result if isinstance(result, dict) else {"targets": {"success": [], "error": []}}

    def update_targets(self, targets: JSONList) -> JSONData:
        """批量更新SB Target"""
        result = self.put("/sb/targets", json_data=targets)
        return result if isinstance(result, dict) else {"targets": {"success": [], "error": []}}

    def delete_target(self, target_id: str) -> JSONData:
        """归档Target"""
        return self.delete(f"/sb/targets/{target_id}")

    # ============ Negative Targets ============

    def list_negative_targets(
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

        result = self.post("/sb/negativeTargets/list", json_data=params)
        return result if isinstance(result, dict) else {"negativeTargets": []}

    def create_negative_targets(self, targets: JSONList) -> JSONData:
        """批量创建SB Negative Target"""
        result = self.post("/sb/negativeTargets", json_data=targets)
        return result if isinstance(result, dict) else {"negativeTargets": {"success": [], "error": []}}

    # ============ Recommendations ============

    def get_keyword_recommendations(
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

        result = self.post("/sb/recommendations/keyword", json_data=body)
        return result if isinstance(result, dict) else {"recommendations": []}

    def get_targeting_recommendations(
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

        result = self.post("/sb/recommendations/targets", json_data=body)
        return result if isinstance(result, dict) else {"recommendations": []}

    def get_bid_recommendations(
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

        result = self.post("/sb/recommendations/bids", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ Category Targeting ============

    def get_targeting_categories(
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

        result = self.post("/sb/targets/categories", json_data=body)
        return result if isinstance(result, dict) else {"categories": []}

    # ============ 便捷方法 ============

    def pause_keyword(self, keyword_id: str) -> JSONData:
        """暂停Keyword"""
        return self.update_keywords([{"keywordId": keyword_id, "state": "paused"}])

    def update_bid(self, keyword_id: str, bid: float) -> JSONData:
        """更新Keyword竞价"""
        return self.update_keywords([{"keywordId": keyword_id, "bid": bid}])

    def list_all_keywords(
        self,
        campaign_id: str | None = None,
        state_filter: str | None = None,
    ) -> JSONList:
        """获取所有Keyword（自动分页）"""
        all_keywords = []
        next_token = None

        while True:
            result = self.list_keywords(
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

