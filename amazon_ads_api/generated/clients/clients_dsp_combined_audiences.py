"""Auto-generated async API client. Do not edit manually.

Source: CombinedAudienceAPI_prod_3p.json
Title:  Combined Audience API
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_dsp_combined_audiences import *  # noqa: F403
except ImportError:
    pass


class DspCombinedAudiencesClient(BaseAdsClient):
    """Auto-generated from CombinedAudienceAPI_prod_3p.json (2 operations)"""

    async def create_combined_audience(self, body: CreateCombinedAudienceRequestBody | dict[str, Any] | None = None, advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/audiences/combinedAudiences

        Creates a new combined audience based on the input audience expression.  **Authorized resource type**: DSP Rodeo Entity
        """
        endpoint = "/dsp/audiences/combinedAudiences"
        params: dict[str, Any] = {}
        if advertiser_id is not None:
            params["advertiserId"] = advertiser_id
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.createcombinedaudiencerequestbody.v1+json")

    async def get_combined_audience_details(self, audience_id: str, advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /dsp/audiences/combinedAudiences/{audienceId}

        Gets details of an existing combined audience.  **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser Accoun
        """
        endpoint = f"/dsp/audiences/combinedAudiences/{audience_id}"
        params: dict[str, Any] = {}
        if advertiser_id is not None:
            params["advertiserId"] = advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

