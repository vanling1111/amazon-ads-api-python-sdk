"""Auto-generated async API client. Do not edit manually.

Source: Portfolios_prod_3p.json
Title:  Portfolios
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_portfolios import *  # noqa: F403
except ImportError:
    pass


class PortfoliosClient(BaseAdsClient):
    """Auto-generated from Portfolios_prod_3p.json (4 operations)"""

    async def create_portfolios(self, body: CreatePortfoliosRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /portfolios

        **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/portfolios"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spPortfolio.v3+json")

    async def update_portfolios(self, body: UpdatePortfoliosRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """PUT /portfolios

        **Requires one of these permissions**: ['advertiser_campaign_edit']
        """
        endpoint = "/portfolios"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.spPortfolio.v3+json")

    async def portfolio_budget_usage(self, body: BudgetUsagePortfolioRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /portfolios/budget/usage

        Budget usage API for portfolios
        """
        endpoint = "/portfolios/budget/usage"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.portfoliobudgetusage.v1+json")

    async def list_portfolios(self, body: ListPortfoliosRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /portfolios/list

        **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign_view']
        """
        endpoint = "/portfolios/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spPortfolio.v3+json")

