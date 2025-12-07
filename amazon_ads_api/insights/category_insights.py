"""
Category Insights API
品类洞察分析
"""

from ..base import BaseAdsClient, JSONData, JSONList


class CategoryInsightsAPI(BaseAdsClient):
    """Category Insights API"""

    # ============ Category Discovery ============

    def search_categories(
        self,
        query: str,
        marketplace: str = "US",
        max_results: int = 100,
    ) -> JSONData:
        """
        搜索品类
        
        Args:
            query: 搜索词
            marketplace: US, CA, UK, DE, FR, IT, ES, JP, AU, etc.
        """
        result = self.post("/insights/categories/search", json_data={
            "query": query,
            "marketplace": marketplace,
            "maxResults": max_results,
        })
        return result if isinstance(result, dict) else {"categories": []}

    def get_category(self, category_id: str) -> JSONData:
        """获取品类详情"""
        result = self.get(f"/insights/categories/{category_id}")
        return result if isinstance(result, dict) else {}

    def list_subcategories(self, parent_category_id: str) -> JSONList:
        """获取子品类列表"""
        result = self.get(f"/insights/categories/{parent_category_id}/subcategories")
        return result if isinstance(result, list) else []

    def get_category_hierarchy(self, category_id: str) -> JSONData:
        """获取品类层级路径"""
        result = self.get(f"/insights/categories/{category_id}/hierarchy")
        return result if isinstance(result, dict) else {}

    # ============ Category Metrics ============

    def get_category_metrics(
        self,
        category_id: str,
        start_date: str,
        end_date: str,
        metrics: list[str] | None = None,
    ) -> JSONData:
        """
        获取品类指标
        
        Args:
            metrics: [
                "searchVolume", "clickVolume", "conversionRate",
                "averagePrice", "totalSales", "brandCount"
            ]
        """
        body: JSONData = {
            "categoryId": category_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        if metrics:
            body["metrics"] = metrics

        result = self.post("/insights/categories/metrics", json_data=body)
        return result if isinstance(result, dict) else {}

    def get_category_trends(
        self,
        category_id: str,
        period: str = "LAST_30_DAYS",
        granularity: str = "DAILY",
    ) -> JSONData:
        """
        获取品类趋势
        
        Args:
            period: LAST_7_DAYS | LAST_30_DAYS | LAST_90_DAYS | LAST_YEAR
            granularity: DAILY | WEEKLY | MONTHLY
        """
        result = self.get(f"/insights/categories/{category_id}/trends", params={
            "period": period,
            "granularity": granularity,
        })
        return result if isinstance(result, dict) else {}

    def get_category_seasonality(self, category_id: str) -> JSONData:
        """获取品类季节性数据"""
        result = self.get(f"/insights/categories/{category_id}/seasonality")
        return result if isinstance(result, dict) else {}

    # ============ Category Competition ============

    def get_category_competition(self, category_id: str) -> JSONData:
        """
        获取品类竞争分析
        
        返回广告竞争度、CPC范围等
        """
        result = self.get(f"/insights/categories/{category_id}/competition")
        return result if isinstance(result, dict) else {}

    def get_top_brands_in_category(
        self,
        category_id: str,
        limit: int = 20,
    ) -> JSONList:
        """获取品类Top品牌"""
        result = self.get(f"/insights/categories/{category_id}/topBrands", params={
            "limit": limit
        })
        return result if isinstance(result, list) else []

    def get_top_asins_in_category(
        self,
        category_id: str,
        limit: int = 100,
        sort_by: str = "SALES",
    ) -> JSONList:
        """
        获取品类Top ASIN
        
        Args:
            sort_by: SALES | REVIEWS | RATING | SEARCH_RANK
        """
        result = self.get(f"/insights/categories/{category_id}/topAsins", params={
            "limit": limit,
            "sortBy": sort_by,
        })
        return result if isinstance(result, list) else []

    # ============ Category Keywords ============

    def get_category_keywords(
        self,
        category_id: str,
        limit: int = 100,
        sort_by: str = "SEARCH_VOLUME",
    ) -> JSONList:
        """
        获取品类热门关键词
        
        Args:
            sort_by: SEARCH_VOLUME | COMPETITION | CPC
        """
        result = self.get(f"/insights/categories/{category_id}/keywords", params={
            "limit": limit,
            "sortBy": sort_by,
        })
        return result if isinstance(result, list) else []

    def get_category_search_terms(
        self,
        category_id: str,
        period: str = "LAST_30_DAYS",
        limit: int = 100,
    ) -> JSONList:
        """获取品类热门搜索词"""
        result = self.get(f"/insights/categories/{category_id}/searchTerms", params={
            "period": period,
            "limit": limit,
        })
        return result if isinstance(result, list) else []

    # ============ Category Advertising Metrics ============

    def get_category_ad_metrics(
        self,
        category_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """
        获取品类广告指标
        
        返回该品类的平均CTR、CPC、CVR、ACoS等
        """
        result = self.post("/insights/categories/adMetrics", json_data={
            "categoryId": category_id,
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, dict) else {}

    def get_category_benchmark(
        self,
        category_id: str,
        metrics: list[str] | None = None,
    ) -> JSONData:
        """
        获取品类基准数据
        
        用于与自己的广告效果对比
        """
        body: JSONData = {"categoryId": category_id}
        if metrics:
            body["metrics"] = metrics

        result = self.post("/insights/categories/benchmark", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ Market Share ============

    def get_market_share(
        self,
        category_id: str,
        brand_entity_id: str | None = None,
    ) -> JSONData:
        """
        获取市场份额
        
        Args:
            brand_entity_id: 指定品牌，否则返回整体数据
        """
        params: JSONData = {}
        if brand_entity_id:
            params["brandEntityId"] = brand_entity_id

        result = self.get(f"/insights/categories/{category_id}/marketShare", params=params)
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    def get_category_overview(
        self,
        category_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取品类综合概览"""
        category = self.get_category(category_id)
        metrics = self.get_category_metrics(category_id, start_date, end_date)
        competition = self.get_category_competition(category_id)
        ad_metrics = self.get_category_ad_metrics(category_id, start_date, end_date)

        return {
            "category": category,
            "metrics": metrics,
            "competition": competition,
            "adMetrics": ad_metrics,
        }

    def find_high_opportunity_categories(
        self,
        parent_category_id: str,
        min_search_volume: int = 10000,
        max_competition: float = 0.7,
    ) -> JSONList:
        """
        发现高机会品类
        
        筛选搜索量高、竞争度低的品类
        """
        subcategories = self.list_subcategories(parent_category_id)
        opportunities = []

        for subcat in subcategories:
            cat_id = subcat.get("categoryId")
            if not cat_id:
                continue

            competition = self.get_category_competition(cat_id)
            search_volume = competition.get("searchVolume", 0)
            competition_index = competition.get("competitionIndex", 1)

            if search_volume >= min_search_volume and competition_index <= max_competition:
                opportunities.append({
                    **subcat,
                    "searchVolume": search_volume,
                    "competitionIndex": competition_index,
                })

        return sorted(opportunities, key=lambda x: x.get("searchVolume", 0), reverse=True)

