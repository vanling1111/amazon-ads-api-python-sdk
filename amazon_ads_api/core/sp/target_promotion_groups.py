"""
Sponsored Products - Target Promotion Groups API (异步版本)
SP目标推广组管理

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod#tag/TargetPromotionGroups
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

# API Content-Type
TARGET_PROMOTION_GROUPS_CONTENT_TYPE = "application/vnd.sptargetpromotiongroups.v1+json"


class SPTargetPromotionGroupsAPI(BaseAdsClient):
    """
    SP Target Promotion Groups API (全异步)
    
    目标推广组允许将多个相关产品组合在一起进行推广。
    """

    async def create_target_promotion_groups(self, groups: JSONList) -> JSONData:
        """
        创建目标推广组
        
        官方端点: POST /sp/targetPromotionGroups
        
        Args:
            groups: [
                {
                    "name": "Summer Products",
                    "campaignId": "xxx",
                    "adGroupId": "xxx",
                    "targets": [
                        {"asin": "B00XXXX1"},
                        {"asin": "B00XXXX2"}
                    ]
                }
            ]
        """
        result = await self.post(
            "/sp/targetPromotionGroups",
            json_data={"targetPromotionGroups": groups},
            content_type=TARGET_PROMOTION_GROUPS_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"targetPromotionGroups": {"success": [], "error": []}}

    async def list_target_promotion_groups(
        self,
        campaign_ids: list[str] | None = None,
        ad_group_ids: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取目标推广组列表
        
        官方端点: POST /sp/targetPromotionGroups/list
        """
        body: JSONData = {"maxResults": max_results}
        if campaign_ids:
            body["campaignIdFilter"] = campaign_ids
        if ad_group_ids:
            body["adGroupIdFilter"] = ad_group_ids
        if next_token:
            body["nextToken"] = next_token

        result = await self.post(
            "/sp/targetPromotionGroups/list",
            json_data=body,
            content_type=TARGET_PROMOTION_GROUPS_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"targetPromotionGroups": []}

    async def get_target_promotion_group_recommendations(
        self,
        asins: list[str],
        max_results: int = 50,
    ) -> JSONData:
        """
        获取目标推广组建议
        
        官方端点: POST /sp/targetPromotionGroups/recommendations
        
        Args:
            asins: 要分析的ASIN列表
            max_results: 最大建议数
        """
        result = await self.post(
            "/sp/targetPromotionGroups/recommendations",
            json_data={"asins": asins, "maxResults": max_results},
            content_type=TARGET_PROMOTION_GROUPS_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"recommendations": []}

    async def create_target_promotion_group_targets(self, targets: JSONList) -> JSONData:
        """
        为推广组创建目标
        
        官方端点: POST /sp/targetPromotionGroups/targets
        
        Args:
            targets: [
                {
                    "targetPromotionGroupId": "xxx",
                    "asin": "B00XXXX",
                    "bid": 1.0
                }
            ]
        """
        result = await self.post(
            "/sp/targetPromotionGroups/targets",
            json_data={"targets": targets},
            content_type=TARGET_PROMOTION_GROUPS_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"targets": {"success": [], "error": []}}

    async def list_target_promotion_group_targets(
        self,
        target_promotion_group_ids: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取推广组目标列表
        
        官方端点: POST /sp/targetPromotionGroups/targets/list
        """
        body: JSONData = {"maxResults": max_results}
        if target_promotion_group_ids:
            body["targetPromotionGroupIdFilter"] = target_promotion_group_ids
        if next_token:
            body["nextToken"] = next_token

        result = await self.post(
            "/sp/targetPromotionGroups/targets/list",
            json_data=body,
            content_type=TARGET_PROMOTION_GROUPS_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"targets": []}

    # ============ 便捷方法 ============

    async def list_all_target_promotion_groups(
        self,
        campaign_ids: list[str] | None = None,
    ) -> JSONList:
        """获取所有目标推广组（自动分页）"""
        all_groups = []
        next_token = None

        while True:
            result = await self.list_target_promotion_groups(
                campaign_ids=campaign_ids,
                max_results=100,
                next_token=next_token
            )
            groups = result.get("targetPromotionGroups", [])
            all_groups.extend(groups)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_groups

