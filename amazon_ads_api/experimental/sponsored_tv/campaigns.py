"""
Amazon Ads Sponsored TV Campaigns API (异步版本)

API Tier: L4 (Experimental - Beta)
Source: https://advertising.amazon.com/API/docs/en-us/sponsored-tv
OpenAPI: ✅ SponsoredTV_prod_3p.json
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData

# Sponsored TV 自定义 Content-Type
ST_CAMPAIGN_CONTENT_TYPE = "application/vnd.stCampaign.v1+json"
ST_FORECAST_CONTENT_TYPE = "application/vnd.stForecast.v1+json"


class SponsoredTVCampaignsAPI(BaseAdsClient):
    """Sponsored TV Campaigns API (全异步)
    
    API Tier: L4 (Experimental - Beta)
    官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-tv
    """

    async def create_campaigns(
        self,
        campaigns: list[dict[str, Any]],
    ) -> JSONData:
        """创建Sponsored TV广告活动
        
        POST /st/campaigns
        Content-Type: application/vnd.stCampaign.v1+json
        """
        result = await self.post(
            "/st/campaigns", 
            json_data={"campaigns": campaigns},
            content_type=ST_CAMPAIGN_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    async def list_campaigns(
        self,
        *,
        campaign_ids: list[str] | None = None,
        states: list[str] | None = None,
        name_filter: dict[str, Any] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取Sponsored TV广告活动列表
        
        POST /st/campaigns/list
        Content-Type: application/vnd.stCampaign.v1+json
        """
        request_body: dict[str, Any] = {"maxResults": max_results}

        if campaign_ids:
            request_body["campaignIdFilter"] = {"include": campaign_ids}
        if states:
            request_body["stateFilter"] = {"include": states}
        if name_filter:
            request_body["nameFilter"] = name_filter
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post(
            "/st/campaigns/list", 
            json_data=request_body,
            content_type=ST_CAMPAIGN_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {"campaigns": []}

    async def update_campaigns(
        self,
        campaigns: list[dict[str, Any]],
    ) -> JSONData:
        """更新Sponsored TV广告活动
        
        PUT /st/campaigns
        Content-Type: application/vnd.stCampaign.v1+json
        """
        result = await self.put(
            "/st/campaigns", 
            json_data={"campaigns": campaigns},
            content_type=ST_CAMPAIGN_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    async def delete_campaigns(
        self,
        campaign_ids: list[str],
    ) -> JSONData:
        """删除Sponsored TV广告活动
        
        POST /st/campaigns/delete
        Content-Type: application/vnd.stCampaign.v1+json
        """
        result = await self.post(
            "/st/campaigns/delete", 
            json_data={"campaignIds": campaign_ids},
            content_type=ST_CAMPAIGN_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    async def get_forecasts(
        self,
        forecast_request: dict[str, Any],
    ) -> JSONData:
        """获取Sponsored TV预测
        
        POST /st/forecasts
        Content-Type: application/vnd.stForecast.v1+json
        """
        result = await self.post(
            "/st/forecasts", 
            json_data=forecast_request,
            content_type=ST_FORECAST_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}
