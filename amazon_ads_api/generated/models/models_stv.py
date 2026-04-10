"""Auto-generated Pydantic models. Do not edit manually.

Source: SponsoredTV_prod_3p.json
Title:  Sponsored TV
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class AccessDeniedErrorCode(StrEnum):
    ACCESS_DENIED = "ACCESS_DENIED"


class AccessDeniedExceptionResponseContent(BaseModel):
    code: "AccessDeniedErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class AdServingStatus(StrEnum):
    ACCOUNT_OUT_OF_BUDGET = "ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    AD_ARCHIVED = "AD_ARCHIVED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_POLICING_PENDING_REVIEW = "AD_GROUP_POLICING_PENDING_REVIEW"
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    AD_PAUSED = "AD_PAUSED"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    AD_POLICING_SUSPENDED = "AD_POLICING_SUSPENDED"
    AD_STATUS_ARCHIVED = "AD_STATUS_ARCHIVED"
    AD_STATUS_LIVE = "AD_STATUS_LIVE"
    AD_STATUS_PAUSED = "AD_STATUS_PAUSED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    ENDED = "ENDED"
    INELIGIBLE = "INELIGIBLE"
    MISSING_DECORATION = "MISSING_DECORATION"
    NOT_BUYABLE = "NOT_BUYABLE"
    NOT_IN_BUYBOX = "NOT_IN_BUYBOX"
    NOT_IN_POLICY = "NOT_IN_POLICY"
    OTHER = "OTHER"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    PENDING_START_DATE = "PENDING_START_DATE"
    SECURITY_SCAN_PENDING_REVIEW = "SECURITY_SCAN_PENDING_REVIEW"
    SECURITY_SCAN_REJECTED = "SECURITY_SCAN_REJECTED"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"


class AdExtendedData(BaseModel):
    creation_date: Optional[str] = Field(None, alias="creationDate", description="The date in ISO 8601 format")
    last_update_date: Optional[str] = Field(None, alias="lastUpdateDate", description="The date in ISO 8601 format")
    serving_status: Optional["AdServingStatus"] = Field(None, alias="servingStatus")

    model_config = {'populate_by_name': True}


class EntityState(StrEnum):
    ARCHIVED = "ARCHIVED"
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


class Ad(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the Ad Group associated with the Ad.")
    ad_id: str = Field(..., alias="adId", description="The identifier of the Ad.")
    ad_name: Optional[str] = Field(None, alias="adName", description="The name of the Ad.")
    asin: Optional[str] = Field(None, description="The asin associated with this Ad.")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the Campaign associated with the Ad.")
    extended_data: Optional["AdExtendedData"] = Field(None, alias="extendedData")
    full_funnel_campaign_id: Optional[str] = Field(None, alias="fullFunnelCampaignId", description="full funnel campaign id for child ad")
    landing_page_type: Optional[str] = Field(None, alias="landingPageType", description="The landing page type of the Ad. It can be one of ASIN_DP, SKU_DP, OFF_AMAZON_LINK, or STORE with ASIN, SKU, or an HTTPS")
    landing_page_value: Optional[str] = Field(None, alias="landingPageValue", description="The landing page for the Ad.")
    state: "EntityState"

    model_config = {'populate_by_name': True}


class AdErrorType(StrEnum):
    OTHER_ERROR = "OTHER_ERROR"
    RANGE_ERROR = "RANGE_ERROR"


class OtherErrorReason(StrEnum):
    OTHER_ERROR = "OTHER_ERROR"


class ErrorCause(BaseModel):
    """Structure describing error cause - location in the payload and data causing error."""
    location: str = Field(..., description="Error location, JSON Path expression specifying element of API payload causing error.")
    trigger: Optional[str] = Field(None, description="Optional value causing error.")

    model_config = {'populate_by_name': True}


class OtherError(BaseModel):
    """Errors not related to any of the other error types"""
    cause: "ErrorCause"
    message: str = Field(..., description="Human readable error message.")
    reason: "OtherErrorReason"

    model_config = {'populate_by_name': True}


class RangeErrorReason(StrEnum):
    INVALID_ENUM_VALUE = "INVALID_ENUM_VALUE"
    NOT_IN_LIST = "NOT_IN_LIST"
    OTHER = "OTHER"
    TOO_HIGH = "TOO_HIGH"
    TOO_LOW = "TOO_LOW"


class RangeError(BaseModel):
    """Errors related to range constraints and violations"""
    allowed: Optional[list[str]] = Field(None, description="Allowed values")
    cause: "ErrorCause"
    lower_limit: Optional[str] = Field(None, alias="lowerLimit", description="Optional lower limit.")
    message: str = Field(..., description="Human readable error message.")
    reason: "RangeErrorReason"
    upper_limit: Optional[str] = Field(None, alias="upperLimit", description="Optional upper limit.")

    model_config = {'populate_by_name': True}


class AdMutationErrorSelector(BaseModel):
    other_error: Optional["OtherError"] = Field(None, alias="otherError")
    range_error: Optional["RangeError"] = Field(None, alias="rangeError")

    model_config = {'populate_by_name': True}


class AdMutationError(BaseModel):
    error_type: "AdErrorType" = Field(..., alias="errorType")
    error_value: "AdMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class AdFailureResponseItem(BaseModel):
    errors: Optional[list["AdMutationError"]] = Field(None, description="A list of validation errors.")
    index: int = Field(..., description="The index of the ad in the array from the request body.")

    model_config = {'populate_by_name': True}


class AdGroupServingStatus(StrEnum):
    ACCOUNT_OUT_OF_BUDGET = "ACCOUNT_OUT_OF_BUDGET"
    ADGROUP_POLICING_CREATIVE_REJECTED = "ADGROUP_POLICING_CREATIVE_REJECTED"
    ADGROUP_POLICING_PENDING_REVIEW = "ADGROUP_POLICING_PENDING_REVIEW"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_POLICING_CREATIVE_REJECTED = "AD_GROUP_POLICING_CREATIVE_REJECTED"
    AD_GROUP_POLICING_PENDING_REVIEW = "AD_GROUP_POLICING_PENDING_REVIEW"
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    ENDED = "ENDED"
    INELIGIBLE = "INELIGIBLE"
    OTHER = "OTHER"
    PENDING_START_DATE = "PENDING_START_DATE"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"


class AdGroupExtendedData(BaseModel):
    creation_date: Optional[str] = Field(None, alias="creationDate", description="The date in ISO 8601 format")
    last_update_date: Optional[str] = Field(None, alias="lastUpdateDate", description="The date in ISO 8601 format")
    serving_status: Optional["AdGroupServingStatus"] = Field(None, alias="servingStatus")

    model_config = {'populate_by_name': True}


class DefaultBid(BaseModel):
    bid: Optional[float] = Field(None, description="The amount of the default bid associated with the ad group. Used if no bid is specified.")

    model_config = {'populate_by_name': True}


class AdGroup(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the Ad Group.")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the Campaign associated with the Ad Group.")
    default_bid: Optional["DefaultBid"] = Field(None, alias="defaultBid")
    extended_data: Optional["AdGroupExtendedData"] = Field(None, alias="extendedData")
    full_funnel_campaign_id: Optional[str] = Field(None, alias="fullFunnelCampaignId", description="full funnel campaign id for child ad group")
    name: str = Field(..., description="The name of the Ad Group.")
    state: "EntityState"

    model_config = {'populate_by_name': True}


class AdGroupErrorType(StrEnum):
    BIDDING_ERROR = "BIDDING_ERROR"
    DATE_ERROR = "DATE_ERROR"
    OTHER_ERROR = "OTHER_ERROR"
    RANGE_ERROR = "RANGE_ERROR"


class DateErrorReason(StrEnum):
    END_DATE_EARLIER_THAN_TODAY = "END_DATE_EARLIER_THAN_TODAY"
    END_DATE_LATER_THAN_MAXIMUM = "END_DATE_LATER_THAN_MAXIMUM"
    INVALID_DATE = "INVALID_DATE"
    OTHER = "OTHER"
    START_DATE_AFTER_END_DATE = "START_DATE_AFTER_END_DATE"
    START_DATE_EARLIER_THAN_TODAY = "START_DATE_EARLIER_THAN_TODAY"
    START_DATE_LATER_THAN_MAXIMUM = "START_DATE_LATER_THAN_MAXIMUM"
    UPDATING_READ_ONLY_END_DATE = "UPDATING_READ_ONLY_END_DATE"
    UPDATING_READ_ONLY_START_DATE = "UPDATING_READ_ONLY_START_DATE"


class DateError(BaseModel):
    """Errors related to dates."""
    cause: "ErrorCause"
    message: str = Field(..., description="Human readable error message.")
    reason: "DateErrorReason"

    model_config = {'populate_by_name': True}


class BiddingErrorReason(StrEnum):
    BID_GT_BUDGET = "BID_GT_BUDGET"
    BID_OUT_OF_MARKET_PLACE_RANGE = "BID_OUT_OF_MARKET_PLACE_RANGE"
    OTHER = "OTHER"


class BiddingError(BaseModel):
    """Errors related to bids."""
    cause: "ErrorCause"
    lower_limit: Optional[str] = Field(None, alias="lowerLimit")
    message: str = Field(..., description="Human readable error message.")
    reason: "BiddingErrorReason"
    upper_limit: Optional[str] = Field(None, alias="upperLimit")

    model_config = {'populate_by_name': True}


class AdGroupMutationErrorSelector(BaseModel):
    bidding_error: Optional["BiddingError"] = Field(None, alias="biddingError")
    date_error: Optional["DateError"] = Field(None, alias="dateError")
    other_error: Optional["OtherError"] = Field(None, alias="otherError")
    range_error: Optional["RangeError"] = Field(None, alias="rangeError")

    model_config = {'populate_by_name': True}


class AdGroupMutationError(BaseModel):
    error_type: "AdGroupErrorType" = Field(..., alias="errorType")
    error_value: "AdGroupMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class AdGroupFailureResponseItem(BaseModel):
    errors: Optional[list["AdGroupMutationError"]] = Field(None, description="A list of validation errors.")
    index: int = Field(..., description="The index of the ad group in the array from the request body.")

    model_config = {'populate_by_name': True}


class InvalidArgumentErrorCode(StrEnum):
    INVALID_ARGUMENT = "INVALID_ARGUMENT"


class AdGroupMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating campaign management entities"""
    code: "InvalidArgumentErrorCode"
    errors: Optional[list["AdGroupMutationError"]] = None
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class AdGroupSuccessResponseItem(BaseModel):
    ad_group: Optional["AdGroup"] = Field(None, alias="adGroup")
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="The ad group ID.")
    index: int = Field(..., description="The index of the ad group in the array from the request body.")

    model_config = {'populate_by_name': True}


class AdMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating campaign management entities"""
    code: "InvalidArgumentErrorCode"
    errors: Optional[list["AdMutationError"]] = None
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class AdSuccessResponseItem(BaseModel):
    ad: Optional["Ad"] = None
    ad_id: Optional[str] = Field(None, alias="adId", description="The ad ID.")
    index: int = Field(..., description="The index of the ad in the array from the request body.")

    model_config = {'populate_by_name': True}


class AssetProperties(BaseModel):
    """The properties of the video asset to preview. You must provide either `creativeId` or `assetProperties`. `assetProperties` cannot be used in conjunction with `creativeId`."""
    asset_id: str = Field(..., alias="assetId", description="The unique identifier of the video asset. This assetId comes from the Creative Asset Library.")
    asset_version: str = Field(..., alias="assetVersion", description="The identifier of the particular video asset version.")

    model_config = {'populate_by_name': True}


class BillingErrorReason(StrEnum):
    ADVERTISER_BILLING_SETUP_INCOMPLETE = "ADVERTISER_BILLING_SETUP_INCOMPLETE"
    ADVERTISER_SUSPENDED = "ADVERTISER_SUSPENDED"
    BILLING_ACCOUNT_NOT_FOUND = "BILLING_ACCOUNT_NOT_FOUND"
    EXPIRED_PAYMENT_METHOD = "EXPIRED_PAYMENT_METHOD"
    OTHER = "OTHER"
    PAYMENT_PROFILE_NOT_FOUND = "PAYMENT_PROFILE_NOT_FOUND"
    VETTING_FAILURE = "VETTING_FAILURE"


class BillingError(BaseModel):
    """Errors related to billing"""
    cause: "ErrorCause"
    message: str = Field(..., description="Human readable error message.")
    reason: "BillingErrorReason"

    model_config = {'populate_by_name': True}


class BudgetCurrencyCode(StrEnum):
    AED = "AED"
    AUD = "AUD"
    BRL = "BRL"
    CAD = "CAD"
    EGP = "EGP"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"
    JPY = "JPY"
    MXN = "MXN"
    MXP = "MXP"
    PLN = "PLN"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    TRY = "TRY"
    USD = "USD"


class BudgetValue(BaseModel):
    amount: Optional[float] = Field(None, description="The budget amount of the campaign")
    budget_currency_code: Optional["BudgetCurrencyCode"] = Field(None, alias="budgetCurrencyCode")

    model_config = {'populate_by_name': True}


class RecurrenceType(StrEnum):
    DAILY = "DAILY"


class Budget(BaseModel):
    budget_value: "BudgetValue" = Field(..., alias="budgetValue")
    recurrence_type: Optional["RecurrenceType"] = Field(None, alias="recurrenceType")

    model_config = {'populate_by_name': True}


class BudgetErrorReason(StrEnum):
    BUDGETING_POLICY_INVALID = "BUDGETING_POLICY_INVALID"
    BUDGET_CURRENCY_DOES_NOT_MATCH_MARKETPLACE_SETTINGS = "BUDGET_CURRENCY_DOES_NOT_MATCH_MARKETPLACE_SETTINGS"
    BUDGET_LT_DEFAULT_BIDS = "BUDGET_LT_DEFAULT_BIDS"
    BUDGET_LT_PREDEFINED_TARGET_BIDS = "BUDGET_LT_PREDEFINED_TARGET_BIDS"
    BUDGET_OUT_OF_MARKET_PLACE_RANGE = "BUDGET_OUT_OF_MARKET_PLACE_RANGE"
    BUDGET_TOO_HIGH = "BUDGET_TOO_HIGH"
    BUDGET_TOO_LOW = "BUDGET_TOO_LOW"
    MISSING_BUDGETING_POLICY = "MISSING_BUDGETING_POLICY"
    MISSING_IN_BUDGET_FLAG = "MISSING_IN_BUDGET_FLAG"
    OTHER = "OTHER"


class BudgetError(BaseModel):
    """Errors related to budgets"""
    cause: "ErrorCause"
    lower_limit: Optional[str] = Field(None, alias="lowerLimit")
    message: str = Field(..., description="Human readable error message.")
    reason: "BudgetErrorReason"
    upper_limit: Optional[str] = Field(None, alias="upperLimit")

    model_config = {'populate_by_name': True}


class BudgetSettings(BaseModel):
    budget: "Budget"

    model_config = {'populate_by_name': True}


class BulkAdGroupsOperationResponse(BaseModel):
    error: Optional[list["AdGroupFailureResponseItem"]] = None
    success: Optional[list["AdGroupSuccessResponseItem"]] = None

    model_config = {'populate_by_name': True}


class BulkAdsOperationResponse(BaseModel):
    error: Optional[list["AdFailureResponseItem"]] = None
    success: Optional[list["AdSuccessResponseItem"]] = None

    model_config = {'populate_by_name': True}


class CampaignServingStatus(StrEnum):
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    ADVERTISER_OUT_OF_PREPAY_BALANCE = "ADVERTISER_OUT_OF_PREPAY_BALANCE"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_STATUS_ENABLED = "CAMPAIGN_STATUS_ENABLED"
    ELIGIBLE = "ELIGIBLE"
    ENDED = "ENDED"
    INELIGIBLE = "INELIGIBLE"
    OTHER = "OTHER"
    PENDING_REVIEW = "PENDING_REVIEW"
    PENDING_START_DATE = "PENDING_START_DATE"
    PORTFOLIO_ARCHIVED = "PORTFOLIO_ARCHIVED"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    PORTFOLIO_PAUSED = "PORTFOLIO_PAUSED"
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"
    PORTFOLIO_STATUS_ENABLED = "PORTFOLIO_STATUS_ENABLED"
    REJECTED = "REJECTED"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"


class CampaignExtendedData(BaseModel):
    creation_date: Optional[str] = Field(None, alias="creationDate", description="The date in ISO 8601 format.")
    last_update_date: Optional[str] = Field(None, alias="lastUpdateDate", description="The date in ISO 8601 format.")
    serving_status: Optional["CampaignServingStatus"] = Field(None, alias="servingStatus")

    model_config = {'populate_by_name': True}


class Tags(BaseModel):
    """A list of advertiser-specified custom identifiers for the Campaign. Each customer identifier is a key-value pair. Supports up to 50 custom identifiers.  Functionality varies by date and advertiser typ"""
    __root__: dict[str, str] = {}


class TargetingType(StrEnum):
    AUTO_RELEVANT_TO_MY_BUSINESS = "AUTO_RELEVANT_TO_MY_BUSINESS"
    MANUAL = "MANUAL"


class Campaign(BaseModel):
    budget_settings: "BudgetSettings" = Field(..., alias="budgetSettings")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the Campaign.")
    cost_type: Optional[str] = Field(None, alias="costType", description="Cost type of the Campaign. Determines how the Campaign will bid and charge. Note that new values can be added to this li")
    end_date: Optional[str] = Field(None, alias="endDate", description="The YYYYMMDD end date for the Campaign. Must be greater than the value for startDate. If not specified, the Campaign has")
    extended_data: Optional["CampaignExtendedData"] = Field(None, alias="extendedData")
    full_funnel_campaign_id: Optional[str] = Field(None, alias="fullFunnelCampaignId", description="full funnel campaign id for child campaign")
    name: str = Field(..., description="The name of the Campaign.  Note: Names including single quotes must be escaped. For example, to create `Campaign 'A'`, t")
    start_date: Optional[str] = Field(None, alias="startDate", description="The YYYYMMDD start date for the Campaign. If this field is not set to a value, the current date is used.")
    state: "EntityState"
    tags: Optional["Tags"] = None
    targeting_type: Optional["TargetingType"] = Field(None, alias="targetingType")

    model_config = {'populate_by_name': True}


class CampaignSuccessResponseItem(BaseModel):
    campaign: Optional["Campaign"] = None
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="The campaign ID.")
    index: int = Field(..., description="The index of the campaign in the array from the request body.")

    model_config = {'populate_by_name': True}


class CampaignMutationErrorSelector(BaseModel):
    bidding_error: Optional["BiddingError"] = Field(None, alias="biddingError")
    budget_error: Optional["BudgetError"] = Field(None, alias="budgetError")
    date_error: Optional["DateError"] = Field(None, alias="dateError")
    other_error: Optional["OtherError"] = Field(None, alias="otherError")
    range_error: Optional["RangeError"] = Field(None, alias="rangeError")

    model_config = {'populate_by_name': True}


class CampaignErrorType(StrEnum):
    BIDDING_ERROR = "BIDDING_ERROR"
    BILLING_ERROR = "BILLING_ERROR"
    BUDGET_ERROR = "BUDGET_ERROR"
    DATE_ERROR = "DATE_ERROR"
    OTHER_ERROR = "OTHER_ERROR"
    RANGE_ERROR = "RANGE_ERROR"


class CampaignMutationError(BaseModel):
    error_type: "CampaignErrorType" = Field(..., alias="errorType")
    error_value: "CampaignMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class CampaignFailureResponseItem(BaseModel):
    errors: Optional[list["CampaignMutationError"]] = Field(None, description="A list of validation errors.")
    index: int = Field(..., description="the index of the campaign in the array from the request body.")

    model_config = {'populate_by_name': True}


class BulkCampaignOperationResponse(BaseModel):
    error: Optional[list["CampaignFailureResponseItem"]] = None
    success: Optional[list["CampaignSuccessResponseItem"]] = None

    model_config = {'populate_by_name': True}


class CreativeErrorType(StrEnum):
    OTHER_ERROR = "OTHER_ERROR"
    RANGE_ERROR = "RANGE_ERROR"


class CreativeMutationErrorSelector(BaseModel):
    other_error: Optional["OtherError"] = Field(None, alias="otherError")
    range_error: Optional["RangeError"] = Field(None, alias="rangeError")

    model_config = {'populate_by_name': True}


class CreativeMutationError(BaseModel):
    error_type: "CreativeErrorType" = Field(..., alias="errorType")
    error_value: "CreativeMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class CreativeFailureResponseItem(BaseModel):
    errors: Optional[list["CreativeMutationError"]] = Field(None, description="A list of validation errors.")
    index: int = Field(..., description="The index of the creative in the array from the request body.")

    model_config = {'populate_by_name': True}


class SponsoredTvCreativesModerationsStatus(StrEnum):
    APPROVED = "APPROVED"
    PENDING_REVIEW = "PENDING_REVIEW"
    REJECTED = "REJECTED"


class Creative(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the Ad Group to which this Creative is associated.")
    asset_id: str = Field(..., alias="assetId", description="The unique identifier of the video asset in use.")
    asset_version: str = Field(..., alias="assetVersion", description="The identifier of the particular video asset version.")
    creative_id: str = Field(..., alias="creativeId", description="The Creative identifier.")
    full_funnel_campaign_id: Optional[str] = Field(None, alias="fullFunnelCampaignId", description="full funnel campaign id for child creative")
    moderation_status: "SponsoredTvCreativesModerationsStatus" = Field(..., alias="moderationStatus")

    model_config = {'populate_by_name': True}


class CreativeSuccessResponseItem(BaseModel):
    creative: Optional["Creative"] = None
    creative_id: Optional[str] = Field(None, alias="creativeId", description="The creative ID.")
    index: int = Field(..., description="The index of the creative in the array from the request body.")

    model_config = {'populate_by_name': True}


class BulkCreativeOperationResponse(BaseModel):
    error: Optional[list["CreativeFailureResponseItem"]] = None
    success: Optional[list["CreativeSuccessResponseItem"]] = None

    model_config = {'populate_by_name': True}


class LocationErrorType(StrEnum):
    LOCATION_ERROR = "LOCATION_ERROR"
    OTHER_ERROR = "OTHER_ERROR"


class LocationError(BaseModel):
    """Errors related to location validation"""
    cause: Optional["ErrorCause"] = None
    message: str = Field(..., description="Human readable error message.")
    reason: str = Field(..., description="Reason for validation fields error in location")

    model_config = {'populate_by_name': True}


class LocationErrorSelector(BaseModel):
    location_error: Optional["LocationError"] = Field(None, alias="locationError")
    other_error: Optional["OtherError"] = Field(None, alias="otherError")

    model_config = {'populate_by_name': True}


class LocationMutationError(BaseModel):
    error_type: "LocationErrorType" = Field(..., alias="errorType")
    error_value: "LocationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class LocationFailureResponseItem(BaseModel):
    errors: Optional[list["LocationMutationError"]] = Field(None, description="A list of validation errors.")
    index: int = Field(..., description="The index of the location in the array from the request body.")

    model_config = {'populate_by_name': True}


class Location(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the Ad Group to which this Location is associated.")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the Campaign associated with the Ad Group.")
    location_expression_id: str = Field(..., alias="locationExpressionId", description="The Location identifier.")
    location_id: str = Field(..., alias="locationId", description="The Location Geo ACI (Amazon Common Identifier).")
    location_id_resolved: Optional[str] = Field(None, alias="locationIdResolved", description="A human-readable location text.")

    model_config = {'populate_by_name': True}


class LocationSuccessResponseItem(BaseModel):
    index: int = Field(..., description="The index of the location in the array from the request body.")
    location: Optional["Location"] = None

    model_config = {'populate_by_name': True}


class BulkLocationOperationResponse(BaseModel):
    error: Optional[list["LocationFailureResponseItem"]] = None
    success: Optional[list["LocationSuccessResponseItem"]] = None

    model_config = {'populate_by_name': True}


class TargetMutationErrorSelector(BaseModel):
    bidding_error: Optional["BiddingError"] = Field(None, alias="biddingError")
    billing_error: Optional["BillingError"] = Field(None, alias="billingError")
    other_error: Optional["OtherError"] = Field(None, alias="otherError")
    range_error: Optional["RangeError"] = Field(None, alias="rangeError")

    model_config = {'populate_by_name': True}


class TargetingClauseErrorType(StrEnum):
    BIDDING_ERROR = "BIDDING_ERROR"
    BILLING_ERROR = "BILLING_ERROR"
    OTHER_ERROR = "OTHER_ERROR"
    RANGE_ERROR = "RANGE_ERROR"


class TargetMutationError(BaseModel):
    error_type: "TargetingClauseErrorType" = Field(..., alias="errorType")
    error_value: "TargetMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class TargetingClauseFailureResponseItem(BaseModel):
    errors: Optional[list["TargetMutationError"]] = Field(None, description="A list of validation errors")
    index: int = Field(..., description="the index of the targetingClause in the array from the request body")

    model_config = {'populate_by_name': True}


class TargetingResolvedExpressionPredicate(BaseModel):
    type_: Optional[str] = Field(None, alias="type")
    value: Optional[str] = Field(None, description="'The human-readable value of the targeting predicate. Example for retail category '2617941011': `Arts, Crafts & Sewing` ")

    model_config = {'populate_by_name': True}


class TargetServingStatus(StrEnum):
    ACCOUNT_OUT_OF_BUDGET = "ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_POLICING_CREATIVE_REJECTED = "AD_GROUP_POLICING_CREATIVE_REJECTED"
    AD_GROUP_POLICING_PENDING_REVIEW = "AD_GROUP_POLICING_PENDING_REVIEW"
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    ENDED = "ENDED"
    INELIGIBLE = "INELIGIBLE"
    OTHER = "OTHER"
    PENDING_START_DATE = "PENDING_START_DATE"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"
    TARGETING_CLAUSE_ARCHIVED = "TARGETING_CLAUSE_ARCHIVED"
    TARGETING_CLAUSE_BLOCKED = "TARGETING_CLAUSE_BLOCKED"
    TARGETING_CLAUSE_PAUSED = "TARGETING_CLAUSE_PAUSED"
    TARGETING_CLAUSE_POLICING_SUSPENDED = "TARGETING_CLAUSE_POLICING_SUSPENDED"
    TARGETING_CLAUSE_STATUS_LIVE = "TARGETING_CLAUSE_STATUS_LIVE"


class TargetingClauseExtendedData(BaseModel):
    creation_date: Optional[str] = Field(None, alias="creationDate", description="The date in ISO 8601 format.")
    last_update_date: Optional[str] = Field(None, alias="lastUpdateDate", description="The date in ISO 8601 format.")
    serving_status: Optional["TargetServingStatus"] = Field(None, alias="servingStatus")

    model_config = {'populate_by_name': True}


class TargetingExpressionPredicate(BaseModel):
    type_: Optional[str] = Field(None, alias="type")
    value: Optional[str] = Field(None, description="'The value of the targeting predicate. Example for retail category `Arts, Crafts & Sewing`: '2617941011' Example for con")

    model_config = {'populate_by_name': True}


class TargetingClause(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the Ad Group to which this Targeting Clause is associated.")
    bid: Optional[float] = Field(None, description="This shape is deprecated: The bid for Ads sourced using the Targeting Clause. This field will no longer be supported as ")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the Campaign associated with the Ad.")
    expression: list["TargetingExpressionPredicate"] = Field(..., description="The targeting expression.")
    extended_data: Optional["TargetingClauseExtendedData"] = Field(None, alias="extendedData")
    full_funnel_campaign_id: Optional[str] = Field(None, alias="fullFunnelCampaignId", description="full funnel campaign id for child targeting clause")
    resolved_expression: Optional[list["TargetingResolvedExpressionPredicate"]] = Field(None, alias="resolvedExpression", description="A human-readable target text.")
    state: "EntityState"
    target_id: str = Field(..., alias="targetId", description="The Targeting Clause ID.")

    model_config = {'populate_by_name': True}


class TargetingClauseSuccessResponseItem(BaseModel):
    index: int = Field(..., description="the index of the targetingClause in the array from the request body")
    target_id: Optional[str] = Field(None, alias="targetId", description="the targetingClause ID")
    targeting_clause: Optional["TargetingClause"] = Field(None, alias="targetingClause")

    model_config = {'populate_by_name': True}


class BulkTargetingClauseOperationResponse(BaseModel):
    error: Optional[list["TargetingClauseFailureResponseItem"]] = None
    success: Optional[list["TargetingClauseSuccessResponseItem"]] = None

    model_config = {'populate_by_name': True}


class CallToAction(StrEnum):
    LEARN_MORE = "LEARN_MORE"
    SHOP_NOW = "SHOP_NOW"


class CallToActionPosition(StrEnum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class CampaignMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating campaign management entities"""
    code: "InvalidArgumentErrorCode"
    errors: Optional[list["CampaignMutationError"]] = None
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class CreateOrUpdateEntityState(StrEnum):
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


