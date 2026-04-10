"""Auto-generated async API client. Do not edit manually.

Source: AmazonAttribution_prod_3p.json
Title:  Amazon Attribution
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_attribution import *  # noqa: F403
except ImportError:
    pass


class AttributionClient(BaseAdsClient):
    """Auto-generated from AmazonAttribution_prod_3p.json (5 operations)"""

    async def get_advertisers_by_profile(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /attribution/advertisers

        Gets a list of advertisers associated with an Amazon Attribution account.
        """
        endpoint = "/attribution/advertisers"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def get_publishers(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /attribution/publishers

        Gets a list of all available publishers.
        """
        endpoint = "/attribution/publishers"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def get_attribution_tags_by_campaign(self, body: ReportRequestBody | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /attribution/report

        Gets an attribution report for a specified list of advertisers.
        """
        endpoint = "/attribution/report"
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
        return await self.post(endpoint, json_data=json_data, params=params)

    async def get_publisher_attribution_tag_template(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, publisher_ids: str | None = None, advertiser_ids: str | None = None) -> JSONData | JSONList:
        """GET /attribution/tags/macroTag

        Gets a list of attribution tags for third-party publisher campaigns that support macros.
        """
        endpoint = "/attribution/tags/macroTag"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if publisher_ids is not None:
            params["publisherIds"] = publisher_ids
        if advertiser_ids is not None:
            params["advertiserIds"] = advertiser_ids
        return await self.get(endpoint, params=params)

    async def get_publisher_macro_attribution_tag(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, publisher_ids: str | None = None, advertiser_ids: str | None = None) -> JSONData | JSONList:
        """GET /attribution/tags/nonMacroTemplateTag

        Gets a list of attribution tags for third-party publisher campaigns that do not support macros.
        """
        endpoint = "/attribution/tags/nonMacroTemplateTag"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if publisher_ids is not None:
            params["publisherIds"] = publisher_ids
        if advertiser_ids is not None:
            params["advertiserIds"] = advertiser_ids
        return await self.get(endpoint, params=params)

