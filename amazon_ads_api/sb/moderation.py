"""
Sponsored Brands - Moderation API (异步版本)
SB广告审核管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SBModerationAPI(BaseAdsClient):
    """SB Moderation API (全异步)"""

    # ============ Ad Moderation ============

    async def get_ad_moderation_status(self, ad_id: str) -> JSONData:
        """获取广告审核状态"""
        result = await self.get(f"/sb/moderation/ads/{ad_id}")
        return result if isinstance(result, dict) else {}

    async def get_batch_ad_moderation_status(
        self,
        ad_ids: list[str],
    ) -> JSONList:
        """批量获取广告审核状态"""
        result = await self.post("/sb/moderation/ads/batch", json_data={
            "adIds": ad_ids
        })
        return result if isinstance(result, list) else []

    async def submit_ad_for_moderation(self, ad_id: str) -> JSONData:
        """提交广告审核"""
        result = await self.post(f"/sb/moderation/ads/{ad_id}/submit")
        return result if isinstance(result, dict) else {}

    async def request_ad_moderation_review(
        self,
        ad_id: str,
        comments: str | None = None,
    ) -> JSONData:
        """请求重新审核被拒绝的广告"""
        body: JSONData = {}
        if comments:
            body["comments"] = comments

        result = await self.post(f"/sb/moderation/ads/{ad_id}/review", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ Creative Moderation ============

    async def get_creative_moderation_status(self, creative_id: str) -> JSONData:
        """获取创意审核状态"""
        result = await self.get(f"/sb/moderation/creatives/{creative_id}")
        return result if isinstance(result, dict) else {}

    async def get_creative_policy_violations(self, creative_id: str) -> JSONList:
        """获取创意违规详情"""
        result = await self.get(f"/sb/moderation/creatives/{creative_id}/violations")
        return result if isinstance(result, list) else []

    async def get_creative_recommendations(self, creative_id: str) -> JSONData:
        """获取创意改进建议"""
        result = await self.get(f"/sb/moderation/creatives/{creative_id}/recommendations")
        return result if isinstance(result, dict) else {}

    # ============ Headline Moderation ============

    async def validate_headline(
        self,
        headline: str,
        brand_entity_id: str | None = None,
    ) -> JSONData:
        """验证标题是否符合政策"""
        body: JSONData = {"headline": headline}
        if brand_entity_id:
            body["brandEntityId"] = brand_entity_id

        result = await self.post("/sb/moderation/headlines/validate", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_headline_suggestions(
        self,
        rejected_headline: str,
        brand_entity_id: str | None = None,
    ) -> JSONList:
        """获取被拒标题的改进建议"""
        body: JSONData = {"headline": rejected_headline}
        if brand_entity_id:
            body["brandEntityId"] = brand_entity_id

        result = await self.post("/sb/moderation/headlines/suggestions", json_data=body)
        return result if isinstance(result, list) else []

    # ============ Image Moderation ============

    async def validate_image(
        self,
        image_asset_id: str,
        image_type: str = "CUSTOM_IMAGE",
    ) -> JSONData:
        """验证图片是否符合政策"""
        result = await self.post("/sb/moderation/images/validate", json_data={
            "imageAssetId": image_asset_id,
            "imageType": image_type,
        })
        return result if isinstance(result, dict) else {}

    async def get_image_requirements(
        self,
        image_type: str = "CUSTOM_IMAGE",
    ) -> JSONData:
        """获取图片规格要求"""
        result = await self.get(f"/sb/moderation/images/requirements/{image_type}")
        return result if isinstance(result, dict) else {}

    # ============ Video Moderation ============

    async def validate_video(
        self,
        video_asset_id: str,
    ) -> JSONData:
        """验证视频是否符合政策"""
        result = await self.post("/sb/moderation/videos/validate", json_data={
            "videoAssetId": video_asset_id,
        })
        return result if isinstance(result, dict) else {}

    async def get_video_requirements(self) -> JSONData:
        """获取视频规格要求"""
        result = await self.get("/sb/moderation/videos/requirements")
        return result if isinstance(result, dict) else {}

    # ============ Landing Page Moderation ============

    async def validate_landing_page(
        self,
        landing_page_url: str,
    ) -> JSONData:
        """验证落地页是否符合政策"""
        result = await self.post("/sb/moderation/landingPages/validate", json_data={
            "landingPageUrl": landing_page_url,
        })
        return result if isinstance(result, dict) else {}

    async def get_landing_page_requirements(self) -> JSONData:
        """获取落地页要求"""
        result = await self.get("/sb/moderation/landingPages/requirements")
        return result if isinstance(result, dict) else {}

    # ============ Store Moderation ============

    async def get_store_moderation_status(self, store_id: str) -> JSONData:
        """获取旗舰店审核状态"""
        result = await self.get(f"/sb/moderation/stores/{store_id}")
        return result if isinstance(result, dict) else {}

    async def validate_store_page(
        self,
        store_page_url: str,
    ) -> JSONData:
        """验证旗舰店页面"""
        result = await self.post("/sb/moderation/stores/validate", json_data={
            "storePageUrl": store_page_url,
        })
        return result if isinstance(result, dict) else {}

    # ============ Policy Information ============

    async def get_advertising_policies(
        self,
        policy_type: str | None = None,
    ) -> JSONList:
        """获取广告政策列表"""
        params = {}
        if policy_type:
            params["policyType"] = policy_type

        result = await self.get("/sb/moderation/policies", params=params or None)
        return result if isinstance(result, list) else []

    async def get_restricted_content(
        self,
        category: str | None = None,
    ) -> JSONList:
        """获取受限内容列表"""
        params = {}
        if category:
            params["category"] = category

        result = await self.get("/sb/moderation/restrictedContent", params=params or None)
        return result if isinstance(result, list) else []

    async def get_prohibited_claims(self) -> JSONList:
        """获取禁止使用的声明"""
        result = await self.get("/sb/moderation/prohibitedClaims")
        return result if isinstance(result, list) else []

    # ============ Moderation History ============

    async def get_moderation_history(
        self,
        ad_id: str,
        max_results: int = 50,
    ) -> JSONList:
        """获取广告审核历史"""
        result = await self.get(f"/sb/moderation/ads/{ad_id}/history", params={
            "maxResults": max_results
        })
        return result if isinstance(result, list) else []

    # ============ 便捷方法 ============

    async def get_pending_moderation_ads(self) -> JSONList:
        """获取待审核的广告"""
        ads_result = await self.get("/sb/v4/ads", params={"maxResults": 100})
        ads = ads_result.get("ads", []) if isinstance(ads_result, dict) else []

        pending = []
        for ad in ads:
            ad_id = ad.get("adId")
            if not ad_id:
                continue

            moderation = await self.get_ad_moderation_status(ad_id)
            if moderation.get("moderationStatus") == "PENDING":
                pending.append({**ad, "moderation": moderation})

        return pending

    async def get_rejected_ads_with_reasons(self) -> JSONList:
        """获取被拒绝的广告及原因"""
        ads_result = await self.get("/sb/v4/ads", params={"maxResults": 100})
        ads = ads_result.get("ads", []) if isinstance(ads_result, dict) else []

        rejected = []
        for ad in ads:
            ad_id = ad.get("adId")
            if not ad_id:
                continue

            moderation = await self.get_ad_moderation_status(ad_id)
            if moderation.get("moderationStatus") == "REJECTED":
                rejected.append({
                    **ad,
                    "moderation": moderation,
                    "reasons": moderation.get("moderationReasons", []),
                })

        return rejected

    async def pre_validate_ad_content(
        self,
        headline: str,
        image_asset_id: str | None = None,
        video_asset_id: str | None = None,
        landing_page_url: str | None = None,
    ) -> JSONData:
        """预验证广告内容"""
        results = {
            "headline": await self.validate_headline(headline),
        }

        if image_asset_id:
            results["image"] = await self.validate_image(image_asset_id)

        if video_asset_id:
            results["video"] = await self.validate_video(video_asset_id)

        if landing_page_url:
            results["landingPage"] = await self.validate_landing_page(landing_page_url)

        all_valid = all(
            r.get("valid", True) for r in results.values() if isinstance(r, dict)
        )
        results["allValid"] = all_valid

        return results
