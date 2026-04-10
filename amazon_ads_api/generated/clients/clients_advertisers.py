"""Auto-generated async API client. Do not edit manually.

Source: Advertisers_prod_3p.json
Title:  Advertisers
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_advertisers import *  # noqa: F403
except ImportError:
    pass


class AdvertisersClient(BaseAdsClient):
    """Auto-generated from Advertisers_prod_3p.json (2 operations)"""

    async def get_account_budget_feature_flags(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /accountBudgets/featureFlags

        Gets account budget feature flags information.
        """
        endpoint = "/accountBudgets/featureFlags"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def update_account_budget_feature_flags(self, body: UpdateAccountBudgetFeatureFlagsRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /accountBudgets/featureFlags

        Creates or Updates account budget feature flags information.
        """
        endpoint = "/accountBudgets/featureFlags"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.accountBudgetFeatureFlags.v1+json")

