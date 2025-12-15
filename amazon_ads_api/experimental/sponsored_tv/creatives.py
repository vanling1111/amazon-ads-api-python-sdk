"""
Amazon Ads Sponsored TV Creatives API (异步版本)

API Tier: L4 (Experimental - Beta)
Source: https://advertising.amazon.com/API/docs/en-us/sponsored-tv
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData

ST_CREATIVE_CONTENT_TYPE = "application/vnd.stCreative.v1+json"
ST_MODERATION_CONTENT_TYPE = "application/vnd.stCreativeModeration.v1+json"
ST_PREVIEW_CONTENT_TYPE = "application/vnd.stCreativePreview.v1+json"


class SponsoredTVCreativesAPI(BaseAdsClient):
    """Sponsored TV Creatives API (全异步)"""

    async def create_creatives(
        self,
        creatives: list[dict[str, Any]],
    ) -> JSONData:
        """创建创意 - POST /st/creatives"""
        result = await self.post(
            "/st/creatives", 
            json_data={"creatives": creatives},
            content_type=ST_CREATIVE_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    async def list_creatives(
        self,
        *,
        creative_id_filter: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取创意列表 - POST /st/creatives/list"""
        request_body: dict[str, Any] = {"maxResults": max_results}

        if creative_id_filter:
            request_body["creativeIdFilter"] = {"include": creative_id_filter}
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post(
            "/st/creatives/list", 
            json_data=request_body,
            content_type=ST_CREATIVE_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {"creatives": []}

    async def update_creatives(
        self,
        creatives: list[dict[str, Any]],
    ) -> JSONData:
        """更新创意 - PUT /st/creatives"""
        result = await self.put(
            "/st/creatives", 
            json_data={"creatives": creatives},
            content_type=ST_CREATIVE_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    async def list_moderations(
        self,
        *,
        creative_id_filter: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取创意审核状态列表 - POST /st/creatives/moderations/list"""
        request_body: dict[str, Any] = {"maxResults": max_results}

        if creative_id_filter:
            request_body["creativeIdFilter"] = {"include": creative_id_filter}
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post(
            "/st/creatives/moderations/list", 
            json_data=request_body,
            content_type=ST_MODERATION_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {"moderations": []}

    async def list_policy_violations(
        self,
        *,
        creative_id_filter: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取创意政策违规列表 - POST /st/creatives/moderations/policyViolations/list"""
        request_body: dict[str, Any] = {"maxResults": max_results}

        if creative_id_filter:
            request_body["creativeIdFilter"] = {"include": creative_id_filter}
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post(
            "/st/creatives/moderations/policyViolations/list", 
            json_data=request_body,
            content_type=ST_MODERATION_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {"violations": []}

    async def preview_creative(
        self,
        preview_request: dict[str, Any],
    ) -> JSONData:
        """预览创意 - POST /st/creatives/preview"""
        result = await self.post(
            "/st/creatives/preview", 
            json_data=preview_request,
            content_type=ST_PREVIEW_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}
