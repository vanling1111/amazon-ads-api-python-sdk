"""
Keyword Insights API (异步版本)
关键词洞察分析
"""

from ..base import BaseAdsClient, JSONData, JSONList


class KeywordInsightsAPI(BaseAdsClient):
    """Keyword Insights API (全异步)"""

    # ============ Keyword Research ============

    async def search_keywords(
        self,
        seed_keyword: str,
        marketplace: str = "US",
        max_results: int = 100,
    ) -> JSONData:
        """
        关键词搜索/拓展
        
        Args:
            seed_keyword: 种子关键词
            marketplace: 市场
        """
        result = await self.post("/insights/keywords/search", json_data={
            "seedKeyword": seed_keyword,
            "marketplace": marketplace,
            "maxResults": max_results,
        })
        return result if isinstance(result, dict) else {"keywords": []}

    async def get_keyword_suggestions(
        self,
        asins: list[str],
        max_results: int = 100,
        sort_by: str = "RELEVANCE",
    ) -> JSONData:
        """
        基于ASIN获取关键词建议
        
        Args:
            sort_by: RELEVANCE | SEARCH_VOLUME | OPPORTUNITY
        """
        result = await self.post("/insights/keywords/suggestions", json_data={
            "asins": asins,
            "maxResults": max_results,
            "sortBy": sort_by,
        })
        return result if isinstance(result, dict) else {"keywords": []}

    # ============ Keyword Metrics ============

    async def get_keyword_metrics(
        self,
        keywords: list[str],
        marketplace: str = "US",
    ) -> JSONData:
        """
        获取关键词指标
        
        返回搜索量、竞争度、CPC等
        """
        result = await self.post("/insights/keywords/metrics", json_data={
            "keywords": keywords,
            "marketplace": marketplace,
        })
        return result if isinstance(result, dict) else {"keywords": []}

    async def get_keyword_trends(
        self,
        keyword: str,
        marketplace: str = "US",
        period: str = "LAST_12_MONTHS",
    ) -> JSONData:
        """
        获取关键词趋势
        
        Args:
            period: LAST_30_DAYS | LAST_90_DAYS | LAST_12_MONTHS
        """
        result = await self.get("/insights/keywords/trends", params={
            "keyword": keyword,
            "marketplace": marketplace,
            "period": period,
        })
        return result if isinstance(result, dict) else {}

    async def get_keyword_seasonality(
        self,
        keyword: str,
        marketplace: str = "US",
    ) -> JSONData:
        """获取关键词季节性数据"""
        result = await self.get("/insights/keywords/seasonality", params={
            "keyword": keyword,
            "marketplace": marketplace,
        })
        return result if isinstance(result, dict) else {}

    # ============ Keyword Competition ============

    async def get_keyword_competition(
        self,
        keyword: str,
        marketplace: str = "US",
    ) -> JSONData:
        """
        获取关键词竞争分析
        
        返回竞争广告主数量、CPC范围、首页品牌等
        """
        result = await self.get("/insights/keywords/competition", params={
            "keyword": keyword,
            "marketplace": marketplace,
        })
        return result if isinstance(result, dict) else {}

    async def get_keyword_top_asins(
        self,
        keyword: str,
        marketplace: str = "US",
        limit: int = 50,
    ) -> JSONList:
        """获取关键词Top排名ASIN"""
        result = await self.get("/insights/keywords/topAsins", params={
            "keyword": keyword,
            "marketplace": marketplace,
            "limit": limit,
        })
        return result if isinstance(result, list) else []

    async def get_keyword_ad_placements(
        self,
        keyword: str,
        marketplace: str = "US",
    ) -> JSONData:
        """
        获取关键词广告位分析
        
        分析该关键词的广告位分布情况
        """
        result = await self.get("/insights/keywords/adPlacements", params={
            "keyword": keyword,
            "marketplace": marketplace,
        })
        return result if isinstance(result, dict) else {}

    # ============ Related Keywords ============

    async def get_related_keywords(
        self,
        keyword: str,
        marketplace: str = "US",
        max_results: int = 100,
    ) -> JSONList:
        """获取相关关键词"""
        result = await self.get("/insights/keywords/related", params={
            "keyword": keyword,
            "marketplace": marketplace,
            "maxResults": max_results,
        })
        return result if isinstance(result, list) else []

    async def get_long_tail_keywords(
        self,
        seed_keyword: str,
        marketplace: str = "US",
        max_results: int = 100,
    ) -> JSONList:
        """获取长尾关键词"""
        result = await self.post("/insights/keywords/longTail", json_data={
            "seedKeyword": seed_keyword,
            "marketplace": marketplace,
            "maxResults": max_results,
        })
        return result if isinstance(result, list) else []

    async def get_negative_keyword_suggestions(
        self,
        keywords: list[str],
        marketplace: str = "US",
    ) -> JSONList:
        """获取否定关键词建议"""
        result = await self.post("/insights/keywords/negativeSuggestions", json_data={
            "keywords": keywords,
            "marketplace": marketplace,
        })
        return result if isinstance(result, list) else []

    # ============ Keyword Bid Insights ============

    async def get_keyword_bid_landscape(
        self,
        keyword: str,
        match_type: str = "EXACT",
        marketplace: str = "US",
    ) -> JSONData:
        """
        获取关键词竞价全景
        
        分析不同竞价水平下的预期效果
        """
        result = await self.get("/insights/keywords/bidLandscape", params={
            "keyword": keyword,
            "matchType": match_type,
            "marketplace": marketplace,
        })
        return result if isinstance(result, dict) else {}

    async def get_keyword_position_analysis(
        self,
        keyword: str,
        current_bid: float,
        marketplace: str = "US",
    ) -> JSONData:
        """
        获取关键词排名分析
        
        预测当前竞价下的广告排名
        """
        result = await self.post("/insights/keywords/positionAnalysis", json_data={
            "keyword": keyword,
            "currentBid": current_bid,
            "marketplace": marketplace,
        })
        return result if isinstance(result, dict) else {}

    # ============ Search Term Insights ============

    async def get_search_term_insights(
        self,
        search_term: str,
        marketplace: str = "US",
    ) -> JSONData:
        """获取搜索词洞察"""
        result = await self.get("/insights/searchTerms", params={
            "searchTerm": search_term,
            "marketplace": marketplace,
        })
        return result if isinstance(result, dict) else {}

    async def get_trending_search_terms(
        self,
        category_id: str | None = None,
        marketplace: str = "US",
        period: str = "LAST_7_DAYS",
        limit: int = 100,
    ) -> JSONList:
        """获取热门搜索词"""
        params: JSONData = {
            "marketplace": marketplace,
            "period": period,
            "limit": limit,
        }
        if category_id:
            params["categoryId"] = category_id

        result = await self.get("/insights/searchTerms/trending", params=params)
        return result if isinstance(result, list) else []

    # ============ Keyword Opportunity Score ============

    async def get_keyword_opportunity_score(
        self,
        keywords: list[str],
        asins: list[str] | None = None,
        marketplace: str = "US",
    ) -> JSONData:
        """
        获取关键词机会评分
        
        综合搜索量、竞争度、相关性计算机会分数
        """
        body: JSONData = {
            "keywords": keywords,
            "marketplace": marketplace,
        }
        if asins:
            body["asins"] = asins

        result = await self.post("/insights/keywords/opportunityScore", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def get_keyword_full_analysis(
        self,
        keyword: str,
        marketplace: str = "US",
    ) -> JSONData:
        """获取关键词完整分析"""
        metrics = await self.get_keyword_metrics([keyword], marketplace)
        competition = await self.get_keyword_competition(keyword, marketplace)
        trends = await self.get_keyword_trends(keyword, marketplace)
        related = await self.get_related_keywords(keyword, marketplace, max_results=20)
        bid_landscape = await self.get_keyword_bid_landscape(keyword, "EXACT", marketplace)

        return {
            "keyword": keyword,
            "metrics": metrics.get("keywords", [{}])[0] if metrics.get("keywords") else {},
            "competition": competition,
            "trends": trends,
            "relatedKeywords": related,
            "bidLandscape": bid_landscape,
        }

    async def find_high_opportunity_keywords(
        self,
        seed_keywords: list[str],
        min_search_volume: int = 1000,
        max_competition_index: float = 0.5,
        marketplace: str = "US",
    ) -> JSONList:
        """
        发现高机会关键词
        
        筛选高搜索量、低竞争的关键词
        """
        all_keywords = []

        for seed in seed_keywords:
            result = await self.search_keywords(seed, marketplace, max_results=50)
            all_keywords.extend(result.get("keywords", []))

        # 获取详细指标
        keyword_texts = [kw.get("keyword") for kw in all_keywords if kw.get("keyword")]
        if not keyword_texts:
            return []

        metrics = await self.get_keyword_metrics(keyword_texts[:100], marketplace)

        # 筛选
        opportunities = []
        for kw_data in metrics.get("keywords", []):
            search_volume = kw_data.get("searchVolume", 0)
            competition_index = kw_data.get("competitionIndex", 1)

            if search_volume >= min_search_volume and competition_index <= max_competition_index:
                opportunities.append(kw_data)

        return sorted(opportunities, key=lambda x: x.get("searchVolume", 0), reverse=True)

    async def batch_get_keyword_metrics(
        self,
        keywords: list[str],
        marketplace: str = "US",
        batch_size: int = 100,
    ) -> JSONList:
        """批量获取关键词指标"""
        all_results = []

        for i in range(0, len(keywords), batch_size):
            batch = keywords[i:i + batch_size]
            result = await self.get_keyword_metrics(batch, marketplace)
            all_results.extend(result.get("keywords", []))

        return all_results
