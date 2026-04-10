"""Auto-generated async API client. Do not edit manually.

Source: Eligibility_prod_3p.json
Title:  Eligibility
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_eligibility import *  # noqa: F403
except ImportError:
    pass


class EligibilityClient(BaseAdsClient):
    """Auto-generated from Eligibility_prod_3p.json (2 operations)"""

    async def product_eligibility(self, body: ProductEligibilityRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /eligibility/product/list

        Gets advertising eligibility status for a list of products.
        """
        endpoint = "/eligibility/product/list"
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

    async def program_eligibility(self, body: ProgramEligibilityRequestContent | dict[str, Any] | None = None, accept_language: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, content_type: str | None = None) -> JSONData | JSONList:
        """POST /eligibility/programs

        Checks the advertiser's eligibility to ad programs.  **Authorized resource type**: Global Ad Account ID, Profile ID  **P
        """
        endpoint = "/eligibility/programs"
        params: dict[str, Any] = {}
        if accept_language is not None:
            params["Accept-Language"] = accept_language
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if content_type is not None:
            params["Content-Type"] = content_type
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

