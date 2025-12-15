"""
Sponsored Brands - Targeting API (异步版本)
SB定向管理（品类、品牌推荐）

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SBTargetingAPI(BaseAdsClient):
    """SB Targeting API (全异步)"""

    # ============ Categories ============

    async def list_targetable_categories(
        self,
        parent_category_id: str | None = None,
    ) -> JSONData:
        """
        获取可定向的品类列表
        
        Args:
            parent_category_id: 父品类ID（用于获取子品类）
        """
        params = {}
        if parent_category_id:
            params["parentCategoryId"] = parent_category_id

        result = await self.get("/sb/targets/categories", params=params or None)
        return result if isinstance(result, dict) else {"categories": []}

    async def get_category_refinements(
        self,
        category_id: str,
    ) -> JSONData:
        """
        获取品类细化选项
        
        返回可用于细化定向的品牌、价格范围、评分等
        """
        result = await self.get(f"/sb/targets/categories/{category_id}/refinements")
        return result if isinstance(result, dict) else {}

    async def get_product_count(
        self,
        category_id: str,
        refinements: JSONData | None = None,
    ) -> JSONData:
        """
        获取品类中的产品数量
        
        Args:
            category_id: 品类ID
            refinements: 细化条件
        """
        body: JSONData = {"categoryId": category_id}
        if refinements:
            body["refinements"] = refinements

        result = await self.post("/sb/targets/products/count", json_data=body)
        return result if isinstance(result, dict) else {"count": 0}

    # ============ Negative Targets ============

    async def get_negative_brand_recommendations(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
    ) -> JSONData:
        """
        获取否定品牌推荐
        
        Args:
            ad_group_id: Ad Group ID
            campaign_id: Campaign ID
        """
        params = {}
        if ad_group_id:
            params["adGroupId"] = ad_group_id
        if campaign_id:
            params["campaignId"] = campaign_id

        result = await self.get(
            "/sb/negativeTargets/brands/recommendations",
            params=params or None
        )
        return result if isinstance(result, dict) else {"brands": []}

    # ============ 便捷方法 ============

    async def search_categories(
        self,
        query: str,
        max_results: int = 50,
    ) -> JSONData:
        """搜索品类"""
        # 获取根品类列表并过滤
        result = await self.list_targetable_categories()
        categories = result.get("categories", [])
        
        # 简单文本匹配过滤
        filtered = [
            c for c in categories 
            if query.lower() in c.get("name", "").lower()
        ][:max_results]
        
        return {"categories": filtered}

