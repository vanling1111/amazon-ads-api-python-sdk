"""
Amazon Ads Recommendations API

官方文档: https://advertising.amazon.com/API/docs
OpenAPI规范: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Recommendations_prod_3p.json

官方端点 (共3个):
- POST /recommendations/apply - 应用推荐
- POST /recommendations/list - 列出推荐  
- PUT /recommendations/{recommendationId} - 更新推荐
"""

from typing import Literal
from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


# Content-Type 常量
APPLY_REQ_CONTENT_TYPE = "application/vnd.applyRecommendationsRequest.v1+json"
APPLY_RESP_CONTENT_TYPE = "application/vnd.applyRecommendationsResponse.v1+json"
LIST_REQ_CONTENT_TYPE = "application/vnd.listRecommendationsRequest.v1+json"
LIST_RESP_CONTENT_TYPE = "application/vnd.listRecommendationsResponse.v1+json"
UPDATE_REQ_CONTENT_TYPE = "application/vnd.updateRecommendationRequest.v1+json"
UPDATE_RESP_CONTENT_TYPE = "application/vnd.recommendation.v1+json"


# 推荐类型枚举
RecommendationType = Literal[
    "NEW_CAMPAIGN", "NEW_VIDEO_CAMPAIGN", "NEW_AD_GROUP",
    "CAMPAIGN_BIDDING_STRATEGY", "CAMPAIGN_BUDGET", "CAMPAIGN_END_DATE",
    "CAMPAIGN_TOP_PLACEMENT", "CAMPAIGN_PRODUCT_PLACEMENT", "CAMPAIGN_STATE",
    "NEW_CAMPAIGN_BIDDING_RULE", "CAMPAIGN_BIDDING_RULE",
    "NEW_CAMPAIGN_BUDGET_RULE", "CAMPAIGN_BUDGET_RULE",
    "AD_GROUP_STATE", "AD_GROUP_DEFAULT_BID", "AD_GROUP_BID_OPTIMIZATION",
    "NEW_KEYWORD", "KEYWORD_BID", "KEYWORD_STATE",
    "NEW_NEGATIVE_KEYWORD", "NEGATIVE_KEYWORD_STATE",
    "NEW_PRODUCT_AD", "PRODUCT_AD_STATE",
    "NEW_PRODUCT_TARGETING", "PRODUCT_TARGETING_STATE", "PRODUCT_TARGETING_BID",
    "NEW_NEGATIVE_PRODUCT_TARGETING", "NEGATIVE_PRODUCT_TARGETING_STATE",
    "NEW_AUDIENCE_TARGETING", "AUDIENCE_TARGETING_STATE", "AUDIENCE_TARGETING_BID",
    "NEW_NEGATIVE_AUDIENCE_TARGETING", "NEGATIVE_AUDIENCE_TARGETING_STATE",
]

# 广告产品枚举
AdProduct = Literal["SP", "SB", "SD", "ST"]

# 状态枚举
RecommendationStatus = Literal[
    "PUBLISHED", "APPLY_IN_PROGRESS", "APPLY_SUCCESS", "APPLY_FAILED", "REJECTED"
]


