"""Auto-generated async API client. Do not edit manually.

Source: Moderation_prod_3p.json
Title:  Moderation
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_moderation import *  # noqa: F403
except ImportError:
    pass


class ModerationClient(BaseAdsClient):
    """Auto-generated from Moderation_prod_3p.json (1 operations)"""

    async def moderation_results(self, body: ModerationResultsRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /moderation/results

        API to get the moderation results for the ad. Currently this API supports only SponsoredBrands, SponsoredProducts and Sp
        """
        endpoint = "/moderation/results"
        params: dict[str, Any] = {}
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.moderationresultsrequest.v4.1+json")

