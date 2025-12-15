"""
Sponsored Products - Targeting API (异步版本)
SP产品定向管理（Product Ads + Targets + Negative Targets）
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SPTargetingAPI(BaseAdsClient):
    """SP Targeting API (全异步)"""

    # ============ Product Ads ============

    async def list_product_ads(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        ad_ids: list[str] | None = None,
        state_filter: list[str] | str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取Product Ad列表
        
        Args:
            ad_group_id: Ad Group ID过滤
            campaign_id: Campaign ID过滤
            ad_ids: Product Ad ID过滤
            state_filter: 状态过滤 ["ENABLED", "PAUSED", "ARCHIVED"]
            max_results: 最大结果数
            next_token: 分页token
        """
        params: JSONData = {"maxResults": max_results}
        
        # ID过滤 - 官方格式: {"include": [...]}
        if ad_group_id:
            params["adGroupIdFilter"] = {"include": [ad_group_id]}
        if campaign_id:
            params["campaignIdFilter"] = {"include": [campaign_id]}
        if ad_ids:
            params["adIdFilter"] = {"include": ad_ids}
        
        # 状态过滤
        if state_filter:
            states = [state_filter] if isinstance(state_filter, str) else state_filter
            params["stateFilter"] = {"include": [s.upper() for s in states]}
        
        if next_token:
            params["nextToken"] = next_token

        result = await self.post("/sp/productAds/list", json_data=params, content_type=self.SP_PRODUCT_ADS_V3_CONTENT_TYPE)
        return result if isinstance(result, dict) else {"productAds": []}

    async def get_product_ad(self, ad_id: str) -> JSONData:
        """获取单个Product Ad详情"""
        result = await self.get(f"/sp/productAds/{ad_id}")
        return result if isinstance(result, dict) else {}

    async def create_product_ads(self, product_ads: JSONList) -> JSONData:
        """
        批量创建Product Ad
        
        Args:
            product_ads: [
                {
                    "campaignId": "xxx",
                    "adGroupId": "xxx",
                    "state": "enabled",
                    "sku": "SKU123"  # Seller用SKU
                    # 或 "asin": "B00XXXX"  # Vendor用ASIN
                }
            ]
        """
        result = await self.post(
            "/sp/productAds", 
            json_data={"productAds": product_ads},
            content_type=self.SP_PRODUCT_ADS_V3_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"productAds": {"success": [], "error": []}}

    async def update_product_ads(self, product_ads: JSONList) -> JSONData:
        """批量更新Product Ad"""
        result = await self.put(
            "/sp/productAds", 
            json_data={"productAds": product_ads},
            content_type=self.SP_PRODUCT_ADS_V3_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"productAds": {"success": [], "error": []}}

    async def delete_product_ads(self, ad_ids: list[str]) -> JSONData:
        """
        批量归档Product Ad（官方 v3 /delete 端点）
        
        注意：Amazon Ads 不支持真正删除广告实体，此操作将 Product Ad 状态设置为 "archived"。
        
        Args:
            ad_ids: Product Ad ID列表
        """
        # 官方请求格式: {"adIdFilter": {"include": [...]}}
        body = {"adIdFilter": {"include": ad_ids}}
        result = await self.post(
            "/sp/productAds/delete", 
            json_data=body,
            content_type=self.SP_PRODUCT_ADS_V3_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"productAds": {"success": [], "error": []}}

    async def delete_product_ad(self, ad_id: str) -> JSONData:
        """归档单个Product Ad（状态变为 archived）"""
        return await self.delete_product_ads([ad_id])

    # ============ Targets (Product Targeting) ============

    # SP Targeting API v3 Content-Types
    SP_TARGETING_V3_CONTENT_TYPE = "application/vnd.spTargetingClause.v3+json"
    SP_NEG_TARGETING_V3_CONTENT_TYPE = "application/vnd.spNegativeTargetingClause.v3+json"
    SP_PRODUCT_ADS_V3_CONTENT_TYPE = "application/vnd.spProductAd.v3+json"

    async def list_targets(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        target_ids: list[str] | None = None,
        state_filter: list[str] | str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取Target列表 (v3 API)
        
        Args:
            ad_group_id: Ad Group ID过滤
            campaign_id: Campaign ID过滤
            target_ids: Target ID过滤
            state_filter: 状态过滤 ["ENABLED", "PAUSED", "ARCHIVED"]
            max_results: 最大结果数
            next_token: 分页token
        """
        params: JSONData = {"maxResults": max_results}
        
        # ID过滤 - 官方格式: {"include": [...]}
        if ad_group_id:
            params["adGroupIdFilter"] = {"include": [ad_group_id]}
        if campaign_id:
            params["campaignIdFilter"] = {"include": [campaign_id]}
        if target_ids:
            params["targetIdFilter"] = {"include": target_ids}
        
        # 状态过滤
        if state_filter:
            states = [state_filter] if isinstance(state_filter, str) else state_filter
            params["stateFilter"] = {"include": [s.upper() for s in states]}
        
        if next_token:
            params["nextToken"] = next_token

        result = await self.post(
            "/sp/targets/list", 
            json_data=params,
            content_type=self.SP_TARGETING_V3_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"targetingClauses": []}

    async def get_target(self, target_id: str) -> JSONData:
        """获取单个Target详情"""
        result = await self.get(f"/sp/targets/{target_id}")
        return result if isinstance(result, dict) else {}

    async def create_targets(self, targets: JSONList) -> JSONData:
        """
        批量创建Target
        
        Args:
            targets: [
                {
                    "campaignId": "xxx",
                    "adGroupId": "xxx",
                    "state": "enabled",
                    "expression": [
                        {"type": "asinSameAs", "value": "B00XXXX"}
                    ],
                    "expressionType": "manual",
                    "bid": 1.0
                }
            ]
        """
        result = await self.post(
            "/sp/targets", 
            json_data={"targetingClauses": targets},
            content_type=self.SP_TARGETING_V3_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"targetingClauses": {"success": [], "error": []}}

    async def update_targets(self, targets: JSONList) -> JSONData:
        """
        批量更新Target
        
        Args:
            targets: [{"targetId": "xxx", "state": "paused", "bid": 1.5}]
        """
        result = await self.put(
            "/sp/targets", 
            json_data={"targetingClauses": targets},
            content_type=self.SP_TARGETING_V3_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"targetingClauses": {"success": [], "error": []}}

    async def delete_targets(self, target_ids: list[str]) -> JSONData:
        """
        批量归档Target（官方 v3 /delete 端点）
        
        注意：Amazon Ads 不支持真正删除广告实体，此操作将 Target 状态设置为 "archived"。
        
        Args:
            target_ids: Target ID列表
        """
        # 官方请求格式: {"targetIdFilter": {"include": [...]}}
        body = {"targetIdFilter": {"include": target_ids}}
        result = await self.post(
            "/sp/targets/delete", 
            json_data=body,
            content_type=self.SP_TARGETING_V3_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"targetingClauses": {"success": [], "error": []}}

    async def delete_target(self, target_id: str) -> JSONData:
        """归档单个Target（状态变为 archived）"""
        return await self.delete_targets([target_id])

    # ============ 便捷方法 ============

    async def update_target_bid(self, target_id: str, bid: float) -> JSONData:
        """更新Target竞价"""
        return await self.update_targets([{"targetId": target_id, "bid": bid}])

    async def batch_update_target_bids(self, bid_updates: list[dict]) -> JSONData:
        """
        批量更新Target竞价
        
        Args:
            bid_updates: [{"targetId": "xxx", "bid": 1.5}, ...]
        """
        return await self.update_targets(bid_updates)

    # ============ Negative Targets (Ad Group级别) ============

    async def list_negative_targets(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        target_ids: list[str] | None = None,
        state_filter: list[str] | str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取Ad Group级别Negative Target列表 (v3 API)
        
        Args:
            ad_group_id: Ad Group ID过滤
            campaign_id: Campaign ID过滤
            target_ids: Target ID过滤
            state_filter: 状态过滤 ["ENABLED", "ARCHIVED"]
            max_results: 最大结果数
            next_token: 分页token
        """
        params: JSONData = {"maxResults": max_results}
        
        # ID过滤 - 官方格式: {"include": [...]}
        if ad_group_id:
            params["adGroupIdFilter"] = {"include": [ad_group_id]}
        if campaign_id:
            params["campaignIdFilter"] = {"include": [campaign_id]}
        if target_ids:
            params["targetIdFilter"] = {"include": target_ids}
        
        # 状态过滤
        if state_filter:
            states = [state_filter] if isinstance(state_filter, str) else state_filter
            params["stateFilter"] = {"include": [s.upper() for s in states]}
        
        if next_token:
            params["nextToken"] = next_token

        result = await self.post(
            "/sp/negativeTargets/list", 
            json_data=params,
            content_type=self.SP_NEG_TARGETING_V3_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"negativeTargetingClauses": []}

    async def create_negative_targets(self, targets: JSONList) -> JSONData:
        """
        批量创建Negative Target
        
        官方端点: POST /sp/negativeTargets
        
        Args:
            targets: [
                {
                    "campaignId": "xxx",
                    "adGroupId": "xxx",
                    "state": "enabled",
                    "expression": [
                        {"type": "asinSameAs", "value": "B00XXXX"}
                    ],
                    "expressionType": "manual"
                }
            ]
        """
        result = await self.post(
            "/sp/negativeTargets", 
            json_data={"negativeTargetingClauses": targets},
            content_type=self.SP_NEG_TARGETING_V3_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"negativeTargetingClauses": {"success": [], "error": []}}

    async def update_negative_targets(self, targets: JSONList) -> JSONData:
        """
        批量更新Negative Target
        
        官方端点: PUT /sp/negativeTargets
        
        Args:
            targets: [{"targetId": "xxx", "state": "paused"}]
        """
        result = await self.put(
            "/sp/negativeTargets", 
            json_data={"negativeTargetingClauses": targets},
            content_type=self.SP_NEG_TARGETING_V3_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"negativeTargetingClauses": {"success": [], "error": []}}

    async def get_negative_target_brand_recommendations(self) -> JSONData:
        """
        获取Negative Target品牌推荐
        
        官方端点: GET /sp/negativeTargets/brands/recommendations
        """
        result = await self.get(
            "/sp/negativeTargets/brands/recommendations",
            content_type=self.SP_NEG_TARGETING_V3_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"brands": []}

    async def search_negative_target_brands(
        self,
        keyword: str,
        max_results: int = 50,
    ) -> JSONData:
        """
        搜索可用于Negative Target的品牌
        
        官方端点: POST /sp/negativeTargets/brands/search
        
        Args:
            keyword: 搜索关键词
            max_results: 最大结果数
        """
        result = await self.post(
            "/sp/negativeTargets/brands/search",
            json_data={"keyword": keyword, "maxResults": max_results},
            content_type=self.SP_NEG_TARGETING_V3_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"brands": []}

    async def delete_negative_targets(self, target_ids: list[str]) -> JSONData:
        """
        批量归档Negative Target（官方 v3 /delete 端点）
        
        注意：此操作将 Negative Target 状态设置为 "archived"。
        
        Args:
            target_ids: Negative Target ID列表
        """
        # 官方请求格式: {"targetIdFilter": {"include": [...]}}
        body = {"targetIdFilter": {"include": target_ids}}
        result = await self.post(
            "/sp/negativeTargets/delete", 
            json_data=body,
            content_type=self.SP_NEG_TARGETING_V3_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"negativeTargetingClauses": {"success": [], "error": []}}

    async def delete_negative_target(self, target_id: str) -> JSONData:
        """归档单个Negative Target（状态变为 archived）"""
        return await self.delete_negative_targets([target_id])

    # ============ Campaign Negative Targets ============

    async def list_campaign_negative_targets(
        self,
        campaign_id: str | None = None,
        target_ids: list[str] | None = None,
        state_filter: list[str] | str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取Campaign级别Negative Target列表
        
        Args:
            campaign_id: Campaign ID过滤
            target_ids: Target ID过滤
            state_filter: 状态过滤 ["ENABLED", "ARCHIVED"]
            max_results: 最大结果数
            next_token: 分页token
        """
        params: JSONData = {"maxResults": max_results}
        
        # ID过滤 - 官方格式: {"include": [...]}
        if campaign_id:
            params["campaignIdFilter"] = {"include": [campaign_id]}
        if target_ids:
            params["targetIdFilter"] = {"include": target_ids}
        
        # 状态过滤
        if state_filter:
            states = [state_filter] if isinstance(state_filter, str) else state_filter
            params["stateFilter"] = {"include": [s.upper() for s in states]}
        
        if next_token:
            params["nextToken"] = next_token

        result = await self.post(
            "/sp/campaignNegativeTargets/list", 
            json_data=params,
            content_type=self.SP_CAMPAIGN_NEG_TARGETING_V3_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"campaignNegativeTargetingClauses": []}

    # Campaign Negative Targets Content-Type
    SP_CAMPAIGN_NEG_TARGETING_V3_CONTENT_TYPE = "application/vnd.spCampaignNegativeTargetingClause.v3+json"

    async def create_campaign_negative_targets(self, targets: JSONList) -> JSONData:
        """
        批量创建Campaign Negative Target
        
        官方端点: POST /sp/campaignNegativeTargets
        """
        result = await self.post(
            "/sp/campaignNegativeTargets", 
            json_data={"campaignNegativeTargetingClauses": targets},
            content_type=self.SP_CAMPAIGN_NEG_TARGETING_V3_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"campaignNegativeTargetingClauses": {"success": [], "error": []}}

    async def update_campaign_negative_targets(self, targets: JSONList) -> JSONData:
        """
        批量更新Campaign Negative Target
        
        官方端点: PUT /sp/campaignNegativeTargets
        
        Args:
            targets: [{"targetId": "xxx", "state": "paused"}]
        """
        result = await self.put(
            "/sp/campaignNegativeTargets", 
            json_data={"campaignNegativeTargetingClauses": targets},
            content_type=self.SP_CAMPAIGN_NEG_TARGETING_V3_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"campaignNegativeTargetingClauses": {"success": [], "error": []}}

    async def delete_campaign_negative_targets(self, target_ids: list[str]) -> JSONData:
        """
        批量归档Campaign Negative Target
        
        官方端点: POST /sp/campaignNegativeTargets/delete
        官方请求格式: {"targetIdFilter": {"include": [...]}}
        """
        result = await self.post(
            "/sp/campaignNegativeTargets/delete",
            json_data={"targetIdFilter": {"include": target_ids}},
            content_type=self.SP_CAMPAIGN_NEG_TARGETING_V3_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"campaignNegativeTargetingClauses": {"success": [], "error": []}}

    async def delete_campaign_negative_target(self, target_id: str) -> JSONData:
        """归档单个Campaign Negative Target"""
        return await self.delete_campaign_negative_targets([target_id])

    # ============ 批量获取 ============

    async def list_all_targets(
        self,
        campaign_id: str | None = None,
        ad_group_id: str | None = None,
        state_filter: str | None = None,
    ) -> JSONList:
        """获取所有Target（自动分页）"""
        all_targets = []
        next_token = None

        while True:
            result = await self.list_targets(
                campaign_id=campaign_id,
                ad_group_id=ad_group_id,
                state_filter=state_filter,
                max_results=100,
                next_token=next_token,
            )
            targets = result.get("targetingClauses", [])
            all_targets.extend(targets)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_targets
