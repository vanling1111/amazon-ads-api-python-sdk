"""Auto-generated async API client. Do not edit manually.

Source: ProductSelector_prod_3p.json
Title:  Product Selector
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_product_selector import *  # noqa: F403
except ImportError:
    pass


class ProductSelectorClient(BaseAdsClient):
    """Auto-generated from ProductSelector_prod_3p.json (1 operations)"""

    async def product_metadata(self, body: ProductMetadataRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /product/metadata

        Returns product metadata for the advertiser
        """
        endpoint = "/product/metadata"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.productmetadatarequest.v1+json")

