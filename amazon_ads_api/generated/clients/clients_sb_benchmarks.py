"""Auto-generated async API client. Do not edit manually.

Source: SponsoredBrandsCategoryBenchmark_prod_3p.json
Title:  Sponsored Brands Category Benchmark
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_sb_benchmarks import *  # noqa: F403
except ImportError:
    pass


class SbBenchmarksClient(BaseAdsClient):
    """Auto-generated from SponsoredBrandsCategoryBenchmark_prod_3p.json (3 operations)"""

    async def get_brands(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, next_page_token: str | None = None, program_type: str | None = None) -> JSONData | JSONList:
        """GET /benchmarks/brands

        Gets a list of brands
        """
        endpoint = "/benchmarks/brands"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if next_page_token is not None:
            params["nextPageToken"] = next_page_token
        if program_type is not None:
            params["programType"] = program_type
        return await self.get(endpoint, params=params)

    async def get_time_series(self, brand_name: str, category_id: str, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /benchmarks/brands/{brandName}/categories/{categoryId}

        Provides time series data
        """
        endpoint = f"/benchmarks/brands/{brand_name}/categories/{category_id}"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.timeseriesdata.v1+json")

    async def get_report_data(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /benchmarks/brandsAndCategories

        Provides entire report data of peer benchmarks
        """
        endpoint = "/benchmarks/brandsAndCategories"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.reportdata.v1+json")

