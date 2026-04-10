"""Auto-generated async API client. Do not edit manually.

Source: DSP_v3.1_openapi.yaml
Title:  Amazon Ads API - Amazon DSP
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_dsp_v3 import *  # noqa: F403
except ImportError:
    pass


class DspV3Client(BaseAdsClient):
    """Auto-generated from DSP_v3.1_openapi.yaml (27 operations)"""

    async def get_order(self, order_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /dsp/orders/{orderId}

        Gets an order with complete information specified by an identifier.
        """
        endpoint = f"/dsp/orders/{order_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def get_orders(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None, status_filter: str | None = None, order_id_filter: str | None = None, advertiser_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /dsp/orders/

        Gets one or more orders with basic information.
        """
        endpoint = "/dsp/orders/"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if status_filter is not None:
            params["statusFilter"] = status_filter
        if order_id_filter is not None:
            params["orderIdFilter"] = order_id_filter
        if advertiser_id_filter is not None:
            params["advertiserIdFilter"] = advertiser_id_filter
        return await self.get(endpoint, params=params)

    async def update_orders(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /dsp/orders/

        Update an order.
        """
        endpoint = "/dsp/orders/"
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.dsporders.v2.6+json")

    async def get_conversion_trackings(self, order_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /dsp/orders/{orderId}/conversionTracking

        Get conversion tracking information for given order.
        """
        endpoint = f"/dsp/orders/{order_id}/conversionTracking"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def put_dsp_orders_by_id_conversionTracking_products(self, order_id: str, body: ProductTrackingV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /dsp/orders/{orderId}/conversionTracking/products

        Add or remove conversion tracking products from the order.
        """
        endpoint = f"/dsp/orders/{order_id}/conversionTracking/products"
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspproducttracking.v1+json")

    async def get_line_items(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None, status_filter: str | None = None, order_id_filter: str | None = None, line_item_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /dsp/lineItems/

        Gets one or more line items with basic information.
        """
        endpoint = "/dsp/lineItems/"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if status_filter is not None:
            params["statusFilter"] = status_filter
        if order_id_filter is not None:
            params["orderIdFilter"] = order_id_filter
        if line_item_id_filter is not None:
            params["lineItemIdFilter"] = line_item_id_filter
        return await self.get(endpoint, params=params)

    async def update_line_items(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /dsp/lineItems/

        Update line item.
        """
        endpoint = "/dsp/lineItems/"
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.dsplineitems.v3.3+json")

    async def get_creatives(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None, creative_id_filter: str | None = None, advertiser_id_filter: str | None = None, line_item_type_filter: str | None = None) -> JSONData | JSONList:
        """GET /dsp/creatives/

        Gets one or more creatives.
        """
        endpoint = "/dsp/creatives/"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        if creative_id_filter is not None:
            params["creativeIdFilter"] = creative_id_filter
        if advertiser_id_filter is not None:
            params["advertiserIdFilter"] = advertiser_id_filter
        if line_item_type_filter is not None:
            params["lineItemTypeFilter"] = line_item_type_filter
        return await self.get(endpoint, params=params)

    async def get_image_creatives(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, creative_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /dsp/creatives/image

        [DEPRECATED] Get image creative(s).
        """
        endpoint = "/dsp/creatives/image"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if creative_id_filter is not None:
            params["creativeIdFilter"] = creative_id_filter
        return await self.get(endpoint, params=params)

    async def create_image_creative(self, body: DspCreateImageCreativesRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/creatives/image

        [DEPRECATED] Create image creative(s).
        """
        endpoint = "/dsp/creatives/image"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspcreateimagecreatives.v1+json")

    async def update_image_creative(self, body: DspUpdateImageCreativesRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /dsp/creatives/image

        [DEPRECATED] Update image creative(s).
        """
        endpoint = "/dsp/creatives/image"
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspupdateimagecreatives.v1+json")

    async def preview_image_creative(self, body: DspImageCreativePreviewRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/creatives/image/preview

        [DEPRECATED] Preview an image creative.
        """
        endpoint = "/dsp/creatives/image/preview"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dsppreviewimagecreatives.v1+json")

    async def get_video_creatives(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, creative_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /dsp/creatives/video

        [DEPRECATED] Get video creative(s)
        """
        endpoint = "/dsp/creatives/video"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if creative_id_filter is not None:
            params["creativeIdFilter"] = creative_id_filter
        return await self.get(endpoint, params=params)

    async def create_video_creatives(self, body: DspCreateVideoCreativesRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/creatives/video

        [DEPRECATED] Create video creative(s)
        """
        endpoint = "/dsp/creatives/video"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspcreatevideocreatives.v1+json")

    async def update_video_creatives(self, body: DspUpdateVideoCreativesRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /dsp/creatives/video

        [DEPRECATED] Update video creative(s)
        """
        endpoint = "/dsp/creatives/video"
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspupdatevideocreatives.v1+json")

    async def preview_video_creative(self, body: DspVideoCreativePreviewRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/creatives/video/preview

        [DEPRECATED] Preview a video creative
        """
        endpoint = "/dsp/creatives/video/preview"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dsppreviewvideocreatives.v1+json")

    async def get_rec_creatives(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, creative_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /dsp/creatives/rec

        [DEPRECATED] Get Responsive eCommerce Creative  (REC).
        """
        endpoint = "/dsp/creatives/rec"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if creative_id_filter is not None:
            params["creativeIdFilter"] = creative_id_filter
        return await self.get(endpoint, params=params)

    async def create_rec_creatives(self, body: DspCreateRecCreativesRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/creatives/rec

        [DEPRECATED] Create Responsive eCommerce Creatives(REC).
        """
        endpoint = "/dsp/creatives/rec"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspcreatereccreatives.v1+json")

    async def update_rec_creatives(self, body: DspUpdateRecCreativesRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /dsp/creatives/rec

        [DEPRECATED] Update Responsive eCommerce Creatives(REC).
        """
        endpoint = "/dsp/creatives/rec"
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspupdatereccreatives.v1+json")

    async def preview_rec_creative(self, body: DspRecCreativePreviewRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/creatives/rec/preview

        [DEPRECATED] Preview a Responsive eCommerce Creative(REC).
        """
        endpoint = "/dsp/creatives/rec/preview"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dsppreviewreccreatives.v1+json")

    async def get_third_party_creatives(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, creative_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /dsp/creatives/thirdparty

        [DEPRECATED] Get third party creative(s).
        """
        endpoint = "/dsp/creatives/thirdparty"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if creative_id_filter is not None:
            params["creativeIdFilter"] = creative_id_filter
        return await self.get(endpoint, params=params)

    async def create_third_party_creative(self, body: DspCreateThirdPartyCreativesRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/creatives/thirdparty

        [DEPRECATED] Create third party creative(s).
        """
        endpoint = "/dsp/creatives/thirdparty"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspcreatethirdpartycreatives.v1+json")

    async def update_third_party_creative(self, body: DspUpdateThirdPartyCreativesRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /dsp/creatives/thirdparty

        [DEPRECATED] Update third party creative(s).
        """
        endpoint = "/dsp/creatives/thirdparty"
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspupdatethirdpartycreatives.v1+json")

    async def preview_third_party_creative(self, body: DspThirdPartyCreativePreviewRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/creatives/thirdparty/preview

        [DEPRECATED] Preview third party creative.
        """
        endpoint = "/dsp/creatives/thirdparty/preview"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dsppreviewthirdpartycreatives.v1+json")

    async def get_creative_moderation(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, creative_id_filter: str | None = None) -> JSONData | JSONList:
        """GET /dsp/moderation/creatives

        [DEPRECATED] Get creative moderation summary by creativeId.
        """
        endpoint = "/dsp/moderation/creatives"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if creative_id_filter is not None:
            params["creativeIdFilter"] = creative_id_filter
        return await self.get(endpoint, params=params)

    async def associate_line_items_to_creatives(self, body: LineItemCreativeAssociationsRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/lineItemCreativeAssociations

        [DEPRECATED] Create/delete association between line item and creative.
        """
        endpoint = "/dsp/lineItemCreativeAssociations"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dsplineitemcreativeassociations.v2.1+json")

    async def get_geo_locations(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, geo_location_id_filter: str | None = None, text_query: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """GET /dsp/geoLocations

        Gets locationTargeting objects based on locationTargetingId or text query
        """
        endpoint = "/dsp/geoLocations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if geo_location_id_filter is not None:
            params["geoLocationIdFilter"] = geo_location_id_filter
        if text_query is not None:
            params["textQuery"] = text_query
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        return await self.get(endpoint, params=params)

