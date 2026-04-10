"""Auto-generated async API client. Do not edit manually.

Source: SponsoredTV_prod_3p.json
Title:  Sponsored TV
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_stv import *  # noqa: F403
except ImportError:
    pass


class StvClient(BaseAdsClient):
    """Auto-generated from SponsoredTV_prod_3p.json (26 operations)"""

    async def create_sponsored_tv_ad_groups(self, body: CreateSponsoredTvAdGroupsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /st/adGroups

        Creates Sponsored Tv Ad Groups.  **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/st/adGroups"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stAdGroup.v1+json")

    async def update_sponsored_tv_ad_groups(self, body: UpdateSponsoredTvAdGroupsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """PUT /st/adGroups

        Updates Sponsored Tv Ad Groups.  **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/st/adGroups"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.stAdGroup.v1+json")

    async def delete_sponsored_tv_ad_groups(self, body: DeleteSponsoredTvAdGroupsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /st/adGroups/delete

        Deletes Sponsored Tv Ad Groups.  **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/st/adGroups/delete"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stAdGroup.v1+json")

    async def list_sponsored_tv_ad_groups(self, body: ListSponsoredTvAdGroupsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /st/adGroups/list

        Lists Sponsored Tv Ad Groups.  **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign_v
        """
        endpoint = "/st/adGroups/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stAdGroup.v1+json")

    async def create_sponsored_tv_ads(self, body: CreateSponsoredTvAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /st/ads

        Creates Sponsored Tv Ads.  **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/st/ads"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stAd.v1+json")

    async def update_sponsored_tv_ads(self, body: UpdateSponsoredTvAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """PUT /st/ads

        Updates Sponsored Tv Ads.  **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/st/ads"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.stAd.v1+json")

    async def delete_sponsored_tv_ads(self, body: DeleteSponsoredTvAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /st/ads/delete

        Deletes Sponsored Tv Ads.  **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/st/ads/delete"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stAd.v1+json")

    async def list_sponsored_tv_ads(self, body: ListSponsoredTvAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /st/ads/list

        Lists Sponsored Tv Ads.  **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign_view']
        """
        endpoint = "/st/ads/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stAd.v1+json")

    async def create_sponsored_tv_campaigns(self, body: CreateSponsoredTvCampaignsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /st/campaigns

        Creates Sponsored Tv campaigns.  **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/st/campaigns"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stCampaign.v1+json")

    async def update_sponsored_tv_campaigns(self, body: UpdateSponsoredTvCampaignsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """PUT /st/campaigns

        Updates Sponsored Tv campaigns.  **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/st/campaigns"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.stCampaign.v1+json")

    async def delete_sponsored_tv_campaigns(self, body: DeleteSponsoredTvCampaignsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /st/campaigns/delete

        Deletes Sponsored Tv campaigns.  **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/st/campaigns/delete"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stCampaign.v1+json")

    async def list_sponsored_tv_campaigns(self, body: ListSponsoredTvCampaignsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /st/campaigns/list

        Lists Sponsored Tv Campaigns  **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign_vi
        """
        endpoint = "/st/campaigns/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stCampaign.v1+json")

    async def create_sponsored_tv_creatives(self, body: CreateSponsoredTvCreativesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /st/creatives

        **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/st/creatives"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stCreative.v1+json")

    async def update_sponsored_tv_creatives(self, body: UpdateSponsoredTvCreativesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /st/creatives

        **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/st/creatives"
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.stCreative.v1+json")

    async def list_sponsored_tv_creatives(self, body: ListSponsoredTvCreativesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /st/creatives/list

        **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign_view']
        """
        endpoint = "/st/creatives/list"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stCreative.v1+json")

    async def list_sponsored_tv_creatives_moderations(self, body: ListSponsoredTvCreativesModerationsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /st/creatives/moderations/list

        **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign_view']
        """
        endpoint = "/st/creatives/moderations/list"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stCreativesModerations.v1+json")

    async def list_sponsored_tv_creatives_moderations_policy_violations(self, body: ListSponsoredTvCreativesModerationsPolicyViolationsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /st/creatives/moderations/policyViolations/list

        **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign_view']
        """
        endpoint = "/st/creatives/moderations/policyViolations/list"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stCreativesModerations.v1+json")

    async def preview_sponsored_tv_creative(self, body: PreviewSponsoredTvCreativeRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /st/creatives/preview

        **Requires one of these permissions**: ['advertiser_campaign_view']
        """
        endpoint = "/st/creatives/preview"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stCreativesPreview.v1+json")

    async def sponsored_tv_forecasts(self, body: SponsoredTvForecastsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /st/forecasts

        Returns forecasts for a given ad group specified in Sponsored TV forecast request.  **Requires one of these permissions*
        """
        endpoint = "/st/forecasts"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stForecast.v1+json")

    async def create_sponsored_tv_locations(self, body: CreateSponsoredTvLocationsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /st/locations

        **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/st/locations"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stLocation.v1+json")

    async def delete_sponsored_tv_locations(self, body: DeleteSponsoredTvLocationsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /st/locations/delete

        **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/st/locations/delete"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stLocation.v1+json")

    async def list_sponsored_tv_locations(self, body: ListSponsoredTvLocationsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /st/locations/list

        **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign_view']
        """
        endpoint = "/st/locations/list"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stLocation.v1+json")

    async def create_sponsored_tv_targeting_clauses(self, body: CreateSponsoredTvTargetingClausesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /st/targets

        **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/st/targets"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stTargetingClause.v1+json")

    async def update_sponsored_tv_targeting_clauses(self, body: UpdateSponsoredTvTargetingClausesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """PUT /st/targets

        **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/st/targets"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.stTargetingClause.v1+json")

    async def delete_sponsored_tv_targeting_clauses(self, body: DeleteSponsoredTvTargetingClausesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /st/targets/delete

        **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/st/targets/delete"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stTargetingClause.v1+json")

    async def list_sponsored_tv_targeting_clauses(self, body: ListSponsoredTvTargetingClausesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /st/targets/list

        **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign_view']
        """
        endpoint = "/st/targets/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.stTargetingClause.v1+json")

