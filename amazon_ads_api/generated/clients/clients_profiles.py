"""Auto-generated async API client. Do not edit manually.

Source: Profiles_prod_3p.json
Title:  Profiles
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_profiles import *  # noqa: F403
except ImportError:
    pass


class ProfilesClient(BaseAdsClient):
    """Auto-generated from Profiles_prod_3p.json (1 operations)"""

    async def list_profiles(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, valid_payment_method_filter: str | None = None, profile_type_filter: str | None = None, exclude_sub_type_filter: str | None = None) -> JSONData | JSONList:
        """GET /profiles

        Note that this operation does not return a response unless the current account has created at least one campaign using t
        """
        endpoint = "/profiles"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if valid_payment_method_filter is not None:
            params["validPaymentMethodFilter"] = valid_payment_method_filter
        if profile_type_filter is not None:
            params["profileTypeFilter"] = profile_type_filter
        if exclude_sub_type_filter is not None:
            params["excludeSubTypeFilter"] = exclude_sub_type_filter
        return await self.get(endpoint, params=params)

