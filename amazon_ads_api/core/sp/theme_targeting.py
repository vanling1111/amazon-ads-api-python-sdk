"""
Sponsored Products - Theme & Category Targeting API (异步版本)
SP主题定向和品类定向

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod
OpenAPI Spec: SponsoredProducts_prod_3p.json
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

# API Content-Types
KEYWORD_GROUPS_CONTENT_TYPE = "application/vnd.spkeywordgroupsrecommendation.v1+json"
PRODUCTS_COUNT_CONTENT_TYPE = "application/vnd.sptargetsproductscount.v1+json"


class SPThemeTargetingAPI(BaseAdsClient):
    """
    SP Theme & Category Targeting API (全异步)
    
    官方端点 (共4个):
    - GET /sp/targets/categories - 获取可定向品类
    - POST /sp/targets/categories/recommendations - 获取品类建议
    - GET /sp/targets/category/{categoryId}/refinements - 获取品类细化选项
    - POST /sp/targets/products/count - 获取产品数量
    - POST /sp/targeting/recommendations/keywordGroups - 获取关键词分组建议
    """

    async def list_targetable_categories(
        self,
        asins: list[str] | None = None,
    ) -> JSONData:
        """
        获取可定向的品类列表
        
        官方端点: GET /sp/targets/categories
        
        Args:
            asins: 可选，要分析的 ASIN 列表（用于获取相关品类）
        
        Returns:
            {
                "categories": [
                    {
                        "id": "category_id",
                        "name": "Category Name",
                        "path": ["Root", "Parent", "Category"],
                        "isTargetable": true
                    }
                ]
            }
        """
        params = {}
        if asins:
            params["asins"] = ",".join(asins)
        
        result = await self.get("/sp/targets/categories", params=params if params else None)
        return result if isinstance(result, dict) else {"categories": []}

    async def get_category_recommendations(
        self,
        asins: list[str],
        max_results: int = 50,
    ) -> JSONData:
        """
        获取品类定向建议
        
        官方端点: POST /sp/targets/categories/recommendations
        
        Args:
            asins: 要分析的 ASIN 列表
            max_results: 最大结果数
        
        Returns:
            {
                "categoryRecommendations": [
                    {
                        "categoryId": "xxx",
                        "categoryName": "Category",
                        "categoryPath": ["..."],
                        "suggestedBid": 1.50
                    }
                ]
            }
        """
        result = await self.post(
            "/sp/targets/categories/recommendations",
            json_data={"asins": asins, "maxResults": max_results}
        )
        return result if isinstance(result, dict) else {"categoryRecommendations": []}

    async def get_category_refinements(
        self,
        category_id: str,
    ) -> JSONData:
        """
        获取品类细化选项
        
        官方端点: GET /sp/targets/category/{categoryId}/refinements
        
        返回可用于细化定向的品牌、价格范围、评分等选项。
        
        Returns:
            {
                "brands": [{"brandId": "...", "brandName": "..."}],
                "priceRanges": [{"min": 0, "max": 50}, ...],
                "reviewRatings": [4, 3, 2, 1]
            }
        """
        result = await self.get(f"/sp/targets/category/{category_id}/refinements")
        return result if isinstance(result, dict) else {}

    async def get_products_count(
        self,
        expressions: JSONList,
    ) -> JSONData:
        """
        获取目标表达式匹配的产品数量
        
        官方端点: POST /sp/targets/products/count
        
        用于评估定向表达式的覆盖范围。
        
        Args:
            expressions: 定向表达式列表
            [
                {
                    "type": "asinCategorySameAs",
                    "value": "1234567890"
                },
                {
                    "type": "asinSameAs",
                    "value": "B00XXXX"
                }
            ]
        
        Returns:
            {
                "counts": [
                    {"expression": {...}, "count": 1234}
                ]
            }
        """
        result = await self.post(
            "/sp/targets/products/count",
            json_data={"expressions": expressions},
            content_type=PRODUCTS_COUNT_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"counts": []}

    async def get_keyword_groups_recommendations(
        self,
        asins: list[str],
        max_results: int = 50,
    ) -> JSONData:
        """
        获取关键词分组推荐
        
        官方端点: POST /sp/targeting/recommendations/keywordGroups
        
        返回基于 ASIN 的关键词分组推荐，用于优化定向策略。
        
        Args:
            asins: 要分析的 ASIN 列表
            max_results: 最大结果数
        
        Returns:
            {
                "keywordGroups": [
                    {
                        "groupId": "xxx",
                        "groupName": "Group Name",
                        "keywords": [
                            {"keyword": "...", "matchType": "BROAD", "suggestedBid": 1.0}
                        ],
                        "theme": "..."
                    }
                ]
            }
        """
        result = await self.post(
            "/sp/targeting/recommendations/keywordGroups",
            json_data={"asins": asins, "maxResults": max_results},
            content_type=KEYWORD_GROUPS_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"keywordGroups": []}

    # ============ Targeting Expression Builder (Utilities) ============

    def build_category_expression(
        self,
        category_id: str,
        brand_ids: list[str] | None = None,
        price_min: float | None = None,
        price_max: float | None = None,
        review_rating: int | None = None,
    ) -> JSONList:
        """
        构建品类定向表达式
        
        这是一个工具方法，帮助构建正确的定向表达式格式。
        
        Args:
            category_id: 品类 ID
            brand_ids: 品牌筛选（来自 refinements）
            price_min/max: 价格范围（来自 refinements）
            review_rating: 最低评分（来自 refinements）
        
        Returns:
            可用于 targets API 的表达式列表
        """
        expression = [{"type": "asinCategorySameAs", "value": category_id}]

        if brand_ids:
            for brand_id in brand_ids:
                expression.append({
                    "type": "asinBrandSameAs",
                    "value": brand_id
                })

        if price_min is not None and price_max is not None:
            expression.append({
                "type": "asinPriceBetween",
                "value": f"{price_min}-{price_max}"
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
            asins: ASIN 列表
            expanded: 是否扩展到相似产品
        """
        expressions = []
        for asin in asins:
            exp_type = "asinExpandedFrom" if expanded else "asinSameAs"
            expressions.append({
                "type": exp_type,
                "value": asin
            })
        return expressions

    # ============ 便捷方法 ============

    async def estimate_category_reach(
        self,
        category_id: str,
        refinements: dict | None = None,
    ) -> int:
        """
        估算品类定向覆盖的产品数量
        
        Args:
            category_id: 品类 ID
            refinements: 可选的细化条件
        """
        expression = self.build_category_expression(
            category_id,
            brand_ids=refinements.get("brand_ids") if refinements else None,
            price_min=refinements.get("price_min") if refinements else None,
            price_max=refinements.get("price_max") if refinements else None,
            review_rating=refinements.get("review_rating") if refinements else None,
        )
        
        result = await self.get_products_count([{"expression": expression}])
        counts = result.get("counts", [])
        return counts[0].get("count", 0) if counts else 0

    async def get_category_with_refinements(
        self,
        category_id: str,
    ) -> JSONData:
        """获取品类信息及其细化选项"""
        refinements = await self.get_category_refinements(category_id)
        return {
            "categoryId": category_id,
            "refinements": refinements,
        }
