"""Auto-generated async API client. Do not edit manually.

Source: AccountManagement_prod_3p.json
Title:  Account Management
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_account_management import *  # noqa: F403
except ImportError:
    pass


class AccountManagementClient(BaseAdsClient):
    """Auto-generated from AccountManagement_prod_3p.json (6 operations)"""

    async def get_account(self, advertising_account_id: str) -> JSONData | JSONList:
        """GET /adsAccounts/{advertisingAccountId}

        Request attributes of a given global advertising account.
        """
        endpoint = f"/adsAccounts/{advertising_account_id}"
        return await self.get(endpoint)

    async def create_account_property(self, advertising_account_id: str, property_namespace: str, property_name: str, body: CreateAccountPropertyRequestContent | dict[str, Any] | None = None) -> JSONData | JSONList:
        """POST /advertisingAccounts/{advertisingAccountId}/propertyNamespaces/{propertyNamespace}/properties/{propertyName}

        Add a new Account Property to the requested account.
        """
        endpoint = f"/advertisingAccounts/{advertising_account_id}/propertyNamespaces/{property_namespace}/properties/{property_name}"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, content_type="application/vnd.GlobalAccountManagementService.ManagePropertyResource.v1.0+json")

    async def delete_account_property(self, advertising_account_id: str, property_namespace: str, property_name: str, property_value: str | None = None) -> JSONData | JSONList:
        """DELETE /advertisingAccounts/{advertisingAccountId}/propertyNamespaces/{propertyNamespace}/properties/{propertyName}

        Removes an Account Property from the requested account.
        """
        endpoint = f"/advertisingAccounts/{advertising_account_id}/propertyNamespaces/{property_namespace}/properties/{property_name}"
        params: dict[str, Any] = {}
        if property_value is not None:
            params["propertyValue"] = property_value
        return await self.delete(endpoint, params=params)

    async def update_account_property(self, advertising_account_id: str, property_namespace: str, property_name: str, body: UpdateAccountPropertyRequestContent | dict[str, Any] | None = None) -> JSONData | JSONList:
        """PUT /advertisingAccounts/{advertisingAccountId}/propertyNamespaces/{propertyNamespace}/properties/{propertyName}

        Update an existing Account Property for the requested account.
        """
        endpoint = f"/advertisingAccounts/{advertising_account_id}/propertyNamespaces/{property_namespace}/properties/{property_name}"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, content_type="application/vnd.GlobalAccountManagementService.ManagePropertyResource.v1.0+json")

    async def get_accounts_by_attribute(self, body: GetAccountsByAttributeRequestContent | dict[str, Any] | None = None) -> JSONData | JSONList:
        """POST /advertisingAccountsByAttributes

        Get global advertising accounts by attribute.
        """
        endpoint = "/advertisingAccountsByAttributes"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, content_type="application/vnd.GlobalAccountManagementService.ManageAccountResource.v1.0+json")

    async def list_ads_accounts(self, body: ListAdsAccountsRequestContent | dict[str, Any] | None = None) -> JSONData | JSONList:
        """POST /adsAccounts/list

        Request list of advertising accounts given principalId.
        """
        endpoint = "/adsAccounts/list"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, content_type="application/vnd.listaccountsresource.v1+json")

