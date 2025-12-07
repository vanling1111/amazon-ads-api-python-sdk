"""
Sponsored Brands - Video API
SB视频广告管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SBBrandVideoAPI(BaseAdsClient):
    """SB Brand Video API"""

    # ============ Video Campaigns ============

    def list_video_campaigns(
        self,
        state_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取视频广告Campaign列表"""
        params: JSONData = {"maxResults": max_results}
        if state_filter:
            params["stateFilter"] = state_filter
        if next_token:
            params["nextToken"] = next_token

        result = self.get("/sb/v4/campaigns", params={
            **params,
            "campaignType": "VIDEO"
        })
        return result if isinstance(result, dict) else {"campaigns": []}

    def create_video_campaign(
        self,
        name: str,
        budget: float,
        start_date: str,
        end_date: str | None = None,
        bidding_strategy: str = "AUTO_FOR_SALES",
        brand_entity_id: str | None = None,
    ) -> JSONData:
        """
        创建视频广告Campaign
        
        Args:
            bidding_strategy: AUTO_FOR_SALES | MANUAL | RULE_BASED
        """
        body: JSONData = {
            "name": name,
            "budget": budget,
            "startDate": start_date,
            "campaignType": "VIDEO",
            "biddingStrategy": bidding_strategy,
        }
        if end_date:
            body["endDate"] = end_date
        if brand_entity_id:
            body["brandEntityId"] = brand_entity_id

        result = self.post("/sb/v4/campaigns", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ Video Ads ============

    def list_video_ads(
        self,
        campaign_id: str | None = None,
        state_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取视频广告列表"""
        params: JSONData = {"maxResults": max_results}
        if campaign_id:
            params["campaignIdFilter"] = campaign_id
        if state_filter:
            params["stateFilter"] = state_filter
        if next_token:
            params["nextToken"] = next_token

        result = self.get("/sb/v4/ads", params={
            **params,
            "adFormat": "VIDEO"
        })
        return result if isinstance(result, dict) else {"ads": []}

    def get_video_ad(self, ad_id: str) -> JSONData:
        """获取视频广告详情"""
        result = self.get(f"/sb/v4/ads/{ad_id}")
        return result if isinstance(result, dict) else {}

    def create_video_ad(
        self,
        ad_group_id: str,
        name: str,
        video_asset_id: str,
        asin: str,
        headline: str | None = None,
        landing_page_url: str | None = None,
    ) -> JSONData:
        """
        创建视频广告
        
        Args:
            video_asset_id: 视频资产ID
            asin: 推广的ASIN
        """
        body: JSONData = {
            "adGroupId": ad_group_id,
            "name": name,
            "adFormat": "VIDEO",
            "creative": {
                "videoAssetId": video_asset_id,
                "asins": [asin],
            }
        }
        if headline:
            body["creative"]["headline"] = headline
        if landing_page_url:
            body["creative"]["landingPageUrl"] = landing_page_url

        result = self.post("/sb/v4/ads", json_data=body)
        return result if isinstance(result, dict) else {}

    def update_video_ad(
        self,
        ad_id: str,
        updates: JSONData,
    ) -> JSONData:
        """更新视频广告"""
        result = self.put(f"/sb/v4/ads/{ad_id}", json_data=updates)
        return result if isinstance(result, dict) else {}

    # ============ Video Assets ============

    def list_video_assets(
        self,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取视频资产列表"""
        params: JSONData = {"maxResults": max_results}
        if next_token:
            params["nextToken"] = next_token

        result = self.get("/sb/v4/assets", params={
            **params,
            "assetType": "VIDEO"
        })
        return result if isinstance(result, dict) else {"assets": []}

    def upload_video_asset(
        self,
        name: str,
        video_content: bytes,
        content_type: str = "video/mp4",
    ) -> JSONData:
        """
        上传视频资产
        
        Args:
            content_type: video/mp4, video/mov, video/avi
        """
        # 1. 注册上传
        registration = self.post("/sb/v4/assets/register", json_data={
            "name": name,
            "assetType": "VIDEO",
            "contentType": content_type,
        })

        asset_id = registration.get("assetId")
        upload_url = registration.get("uploadUrl")

        if not asset_id or not upload_url:
            return {"error": "Failed to register upload"}

        # 2. 上传文件
        response = self.session.put(
            upload_url,
            data=video_content,
            headers={"Content-Type": content_type},
            timeout=300,  # 视频上传可能较慢
        )

        if not response.ok:
            return {"error": f"Upload failed: {response.status_code}"}

        # 3. 确认上传完成
        result = self.post(f"/sb/v4/assets/{asset_id}/complete")
        return result if isinstance(result, dict) else {}

    def get_video_asset(self, asset_id: str) -> JSONData:
        """获取视频资产详情"""
        result = self.get(f"/sb/v4/assets/{asset_id}")
        return result if isinstance(result, dict) else {}

    def delete_video_asset(self, asset_id: str) -> JSONData:
        """删除视频资产"""
        return self.delete(f"/sb/v4/assets/{asset_id}")

    # ============ Video Specifications ============

    def get_video_specifications(self) -> JSONData:
        """
        获取视频规格要求
        
        返回分辨率、时长、文件大小等要求
        """
        result = self.get("/sb/v4/assets/specifications/video")
        return result if isinstance(result, dict) else {}

    def validate_video(
        self,
        asset_id: str,
    ) -> JSONData:
        """验证视频是否符合要求"""
        result = self.post(f"/sb/v4/assets/{asset_id}/validate")
        return result if isinstance(result, dict) else {}

    # ============ Video Moderation ============

    def get_video_moderation_status(self, ad_id: str) -> JSONData:
        """获取视频审核状态"""
        result = self.get(f"/sb/v4/ads/{ad_id}/moderation")
        return result if isinstance(result, dict) else {}

    def submit_video_for_moderation(self, ad_id: str) -> JSONData:
        """提交视频审核"""
        result = self.post(f"/sb/v4/ads/{ad_id}/moderation/submit")
        return result if isinstance(result, dict) else {}

    # ============ Video Performance ============

    def get_video_ad_performance(
        self,
        ad_id: str,
        start_date: str,
        end_date: str,
        metrics: list[str] | None = None,
    ) -> JSONData:
        """
        获取视频广告效果
        
        Args:
            metrics: [
                "impressions", "clicks", "cost", "sales",
                "videoFirstQuartileViews", "videoMidpointViews",
                "videoThirdQuartileViews", "videoCompleteViews"
            ]
        """
        body: JSONData = {
            "adId": ad_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        if metrics:
            body["metrics"] = metrics

        result = self.post("/sb/v4/ads/performance", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    def list_all_video_campaigns(self) -> JSONList:
        """获取所有视频Campaign（自动分页）"""
        all_campaigns = []
        next_token = None

        while True:
            result = self.list_video_campaigns(
                max_results=100,
                next_token=next_token,
            )
            campaigns = result.get("campaigns", [])
            all_campaigns.extend(campaigns)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_campaigns

    def create_video_campaign_with_ad(
        self,
        campaign_name: str,
        budget: float,
        ad_group_name: str,
        video_asset_id: str,
        asin: str,
        keywords: list[dict],
        start_date: str,
    ) -> JSONData:
        """
        一站式创建视频广告Campaign
        
        创建Campaign -> Ad Group -> Ad -> Keywords
        """
        # 1. 创建Campaign
        campaign = self.create_video_campaign(
            name=campaign_name,
            budget=budget,
            start_date=start_date,
        )
        campaign_id = campaign.get("campaignId")
        if not campaign_id:
            return {"error": "Failed to create campaign", "details": campaign}

        # 2. 创建Ad Group
        ad_group = self.post("/sb/v4/adGroups", json_data={
            "campaignId": campaign_id,
            "name": ad_group_name,
        })
        ad_group_id = ad_group.get("adGroupId")
        if not ad_group_id:
            return {"error": "Failed to create ad group", "details": ad_group}

        # 3. 创建Video Ad
        ad = self.create_video_ad(
            ad_group_id=ad_group_id,
            name=f"{campaign_name}_video_ad",
            video_asset_id=video_asset_id,
            asin=asin,
        )

        # 4. 添加关键词
        self.post("/sb/v4/keywords", json_data={
            "adGroupId": ad_group_id,
            "keywords": keywords,
        })

        return {
            "campaign": campaign,
            "adGroup": ad_group,
            "ad": ad,
        }

