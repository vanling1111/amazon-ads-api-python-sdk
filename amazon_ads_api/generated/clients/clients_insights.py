"""Auto-generated async API client. Do not edit manually.

Source: Insights_prod_3p.json
Title:  Insights
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_insights import *  # noqa: F403
except ImportError:
    pass


class InsightsClient(BaseAdsClient):
    """Auto-generated from Insights_prod_3p.json (1 operations)"""

    async def insights_get_audiences_overlapping_audiences(self, audience_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, ad_type: str | None = None, advertiser_id: str | None = None, minimum_overlap_affinity: str | None = None, maximum_overlap_affinity: str | None = None, audience_category: str | None = None, max_results: str | None = None, next_token: str | None = None) -> JSONData | JSONList:
        """GET /insights/audiences/{audienceId}/overlappingAudiences

        Retrieves the top audiences that overlap with the provided audience.
        """
        endpoint = f"/insights/audiences/{audience_id}/overlappingAudiences"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if ad_type is not None:
            params["adType"] = ad_type
        if advertiser_id is not None:
            params["advertiserId"] = advertiser_id
        if minimum_overlap_affinity is not None:
            params["minimumOverlapAffinity"] = minimum_overlap_affinity
        if maximum_overlap_affinity is not None:
            params["maximumOverlapAffinity"] = maximum_overlap_affinity
        if audience_category is not None:
            params["audienceCategory"] = audience_category
        if max_results is not None:
            params["maxResults"] = max_results
        if next_token is not None:
            params["nextToken"] = next_token
        return await self.get(endpoint, params=params)

