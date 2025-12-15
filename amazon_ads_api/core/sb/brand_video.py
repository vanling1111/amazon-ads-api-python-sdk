"""
Sponsored Brands - Video API (异步版本)
SB视频广告管理
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SBBrandVideoAPI(BaseAdsClient):
    """SB Brand Video API (全异步)"""

    # ============ Video Campaigns ============

    async def list_video_campaigns(
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

        result = await self.get("/sb/v4/campaigns", params={
            **params,
            "campaignType": "VIDEO"
        })
        return result if isinstance(result, dict) else {"campaigns": []}

    async def create_video_campaign(
        self,
        name: str,
        budget: float,
        start_date: str,
        end_date: str | None = None,
        bidding_strategy: str = "AUTO_FOR_SALES",
        brand_entity_id: str | None = None,
    ) -> JSONData:
        """创建视频广告Campaign"""
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

        result = await self.post("/sb/v4/campaigns", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ Video Ads ============

    async def list_video_ads(
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

        result = await self.get("/sb/v4/ads", params={
            **params,
            "adFormat": "VIDEO"
        })
        return result if isinstance(result, dict) else {"ads": []}

    async def get_video_ad(self, ad_id: str) -> JSONData:
        """获取视频广告详情"""
        result = await self.get(f"/sb/v4/ads/{ad_id}")
        return result if isinstance(result, dict) else {}

    async def create_video_ad(
        self,
        ad_group_id: str,
        name: str,
        video_asset_id: str,
        asin: str,
        headline: str | None = None,
        landing_page_url: str | None = None,
    ) -> JSONData:
        """创建视频广告"""
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

        result = await self.post("/sb/v4/ads", json_data=body)
        return result if isinstance(result, dict) else {}

    async def update_video_ad(
        self,
        ad_id: str,
        updates: JSONData,
    ) -> JSONData:
        """更新视频广告"""
        result = await self.put(f"/sb/v4/ads/{ad_id}", json_data=updates)
        return result if isinstance(result, dict) else {}

    # ============ Video Assets ============

    async def list_video_assets(
        self,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取视频资产列表"""
        params: JSONData = {"maxResults": max_results}
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/sb/v4/assets", params={
            **params,
            "assetType": "VIDEO"
        })
        return result if isinstance(result, dict) else {"assets": []}

    async def get_video_asset(self, asset_id: str) -> JSONData:
        """获取视频资产详情"""
        result = await self.get(f"/sb/v4/assets/{asset_id}")
        return result if isinstance(result, dict) else {}

    async def delete_video_asset(self, asset_id: str) -> JSONData:
        """删除视频资产"""
        return await self.delete(f"/sb/v4/assets/{asset_id}")

    # ============ Video Specifications ============

    async def get_video_specifications(self) -> JSONData:
        """获取视频规格要求"""
        result = await self.get("/sb/v4/assets/specifications/video")
        return result if isinstance(result, dict) else {}

    async def validate_video(
        self,
        asset_id: str,
    ) -> JSONData:
        """验证视频是否符合要求"""
        result = await self.post(f"/sb/v4/assets/{asset_id}/validate")
        return result if isinstance(result, dict) else {}

    # ============ Video Moderation ============

    async def get_video_moderation_status(self, ad_id: str) -> JSONData:
        """获取视频审核状态"""
        result = await self.get(f"/sb/v4/ads/{ad_id}/moderation")
        return result if isinstance(result, dict) else {}

    async def submit_video_for_moderation(self, ad_id: str) -> JSONData:
        """提交视频审核"""
        result = await self.post(f"/sb/v4/ads/{ad_id}/moderation/submit")
        return result if isinstance(result, dict) else {}

    # ============ Video Performance ============

    async def get_video_ad_performance(
        self,
        ad_id: str,
        start_date: str,
        end_date: str,
        metrics: list[str] | None = None,
    ) -> JSONData:
        """获取视频广告效果"""
        body: JSONData = {
            "adId": ad_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        if metrics:
            body["metrics"] = metrics

        result = await self.post("/sb/v4/ads/performance", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def list_all_video_campaigns(self) -> JSONList:
        """获取所有视频Campaign（自动分页）"""
        all_campaigns = []
        next_token = None

        while True:
            result = await self.list_video_campaigns(
                max_results=100,
                next_token=next_token,
            )
            campaigns = result.get("campaigns", [])
            all_campaigns.extend(campaigns)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_campaigns

    async def create_video_campaign_with_ad(
        self,
        campaign_name: str,
        budget: float,
        ad_group_name: str,
        video_asset_id: str,
        asin: str,
        keywords: list[dict],
        start_date: str,
    ) -> JSONData:
        """一站式创建视频广告Campaign"""
        # 1. 创建Campaign
        campaign = await self.create_video_campaign(
            name=campaign_name,
            budget=budget,
            start_date=start_date,
        )
        campaign_id = campaign.get("campaignId")
        if not campaign_id:
            return {"error": "Failed to create campaign", "details": campaign}

        # 2. 创建Ad Group
        ad_group = await self.post("/sb/v4/adGroups", json_data={
            "campaignId": campaign_id,
            "name": ad_group_name,
        })
        ad_group_id = ad_group.get("adGroupId")
        if not ad_group_id:
            return {"error": "Failed to create ad group", "details": ad_group}

        # 3. 创建Video Ad
        ad = await self.create_video_ad(
            ad_group_id=ad_group_id,
            name=f"{campaign_name}_video_ad",
            video_asset_id=video_asset_id,
            asin=asin,
        )

        # 4. 添加关键词
        await self.post("/sb/v4/keywords", json_data={
            "adGroupId": ad_group_id,
            "keywords": keywords,
        })

        return {
            "campaign": campaign,
            "adGroup": ad_group,
            "ad": ad,
        }
