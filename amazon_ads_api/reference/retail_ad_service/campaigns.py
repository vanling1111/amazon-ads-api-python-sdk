"""
Amazon Ads Retail Ad Service Campaigns API (异步版本)
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData


class RASCampaignsAPI(BaseAdsClient):
    """Retail Ad Service Campaigns API (全异步)"""

    async def create_campaigns(
        self,
        campaigns: list[dict[str, Any]],
    ) -> JSONData:
        """创建RAS广告活动"""
        result = await self.post("/ras/v1/campaigns", json_data={"campaigns": campaigns})
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
        """获取RAS广告活动列表"""
        request_body: dict[str, Any] = {"maxResults": max_results}

        if campaign_ids:
            request_body["entityIdFilter"] = {"include": campaign_ids}
        if states:
            request_body["stateFilter"] = {"include": states}
        if name_filter:
            request_body["nameFilter"] = name_filter
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post("/ras/v1/campaigns/list", json_data=request_body)
        return result if isinstance(result, dict) else {"campaigns": []}

    async def update_campaigns(
        self,
        campaigns: list[dict[str, Any]],
    ) -> JSONData:
        """更新RAS广告活动"""
        result = await self.put("/ras/v1/campaigns", json_data={"campaigns": campaigns})
        return result if isinstance(result, dict) else {}

    async def delete_campaigns(
        self,
        campaign_ids: list[str],
    ) -> JSONData:
        """删除RAS广告活动
        
        官方请求格式: {"campaignIdFilter": {"include": [...]}}
        """
        result = await self.post(
            "/ras/v1/campaigns/delete", 
            json_data={"campaignIdFilter": {"include": campaign_ids}}
        )
        return result if isinstance(result, dict) else {}
