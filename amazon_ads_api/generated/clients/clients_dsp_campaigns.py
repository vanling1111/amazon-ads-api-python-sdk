"""Auto-generated async API client. Do not edit manually.

Source: DSPCampaignManagement_prod_3p.json
Title:  DSP Campaign Management
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_dsp_campaigns import *  # noqa: F403
except ImportError:
    pass


class DspCampaignsClient(BaseAdsClient):
    """Auto-generated from DSPCampaignManagement_prod_3p.json (2 operations)"""

    async def get_advertisers(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None, advertiser_id_filter: str | None = None, name_contains: str | None = None) -> JSONData | JSONList:
        """GET /dsp/advertisers

        Gets a list of advertisers.
        """
        endpoint = "/dsp/advertisers"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if advertiser_id_filter is not None:
            params["advertiserIdFilter"] = advertiser_id_filter
        if name_contains is not None:
            params["nameContains"] = name_contains
        return await self.get(endpoint, params=params)

    async def get_advertiser(self, advertiser_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /dsp/advertisers/{advertiserId}

        Gets an advertiser specified by identifier.
        """
        endpoint = f"/dsp/advertisers/{advertiser_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