class CreateAd(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the Ad Group associated with the Ad.")
    ad_name: Optional[str] = Field(None, alias="adName", description="The name of the Ad.")
    full_funnel_campaign_id: Optional[str] = Field(None, alias="fullFunnelCampaignId", description="full funnel campaign id for child ad")
    landing_page_type: Optional[str] = Field(None, alias="landingPageType", description="The type of landing page for the Ad. You can specify one of these values: | Type | Description | | --- | ------- | | ASI")
    landing_page_value: Optional[str] = Field(None, alias="landingPageValue", description="The landing page for the Ad.")
    state: "CreateOrUpdateEntityState"

    model_config = {'populate_by_name': True}


class CreateAdGroup(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the Campaign associated with the Ad Group.")
    default_bid: Optional["DefaultBid"] = Field(None, alias="defaultBid")
    full_funnel_campaign_id: Optional[str] = Field(None, alias="fullFunnelCampaignId", description="full funnel campaign id for child ad group")
    name: str = Field(..., description="The name of the Ad Group.")
    state: "CreateOrUpdateEntityState"

    model_config = {'populate_by_name': True}


class CreateCampaign(BaseModel):
    budget_settings: "BudgetSettings" = Field(..., alias="budgetSettings")
    cost_type: Optional[str] = Field(None, alias="costType", description="Cost type of the Campaign. Determines how the Campaign will bid and charge. Note that new values can be added to this li")
    end_date: Optional[str] = Field(None, alias="endDate", description="endDate is optional. If endDate is specified, startDate must be specified as well.")
    full_funnel_campaign_id: Optional[str] = Field(None, alias="fullFunnelCampaignId", description="full funnel campaign id for child campaign")
    name: str = Field(..., description="The name of the Campaign.  Note: Names including single quotes must be escaped. For example, to create `Campaign 'A'`, t")
    start_date: Optional[str] = Field(None, alias="startDate", description="startDate is optional. If startDate is not specified, current date will be used.")
    state: "CreateOrUpdateEntityState"
    tags: Optional["Tags"] = None
    targeting_type: Optional["TargetingType"] = Field(None, alias="targetingType")

    model_config = {'populate_by_name': True}


class CreateCreative(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the Ad Group to which this Creative is associated.")
    asset_id: str = Field(..., alias="assetId", description="The unique identifier of the video asset. This assetId comes from the Creative Asset Library.")
    asset_version: str = Field(..., alias="assetVersion", description="The identifier of the particular video asset version.")
    full_funnel_campaign_id: Optional[str] = Field(None, alias="fullFunnelCampaignId", description="full funnel campaign id for child creative")

    model_config = {'populate_by_name': True}


class CreateLocation(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the Ad Group to which this Location is associated.")
    location_id: str = Field(..., alias="locationId", description="The Location Geo ACI (Amazon Common Identifier).")

    model_config = {'populate_by_name': True}


class CreateSponsoredTvAdGroupsRequestContent(BaseModel):
    ad_groups: list["CreateAdGroup"] = Field(..., alias="adGroups", description="An array of Sponsored TV ad groups.")

    model_config = {'populate_by_name': True}


class CreateSponsoredTvAdGroupsResponseContent(BaseModel):
    ad_groups: Optional["BulkAdGroupsOperationResponse"] = Field(None, alias="adGroups")

    model_config = {'populate_by_name': True}


class CreateSponsoredTvAdsRequestContent(BaseModel):
    ads: list["CreateAd"] = Field(..., description="An array of Sponsored TV ads.")

    model_config = {'populate_by_name': True}


class CreateSponsoredTvAdsResponseContent(BaseModel):
    ads: Optional["BulkAdsOperationResponse"] = None

    model_config = {'populate_by_name': True}


class CreateSponsoredTvCampaignsRequestContent(BaseModel):
    campaigns: list["CreateCampaign"]

    model_config = {'populate_by_name': True}


class CreateSponsoredTvCampaignsResponseContent(BaseModel):
    campaigns: Optional["BulkCampaignOperationResponse"] = None

    model_config = {'populate_by_name': True}


class CreateSponsoredTvCreativesRequestContent(BaseModel):
    creatives: list["CreateCreative"] = Field(..., description="An array of creatives.")

    model_config = {'populate_by_name': True}


class CreateSponsoredTvCreativesResponseContent(BaseModel):
    creatives: "BulkCreativeOperationResponse"

    model_config = {'populate_by_name': True}


class CreateSponsoredTvLocationsRequestContent(BaseModel):
    locations: list["CreateLocation"] = Field(..., description="An array of locations.")

    model_config = {'populate_by_name': True}


class CreateSponsoredTvLocationsResponseContent(BaseModel):
    locations: "BulkLocationOperationResponse"

    model_config = {'populate_by_name': True}


class CreateTargetingExpressionPredicate(BaseModel):
    type_: str = Field(..., alias="type", description="Determines the type of targeting. Note that new values can be added to this list in the future. Support for the response")
    value: str = Field(..., description="'The value of the targeting predicate. Example for retail category `Arts, Crafts & Sewing`: '2617941011' Example for con")

    model_config = {'populate_by_name': True}


class CreateTargetingClause(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the Ad Group to which this Targeting Clause is associated.")
    bid: Optional[float] = Field(None, description="This shape is deprecated: The bid for Ads sourced using the Targeting Clause. This field will no longer be supported as ")
    expression: list["CreateTargetingExpressionPredicate"] = Field(..., description="The targeting expression.")
    full_funnel_campaign_id: Optional[str] = Field(None, alias="fullFunnelCampaignId", description="full funnel campaign id for child targeting clause")
    state: "CreateOrUpdateEntityState"

    model_config = {'populate_by_name': True}


class CreateSponsoredTvTargetingClausesRequestContent(BaseModel):
    targeting_clauses: list["CreateTargetingClause"] = Field(..., alias="targetingClauses", description="An array of targetingClauses.")

    model_config = {'populate_by_name': True}


class CreateSponsoredTvTargetingClausesResponseContent(BaseModel):
    targeting_clauses: "BulkTargetingClauseOperationResponse" = Field(..., alias="targetingClauses")

    model_config = {'populate_by_name': True}


class CreativeIdFilter(BaseModel):
    """Filter entities by the list of creativeIds."""
    include: list[str]

    model_config = {'populate_by_name': True}


class CreativeMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating creative management entities"""
    code: "InvalidArgumentErrorCode"
    errors: Optional[list["CreativeMutationError"]] = None
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class CreativesModerations(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the Ad Group to which this Creative is associated.")
    creative_id: str = Field(..., alias="creativeId", description="The Creative identifier.")
    eta_for_moderation: Optional[str] = Field(None, alias="etaForModeration", description="Expected date and time by which moderation will be complete.")
    moderation_status: "SponsoredTvCreativesModerationsStatus" = Field(..., alias="moderationStatus")
    reviewed_video_url: Optional[str] = Field(None, alias="reviewedVideoUrl", description="Address of the video reviewed during moderation.")

    model_config = {'populate_by_name': True}


class ObjectIdFilter(BaseModel):
    """Filter entities by the list of objectIds."""
    include: list[str]

    model_config = {'populate_by_name': True}


class DeleteSponsoredTvAdGroupsRequestContent(BaseModel):
    ad_group_id_filter: "ObjectIdFilter" = Field(..., alias="adGroupIdFilter")

    model_config = {'populate_by_name': True}


class DeleteSponsoredTvAdGroupsResponseContent(BaseModel):
    ad_groups: Optional["BulkAdGroupsOperationResponse"] = Field(None, alias="adGroups")

    model_config = {'populate_by_name': True}


class DeleteSponsoredTvAdsRequestContent(BaseModel):
    ad_id_filter: "ObjectIdFilter" = Field(..., alias="adIdFilter")

    model_config = {'populate_by_name': True}


class DeleteSponsoredTvAdsResponseContent(BaseModel):
    ads: Optional["BulkAdsOperationResponse"] = None

    model_config = {'populate_by_name': True}


class DeleteSponsoredTvCampaignsRequestContent(BaseModel):
    campaign_id_filter: "ObjectIdFilter" = Field(..., alias="campaignIdFilter")

    model_config = {'populate_by_name': True}


class DeleteSponsoredTvCampaignsResponseContent(BaseModel):
    campaigns: Optional["BulkCampaignOperationResponse"] = None

    model_config = {'populate_by_name': True}


class DeleteSponsoredTvLocationsRequestContent(BaseModel):
    location_expression_id_filter: "ObjectIdFilter" = Field(..., alias="locationExpressionIdFilter")

    model_config = {'populate_by_name': True}


class DeleteSponsoredTvLocationsResponseContent(BaseModel):
    locations: "BulkLocationOperationResponse"

    model_config = {'populate_by_name': True}


class DeleteSponsoredTvTargetingClausesRequestContent(BaseModel):
    target_id_filter: "ObjectIdFilter" = Field(..., alias="targetIdFilter")

    model_config = {'populate_by_name': True}


class DeleteSponsoredTvTargetingClausesResponseContent(BaseModel):
    targeting_clauses: "BulkTargetingClauseOperationResponse" = Field(..., alias="targetingClauses")

    model_config = {'populate_by_name': True}


class EntityStateFilter(BaseModel):
    """Filter entities by state."""
    include: list["EntityState"]

    model_config = {'populate_by_name': True}


class Experience(BaseModel):
    """The advertiser experience type for a given preview video."""
    call_to_action: "CallToAction" = Field(..., alias="callToAction")
    interactivity: str = Field(..., description="The types of interactivity experiences Sponsored TV supports. Possible values: - BASE: viewers cannot have any interacti")

    model_config = {'populate_by_name': True}


class ForecastMetricType(StrEnum):
    CLICKS = "CLICKS"
    DETAIL_PAGE_VIEWS = "DETAIL_PAGE_VIEWS"
    IMPRESSIONS = "IMPRESSIONS"
    REACH = "REACH"


class ForecastValue(BaseModel):
    max: Optional[int] = None
    min: Optional[int] = None

    model_config = {'populate_by_name': True}


class Forecast(BaseModel):
    metric: Optional["ForecastMetricType"] = None
    value: Optional["ForecastValue"] = None

    model_config = {'populate_by_name': True}


class ForecastAd(BaseModel):
    """Simplified Ad for Forecast. Asin and sku used for vendors and sellers"""
    landing_page_type: str = Field(..., alias="landingPageType", description="The landing page type of the Ad. Forecast only use ASIN_DP or SKU_DP with asin or sku value in the `landingPageValue` fi")
    landing_page_value: str = Field(..., alias="landingPageValue", description="The landing page for the Ad")

    model_config = {'populate_by_name': True}


class ForecastAdGroup(BaseModel):
    """Simplified AdGroup needed for Forecast"""
    default_bid: Optional["DefaultBid"] = Field(None, alias="defaultBid")

    model_config = {'populate_by_name': True}


class ForecastCampaign(BaseModel):
    """Simplified Campaign needed for Forecast"""
    budget_settings: "BudgetSettings" = Field(..., alias="budgetSettings")
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="The identifier of the forecast campaign.")
    cost_type: Optional[str] = Field(None, alias="costType", description="Support for the responses with newly added values should be ensured for using them at the time of creation or updates.  ")
    end_date: Optional[str] = Field(None, alias="endDate", description="The yyyy-MM-dd'T'hh:mm:ss'Z' end date for the campaign in forecast. Must be greater than the value for startDate. If not")
    start_date: str = Field(..., alias="startDate", description="The yyyy-MM-dd'T'hh:mm:ss'Z' start date for the campaign in forecast. If this field is not set to a value, the current d")
    targeting_type: Optional["TargetingType"] = Field(None, alias="targetingType")

    model_config = {'populate_by_name': True}


class ForecastCreative(BaseModel):
    """Simplified Creative needed for Forecast"""
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="The identifier of the ad group to which this creative is associated.")
    asset_id: Optional[str] = Field(None, alias="assetId", description="The unique identifier of the video asset in use.")
    asset_version: Optional[str] = Field(None, alias="assetVersion", description="The identifier of the particular video asset version.")
    creative_id: Optional[str] = Field(None, alias="creativeId", description="The creative identifier.")
    video_duration: int = Field(..., alias="videoDuration", description="The duration time of the creative")

    model_config = {'populate_by_name': True}


class ForecastRulesError(BaseModel):
    """Forecast Errors related to forecast rules as too broad or too narrow"""
    cause: "ErrorCause"
    message: str = Field(..., description="Human readable error message.")
    reason: str = Field(..., description="Reason for forecast rules error")

    model_config = {'populate_by_name': True}


class ForecastValidationError(BaseModel):
    """Errors related to forecast input validation errors"""
    cause: "ErrorCause"
    message: str = Field(..., description="Human readable error message.")
    reason: str = Field(..., description="Reason for validation fields error in forecast")

    model_config = {'populate_by_name': True}


class ForecastOtherError(BaseModel):
    """Forecast Errors just targeting on the general forecast error type"""
    cause: "ErrorCause"
    message: str = Field(..., description="Human readable error message.")
    reason: str = Field(..., description="Reason for forecast other error")

    model_config = {'populate_by_name': True}


class ForecastModelError(BaseModel):
    """Forecast Errors related to forecast model"""
    cause: "ErrorCause"
    message: str = Field(..., description="Human readable error message.")
    reason: str = Field(..., description="Reason for forecast model error")

    model_config = {'populate_by_name': True}


class ForecastErrorSelector(BaseModel):
    forecast_model_error: Optional["ForecastModelError"] = Field(None, alias="forecastModelError")
    forecast_other_error: Optional["ForecastOtherError"] = Field(None, alias="forecastOtherError")
    forecast_rules_error: Optional["ForecastRulesError"] = Field(None, alias="forecastRulesError")
    forecast_validation_error: Optional["ForecastValidationError"] = Field(None, alias="forecastValidationError")

    model_config = {'populate_by_name': True}


class ForecastErrorType(StrEnum):
    FORECAST_MODEL_ERROR = "FORECAST_MODEL_ERROR"
    FORECAST_OTHER_ERROR = "FORECAST_OTHER_ERROR"
    FORECAST_RULES_ERROR = "FORECAST_RULES_ERROR"
    FORECAST_VALIDATION_ERROR = "FORECAST_VALIDATION_ERROR"


class ForecastErrorItem(BaseModel):
    error_type: "ForecastErrorType" = Field(..., alias="errorType")
    error_value: "ForecastErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class ForecastExceptionResponseContent(BaseModel):
    """Bad Request exception resulting in errors in ST forecast"""
    code: "InvalidArgumentErrorCode"
    errors: Optional[list["ForecastErrorItem"]] = None
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class ForecastLocationTargetingClause(BaseModel):
    """Simplified Location Targeting Clause for Forecast"""
    category: Optional[str] = Field(None, description="The category of the location, including DMA, CITY, POSTAL_CODE and so on.")
    location_id: str = Field(..., alias="locationId", description="The Location Geo ACI (Amazon Common Identifier).")
    location_id_resolved: Optional[str] = Field(None, alias="locationIdResolved", description="The human readable location information.")

    model_config = {'populate_by_name': True}


class ForecastTargetingClause(BaseModel):
    """Simplified Targeting Clause for Forecast, which only list of Targeting Expression and bid price"""
    bid: Optional[float] = Field(None, description="The bid for ads sourced using the target. The US marketplace has a default bid of $15 CPM")
    expression: list["TargetingExpressionPredicate"] = Field(..., description="The targeting expression.")

    model_config = {'populate_by_name': True}


class InternalErrorErrorCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class InternalServerExceptionResponseContent(BaseModel):
    code: "InternalErrorErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class InvalidArgumentErrorSelector(BaseModel):
    other_error: Optional["OtherError"] = Field(None, alias="otherError")
    range_error: Optional["RangeError"] = Field(None, alias="rangeError")

    model_config = {'populate_by_name': True}


class InvalidArgumentError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "InvalidArgumentErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class InvalidArgumentExceptionResponseContent(BaseModel):
    code: "InvalidArgumentErrorCode"
    errors: Optional[list["InvalidArgumentError"]] = None
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class QueryTermMatchType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class NameFilter(BaseModel):
    """Filter entities by name  Note: Names including single quotes must be escaped. For example, to filter for `Campaign 'A'`, provide the following filter array: `['Campaign '\\''A'\\''']`"""
    include: list[str]
    query_term_match_type: Optional["QueryTermMatchType"] = Field(None, alias="queryTermMatchType")

    model_config = {'populate_by_name': True}


class ListSponsoredTvAdGroupsRequestContent(BaseModel):
    ad_group_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    full_funnel_campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="fullFunnelCampaignIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API.")
    name_filter: Optional["NameFilter"] = Field(None, alias="nameFilter")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    state_filter: Optional["EntityStateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class ListSponsoredTvAdGroupsResponseContent(BaseModel):
    ad_groups: Optional[list["AdGroup"]] = Field(None, alias="adGroups")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    total_count: Optional[int] = Field(None, alias="totalCount", description="The total number of entities.")

    model_config = {'populate_by_name': True}


class ListSponsoredTvAdsRequestContent(BaseModel):
    ad_group_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    ad_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="adIdFilter")
    campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    full_funnel_campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="fullFunnelCampaignIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    state_filter: Optional["EntityStateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class ListSponsoredTvAdsResponseContent(BaseModel):
    ads: Optional[list["Ad"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    total_count: Optional[int] = Field(None, alias="totalCount", description="The total number of entities.")

    model_config = {'populate_by_name': True}


class ListSponsoredTvCampaignsRequestContent(BaseModel):
    campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    full_funnel_campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="fullFunnelCampaignIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API.")
    name_filter: Optional["NameFilter"] = Field(None, alias="nameFilter")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    state_filter: Optional["EntityStateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class ListSponsoredTvCampaignsResponseContent(BaseModel):
    campaigns: Optional[list["Campaign"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    total_count: Optional[int] = Field(None, alias="totalCount", description="The total number of entities.")

    model_config = {'populate_by_name': True}


class Locale(StrEnum):
    AR_AE = "ar-AE"
    DE_DE = "de-DE"
    EN_AE = "en-AE"
    EN_AU = "en-AU"
    EN_BR = "en-BR"
    EN_CA = "en-CA"
    EN_DE = "en-DE"
    EN_ES = "en-ES"
    EN_FR = "en-FR"
    EN_GB = "en-GB"
    EN_IN = "en-IN"
    EN_IT = "en-IT"
    EN_JP = "en-JP"
    EN_SG = "en-SG"
    EN_US = "en-US"
    ES_ES = "es-ES"
    ES_MX = "es-MX"
    FR_CA = "fr-CA"
    FR_FR = "fr-FR"
    HI_IN = "hi-IN"
    IT_IT = "it-IT"
    JA_JP = "ja-JP"
    KO_KR = "ko-KR"
    NL_NL = "nl-NL"
    PT_BR = "pt-BR"
    ZH_CN = "zh-CN"


class ListSponsoredTvCreativesModerationsPolicyViolationsRequestContent(BaseModel):
    creative_id_filter: "CreativeIdFilter" = Field(..., alias="creativeIdFilter")
    locale: Optional["Locale"] = None
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")

    model_config = {'populate_by_name': True}


class SponsoredTvViolatingVideoEvidence(BaseModel):
    end: Optional[int] = Field(None, description="Time in seconds at which policy violation within the video asset ends.")
    start: Optional[int] = Field(None, description="Time in seconds at which policy violation within the video asset starts.")

    model_config = {'populate_by_name': True}


class SponsoredTvPolicyViolation(BaseModel):
    policy_description: Optional[str] = Field(None, alias="policyDescription", description="A human-readable description of the policy.")
    policy_link_url: Optional[str] = Field(None, alias="policyLinkUrl", description="Address of the policy documentation. Follow the link to learn more about the specified policy.")
    video_evidences: Optional[list["SponsoredTvViolatingVideoEvidence"]] = Field(None, alias="videoEvidences", description="An array of start and end times in seconds for the given policy violation. While there may be more than 15 video evidenc")

    model_config = {'populate_by_name': True}


class ListSponsoredTvCreativesModerationsPolicyViolationsResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    policy_violations: Optional[list["SponsoredTvPolicyViolation"]] = Field(None, alias="policyViolations")

    model_config = {'populate_by_name': True}


class ListSponsoredTvCreativesModerationsRequestContent(BaseModel):
    ad_group_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    creative_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="creativeIdFilter")
    locale: Optional["Locale"] = None
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")

    model_config = {'populate_by_name': True}


class ListSponsoredTvCreativesModerationsResponseContent(BaseModel):
    creatives_moderations: Optional[list["CreativesModerations"]] = Field(None, alias="creativesModerations")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")

    model_config = {'populate_by_name': True}


class ListSponsoredTvCreativesRequestContent(BaseModel):
    ad_group_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    creative_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="creativeIdFilter")
    full_funnel_campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="fullFunnelCampaignIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")

    model_config = {'populate_by_name': True}


class ListSponsoredTvCreativesResponseContent(BaseModel):
    creatives: Optional[list["Creative"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of creative entities.")

    model_config = {'populate_by_name': True}


class ListSponsoredTvLocationsRequestContent(BaseModel):
    ad_group_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    location_expression_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="locationExpressionIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the Locations paginated response. Defaults to max page size for given API.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")

    model_config = {'populate_by_name': True}


class ListSponsoredTvLocationsResponseContent(BaseModel):
    locations: Optional[list["Location"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of entities.")

    model_config = {'populate_by_name': True}


class ListSponsoredTvTargetingClausesRequestContent(BaseModel):
    ad_group_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    full_funnel_campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="fullFunnelCampaignIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    state_filter: Optional["EntityStateFilter"] = Field(None, alias="stateFilter")
    target_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="targetIdFilter")

    model_config = {'populate_by_name': True}


class ListSponsoredTvTargetingClausesResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    targeting_clauses: Optional[list["TargetingClause"]] = Field(None, alias="targetingClauses")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of entities.")

    model_config = {'populate_by_name': True}


class LocationMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating campaign management entities"""
    code: "InvalidArgumentErrorCode"
    errors: Optional[list["LocationMutationError"]] = None
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class PreviewConfiguration(BaseModel):
    """Configuration settings for the preview."""
    asin: Optional[str] = Field(None, description="Amazon Standard Identification Number: The code that identifies the product being advertised. You must provide either `a")
    call_to_action: Optional["CallToAction"] = Field(None, alias="callToAction")
    call_to_action_position: Optional["CallToActionPosition"] = Field(None, alias="callToActionPosition")
    safe_zone_enabled: Optional[bool] = Field(None, alias="safeZoneEnabled", description="Whether or not to see the safe zone as an overlay (true (default) | false).")
    sku: Optional[str] = Field(None, description="Stock Keeping Unit: The unique identifier for the product being advertised. You must provide either `asin` or `sku`.`sku")

    model_config = {'populate_by_name': True}


class PreviewHtml(BaseModel):
    """The experience type and HTML for a given preview video"""
    experience: "Experience"
    html: str = Field(..., description="The HTML for one preview video.")

    model_config = {'populate_by_name': True}


class PreviewSponsoredTvCreativeRequestContent(BaseModel):
    asset_properties: Optional["AssetProperties"] = Field(None, alias="assetProperties")
    creative_id: Optional[str] = Field(None, alias="creativeId", description="The unique identifier of the creative to preview. You must provide either `creativeId` or `assetProperties`. `creativeId")
    preview_configuration: "PreviewConfiguration" = Field(..., alias="previewConfiguration")

    model_config = {'populate_by_name': True}


class PreviewSponsoredTvCreativeResponseContent(BaseModel):
    preview_htmls: list["PreviewHtml"] = Field(..., alias="previewHtmls", description="The list of HTMLs for all the requested preview videos.")

    model_config = {'populate_by_name': True}


class SponsoredTvForecastsRequestContent(BaseModel):
    ad_group: "ForecastAdGroup" = Field(..., alias="adGroup")
    ads: list["ForecastAd"] = Field(..., description="list of product Ads specified in ST forecast.")
    campaign: "ForecastCampaign"
    creative: Optional["ForecastCreative"] = None
    location_targeting_clauses: Optional[list["ForecastLocationTargetingClause"]] = Field(None, alias="locationTargetingClauses", description="list of location targeting clauses specified in ST forecast")
    targeting_clauses: list["ForecastTargetingClause"] = Field(..., alias="targetingClauses", description="list of targeting clauses specified in ST forecast.")

    model_config = {'populate_by_name': True}


class SponsoredTvForecastsResponseContent(BaseModel):
    weekly_forecasts: Optional[list["Forecast"]] = Field(None, alias="weeklyForecasts", description="the weekly forecast response include in a list")

    model_config = {'populate_by_name': True}


class TargetMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating campaign management entities"""
    code: "InvalidArgumentErrorCode"
    errors: Optional[list["TargetMutationError"]] = None
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class ThrottledErrorCode(StrEnum):
    THROTTLED = "THROTTLED"


class ThrottlingExceptionResponseContent(BaseModel):
    code: "ThrottledErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class UnauthorizedErrorCode(StrEnum):
    UNAUTHORIZED = "UNAUTHORIZED"


class UnauthorizedExceptionResponseContent(BaseModel):
    code: "UnauthorizedErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class UpdateAd(BaseModel):
    ad_id: str = Field(..., alias="adId", description="The Ad identifier.")
    ad_name: Optional[str] = Field(None, alias="adName", description="The name of the Ad.")
    state: Optional["CreateOrUpdateEntityState"] = None

    model_config = {'populate_by_name': True}


class UpdateAdGroup(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The Ad Group ID.")
    default_bid: Optional["DefaultBid"] = Field(None, alias="defaultBid")
    name: Optional[str] = Field(None, description="The name of the Ad Group.")
    state: Optional["CreateOrUpdateEntityState"] = None

    model_config = {'populate_by_name': True}


class UpdateCampaign(BaseModel):
    budget_settings: Optional["BudgetSettings"] = Field(None, alias="budgetSettings")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the Campaign.")
    cost_type: Optional[str] = Field(None, alias="costType", description="Cost type of the Campaign. Determines how the campaign will bid and charge. Note that new values can be added to this li")
    end_date: Optional[str] = Field(None, alias="endDate", description="endDate is optional. If endDate is specified, startDate must be specified as well.")
    name: Optional[str] = Field(None, description="The name of the Campaign.  Note: Names including single quotes must be escaped. For example, to update the name to `Camp")
    start_date: Optional[str] = Field(None, alias="startDate", description="startDate can only be changed if the current startDate is in the future.")
    state: Optional["CreateOrUpdateEntityState"] = None
    tags: Optional["Tags"] = None

    model_config = {'populate_by_name': True}


class UpdateCreative(BaseModel):
    asset_id: str = Field(..., alias="assetId", description="The unique identifier of the video asset. This assetId comes from the Creative Asset Library.")
    asset_version: str = Field(..., alias="assetVersion", description="The identifier of the particular video asset version.")
    creative_id: str = Field(..., alias="creativeId", description="The Creative identifier.")

    model_config = {'populate_by_name': True}


class UpdateSponsoredTvAdGroupsRequestContent(BaseModel):
    ad_groups: list["UpdateAdGroup"] = Field(..., alias="adGroups", description="An array of Sponsored TV ad groups.")

    model_config = {'populate_by_name': True}


class UpdateSponsoredTvAdGroupsResponseContent(BaseModel):
    ad_groups: Optional["BulkAdGroupsOperationResponse"] = Field(None, alias="adGroups")

    model_config = {'populate_by_name': True}


class UpdateSponsoredTvAdsRequestContent(BaseModel):
    ads: list["UpdateAd"] = Field(..., description="An array of Sponsored TV ads.")

    model_config = {'populate_by_name': True}


class UpdateSponsoredTvAdsResponseContent(BaseModel):
    ads: Optional["BulkAdsOperationResponse"] = None

    model_config = {'populate_by_name': True}


class UpdateSponsoredTvCampaignsRequestContent(BaseModel):
    campaigns: list["UpdateCampaign"]

    model_config = {'populate_by_name': True}


class UpdateSponsoredTvCampaignsResponseContent(BaseModel):
    campaigns: Optional["BulkCampaignOperationResponse"] = None

    model_config = {'populate_by_name': True}


class UpdateSponsoredTvCreativesRequestContent(BaseModel):
    creatives: list["UpdateCreative"] = Field(..., description="An array of creatives.")

    model_config = {'populate_by_name': True}


class UpdateSponsoredTvCreativesResponseContent(BaseModel):
    creatives: "BulkCreativeOperationResponse"

    model_config = {'populate_by_name': True}


class UpdateTargetingClause(BaseModel):
    bid: Optional[float] = Field(None, description="This shape is deprecated: The bid for Ads sourced using the Targeting Clause. This field will no longer be supported as ")
    state: "CreateOrUpdateEntityState"
    target_id: str = Field(..., alias="targetId", description="The Targeting Clause ID.")

    model_config = {'populate_by_name': True}


class UpdateSponsoredTvTargetingClausesRequestContent(BaseModel):
    targeting_clauses: list["UpdateTargetingClause"] = Field(..., alias="targetingClauses", description="An array of targetingClauses.")

    model_config = {'populate_by_name': True}


class UpdateSponsoredTvTargetingClausesResponseContent(BaseModel):
    targeting_clauses: "BulkTargetingClauseOperationResponse" = Field(..., alias="targetingClauses")

    model_config = {'populate_by_name': True}

