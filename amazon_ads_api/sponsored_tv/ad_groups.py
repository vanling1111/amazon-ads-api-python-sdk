"""
Sponsored TV Ad Groups API

端点前缀: /st/adGroups
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class SponsoredTVAdGroupsAPI(BaseAdsClient):
    """Sponsored TV Ad Groups管理"""
    
    async def create_ad_groups(
        self,
        ad_groups: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """创建广告组"""
        return await self._request(
            "POST",
            "/st/adGroups",
            json={"adGroups": ad_groups}
        )
    
    async def list_ad_groups(
        self,
        *,
        campaign_id_filter: Optional[List[str]] = None,
        ad_group_id_filter: Optional[List[str]] = None,
        states: Optional[List[str]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取广告组列表"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if campaign_id_filter:
            request_body["campaignIdFilter"] = {"include": campaign_id_filter}
        if ad_group_id_filter:
            request_body["adGroupIdFilter"] = {"include": ad_group_id_filter}
        if states:
            request_body["stateFilter"] = {"include": states}
        if next_token:
            request_body["nextToken"] = next_token
            
        return await self._request("POST", "/st/adGroups/list", json=request_body)
    
    async def update_ad_groups(
        self,
        ad_groups: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """更新广告组"""
        return await self._request(
            "PUT",
            "/st/adGroups",
            json={"adGroups": ad_groups}
        )
    
    async def delete_ad_groups(
        self,
        ad_group_ids: List[str],
    ) -> Dict[str, Any]:
        """删除广告组"""
        return await self._request(
            "POST",
            "/st/adGroups/delete",
            json={"adGroupIds": ad_group_ids}
        )

