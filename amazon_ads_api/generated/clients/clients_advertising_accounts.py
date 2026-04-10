"""Auto-generated async API client. Do not edit manually.

Source: AdvertisingAccounts_prod_3p.json
Title:  Advertising Accounts
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_advertising_accounts import *  # noqa: F403
except ImportError:
    pass


class AdvertisingAccountsClient(BaseAdsClient):
    """Auto-generated from AdvertisingAccounts_prod_3p.json (3 operations)"""

    async def register_ads_account(self, body: RegisterAdsAccountRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adsAccounts

        Create a new advertising account tied to a specific Amazon vendor, seller or author, or to a business who does not sell 
        """
        endpoint = "/adsAccounts"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.registeradsaccountresource.v1+json")

    async def create_terms_token(self, body: CreateTermsTokenRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /termsTokens

        Create a new UUID terms token for the customer to accept advertising terms
        """
        endpoint = "/termsTokens"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.GlobalRegistrationService.TermsTokenResource.v1.0+json")

    async def get_terms_token(self, terms_token: str, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /termsTokens/{termsToken}

        Get the terms token status for the customer
        """
        endpoint = f"/termsTokens/{terms_token}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

