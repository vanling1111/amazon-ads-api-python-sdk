"""
Retail Ad Service Product Ads API

端点前缀: /ras/v1/productAds
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class RASProductAdsAPI(BaseAdsClient):
    """Retail Ad Service Product Ads管理"""
    
    async def create_product_ads(
        self,
        product_ads: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """创建产品广告"""
        return await self._request(
            "POST",
            "/ras/v1/productAds",
            json={"productAds": product_ads}
        )
    
    async def list_product_ads(
        self,
        *,
        campaign_id_filter: Optional[List[str]] = None,
        ad_group_id_filter: Optional[List[str]] = None,
        product_ad_id_filter: Optional[List[str]] = None,
        states: Optional[List[str]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取产品广告列表"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if campaign_id_filter:
            request_body["campaignIdFilter"] = {"include": campaign_id_filter}
        if ad_group_id_filter:
            request_body["adGroupIdFilter"] = {"include": ad_group_id_filter}
        if product_ad_id_filter:
            request_body["entityIdFilter"] = {"include": product_ad_id_filter}
        if states:
            request_body["stateFilter"] = {"include": states}
        if next_token:
            request_body["nextToken"] = next_token
            
        return await self._request("POST", "/ras/v1/productAds/list", json=request_body)
    
    async def update_product_ads(
        self,
        product_ads: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """更新产品广告"""
        return await self._request(
            "PUT",
            "/ras/v1/productAds",
            json={"productAds": product_ads}
        )
    
    async def delete_product_ads(
        self,
        product_ad_ids: List[str],
    ) -> Dict[str, Any]:
        """删除产品广告"""
        return await self._request(
            "POST",
            "/ras/v1/productAds/delete",
            json={"productAdIds": product_ad_ids}
        )

