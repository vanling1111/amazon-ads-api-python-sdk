"""Auto-generated async API client. Do not edit manually.

Source: DSPReports_prod_3p.json
Title:  DSP Reports
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_dsp_reports import *  # noqa: F403
except ImportError:
    pass


class DspReportsClient(BaseAdsClient):
    """Auto-generated from DSPReports_prod_3p.json (2 operations)"""

    async def create_report_v3(self, account_id: str, body: CreateReportRequestBodyV3 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /accounts/{accountId}/dsp/reports

        Creates a report request.
        """
        endpoint = f"/accounts/{account_id}/dsp/reports"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspcreatereports.v3+json")

    async def get_campaign_report_v3(self, account_id: str, report_id: str, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /accounts/{accountId}/dsp/reports/{reportId}

        Gets the metadata of a report previously requested.
        """
        endpoint = f"/accounts/{account_id}/dsp/reports/{report_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

