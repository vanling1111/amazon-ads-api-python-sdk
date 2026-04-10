"""Auto-generated async API client. Do not edit manually.

Source: Diagnostics_prod_3p.json
Title:  Diagnostics
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_diagnostics import *  # noqa: F403
except ImportError:
    pass


class DiagnosticsClient(BaseAdsClient):
    """Auto-generated from Diagnostics_prod_3p.json (1 operations)"""

    async def campaign_diagnostics(self, body: CampaignDiagnosticsRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /diagnostics/campaigns/issues

        Returns campaign issues
        """
        endpoint = "/diagnostics/campaigns/issues"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.campaigndiagnosticsissues.v1+json")

