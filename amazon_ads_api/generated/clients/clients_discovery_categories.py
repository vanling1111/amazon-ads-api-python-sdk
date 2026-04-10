"""Auto-generated async API client. Do not edit manually.

Source: Discovery-AdvertisedProductCategories-V1_prod_3p.json
Title:  Discovery - Advertised Product Categories - V1
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_discovery_categories import *  # noqa: F403
except ImportError:
    pass


class DiscoveryCategoriesClient(BaseAdsClient):
    """Auto-generated from Discovery-AdvertisedProductCategories-V1_prod_3p.json (1 operations)"""

    async def dsp_list_advertised_product_categories_v1(self, body: DspListAdvertisedProductCategoriesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/v1/advertisedProductCategories/list

        Gets the hierarchy of product category objects as a list sorted by ID in ascending order. We use categories to determine
        """
        endpoint = "/dsp/v1/advertisedProductCategories/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

