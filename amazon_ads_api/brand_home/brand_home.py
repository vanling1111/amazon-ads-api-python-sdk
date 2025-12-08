"""
Brand Home API - 品牌主页 (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/brand-home
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient, JSONData


class BrandHomeAPI(BaseAdsClient):
    """Brand Home API - 管理品牌主页 (全异步)"""
    
    async def get_brand_home(
        self,
        brand_entity_id: str,
    ) -> JSONData:
        """获取品牌主页信息"""
        result = await self.get(f"/brandHome/{brand_entity_id}")
        return result if isinstance(result, dict) else {}
    
    async def list_brand_homes(
        self,
        *,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """获取品牌主页列表"""
        params: Dict[str, Any] = {"maxResults": max_results}
        if next_token:
            params["nextToken"] = next_token
        result = await self.get("/brandHome", params=params)
        return result if isinstance(result, dict) else {"brandHomes": []}
    
    async def get_brand_metrics(
        self,
        brand_entity_id: str,
        *,
        start_date: str,
        end_date: str,
        metrics: Optional[List[str]] = None,
    ) -> JSONData:
        """获取品牌主页指标"""
        request_body: Dict[str, Any] = {
            "startDate": start_date,
            "endDate": end_date,
        }
        if metrics:
            request_body["metrics"] = metrics
            
        result = await self.post(
            f"/brandHome/{brand_entity_id}/metrics",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {}
    
    async def get_brand_insights(
        self,
        brand_entity_id: str,
    ) -> JSONData:
        """获取品牌洞察"""
        result = await self.get(f"/brandHome/{brand_entity_id}/insights")
        return result if isinstance(result, dict) else {}
