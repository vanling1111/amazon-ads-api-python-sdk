"""Auto-generated async API client. Do not edit manually.

Source: DataProvider_prod_3p.json
Title:  DataProvider
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_data_provider import *  # noqa: F403
except ImportError:
    pass


class DataProviderClient(BaseAdsClient):
    """Auto-generated from DataProvider_prod_3p.json (2 operations)"""

    async def get_campaigns_validation_configs(self, body: getCampaignsValidationConfigsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /validationConfigurations/campaigns

        Retrieves the campaign configuration values used for campaign validation for the requested marketplace,     entityType, 
        """
        endpoint = "/validationConfigurations/campaigns"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.AdsApiValidationConfigsServiceLambda.CampaignsResource.v1+json")

    async def get_targeting_clauses_validation_configs(self, body: getTargetingClausesValidationConfigsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /validationConfigurations/targetingClauses

        Retrieves the configuration values used in targeting clause validation for the requested inputted     marketplace, entit
        """
        endpoint = "/validationConfigurations/targetingClauses"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.AdsApiValidationConfigsServiceLambda.TargetingClausesResource.v1+json")

