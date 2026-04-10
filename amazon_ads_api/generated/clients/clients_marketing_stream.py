"""Auto-generated async API client. Do not edit manually.

Source: AmazonMarketingStream_prod_3p.json
Title:  Amazon Marketing Stream
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_marketing_stream import *  # noqa: F403
except ImportError:
    pass


class MarketingStreamClient(BaseAdsClient):
    """Auto-generated from AmazonMarketingStream_prod_3p.json (8 operations)"""

    async def list_dsp_stream_subscriptions(self, max_results: str | None = None, starting_token: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /dsp/streams/subscriptions

        List subscriptions Note: trailing slash in request uri is not allowed  **Authorized resource type**: DSP Rodeo Entity ID
        """
        endpoint = "/dsp/streams/subscriptions"
        params: dict[str, Any] = {}
        if max_results is not None:
            params["maxResults"] = max_results
        if starting_token is not None:
            params["startingToken"] = starting_token
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-Account-ID"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

    async def create_dsp_stream_subscription(self, body: CreateDspStreamSubscriptionRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /dsp/streams/subscriptions

        Create a new subscription Note: trailing slash in request uri is not allowed  **Authorized resource type**: DSP Rodeo En
        """
        endpoint = "/dsp/streams/subscriptions"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-Account-ID"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amazonmarketingstreamsubscriptions.v1+json")

    async def get_dsp_stream_subscription(self, subscription_id: str, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /dsp/streams/subscriptions/{subscriptionId}

        Fetch a specific subscription by Id Note: trailing slash in request uri is not allowed  **Authorized resource type**: DS
        """
        endpoint = f"/dsp/streams/subscriptions/{subscription_id}"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-Account-ID"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

    async def update_dsp_stream_subscription(self, subscription_id: str, body: UpdateDspStreamSubscriptionRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """PUT /dsp/streams/subscriptions/{subscriptionId}

        Update an existing subscription Note: trailing slash in request uri is not allowed  **Authorized resource type**: DSP Ro
        """
        endpoint = f"/dsp/streams/subscriptions/{subscription_id}"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-Account-ID"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.amazonmarketingstreamsubscriptions.v1+json")

    async def list_stream_subscriptions(self, max_results: str | None = None, starting_token: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /streams/subscriptions

        List subscriptions Note: trailing slash in request uri is not allowed  **Authorized resource type**: DSP Rodeo Entity ID
        """
        endpoint = "/streams/subscriptions"
        params: dict[str, Any] = {}
        if max_results is not None:
            params["maxResults"] = max_results
        if starting_token is not None:
            params["startingToken"] = starting_token
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def create_stream_subscription(self, body: CreateStreamSubscriptionRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /streams/subscriptions

        Create a new subscription Note: trailing slash in request uri is not allowed  **Authorized resource type**: DSP Rodeo En
        """
        endpoint = "/streams/subscriptions"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amazonmarketingstreamsubscriptions.v1+json")

    async def get_stream_subscription(self, subscription_id: str, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /streams/subscriptions/{subscriptionId}

        Fetch a specific subscription by Id Note: trailing slash in request uri is not allowed  **Authorized resource type**: DS
        """
        endpoint = f"/streams/subscriptions/{subscription_id}"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def update_stream_subscription(self, subscription_id: str, body: UpdateStreamSubscriptionRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /streams/subscriptions/{subscriptionId}

        Update an existing subscription Note: trailing slash in request uri is not allowed  **Authorized resource type**: DSP Ro
        """
        endpoint = f"/streams/subscriptions/{subscription_id}"
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.amazonmarketingstreamsubscriptions.v1+json")

