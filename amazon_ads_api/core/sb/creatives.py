"""
Sponsored Brands - Creatives API (异步版本)
SB创意管理（标题、Logo、视频等）
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SBCreativesAPI(BaseAdsClient):
    """SB Creatives API (全异步)"""

    # ============ Ad Creatives ============

    async def get_ad_creative(self, ad_id: str) -> JSONData:
        """获取广告创意详情"""
        result = await self.get(f"/sb/v4/ads/{ad_id}/creative")
        return result if isinstance(result, dict) else {}

    async def update_ad_creative(
        self,
        ad_id: str,
        creative: JSONData,
    ) -> JSONData:
        """
        更新广告创意
        
        Args:
            creative: {
                "headline": "New Headline",
                "brandName": "Brand Name",
                "brandLogoAssetID": "xxx",
                "asins": ["B00XXXX"]
            }
        """
        result = await self.put(f"/sb/v4/ads/{ad_id}/creative", json_data=creative)
        return result if isinstance(result, dict) else {}

    # ============ Headline Recommendations ============

    async def get_headline_recommendations(
        self,
        asins: list[str],
        max_recommendations: int = 10,
    ) -> JSONData:
        """
        获取标题建议
        
        AI生成的广告标题推荐
        """
        result = await self.post("/sb/recommendations/creative/headline", json_data={
            "asins": asins,
            "maxRecommendations": max_recommendations,
        })
        return result if isinstance(result, dict) else {"recommendations": []}

    # ============ Brand Logo ============

    async def list_brand_logos(self, brand_entity_id: str | None = None) -> JSONList:
        """获取可用的品牌Logo列表"""
        params = {}
        if brand_entity_id:
            params["brandEntityId"] = brand_entity_id

        result = await self.get("/sb/brands/logos", params=params or None)
        return result if isinstance(result, list) else []

    async def validate_brand_logo(self, asset_id: str) -> JSONData:
        """验证品牌Logo是否符合要求"""
        result = await self.post("/sb/brands/logos/validate", json_data={
            "assetId": asset_id
        })
        return result if isinstance(result, dict) else {}

    # ============ Video Creatives ============

    async def validate_video(self, video_asset_id: str) -> JSONData:
        """验证视频是否符合SB要求"""
        result = await self.post("/sb/videos/validate", json_data={
            "videoAssetId": video_asset_id
        })
        return result if isinstance(result, dict) else {}

    async def get_video_status(self, video_asset_id: str) -> JSONData:
        """获取视频处理状态"""
        result = await self.get(f"/sb/videos/{video_asset_id}/status")
        return result if isinstance(result, dict) else {}

    # ============ Store Page Creatives ============

    async def get_store_page_info(self, store_page_url: str) -> JSONData:
        """获取品牌旗舰店页面信息"""
        result = await self.post("/sb/stores/pageInfo", json_data={
            "storePageUrl": store_page_url
        })
        return result if isinstance(result, dict) else {}

    async def list_store_pages(self, brand_entity_id: str) -> JSONList:
        """获取品牌旗舰店页面列表"""
        result = await self.get(f"/sb/brands/{brand_entity_id}/stores/pages")
        return result if isinstance(result, list) else []

    # ============ Pre-moderation (预审核) ============

    async def submit_for_premoderation(
        self,
        creative: JSONData,
    ) -> JSONData:
        """提交创意预审核"""
        result = await self.post("/sb/preModeration", json_data=creative)
        return result if isinstance(result, dict) else {}

    async def get_premoderation_result(self, premoderation_id: str) -> JSONData:
        """获取预审核结果"""
        result = await self.get(f"/sb/preModeration/{premoderation_id}")
        return result if isinstance(result, dict) else {}

    # ============ Creative Policy ============

    async def get_creative_policy(self) -> JSONData:
        """获取创意政策信息"""
        result = await self.get("/sb/creative/policy")
        return result if isinstance(result, dict) else {}

    # ============ A/B Testing (Beta) ============

    async def create_creative_test(
        self,
        campaign_id: str,
        ad_group_id: str,
        creative_a: JSONData,
        creative_b: JSONData,
        test_duration_days: int = 14,
    ) -> JSONData:
        """创建创意A/B测试"""
        result = await self.post("/sb/creativeTests", json_data={
            "campaignId": campaign_id,
            "adGroupId": ad_group_id,
            "creativeA": creative_a,
            "creativeB": creative_b,
            "testDurationDays": test_duration_days,
        })
        return result if isinstance(result, dict) else {}

    async def get_creative_test_results(self, test_id: str) -> JSONData:
        """获取A/B测试结果"""
        result = await self.get(f"/sb/creativeTests/{test_id}/results")
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def update_headline(self, ad_id: str, headline: str) -> JSONData:
        """更新广告标题"""
        return await self.update_ad_creative(ad_id, {"headline": headline})

    async def update_brand_logo(self, ad_id: str, logo_asset_id: str) -> JSONData:
        """更新品牌Logo"""
        return await self.update_ad_creative(ad_id, {"brandLogoAssetID": logo_asset_id})

    async def update_asins(self, ad_id: str, asins: list[str]) -> JSONData:
        """更新广告ASIN"""
        return await self.update_ad_creative(ad_id, {"asins": asins[:3]})
