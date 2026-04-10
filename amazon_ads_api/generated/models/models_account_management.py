"""Auto-generated Pydantic models. Do not edit manually.

Source: AccountManagement_prod_3p.json
Title:  Account Management
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class Attribute(BaseModel):
    value: Optional[str] = None
    key: Optional[str] = None

    model_config = {'populate_by_name': True}


class Property(BaseModel):
    """Additional account attributes represented as generic objects."""
    namespace: str = Field(..., description="Identifies the the group the property belongs to.")
    name: str = Field(..., description="Name of the account property")
    attributes: Optional[list["Attribute"]] = None
    value: str = Field(..., description="Value of the account property.")

    model_config = {'populate_by_name': True}


class SellingBusinessIdentifier(BaseModel):
    type_: str = Field(..., alias="type")
    value: Optional[str] = None

    model_config = {'populate_by_name': True}


class Status(StrEnum):
    PENDING = "PENDING"
    PARTIALLY_CREATED = "PARTIALLY_CREATED"
    CREATED = "CREATED"
    DISABLED = "DISABLED"


class Account(BaseModel):
    """A construct that represents a single advertiser."""
    account_id: Optional[str] = Field(None, alias="accountId", description="This is the global advertising account Id from the client.")
    selling_business_identifiers: Optional[list["SellingBusinessIdentifier"]] = Field(None, alias="sellingBusinessIdentifiers")
    status_reason: Optional[str] = Field(None, alias="statusReason", description="A human-readable description of the global advertising account status.")
    name: Optional[str] = Field(None, description="The name of the global advertising account.")
    properties: Optional[list["Property"]] = None
    status: Optional["Status"] = None

    model_config = {'populate_by_name': True}


class Error(BaseModel):
    """Error structure is to describe the various errors consist of error id, error code, and a readable error message"""
    error_message: Optional[str] = Field(None, alias="errorMessage")
    error_code: Optional[str] = Field(None, alias="errorCode")
    error_id: Optional[float] = Field(None, alias="errorId")

    model_config = {'populate_by_name': True}


class CountryCodeToErrorListMap(BaseModel):
    __root__: dict[str, list["Error"]] = {}


class AlternateId(BaseModel):
    """A construct that represents alternate Id an Ads Account could have, such profile Id"""
    profile_id: Optional[float] = Field(None, alias="profileId", description="The Profile Id of the advertising account")
    country_code: Optional[str] = Field(None, alias="countryCode", description="The country code of the advertising account")
    entity_id: Optional[str] = Field(None, alias="entityId", description="The entity id of the advertising account")

    model_config = {'populate_by_name': True}


class AdsAccountWithMetaData(BaseModel):
    """Ads Account structure response consists of the GlobalAccountID (advertisingAccountId) and other account metadata."""
    country_codes: Optional[list[str]] = Field(None, alias="countryCodes", description="Amazon Ads is available in many but not all countries where Amazon sells goods. For vendors, Global accounts come stock ")
    alternate_ids: Optional[list["AlternateId"]] = Field(None, alias="alternateIds")
    account_name: Optional[str] = Field(None, alias="accountName")
    ads_account_id: str = Field(..., alias="adsAccountId", description="This is the global advertising account Id from the client.")
    errors: Optional["CountryCodeToErrorListMap"] = None
    status: Optional["Status"] = None

    model_config = {'populate_by_name': True}


class GetAccountResponseContent(BaseModel):
    ads_account: Optional["AdsAccountWithMetaData"] = Field(None, alias="adsAccount")

    model_config = {'populate_by_name': True}


class DeleteAccountPropertyResponseContent(BaseModel):
    account: Optional["Account"] = None

    model_config = {'populate_by_name': True}


class V2RateExceededExceptionResponseContent(BaseModel):
    """Maximum sending rate exceeded."""
    errors: Optional[list["Error"]] = None

    model_config = {'populate_by_name': True}


class InternalInvalidInputExceptionResponseContent(BaseModel):
    """Request failed because invalid parameters were provided. Ensure that all required parameters are provided."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class InternalServerExceptionResponseContent(BaseModel):
    """Unexpected error during processing of request."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class AccessDeniedExceptionResponseContent(BaseModel):
    """User does not have sufficient access to perform this action."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class ListAdsAccountsRequestContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="The token is used to fetch the next page of results if they exist.")
    max_results: Optional[float] = Field(None, alias="maxResults")

    model_config = {'populate_by_name': True}


class CreateAccountPropertyResponseContent(BaseModel):
    account: Optional["Account"] = None

    model_config = {'populate_by_name': True}


class DependencyExceptionResponseContent(BaseModel):
    """A dependency service failed."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class StaleUpdateExceptionResponseContent(BaseModel):
    """The account was modified elsewhere. This is a retryable error"""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class InvalidInputExceptionResponseContent(BaseModel):
    """Request failed because invalid parameters were provided. Ensure that all required parameters are provided."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class UpdateAccountPropertyRequestContent(BaseModel):
    property_attributes: Optional[list["Attribute"]] = Field(None, alias="propertyAttributes")
    property_value: str = Field(..., alias="propertyValue", description="Value of the account property.")

    model_config = {'populate_by_name': True}


class GetAccountsByAttributeRequestContent(BaseModel):
    attribute_value: str = Field(..., alias="attributeValue", description="A value by which you can filter accounts.")
    next_token: Optional[str] = Field(None, alias="nextToken")
    max_results: Optional[float] = Field(None, alias="maxResults")
    namespace_filter: str = Field(..., alias="namespaceFilter", description="Identifies the group the filter attribute belongs to.")
    attribute_filter: str = Field(..., alias="attributeFilter", description="Name of the attribute to filter on.")

    model_config = {'populate_by_name': True}


class GetAccountsByAttributeResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken")
    account_ids: list[str] = Field(..., alias="accountIds")

    model_config = {'populate_by_name': True}


class RateExceededExceptionResponseContent(BaseModel):
    """Maximum sending rate exceeded."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class ListAdsAccountsResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken")
    ads_accounts: Optional[list["AdsAccountWithMetaData"]] = Field(None, alias="adsAccounts")

    model_config = {'populate_by_name': True}


class UpdateAccountPropertyResponseContent(BaseModel):
    account: Optional["Account"] = None

    model_config = {'populate_by_name': True}


class CreateAccountPropertyRequestContent(BaseModel):
    property_attributes: Optional[list["Attribute"]] = Field(None, alias="propertyAttributes")
    property_value: str = Field(..., alias="propertyValue", description="Value of the account property.")

    model_config = {'populate_by_name': True}


class V2AccessDeniedExceptionResponseContent(BaseModel):
    """User does not have sufficient access to perform this action."""
    errors: Optional[list["Error"]] = None

    model_config = {'populate_by_name': True}


class V2InternalServerExceptionResponseContent(BaseModel):
    """Unexpected error during processing of request."""
    errors: Optional[list["Error"]] = None

    model_config = {'populate_by_name': True}


class V2InvalidInputExceptionResponseContent(BaseModel):
    """Request failed because invalid parameters were provided. Ensure that all required parameters are provided."""
    errors: Optional[list["Error"]] = None

    model_config = {'populate_by_name': True}


class AdvertisingAccountNotFoundExceptionResponseContent(BaseModel):
    """Advertising Account not found."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}

