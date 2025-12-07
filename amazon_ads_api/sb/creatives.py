"""
Sponsored Brands - Creatives API
SB创意管理（标题、Logo、视频等）
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SBCreativesAPI(BaseAdsClient):
    """SB Creatives API"""

    # ============ Ad Creatives ============

    def get_ad_creative(self, ad_id: str) -> JSONData:
        """获取广告创意详情"""
        result = self.get(f"/sb/v4/ads/{ad_id}/creative")
        return result if isinstance(result, dict) else {}

    def update_ad_creative(
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
        result = self.put(f"/sb/v4/ads/{ad_id}/creative", json_data=creative)
        return result if isinstance(result, dict) else {}

    # ============ Headline Recommendations ============

    def get_headline_recommendations(
        self,
        asins: list[str],
        max_recommendations: int = 10,
    ) -> JSONData:
        """
        获取标题建议
        
        AI生成的广告标题推荐
        
        Args:
            asins: 要推广的ASIN列表
            max_recommendations: 最大建议数
        """
        result = self.post("/sb/recommendations/creative/headline", json_data={
            "asins": asins,
            "maxRecommendations": max_recommendations,
        })
        return result if isinstance(result, dict) else {"recommendations": []}

    # ============ Brand Logo ============

    def list_brand_logos(self, brand_entity_id: str | None = None) -> JSONList:
        """
        获取可用的品牌Logo列表
        
        Logo必须先上传到Creative Assets
        """
        params = {}
        if brand_entity_id:
            params["brandEntityId"] = brand_entity_id

        result = self.get("/sb/brands/logos", params=params or None)
        return result if isinstance(result, list) else []

    def validate_brand_logo(self, asset_id: str) -> JSONData:
        """
        验证品牌Logo是否符合要求
        
        SB对Logo有特定要求（尺寸、格式等）
        """
        result = self.post("/sb/brands/logos/validate", json_data={
            "assetId": asset_id
        })
        return result if isinstance(result, dict) else {}

    # ============ Video Creatives ============

    def validate_video(self, video_asset_id: str) -> JSONData:
        """
        验证视频是否符合SB要求
        
        视频要求：
        - 时长：6-45秒
        - 分辨率：最小1280x720
        - 格式：MP4, MOV
        """
        result = self.post("/sb/videos/validate", json_data={
            "videoAssetId": video_asset_id
        })
        return result if isinstance(result, dict) else {}

    def get_video_status(self, video_asset_id: str) -> JSONData:
        """获取视频处理状态"""
        result = self.get(f"/sb/videos/{video_asset_id}/status")
        return result if isinstance(result, dict) else {}

    # ============ Store Page Creatives ============

    def get_store_page_info(self, store_page_url: str) -> JSONData:
        """
        获取品牌旗舰店页面信息
        
        用于Store Spotlight广告
        """
        result = self.post("/sb/stores/pageInfo", json_data={
            "storePageUrl": store_page_url
        })
        return result if isinstance(result, dict) else {}

    def list_store_pages(self, brand_entity_id: str) -> JSONList:
        """获取品牌旗舰店页面列表"""
        result = self.get(f"/sb/brands/{brand_entity_id}/stores/pages")
        return result if isinstance(result, list) else []

    # ============ Pre-moderation (预审核) ============

    def submit_for_premoderation(
        self,
        creative: JSONData,
    ) -> JSONData:
        """
        提交创意预审核
        
        在正式创建广告前，可以先验证创意是否符合政策
        
        Args:
            creative: 创意内容（与create_ad相同格式）
        """
        result = self.post("/sb/preModeration", json_data=creative)
        return result if isinstance(result, dict) else {}

    def get_premoderation_result(self, premoderation_id: str) -> JSONData:
        """获取预审核结果"""
        result = self.get(f"/sb/preModeration/{premoderation_id}")
        return result if isinstance(result, dict) else {}

    # ============ Creative Policy ============

    def get_creative_policy(self) -> JSONData:
        """
        获取创意政策信息
        
        返回当前的创意要求和限制
        """
        result = self.get("/sb/creative/policy")
        return result if isinstance(result, dict) else {}

    # ============ A/B Testing (Beta) ============

    def create_creative_test(
        self,
        campaign_id: str,
        ad_group_id: str,
        creative_a: JSONData,
        creative_b: JSONData,
        test_duration_days: int = 14,
    ) -> JSONData:
        """
        创建创意A/B测试
        
        测试不同标题、图片的效果
        """
        result = self.post("/sb/creativeTests", json_data={
            "campaignId": campaign_id,
            "adGroupId": ad_group_id,
            "creativeA": creative_a,
            "creativeB": creative_b,
            "testDurationDays": test_duration_days,
        })
        return result if isinstance(result, dict) else {}

    def get_creative_test_results(self, test_id: str) -> JSONData:
        """获取A/B测试结果"""
        result = self.get(f"/sb/creativeTests/{test_id}/results")
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    def update_headline(self, ad_id: str, headline: str) -> JSONData:
        """更新广告标题"""
        return self.update_ad_creative(ad_id, {"headline": headline})

    def update_brand_logo(self, ad_id: str, logo_asset_id: str) -> JSONData:
        """更新品牌Logo"""
        return self.update_ad_creative(ad_id, {"brandLogoAssetID": logo_asset_id})

    def update_asins(self, ad_id: str, asins: list[str]) -> JSONData:
        """更新广告ASIN"""
        return self.update_ad_creative(ad_id, {"asins": asins[:3]})

