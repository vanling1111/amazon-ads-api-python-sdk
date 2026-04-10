"""Auto-generated async API client. Do not edit manually.

Source: CampaignManagement_prod_3p.json
Title:  Campaign Management
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_campaign_management import *  # noqa: F403
except ImportError:
    pass


class CampaignManagementClient(BaseAdsClient):
    """Auto-generated from CampaignManagement_prod_3p.json (2 operations)"""

    async def copy_campaigns(self, body: copyCampaignsRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /campaigns/copy

        This API copies a campaign within a country or from one country to other country(s) within a region. When campaigns are
        """
        endpoint = "/campaigns/copy"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.copycampaignsrequest.v1+json")

    async def get_copy_status(self, request_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """GET /sp/campaigns/copy/requests/{requestId}

        This API gets the status of a campaign being copied.
        """
        endpoint = f"/sp/campaigns/copy/requests/{request_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        return await self.get(endpoint, params=params)

