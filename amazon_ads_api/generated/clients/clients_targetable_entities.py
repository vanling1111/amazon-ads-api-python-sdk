"""Auto-generated async API client. Do not edit manually.

Source: TargetableEntities_prod_3p.json
Title:  Targetable Entities
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_targetable_entities import *  # noqa: F403
except ImportError:
    pass


class TargetableEntitiesClient(BaseAdsClient):
    """Auto-generated from TargetableEntities_prod_3p.json (3 operations)"""

    async def list_targetable_entities(self, body: ListTargetableEntitiesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_account_id: str | None = None) -> JSONData | JSONList:
        """POST /targetableEntities/list

        **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser Account ID  **Parameter name**: Amazon-Advertising-Acc
        """
        endpoint = "/targetableEntities/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_account_id is not None:
            params["Amazon-Advertising-AccountId"] = amazon_advertising_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.Mindreader.TargetableEntitiesResource.v1+json")

    async def list_targetable_entity_paths(self, body: ListTargetableEntityPathsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_account_id: str | None = None) -> JSONData | JSONList:
        """POST /targetableEntities/paths/list

        **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser Account ID  **Parameter name**: Amazon-Advertising-Acc
        """
        endpoint = "/targetableEntities/paths/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_account_id is not None:
            params["Amazon-Advertising-AccountId"] = amazon_advertising_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.Mindreader.TargetableEntitiesResource.v1+json")

    async def text_input_search(self, body: TextInputSearchRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_account_id: str | None = None) -> JSONData | JSONList:
        """POST /textinput/targetableEntities

        **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser Account ID  **Parameter name**: Amazon-Advertising-Acc
        """
        endpoint = "/textinput/targetableEntities"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_account_id is not None:
            params["Amazon-Advertising-AccountId"] = amazon_advertising_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.Mindreader.TextInputResource.v1+json")

