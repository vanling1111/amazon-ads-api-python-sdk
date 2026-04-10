"""Auto-generated async API client. Do not edit manually.

Source: BrandBenchmarks_prod_3p.json
Title:  Brand Benchmarks
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_brand_benchmarks import *  # noqa: F403
except ImportError:
    pass


class BrandBenchmarksClient(BaseAdsClient):
    """Auto-generated from BrandBenchmarks_prod_3p.json (2 operations)"""

    async def list_advertiser_report_metadata(self, advertiser_id: str, next_token: str | None = None, max_results: str | None = None, latest_only: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """GET /insights/brandBenchmarks/advertisers/{advertiserId}/allReportMetadata

        Gets all of the report metadata the specified advertiser at the specified marketplace.  **Authorized resource type**: Gl
        """
        endpoint = f"/insights/brandBenchmarks/advertisers/{advertiser_id}/allReportMetadata"
        params: dict[str, Any] = {}
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        if latest_only is not None:
            params["latestOnly"] = latest_only
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        return await self.get(endpoint, params=params)

    async def get_advertiser_report(self, advertiser_id: str, index_date: str, report_type: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """GET /insights/brandBenchmarks/advertisers/{advertiserId}/reports/{reportType}/indexDates/{indexDate}

        Gets the download link for an advertiser's metric report in the specified marketplace.  **Authorized resource type**: Gl
        """
        endpoint = f"/insights/brandBenchmarks/advertisers/{advertiser_id}/reports/{report_type}/indexDates/{index_date}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        return await self.get(endpoint, params=params)

