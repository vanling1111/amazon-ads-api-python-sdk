"""
Sponsored Products - Targeting API (异步版本)
SP产品定向管理（Product Ads + Targets + Negative Targets）
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SPTargetingAPI(BaseAdsClient):
    """SP Targeting API (全异步)"""

    # ============ Product Ads ============

    async def list_product_ads(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        state_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取Product Ad列表"""
        params: JSONData = {"maxResults": max_results}
        if ad_group_id:
            params["adGroupIdFilter"] = [ad_group_id]
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]
        if state_filter:
            params["stateFilter"] = state_filter
        if next_token:
            params["nextToken"] = next_token

        result = await self.post("/sp/productAds/list", json_data=params)
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
        result = await self.post("/sp/productAds", json_data={"productAds": product_ads})
        return result if isinstance(result, dict) else {"productAds": {"success": [], "error": []}}

    async def update_product_ads(self, product_ads: JSONList) -> JSONData:
        """批量更新Product Ad"""
        result = await self.put("/sp/productAds", json_data={"productAds": product_ads})
        return result if isinstance(result, dict) else {"productAds": {"success": [], "error": []}}

    async def delete_product_ad(self, ad_id: str) -> JSONData:
        """归档Product Ad"""
        return await self.delete(f"/sp/productAds/{ad_id}")

    # ============ Targets (Product Targeting) ============

    async def list_targets(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        state_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取Target列表"""
        params: JSONData = {"maxResults": max_results}
        if ad_group_id:
            params["adGroupIdFilter"] = [ad_group_id]
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]
        if state_filter:
            params["stateFilter"] = state_filter
        if next_token:
            params["nextToken"] = next_token

        result = await self.post("/sp/targets/list", json_data=params)
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
        result = await self.post("/sp/targets", json_data={"targetingClauses": targets})
        return result if isinstance(result, dict) else {"targetingClauses": {"success": [], "error": []}}

    async def update_targets(self, targets: JSONList) -> JSONData:
        """
        批量更新Target
        
        Args:
            targets: [{"targetId": "xxx", "state": "paused", "bid": 1.5}]
        """
        result = await self.put("/sp/targets", json_data={"targetingClauses": targets})
        return result if isinstance(result, dict) else {"targetingClauses": {"success": [], "error": []}}

    async def delete_target(self, target_id: str) -> JSONData:
        """归档Target"""
        return await self.delete(f"/sp/targets/{target_id}")

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
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取Ad Group级别Negative Target列表"""
        params: JSONData = {"maxResults": max_results}
        if ad_group_id:
            params["adGroupIdFilter"] = [ad_group_id]
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]
        if next_token:
            params["nextToken"] = next_token

        result = await self.post("/sp/negativeTargets/list", json_data=params)
        return result if isinstance(result, dict) else {"negativeTargetingClauses": []}

    async def create_negative_targets(self, targets: JSONList) -> JSONData:
        """
        批量创建Negative Target
        
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
        result = await self.post("/sp/negativeTargets", json_data={"negativeTargetingClauses": targets})
        return result if isinstance(result, dict) else {"negativeTargetingClauses": {"success": [], "error": []}}

    async def delete_negative_target(self, target_id: str) -> JSONData:
        """删除Negative Target"""
        return await self.delete(f"/sp/negativeTargets/{target_id}")

    # ============ Campaign Negative Targets ============

    async def list_campaign_negative_targets(
        self,
        campaign_id: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取Campaign级别Negative Target列表"""
        params: JSONData = {"maxResults": max_results}
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]
        if next_token:
            params["nextToken"] = next_token

        result = await self.post("/sp/campaignNegativeTargets/list", json_data=params)
        return result if isinstance(result, dict) else {"campaignNegativeTargetingClauses": []}

    async def create_campaign_negative_targets(self, targets: JSONList) -> JSONData:
        """批量创建Campaign Negative Target"""
        result = await self.post("/sp/campaignNegativeTargets", json_data={"campaignNegativeTargetingClauses": targets})
        return result if isinstance(result, dict) else {"campaignNegativeTargetingClauses": {"success": [], "error": []}}

    async def delete_campaign_negative_target(self, target_id: str) -> JSONData:
        """删除Campaign Negative Target"""
        return await self.delete(f"/sp/campaignNegativeTargets/{target_id}")

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
