"""Auto-generated async API client. Do not edit manually.

Source: Locations_prod_3p.json
Title:  Locations
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_locations import *  # noqa: F403
except ImportError:
    pass


class LocationsClient(BaseAdsClient):
    """Auto-generated from Locations_prod_3p.json (1 operations)"""

    async def list_locations(self, body: ListLocationsRequestBodyV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """POST /locations/list

        Gets location objects based on one or more filters.
        """
        endpoint = "/locations/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

