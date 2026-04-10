"""Auto-generated Pydantic models. Do not edit manually.

Source: Eligibility_prod_3p.json
Title:  Eligibility
"""

from __future__ import annotations

from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field



class AcceptLanguage(StrEnum):
    AR_AE = "ar-AE"
    DE_DE = "de-DE"
    EN_AU = "en-AU"
    EN_CA = "en-CA"
    EN_GB = "en-GB"
    EN_IN = "en-IN"
    EN_US = "en-US"
    ES_ES = "es-ES"
    ES_MX = "es-MX"
    ES_US = "es-US"
    FR_CA = "fr-CA"
    FR_FR = "fr-FR"
    IT_IT = "it-IT"
    JA_JP = "ja-JP"
    KO_KR = "ko-KR"
    NL_NL = "nl-NL"
    PL_PL = "pl-PL"
    PT_BR = "pt-BR"
    TR_TR = "tr-TR"
    ZH_CN = "zh-CN"


class AdProgram(StrEnum):
    DTC = "DTC"
    MAAS = "MAAS"
    SB = "SB"
    SD = "SD"
    SPOT = "SPOT"


class BadRequestExceptionResponseContent(BaseModel):
    code: Optional[float] = Field(None, description="Programmatic status code.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class Check(BaseModel):
    """A union of all the checks that we would want to skip"""
    pass


class EligibilityStatusName(StrEnum):
    ADULT_PRODUCT = "ADULT_PRODUCT"
    CLOSED_CATEGORY = "CLOSED_CATEGORY"
    INELIGIBLE_CONDITION = "INELIGIBLE_CONDITION"
    INELIGIBLE_OFFER = "INELIGIBLE_OFFER"
    INELIGIBLE_PRODUCT_COST = "INELIGIBLE_PRODUCT_COST"
    LISTING_SUPRESSED = "LISTING_SUPRESSED"
    MISSING_IMAGE = "MISSING_IMAGE"
    MISSING_TITLE = "MISSING_TITLE"
    NOT_IN_BUYBOX = "NOT_IN_BUYBOX"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    RESTRICTED_CATEGORY = "RESTRICTED_CATEGORY"
    VARIATION_PARENT = "VARIATION_PARENT"


class EligibilityStatusSeverity(StrEnum):
    ELIGIBLE_WITH_WARNING = "ELIGIBLE_WITH_WARNING"
    INELIGIBLE = "INELIGIBLE"


class EligibilityStatus(BaseModel):
    """The advertising eligibility status of a product."""
    help_url: Optional[str] = Field(None, alias="helpUrl", description="A URL with additional information about the status identifier. May not be present for all status identifiers.")
    message: Optional[str] = Field(None, description="A human-readable description of the status identifier specified in the `name` field.")
    name: Optional[EligibilityStatusName] = Field(None, description="The status identifier.")
    severity: Optional[EligibilityStatusSeverity] = Field(None, description="An enumerated advertising eligibility severity status. If set to `INELIGIBLE`, the product cannot be included in an adve")

    model_config = {'populate_by_name': True}


class ReasonCode(StrEnum):
    ACCOUNT_SUSPENDED = "ACCOUNT_SUSPENDED"
    ADS_TERMS_NOT_ACCEPTED = "ADS_TERMS_NOT_ACCEPTED"
    ADVERTISER_TYPE_NOT_SUPPORTED = "ADVERTISER_TYPE_NOT_SUPPORTED"
    ADVERTISING_ACCOUNT_NOT_FOUND = "ADVERTISING_ACCOUNT_NOT_FOUND"
    AMAZON_BUSINESS_EXCLUSIVE_CAMPAIGN_NOT_ELIGIBLE = "AMAZON_BUSINESS_EXCLUSIVE_CAMPAIGN_NOT_ELIGIBLE"
    AMAZON_HAUL_EXCLUSIVE_CAMPAIGN_NOT_ELIGIBLE = "AMAZON_HAUL_EXCLUSIVE_CAMPAIGN_NOT_ELIGIBLE"
    AMAZON_MARKETING_CLOUD_ON_DEMAND_NOT_ELIGIBLE = "AMAZON_MARKETING_CLOUD_ON_DEMAND_NOT_ELIGIBLE"
    AUTONOMOUS_CAMPAIGNS_FEATURE_NOT_ELIGIBLE = "AUTONOMOUS_CAMPAIGNS_FEATURE_NOT_ELIGIBLE"
    BILLING_ACCOUNT_NOT_FOUND = "BILLING_ACCOUNT_NOT_FOUND"
    BLOCKED = "BLOCKED"
    BUSINESS_NOT_VERIFIED = "BUSINESS_NOT_VERIFIED"
    BUSINESS_THRESHOLDS_NOT_MET = "BUSINESS_THRESHOLDS_NOT_MET"
    DIRECT_TO_CONSUMER_OWNER_TAG_ID_NOT_FOUND = "DIRECT_TO_CONSUMER_OWNER_TAG_ID_NOT_FOUND"
    DIRECT_TO_CONSUMER_SUBSCRIPTION_NOT_FOUND = "DIRECT_TO_CONSUMER_SUBSCRIPTION_NOT_FOUND"
    DSP_NOT_REQUESTED = "DSP_NOT_REQUESTED"
    DSP_PENDING_SETUP = "DSP_PENDING_SETUP"
    DSP_REQUEST_PENDING = "DSP_REQUEST_PENDING"
    DSP_REQUEST_REJECTED = "DSP_REQUEST_REJECTED"
    DYNAMIC_PRODUCT_SETS_CAMPAIGN_FEATURE_NOT_ELIGIBLE = "DYNAMIC_PRODUCT_SETS_CAMPAIGN_FEATURE_NOT_ELIGIBLE"
    EXPIRED_PAYMENT_METHOD = "EXPIRED_PAYMENT_METHOD"
    GEO_GATED_CAMPAIGN_FEATURE_NOT_ELIGIBLE = "GEO_GATED_CAMPAIGN_FEATURE_NOT_ELIGIBLE"
    GLOBAL_ACCOUNT_ALREADY_EXISTS = "GLOBAL_ACCOUNT_ALREADY_EXISTS"
    GLOBAL_AUTO_SCALING_CAMPAIGNS_NOT_ELIGIBLE = "GLOBAL_AUTO_SCALING_CAMPAIGNS_NOT_ELIGIBLE"
    GLOBAL_CAMPAIGNS_NOT_ELIGIBLE = "GLOBAL_CAMPAIGNS_NOT_ELIGIBLE"
    MTA_NOT_ELIGIBLE = "MTA_NOT_ELIGIBLE"
    NOT_BRAND_REPRESENTATIVE = "NOT_BRAND_REPRESENTATIVE"
    NOT_LAUNCHED_IN_MARKETPLACE = "NOT_LAUNCHED_IN_MARKETPLACE"
    NOT_SETUP_FOR_DSP = "NOT_SETUP_FOR_DSP"
    NO_BRAND_RELATIONS = "NO_BRAND_RELATIONS"
    NO_TACTIC_ENABLED = "NO_TACTIC_ENABLED"
    PAYMENT_METHOD_NOT_FOUND = "PAYMENT_METHOD_NOT_FOUND"
    PAYMENT_METHOD_NOT_VALID = "PAYMENT_METHOD_NOT_VALID"
    PAYMENT_PROFILE_NOT_FOUND = "PAYMENT_PROFILE_NOT_FOUND"
    PREPAY_BALANCE_TOO_LOW = "PREPAY_BALANCE_TOO_LOW"
    RO_BALANCE_TOO_LOW = "RO_BALANCE_TOO_LOW"
    STOCK_FILTER_CAMPAIGN_FEATURE_NOT_ELIGIBLE = "STOCK_FILTER_CAMPAIGN_FEATURE_NOT_ELIGIBLE"
    SUBSCRIPTION_NOT_FOUND = "SUBSCRIPTION_NOT_FOUND"
    TAX_INFO_NOT_COMPLETE = "TAX_INFO_NOT_COMPLETE"
    UNKNOWN = "UNKNOWN"
    VETTING_FAILURE = "VETTING_FAILURE"


class IneligibleLevel(StrEnum):
    INELIGIBLE = "INELIGIBLE"
    INELIGIBLE_WITH_RESOLUTION = "INELIGIBLE_WITH_RESOLUTION"


class ReasonItem(BaseModel):
    code: Optional["ReasonCode"] = None
    description: Optional[str] = Field(None, description="Message explaining what the status means. Example: Payment preference not found for associated billing account. Please a")
    level: Optional["IneligibleLevel"] = None

    model_config = {'populate_by_name': True}


class EligibilityStatusDetail(BaseModel):
    """Describes a single program's eligibility status"""
    eligible: Optional[bool] = Field(None, description="Boolean value where if true, advertiser is eligible to access the given program.")
    reasons: Optional[list["ReasonItem"]] = Field(None, description="String identifier for the status.")

    model_config = {'populate_by_name': True}


class EligibilityStatusDetailV2(BaseModel):
    """Describes a single program's eligibility status"""
    ad_program: Optional["AdProgram"] = Field(None, alias="adProgram")
    eligible: Optional[bool] = Field(None, description="Boolean value where if true, advertiser is eligible to access the given program.")
    reasons: Optional[list["ReasonItem"]] = Field(None, description="String identifier for the status.")

    model_config = {'populate_by_name': True}


class EligibilityStatusMap(BaseModel):
    """This is a map that will be key'd on the ad program (SB/SD/DTC/MAAS/SPOT); the value will be an eligibility object."""
    __root__: dict[str, "EligibilityStatusDetail"] = {}


class GlobalStoreSetting(BaseModel):
    """Fields required to check eligibility for [GlobalStore Program](https://sellercentral.amazon.com/help/hub/reference/external/202139180) Ads."""
    catalog_source_country_code: Optional[str] = Field(None, alias="catalogSourceCountryCode", description="Country code of source marketplace where seller has listed the product. Possible source country codes include US, UK, DE")

    model_config = {'populate_by_name': True}


class InternalServerErrorExceptionResponseContent(BaseModel):
    code: Optional[float] = Field(None, description="Programmatic status code.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class MarketplaceEntitiesEligibilityStatusList(BaseModel):
    eligibility_status_list: Optional[list["EligibilityStatusDetailV2"]] = Field(None, alias="eligibilityStatusList", description="This is a map that will be key'd on the ad program (SB/SD/DTC/MAAS/SPOT); the value will be an eligibility object.")
    marketplace_id: Optional[str] = Field(None, alias="marketplaceId")

    model_config = {'populate_by_name': True}


class NotFoundExceptionResponseContent(BaseModel):
    code: Optional[float] = Field(None, description="Programmatic status code.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class ProductDetails(BaseModel):
    """An Amazon product identifier, seller product identifier, or both."""
    asin: str = Field(..., description="An Amazon product identifier.")
    global_store_setting: Optional["GlobalStoreSetting"] = Field(None, alias="globalStoreSetting")
    sku: Optional[str] = Field(None, description="A seller product identifier.")

    model_config = {'populate_by_name': True}


class ProductEligibilityError(BaseModel):
    """The error response object."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class ProductEligibilityRequestAdtype(StrEnum):
    DSP = "dsp"
    SB = "sb"
    SD = "sd"
    SP = "sp"


class ProductEligibilityRequest(BaseModel):
    """A product advertising eligibility request object."""
    ad_type: Optional[ProductEligibilityRequestAdtype] = Field(None, alias="adType", description="Set to 'sp' to check product eligibility for Sponsored Products advertisements. Set to 'sb' to check product eligibility")
    locale: Optional[str] = Field(None, description="Set locale string as 'en_US' to specify the language in which the response is returned")
    product_details_list: list["ProductDetails"] = Field(..., alias="productDetailsList", description="A list of product identifier objects.")

    model_config = {'populate_by_name': True}


class ProductResponseOverallstatus(StrEnum):
    ELIGIBLE = "ELIGIBLE"
    ELIGIBLE_WITH_WARNING = "ELIGIBLE_WITH_WARNING"
    INELIGIBLE = "INELIGIBLE"


class ProductResponse(BaseModel):
    """An product advertising eligibility response."""
    eligibility_status_list: list["EligibilityStatus"] = Field(..., alias="eligibilityStatusList")
    overall_status: ProductResponseOverallstatus = Field(..., alias="overallStatus", description="A human-readable description of the product's advertising eligibility status. Inherits highest severity from eligibility")
    product_details: "ProductDetails" = Field(..., alias="productDetails")

    model_config = {'populate_by_name': True}


class ProductEligibilityResponse(BaseModel):
    """A product advertising eligibility response object."""
    product_response_list: Optional[list["ProductResponse"]] = Field(None, alias="productResponseList", description="A list of product advertising eligibility responses.")

    model_config = {'populate_by_name': True}


class ProgramEligibilityRequestContent(BaseModel):
    """A request to evaluate account level eligibility for Amazon ad programs (Sponsored Products, Sponsored Brands, Sponsored Display, Stores, DirectToConsumer, Amazon Attribution, etc)."""
    skip_checks: Optional["Check"] = Field(None, alias="skipChecks")

    model_config = {'populate_by_name': True}


class ProgramEligibilityResponseContent(BaseModel):
    """An object of program eligibility responses for an advertiser."""
    eligibility_status_map: Optional["EligibilityStatusMap"] = Field(None, alias="eligibilityStatusMap")

    model_config = {'populate_by_name': True}


class ProgramEligibilityV2RequestContent(BaseModel):
    """A request to evaluate account level eligibility for Amazon ad programs (Sponsored Products, Sponsored Brands, Sponsored Display, Stores, DirectToConsumer, Amazon Attribution, etc)."""
    max_results: Optional[float] = Field(None, alias="maxResults", description="Max results for pagination")
    next_token: Optional[str] = Field(None, alias="nextToken", description="The pagination token that is required to go to the next page")

    model_config = {'populate_by_name': True}


class ProgramEligibilityV2ResponseContent(BaseModel):
    """An object of program eligibility responses for an advertiser."""
    eligibility_status_lists: Optional[list["MarketplaceEntitiesEligibilityStatusList"]] = Field(None, alias="eligibilityStatusLists")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")

    model_config = {'populate_by_name': True}


class RateExceededExceptionResponseContent(BaseModel):
    code: Optional[float] = Field(None, description="Programmatic status code.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class UnauthorizedExceptionResponseContent(BaseModel):
    code: Optional[float] = Field(None, description="Programmatic status code.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}

