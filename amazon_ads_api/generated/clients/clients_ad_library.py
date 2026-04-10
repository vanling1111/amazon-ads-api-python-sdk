"""Auto-generated async API client. Do not edit manually.

Source: AdLibraryAPI_prod_3p.json
Title:  Ad Library API
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_ad_library import *  # noqa: F403
except ImportError:
    pass


class AdLibraryClient(BaseAdsClient):
    """Auto-generated from AdLibraryAPI_prod_3p.json (2 operations)"""

    async def list_ads(self, body: ListAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adRepository/ads/list

        This is the primary paginated API for retrieving, listing, and searching through the ad repository. By default, a reques
        """
        endpoint = "/adRepository/ads/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.adsrepository.v1.1+json")

    async def get_ads_by_id(self, id: str, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /adRepository/ads/{id}

        This is the API for retrieving a single advertisement metadata specified by its id from the ad repository.  **Requires o
        """
        endpoint = f"/adRepository/ads/{id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

