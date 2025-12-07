"""
Brand Home API - 品牌主页

官方文档: https://advertising.amazon.com/API/docs/en-us/brand-home
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class BrandHomeAPI(BaseAdsClient):
    """Brand Home API - 管理品牌主页"""
    
    async def get_brand_home(
        self,
        brand_entity_id: str,
    ) -> Dict[str, Any]:
        """获取品牌主页信息"""
        return await self._request(
            "GET",
            f"/brandHome/{brand_entity_id}"
        )
    
    async def list_brand_homes(
        self,
        *,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取品牌主页列表"""
        params: Dict[str, Any] = {"maxResults": max_results}
        if next_token:
            params["nextToken"] = next_token
        return await self._request("GET", "/brandHome", params=params)
    
    async def get_brand_metrics(
        self,
        brand_entity_id: str,
        *,
        start_date: str,
        end_date: str,
        metrics: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """获取品牌主页指标"""
        request_body: Dict[str, Any] = {
            "startDate": start_date,
            "endDate": end_date,
        }
        if metrics:
            request_body["metrics"] = metrics
            
        return await self._request(
            "POST",
            f"/brandHome/{brand_entity_id}/metrics",
            json=request_body
        )
    
    async def get_brand_insights(
        self,
        brand_entity_id: str,
    ) -> Dict[str, Any]:
        """获取品牌洞察"""
        return await self._request(
            "GET",
            f"/brandHome/{brand_entity_id}/insights"
        )

