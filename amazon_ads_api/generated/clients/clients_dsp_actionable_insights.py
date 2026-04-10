"""Auto-generated async API client. Do not edit manually.

Source: D16GDspApiActionableInsights_prod_3p.json
Title:  D16GDspApiActionableInsights
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_dsp_actionable_insights import *  # noqa: F403
except ImportError:
    pass


class DspActionableInsightsClient(BaseAdsClient):
    """Auto-generated from D16GDspApiActionableInsights_prod_3p.json (2 operations)"""

    async def list_frequency_distribution_insights_v1(self, body: FrequencyDistributionRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_account_id: str | None = None) -> JSONData | JSONList:
        """POST /dsp/v1/frequencyDistributionInsights/list

        Gets frequency distribution insights for Amazon DSP, showing the number of unique users exposed to ads at different freq
        """
        endpoint = "/dsp/v1/frequencyDistributionInsights/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_account_id is not None:
            params["Amazon-Advertising-AccountId"] = amazon_advertising_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspFrequencyDistributionInsight.v1+json")

    async def list_frequency_savings_insights_v1(self, body: ListFrequencySavingsInsightsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_account_id: str | None = None) -> JSONData | JSONList:
        """POST /dsp/v1/frequencySavingsInsights/list

        Gets frequency savings insights for Amazon DSP.  **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser Accou
        """
        endpoint = "/dsp/v1/frequencySavingsInsights/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_account_id is not None:
            params["Amazon-Advertising-AccountId"] = amazon_advertising_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspFrequencySavingsInsight.v1+json")

