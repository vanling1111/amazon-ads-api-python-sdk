"""Auto-generated async API client. Do not edit manually.

Source: AdvertisingTestAccount_prod_3p.json
Title:  AdvertisingTestAccount
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_test_accounts import *  # noqa: F403
except ImportError:
    pass


class TestAccountsClient(BaseAdsClient):
    """Auto-generated from AdvertisingTestAccount_prod_3p.json (2 operations)"""

    async def get_account_information(self, request_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /testAccounts

        API to get Account information.
        """
        endpoint = "/testAccounts"
        params: dict[str, Any] = {}
        if request_id is not None:
            params["requestId"] = request_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

    async def create_account(self, body: CreateAccountRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /testAccounts

        API to create test accounts
        """
        endpoint = "/testAccounts"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

