"""
Amazon Ads Retail Ad Service Ad Groups API (异步版本)
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData


class RASAdGroupsAPI(BaseAdsClient):
    """Retail Ad Service Ad Groups API (全异步)"""

    async def create_ad_groups(
        self,
        ad_groups: list[dict[str, Any]],
    ) -> JSONData:
        """创建广告组"""
        result = await self.post("/ras/v1/adGroups", json_data={"adGroups": ad_groups})
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
        """获取广告组列表"""
        request_body: dict[str, Any] = {"maxResults": max_results}

        if campaign_id_filter:
            request_body["campaignIdFilter"] = {"include": campaign_id_filter}
        if ad_group_id_filter:
            request_body["entityIdFilter"] = {"include": ad_group_id_filter}
        if states:
            request_body["stateFilter"] = {"include": states}
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post("/ras/v1/adGroups/list", json_data=request_body)
        return result if isinstance(result, dict) else {"adGroups": []}

    async def update_ad_groups(
        self,
        ad_groups: list[dict[str, Any]],
    ) -> JSONData:
        """更新广告组"""
        result = await self.put("/ras/v1/adGroups", json_data={"adGroups": ad_groups})
        return result if isinstance(result, dict) else {}

    async def delete_ad_groups(
        self,
        ad_group_ids: list[str],
    ) -> JSONData:
        """删除广告组
        
        官方请求格式: {"adGroupIdFilter": {"include": [...]}}
        """
        result = await self.post(
            "/ras/v1/adGroups/delete", 
            json_data={"adGroupIdFilter": {"include": ad_group_ids}}
        )
        return result if isinstance(result, dict) else {}
