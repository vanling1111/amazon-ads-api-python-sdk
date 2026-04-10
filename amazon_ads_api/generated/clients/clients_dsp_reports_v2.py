"""Auto-generated async API client. Do not edit manually.

Source: DSP_Reports_v2_openapi.yaml
Title:  DSP Reports
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_dsp_reports_v2 import *  # noqa: F403
except ImportError:
    pass


class DspReportsV2Client(BaseAdsClient):
    """Auto-generated from DSP_Reports_v2_openapi.yaml (2 operations)"""

    async def create_report_v2(self, body: CreateReportRequestBodyV2 | dict[str, Any] | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /dsp/reports

        Creates a report request.
        """
        endpoint = "/dsp/reports"
        params: dict[str, Any] = {}
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspcreatereports.v2_2+json")

    async def get_campaign_report_v2(self, report_id: str, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /dsp/reports/{reportId}

        Gets the metadata of a report previously requested.
        """
        endpoint = f"/dsp/reports/{report_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

