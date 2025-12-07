"""
Sponsored TV Creatives API

端点前缀: /st/creatives
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class SponsoredTVCreativesAPI(BaseAdsClient):
    """Sponsored TV Creatives管理"""
    
    async def create_creatives(
        self,
        creatives: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """创建创意"""
        return await self._request(
            "POST",
            "/st/creatives",
            json={"creatives": creatives}
        )
    
    async def list_creatives(
        self,
        *,
        creative_id_filter: Optional[List[str]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取创意列表"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if creative_id_filter:
            request_body["creativeIdFilter"] = {"include": creative_id_filter}
        if next_token:
            request_body["nextToken"] = next_token
            
        return await self._request("POST", "/st/creatives/list", json=request_body)
    
    async def update_creatives(
        self,
        creatives: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """更新创意"""
        return await self._request(
            "PUT",
            "/st/creatives",
            json={"creatives": creatives}
        )
    
    async def list_moderations(
        self,
        *,
        creative_id_filter: Optional[List[str]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取创意审核状态列表"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if creative_id_filter:
            request_body["creativeIdFilter"] = {"include": creative_id_filter}
        if next_token:
            request_body["nextToken"] = next_token
            
        return await self._request("POST", "/st/creatives/moderations/list", json=request_body)
    
    async def list_policy_violations(
        self,
        *,
        creative_id_filter: Optional[List[str]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取创意政策违规列表"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if creative_id_filter:
            request_body["creativeIdFilter"] = {"include": creative_id_filter}
        if next_token:
            request_body["nextToken"] = next_token
            
        return await self._request(
            "POST",
            "/st/creatives/moderations/policyViolations/list",
            json=request_body
        )
    
    async def preview_creative(
        self,
        preview_request: Dict[str, Any],
    ) -> Dict[str, Any]:
        """预览创意"""
        return await self._request(
            "POST",
            "/st/creatives/preview",
            json=preview_request
        )

