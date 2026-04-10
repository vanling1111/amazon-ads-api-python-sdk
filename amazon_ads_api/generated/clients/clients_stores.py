"""Auto-generated async API client. Do not edit manually.

Source: Stores_prod_3p.json
Title:  Stores
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_stores import *  # noqa: F403
except ImportError:
    pass


class StoresClient(BaseAdsClient):
    """Auto-generated from Stores_prod_3p.json (2 operations)"""

    async def get_asin_engagement_for_store(self, brand_entity_id: str, body: GetAsinEngagementForStoreRequest | dict[str, Any] | None = None) -> JSONData | JSONList:
        """POST /stores/{brandEntityId}/asinMetrics

        Store asin metrics provides information about your store asin performance, including rendered impressions, viewed impres
        """
        endpoint = f"/stores/{brand_entity_id}/asinMetrics"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, content_type="application/vnd.GetAsinEngagementForStoreRequest.v1+json")

    async def get_insights_for_store_api(self, brand_entity_id: str, body: GetInsightsForStoreRequest | dict[str, Any] | None = None) -> JSONData | JSONList:
        """POST /stores/{brandEntityId}/insights

        Stores insights provides information about your store's performance, including traffic and sales. You can access Stores
        """
        endpoint = f"/stores/{brand_entity_id}/insights"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, content_type="application/vnd.GetInsightsForStoreRequest.v1+json")

