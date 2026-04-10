"""Auto-generated Pydantic models. Do not edit manually.

Source: AdvertisingAccounts_prod_3p.json
Title:  Advertising Accounts
"""

from __future__ import annotations

from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field



class AccessDeniedExceptionResponseContent(BaseModel):
    """User does not have sufficient access to perform this action."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class Status(StrEnum):
    CREATED = "CREATED"
    DISABLED = "DISABLED"
    PARTIALLY_CREATED = "PARTIALLY_CREATED"
    PENDING = "PENDING"


class AdsAccount(BaseModel):
    """Ads Account structure response consists of the GlobalAccountID (advertisingAccountId) and other account metadata."""
    account_name: Optional[str] = Field(None, alias="accountName")
    ads_account_id: str = Field(..., alias="adsAccountId", description="This is the global advertising account Id from the client.")
    status: Optional["Status"] = None

    model_config = {'populate_by_name': True}


class Error(BaseModel):
    """Error structure is to describe the various errors consist of error id, error code, and a readable error message"""
    error_code: Optional[str] = Field(None, alias="errorCode")
    error_id: Optional[float] = Field(None, alias="errorId")
    error_message: Optional[str] = Field(None, alias="errorMessage")

    model_config = {'populate_by_name': True}


class CountryCodeToErrorListMap(BaseModel):
    __root__: dict[str, list["Error"]] = {}


class AlternateId(BaseModel):
    """A construct that represents alternate Id an Ads Account could have, such profile Id"""
    country_code: Optional[str] = Field(None, alias="countryCode", description="The country code of the advertising account")
    entity_id: Optional[str] = Field(None, alias="entityId", description="The entity id of the advertising account")
    profile_id: Optional[float] = Field(None, alias="profileId", description="The Profile Id of the advertising account")

    model_config = {'populate_by_name': True}


class AdsAccountWithMetaData(BaseModel):
    """Ads Account structure response consists of the GlobalAccountID (advertisingAccountId) and other account metadata."""
    account_name: Optional[str] = Field(None, alias="accountName")
    ads_account_id: str = Field(..., alias="adsAccountId", description="This is the global advertising account Id from the client.")
    alternate_ids: Optional[list["AlternateId"]] = Field(None, alias="alternateIds")
    country_codes: Optional[list[str]] = Field(None, alias="countryCodes", description="Amazon Ads is available in many but not all countries where Amazon sells goods. For vendors, Global accounts come stock ")
    errors: Optional["CountryCodeToErrorListMap"] = None
    status: Optional["Status"] = None

    model_config = {'populate_by_name': True}


class AdvertisingAccountNotFoundExceptionResponseContent(BaseModel):
    """Advertising Account not found."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class AmazonAuthor(BaseModel):
    """Represent an Amazon Author."""
    email: Optional[str] = Field(None, description="The email address of the KDP or Author Central account")

    model_config = {'populate_by_name': True}


class AmazonSeller(BaseModel):
    """Represent an Amazon Seller."""
    seller_central_account: Optional[str] = Field(None, alias="sellerCentralAccount", description="The merchant customer id of the seller central account")

    model_config = {'populate_by_name': True}


class AmazonVendor(BaseModel):
    """Represent an Amazon Vendor."""
    vendor_group: Optional[str] = Field(None, alias="vendorGroup", description="The vendor group id of the vendor")

    model_config = {'populate_by_name': True}


class Business(BaseModel):
    """Represent a business who does not sell on Amazon. These fields are containing information about the client's business and will be used for business verification."""
    address_line1: Optional[str] = Field(None, alias="addressLine1", description="Address line 1 of the business")
    address_line2: Optional[str] = Field(None, alias="addressLine2", description="Address line 2 of the business.")
    city: Optional[str] = Field(None, description="The city of the business.")
    country_code: Optional[str] = Field(None, alias="countryCode", description="Country code of the business.")
    name: Optional[str] = Field(None, description="The name of the business.")
    phone: Optional[str] = Field(None, description="The phone number of the business.")
    state: Optional[str] = Field(None, description="The state of the business.")
    website_url: Optional[str] = Field(None, alias="websiteUrl", description="The website url of the business.")
    zip_code: Optional[str] = Field(None, alias="zipCode", description="Zip code of the business.")

    model_config = {'populate_by_name': True}


