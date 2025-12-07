"""
Sponsored TV Targeting API

端点前缀: /st/targets, /st/locations
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class SponsoredTVTargetingAPI(BaseAdsClient):
    """Sponsored TV Targeting管理"""
    
    # ==================== Targeting Clauses ====================
    
    async def create_targeting_clauses(
        self,
        targets: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """创建定向条件"""
        return await self._request(
            "POST",
            "/st/targets",
            json={"targets": targets}
        )
    
    async def list_targeting_clauses(
        self,
        *,
        campaign_id_filter: Optional[List[str]] = None,
        ad_group_id_filter: Optional[List[str]] = None,
        target_id_filter: Optional[List[str]] = None,
        states: Optional[List[str]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取定向条件列表"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
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
            
        return await self._request("POST", "/st/targets/list", json=request_body)
    
    async def update_targeting_clauses(
        self,
        targets: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """更新定向条件"""
        return await self._request(
            "PUT",
            "/st/targets",
            json={"targets": targets}
        )
    
    async def delete_targeting_clauses(
        self,
        target_ids: List[str],
    ) -> Dict[str, Any]:
        """删除定向条件"""
        return await self._request(
            "POST",
            "/st/targets/delete",
            json={"targetIds": target_ids}
        )
    
    # ==================== Locations ====================
    
    async def create_locations(
        self,
        locations: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """创建地理位置定向"""
        return await self._request(
            "POST",
            "/st/locations",
            json={"locations": locations}
        )
    
    async def list_locations(
        self,
        *,
        campaign_id_filter: Optional[List[str]] = None,
        location_id_filter: Optional[List[str]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取地理位置定向列表"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if campaign_id_filter:
            request_body["campaignIdFilter"] = {"include": campaign_id_filter}
        if location_id_filter:
            request_body["locationIdFilter"] = {"include": location_id_filter}
        if next_token:
            request_body["nextToken"] = next_token
            
        return await self._request("POST", "/st/locations/list", json=request_body)
    
    async def delete_locations(
        self,
        location_ids: List[str],
    ) -> Dict[str, Any]:
        """删除地理位置定向"""
        return await self._request(
            "POST",
            "/st/locations/delete",
            json={"locationIds": location_ids}
        )

