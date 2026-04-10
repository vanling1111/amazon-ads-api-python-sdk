"""Auto-generated async API client. Do not edit manually.

Source: PersonaBuilderAPI_prod_3p.json
Title:  Persona Builder API
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_persona_builder import *  # noqa: F403
except ImportError:
    pass


class PersonaBuilderClient(BaseAdsClient):
    """Auto-generated from PersonaBuilderAPI_prod_3p.json (5 operations)"""

    async def banded_size(self, body: InputExpression | dict[str, Any] | None = None, advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /insights/bandedSize

        Get banded size of number of unique customers that are in the input expression.  **Authorized resource type**: DSP Rodeo
        """
        endpoint = "/insights/bandedSize"
        params: dict[str, Any] = {}
        if advertiser_id is not None:
            params["advertiserId"] = advertiser_id
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.bandedsizeinputexpression.v1+json")

    async def demographics(self, body: InputExpression | dict[str, Any] | None = None, advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /insights/demographics

        Get demographic insights for the input expression.  **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser Ac
        """
        endpoint = "/insights/demographics"
        params: dict[str, Any] = {}
        if advertiser_id is not None:
            params["advertiserId"] = advertiser_id
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.demographicinputexpressions.v1+json")

    async def prime_video(self, body: PrimeVideoInputExpression | dict[str, Any] | None = None, advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /insights/primeVideo

        Get Prime Video insights for the input expression.  **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser Ac
        """
        endpoint = "/insights/primeVideo"
        params: dict[str, Any] = {}
        if advertiser_id is not None:
            params["advertiserId"] = advertiser_id
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.primevideoinputexpressions.v1+json")

    async def top_categories_purchased(self, body: InputExpression | dict[str, Any] | None = None, advertiser_id: str | None = None, max_results: str | None = None, next_token: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /insights/topCategoriesPurchased

        Get insights on top retail categories purchased by customers in the input expression.  **Authorized resource type**: DSP
        """
        endpoint = "/insights/topCategoriesPurchased"
        params: dict[str, Any] = {}
        if advertiser_id is not None:
            params["advertiserId"] = advertiser_id
        if max_results is not None:
            params["maxResults"] = max_results
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.topcategoriespurchasedinputexpression.v1+json")

    async def top_overlapping_audiences(self, body: TopOverlappingAudiencesInputExpression | dict[str, Any] | None = None, advertiser_id: str | None = None, max_results: str | None = None, next_token: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /insights/topOverlappingAudiences

        Get top audiences overlapping with the input expression.  **Authorized resource type**: DSP Rodeo Entity ID, DSP Adverti
        """
        endpoint = "/insights/topOverlappingAudiences"
        params: dict[str, Any] = {}
        if advertiser_id is not None:
            params["advertiserId"] = advertiser_id
        if max_results is not None:
            params["maxResults"] = max_results
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.topoverlappingaudiencesinputexpression.v1+json")

