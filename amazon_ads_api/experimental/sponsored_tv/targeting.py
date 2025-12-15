"""
Amazon Ads Sponsored TV Targeting API (异步版本)

API Tier: L4 (Experimental - Beta)
Source: https://advertising.amazon.com/API/docs/en-us/sponsored-tv
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData

ST_TARGET_CONTENT_TYPE = "application/vnd.stTargetingClause.v1+json"
ST_LOCATION_CONTENT_TYPE = "application/vnd.stLocation.v1+json"


class SponsoredTVTargetingAPI(BaseAdsClient):
    """Sponsored TV Targeting API (全异步)"""

    # ==================== Targeting Clauses ====================

    async def create_targeting_clauses(
        self,
        targets: list[dict[str, Any]],
    ) -> JSONData:
        """创建定向条件 - POST /st/targets"""
        result = await self.post(
            "/st/targets", 
            json_data={"targets": targets},
            content_type=ST_TARGET_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    async def list_targeting_clauses(
        self,
        *,
        campaign_id_filter: list[str] | None = None,
        ad_group_id_filter: list[str] | None = None,
        target_id_filter: list[str] | None = None,
        states: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取定向条件列表 - POST /st/targets/list"""
        request_body: dict[str, Any] = {"maxResults": max_results}

        if campaign_id_filter:
            request_body["campaignIdFilter"] = {"include": campaign_id_filter}
        if ad_group_id_filter:
            request_body["adGroupIdFilter"] = {"include": ad_group_id_filter}
        if target_id_filter:
            request_body["targetIdFilter"] = {"include": target_id_filter}
        if states:
            request_body["stateFilter"] = {"include": states}
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post(
            "/st/targets/list", 
            json_data=request_body,
            content_type=ST_TARGET_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {"targets": []}

    async def update_targeting_clauses(
        self,
        targets: list[dict[str, Any]],
    ) -> JSONData:
        """更新定向条件 - PUT /st/targets"""
        result = await self.put(
            "/st/targets", 
            json_data={"targets": targets},
            content_type=ST_TARGET_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    async def delete_targeting_clauses(
        self,
        target_ids: list[str],
    ) -> JSONData:
        """删除定向条件 - POST /st/targets/delete"""
        result = await self.post(
            "/st/targets/delete", 
            json_data={"targetIds": target_ids},
            content_type=ST_TARGET_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    # ==================== Locations ====================

    async def create_locations(
        self,
        locations: list[dict[str, Any]],
    ) -> JSONData:
        """创建地理位置定向 - POST /st/locations"""
        result = await self.post(
            "/st/locations", 
            json_data={"locations": locations},
            content_type=ST_LOCATION_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    async def list_locations(
        self,
        *,
        campaign_id_filter: list[str] | None = None,
        location_id_filter: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取地理位置定向列表 - POST /st/locations/list"""
        request_body: dict[str, Any] = {"maxResults": max_results}

        if campaign_id_filter:
            request_body["campaignIdFilter"] = {"include": campaign_id_filter}
        if location_id_filter:
            request_body["locationIdFilter"] = {"include": location_id_filter}
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post(
            "/st/locations/list", 
            json_data=request_body,
            content_type=ST_LOCATION_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {"locations": []}

    async def delete_locations(
        self,
        location_ids: list[str],
    ) -> JSONData:
        """删除地理位置定向 - POST /st/locations/delete"""
        result = await self.post(
            "/st/locations/delete", 
            json_data={"locationIds": location_ids},
            content_type=ST_LOCATION_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}
