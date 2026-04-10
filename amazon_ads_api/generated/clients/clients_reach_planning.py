"""Auto-generated async API client. Do not edit manually.

Source: ReachPlanningService_prod_3p.json
Title:  Reach Planning Service
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_reach_planning import *  # noqa: F403
except ImportError:
    pass


class ReachPlanningClient(BaseAdsClient):
    """Auto-generated from ReachPlanningService_prod_3p.json (5 operations)"""

    async def create_deduplicated_reach_forecasts_v1(self, body: CreateDeduplicatedReachForecastsV1RequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /mediaPlan/v1/deduplicatedReachForecasts

        Creates a list of De-duplicated Reach Forecasts.  **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser Acco
        """
        endpoint = "/mediaPlan/v1/deduplicatedReachForecasts"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-AccountId"] = amazon_ads_manager_account_id
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

    async def generate_performance_forecasts_v1(self, body: GeneratePerformanceForecastsV1RequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /mediaPlan/v1/performanceForecasts

        Generates forecast curve for the provided performance metric and targets.  **Authorized resource type**: DSP Rodeo Entit
        """
        endpoint = "/mediaPlan/v1/performanceForecasts"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-AccountId"] = amazon_ads_manager_account_id
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

    async def create_reach_forecasts_v1(self, body: CreateReachForecastsV1RequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /mediaPlan/v1/reachForecasts

        Creates a list of new Reach Forecasts in bulk action.  **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser
        """
        endpoint = "/mediaPlan/v1/reachForecasts"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-AccountId"] = amazon_ads_manager_account_id
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

    async def list_reach_forecasts_v1(self, body: ListReachForecastsV1RequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /mediaPlan/v1/reachForecasts/list

        Gets a list of Reach Forecasts by IDs  **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser Account ID  **P
        """
        endpoint = "/mediaPlan/v1/reachForecasts/list"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-AccountId"] = amazon_ads_manager_account_id
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

    async def list_reach_forecast_targets_v1(self, body: ListReachForecastTargetsV1RequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /mediaPlan/v1/reachForecasts/targets/list

        Gets a list of targets of a Reach Forecast  **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser Account ID
        """
        endpoint = "/mediaPlan/v1/reachForecasts/targets/list"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-AccountId"] = amazon_ads_manager_account_id
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

