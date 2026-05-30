"""Amazon Marketing Stream subscriptions (L2 reference, OpenAPI-generated).

Official spec: ``AmazonMarketingStream_prod_3p.json``
Docs: https://advertising.amazon.com/API/docs/en-us/amazon-marketing-stream/overview

Wire surface::
    client.reference.stream.subscriptions.create_subscription(body)
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import JSONData, JSONList

try:
    from amazon_ads_api.generated.clients.clients_marketing_stream import (
        MarketingStreamClient as _GenBase,
    )
except ImportError:
    from amazon_ads_api.base import BaseAdsClient as _GenBase  # type: ignore[assignment]


class MarketingStreamSubscriptionsAPI(_GenBase):
    """Thin alias layer over generated Marketing Stream operations."""

    async def list_subscriptions(
        self,
        *,
        max_results: str | None = None,
        starting_token: str | None = None,
        amazon_ads_account_id: str | None = None,
    ) -> JSONData | JSONList:
        return await self.list_stream_subscriptions(
            max_results=max_results,
            starting_token=starting_token,
            amazon_ads_account_id=amazon_ads_account_id,
            amazon_advertising_api_client_id=self.client_id,
            amazon_advertising_api_scope=self.profile_id,
        )

    async def create_subscription(
        self,
        body: dict[str, Any],
        *,
        amazon_ads_account_id: str | None = None,
    ) -> JSONData | JSONList:
        return await self.create_stream_subscription(
            body=body,
            amazon_ads_account_id=amazon_ads_account_id,
            amazon_advertising_api_client_id=self.client_id,
            amazon_advertising_api_scope=self.profile_id,
        )

    async def get_subscription(
        self,
        subscription_id: str,
        *,
        amazon_ads_account_id: str | None = None,
    ) -> JSONData | JSONList:
        return await self.get_stream_subscription(
            subscription_id,
            amazon_ads_account_id=amazon_ads_account_id,
            amazon_advertising_api_client_id=self.client_id,
            amazon_advertising_api_scope=self.profile_id,
        )

    async def update_subscription(
        self,
        subscription_id: str,
        body: dict[str, Any],
        *,
        amazon_ads_account_id: str | None = None,
    ) -> JSONData | JSONList:
        return await self.update_stream_subscription(
            subscription_id,
            body=body,
            amazon_ads_account_id=amazon_ads_account_id,
            amazon_advertising_api_client_id=self.client_id,
            amazon_advertising_api_scope=self.profile_id,
        )

    async def list_dsp_subscriptions(
        self,
        *,
        max_results: str | None = None,
        starting_token: str | None = None,
        amazon_ads_account_id: str | None = None,
    ) -> JSONData | JSONList:
        return await self.list_dsp_stream_subscriptions(
            max_results=max_results,
            starting_token=starting_token,
            amazon_ads_account_id=amazon_ads_account_id,
            amazon_advertising_api_client_id=self.client_id,
        )

    async def create_dsp_subscription(
        self,
        body: dict[str, Any],
        *,
        amazon_ads_account_id: str | None = None,
    ) -> JSONData | JSONList:
        return await self.create_dsp_stream_subscription(
            body=body,
            amazon_ads_account_id=amazon_ads_account_id,
            amazon_advertising_api_client_id=self.client_id,
        )


# Backward-compatible export name used by older imports.
MarketingStreamAPI = MarketingStreamSubscriptionsAPI

__all__ = ["MarketingStreamAPI", "MarketingStreamSubscriptionsAPI"]
