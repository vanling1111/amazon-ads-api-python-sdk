"""
Sponsored Products - Product Ads API (异步版本)
SP商品广告管理

API Tier: L1 (OpenAPI Verified)
Source: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json
OpenAPI: ✅
Stability: 高
"""

from amazon_ads_api.base import JSONData, JSONList

try:
    from amazon_ads_api.generated.clients.clients_sp import SpClient as _GenBase
except ImportError:
    from amazon_ads_api.base import BaseAdsClient as _GenBase  # type: ignore[assignment]

# API v3 Content-Type
CONTENT_TYPE_PRODUCT_AD = "application/vnd.spProductAd.v3+json"


class SPProductAdsAPI(_GenBase):
    """SP Product Ads API (全异步)

    基于官方OpenAPI规范实现：
    - POST /sp/productAds - 创建Product Ads
    - PUT /sp/productAds - 更新Product Ads
    - POST /sp/productAds/delete - 删除Product Ads
    - POST /sp/productAds/list - 列出Product Ads
    """

    API_TIER = "L1"
    API_SOURCE = "openapi"

    async def create_product_ads(self, product_ads: JSONList) -> JSONData:
        """
        批量创建Product Ads

        POST /sp/productAds

        Args:
            product_ads: Product Ad列表
            [
                {
                    "campaignId": "123456789",
                    "adGroupId": "987654321",
                    "state": "ENABLED",  # ENABLED | PAUSED
                    "asin": "B08N5WRWNW",  # For vendors
                    # OR
                    "sku": "MY-SKU-001"  # For sellers
                }
            ]

        Returns:
            {
                "productAds": {
                    "success": [
                        {
                            "adId": "123",
                            "index": 0
                        }
                    ],
                    "error": []
                }
            }

        Required fields:
            - adGroupId: Ad Group ID
            - campaignId: Campaign ID  
            - state: ENABLED | PAUSED
            - asin (vendors) OR sku (sellers): 二选一

        OpenAPI Schema: SponsoredProductsCreateSponsoredProductsProductAdsRequestContent
        """
        payload = {"productAds": product_ads}
        result = await self.post(
            "/sp/productAds",
            json_data=payload,
            content_type=CONTENT_TYPE_PRODUCT_AD
        )

        # 解析207 Multi-Status响应
        # OpenAPI定义的返回格式已经是 {"productAds": {"success": [...], "error": [...]}}
        return result

    async def update_product_ads(self, product_ads: JSONList) -> JSONData:
        """
        批量更新Product Ads

        PUT /sp/productAds

        Args:
            product_ads: Product Ad更新列表
            [
                {
                    "adId": "123456789",
                    "state": "PAUSED"  # ENABLED | PAUSED
                }
            ]

        Returns:
            {
                "productAds": {
                    "success": [
                        {
                            "adId": "123",
                            "index": 0
                        }
                    ],
                    "error": []
                }
            }

        Required fields:
            - adId: Product Ad ID

        Optional fields:
            - state: ENABLED | PAUSED

        OpenAPI Schema: SponsoredProductsUpdateSponsoredProductsProductAdsRequestContent
        """
        payload = {"productAds": product_ads}
        result = await self.put(
            "/sp/productAds",
            json_data=payload,
            content_type=CONTENT_TYPE_PRODUCT_AD
        )
        return result

    async def delete_product_ads(self, ad_ids: list[str]) -> JSONData:
        """
        批量删除Product Ads

        POST /sp/productAds/delete

        Args:
            ad_ids: Product Ad ID列表

        Returns:
            {
                "productAds": {
                    "success": [
                        {
                            "adId": "123",
                            "index": 0
                        }
                    ],
                    "error": []
                }
            }

        OpenAPI Schema: SponsoredProductsDeleteSponsoredProductsProductAdsRequestContent
        Note: 使用 adIdFilter.include 格式
        """
        payload = {
            "adIdFilter": {
                "include": ad_ids
            }
        }
        result = await self.post(
            "/sp/productAds/delete",
            json_data=payload,
            content_type=CONTENT_TYPE_PRODUCT_AD
        )
        return result

    async def list_product_ads(
        self,
        ad_ids: list[str] | None = None,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        state_filter: list[str] | str | None = None,
        max_results: int | None = None,
        next_token: str | None = None,
        include_extended_data: bool = False,
    ) -> JSONData:
        """
        列出Product Ads

        POST /sp/productAds/list

        Args:
            ad_ids: Product Ad ID过滤
            ad_group_id: Ad Group ID过滤
            campaign_id: Campaign ID过滤
            state_filter: 状态过滤 ["ENABLED", "PAUSED", "ARCHIVED"]
            max_results: 最大结果数
            next_token: 分页token
            include_extended_data: 是否包含扩展字段（creationDate, lastUpdateDate, servingStatus）

        Returns:
            {
                "productAds": [...],
                "nextToken": "..."  # 如果有下一页
            }

        OpenAPI Schema: SponsoredProductsListSponsoredProductsProductAdsRequestContent
        Response: 200 OK (not 207)
        """
        params: JSONData = {}

        # Ad ID过滤 - 格式: {"include": [...]}
        if ad_ids:
            params["adIdFilter"] = {"include": ad_ids}

        # Ad Group ID过滤 - 使用ReducedObjectIdFilter格式
        if ad_group_id:
            params["adGroupIdFilter"] = {"include": [ad_group_id]}

        # Campaign ID过滤 - 使用ReducedObjectIdFilter格式
        if campaign_id:
            params["campaignIdFilter"] = {"include": [campaign_id]}

        # 状态过滤 - 格式: {"include": ["ENABLED", ...]}
        if state_filter:
            states = [state_filter] if isinstance(state_filter, str) else state_filter
            params["stateFilter"] = {"include": [s.upper() for s in states]}

        if max_results is not None:
            params["maxResults"] = max_results

        if next_token:
            params["nextToken"] = next_token

        if include_extended_data:
            params["includeExtendedDataFields"] = True

        result = await self.post(
            "/sp/productAds/list",
            json_data=params,
            content_type=CONTENT_TYPE_PRODUCT_AD
        )

        # list接口返回200 OK，格式: {"productAds": [...], "nextToken": "..."}
        if not isinstance(result, dict):
            return {"productAds": []}
        return result

    async def archive_product_ad(self, ad_id: str) -> JSONData:
        """
        归档单个Product Ad（便利方法）

        内部调用 delete_product_ads([ad_id])

        Args:
            ad_id: Product Ad ID

        Returns:
            {
                "productAds": {
                    "success": [{"adId": "123", "index": 0}],
                    "error": []
                }
            }
        """
        return await self.delete_product_ads([ad_id])

