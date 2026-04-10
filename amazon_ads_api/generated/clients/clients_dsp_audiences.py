"""Auto-generated async API client. Do not edit manually.

Source: ADSPAudiences_prod_3p.json
Title:  ADSP Audiences
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_dsp_audiences import *  # noqa: F403
except ImportError:
    pass


class DspAudiencesClient(BaseAdsClient):
    """Auto-generated from ADSPAudiences_prod_3p.json (1 operations)"""

    async def dsp_create_audiences_post(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, advertiser_id: str | None = None) -> JSONData | JSONList:
        """POST /dsp/audiences

        Creates an audience.
        """
        endpoint = "/dsp/audiences"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if advertiser_id is not None:
            params["advertiserId"] = advertiser_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspaudiences.v1+json")

