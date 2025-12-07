"""
Sponsored TV Ads API

端点前缀: /st/ads
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class SponsoredTVAdsAPI(BaseAdsClient):
    """Sponsored TV Ads管理"""
    
    async def create_ads(
        self,
        ads: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """创建广告"""
        return await self._request(
            "POST",
            "/st/ads",
            json={"ads": ads}
        )
    
    async def list_ads(
        self,
        *,
        campaign_id_filter: Optional[List[str]] = None,
        ad_group_id_filter: Optional[List[str]] = None,
        ad_id_filter: Optional[List[str]] = None,
        states: Optional[List[str]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取广告列表"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if campaign_id_filter:
            request_body["campaignIdFilter"] = {"include": campaign_id_filter}
        if ad_group_id_filter:
            request_body["adGroupIdFilter"] = {"include": ad_group_id_filter}
        if ad_id_filter:
            request_body["adIdFilter"] = {"include": ad_id_filter}
        if states:
            request_body["stateFilter"] = {"include": states}
        if next_token:
            request_body["nextToken"] = next_token
            
        return await self._request("POST", "/st/ads/list", json=request_body)
    
    async def update_ads(
        self,
        ads: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """更新广告"""
        return await self._request(
            "PUT",
            "/st/ads",
            json={"ads": ads}
        )
    
    async def delete_ads(
        self,
        ad_ids: List[str],
    ) -> Dict[str, Any]:
        """删除广告"""
        return await self._request(
            "POST",
            "/st/ads/delete",
            json={"adIds": ad_ids}
        )

