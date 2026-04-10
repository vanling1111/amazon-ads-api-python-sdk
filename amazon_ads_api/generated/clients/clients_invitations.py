"""Auto-generated async API client. Do not edit manually.

Source: AdvertisingInvitations_prod_3p.json
Title:  Advertising Invitations
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_invitations import *  # noqa: F403
except ImportError:
    pass


class InvitationsClient(BaseAdsClient):
    """Auto-generated from AdvertisingInvitations_prod_3p.json (5 operations)"""

    async def create_user_invitations(self, body: CreateUserInvitationsRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /user-invitations

        **Authorized resource type**: Global Ad Account ID, Profile ID  **Parameter name**: Amazon-Ads-AccountId  **Parameter in
        """
        endpoint = "/user-invitations"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-ManagerAccountId"] = amazon_ads_manager_account_id
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.CreateUserInvitations.v1+json")

    async def update_user_invitations(self, body: UpdateUserInvitationsRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /user-invitations

        **Authorized resource type**: Global Ad Account ID, Profile ID  **Parameter name**: Amazon-Ads-AccountId  **Parameter in
        """
        endpoint = "/user-invitations"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-ManagerAccountId"] = amazon_ads_manager_account_id
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.UpdateUserInvitations.v1+json")

    async def list_user_invitations(self, body: ListUserInvitationsRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /user-invitations/list

        **Authorized resource type**: Global Ad Account ID, Profile ID  **Parameter name**: Amazon-Ads-AccountId  **Parameter in
        """
        endpoint = "/user-invitations/list"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-ManagerAccountId"] = amazon_ads_manager_account_id
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.ListUserInvitations.v1+json")

    async def redeem_user_invitation(self, body: RedeemUserInvitationRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """PUT /user-invitations/redeem

        **Requires one of these permissions**: []
        """
        endpoint = "/user-invitations/redeem"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.RedeemUserInvitation.v1+json")

    async def get_user_invitation(self, invitation_id: str, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /user-invitations/{invitationId}

        **Requires one of these permissions**: []
        """
        endpoint = f"/user-invitations/{invitation_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

