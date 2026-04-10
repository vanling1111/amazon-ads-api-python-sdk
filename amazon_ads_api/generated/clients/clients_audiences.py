"""Auto-generated async API client. Do not edit manually.

Source: Audiences_prod_3p.json
Title:  Audiences
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_audiences import *  # noqa: F403
except ImportError:
    pass


class AudiencesClient(BaseAdsClient):
    """Auto-generated from Audiences_prod_3p.json (4 operations)"""

    async def list_audiences(self, body: ListAudiencesRequestBodyV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, advertiser_id: str | None = None, can_target: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """POST /audiences/list

        Gets audience segments based on filters
        """
        endpoint = "/audiences/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if advertiser_id is not None:
            params["advertiserId"] = advertiser_id
        if can_target is not None:
            params["canTarget"] = can_target
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def fetch_taxonomy(self, body: FetchTaxonomyRequestBodyV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, advertiser_id: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """POST /audiences/taxonomy/list

        Browse the taxonomy of audience categories
        """
        endpoint = "/audiences/taxonomy/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if advertiser_id is not None:
            params["advertiserId"] = advertiser_id
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def dsp_audience_delete(self, body: DspAudienceDeleteRequestContent | dict[str, Any] | None = None, advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/audiences/delete

        Deletes an existing targeting audience based on audience ID. Only available for the audiences of the type: *PRODUCT_PURC
        """
        endpoint = "/dsp/audiences/delete"
        params: dict[str, Any] = {}
        if advertiser_id is not None:
            params["AdvertiserId"] = advertiser_id
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspaudiences.v1+json")

    async def dsp_audience_edit(self, body: DspAudienceEditRequestContent | dict[str, Any] | None = None, advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /dsp/audiences/edit

        Updates an existing targeting audience based on an audience definition and audience ID.  **Requires one of these permiss
        """
        endpoint = "/dsp/audiences/edit"
        params: dict[str, Any] = {}
        if advertiser_id is not None:
            params["AdvertiserId"] = advertiser_id
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspaudiences.v1+json")

