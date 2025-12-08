"""
Sponsored Products - Theme Targeting API (异步版本)
SP主题定向和品类定向
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SPThemeTargetingAPI(BaseAdsClient):
    """SP Theme Targeting API (全异步)"""

    # ============ Theme-based Targeting ============

    async def get_theme_recommendations(
        self,
        asins: list[str],
        max_results: int = 100,
    ) -> JSONData:
        """
        获取主题定向建议
        
        基于ASIN推荐相关主题
        """
        result = await self.post("/sp/themes/recommendations", json_data={
            "asins": asins,
            "maxResults": max_results,
        })
        return result if isinstance(result, dict) else {"themes": []}

    async def search_themes(
        self,
        query: str,
        max_results: int = 100,
    ) -> JSONData:
        """搜索主题"""
        result = await self.post("/sp/themes/search", json_data={
            "query": query,
            "maxResults": max_results,
        })
        return result if isinstance(result, dict) else {"themes": []}

    async def get_theme_details(self, theme_id: str) -> JSONData:
        """获取主题详情"""
        result = await self.get(f"/sp/themes/{theme_id}")
        return result if isinstance(result, dict) else {}

    # ============ Category Targeting ============

    async def list_targetable_categories(
        self,
        parent_category_id: str | None = None,
    ) -> JSONList:
        """获取可定向的品类列表"""
        params = {}
        if parent_category_id:
            params["parentCategoryId"] = parent_category_id

        result = await self.get("/sp/targets/categories", params=params or None)
        return result if isinstance(result, list) else []

    async def get_category_refinements(
        self,
        category_id: str,
    ) -> JSONData:
        """
        获取品类细化选项
        
        返回可用于细化定向的品牌、价格范围等
        """
        result = await self.get(f"/sp/targets/categories/{category_id}/refinements")
        return result if isinstance(result, dict) else {}

    async def get_category_bid_recommendations(
        self,
        category_id: str,
        ad_group_id: str,
    ) -> JSONData:
        """获取品类定向竞价建议"""
        result = await self.post("/sp/targets/categories/bidRecommendations", json_data={
            "categoryId": category_id,
            "adGroupId": ad_group_id,
        })
        return result if isinstance(result, dict) else {}

    # ============ Product Attribute Targeting ============

    async def get_brand_targeting_options(
        self,
        category_id: str,
    ) -> JSONList:
        """获取品牌定向选项"""
        result = await self.get(f"/sp/targets/categories/{category_id}/brands")
        return result if isinstance(result, list) else []

    async def get_price_range_targeting_options(
        self,
        category_id: str,
    ) -> JSONData:
        """获取价格范围定向选项"""
        result = await self.get(f"/sp/targets/categories/{category_id}/priceRanges")
        return result if isinstance(result, dict) else {}

    async def get_review_rating_targeting_options(
        self,
        category_id: str,
    ) -> JSONList:
        """获取评分定向选项"""
        result = await self.get(f"/sp/targets/categories/{category_id}/reviewRatings")
        return result if isinstance(result, list) else []

    # ============ Similar Product Targeting ============

    async def get_similar_products(
        self,
        asin: str,
        max_results: int = 50,
    ) -> JSONData:
        """获取相似产品（用于定向）"""
        result = await self.post("/sp/targets/similarProducts", json_data={
            "asin": asin,
            "maxResults": max_results,
        })
        return result if isinstance(result, dict) else {"products": []}

    async def get_complementary_products(
        self,
        asin: str,
        max_results: int = 50,
    ) -> JSONData:
        """获取互补产品（用于定向）"""
        result = await self.post("/sp/targets/complementaryProducts", json_data={
            "asin": asin,
            "maxResults": max_results,
        })
        return result if isinstance(result, dict) else {"products": []}

    async def get_substitute_products(
        self,
        asin: str,
        max_results: int = 50,
    ) -> JSONData:
        """获取替代产品（用于定向）"""
        result = await self.post("/sp/targets/substituteProducts", json_data={
            "asin": asin,
            "maxResults": max_results,
        })
        return result if isinstance(result, dict) else {"products": []}

    # ============ Contextual Targeting ============

    async def get_contextual_targeting_recommendations(
        self,
        asins: list[str],
        max_results: int = 100,
    ) -> JSONData:
        """获取上下文定向建议"""
        result = await self.post("/sp/targets/contextual/recommendations", json_data={
            "asins": asins,
            "maxResults": max_results,
        })
        return result if isinstance(result, dict) else {}

    # ============ Audience-based Targeting ============

    async def get_audience_targeting_recommendations(
        self,
        asins: list[str],
        max_results: int = 50,
    ) -> JSONData:
        """
        获取受众定向建议（SP Beta）
        
        SP的受众定向功能
        """
        result = await self.post("/sp/targets/audiences/recommendations", json_data={
            "asins": asins,
            "maxResults": max_results,
        })
        return result if isinstance(result, dict) else {}

    # ============ Targeting Expression Builder ============

    def build_category_expression(
        self,
        category_id: str,
        brand_filter: list[str] | None = None,
        price_range: dict | None = None,
        review_rating: float | None = None,
    ) -> JSONList:
        """
        构建品类定向表达式
        
        Args:
            brand_filter: 品牌筛选
            price_range: {"min": 10, "max": 100}
            review_rating: 最低评分
        """
        expression = [{"type": "asinCategorySameAs", "value": category_id}]

        if brand_filter:
            expression.append({
                "type": "asinBrandSameAs",
                "value": brand_filter
            })

        if price_range:
            expression.append({
                "type": "asinPriceBetween",
                "value": f"{price_range.get('min', 0)}-{price_range.get('max', 999999)}"
            })

        if review_rating:
            expression.append({
                "type": "asinReviewRatingGreaterThan",
                "value": str(review_rating)
            })

        return expression

    def build_product_expression(
        self,
        asins: list[str],
        expanded: bool = False,
    ) -> JSONList:
        """
        构建产品定向表达式
        
        Args:
            expanded: 是否扩展到相似产品
        """
        expressions = []
        for asin in asins:
            if expanded:
                expressions.append({
                    "type": "asinExpandedFrom",
                    "value": asin
                })
            else:
                expressions.append({
                    "type": "asinSameAs",
                    "value": asin
                })
        return expressions

    # ============ 便捷方法 ============

    async def get_all_targetable_categories(self) -> JSONList:
        """获取所有可定向品类（递归）"""
        all_categories = []

        async def fetch_recursive(parent_id: str | None = None):
            categories = await self.list_targetable_categories(parent_id)
            for cat in categories:
                all_categories.append(cat)
                cat_id = cat.get("categoryId")
                if cat_id and cat.get("hasChildren"):
                    await fetch_recursive(cat_id)

        await fetch_recursive()
        return all_categories

    async def get_comprehensive_targeting_suggestions(
        self,
        asins: list[str],
    ) -> JSONData:
        """获取综合定向建议"""
        themes = await self.get_theme_recommendations(asins)
        similar = []
        complementary = []

        for asin in asins[:5]:  # 限制数量
            similar_result = await self.get_similar_products(asin, 10)
            similar.extend(similar_result.get("products", []))
            comp_result = await self.get_complementary_products(asin, 10)
            complementary.extend(comp_result.get("products", []))

        return {
            "themes": themes.get("themes", []),
            "similarProducts": similar,
            "complementaryProducts": complementary,
        }