class RecommendationsAPI(BaseAdsClient):
    """
    Recommendations API
    
    官方端点 (共3个):
    - POST /recommendations/apply
    - POST /recommendations/list
    - PUT /recommendations/{recommendationId}
    """

    async def list_recommendations(
        self,
        filters: list[dict] | None = None,
        locale: str | None = None,
        max_results: int = 500,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取推荐列表
        
        官方端点: POST /recommendations/list
        
        Args:
            filters: 过滤条件列表，每个过滤器包含:
                - field: 过滤字段 (AD_PRODUCT, CAMPAIGN_ID, RECOMMENDATION_TYPE, STATUS, GROUPING_TYPE)
                - operator: 操作符 (EXACT)
                - values: 值列表
                - include: 是否包含 (默认True)
            locale: 语言代码 (如 "en_US", "zh_CN")
            max_results: 最大结果数 (1-500，默认500)
            next_token: 分页token
            
        Returns:
            {
                "recommendations": [...],
                "totalResults": int,
                "nextToken": str | None
            }
        """
        body: dict = {"maxResults": max_results}
        
        if filters:
            body["filters"] = filters
        if locale:
            body["locale"] = locale
        if next_token:
            body["nextToken"] = next_token
        
        result = await self.post(
            "/recommendations/list",
            json_data=body,
            content_type=LIST_REQ_CONTENT_TYPE,
            accept=LIST_RESP_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    async def apply_recommendations(
        self,
        recommendation_ids: list[str],
    ) -> JSONData:
        """
        应用一个或多个推荐
        
        官方端点: POST /recommendations/apply
        
        Args:
            recommendation_ids: 推荐ID列表 (1-100个)
            
        Returns:
            {
                "successes": [
                    {
                        "index": int,
                        "recommendationId": str,
                        "recommendation": {...},
                        "success": {"code": str, "message": str}
                    }
                ],
                "failures": [
                    {
                        "index": int,
                        "recommendationId": str,
                        "error": {"code": str, "message": str}
                    }
                ]
            }
        """
        if not recommendation_ids or len(recommendation_ids) > 100:
            raise ValueError("recommendation_ids must have 1-100 items")
        
        result = await self.post(
            "/recommendations/apply",
            json_data={"recommendationIds": recommendation_ids},
            content_type=APPLY_REQ_CONTENT_TYPE,
            accept=APPLY_RESP_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    async def update_recommendation(
        self,
        recommendation_id: str,
        recommended_value: str | None = None,
        budget_rule: dict | None = None,
        rule_based_bidding: dict | None = None,
    ) -> JSONData:
        """
        更新推荐
        
        官方端点: PUT /recommendations/{recommendationId}
        
        Args:
            recommendation_id: 推荐ID
            recommended_value: 新的推荐值 (根据推荐类型不同，类型不同)
            budget_rule: 预算规则更新 (用于 NEW_CAMPAIGN_BUDGET_RULE, CAMPAIGN_BUDGET_RULE)
            rule_based_bidding: 规则出价更新 (用于 NEW_CAMPAIGN_BIDDING_RULE, CAMPAIGN_BIDDING_RULE)
            
        Returns:
            更新后的推荐对象
        """
        body: dict = {}
        
        if recommended_value is not None:
            body["recommendedValue"] = recommended_value
        if budget_rule:
            body["budgetRule"] = budget_rule
        if rule_based_bidding:
            body["ruleBasedBidding"] = rule_based_bidding
        
        result = await self.put(
            f"/recommendations/{recommendation_id}",
            json_data=body,
            content_type=UPDATE_REQ_CONTENT_TYPE,
            accept=UPDATE_RESP_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def get_all_recommendations(
        self,
        ad_product: AdProduct | None = None,
        recommendation_type: RecommendationType | None = None,
        status: RecommendationStatus | None = None,
        campaign_id: str | None = None,
        max_pages: int = 10,
    ) -> list[JSONData]:
        """
        获取所有推荐（自动分页）
        
        Args:
            ad_product: 广告产品过滤 (SP, SB, SD, ST)
            recommendation_type: 推荐类型过滤
            status: 状态过滤
            campaign_id: Campaign ID过滤
            max_pages: 最大页数限制
            
        Returns:
            所有推荐列表
        """
        filters = []
        
        if ad_product:
            filters.append({
                "field": "AD_PRODUCT",
                "operator": "EXACT",
                "values": [ad_product],
            })
        if recommendation_type:
            filters.append({
                "field": "RECOMMENDATION_TYPE",
                "operator": "EXACT",
                "values": [recommendation_type],
            })
        if status:
            filters.append({
                "field": "STATUS",
                "operator": "EXACT",
                "values": [status],
            })
        if campaign_id:
            filters.append({
                "field": "CAMPAIGN_ID",
                "operator": "EXACT",
                "values": [campaign_id],
            })
        
        all_recommendations = []
        next_token = None
        
        for _ in range(max_pages):
            result = await self.list_recommendations(
                filters=filters if filters else None,
                max_results=500,
                next_token=next_token,
            )
            
            recommendations = result.get("recommendations", [])
            all_recommendations.extend(recommendations)
            
            next_token = result.get("nextToken")
            if not next_token:
                break
        
        return all_recommendations

    async def apply_and_check(
        self,
        recommendation_ids: list[str],
    ) -> tuple[list[str], list[str]]:
        """
        应用推荐并返回成功/失败的ID
        
        Args:
            recommendation_ids: 推荐ID列表
            
        Returns:
            (成功的ID列表, 失败的ID列表)
        """
        result = await self.apply_recommendations(recommendation_ids)
        
        success_ids = [
            s.get("recommendationId", "")
            for s in result.get("successes", [])
        ]
        failure_ids = [
            f.get("recommendationId", "")
            for f in result.get("failures", [])
        ]
        
        return success_ids, failure_ids

