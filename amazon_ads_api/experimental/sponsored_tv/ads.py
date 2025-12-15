"""
Amazon Ads Sponsored TV Ads API (异步版本)

API Tier: L4 (Experimental - Beta)
Source: https://advertising.amazon.com/API/docs/en-us/sponsored-tv
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData

ST_AD_CONTENT_TYPE = "application/vnd.stAd.v1+json"


class SponsoredTVAdsAPI(BaseAdsClient):
    """Sponsored TV Ads API (全异步)"""

    async def create_ads(
        self,
        ads: list[dict[str, Any]],
    ) -> JSONData:
        """创建广告 - POST /st/ads"""
        result = await self.post(
            "/st/ads", 
            json_data={"ads": ads},
            content_type=ST_AD_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    async def list_ads(
        self,
        *,
        campaign_id_filter: list[str] | None = None,
        ad_group_id_filter: list[str] | None = None,
        ad_id_filter: list[str] | None = None,
        states: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取广告列表 - POST /st/ads/list"""
        request_body: dict[str, Any] = {"maxResults": max_results}

        if campaign_id_filter:
            request_body["campaignIdFilter"] = {"include": campaign_id_filter}
        if ad_group_id_filter:
            request_body["adGroupIdFilter"] = {"include": ad_group_id_filter}
        if ad_id_filter:
            request_body["adIdFilter"] = {"include": ad_id_filter}
        if states:
            request_body["stateFilter"] = {"include": states}
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post(
            "/st/ads/list", 
            json_data=request_body,
            content_type=ST_AD_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {"ads": []}

    async def update_ads(
        self,
        ads: list[dict[str, Any]],
    ) -> JSONData:
        """更新广告 - PUT /st/ads"""
        result = await self.put(
            "/st/ads", 
            json_data={"ads": ads},
            content_type=ST_AD_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    async def delete_ads(
        self,
        ad_ids: list[str],
    ) -> JSONData:
        """删除广告 - POST /st/ads/delete"""
        result = await self.post(
            "/st/ads/delete", 
            json_data={"adIds": ad_ids},
            content_type=ST_AD_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}
