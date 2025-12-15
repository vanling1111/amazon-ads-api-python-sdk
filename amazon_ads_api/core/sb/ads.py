"""
Sponsored Brands - Ads API (异步版本)
SB广告管理（不同类型的品牌广告）
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SBAdsAPI(BaseAdsClient):
    """SB Ads API (全异步)"""

    # SB v4 Content-Types
    SB_AD_V4_CONTENT_TYPE = "application/vnd.sbadresource.v4+json"

    # ============ Ads (V4) ============

    async def list_ads(
        self,
        campaign_id: str | None = None,
        ad_group_id: str | None = None,
        ad_ids: list[str] | None = None,
        state_filter: list[str] | str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取SB Ad列表
        
        SB广告类型:
        - productCollection: 产品集广告
        - video: 视频广告
        - storeSpotlight: 品牌旗舰店聚焦广告
        
        Args:
            campaign_id: Campaign ID过滤
            ad_group_id: Ad Group ID过滤
            ad_ids: Ad ID过滤
            state_filter: 状态过滤 ["ENABLED", "PAUSED", "ARCHIVED"]
            max_results: 最大结果数
            next_token: 分页token
        """
        params: JSONData = {"maxResults": max_results}
        
        # ID过滤 - 官方格式: {"include": [...]}
        if campaign_id:
            params["campaignIdFilter"] = {"include": [campaign_id]}
        if ad_group_id:
            params["adGroupIdFilter"] = {"include": [ad_group_id]}
        if ad_ids:
            params["adIdFilter"] = {"include": ad_ids}
        
        # 状态过滤
        if state_filter:
            states = [state_filter] if isinstance(state_filter, str) else state_filter
            params["stateFilter"] = {"include": [s.upper() for s in states]}
        
        if next_token:
            params["nextToken"] = next_token

        result = await self.post(
            "/sb/v4/ads/list", 
            json_data=params,
            content_type="application/vnd.sbadresource.v4+json"
        )
        return result if isinstance(result, dict) else {"ads": []}

    async def get_ad(self, ad_id: str) -> JSONData:
        """获取单个SB Ad详情"""
        result = await self.get(f"/sb/v4/ads/{ad_id}")
        return result if isinstance(result, dict) else {}

    async def create_ads(self, ads: JSONList) -> JSONData:
        """
        批量创建SB Ad
        
        Args:
            ads: [
                {
                    "campaignId": "xxx",
                    "adGroupId": "xxx",
                    "state": "enabled",
                    "adType": "productCollection",
                    "creative": {
                        "brandName": "My Brand",
                        "brandLogoAssetID": "xxx",
                        "headline": "Shop Our Products",
                        "asins": ["B00XXXX", "B00YYYY"]
                    },
                    "landingPage": {
                        "pageType": "STORE",
                        "url": "https://www.amazon.com/stores/..."
                    }
                }
            ]
        """
        result = await self.post(
            "/sb/v4/ads", 
            json_data={"ads": ads},
            content_type=self.SB_AD_V4_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"ads": {"success": [], "error": []}}

    async def update_ads(self, ads: JSONList) -> JSONData:
        """批量更新SB Ad"""
        result = await self.put(
            "/sb/v4/ads", 
            json_data={"ads": ads},
            content_type=self.SB_AD_V4_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"ads": {"success": [], "error": []}}

    async def delete_ads(self, ad_ids: list[str]) -> JSONData:
        """
        批量归档SB Ad（官方 v4 /delete 端点）
        
        注意：Amazon Ads 不支持真正删除，此操作将 Ad 状态设置为 "archived"。
        """
        result = await self.post(
            "/sb/v4/ads/delete",
            json_data={"adIdFilter": {"include": ad_ids}},
            content_type=self.SB_AD_V4_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"ads": {"success": [], "error": []}}

    async def delete_ad(self, ad_id: str) -> JSONData:
        """归档单个SB Ad"""
        return await self.delete_ads([ad_id])

    # ============ Creative Types - Official v4 Endpoints ============

    async def create_product_collection_ads_v4(self, ads: JSONList) -> JSONData:
        """创建产品集广告（官方 v4 端点）"""
        result = await self.post(
            "/sb/v4/ads/productCollection", 
            json_data={"ads": ads},
            content_type=self.SB_AD_V4_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"ads": {"success": [], "error": []}}

    async def create_product_collection_extended_ads_v4(self, ads: JSONList) -> JSONData:
        """创建扩展产品集广告（官方 v4 端点）"""
        result = await self.post(
            "/sb/v4/ads/productCollectionExtended", 
            json_data={"ads": ads},
            content_type=self.SB_AD_V4_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"ads": {"success": [], "error": []}}

    async def create_video_ads_v4(self, ads: JSONList) -> JSONData:
        """创建视频广告（官方 v4 端点）"""
        result = await self.post(
            "/sb/v4/ads/video", 
            json_data={"ads": ads},
            content_type=self.SB_AD_V4_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"ads": {"success": [], "error": []}}

    async def create_brand_video_ads_v4(self, ads: JSONList) -> JSONData:
        """创建品牌视频广告（官方 v4 端点）"""
        result = await self.post(
            "/sb/v4/ads/brandVideo", 
            json_data={"ads": ads},
            content_type=self.SB_AD_V4_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"ads": {"success": [], "error": []}}

    async def create_store_spotlight_ads_v4(self, ads: JSONList) -> JSONData:
        """创建店铺聚焦广告（官方 v4 端点）"""
        result = await self.post(
            "/sb/v4/ads/storeSpotlight", 
            json_data={"ads": ads},
            content_type=self.SB_AD_V4_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"ads": {"success": [], "error": []}}

    # ============ Creative List Endpoints ============

    async def list_creatives(
        self,
        creative_type: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取创意列表"""
        body: JSONData = {"maxResults": max_results}
        if creative_type:
            body["creativeTypeFilter"] = creative_type
        if next_token:
            body["nextToken"] = next_token

        result = await self.post("/sb/ads/creatives/list", json_data=body)
        return result if isinstance(result, dict) else {"creatives": []}

    async def create_brand_video_creative(self, creatives: JSONList) -> JSONData:
        """创建品牌视频创意"""
        result = await self.post("/sb/ads/creatives/brandVideo", json_data={"creatives": creatives})
        return result if isinstance(result, dict) else {"creatives": {"success": [], "error": []}}

    async def create_product_collection_creative(self, creatives: JSONList) -> JSONData:
        """创建产品集创意"""
        result = await self.post("/sb/ads/creatives/productCollection", json_data={"creatives": creatives})
        return result if isinstance(result, dict) else {"creatives": {"success": [], "error": []}}

    async def create_product_collection_extended_creative(self, creatives: JSONList) -> JSONData:
        """创建扩展产品集创意"""
        result = await self.post("/sb/ads/creatives/productCollectionExtended", json_data={"creatives": creatives})
        return result if isinstance(result, dict) else {"creatives": {"success": [], "error": []}}

    async def create_store_spotlight_creative(self, creatives: JSONList) -> JSONData:
        """创建店铺聚焦创意"""
        result = await self.post("/sb/ads/creatives/storeSpotlight", json_data={"creatives": creatives})
        return result if isinstance(result, dict) else {"creatives": {"success": [], "error": []}}

    async def create_video_creative(self, creatives: JSONList) -> JSONData:
        """创建视频创意"""
        result = await self.post("/sb/ads/creatives/video", json_data={"creatives": creatives})
        return result if isinstance(result, dict) else {"creatives": {"success": [], "error": []}}

    # ============ Product Collection Ads ============

    async def create_product_collection_ad(
        self,
        campaign_id: str,
        ad_group_id: str,
        brand_name: str,
        brand_logo_asset_id: str,
        headline: str,
        asins: list[str],
        landing_page_url: str,
    ) -> JSONData:
        """
        创建产品集广告
        
        最常用的SB广告类型
        """
        ads = [{
            "campaignId": campaign_id,
            "adGroupId": ad_group_id,
            "state": "enabled",
            "adType": "productCollection",
            "creative": {
                "brandName": brand_name,
                "brandLogoAssetID": brand_logo_asset_id,
                "headline": headline,
                "asins": asins[:3]  # 最多3个ASIN
            },
            "landingPage": {
                "pageType": "STORE",
                "url": landing_page_url
            }
        }]
        return await self.create_ads(ads)

    # ============ Video Ads ============

    async def create_video_ad(
        self,
        campaign_id: str,
        ad_group_id: str,
        video_asset_id: str,
        asin: str,
    ) -> JSONData:
        """
        创建视频广告
        
        需要先上传视频到Creative Assets
        """
        ads = [{
            "campaignId": campaign_id,
            "adGroupId": ad_group_id,
            "state": "enabled",
            "adType": "video",
            "creative": {
                "videoAssetId": video_asset_id,
                "asin": asin
            }
        }]
        return await self.create_ads(ads)

    # ============ Store Spotlight Ads ============

    async def create_store_spotlight_ad(
        self,
        campaign_id: str,
        ad_group_id: str,
        brand_name: str,
        brand_logo_asset_id: str,
        headline: str,
        store_pages: list[dict],
    ) -> JSONData:
        """
        创建品牌旗舰店聚焦广告
        
        Args:
            store_pages: [
                {"pageTitle": "Page 1", "asin": "B00XXXX"},
                {"pageTitle": "Page 2", "asin": "B00YYYY"},
                {"pageTitle": "Page 3", "asin": "B00ZZZZ"}
            ]
        """
        ads = [{
            "campaignId": campaign_id,
            "adGroupId": ad_group_id,
            "state": "enabled",
            "adType": "storeSpotlight",
            "creative": {
                "brandName": brand_name,
                "brandLogoAssetID": brand_logo_asset_id,
                "headline": headline,
                "storePages": store_pages[:3]  # 最多3个页面
            }
        }]
        return await self.create_ads(ads)

    # ============ Landing Pages ============

    async def get_landing_page_asins(
        self,
        landing_page_url: str,
    ) -> JSONData:
        """
        获取Landing Page上的ASIN
        
        用于验证和选择要推广的产品
        """
        result = await self.post("/sb/landingPageAsins", json_data={
            "landingPageUrl": landing_page_url
        })
        return result if isinstance(result, dict) else {"asins": []}

    # ============ Brands & Stores ============

    async def list_brands(self) -> JSONList:
        """获取可用的品牌列表"""
        result = await self.get("/sb/brands")
        return result if isinstance(result, list) else []

    async def list_stores(self, brand_entity_id: str | None = None) -> JSONList:
        """获取品牌旗舰店列表"""
        params = {}
        if brand_entity_id:
            params["brandEntityId"] = brand_entity_id
        result = await self.get("/sb/stores", params=params or None)
        return result if isinstance(result, list) else []

    # ============ Moderation (审核状态) ============

    async def get_moderation_status(self, ad_ids: list[str]) -> JSONList:
        """
        获取广告审核状态
        
        SB广告需要经过Amazon审核
        """
        result = await self.post("/sb/moderation", json_data={"adIds": ad_ids})
        return result if isinstance(result, list) else []

    # ============ 便捷方法 ============

    async def pause_ad(self, ad_id: str) -> JSONData:
        """暂停广告"""
        return await self.update_ads([{"adId": ad_id, "state": "paused"}])

    async def enable_ad(self, ad_id: str) -> JSONData:
        """启用广告"""
        return await self.update_ads([{"adId": ad_id, "state": "enabled"}])

    async def list_all_ads(
        self,
        campaign_id: str | None = None,
        state_filter: str | None = None,
    ) -> JSONList:
        """获取所有广告（自动分页）"""
        all_ads = []
        next_token = None

        while True:
            result = await self.list_ads(
                campaign_id=campaign_id,
                state_filter=state_filter,
                max_results=100,
                next_token=next_token,
            )
            ads = result.get("ads", [])
            all_ads.extend(ads)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_ads