class Association(BaseModel):
    """Association can represent an Amazon Vendor, Seller or business who does not sell on Amazon"""
    amazon_author: Optional["AmazonAuthor"] = Field(None, alias="amazonAuthor")
    amazon_seller: Optional["AmazonSeller"] = Field(None, alias="amazonSeller")
    amazon_vendor: Optional["AmazonVendor"] = Field(None, alias="amazonVendor")
    business: Optional["Business"] = None

    model_config = {'populate_by_name': True}


class TermsType(StrEnum):
    ADSP = "ADSP"
    ADVERTISING = "ADVERTISING"
    MARKETING_CLOUD = "MARKETING_CLOUD"
    PARTNER_NETWORK = "PARTNER_NETWORK"


class CreateTermsTokenRequestContent(BaseModel):
    account_id: Optional[str] = Field(None, alias="accountId", description="Optional account ID (Global Account or Manager Account) for accepting terms on existing accounts")
    terms_type: Optional["TermsType"] = Field(None, alias="termsType")

    model_config = {'populate_by_name': True}


class CreateTermsTokenResponseContent(BaseModel):
    terms_token: str = Field(..., alias="termsToken", description="A Terms Token refers to an UUID token used for terms and conditions acceptance")
    terms_url: str = Field(..., alias="termsUrl", description="The link to advertising terms page where the advertiser can view and accept.")

    model_config = {'populate_by_name': True}


class GetAccountResponseContent(BaseModel):
    ads_account: Optional["AdsAccountWithMetaData"] = Field(None, alias="adsAccount")

    model_config = {'populate_by_name': True}


class TermsTokenStatus(StrEnum):
    ACCEPTED = "ACCEPTED"
    CREATED = "CREATED"
    REDEEMED = "REDEEMED"


class GetTermsTokenResponseContent(BaseModel):
    terms_token_status: "TermsTokenStatus" = Field(..., alias="termsTokenStatus")
    terms_type: Optional["TermsType"] = Field(None, alias="termsType")

    model_config = {'populate_by_name': True}


class InternalServerExceptionResponseContent(BaseModel):
    """Unexpected error during processing of request."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class InvalidInputExceptionResponseContent(BaseModel):
    """Request failed because invalid parameters were provided. Ensure that all required parameters are provided."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class ListAdsAccountsRequestContent(BaseModel):
    max_results: Optional[float] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken", description="The token is used to fetch the next page of results if they exist.")

    model_config = {'populate_by_name': True}


class ListAdsAccountsResponseContent(BaseModel):
    ads_accounts: Optional[list["AdsAccountWithMetaData"]] = Field(None, alias="adsAccounts")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class RateExceededExceptionResponseContent(BaseModel):
    """Maximum sending rate exceeded."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class RegisterAdsAccountRequestContent(BaseModel):
    account_name: Optional[str] = Field(None, alias="accountName", description="Account names are typically the name of the company or brand being advertised. We recommend that you avoid using persona")
    associations: Optional[list["Association"]] = Field(None, description="Associations you would like to link to this advertising account, could be Amazon Vendor, Seller, or just a regular busin")
    country_codes: Optional[list[str]] = Field(None, alias="countryCodes", description="The countries that you want this account to operate in.")
    terms_token: Optional[str] = Field(None, alias="termsToken", description="We recommend you do not provide this field since we can determine if the customer has accepted the terms for you. An obf")

    model_config = {'populate_by_name': True}


class RegisterAdsAccountResponseContent(BaseModel):
    ads_account: Optional["AdsAccount"] = Field(None, alias="adsAccount")

    model_config = {'populate_by_name': True}


class V2AccessDeniedExceptionResponseContent(BaseModel):
    """User does not have sufficient access to perform this action."""
    errors: Optional[list["Error"]] = None

    model_config = {'populate_by_name': True}


class V2InternalInvalidInputExceptionResponseContent(BaseModel):
    """Request failed because invalid parameters were provided. Ensure that all required parameters are provided."""
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


class V2RateExceededExceptionResponseContent(BaseModel):
    """Maximum sending rate exceeded."""
    errors: Optional[list["Error"]] = None

    model_config = {'populate_by_name': True}

