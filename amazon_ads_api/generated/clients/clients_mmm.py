"""Auto-generated async API client. Do not edit manually.

Source: MarketingMixModeling_prod_3p.json
Title:  Marketing Mix Modeling
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_mmm import *  # noqa: F403
except ImportError:
    pass


class MmmClient(BaseAdsClient):
    """Auto-generated from MarketingMixModeling_prod_3p.json (10 operations)"""

    async def create_mmm_brand_group_overrides(self, body: dict[str, Any] | None = None) -> JSONData | JSONList:
        """POST /mmm/v1/brandGroupOverrides

        Create brand group overrides
        """
        endpoint = "/mmm/v1/brandGroupOverrides"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data)

    async def delete_mmm_brand_group_overrides(self, body: dict[str, Any] | None = None) -> JSONData | JSONList:
        """POST /mmm/v1/brandGroupOverrides/delete

        Delete brand group overrides
        """
        endpoint = "/mmm/v1/brandGroupOverrides/delete"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data)

    async def list_mmm_brand_group_overrides(self, body: dict[str, Any] | None = None) -> JSONData | JSONList:
        """POST /mmm/v1/brandGroupOverrides/list

        List brand group overrides
        """
        endpoint = "/mmm/v1/brandGroupOverrides/list"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data)

    async def list_mmm_brand_groups(self, body: dict[str, Any] | None = None) -> JSONData | JSONList:
        """POST /mmm/v1/brandGroups/list

        List brand groups
        """
        endpoint = "/mmm/v1/brandGroups/list"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data)

    async def get_mmm_brand_group_campaigns(self, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """GET /mmm/v1/brandGroups/{brandGroupId}/campaigns

        Get campaigns in a brand group
        """
        endpoint = "/mmm/v1/brandGroups/{brandGroupId}/campaigns"
        params: dict[str, Any] = {}
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        return await self.get(endpoint, params=params)

    async def get_mmm_brand_group_products(self, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """GET /mmm/v1/brandGroups/{brandGroupId}/products

        Get products in a brand group
        """
        endpoint = "/mmm/v1/brandGroups/{brandGroupId}/products"
        params: dict[str, Any] = {}
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        return await self.get(endpoint, params=params)

    async def create_mmm_report(self, body: dict[str, Any] | None = None) -> JSONData | JSONList:
        """POST /mmm/v1/reports

        Create a report
        """
        endpoint = "/mmm/v1/reports"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data)

    async def list_mmm_reports(self, body: dict[str, Any] | None = None) -> JSONData | JSONList:
        """POST /mmm/v1/reports/list

        List reports
        """
        endpoint = "/mmm/v1/reports/list"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data)

    async def delete_mmm_report(self) -> JSONData | JSONList:
        """DELETE /mmm/v1/reports/{reportId}

        Delete a report
        """
        endpoint = "/mmm/v1/reports/{reportId}"
        return await self.delete(endpoint)

    async def get_mmm_report(self) -> JSONData | JSONList:
        """GET /mmm/v1/reports/{reportId}

        Get a report
        """
        endpoint = "/mmm/v1/reports/{reportId}"
        return await self.get(endpoint)

