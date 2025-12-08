"""
Amazon Ads Sponsored TV Campaigns API (异步版本)
"""

from typing import Any
from ..base import BaseAdsClient, JSONData


class SponsoredTVCampaignsAPI(BaseAdsClient):
    """Sponsored TV Campaigns API (全异步)"""

    async def create_campaigns(
        self,
        campaigns: list[dict[str, Any]],
    ) -> JSONData:
        """创建Sponsored TV广告活动"""
        result = await self.post("/st/campaigns", json_data={"campaigns": campaigns})
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
        """获取Sponsored TV广告活动列表"""
        request_body: dict[str, Any] = {"maxResults": max_results}

        if campaign_ids:
            request_body["campaignIdFilter"] = {"include": campaign_ids}
        if states:
            request_body["stateFilter"] = {"include": states}
        if name_filter:
            request_body["nameFilter"] = name_filter
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post("/st/campaigns/list", json_data=request_body)
        return result if isinstance(result, dict) else {"campaigns": []}

    async def update_campaigns(
        self,
        campaigns: list[dict[str, Any]],
    ) -> JSONData:
        """更新Sponsored TV广告活动"""
        result = await self.put("/st/campaigns", json_data={"campaigns": campaigns})
        return result if isinstance(result, dict) else {}

    async def delete_campaigns(
        self,
        campaign_ids: list[str],
    ) -> JSONData:
        """删除Sponsored TV广告活动"""
        result = await self.post("/st/campaigns/delete", json_data={"campaignIds": campaign_ids})
        return result if isinstance(result, dict) else {}

    async def get_forecasts(
        self,
        forecast_request: dict[str, Any],
    ) -> JSONData:
        """获取Sponsored TV预测"""
        result = await self.post("/st/forecasts", json_data=forecast_request)
        return result if isinstance(result, dict) else {}
