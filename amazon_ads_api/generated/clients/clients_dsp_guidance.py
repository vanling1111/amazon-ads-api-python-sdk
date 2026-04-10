"""Auto-generated async API client. Do not edit manually.

Source: DSPGuidance_prod_3p.json
Title:  DSP Guidance
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_dsp_guidance import *  # noqa: F403
except ImportError:
    pass


class DspGuidanceClient(BaseAdsClient):
    """Auto-generated from DSPGuidance_prod_3p.json (3 operations)"""

    async def list_ad_group_guidance_v1(self, body: listAdGroupGuidanceV1Request | dict[str, Any] | None = None, accept_language: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/v1/guidance/adGroups/list

        Retrieves a list of dynamically generated guidance based on recommendations present for a list of ad groups specified in
        """
        endpoint = "/dsp/v1/guidance/adGroups/list"
        params: dict[str, Any] = {}
        if accept_language is not None:
            params["Accept-Language"] = accept_language
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspRecommendationsListAdGroupGuidanceV1Request.v1.0+json")

    async def list_advertiser_guidance_v1(self, body: listAdvertiserGuidanceV1Request | dict[str, Any] | None = None, accept_language: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/v1/guidance/advertisers/list

        Retrieves a list of dynamically generated guidance based on recommendations present for a list of advertisers specified
        """
        endpoint = "/dsp/v1/guidance/advertisers/list"
        params: dict[str, Any] = {}
        if accept_language is not None:
            params["Accept-Language"] = accept_language
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspRecommendationsListAdvertiserGuidanceV1Request.v1.0+json")

    async def list_campaign_guidance_v1(self, body: listCampaignGuidanceV1Request | dict[str, Any] | None = None, accept_language: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/v1/guidance/campaigns/list

        Retrieves a list of dynamically generated guidance based on recommendations present for a list of campaigns specified in
        """
        endpoint = "/dsp/v1/guidance/campaigns/list"
        params: dict[str, Any] = {}
        if accept_language is not None:
            params["Accept-Language"] = accept_language
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspRecommendationsListCampaignGuidanceV1Request.v1.0+json")

