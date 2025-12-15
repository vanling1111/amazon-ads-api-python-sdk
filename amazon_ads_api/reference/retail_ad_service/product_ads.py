"""
Amazon Ads Retail Ad Service Product Ads API (异步版本)
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData


class RASProductAdsAPI(BaseAdsClient):
    """Retail Ad Service Product Ads API (全异步)"""

    async def create_product_ads(
        self,
        product_ads: list[dict[str, Any]],
    ) -> JSONData:
        """创建产品广告"""
        result = await self.post("/ras/v1/productAds", json_data={"productAds": product_ads})
        return result if isinstance(result, dict) else {}

    async def list_product_ads(
        self,
        *,
        campaign_id_filter: list[str] | None = None,
        ad_group_id_filter: list[str] | None = None,
        product_ad_id_filter: list[str] | None = None,
        states: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取产品广告列表"""
        request_body: dict[str, Any] = {"maxResults": max_results}

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

        result = await self.post("/ras/v1/productAds/list", json_data=request_body)
        return result if isinstance(result, dict) else {"productAds": []}

    async def update_product_ads(
        self,
        product_ads: list[dict[str, Any]],
    ) -> JSONData:
        """更新产品广告"""
        result = await self.put("/ras/v1/productAds", json_data={"productAds": product_ads})
        return result if isinstance(result, dict) else {}

    async def delete_product_ads(
        self,
        product_ad_ids: list[str],
    ) -> JSONData:
        """删除产品广告
        
        官方请求格式: {"productAdIdFilter": {"include": [...]}}
        """
        result = await self.post(
            "/ras/v1/productAds/delete", 
            json_data={"productAdIdFilter": {"include": product_ad_ids}}
        )
        return result if isinstance(result, dict) else {}
