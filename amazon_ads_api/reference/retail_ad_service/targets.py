"""
Amazon Ads Retail Ad Service Targets API (异步版本)
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData


class RASTargetsAPI(BaseAdsClient):
    """Retail Ad Service Targets API (全异步)"""

    async def create_targets(
        self,
        targets: list[dict[str, Any]],
    ) -> JSONData:
        """创建定向"""
        result = await self.post("/ras/v1/targets", json_data={"targets": targets})
        return result if isinstance(result, dict) else {}

    async def list_targets(
        self,
        *,
        campaign_id_filter: list[str] | None = None,
        ad_group_id_filter: list[str] | None = None,
        target_id_filter: list[str] | None = None,
        states: list[str] | None = None,
        target_type_filter: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取定向列表"""
        request_body: dict[str, Any] = {"maxResults": max_results}

        if campaign_id_filter:
            request_body["campaignIdFilter"] = {"include": campaign_id_filter}
        if ad_group_id_filter:
            request_body["adGroupIdFilter"] = {"include": ad_group_id_filter}
        if target_id_filter:
            request_body["entityIdFilter"] = {"include": target_id_filter}
        if states:
            request_body["stateFilter"] = {"include": states}
        if target_type_filter:
            request_body["targetTypeFilter"] = {"include": target_type_filter}
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post("/ras/v1/targets/list", json_data=request_body)
        return result if isinstance(result, dict) else {"targets": []}

    async def update_targets(
        self,
        targets: list[dict[str, Any]],
    ) -> JSONData:
        """更新定向"""
        result = await self.put("/ras/v1/targets", json_data={"targets": targets})
        return result if isinstance(result, dict) else {}

    async def delete_targets(
        self,
        target_ids: list[str],
    ) -> JSONData:
        """删除定向
        
        官方请求格式: {"targetIdFilter": {"include": [...]}}
        """
        result = await self.post(
            "/ras/v1/targets/delete", 
            json_data={"targetIdFilter": {"include": target_ids}}
        )
        return result if isinstance(result, dict) else {}
