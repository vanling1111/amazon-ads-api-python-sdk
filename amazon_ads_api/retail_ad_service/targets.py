"""
Retail Ad Service Targets API

端点前缀: /ras/v1/targets
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class RASTargetsAPI(BaseAdsClient):
    """Retail Ad Service Targets管理"""
    
    async def create_targets(
        self,
        targets: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """创建定向"""
        return await self._request(
            "POST",
            "/ras/v1/targets",
            json={"targets": targets}
        )
    
    async def list_targets(
        self,
        *,
        campaign_id_filter: Optional[List[str]] = None,
        ad_group_id_filter: Optional[List[str]] = None,
        target_id_filter: Optional[List[str]] = None,
        states: Optional[List[str]] = None,
        target_type_filter: Optional[List[str]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取定向列表"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
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
            
        return await self._request("POST", "/ras/v1/targets/list", json=request_body)
    
    async def update_targets(
        self,
        targets: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """更新定向"""
        return await self._request(
            "PUT",
            "/ras/v1/targets",
            json={"targets": targets}
        )
    
    async def delete_targets(
        self,
        target_ids: List[str],
    ) -> Dict[str, Any]:
        """删除定向"""
        return await self._request(
            "POST",
            "/ras/v1/targets/delete",
            json={"targetIds": target_ids}
        )

