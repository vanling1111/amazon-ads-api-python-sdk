"""Auto-generated Pydantic models. Do not edit manually.

Source: ManagerAccount_prod_3p.json
Title:  Manager Account
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class AccountType(StrEnum):
    DSP_ADVERTISING_ACCOUNT = "DSP_ADVERTISING_ACCOUNT"
    MARKETING_CLOUD = "MARKETING_CLOUD"
    SELLER = "SELLER"
    VENDOR = "VENDOR"


class Account(BaseModel):
    """Object representation of an Amazon Advertising account."""
    account_id: Optional[str] = Field(None, alias="accountId", description="Id of the Amazon Advertising account.")
    account_name: Optional[str] = Field(None, alias="accountName", description="The name given to the Amazon Advertising account.")
    account_type: Optional["AccountType"] = Field(None, alias="accountType")
    dsp_advertiser_id: Optional[str] = Field(None, alias="dspAdvertiserId", description="The identifier of a DSP advertiser. Note that this value is only populated for accounts with type `DSP_ADVERTISING_ACCOU")
    marketplace_id: Optional[str] = Field(None, alias="marketplaceId", description="The identifier of the marketplace to which the account is associated. See [this table](https://docs.developer.amazonserv")
    profile_id: Optional[str] = Field(None, alias="profileId", description="The identifier of a profile associated with the advertiser account. Note that this value is only populated for a subset ")

    model_config = {'populate_by_name': True}


class AccountRelationshipRole(StrEnum):
    ENTITY_OWNER = "ENTITY_OWNER"
    ENTITY_USER = "ENTITY_USER"
    ENTITY_VIEWER = "ENTITY_VIEWER"
    SELLER_USER = "SELLER_USER"


class AccountToUpdateType(StrEnum):
    ACCOUNT_ID = "ACCOUNT_ID"
    DSP_ADVERTISER_ID = "DSP_ADVERTISER_ID"


class AccountToUpdate(BaseModel):
    """String identifier for an Amazon Advertising account or advertiser. `ACCOUNT_ID` is an identifier that is returned by the [Profiles resource](https://advertising.amazon.com/API/docs/en-us/reference/2/p"""
    id_: Optional[str] = Field(None, alias="id", description="Id of the Amazon Advertising account.")
    roles: Optional[list["AccountRelationshipRole"]] = Field(None, description="The types of role that will exist with the Amazon Advertising account. Depending on account type, the default role will ")
    type_: Optional[AccountToUpdateType] = Field(None, alias="type", description="The type of the Id")

    model_config = {'populate_by_name': True}


class ErrorDetailCode(StrEnum):
    BAD_REQUEST = "BAD_REQUEST"
    FORBIDDEN = "FORBIDDEN"
    INTERNAL_SERVICE_ERROR = "INTERNAL_SERVICE_ERROR"
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"
    UNAUTHORIZED = "UNAUTHORIZED"


class ErrorDetail(BaseModel):
    """The error response object."""
    code: Optional[ErrorDetailCode] = None
    message: Optional[str] = Field(None, description="A human-readable description of the error.")

    model_config = {'populate_by_name': True}


class AccountToUpdateFailure(BaseModel):
    """Object representation of an Amazon Advertising account or [DSP advertiser](https://advertising.amazon.com/API/docs/en-us/dsp-advertiser/#/) that failed to update."""
    account: Optional["AccountToUpdate"] = None
    error: Optional["ErrorDetail"] = None

    model_config = {'populate_by_name': True}


class CreateManagerAccountRequestManageraccounttype(StrEnum):
    ADVERTISER = "Advertiser"
    AGENCY = "Agency"


class CreateManagerAccountRequest(BaseModel):
    """Request object that defines the fields required to create a Manager account."""
    manager_account_name: Optional[str] = Field(None, alias="managerAccountName", description="Name of the Manager account.")
    manager_account_type: Optional[CreateManagerAccountRequestManageraccounttype] = Field(None, alias="managerAccountType", description="Type of the Manager account, which indicates how the Manager account will be used. Use `Advertiser` if the Manager accou")

    model_config = {'populate_by_name': True}


class ManagerAccount(BaseModel):
    """Object representation of an Amazon Advertising Manager Account."""
    linked_accounts: Optional[list["Account"]] = Field(None, alias="linkedAccounts")
    manager_account_id: Optional[str] = Field(None, alias="managerAccountId", description="Id of the Manager Account.")
    manager_account_name: Optional[str] = Field(None, alias="managerAccountName", description="The name given to a Manager Account.")

    model_config = {'populate_by_name': True}


class GetManagerAccountsResponse(BaseModel):
    """Response containing a list of Manager Accounts that a given user has access to."""
    manager_accounts: Optional[list["ManagerAccount"]] = Field(None, alias="managerAccounts", description="List of Manager Accounts that the user has access to")

    model_config = {'populate_by_name': True}


class UpdateAdvertisingAccountsInManagerAccountRequest(BaseModel):
    """A list of Advertising accounts or advertisers to link/unlink with [Manager Account](https://advertising.amazon.com/help?ref_=a20m_us_blog_whtsnewfb2020_040120#GU3YDB26FR7XT3C8). User can pass a list w"""
    accounts: Optional[list["AccountToUpdate"]] = Field(None, description="List of Advertising accounts or advertisers to link/unlink with [Manager Account](https://advertising.amazon.com/help?re")

    model_config = {'populate_by_name': True}


class UpdateAdvertisingAccountsInManagerAccountResponse(BaseModel):
    """Link/Unlink Advertising account or advertiser Response"""
    failed_accounts: Optional[list["AccountToUpdateFailure"]] = Field(None, alias="failedAccounts", description="List of Advertising accounts or advertisers failed to Link/Unlink with [Manager Account](https://advertising.amazon.com/")
    succeed_accounts: Optional[list["AccountToUpdate"]] = Field(None, alias="succeedAccounts", description="List of Advertising accounts or advertisers successfully Link/Unlink with [Manager Account](https://advertising.amazon.c")

    model_config = {'populate_by_name': True}

