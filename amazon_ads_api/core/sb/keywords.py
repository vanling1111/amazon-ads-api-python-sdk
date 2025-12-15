"""
Sponsored Brands - Keywords API (异步版本)
SB关键词管理
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SBKeywordsAPI(BaseAdsClient):
    """SB Keywords API (全异步)"""
    
    # SB Keywords API v4 Content-Type
    SB_KEYWORDS_V4_CONTENT_TYPE = "application/vnd.sbkeywordresource.v4+json"

    # ============ Keywords ============

    async def list_keywords(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        state_filter: str | None = None,
        max_results: int = 100,
        start_index: int = 0,
    ) -> JSONList:
        """
        获取SB Keyword列表 (v3 API - GET /sb/keywords)
        
        官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi#tag/Keywords
        
        Args:
            ad_group_id: 广告组ID筛选
            campaign_id: Campaign ID筛选
            state_filter: 状态筛选 (enabled, paused, archived)
            max_results: 最大返回数量 (1-5000)
            start_index: 分页起始位置
        """
        params: JSONData = {"count": max_results, "startIndex": start_index}
        if ad_group_id:
            params["adGroupIdFilter"] = ad_group_id
        if campaign_id:
            params["campaignIdFilter"] = campaign_id
        if state_filter:
            params["stateFilter"] = state_filter

        result = await self.get("/sb/keywords", params=params)
        return result if isinstance(result, list) else []

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

    async def list_negative_keywords_v3(
        self,
        start_index: int = 0,
        count: int = 100,
        match_type_filter: str | None = None,
        keyword_text: str | None = None,
        state_filter: str | None = None,
        campaign_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        keyword_id_filter: str | None = None,
        creative_type: str | None = None,
    ) -> JSONList:
        """
        获取SB Negative Keyword列表 (v3 GET API)
        
        官方端点: GET /sb/negativeKeywords
        官方文档: SponsoredBrands_v3.yaml
        """
        params: JSONData = {"startIndex": start_index, "count": count}
        if match_type_filter:
            params["matchTypeFilter"] = match_type_filter
        if keyword_text:
            params["keywordText"] = keyword_text
        if state_filter:
            params["stateFilter"] = state_filter
        if campaign_id_filter:
            params["campaignIdFilter"] = campaign_id_filter
        if ad_group_id_filter:
            params["adGroupIdFilter"] = ad_group_id_filter
        if keyword_id_filter:
            params["keywordIdFilter"] = keyword_id_filter
        if creative_type:
            params["creativeType"] = creative_type

        result = await self.get("/sb/negativeKeywords", params=params)
        return result if isinstance(result, list) else []

    async def get_negative_keyword(self, keyword_id: str) -> JSONData:
        """
        获取单个 Negative Keyword 详情
        
        官方端点: GET /sb/negativeKeywords/{keywordId}
        """
        result = await self.get(f"/sb/negativeKeywords/{keyword_id}")
        return result if isinstance(result, dict) else {}

    async def list_negative_keywords(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        max_results: int = 100,
    ) -> JSONData:
        """获取SB Negative Keyword列表 (POST /sb/negativeKeywords/list)"""
        params: JSONData = {"maxResults": max_results}
        if ad_group_id:
            params["adGroupIdFilter"] = [ad_group_id]
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]

        result = await self.post("/sb/negativeKeywords/list", json_data=params)
        return result if isinstance(result, dict) else {"negativeKeywords": []}

    async def create_negative_keywords(self, keywords: JSONList) -> JSONData:
        """
        批量创建SB Negative Keyword
        
        官方端点: POST /sb/negativeKeywords
        """
        result = await self.post("/sb/negativeKeywords", json_data=keywords)
        return result if isinstance(result, dict) else {"negativeKeywords": {"success": [], "error": []}}

    async def update_negative_keywords(self, keywords: JSONList) -> JSONData:
        """
        批量更新SB Negative Keyword
        
        官方端点: PUT /sb/negativeKeywords
        """
        result = await self.put("/sb/negativeKeywords", json_data=keywords)
        return result if isinstance(result, dict) else {"negativeKeywords": {"success": [], "error": []}}

    async def delete_negative_keyword(self, keyword_id: str) -> JSONData:
        """
        删除Negative Keyword
        
        官方端点: DELETE /sb/negativeKeywords/{keywordId}
        """
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

    async def get_target(self, target_id: str) -> JSONData:
        """
        获取单个 Target 详情
        
        官方端点: GET /sb/targets/{targetId}
        """
        result = await self.get(f"/sb/targets/{target_id}")
        return result if isinstance(result, dict) else {}

    async def delete_target(self, target_id: str) -> JSONData:
        """
        归档Target
        
        官方端点: DELETE /sb/targets/{targetId}
        """
        return await self.delete(f"/sb/targets/{target_id}")

    # ============ Negative Targets ============

    async def list_negative_targets(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        max_results: int = 100,
    ) -> JSONData:
        """
        获取SB Negative Target列表
        
        官方端点: POST /sb/negativeTargets/list
        """
        params: JSONData = {"maxResults": max_results}
        if ad_group_id:
            params["adGroupIdFilter"] = [ad_group_id]
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]

        result = await self.post("/sb/negativeTargets/list", json_data=params)
        return result if isinstance(result, dict) else {"negativeTargets": []}

    async def get_negative_target(self, negative_target_id: str) -> JSONData:
        """
        获取单个 Negative Target 详情
        
        官方端点: GET /sb/negativeTargets/{negativeTargetId}
        """
        result = await self.get(f"/sb/negativeTargets/{negative_target_id}")
        return result if isinstance(result, dict) else {}

    async def create_negative_targets(self, targets: JSONList) -> JSONData:
        """
        批量创建SB Negative Target
        
        官方端点: POST /sb/negativeTargets
        """
        result = await self.post("/sb/negativeTargets", json_data=targets)
        return result if isinstance(result, dict) else {"negativeTargets": {"success": [], "error": []}}

    async def update_negative_targets(self, targets: JSONList) -> JSONData:
        """
        批量更新SB Negative Target
        
        官方端点: PUT /sb/negativeTargets
        """
        result = await self.put("/sb/negativeTargets", json_data=targets)
        return result if isinstance(result, dict) else {"negativeTargets": {"success": [], "error": []}}

    async def delete_negative_target(self, negative_target_id: str) -> JSONData:
        """
        归档 Negative Target
        
        官方端点: DELETE /sb/negativeTargets/{negativeTargetId}
        """
        return await self.delete(f"/sb/negativeTargets/{negative_target_id}")

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

    # ============ Target Recommendations ============

    async def get_brand_recommendations(
        self,
        asins: list[str] | None = None,
        page_url: str | None = None,
    ) -> JSONData:
        """
        获取品牌推荐列表
        
        官方端点: POST /sb/recommendations/targets/brand
        官方文档: SponsoredBrands_v3.yaml
        """
        body: JSONData = {}
        if asins:
            body["asins"] = asins
        if page_url:
            body["pageUrl"] = page_url

        result = await self.post("/sb/recommendations/targets/brand", json_data=body)
        return result if isinstance(result, dict) else {"brands": []}

    async def get_category_recommendations(
        self,
        asins: list[str] | None = None,
        locale: str | None = None,
    ) -> JSONData:
        """
        获取品类推荐列表
        
        官方端点: POST /sb/recommendations/targets/category
        官方文档: SponsoredBrands_v3.yaml
        """
        body: JSONData = {}
        if asins:
            body["asins"] = asins

        params = {}
        if locale:
            params["locale"] = locale

        result = await self.post(
            "/sb/recommendations/targets/category", 
            json_data=body,
            params=params if params else None
        )
        return result if isinstance(result, dict) else {"categories": []}

    async def get_product_recommendations(
        self,
        targets: list[dict] | None = None,
        next_token: str | None = None,
        max_results: int = 100,
    ) -> JSONData:
        """
        获取产品推荐列表
        
        官方端点: POST /sb/recommendations/targets/product/list
        官方文档: SponsoredBrands_v3.yaml
        """
        body: JSONData = {"maxResults": max_results}
        if targets:
            body["targets"] = targets
        if next_token:
            body["nextToken"] = next_token

        result = await self.post("/sb/recommendations/targets/product/list", json_data=body)
        return result if isinstance(result, dict) else {"recommendedProducts": []}

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
        start_index = 0
        page_size = 5000  # SB API 最大支持 5000

        while True:
            keywords = await self.list_keywords(
                campaign_id=campaign_id,
                state_filter=state_filter,
                max_results=page_size,
                start_index=start_index,
            )
            
            if not keywords:
                break
                
            all_keywords.extend(keywords)
            
            if len(keywords) < page_size:
                break
                
            start_index += len(keywords)

        return all_keywords
