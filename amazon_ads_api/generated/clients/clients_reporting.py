"""Auto-generated async API client. Do not edit manually.

Source: OfflineReport_prod_3p.json
Title:  Offline Report
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_reporting import *  # noqa: F403
except ImportError:
    pass


class ReportingClient(BaseAdsClient):
    """Auto-generated from OfflineReport_prod_3p.json (3 operations)"""

    async def create_async_report(self, body: CreateAsyncReportRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /reporting/reports

        Creates a report request
        """
        endpoint = "/reporting/reports"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.createasyncreportrequest.v3+json")

    async def delete_async_report(self, report_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """DELETE /reporting/reports/{reportId}

        Deletes a report by id
        """
        endpoint = f"/reporting/reports/{report_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        return await self.delete(endpoint, params=params)

    async def get_async_report(self, report_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """GET /reporting/reports/{reportId}

        Gets a generation status of report by id
        """
        endpoint = f"/reporting/reports/{report_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        return await self.get(endpoint, params=params)

