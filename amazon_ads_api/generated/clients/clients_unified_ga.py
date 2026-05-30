"""Auto-generated async API client. Do not edit manually.

Source: AmazonAdsAPIALLMerged_prod_3p.json
Title:  Amazon Ads API ALL Merged
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_unified_ga import *  # noqa: F403
except ImportError:
    pass


class UnifiedGaClient(BaseAdsClient):
    """Auto-generated from AmazonAdsAPIALLMerged_prod_3p.json (50 operations)"""

    async def list_brand_store_edition(self, brand_store_id: str | None = None, next_token: str | None = None, max_results: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /adsApi/v1/brandStoreEditions

        Retrieve brand store page content  **Requires one of these permissions**: ['amazon_stores_edit','amazon_stores_view']
        """
        endpoint = "/adsApi/v1/brandStoreEditions"
        params: dict[str, Any] = {}
        if brand_store_id is not None:
            params["brandStoreId"] = brand_store_id
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def dsp_list_commitment(self, next_token: str | None = None, max_results: str | None = None, amazon_ads_client_id: str | None = None) -> JSONData | JSONList:
        """GET /adsApi/v1/commitments/dsp

        List commitments  **Requires one of these permissions**: []
        """
        endpoint = "/adsApi/v1/commitments/dsp"
        params: dict[str, Any] = {}
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        return await self.get(endpoint, params=params)

    async def create_ad_association(self, body: CreateAdAssociationRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/create/adAssociations

        Create Ad Association  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific doc
        """
        endpoint = "/adsApi/v1/create/adAssociations"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def create_ad_extension(self, body: CreateAdExtensionRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/create/adExtensions

        Create ad extensions - API is in open beta  **Note:** Batch size limits are specific to each ad product. Refer to the ad
        """
        endpoint = "/adsApi/v1/create/adExtensions"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def create_ad_group(self, body: CreateAdGroupRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/create/adGroups

        Create ad groups  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific document
        """
        endpoint = "/adsApi/v1/create/adGroups"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def create_ad(self, body: CreateAdRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/create/ads

        Create ads  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific documentation
        """
        endpoint = "/adsApi/v1/create/ads"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def sb_create_advertising_deal_target(self, body: SBCreateAdvertisingDealTargetRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/create/advertisingDealTargets/sb

        Create advertisingDealTarget  **Requires one of these permissions**: ['advertiser_campaign_edit', 'advertiser_campaign_v
        """
        endpoint = "/adsApi/v1/create/advertisingDealTargets/sb"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def sb_create_advertising_deal(self, body: SBCreateAdvertisingDealRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/create/advertisingDeals/sb

        Create advertisingDeal  **Requires one of these permissions**: ['advertiser_campaign_edit', 'advertiser_campaign_view']
        """
        endpoint = "/adsApi/v1/create/advertisingDeals/sb"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def sb_create_branded_keywords_pricing(self, body: SBCreateBrandedKeywordsPricingRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/create/brandedKeywordsPricings/sb

        Create brandedKeywords pricing  **Requires one of these permissions**: ['advertiser_campaign_edit', 'advertiser_campaign
        """
        endpoint = "/adsApi/v1/create/brandedKeywordsPricings/sb"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def create_campaign(self, body: CreateCampaignRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/create/campaigns

        Create campaigns  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific document
        """
        endpoint = "/adsApi/v1/create/campaigns"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def dsp_create_commitment(self, body: DSPCreateCommitmentRequest | dict[str, Any] | None = None, amazon_ads_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/create/commitments/dsp

        Create commitments  **Requires one of these permissions**: []
        """
        endpoint = "/adsApi/v1/create/commitments/dsp"
        params: dict[str, Any] = {}
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def create_geo_location(self, body: CreateGeoLocationRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_ads_manager_account_id: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/create/geoLocations

        Create geo location targeting definitions. Supports smart locations, which target users based on their percentile rank w
        """
        endpoint = "/adsApi/v1/create/geoLocations"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-AccountId"] = amazon_ads_manager_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def sb_create_keyword_reservation_validation(self, body: SBCreateKeywordReservationValidationRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/create/keywordReservationValidations/sb

        Validate keyword reservation  **Requires one of these permissions**: ['advertiser_campaign_edit', 'advertiser_campaign_v
        """
        endpoint = "/adsApi/v1/create/keywordReservationValidations/sb"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def create_location_index(self, body: CreateLocationIndexRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_ads_manager_account_id: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/create/locationIndexes

        Create a Smart Location Index. A Smart Location Index is a named dataset that maps postal codes to index values represen
        """
        endpoint = "/adsApi/v1/create/locationIndexes"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-AccountId"] = amazon_ads_manager_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def sb_create_recommendation(self, body: SBCreateRecommendationRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/create/recommendations/sb

        Create recommendations  **Requires one of these permissions**: ['advertiser_campaign_view']
        """
        endpoint = "/adsApi/v1/create/recommendations/sb"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def create_target(self, body: CreateTargetRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/create/targets

        Create target  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific documentati
        """
        endpoint = "/adsApi/v1/create/targets"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def delete_ad_association(self, body: DeleteAdAssociationRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/delete/adAssociations

        Delete Ad Association  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific doc
        """
        endpoint = "/adsApi/v1/delete/adAssociations"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def delete_ad_group(self, body: DeleteAdGroupRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/delete/adGroups

        Delete ad groups  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific document
        """
        endpoint = "/adsApi/v1/delete/adGroups"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def delete_ad(self, body: DeleteAdRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/delete/ads

        Delete ads  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific documentation
        """
        endpoint = "/adsApi/v1/delete/ads"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def sb_delete_advertising_deal_target(self, body: SBDeleteAdvertisingDealTargetRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/delete/advertisingDealTargets/sb

        Delete advertisingDealTarget  **Requires one of these permissions**: ['advertiser_campaign_edit', 'advertiser_campaign_v
        """
        endpoint = "/adsApi/v1/delete/advertisingDealTargets/sb"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def sb_delete_advertising_deal(self, body: SBDeleteAdvertisingDealRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/delete/advertisingDeals/sb

        Delete advertisingDeal  **Requires one of these permissions**: ['advertiser_campaign_edit', 'advertiser_campaign_view']
        """
        endpoint = "/adsApi/v1/delete/advertisingDeals/sb"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def delete_campaign(self, body: DeleteCampaignRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/delete/campaigns

        Delete campaigns  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific document
        """
        endpoint = "/adsApi/v1/delete/campaigns"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def delete_target(self, body: DeleteTargetRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/delete/targets

        Delete target  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific documentati
        """
        endpoint = "/adsApi/v1/delete/targets"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def list_location_index(self, next_token: str | None = None, max_results: str | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_ads_manager_account_id: str | None = None) -> JSONData | JSONList:
        """GET /adsApi/v1/locationIndexes

        List all Smart Location Indexes for the authenticated advertiser. Returns a paginated collection of indexes including th
        """
        endpoint = "/adsApi/v1/locationIndexes"
        params: dict[str, Any] = {}
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-AccountId"] = amazon_ads_manager_account_id
        return await self.get(endpoint, params=params)

    async def query_ad_association(self, body: QueryAdAssociationRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/query/adAssociations

        Query Ad Association  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific docu
        """
        endpoint = "/adsApi/v1/query/adAssociations"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def query_ad_extension(self, body: QueryAdExtensionRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/query/adExtensions

        Query ad_extension - API is in open beta  **Note:** Batch size limits are specific to each ad product. Refer to the ad-p
        """
        endpoint = "/adsApi/v1/query/adExtensions"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def query_ad_group(self, body: QueryAdGroupRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/query/adGroups

        List ad groups  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific documentat
        """
        endpoint = "/adsApi/v1/query/adGroups"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def query_ad(self, body: QueryAdRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/query/ads

        List ads  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific documentation fo
        """
        endpoint = "/adsApi/v1/query/ads"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def sb_query_advertising_deal_target(self, body: SBQueryAdvertisingDealTargetRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/query/advertisingDealTargets/sb

        Query advertisingDealTarget  **Requires one of these permissions**: ['advertiser_campaign_edit', 'advertiser_campaign_vi
        """
        endpoint = "/adsApi/v1/query/advertisingDealTargets/sb"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def sb_query_advertising_deal(self, body: SBQueryAdvertisingDealRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/query/advertisingDeals/sb

        Query advertisingDeal  **Requires one of these permissions**: ['advertiser_campaign_edit', 'advertiser_campaign_view']
        """
        endpoint = "/adsApi/v1/query/advertisingDeals/sb"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def query_brand_store_edition_publish_version(self, body: QueryBrandStoreEditionPublishVersionRequest | dict[str, Any] | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/query/brandStoreEditionPublishVersions

        Query store edition publish versions  **Requires one of these permissions**: ['amazon_stores_edit','amazon_stores_view']
        """
        endpoint = "/adsApi/v1/query/brandStoreEditionPublishVersions"
        params: dict[str, Any] = {}
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def query_brand_store_page(self, body: QueryBrandStorePageRequest | dict[str, Any] | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/query/brandStorePages

        Retrieve brand store page content  **Requires one of these permissions**: ['amazon_stores_edit','amazon_stores_view']
        """
        endpoint = "/adsApi/v1/query/brandStorePages"
        params: dict[str, Any] = {}
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def query_brand_store(self, body: QueryBrandStoreRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/query/brandStores

        Query brand store content  **Requires one of these permissions**: ['advertiser_campaign_edit', 'creatives_view', 'accoun
        """
        endpoint = "/adsApi/v1/query/brandStores"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def query_campaign(self, body: QueryCampaignRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/query/campaigns

        Query campaign  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific documentat
        """
        endpoint = "/adsApi/v1/query/campaigns"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def sb_query_recommendation_type(self, body: SBQueryRecommendationTypeRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/query/recommendationTypes/sb

        Query RecommendationTypes  **Requires one of these permissions**: ['advertiser_campaign_view']
        """
        endpoint = "/adsApi/v1/query/recommendationTypes/sb"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def query_target(self, body: QueryTargetRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/query/targets

        List target  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific documentation
        """
        endpoint = "/adsApi/v1/query/targets"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def dsp_retrieve_campaign_forecast(self, body: DSPRetrieveCampaignForecastRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/retrieve/campaignForecasts/dsp

        Retrieve campaign forecast  **Requires one of these permissions**: ['campaign_view', 'advertiser_campaign_view']
        """
        endpoint = "/adsApi/v1/retrieve/campaignForecasts/dsp"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def dsp_retrieve_commitment_spend(self, body: DSPRetrieveCommitmentSpendRequest | dict[str, Any] | None = None, amazon_ads_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/retrieve/commitmentSpends/dsp

        Retrieve commitment spend  **Requires one of these permissions**: []
        """
        endpoint = "/adsApi/v1/retrieve/commitmentSpends/dsp"
        params: dict[str, Any] = {}
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def dsp_retrieve_commitment(self, body: DSPRetrieveCommitmentRequest | dict[str, Any] | None = None, amazon_ads_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/retrieve/commitments/dsp

        Get Commitments  **Requires one of these permissions**: []
        """
        endpoint = "/adsApi/v1/retrieve/commitments/dsp"
        params: dict[str, Any] = {}
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def retrieve_location_index(self, body: RetrieveLocationIndexRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_ads_manager_account_id: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/retrieve/locationIndexes

        Retrieve one or more Smart Location Indexes by ID. Returns the current metadata and processing status for each requested
        """
        endpoint = "/adsApi/v1/retrieve/locationIndexes"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-AccountId"] = amazon_ads_manager_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def update_ad_association(self, body: UpdateAdAssociationRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/update/adAssociations

        Update Ad Association  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific doc
        """
        endpoint = "/adsApi/v1/update/adAssociations"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def update_ad_extension(self, body: UpdateAdExtensionRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/update/adExtensions

        Update ad_extension - API is in open beta  **Note:** Batch size limits are specific to each ad product. Refer to the ad-
        """
        endpoint = "/adsApi/v1/update/adExtensions"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def update_ad_group(self, body: UpdateAdGroupRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/update/adGroups

        Update ad groups  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific document
        """
        endpoint = "/adsApi/v1/update/adGroups"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def update_ad(self, body: UpdateAdRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/update/ads

        Update ads  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific documentation
        """
        endpoint = "/adsApi/v1/update/ads"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def sb_update_advertising_deal(self, body: SBUpdateAdvertisingDealRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/update/advertisingDeals/sb

        Update advertisingDeal  **Requires one of these permissions**: ['advertiser_campaign_edit', 'advertiser_campaign_view']
        """
        endpoint = "/adsApi/v1/update/advertisingDeals/sb"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def update_brand_store_edition_publish_version(self, body: UpdateBrandStoreEditionPublishVersionRequest | dict[str, Any] | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/update/brandStoreEditionPublishVersions

        Update store edition publish versions  **Requires one of these permissions**: ['amazon_stores_edit']
        """
        endpoint = "/adsApi/v1/update/brandStoreEditionPublishVersions"
        params: dict[str, Any] = {}
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def update_campaign(self, body: UpdateCampaignRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/update/campaigns

        Update campaign  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific documenta
        """
        endpoint = "/adsApi/v1/update/campaigns"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def dsp_update_commitment(self, body: DSPUpdateCommitmentRequest | dict[str, Any] | None = None, amazon_ads_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/update/commitments/dsp

        Update commitments  **Requires one of these permissions**: []
        """
        endpoint = "/adsApi/v1/update/commitments/dsp"
        params: dict[str, Any] = {}
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def update_location_index(self, body: UpdateLocationIndexRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_ads_manager_account_id: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/update/locationIndexes

        Update the data for an existing Smart Location Index. Replaces the index's postal code values with the provided dataset.
        """
        endpoint = "/adsApi/v1/update/locationIndexes"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-AccountId"] = amazon_ads_manager_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def update_target(self, body: UpdateTargetRequest | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/update/targets

        Update target  **Note:** Batch size limits are specific to each ad product. Refer to the ad-product-specific documentati
        """
        endpoint = "/adsApi/v1/update/targets"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_client_id is not None:
            params["Amazon-Ads-ClientId"] = amazon_ads_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

