"""
Amazon Ads Sponsored TV Creatives API (异步版本)
"""

from typing import Any
from ..base import BaseAdsClient, JSONData


class SponsoredTVCreativesAPI(BaseAdsClient):
    """Sponsored TV Creatives API (全异步)"""

    async def create_creatives(
        self,
        creatives: list[dict[str, Any]],
    ) -> JSONData:
        """创建创意"""
        result = await self.post("/st/creatives", json_data={"creatives": creatives})
        return result if isinstance(result, dict) else {}

    async def list_creatives(
        self,
        *,
        creative_id_filter: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取创意列表"""
        request_body: dict[str, Any] = {"maxResults": max_results}

        if creative_id_filter:
            request_body["creativeIdFilter"] = {"include": creative_id_filter}
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post("/st/creatives/list", json_data=request_body)
        return result if isinstance(result, dict) else {"creatives": []}

    async def update_creatives(
        self,
        creatives: list[dict[str, Any]],
    ) -> JSONData:
        """更新创意"""
        result = await self.put("/st/creatives", json_data={"creatives": creatives})
        return result if isinstance(result, dict) else {}

    async def list_moderations(
        self,
        *,
        creative_id_filter: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取创意审核状态列表"""
        request_body: dict[str, Any] = {"maxResults": max_results}

        if creative_id_filter:
            request_body["creativeIdFilter"] = {"include": creative_id_filter}
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post("/st/creatives/moderations/list", json_data=request_body)
        return result if isinstance(result, dict) else {"moderations": []}

    async def list_policy_violations(
        self,
        *,
        creative_id_filter: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取创意政策违规列表"""
        request_body: dict[str, Any] = {"maxResults": max_results}

        if creative_id_filter:
            request_body["creativeIdFilter"] = {"include": creative_id_filter}
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post(
            "/st/creatives/moderations/policyViolations/list", json_data=request_body
        )
        return result if isinstance(result, dict) else {"violations": []}

    async def preview_creative(
        self,
        preview_request: dict[str, Any],
    ) -> JSONData:
        """预览创意"""
        result = await self.post("/st/creatives/preview", json_data=preview_request)
        return result if isinstance(result, dict) else {}
