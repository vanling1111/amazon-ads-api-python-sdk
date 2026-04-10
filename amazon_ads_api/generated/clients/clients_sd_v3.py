"""Auto-generated async API client. Do not edit manually.

Source: SponsoredDisplay_v3_openapi.yaml
Title:  Amazon Ads API for Sponsored Display
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_sd_v3 import *  # noqa: F403
except ImportError:
    pass


class SdV3Client(BaseAdsClient):
    """Auto-generated from SponsoredDisplay_v3_openapi.yaml (54 operations)"""

    async def list_campaigns(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None, state_filter: str | None = None, name: str | None = None, campaign_id_filter: str | None = None, portfolio_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /sd/campaigns

        Gets a list of campaigns.
        """
        endpoint = "/sd/campaigns"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if state_filter is not None:
            params["stateFilter"] = state_filter
        if name is not None:
            params["name"] = name
        if campaign_id_filter is not None:
            params["campaignIdFilter"] = campaign_id_filter
        if portfolio_id_filter is not None:
            params["portfolioIdFilter"] = portfolio_id_filter
        return await self.get(endpoint, params=params)

    async def update_campaigns(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /sd/campaigns

        Updates one or more campaigns.
        """
        endpoint = "/sd/campaigns"
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
        return await self.put(endpoint, json_data=json_data, params=params)

    async def create_campaigns(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/campaigns

        Creates one or more campaigns.
        """
        endpoint = "/sd/campaigns"
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

    async def get_campaign(self, campaign_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/campaigns/{campaignId}

        Gets a requested campaign.
        """
        endpoint = f"/sd/campaigns/{campaign_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def archive_campaign(self, campaign_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """DELETE /sd/campaigns/{campaignId}

        Sets the campaign status to archived.
        """
        endpoint = f"/sd/campaigns/{campaign_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.delete(endpoint, params=params)

    async def list_campaigns_ex(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None, state_filter: str | None = None, name: str | None = None, campaign_id_filter: str | None = None, portfolio_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /sd/campaigns/extended

        Gets a list of campaigns with extended fields.
        """
        endpoint = "/sd/campaigns/extended"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if state_filter is not None:
            params["stateFilter"] = state_filter
        if name is not None:
            params["name"] = name
        if campaign_id_filter is not None:
            params["campaignIdFilter"] = campaign_id_filter
        if portfolio_id_filter is not None:
            params["portfolioIdFilter"] = portfolio_id_filter
        return await self.get(endpoint, params=params)

    async def get_campaign_response_ex(self, campaign_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/campaigns/extended/{campaignId}

        Gets extended information for a requested campaign.
        """
        endpoint = f"/sd/campaigns/extended/{campaign_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def list_ad_groups(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None, state_filter: str | None = None, campaign_id_filter: str | None = None, ad_group_id_filter: str | None = None, name: str | None = None) -> JSONData | JSONList:
        """GET /sd/adGroups

        Gets a list of ad groups.
        """
        endpoint = "/sd/adGroups"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if state_filter is not None:
            params["stateFilter"] = state_filter
        if campaign_id_filter is not None:
            params["campaignIdFilter"] = campaign_id_filter
        if ad_group_id_filter is not None:
            params["adGroupIdFilter"] = ad_group_id_filter
        if name is not None:
            params["name"] = name
        return await self.get(endpoint, params=params)

    async def update_ad_groups(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /sd/adGroups

        Updates on or more ad groups.
        """
        endpoint = "/sd/adGroups"
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
        return await self.put(endpoint, json_data=json_data, params=params)

    async def create_ad_groups(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/adGroups

        Creates one or more ad groups.
        """
        endpoint = "/sd/adGroups"
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

    async def get_ad_group(self, ad_group_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/adGroups/{adGroupId}

        Gets a requested ad group.
        """
        endpoint = f"/sd/adGroups/{ad_group_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def archive_ad_group(self, ad_group_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """DELETE /sd/adGroups/{adGroupId}

        Sets the ad group status to archived.
        """
        endpoint = f"/sd/adGroups/{ad_group_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.delete(endpoint, params=params)

    async def list_ad_groups_ex(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None, state_filter: str | None = None, campaign_id_filter: str | None = None, ad_group_id_filter: str | None = None, name: str | None = None) -> JSONData | JSONList:
        """GET /sd/adGroups/extended

        Gets a list of ad groups with extended fields.
        """
        endpoint = "/sd/adGroups/extended"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if state_filter is not None:
            params["stateFilter"] = state_filter
        if campaign_id_filter is not None:
            params["campaignIdFilter"] = campaign_id_filter
        if ad_group_id_filter is not None:
            params["adGroupIdFilter"] = ad_group_id_filter
        if name is not None:
            params["name"] = name
        return await self.get(endpoint, params=params)

    async def get_ad_group_response_ex(self, ad_group_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/adGroups/extended/{adGroupId}

        Gets extended information for a requested ad group.
        """
        endpoint = f"/sd/adGroups/extended/{ad_group_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def list_product_ads(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None, state_filter: str | None = None, ad_id_filter: str | None = None, ad_group_id_filter: str | None = None, campaign_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /sd/productAds

        Gets a list of product ads.
        """
        endpoint = "/sd/productAds"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if state_filter is not None:
            params["stateFilter"] = state_filter
        if ad_id_filter is not None:
            params["adIdFilter"] = ad_id_filter
        if ad_group_id_filter is not None:
            params["adGroupIdFilter"] = ad_group_id_filter
        if campaign_id_filter is not None:
            params["campaignIdFilter"] = campaign_id_filter
        return await self.get(endpoint, params=params)

    async def update_product_ads(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /sd/productAds

        Updates one or more product ads.
        """
        endpoint = "/sd/productAds"
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
        return await self.put(endpoint, json_data=json_data, params=params)

    async def create_product_ads(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/productAds

        Creates one or more product ads.
        """
        endpoint = "/sd/productAds"
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

    async def get_product_ad(self, ad_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/productAds/{adId}

        Gets a requested product ad.
        """
        endpoint = f"/sd/productAds/{ad_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def archive_product_ad(self, ad_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """DELETE /sd/productAds/{adId}

        Sets the status of a sproduct ad to archived.
        """
        endpoint = f"/sd/productAds/{ad_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.delete(endpoint, params=params)

    async def list_product_ads_ex(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None, state_filter: str | None = None, ad_id_filter: str | None = None, ad_group_id_filter: str | None = None, campaign_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /sd/productAds/extended

        Gets a list of product ads with extended fields.
        """
        endpoint = "/sd/productAds/extended"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if state_filter is not None:
            params["stateFilter"] = state_filter
        if ad_id_filter is not None:
            params["adIdFilter"] = ad_id_filter
        if ad_group_id_filter is not None:
            params["adGroupIdFilter"] = ad_group_id_filter
        if campaign_id_filter is not None:
            params["campaignIdFilter"] = campaign_id_filter
        return await self.get(endpoint, params=params)

    async def get_product_ad_response_ex(self, ad_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/productAds/extended/{adId}

        Gets extended information for a product ad.
        """
        endpoint = f"/sd/productAds/extended/{ad_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def get_report_status(self, report_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /v2/reports/{reportId}

        Gets the status of a report previously requested.
        """
        endpoint = f"/v2/reports/{report_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def download_report(self, report_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /v2/reports/{reportId}/download

        Downloads a previously requested report identified by reportId.
        """
        endpoint = f"/v2/reports/{report_id}/download"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def request_report(self, record_type: str, body: ReportRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/{recordType}/report

        Creates a report request.
        """
        endpoint = f"/sd/{record_type}/report"
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

    async def list_targeting_clauses(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None, state_filter: str | None = None, target_id_filter: str | None = None, ad_group_id_filter: str | None = None, campaign_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /sd/targets

        Gets a list of targeting clauses.
        """
        endpoint = "/sd/targets"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if state_filter is not None:
            params["stateFilter"] = state_filter
        if target_id_filter is not None:
            params["targetIdFilter"] = target_id_filter
        if ad_group_id_filter is not None:
            params["adGroupIdFilter"] = ad_group_id_filter
        if campaign_id_filter is not None:
            params["campaignIdFilter"] = campaign_id_filter
        return await self.get(endpoint, params=params)

    async def update_targeting_clauses(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /sd/targets

        Updates one or more targeting clauses.
        """
        endpoint = "/sd/targets"
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
        return await self.put(endpoint, json_data=json_data, params=params)

    async def create_targeting_clauses(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/targets

        Creates one or more targeting clauses.
        """
        endpoint = "/sd/targets"
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

    async def get_targets(self, target_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/targets/{targetId}

        Gets a targeting clause specified by identifier.
        """
        endpoint = f"/sd/targets/{target_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def archive_targeting_clause(self, target_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """DELETE /sd/targets/{targetId}

        Sets the `state` of a targeting clause to `archived`.
        """
        endpoint = f"/sd/targets/{target_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.delete(endpoint, params=params)

    async def list_targeting_clauses_ex(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None, state_filter: str | None = None, target_id_filter: str | None = None, ad_group_id_filter: str | None = None, campaign_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /sd/targets/extended

        Gets a list of targeting clause objects with extended fields.
        """
        endpoint = "/sd/targets/extended"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if state_filter is not None:
            params["stateFilter"] = state_filter
        if target_id_filter is not None:
            params["targetIdFilter"] = target_id_filter
        if ad_group_id_filter is not None:
            params["adGroupIdFilter"] = ad_group_id_filter
        if campaign_id_filter is not None:
            params["campaignIdFilter"] = campaign_id_filter
        return await self.get(endpoint, params=params)

    async def get_targets_ex(self, target_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/targets/extended/{targetId}

        Gets extended information for a targeting clause.
        """
        endpoint = f"/sd/targets/extended/{target_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def list_negative_targeting_clauses(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None, state_filter: str | None = None, ad_group_id_filter: str | None = None, campaign_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /sd/negativeTargets

        Gets a list of negative targeting clauses.
        """
        endpoint = "/sd/negativeTargets"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if state_filter is not None:
            params["stateFilter"] = state_filter
        if ad_group_id_filter is not None:
            params["adGroupIdFilter"] = ad_group_id_filter
        if campaign_id_filter is not None:
            params["campaignIdFilter"] = campaign_id_filter
        return await self.get(endpoint, params=params)

    async def update_negative_targeting_clauses(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /sd/negativeTargets

        Updates one or more negative targeting clauses.
        """
        endpoint = "/sd/negativeTargets"
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
        return await self.put(endpoint, json_data=json_data, params=params)

    async def create_negative_targeting_clauses(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/negativeTargets

        Creates one or more negative targeting clauses.
        """
        endpoint = "/sd/negativeTargets"
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

    async def get_negative_targets(self, negative_target_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/negativeTargets/{negativeTargetId}

        Gets a negative targeting clause specified by identifier.
        """
        endpoint = f"/sd/negativeTargets/{negative_target_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def archive_negative_targeting_clause(self, negative_target_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """DELETE /sd/negativeTargets/{negativeTargetId}

        Sets the `state` of a negative targeting clause to `archived`.
        """
        endpoint = f"/sd/negativeTargets/{negative_target_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.delete(endpoint, params=params)

    async def list_negative_targeting_clauses_ex(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None, state_filter: str | None = None, target_id_filter: str | None = None, ad_group_id_filter: str | None = None, campaign_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /sd/negativeTargets/extended

        Gets a list of negative targeting clause objects with extended fields.
        """
        endpoint = "/sd/negativeTargets/extended"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if state_filter is not None:
            params["stateFilter"] = state_filter
        if target_id_filter is not None:
            params["targetIdFilter"] = target_id_filter
        if ad_group_id_filter is not None:
            params["adGroupIdFilter"] = ad_group_id_filter
        if campaign_id_filter is not None:
            params["campaignIdFilter"] = campaign_id_filter
        return await self.get(endpoint, params=params)

    async def get_negative_targets_ex(self, negative_target_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/negativeTargets/extended/{negativeTargetId}

        Gets extended information for a negative targeting clause.
        """
        endpoint = f"/sd/negativeTargets/extended/{negative_target_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def list_creatives(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None, ad_group_id_filter: str | None = None, creative_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /sd/creatives

        Gets a list of creatives
        """
        endpoint = "/sd/creatives"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if ad_group_id_filter is not None:
            params["adGroupIdFilter"] = ad_group_id_filter
        if creative_id_filter is not None:
            params["creativeIdFilter"] = creative_id_filter
        return await self.get(endpoint, params=params)

    async def update_creatives(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /sd/creatives

        Updates one or more creatives.
        """
        endpoint = "/sd/creatives"
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
        return await self.put(endpoint, json_data=json_data, params=params)

    async def create_creatives(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/creatives

        A POST request of one or more creatives.
        """
        endpoint = "/sd/creatives"
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

    async def post_creative_preview(self, body: CreativePreviewRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/creatives/preview

        Gets creative preview HTML.
        """
        endpoint = "/sd/creatives/preview"
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

    async def list_creative_moderations(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, language: str | None = None, start_index: str | None = None, count: str | None = None, ad_group_id_filter: str | None = None, creative_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /sd/moderation/creatives

        Gets a list of creative moderations
        """
        endpoint = "/sd/moderation/creatives"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if language is not None:
            params["language"] = language
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if ad_group_id_filter is not None:
            params["adGroupIdFilter"] = ad_group_id_filter
        if creative_id_filter is not None:
            params["creativeIdFilter"] = creative_id_filter
        return await self.get(endpoint, params=params)

    async def list_optimization_rules(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None, state_filter: str | None = None, name: str | None = None, optimization_rule_id_filter: str | None = None, ad_group_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /sd/optimizationRules

        Gets a list of optimization rules.
        """
        endpoint = "/sd/optimizationRules"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if state_filter is not None:
            params["stateFilter"] = state_filter
        if name is not None:
            params["name"] = name
        if optimization_rule_id_filter is not None:
            params["optimizationRuleIdFilter"] = optimization_rule_id_filter
        if ad_group_id_filter is not None:
            params["adGroupIdFilter"] = ad_group_id_filter
        return await self.get(endpoint, params=params)

    async def update_optimization_rules(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /sd/optimizationRules

        Updates one or more optimization rules.
        """
        endpoint = "/sd/optimizationRules"
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
        return await self.put(endpoint, json_data=json_data, params=params)

    async def create_optimization_rules(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/optimizationRules

        Creates one or more optimization rules, also known as outcome optimizations.
        """
        endpoint = "/sd/optimizationRules"
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

    async def get_sd_optimizationRules_by_id(self, optimization_rule_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/optimizationRules/{optimizationRuleId}

        Gets a requested optimization rule.
        """
        endpoint = f"/sd/optimizationRules/{optimization_rule_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def associate_optimization_rules_with_ad_group(self, ad_group_id: str, body: CreateAssociatedOptimizationRulesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/adGroups/{adGroupId}/optimizationRules

        Associate one or more optimization rules to an ad group specified by identifier.
        """
        endpoint = f"/sd/adGroups/{ad_group_id}/optimizationRules"
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

    async def get_sd_adGroups_by_id_optimizationRules(self, ad_group_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/adGroups/{adGroupId}/optimizationRules

        Gets a list of optimization rules associated to an adgroup specified by identifier.
        """
        endpoint = f"/sd/adGroups/{ad_group_id}/optimizationRules"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def disassociate_optimization_rules_from_ad_group(self, ad_group_id: str, body: CreateAssociatedOptimizationRulesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/adGroups/{adGroupId}/optimizationRules/disassociate

        Disassociate one or more optimization rules from an ad group specified by identifier.
        """
        endpoint = f"/sd/adGroups/{ad_group_id}/optimizationRules/disassociate"
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

    async def create_sd_forecast(self, body: SDForecastRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/forecasts

        Return forecasts for an ad group that may or may not exist.
        """
        endpoint = "/sd/forecasts"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sdforecasts.v3.1+json")

    async def list_locations(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None, state_filter: str | None = None, ad_group_id_filter: str | None = None, campaign_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /sd/locations

        Gets a list of locations associated with ad groups.
        """
        endpoint = "/sd/locations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if state_filter is not None:
            params["stateFilter"] = state_filter
        if ad_group_id_filter is not None:
            params["adGroupIdFilter"] = ad_group_id_filter
        if campaign_id_filter is not None:
            params["campaignIdFilter"] = campaign_id_filter
        return await self.get(endpoint, params=params)

    async def create_locations(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/locations

        Creates one or more locations associated with an ad group.
        """
        endpoint = "/sd/locations"
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

    async def archive_locations(self, body: ArchiveLocationRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/locations/delete

        Sets the `state` of each Location clause given to `archived`.
        """
        endpoint = "/sd/locations/delete"
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

