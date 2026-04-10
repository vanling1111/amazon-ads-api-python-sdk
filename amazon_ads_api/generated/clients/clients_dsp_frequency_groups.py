"""Auto-generated async API client. Do not edit manually.

Source: D16GFMApiFrequencyGroupV1_prod_3p.json
Title:  D16GFMApiFrequencyGroupV1
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_dsp_frequency_groups import *  # noqa: F403
except ImportError:
    pass


class DspFrequencyGroupsClient(BaseAdsClient):
    """Auto-generated from D16GFMApiFrequencyGroupV1_prod_3p.json (4 operations)"""

    async def create_frequency_group_v1(self, body: CreateFrequencyGroupsV1 | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /frequencyGroups/v1

        Creates a frequency group with basic details and generates a frequency group identifier.  **Authorized resource type**:
        """
        endpoint = "/frequencyGroups/v1"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
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

    async def list_frequency_groups_v1(self, body: ListFrequencyGroupsRequestContentV1 | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /frequencyGroups/v1/list

        Gets a list of frequency groups for a given advertiser or entity.  **Authorized resource type**: Global Ad Account ID  *
        """
        endpoint = "/frequencyGroups/v1/list"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-AccountId"] = amazon_ads_manager_account_id
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

    async def get_frequency_group_v1(self, frequency_group_id: str, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /frequencyGroups/v1/{frequencyGroupId}

        Gets basic details for a frequency group given a frequency group identifier.  **Authorized resource type**: Global Ad Ac
        """
        endpoint = f"/frequencyGroups/v1/{frequency_group_id}"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def patch_frequency_group_v1(self, frequency_group_id: str, body: PatchFrequencyGroupRequestContentV1 | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PATCH /frequencyGroups/v1/{frequencyGroupId}

        Updates a frequency group.  **Authorized resource type**: Global Ad Account ID  **Parameter name**: Amazon-Ads-AccountId
        """
        endpoint = f"/frequencyGroups/v1/{frequency_group_id}"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
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
        return await self._request('PATCH', endpoint, json_data=json_data, params=params)

