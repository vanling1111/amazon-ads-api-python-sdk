"""Auto-generated async API client. Do not edit manually.

Source: BrandHome_prod_3p.json
Title:  Brand Home
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_brand_home import *  # noqa: F403
except ImportError:
    pass


class BrandHomeClient(BaseAdsClient):
    """Auto-generated from BrandHome_prod_3p.json (2 operations)"""

    async def list_pages(self, body: ListPagesRequest | dict[str, Any] | None = None) -> JSONData | JSONList:
        """POST /brand/stores/v1/storePages/list

        List all Store pages for Advertiser  **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser Account ID  **Par
        """
        endpoint = "/brand/stores/v1/storePages/list"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, content_type="application/brandStore.ListPages.v1+json")

    async def list_stores(self, body: ListStoresRequest | dict[str, Any] | None = None) -> JSONData | JSONList:
        """POST /brand/stores/v1/stores/list

        Lists all Stores for Advertiser  **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser Account ID  **Paramet
        """
        endpoint = "/brand/stores/v1/stores/list"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, content_type="application/brandStores.ListStores.v1+json")

