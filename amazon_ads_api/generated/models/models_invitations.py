"""Auto-generated Pydantic models. Do not edit manually.

Source: AdvertisingInvitations_prod_3p.json
Title:  Advertising Invitations
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field



class BadRequestExceptionResponseContent(BaseModel):
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class Country(BaseModel):
    country_code: Optional[str] = Field(None, alias="countryCode")

    model_config = {'populate_by_name': True}


class User(BaseModel):
    email_address: str = Field(..., alias="emailAddress", description="Email address of the user to be invited")
    user_name: str = Field(..., alias="userName", description="Name of the user to be invited")

    model_config = {'populate_by_name': True}


class Role(BaseModel):
    name: Optional[str] = None

    model_config = {'populate_by_name': True}


class Permission(BaseModel):
    name: Optional[str] = None

    model_config = {'populate_by_name': True}


class PermissionSet(BaseModel):
    custom_permission_set: Optional[list["Permission"]] = Field(None, alias="customPermissionSet", description="If type = CUSTOM_PERMISSION_SET, indicates the permissions of the invitation. Different permissions are supported for di")
    role: Optional["Role"] = None
    type_: Optional[str] = Field(None, alias="type", description="Type of permission set. Supported values: ROLE, CUSTOM_PERMISSION_SET")

    model_config = {'populate_by_name': True}


class UserInvitationRequest(BaseModel):
    countries: Optional[list["Country"]] = Field(None, description="List of two-letter ISO 3166 country codes that the user is invited to. Only valid for invitations to global accounts.")
    permission_set: Optional["PermissionSet"] = Field(None, alias="permissionSet")
    user: Optional["User"] = None

    model_config = {'populate_by_name': True}


class CreateUserInvitationsRequestContent(BaseModel):
    notify_invited_users: Optional[bool] = Field(None, alias="notifyInvitedUsers", description="Indicates if an invitation email will be sent to the invited user. This email will direct users to the Amazon Ads Consol")
    user_invitation_requests: list["UserInvitationRequest"] = Field(..., alias="userInvitationRequests", description="List of invitations to be sent to users.")

    model_config = {'populate_by_name': True}


class InvitationError(BaseModel):
    error_code: Optional[str] = Field(None, alias="errorCode")
    error_detail: Optional[str] = Field(None, alias="errorDetail")
    error_message: Optional[str] = Field(None, alias="errorMessage")
    identifier: Optional[str] = None

    model_config = {'populate_by_name': True}


class UserInvitation(BaseModel):
    countries: Optional[list["Country"]] = None
    created_at: Optional[float] = Field(None, alias="createdAt")
    created_by: Optional[str] = Field(None, alias="createdBy")
    expiration: Optional[float] = None
    invitation_id: Optional[str] = Field(None, alias="invitationId")
    permission_set: Optional["PermissionSet"] = Field(None, alias="permissionSet")
    state: Optional[str] = None
    target_id: Optional[str] = Field(None, alias="targetId")
    user: Optional["User"] = None

    model_config = {'populate_by_name': True}


class CreateUserInvitationsResponseContent(BaseModel):
    errors: Optional[list["InvitationError"]] = None
    successes: Optional[list["UserInvitation"]] = None

    model_config = {'populate_by_name': True}


class ForbiddenExceptionResponseContent(BaseModel):
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class GetUserInvitationResponseContent(BaseModel):
    invitation: Optional["UserInvitation"] = None
    terms_types: Optional[list[str]] = Field(None, alias="termsTypes")

    model_config = {'populate_by_name': True}


class InternalServerExceptionResponseContent(BaseModel):
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class ListUserInvitationsRequestContent(BaseModel):
    max_results: Optional[float] = Field(None, alias="maxResults", description="Max results to fetch per page.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Identifier of the next pagination token.")

    model_config = {'populate_by_name': True}


class ListUserInvitationsResponseContent(BaseModel):
    invitations: Optional[list["UserInvitation"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class RedeemUserInvitationRequestContent(BaseModel):
    invitation_id: str = Field(..., alias="invitationId", description="Identifier of the invitation to be redeemed.")

    model_config = {'populate_by_name': True}


class ResourceNotFoundExceptionResponseContent(BaseModel):
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class RetryableServiceExceptionResponseContent(BaseModel):
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class Update(BaseModel):
    invitation_id: str = Field(..., alias="invitationId", description="Identifier of the invitation you want to update.")
    state: str = Field(..., description="State to change your invitation to. Support states: REVOKED, RESENT.")

    model_config = {'populate_by_name': True}


class UpdateUserInvitationsRequestContent(BaseModel):
    notify_invited_users: Optional[bool] = Field(None, alias="notifyInvitedUsers", description="Indicates if an invitation email will be sent to the invited user. This email will direct users to the Amazon Ads Consol")
    updates: list["Update"] = Field(..., description="List of updates to perform for a set of invitations.")

    model_config = {'populate_by_name': True}


class UpdateUserInvitationsResponseContent(BaseModel):
    errors: Optional[list["InvitationError"]] = None
    successes: Optional[list["Update"]] = None

    model_config = {'populate_by_name': True}

