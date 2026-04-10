"""Auto-generated async API client. Do not edit manually.

Source: RetailerIdentityAPIforRetailAdService_prod_3p.json
Title:  Retailer Identity API for Retail Ad Service
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_retail_identity import *  # noqa: F403
except ImportError:
    pass


class RetailIdentityClient(BaseAdsClient):
    """Auto-generated from RetailerIdentityAPIforRetailAdService_prod_3p.json (1 operations)"""

    async def ra_sv1_list_retailers(self, body: ListRetailersRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /ras/v1/retailers/list

        Returns a list of Retailers.
        """
        endpoint = "/ras/v1/retailers/list"
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

