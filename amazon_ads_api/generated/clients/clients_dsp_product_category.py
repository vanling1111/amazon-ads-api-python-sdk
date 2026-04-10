"""Auto-generated async API client. Do not edit manually.

Source: AdGroupTargeting-ProductCategory_prod_3p.json
Title:  Ad Group Targeting - Product Category
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_dsp_product_category import *  # noqa: F403
except ImportError:
    pass


class DspProductCategoryClient(BaseAdsClient):
    """Auto-generated from AdGroupTargeting-ProductCategory_prod_3p.json (3 operations)"""

    async def dsp_get_ad_group_product_category_targets(self, ad_group_id: str, next_token: str | None = None, max_results: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /dsp/adGroups/{adGroupId}/targetingTypes/productCategory/targets

        Gets a list of product category targets associated to an ad group.  **Requires one of these permissions**: []
        """
        endpoint = f"/dsp/adGroups/{ad_group_id}/targetingTypes/productCategory/targets"
        params: dict[str, Any] = {}
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def dsp_create_ad_group_product_category_targets(self, ad_group_id: str, body: DspCreateAdGroupProductCategoryTargetsRequestContentV1 | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/adGroups/{adGroupId}/targetingTypes/productCategory/targets

        Creates and associates one or more product category targets to an ad group.  **Requires one of these permissions**: []
        """
        endpoint = f"/dsp/adGroups/{ad_group_id}/targetingTypes/productCategory/targets"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspadgroupproductcategorytargets.v1+json")

    async def dsp_delete_ad_group_product_category_targets(self, ad_group_id: str, body: DspDeleteAdGroupProductCategoryTargetsRequestContentV1 | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/adGroups/{adGroupId}/targetingTypes/productCategory/targets/delete

        Removes one or more product category targets from an ad group.  **Requires one of these permissions**: []
        """
        endpoint = f"/dsp/adGroups/{ad_group_id}/targetingTypes/productCategory/targets/delete"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspadgroupproductcategorytargets.v1+json")

