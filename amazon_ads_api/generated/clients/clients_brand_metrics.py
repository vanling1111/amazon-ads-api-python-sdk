"""Auto-generated async API client. Do not edit manually.

Source: BrandMetrics_prod_3p.json
Title:  Brand Metrics
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_brand_metrics import *  # noqa: F403
except ImportError:
    pass


class BrandMetricsClient(BaseAdsClient):
    """Auto-generated from BrandMetrics_prod_3p.json (2 operations)"""

    async def generate_brand_metrics_report(self, body: brandMetricsGenerateReportRequest | dict[str, Any] | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /insights/brandMetrics/report

        Generate Brand Metrics Report. Each response record will include the following dimensional fields (in addition to the re
        """
        endpoint = "/insights/brandMetrics/report"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.insightsbrandmetrics.v1+json")

    async def get_brand_metrics_report(self, report_id: str, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /insights/brandMetrics/report/{reportId}

        Retrieve the status and the URL of the Brand Metrics Report being generated
        """
        endpoint = f"/insights/brandMetrics/report/{report_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

