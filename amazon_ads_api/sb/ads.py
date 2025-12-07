"""
Sponsored Brands - Ads API
SB广告管理（不同类型的品牌广告）
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SBAdsAPI(BaseAdsClient):
    """SB Ads API"""

    # ============ Ads (V4) ============

    def list_ads(
        self,
        campaign_id: str | None = None,
        ad_group_id: str | None = None,
        state_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取SB Ad列表
        
        SB广告类型:
        - productCollection: 产品集广告
        - video: 视频广告
        - storeSpotlight: 品牌旗舰店聚焦广告
        """
        params: JSONData = {"maxResults": max_results}
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]
        if ad_group_id:
            params["adGroupIdFilter"] = [ad_group_id]
        if state_filter:
            params["stateFilter"] = state_filter
        if next_token:
            params["nextToken"] = next_token

        result = self.post("/sb/v4/ads/list", json_data=params)
        return result if isinstance(result, dict) else {"ads": []}

    def get_ad(self, ad_id: str) -> JSONData:
        """获取单个SB Ad详情"""
        result = self.get(f"/sb/v4/ads/{ad_id}")
        return result if isinstance(result, dict) else {}

    def create_ads(self, ads: JSONList) -> JSONData:
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
        result = self.post("/sb/v4/ads", json_data={"ads": ads})
        return result if isinstance(result, dict) else {"ads": {"success": [], "error": []}}

    def update_ads(self, ads: JSONList) -> JSONData:
        """批量更新SB Ad"""
        result = self.put("/sb/v4/ads", json_data={"ads": ads})
        return result if isinstance(result, dict) else {"ads": {"success": [], "error": []}}

    def delete_ad(self, ad_id: str) -> JSONData:
        """归档SB Ad"""
        return self.delete(f"/sb/v4/ads/{ad_id}")

    # ============ Product Collection Ads ============

    def create_product_collection_ad(
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
        return self.create_ads(ads)

    # ============ Video Ads ============

    def create_video_ad(
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
        return self.create_ads(ads)

    # ============ Store Spotlight Ads ============

    def create_store_spotlight_ad(
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
        return self.create_ads(ads)

    # ============ Landing Pages ============

    def get_landing_page_asins(
        self,
        landing_page_url: str,
    ) -> JSONData:
        """
        获取Landing Page上的ASIN
        
        用于验证和选择要推广的产品
        """
        result = self.post("/sb/landingPageAsins", json_data={
            "landingPageUrl": landing_page_url
        })
        return result if isinstance(result, dict) else {"asins": []}

    # ============ Brands & Stores ============

    def list_brands(self) -> JSONList:
        """获取可用的品牌列表"""
        result = self.get("/sb/brands")
        return result if isinstance(result, list) else []

    def list_stores(self, brand_entity_id: str | None = None) -> JSONList:
        """获取品牌旗舰店列表"""
        params = {}
        if brand_entity_id:
            params["brandEntityId"] = brand_entity_id
        result = self.get("/sb/stores", params=params or None)
        return result if isinstance(result, list) else []

    # ============ Moderation (审核状态) ============

    def get_moderation_status(self, ad_ids: list[str]) -> JSONList:
        """
        获取广告审核状态
        
        SB广告需要经过Amazon审核
        """
        result = self.post("/sb/moderation", json_data={"adIds": ad_ids})
        return result if isinstance(result, list) else []

    # ============ 便捷方法 ============

    def pause_ad(self, ad_id: str) -> JSONData:
        """暂停广告"""
        return self.update_ads([{"adId": ad_id, "state": "paused"}])

    def enable_ad(self, ad_id: str) -> JSONData:
        """启用广告"""
        return self.update_ads([{"adId": ad_id, "state": "enabled"}])

    def list_all_ads(
        self,
        campaign_id: str | None = None,
        state_filter: str | None = None,
    ) -> JSONList:
        """获取所有广告（自动分页）"""
        all_ads = []
        next_token = None

        while True:
            result = self.list_ads(
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

