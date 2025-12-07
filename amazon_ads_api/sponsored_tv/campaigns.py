"""
Sponsored TV Campaigns API

基于Go SDK: pkg/adsapi/sponsored-tv/
端点前缀: /st/campaigns
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class SponsoredTVCampaignsAPI(BaseAdsClient):
    """Sponsored TV Campaigns管理"""
    
    async def create_campaigns(
        self,
        campaigns: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """创建Sponsored TV广告活动"""
        return await self._request(
            "POST",
            "/st/campaigns",
            json={"campaigns": campaigns}
        )
    
    async def list_campaigns(
        self,
        *,
        campaign_ids: Optional[List[str]] = None,
        states: Optional[List[str]] = None,
        name_filter: Optional[Dict[str, Any]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取Sponsored TV广告活动列表"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if campaign_ids:
            request_body["campaignIdFilter"] = {"include": campaign_ids}
        if states:
            request_body["stateFilter"] = {"include": states}
        if name_filter:
            request_body["nameFilter"] = name_filter
        if next_token:
            request_body["nextToken"] = next_token
            
        return await self._request("POST", "/st/campaigns/list", json=request_body)
    
    async def update_campaigns(
        self,
        campaigns: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """更新Sponsored TV广告活动"""
        return await self._request(
            "PUT",
            "/st/campaigns",
            json={"campaigns": campaigns}
        )
    
    async def delete_campaigns(
        self,
        campaign_ids: List[str],
    ) -> Dict[str, Any]:
        """删除Sponsored TV广告活动"""
        return await self._request(
            "POST",
            "/st/campaigns/delete",
            json={"campaignIds": campaign_ids}
        )
    
    async def get_forecasts(
        self,
        forecast_request: Dict[str, Any],
    ) -> Dict[str, Any]:
        """获取Sponsored TV预测"""
        return await self._request(
            "POST",
            "/st/forecasts",
            json=forecast_request
        )

