"""Auto-generated async API client. Do not edit manually.

Source: MediaInsightsHub_prod_3p.json
Title:  Media Insights Hub
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_media_insights import *  # noqa: F403
except ImportError:
    pass


class MediaInsightsClient(BaseAdsClient):
    """Auto-generated from MediaInsightsHub_prod_3p.json (5 operations)"""

    async def list_historical_reach_curves(self, body: ListHistoricalReachCurvesRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /mediaPlan/historicalReachCurves/list

        Lists Historical Reach Curves.  **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser Account ID  **Paramete
        """
        endpoint = "/mediaPlan/historicalReachCurves/list"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.mediaplanhistoricalreachcurves.v1+json")

    async def list_historical_reach_curves_metadata(self, body: ListHistoricalReachCurvesMetadataRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /mediaPlan/historicalReachCurvesMetadata/list

        **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser Account ID  **Parameter name**: Amazon-Ads-AccountId
        """
        endpoint = "/mediaPlan/historicalReachCurvesMetadata/list"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.mediaplanhistoricalreachcurves.v1+json")

    async def create_historical_reach_curve(self, body: CreateHistoricalReachCurveRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /mediaPlan/v2/historicalReachCurves

        Submit a request to generate a Historical Reach Curve.  **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertise
        """
        endpoint = "/mediaPlan/v2/historicalReachCurves"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
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

    async def get_historical_reach_curve(self, report_id: str, max_results: str | None = None, next_token: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /mediaPlan/v2/historicalReachCurves/{reportId}

        Download the Historical Reach Curve.  **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser Account ID  **Pa
        """
        endpoint = f"/mediaPlan/v2/historicalReachCurves/{report_id}"
        params: dict[str, Any] = {}
        if max_results is not None:
            params["maxResults"] = max_results
        if next_token is not None:
            params["nextToken"] = next_token
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def get_historical_reach_curve_status(self, report_id: str, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /mediaPlan/v2/historicalReachCurves/{reportId}/status

        Get the status of the Historical Reach Curve.  **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser Account
        """
        endpoint = f"/mediaPlan/v2/historicalReachCurves/{report_id}/status"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

