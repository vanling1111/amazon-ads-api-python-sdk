"""Auto-generated async API client. Do not edit manually.

Source: Profiles_v3_openapi.yaml
Title:  Amazon Ads API - Profiles
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_profiles_v3 import *  # noqa: F403
except ImportError:
    pass


class ProfilesV3Client(BaseAdsClient):
    """Auto-generated from Profiles_v3_openapi.yaml (3 operations)"""

    async def list_profiles(self, amazon_advertising_api_client_id: str | None = None, api_program: str | None = None, access_level: str | None = None, profile_type_filter: str | None = None, valid_payment_method_filter: str | None = None) -> JSONData | JSONList:
        """GET /v2/profiles

        Gets a list of profiles.
        """
        endpoint = "/v2/profiles"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if api_program is not None:
            params["apiProgram"] = api_program
        if access_level is not None:
            params["accessLevel"] = access_level
        if profile_type_filter is not None:
            params["profileTypeFilter"] = profile_type_filter
        if valid_payment_method_filter is not None:
            params["validPaymentMethodFilter"] = valid_payment_method_filter
        return await self.get(endpoint, params=params)

    async def update_profiles(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """PUT /v2/profiles

        Update the daily budget for one or more profiles.
        """
        endpoint = "/v2/profiles"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params)

    async def get_profile_by_id(self, profile_id: str, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /v2/profiles/{profileId}

        Gets a profile specified by identifier.
        """
        endpoint = f"/v2/profiles/{profile_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

