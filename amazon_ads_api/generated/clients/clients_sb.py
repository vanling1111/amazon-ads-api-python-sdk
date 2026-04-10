"""Auto-generated async API client. Do not edit manually.

Source: SponsoredBrands_v4_openapi.json
Title:  Sponsored Brands campaign management
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_sb import *  # noqa: F403
except ImportError:
    pass


class SbClient(BaseAdsClient):
    """Auto-generated from SponsoredBrands_v4_openapi.json (53 operations)"""

    async def create_sponsored_brands_campaigns(self, body: CreateSponsoredBrandsCampaignsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/campaigns

        Create campaigns
        """
        endpoint = "/sb/v4/campaigns"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbcampaignresource.v4+json")

    async def update_sponsored_brands_campaigns(self, body: UpdateSponsoredBrandsCampaignsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /sb/v4/campaigns

        Update campaigns
        """
        endpoint = "/sb/v4/campaigns"
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbcampaignresource.v4+json")

    async def list_sponsored_brands_campaigns(self, body: ListSponsoredBrandsCampaignsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/campaigns/list

        List campaigns
        """
        endpoint = "/sb/v4/campaigns/list"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbcampaignresource.v4+json")

    async def delete_sponsored_brands_campaigns(self, body: DeleteSponsoredBrandsCampaignsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/campaigns/delete

        Delete campaigns.
        """
        endpoint = "/sb/v4/campaigns/delete"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbcampaignresource.v4+json")

    async def create_sponsored_brands_ad_groups(self, body: CreateSponsoredBrandsAdGroupsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/adGroups

        Create ad groups
        """
        endpoint = "/sb/v4/adGroups"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbadgroupresource.v4+json")

    async def update_sponsored_brands_ad_groups(self, body: UpdateSponsoredBrandsAdGroupsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /sb/v4/adGroups

        Update ad groups
        """
        endpoint = "/sb/v4/adGroups"
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbadgroupresource.v4+json")

    async def list_sponsored_brands_ad_groups(self, body: ListSponsoredBrandsAdGroupsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/adGroups/list

        List ad groups
        """
        endpoint = "/sb/v4/adGroups/list"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbadgroupresource.v4+json")

    async def delete_sponsored_brands_ad_groups(self, body: DeleteSponsoredBrandsAdGroupsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/adGroups/delete

        Delete ad groups
        """
        endpoint = "/sb/v4/adGroups/delete"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbadgroupresource.v4+json")

    async def create_sponsored_brands_auto_collection_ads(self, body: CreateSponsoredBrandsAutoCollectionAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/ads/autoCollection

        Create Sponsored Brands Auto Collection Ads
        """
        endpoint = "/sb/v4/ads/autoCollection"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbadresource.v4+json")

    async def create_sponsored_brands_manual_collection_ads(self, body: CreateSponsoredBrandsManualCollectionAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/ads/manualCollection

        Create Sponsored Brands Manual Collection Ads
        """
        endpoint = "/sb/v4/ads/manualCollection"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbadresource.v4+json")

    async def create_sponsored_brands_brand_video_ads(self, body: CreateSponsoredBrandsBrandVideoAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/ads/brandVideo

        Create brand video ads
        """
        endpoint = "/sb/v4/ads/brandVideo"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbadresource.v4+json")

    async def create_sponsored_brands_extended_product_collection_ads(self, body: CreateSponsoredBrandsExtendedProductCollectionAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/ads/productCollectionExtended

        Creates Sponsored Brands new product collection ads with collection of custom images
        """
        endpoint = "/sb/v4/ads/productCollectionExtended"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbadresource.v4+json")

    async def create_sponsored_brands_video_ads(self, body: CreateSponsoredBrandsVideoAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/ads/video

        Create video ads
        """
        endpoint = "/sb/v4/ads/video"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbadresource.v4+json")

    async def create_sponsored_brands_product_collection_ads(self, body: CreateSponsoredBrandsProductCollectionAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/ads/productCollection

        Create product collection ads
        """
        endpoint = "/sb/v4/ads/productCollection"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbadresource.v4+json")

    async def create_sponsored_brand_store_spotlight_ads(self, body: CreateSponsoredBrandStoreSpotlightAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/ads/storeSpotlight

        Create store spotlight ads
        """
        endpoint = "/sb/v4/ads/storeSpotlight"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbadresource.v4+json")

    async def update_sponsored_brands_ads(self, body: UpdateSponsoredBrandsAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /sb/v4/ads

        Update ads
        """
        endpoint = "/sb/v4/ads"
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbadresource.v4+json")

    async def update_sponsored_brands_auto_collection_ads(self, body: UpdateSponsoredBrandsAutoCollectionAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/ads/creatives/autoCollection

        Update Sponsored Brands Auto Collection Ads
        """
        endpoint = "/sb/ads/creatives/autoCollection"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbadresource.v4+json")

    async def update_sponsored_brands_manual_collection_ads(self, body: UpdateSponsoredBrandsManualCollectionAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/ads/creatives/manualCollection

        Update Sponsored Brands Manual Collection Ads
        """
        endpoint = "/sb/ads/creatives/manualCollection"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbadresource.v4+json")

    async def list_sponsored_brands_ads(self, body: ListSponsoredBrandsAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/ads/list

        List ads
        """
        endpoint = "/sb/v4/ads/list"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbadresource.v4+json")

    async def delete_sponsored_brands_ads(self, body: DeleteSponsoredBrandsAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/ads/delete

        Delete ads
        """
        endpoint = "/sb/v4/ads/delete"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbadresource.v4+json")

    async def create_brand_video_creative(self, body: CreateBrandVideoCreativeRequestContent | dict[str, Any] | None = None, accept: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/ads/creatives/brandVideo

        Create new version of brand video ad creative
        """
        endpoint = "/sb/ads/creatives/brandVideo"
        params: dict[str, Any] = {}
        if accept is not None:
            params["Accept"] = accept
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbAdCreativeResource.v4+json")

    async def create_extended_product_collection_creative(self, body: CreateExtendedProductCollectionCreativeRequestContent | dict[str, Any] | None = None, accept: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/ads/creatives/productCollectionExtended

        Creates Sponsored Brands new version of product collection with collection of custom image ads
        """
        endpoint = "/sb/ads/creatives/productCollectionExtended"
        params: dict[str, Any] = {}
        if accept is not None:
            params["Accept"] = accept
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbAdCreativeResource.v4+json")

    async def create_video_creative(self, body: CreateVideoCreativeRequestContent | dict[str, Any] | None = None, accept: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/ads/creatives/video

        Create new version of video ad creative
        """
        endpoint = "/sb/ads/creatives/video"
        params: dict[str, Any] = {}
        if accept is not None:
            params["Accept"] = accept
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbAdCreativeResource.v4+json")

    async def create_product_collection_creative(self, body: CreateProductCollectionCreativeRequestContent | dict[str, Any] | None = None, accept: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/ads/creatives/productCollection

        Create new version of product collection ad creative
        """
        endpoint = "/sb/ads/creatives/productCollection"
        params: dict[str, Any] = {}
        if accept is not None:
            params["Accept"] = accept
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbAdCreativeResource.v4+json")

    async def create_store_spotlight_creative(self, body: CreateStoreSpotlightCreativeRequestContent | dict[str, Any] | None = None, accept: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/ads/creatives/storeSpotlight

        Create new version of store spotlight ad creative
        """
        endpoint = "/sb/ads/creatives/storeSpotlight"
        params: dict[str, Any] = {}
        if accept is not None:
            params["Accept"] = accept
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbAdCreativeResource.v4+json")

    async def list_creatives(self, body: ListCreativesRequestContent | dict[str, Any] | None = None, accept: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/ads/creatives/list

        List ad creatives
        """
        endpoint = "/sb/ads/creatives/list"
        params: dict[str, Any] = {}
        if accept is not None:
            params["Accept"] = accept
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbAdCreativeResource.v4+json")

    async def sb_targeting_get_negative_brands(self, next_token: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sb/negativeTargets/brands/recommendations

        Get brand recommendations for negative targeting
        """
        endpoint = "/sb/negativeTargets/brands/recommendations"
        params: dict[str, Any] = {}
        if next_token is not None:
            params["nextToken"] = next_token
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def sb_optimization_recommendation(self, body: SBOptimizationRecommendationRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/recommendations/optimization

        Get recommendation for optimization rule
        """
        endpoint = "/sb/recommendations/optimization"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sboptimizationrecommendationresource.v4+json")

    async def get_headline_recommendations(self, body: HeadlineSuggestionRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/recommendations/creative/headline

        Get recommendations for creative headline
        """
        endpoint = "/sb/recommendations/creative/headline"
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

    async def get_budget_recommendations(self, body: GetBudgetRecommendationsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /sb/campaigns/budgetRecommendations

        Get budget recommendations
        """
        endpoint = "/sb/campaigns/budgetRecommendations"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbbudgetrecommendation.v4+json")

    async def sb_targeting_get_targetable_categories(self, locale: str | None = None, supply_source: str | None = None, include_only_root_categories: str | None = None, parent_category_refinement_id: str | None = None, next_token: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sb/targets/categories

        Get targetable categories
        """
        endpoint = "/sb/targets/categories"
        params: dict[str, Any] = {}
        if locale is not None:
            params["locale"] = locale
        if supply_source is not None:
            params["supplySource"] = supply_source
        if include_only_root_categories is not None:
            params["includeOnlyRootCategories"] = include_only_root_categories
        if parent_category_refinement_id is not None:
            params["parentCategoryRefinementId"] = parent_category_refinement_id
        if next_token is not None:
            params["nextToken"] = next_token
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def sb_targeting_get_targetable_asin_counts(self, body: SBTargetingGetTargetableASINCountsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/targets/products/count

        Get number of products in a category
        """
        endpoint = "/sb/targets/products/count"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbtargeting.v4+json")

    async def sb_targeting_get_refinements_for_category(self, category_refinement_id: str, locale: str | None = None, next_token: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sb/targets/categories/{categoryRefinementId}/refinements

        Get refinements for category
        """
        endpoint = f"/sb/targets/categories/{category_refinement_id}/refinements"
        params: dict[str, Any] = {}
        if locale is not None:
            params["locale"] = locale
        if next_token is not None:
            params["nextToken"] = next_token
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def sb_insights_campaign_insights(self, body: SBInsightsCampaignInsightsRequestContent | dict[str, Any] | None = None, next_token: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/campaigns/insights

        Get insights for campaigns
        """
        endpoint = "/sb/campaigns/insights"
        params: dict[str, Any] = {}
        if next_token is not None:
            params["nextToken"] = next_token
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbinsights.v4+json")

    async def create_budget_rules_for_sb_campaigns(self, body: CreateSBBudgetRulesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/budgetRules

        Create budget rules
        """
        endpoint = "/sb/budgetRules"
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

    async def update_budget_rules_for_sb_campaigns(self, body: UpdateSBBudgetRulesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /sb/budgetRules

        Update budget rules
        """
        endpoint = "/sb/budgetRules"
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

    async def get_sb_budget_rules_for_advertiser(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, next_token: str | None = None, page_size: str | None = None) -> JSONData | JSONList:
        """GET /sb/budgetRules

        Get budget rules
        """
        endpoint = "/sb/budgetRules"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if next_token is not None:
            params["nextToken"] = next_token
        if page_size is not None:
            params["pageSize"] = page_size
        return await self.get(endpoint, params=params)

    async def get_budget_rule_by_rule_id_for_sb_campaigns(self, budget_rule_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sb/budgetRules/{budgetRuleId}

        Get budget rule by ID
        """
        endpoint = f"/sb/budgetRules/{budget_rule_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def create_associated_budget_rules_for_sb_campaigns(self, campaign_id: str, body: CreateAssociatedBudgetRulesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/campaigns/{campaignId}/budgetRules

        Associate budget rules to campaign
        """
        endpoint = f"/sb/campaigns/{campaign_id}/budgetRules"
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

    async def list_associated_budget_rules_for_sb_campaigns(self, campaign_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sb/campaigns/{campaignId}/budgetRules

        Get budget rules associated to campaign
        """
        endpoint = f"/sb/campaigns/{campaign_id}/budgetRules"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def get_campaigns_associated_with_sb_budget_rule(self, budget_rule_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, next_token: str | None = None, page_size: str | None = None) -> JSONData | JSONList:
        """GET /sb/budgetRules/{budgetRuleId}/campaigns

        Get campaigns associated with budget rule
        """
        endpoint = f"/sb/budgetRules/{budget_rule_id}/campaigns"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if next_token is not None:
            params["nextToken"] = next_token
        if page_size is not None:
            params["pageSize"] = page_size
        return await self.get(endpoint, params=params)

    async def disassociate_associated_budget_rule_for_sb_campaigns(self, campaign_id: str, budget_rule_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """DELETE /sb/campaigns/{campaignId}/budgetRules/{budgetRuleId}

        Disassociate budget rule from campaign
        """
        endpoint = f"/sb/campaigns/{campaign_id}/budgetRules/{budget_rule_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.delete(endpoint, params=params)

    async def sb_campaigns_budget_usage(self, body: BudgetUsageCampaignRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/campaigns/budget/usage

        Get budget usage
        """
        endpoint = "/sb/campaigns/budget/usage"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbcampaignbudgetusage.v1+json")

    async def sb_campaign_performance_forecasts(self, body: SBCampaignPerformanceForecastsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/forecasts

        Get performance forecasts for campaigns
        """
        endpoint = "/sb/forecasts"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbforecasting.v4+json")

    async def create_sponsored_brands_optimization_rules(self, body: CreateSponsoredBrandsOptimizationRulesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/rules/optimization

        Create optimization rules
        """
        endpoint = "/sb/rules/optimization"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbruleoptimization.v4+json")

    async def update_sponsored_brands_optimization_rules(self, body: UpdateSponsoredBrandsOptimizationRulesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /sb/rules/optimization

        Update optimization rules
        """
        endpoint = "/sb/rules/optimization"
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbruleoptimization.v4+json")

    async def associate_sponsored_brands_optimization_rules(self, body: AssociateSponsoredBrandsOptimizationRulesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/rules/optimization/associate

        Associate optimization rules
        """
        endpoint = "/sb/rules/optimization/associate"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbruleoptimization.v4+json")

    async def list_sponsored_brands_optimization_rules(self, body: ListSponsoredBrandsOptimizationRulesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/rules/optimization/list

        List optimization rules
        """
        endpoint = "/sb/rules/optimization/list"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbruleoptimization.v4+json")

    async def disassociate_sponsored_brands_optimization_rules(self, body: DisassociateSponsoredBrandsOptimizationRulesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/rules/optimization/disassociate

        Disassociate optimization rules
        """
        endpoint = "/sb/rules/optimization/disassociate"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sbruleoptimization.v4+json")

    async def start_migration_job(self, body: StartMigrationJobRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/legacyCampaigns/migrationJob

        Creates Migration Job for V3 campaigns.
        """
        endpoint = "/sb/v4/legacyCampaigns/migrationJob"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4+json")

    async def migration_job_results(self, body: MigrationJobResultsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/legacyCampaigns/migrationJob/results

        List Migration Results of all Campaign.
        """
        endpoint = "/sb/v4/legacyCampaigns/migrationJob/results"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4+json")

    async def migration_job_status(self, body: MigrationJobStatusRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/legacyCampaigns/migrationJob/status

        List Migration Job Status.
        """
        endpoint = "/sb/v4/legacyCampaigns/migrationJob/status"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4+json")

    async def migration_results(self, body: MigrationResultsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sb/v4/legacyCampaigns/overallMigrationResults

        Lists all Campaign Migration results for an advertiser.
        """
        endpoint = "/sb/v4/legacyCampaigns/overallMigrationResults"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4+json")

