"""
Amazon Ads Sponsored TV Ad Groups API (异步版本)

API Tier: L4 (Experimental - Beta)
Source: https://advertising.amazon.com/API/docs/en-us/sponsored-tv
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData

ST_ADGROUP_CONTENT_TYPE = "application/vnd.stAdGroup.v1+json"


class SponsoredTVAdGroupsAPI(BaseAdsClient):
    """Sponsored TV Ad Groups API (全异步)"""

    async def create_ad_groups(
        self,
        ad_groups: list[dict[str, Any]],
    ) -> JSONData:
        """创建广告组 - POST /st/adGroups"""
        result = await self.post(
            "/st/adGroups", 
            json_data={"adGroups": ad_groups},
            content_type=ST_ADGROUP_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    async def list_ad_groups(
        self,
        *,
        campaign_id_filter: list[str] | None = None,
        ad_group_id_filter: list[str] | None = None,
        states: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取广告组列表 - POST /st/adGroups/list"""
        request_body: dict[str, Any] = {"maxResults": max_results}

        if campaign_id_filter:
            request_body["campaignIdFilter"] = {"include": campaign_id_filter}
        if ad_group_id_filter:
            request_body["adGroupIdFilter"] = {"include": ad_group_id_filter}
        if states:
            request_body["stateFilter"] = {"include": states}
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post(
            "/st/adGroups/list", 
            json_data=request_body,
            content_type=ST_ADGROUP_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {"adGroups": []}

    async def update_ad_groups(
        self,
        ad_groups: list[dict[str, Any]],
    ) -> JSONData:
        """更新广告组 - PUT /st/adGroups"""
        result = await self.put(
            "/st/adGroups", 
            json_data={"adGroups": ad_groups},
            content_type=ST_ADGROUP_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    async def delete_ad_groups(
        self,
        ad_group_ids: list[str],
    ) -> JSONData:
        """删除广告组 - POST /st/adGroups/delete"""
        result = await self.post(
            "/st/adGroups/delete", 
            json_data={"adGroupIds": ad_group_ids},
            content_type=ST_ADGROUP_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}
