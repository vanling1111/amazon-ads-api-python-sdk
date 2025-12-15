"""
Sponsored Products - Global Recommendations API (异步版本)
全局推荐（跨账号）

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

# API Content-Type
GLOBAL_BID_RECOMMENDATIONS_CONTENT_TYPE = "application/vnd.spglobaltargetbidrecommendation.v1+json"
GLOBAL_KEYWORD_RECOMMENDATIONS_CONTENT_TYPE = "application/vnd.spglobalkeywordrecommendation.v1+json"


class SPGlobalRecommendationsAPI(BaseAdsClient):
    """
    SP Global Recommendations API (全异步)
    
    提供跨账号的全局推荐，无需特定Campaign/AdGroup。
    """

    async def get_global_bid_recommendations(
        self,
        targets: JSONList,
        marketplace_id: str,
    ) -> JSONData:
        """
        获取全局目标竞价建议
        
        官方端点: POST /sp/global/targets/bid/recommendations
        
        该端点允许在没有Campaign的情况下获取目标竞价建议。
        适用于前期规划和竞价评估。
        
        Args:
            targets: [
                {
                    "targetingExpression": {
                        "type": "asinCategorySameAs",
                        "value": "1234567890"
                    }
                }
            ]
            marketplace_id: 市场ID (如 "ATVPDKIKX0DER" for US)
        """
        result = await self.post(
            "/sp/global/targets/bid/recommendations",
            json_data={
                "targets": targets,
                "marketplaceId": marketplace_id
            },
            content_type=GLOBAL_BID_RECOMMENDATIONS_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"bidRecommendations": []}

    async def list_global_keyword_recommendations(
        self,
        asins: list[str],
        marketplace_id: str,
        keyword_types: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取全局关键词推荐列表
        
        官方端点: POST /sp/global/targets/keywords/recommendations/list
        
        该端点允许在没有Campaign的情况下获取关键词推荐。
        适用于前期规划和关键词研究。
        
        Args:
            asins: 要分析的ASIN列表
            marketplace_id: 市场ID
            keyword_types: 关键词类型过滤 ["KEYWORD", "PRODUCT_TARGETING"]
            max_results: 最大结果数 (默认100, 最大500)
            next_token: 分页Token
        """
        body: JSONData = {
            "asins": asins,
            "marketplaceId": marketplace_id,
            "maxResults": max_results
        }
        if keyword_types:
            body["keywordTypes"] = keyword_types
        if next_token:
            body["nextToken"] = next_token

        result = await self.post(
            "/sp/global/targets/keywords/recommendations/list",
            json_data=body,
            content_type=GLOBAL_KEYWORD_RECOMMENDATIONS_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"keywordRecommendations": []}

    # ============ 便捷方法 ============

    async def list_all_global_keyword_recommendations(
        self,
        asins: list[str],
        marketplace_id: str,
    ) -> JSONList:
        """获取所有全局关键词推荐（自动分页）"""
        all_recommendations = []
        next_token = None

        while True:
            result = await self.list_global_keyword_recommendations(
                asins=asins,
                marketplace_id=marketplace_id,
                max_results=500,
                next_token=next_token
            )
            recommendations = result.get("keywordRecommendations", [])
            all_recommendations.extend(recommendations)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_recommendations

    async def get_bid_recommendation_for_category(
        self,
        category_id: str,
        marketplace_id: str,
    ) -> JSONData:
        """
        获取特定类目的竞价建议
        
        便捷方法，封装了 get_global_bid_recommendations
        """
        targets = [
            {
                "targetingExpression": {
                    "type": "asinCategorySameAs",
                    "value": category_id
                }
            }
        ]
        return await self.get_global_bid_recommendations(targets, marketplace_id)

    async def get_bid_recommendation_for_asin(
        self,
        asin: str,
        marketplace_id: str,
    ) -> JSONData:
        """
        获取特定ASIN的竞价建议
        
        便捷方法，封装了 get_global_bid_recommendations
        """
        targets = [
            {
                "targetingExpression": {
                    "type": "asinSameAs",
                    "value": asin
                }
            }
        ]
        return await self.get_global_bid_recommendations(targets, marketplace_id)

