"""
Amazon Ads Category Insights API (异步版本)
品类洞察分析
"""

from ..base import BaseAdsClient, JSONData, JSONList


class CategoryInsightsAPI(BaseAdsClient):
    """Category Insights API (全异步)"""

    # ============ Category Discovery ============

    async def search_categories(
        self,
        query: str,
        marketplace: str = "US",
        max_results: int = 100,
    ) -> JSONData:
        """搜索品类"""
        result = await self.post("/insights/categories/search", json_data={
            "query": query,
            "marketplace": marketplace,
            "maxResults": max_results,
        })
        return result if isinstance(result, dict) else {"categories": []}

    async def get_category(self, category_id: str) -> JSONData:
        """获取品类详情"""
        result = await self.get(f"/insights/categories/{category_id}")
        return result if isinstance(result, dict) else {}

    async def list_subcategories(self, parent_category_id: str) -> JSONList:
        """获取子品类列表"""
        result = await self.get(f"/insights/categories/{parent_category_id}/subcategories")
        return result if isinstance(result, list) else []

    async def get_category_hierarchy(self, category_id: str) -> JSONData:
        """获取品类层级路径"""
        result = await self.get(f"/insights/categories/{category_id}/hierarchy")
        return result if isinstance(result, dict) else {}

    # ============ Category Metrics ============

    async def get_category_metrics(
        self,
        category_id: str,
        start_date: str,
        end_date: str,
        metrics: list[str] | None = None,
    ) -> JSONData:
        """获取品类指标"""
        body: JSONData = {
            "categoryId": category_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        if metrics:
            body["metrics"] = metrics

        result = await self.post("/insights/categories/metrics", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_category_trends(
        self,
        category_id: str,
        period: str = "LAST_30_DAYS",
        granularity: str = "DAILY",
    ) -> JSONData:
        """获取品类趋势"""
        result = await self.get(f"/insights/categories/{category_id}/trends", params={
            "period": period,
            "granularity": granularity,
        })
        return result if isinstance(result, dict) else {}

    async def get_category_seasonality(self, category_id: str) -> JSONData:
        """获取品类季节性数据"""
        result = await self.get(f"/insights/categories/{category_id}/seasonality")
        return result if isinstance(result, dict) else {}

    # ============ Category Competition ============

    async def get_category_competition(self, category_id: str) -> JSONData:
        """获取品类竞争分析"""
        result = await self.get(f"/insights/categories/{category_id}/competition")
        return result if isinstance(result, dict) else {}

    async def get_top_brands_in_category(
        self,
        category_id: str,
        limit: int = 20,
    ) -> JSONList:
        """获取品类Top品牌"""
        result = await self.get(f"/insights/categories/{category_id}/topBrands", params={
            "limit": limit
        })
        return result if isinstance(result, list) else []

    async def get_top_asins_in_category(
        self,
        category_id: str,
        limit: int = 100,
        sort_by: str = "SALES",
    ) -> JSONList:
        """获取品类Top ASIN"""
        result = await self.get(f"/insights/categories/{category_id}/topAsins", params={
            "limit": limit,
            "sortBy": sort_by,
        })
        return result if isinstance(result, list) else []

    # ============ Category Keywords ============

    async def get_category_keywords(
        self,
        category_id: str,
        limit: int = 100,
        sort_by: str = "SEARCH_VOLUME",
    ) -> JSONList:
        """获取品类热门关键词"""
        result = await self.get(f"/insights/categories/{category_id}/keywords", params={
            "limit": limit,
            "sortBy": sort_by,
        })
        return result if isinstance(result, list) else []

    async def get_category_search_terms(
        self,
        category_id: str,
        period: str = "LAST_30_DAYS",
        limit: int = 100,
    ) -> JSONList:
        """获取品类热门搜索词"""
        result = await self.get(f"/insights/categories/{category_id}/searchTerms", params={
            "period": period,
            "limit": limit,
        })
        return result if isinstance(result, list) else []

    # ============ Category Advertising Metrics ============

    async def get_category_ad_metrics(
        self,
        category_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取品类广告指标"""
        result = await self.post("/insights/categories/adMetrics", json_data={
            "categoryId": category_id,
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, dict) else {}

    async def get_category_benchmark(
        self,
        category_id: str,
        metrics: list[str] | None = None,
    ) -> JSONData:
        """获取品类基准数据"""
        body: JSONData = {"categoryId": category_id}
        if metrics:
            body["metrics"] = metrics

        result = await self.post("/insights/categories/benchmark", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ Market Share ============

    async def get_market_share(
        self,
        category_id: str,
        brand_entity_id: str | None = None,
    ) -> JSONData:
        """获取市场份额"""
        params: JSONData = {}
        if brand_entity_id:
            params["brandEntityId"] = brand_entity_id

        result = await self.get(f"/insights/categories/{category_id}/marketShare", params=params)
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def get_category_overview(
        self,
        category_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取品类综合概览"""
        category = await self.get_category(category_id)
        metrics = await self.get_category_metrics(category_id, start_date, end_date)
        competition = await self.get_category_competition(category_id)
        ad_metrics = await self.get_category_ad_metrics(category_id, start_date, end_date)

        return {
            "category": category,
            "metrics": metrics,
            "competition": competition,
            "adMetrics": ad_metrics,
        }
