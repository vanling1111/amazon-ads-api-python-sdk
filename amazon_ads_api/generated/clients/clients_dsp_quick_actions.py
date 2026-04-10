"""Auto-generated async API client. Do not edit manually.

Source: DSPQuickActions_prod_3p.json
Title:  DSP Quick Actions
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_dsp_quick_actions import *  # noqa: F403
except ImportError:
    pass


class DspQuickActionsClient(BaseAdsClient):
    """Auto-generated from DSPQuickActions_prod_3p.json (5 operations)"""

    async def batch_create_executions_v1(self, body: batchCreateExecutionsRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /dsp/v1/quickactions/batchCreateExecutions

        Creates multiple executions based on batchCreateExecutionsRequest body.
        """
        endpoint = "/dsp/v1/quickactions/batchCreateExecutions"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspbatchcreateexecutionsrequest.v1.0+json")

    async def batch_get_executions_v1(self, body: batchGetExecutionsRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /dsp/v1/quickactions/batchGetExecutions

        Gets multiple executions based on batchGetExecutionsRequest body.
        """
        endpoint = "/dsp/v1/quickactions/batchGetExecutions"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspbatchgetexecutionsrequest.v1.0+json")

    async def create_execution_v1(self, action_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_ads_account_id: str | None = None, preview: str | None = None) -> JSONData | JSONList:
        """POST /dsp/v1/quickactions/{actionId}/executions

        Creates an execution for an action.
        """
        endpoint = f"/dsp/v1/quickactions/{action_id}/executions"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if preview is not None:
            params["preview"] = preview
        return await self.post(endpoint, params=params)

    async def get_execution_v1(self, action_id: str, execution_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """GET /dsp/v1/quickactions/{actionId}/executions/{executionId}

        Gets an execution.
        """
        endpoint = f"/dsp/v1/quickactions/{action_id}/executions/{execution_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        return await self.get(endpoint, params=params)

    async def start_execution_v1(self, action_id: str, execution_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_ads_account_id: str | None = None, omit_step_ids: str | None = None) -> JSONData | JSONList:
        """PUT /dsp/v1/quickactions/{actionId}/executions/{executionId}/start

        Starts an execution.
        """
        endpoint = f"/dsp/v1/quickactions/{action_id}/executions/{execution_id}/start"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if omit_step_ids is not None:
            params["omitStepIds"] = omit_step_ids
        return await self.put(endpoint, params=params)

