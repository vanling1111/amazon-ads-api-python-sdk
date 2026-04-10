"""Auto-generated async API client. Do not edit manually.

Source: ManagerAccount_prod_3p.json
Title:  Manager Account
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_manager_accounts import *  # noqa: F403
except ImportError:
    pass


class ManagerAccountsClient(BaseAdsClient):
    """Auto-generated from ManagerAccount_prod_3p.json (4 operations)"""

    async def get_manager_accounts_for_user(self, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /managerAccounts

        Returns all Manager accounts that a given Amazon Advertising user has access to.
        """
        endpoint = "/managerAccounts"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

    async def create_manager_account(self, body: CreateManagerAccountRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /managerAccounts

        Creates a new Amazon Advertising Manager account.
        """
        endpoint = "/managerAccounts"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.createmanageraccountrequest.v1+json")

    async def link_advertising_accounts_to_manager_account_public_api(self, manager_account_id: str, body: UpdateAdvertisingAccountsInManagerAccountRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /managerAccounts/{managerAccountId}/associate

        Link Amazon Advertising accounts or advertisers with a Manager Account.
        """
        endpoint = f"/managerAccounts/{manager_account_id}/associate"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.updateadvertisingaccountsinmanageraccountrequest.v1+json")

    async def unlink_advertising_accounts_to_manager_account_public_api(self, manager_account_id: str, body: UpdateAdvertisingAccountsInManagerAccountRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /managerAccounts/{managerAccountId}/disassociate

        Unlink Amazon Advertising accounts or advertisers with a Manager Account.
        """
        endpoint = f"/managerAccounts/{manager_account_id}/disassociate"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.updateadvertisingaccountsinmanageraccountrequest.v1+json")

