"""Auto-generated Pydantic models. Do not edit manually.

Source: AmazonAdvertiserAPIforRetailAdService_prod_3p.json
Title:  Amazon Advertiser API for Retail Ad Service
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class RASv1AccessDeniedErrorCode(StrEnum):
    ACCESS_DENIED = "ACCESS_DENIED"


class RASv1AccessDeniedExceptionResponseContent(BaseModel):
    code: "RASv1AccessDeniedErrorCode"
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class RASv1Marketplace(StrEnum):
    US = "US"


class RASv1ErrorCause(BaseModel):
    """Structure describing error cause - location in the payload and data causing error"""
    location: str = Field(..., description="Error location, JSON Path expression specifying element of API payload causing error")
    trigger: Optional[str] = Field(None, description="optional value causing error")

    model_config = {'populate_by_name': True}


class RASv1AdEligibilityErrorReason(StrEnum):
    AD_INELIGIBLE = "AD_INELIGIBLE"


class RASv1AdEligibilityError(BaseModel):
    """Errors related to ad eligibility"""
    cause: Optional["RASv1ErrorCause"] = None
    marketplace: Optional["RASv1Marketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "RASv1AdEligibilityErrorReason"

    model_config = {'populate_by_name': True}


class RASv1OtherErrorReason(StrEnum):
    OTHER_ERROR = "OTHER_ERROR"


class RASv1OtherError(BaseModel):
    """Errors not related to any of the other error types"""
    cause: Optional["RASv1ErrorCause"] = None
    marketplace: Optional["RASv1Marketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "RASv1OtherErrorReason"

    model_config = {'populate_by_name': True}


class RASv1MalformedValueErrorReason(StrEnum):
    BLANK = "BLANK"
    FORBIDDEN_CHARS = "FORBIDDEN_CHARS"
    LEADING_OR_TRAILING_WHITESPACE = "LEADING_OR_TRAILING_WHITESPACE"
    PATTERN_NOT_MATCHED = "PATTERN_NOT_MATCHED"
    TOO_LONG = "TOO_LONG"
    TOO_SHORT = "TOO_SHORT"


class RASv1MalformedValueError(BaseModel):
    """Errors being used to represent malformed values e.g. containing not allowed characters, not following patters etc"""
    cause: Optional["RASv1ErrorCause"] = None
    fragment: Optional[str] = Field(None, description="fragment of the value which is wrong")
    marketplace: Optional["RASv1Marketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "RASv1MalformedValueErrorReason"

    model_config = {'populate_by_name': True}


class RASv1ThrottledErrorReason(StrEnum):
    THROTTLED = "THROTTLED"


class RASv1ThrottledError(BaseModel):
    """Error that represents failure due to API caller exceeding allowed service limits."""
    cause: Optional["RASv1ErrorCause"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "RASv1ThrottledErrorReason"

    model_config = {'populate_by_name': True}


class RASv1EntityType(StrEnum):
    AD_GROUP = "AD_GROUP"
    CAMPAIGN = "CAMPAIGN"
    CAMPAIGN_NEGATIVE_KEYWORD = "CAMPAIGN_NEGATIVE_KEYWORD"
    CAMPAIGN_NEGATIVE_TARGETING_CLAUSE = "CAMPAIGN_NEGATIVE_TARGETING_CLAUSE"
    KEYWORD = "KEYWORD"
    NEGATIVE_KEYWORD = "NEGATIVE_KEYWORD"
    NEGATIVE_TARGETING_CLAUSE = "NEGATIVE_TARGETING_CLAUSE"
    PRODUCT_AD = "PRODUCT_AD"
    TARGETING_CLAUSE = "TARGETING_CLAUSE"


class RASv1EntityNotFoundErrorReason(StrEnum):
    ENTITY_NOT_FOUND = "ENTITY_NOT_FOUND"


class RASv1EntityNotFoundError(BaseModel):
    cause: Optional["RASv1ErrorCause"] = None
    entity_id: str = Field(..., alias="entityId", description="The entity id in the request")
    entity_type: "RASv1EntityType" = Field(..., alias="entityType")
    message: str = Field(..., description="Human readable error message")
    reason: "RASv1EntityNotFoundErrorReason"

    model_config = {'populate_by_name': True}


class RASv1InternalServerErrorReason(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class RASv1InternalServerError(BaseModel):
    """Error that represents non-retryable API service error. Sending the same request will result in another error."""
    cause: Optional["RASv1ErrorCause"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "RASv1InternalServerErrorReason"

    model_config = {'populate_by_name': True}


class RASv1ValueLimitErrorReason(StrEnum):
    INVALID_ENUM_VALUE = "INVALID_ENUM_VALUE"
    NOT_IN_LIST = "NOT_IN_LIST"
    TOO_HIGH = "TOO_HIGH"
    TOO_LOW = "TOO_LOW"


class RASv1RangeError(BaseModel):
    """Errors related to range constraints violations"""
    allowed: Optional[list[str]] = Field(None, description="allowed values")
    cause: Optional["RASv1ErrorCause"] = None
    lower_limit: Optional[str] = Field(None, alias="lowerLimit", description="optional lower limit")
    marketplace: Optional["RASv1Marketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "RASv1ValueLimitErrorReason"
    upper_limit: Optional[str] = Field(None, alias="upperLimit", description="optional upper limit")

    model_config = {'populate_by_name': True}


class RASv1MissingValueErrorReason(StrEnum):
    MISSING_VALUE = "MISSING_VALUE"


class RASv1MissingValueError(BaseModel):
    """Error describing missing values in API payloads"""
    cause: Optional["RASv1ErrorCause"] = None
    marketplace: Optional["RASv1Marketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "RASv1MissingValueErrorReason"

    model_config = {'populate_by_name': True}


class RASv1AdGroupAccessErrorSelector(BaseModel):
    entity_not_found_error: Optional["RASv1EntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    internal_server_error: Optional["RASv1InternalServerError"] = Field(None, alias="internalServerError")
    malformed_value_error: Optional["RASv1MalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["RASv1MissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["RASv1OtherError"] = Field(None, alias="otherError")
    range_error: Optional["RASv1RangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["RASv1ThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class RASv1AdGroupAccessError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "RASv1AdGroupAccessErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class RASv1InvalidArgumentErrorCode(StrEnum):
    INVALID_ARGUMENT = "INVALID_ARGUMENT"


class RASv1AdGroupAccessExceptionResponseContent(BaseModel):
    """Exception resulting in accessing ad group entities"""
    code: "RASv1InvalidArgumentErrorCode"
    errors: Optional[list["RASv1AdGroupAccessError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class RASv1AdGroupServingStatusReason(StrEnum):
    ADVERTISER_ARCHIVED_DETAIL = "ADVERTISER_ARCHIVED_DETAIL"
    ADVERTISER_OUT_OF_BUDGET_DETAIL = "ADVERTISER_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_PAUSED_DETAIL = "ADVERTISER_PAUSED_DETAIL"
    ADVERTISER_PAYMENT_FAILURE_DETAIL = "ADVERTISER_PAYMENT_FAILURE_DETAIL"
    ADVERTISER_POLICING_PENDING_REVIEW_DETAIL = "ADVERTISER_POLICING_PENDING_REVIEW_DETAIL"
    ADVERTISER_POLICING_SUSPENDED_DETAIL = "ADVERTISER_POLICING_SUSPENDED_DETAIL"
    AD_GROUP_ARCHIVED_DETAIL = "AD_GROUP_ARCHIVED_DETAIL"
    AD_GROUP_INCOMPLETE_DETAIL = "AD_GROUP_INCOMPLETE_DETAIL"
    AD_GROUP_LOW_BID_DETAIL = "AD_GROUP_LOW_BID_DETAIL"
    AD_GROUP_PAUSED_DETAIL = "AD_GROUP_PAUSED_DETAIL"
    AD_GROUP_POLICING_CREATIVE_REJECTED_DETAIL = "AD_GROUP_POLICING_CREATIVE_REJECTED_DETAIL"
    AD_GROUP_POLICING_PENDING_REVIEW_DETAIL = "AD_GROUP_POLICING_PENDING_REVIEW_DETAIL"
    AD_GROUP_STATUS_ENABLED_DETAIL = "AD_GROUP_STATUS_ENABLED_DETAIL"
    CAMPAIGN_ARCHIVED_DETAIL = "CAMPAIGN_ARCHIVED_DETAIL"
    CAMPAIGN_INCOMPLETE_DETAIL = "CAMPAIGN_INCOMPLETE_DETAIL"
    CAMPAIGN_OUT_OF_BUDGET_DETAIL = "CAMPAIGN_OUT_OF_BUDGET_DETAIL"
    CAMPAIGN_PAUSED_DETAIL = "CAMPAIGN_PAUSED_DETAIL"
    CAMPAIGN_STATUS_ENABLED_DETAIL = "CAMPAIGN_STATUS_ENABLED_DETAIL"
    ENDED_DETAIL = "ENDED_DETAIL"
    OTHER = "OTHER"
    PENDING_REVIEW_DETAIL = "PENDING_REVIEW_DETAIL"
    PENDING_START_DATE_DETAIL = "PENDING_START_DATE_DETAIL"
    PORTFOLIO_ARCHIVED_DETAIL = "PORTFOLIO_ARCHIVED_DETAIL"
    PORTFOLIO_ENDED_DETAIL = "PORTFOLIO_ENDED_DETAIL"
    PORTFOLIO_OUT_OF_BUDGET_DETAIL = "PORTFOLIO_OUT_OF_BUDGET_DETAIL"
    PORTFOLIO_PAUSED_DETAIL = "PORTFOLIO_PAUSED_DETAIL"
    PORTFOLIO_PENDING_START_DATE_DETAIL = "PORTFOLIO_PENDING_START_DATE_DETAIL"
    PORTFOLIO_STATUS_ENABLED_DETAIL = "PORTFOLIO_STATUS_ENABLED_DETAIL"
    REJECTED_DETAIL = "REJECTED_DETAIL"


class RASv1AdGroupServingStatusDetailItem(BaseModel):
    help_url: Optional[str] = Field(None, alias="helpUrl", description="A URL with additional information about the status identifier.")
    message: Optional[str] = Field(None, description="A human-readable description of the status identifier specified in the name field.")
    name: Optional["RASv1AdGroupServingStatusReason"] = None

    model_config = {'populate_by_name': True}


class RASv1AdGroupServingStatus(StrEnum):
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_POLICING_CREATIVE_REJECTED = "AD_GROUP_POLICING_CREATIVE_REJECTED"
    AD_GROUP_POLICING_PENDING_REVIEW = "AD_GROUP_POLICING_PENDING_REVIEW"
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_STATUS_ENABLED = "CAMPAIGN_STATUS_ENABLED"
    ENDED = "ENDED"
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


class RASv1AdGroupExtendedData(BaseModel):
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="Creation date in ISO 8601.")
    last_update_date_time: Optional[str] = Field(None, alias="lastUpdateDateTime", description="Last updated date in ISO 8601.")
    serving_status: Optional["RASv1AdGroupServingStatus"] = Field(None, alias="servingStatus")
    serving_status_details: Optional[list["RASv1AdGroupServingStatusDetailItem"]] = Field(None, alias="servingStatusDetails", description="The serving status reasons of the AdGroup")

    model_config = {'populate_by_name': True}


class RASv1ParentEntityErrorReason(StrEnum):
    PARENT_ENTITY_NOT_FOUND = "PARENT_ENTITY_NOT_FOUND"


class RASv1ParentEntityError(BaseModel):
    """Errors related to parent entity"""
    cause: Optional["RASv1ErrorCause"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "RASv1ParentEntityErrorReason"

    model_config = {'populate_by_name': True}


class RASv1EntityStateErrorReason(StrEnum):
    ARCHIVED_ENTITY_CANNOT_BE_MODIFIED = "ARCHIVED_ENTITY_CANNOT_BE_MODIFIED"
    PARENT_ARCHIVED_FORBIDS_UPDATES = "PARENT_ARCHIVED_FORBIDS_UPDATES"
    PARENT_ENTITY_FORBIDS_CREATION = "PARENT_ENTITY_FORBIDS_CREATION"
    PARENT_STATUS_FORBIDS_UPDATES_AND_CREATES = "PARENT_STATUS_FORBIDS_UPDATES_AND_CREATES"


class RASv1EntityStateError(BaseModel):
    """entity state update errors"""
    cause: Optional["RASv1ErrorCause"] = None
    marketplace: Optional["RASv1Marketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "RASv1EntityStateErrorReason"

    model_config = {'populate_by_name': True}


class RASv1BiddingErrorReason(StrEnum):
    BID_GT_BUDGET = "BID_GT_BUDGET"
    BID_OUT_OF_MARKET_PLACE_RANGE = "BID_OUT_OF_MARKET_PLACE_RANGE"


class RASv1BiddingError(BaseModel):
    """Errors related to bids"""
    cause: Optional["RASv1ErrorCause"] = None
    lower_limit: Optional[str] = Field(None, alias="lowerLimit")
    marketplace: Optional["RASv1Marketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "RASv1BiddingErrorReason"
    upper_limit: Optional[str] = Field(None, alias="upperLimit")

    model_config = {'populate_by_name': True}


class RASv1DuplicateValueErrorReason(StrEnum):
    DUPLICATE_VALUE = "DUPLICATE_VALUE"


class RASv1DuplicateValueError(BaseModel):
    cause: Optional["RASv1ErrorCause"] = None
    marketplace: Optional["RASv1Marketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "RASv1DuplicateValueErrorReason"

    model_config = {'populate_by_name': True}


class RASv1AdGroupMutationErrorSelector(BaseModel):
    bidding_error: Optional["RASv1BiddingError"] = Field(None, alias="biddingError")
    duplicate_value_error: Optional["RASv1DuplicateValueError"] = Field(None, alias="duplicateValueError")
    entity_not_found_error: Optional["RASv1EntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    entity_state_error: Optional["RASv1EntityStateError"] = Field(None, alias="entityStateError")
    internal_server_error: Optional["RASv1InternalServerError"] = Field(None, alias="internalServerError")
    malformed_value_error: Optional["RASv1MalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["RASv1MissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["RASv1OtherError"] = Field(None, alias="otherError")
    parent_entity_error: Optional["RASv1ParentEntityError"] = Field(None, alias="parentEntityError")
    range_error: Optional["RASv1RangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["RASv1ThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class RASv1AdGroupMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "RASv1AdGroupMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class RASv1AdGroupMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating AdGroup management entities"""
    code: "RASv1InvalidArgumentErrorCode"
    errors: Optional[list["RASv1AdGroupMutationError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class RASv1EntityState(StrEnum):
    ARCHIVED = "ARCHIVED"
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


class RASv1AdGroupOutput(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the AdGroup.")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign.")
    default_bid: float = Field(..., alias="defaultBid", description="A bid value for use when no bid is specified for keywords in the ad group. For more information about bid constraints by")
    extended_data: Optional["RASv1AdGroupExtendedData"] = Field(None, alias="extendedData")
    name: str = Field(..., description="The name of the ad group.")
    retailer_id: str = Field(..., alias="retailerId", description="Id of retailer targeted by the ad group")
    state: "RASv1EntityState"

    model_config = {'populate_by_name': True}


class RASv1AutoMatchType(StrEnum):
    KEYWORDS_CLOSE_MATCH = "KEYWORDS_CLOSE_MATCH"
    KEYWORDS_LOOSE_MATCH = "KEYWORDS_LOOSE_MATCH"
    PRODUCT_COMPLEMENTS = "PRODUCT_COMPLEMENTS"
    PRODUCT_SUBSTITUTES = "PRODUCT_SUBSTITUTES"


class RASv1AutoTarget(BaseModel):
    match_type: "RASv1AutoMatchType" = Field(..., alias="matchType")

    model_config = {'populate_by_name': True}


class RASv1BadGatewayExceptionResponseContent(BaseModel):
    code: Optional[str] = Field(None, description="Error code")
    message: Optional[str] = Field(None, description="Human readable response message")

    model_config = {'populate_by_name': True}


class RASv1BiddingStrategy(StrEnum):
    MANUAL = "MANUAL"


class RASv1BudgetErrorReason(StrEnum):
    BUDGETING_POLICY_INVALID = "BUDGETING_POLICY_INVALID"
    BUDGET_CURRENCY_DOES_NOT_MATCH_MARKETPLACE_SETTINGS = "BUDGET_CURRENCY_DOES_NOT_MATCH_MARKETPLACE_SETTINGS"
    BUDGET_LT_DEFAULT_BIDS = "BUDGET_LT_DEFAULT_BIDS"
    BUDGET_LT_KEYWORD_BIDS = "BUDGET_LT_KEYWORD_BIDS"
    BUDGET_LT_PREDEFINED_TARGET_BIDS = "BUDGET_LT_PREDEFINED_TARGET_BIDS"
    BUDGET_OUT_OF_MARKET_PLACE_RANGE = "BUDGET_OUT_OF_MARKET_PLACE_RANGE"
    BUDGET_TOO_HIGH = "BUDGET_TOO_HIGH"
    BUDGET_TOO_LOW = "BUDGET_TOO_LOW"
    MISSING_BUDGETING_POLICY = "MISSING_BUDGETING_POLICY"
    MISSING_IN_BUDGET_FLAG = "MISSING_IN_BUDGET_FLAG"


class RASv1BudgetError(BaseModel):
    cause: Optional["RASv1ErrorCause"] = None
    lower_limit: Optional[str] = Field(None, alias="lowerLimit")
    message: str = Field(..., description="Human readable error message")
    reason: "RASv1BudgetErrorReason"
    upper_limit: Optional[str] = Field(None, alias="upperLimit")

    model_config = {'populate_by_name': True}


class RASv1BudgetType(StrEnum):
    DAILY = "DAILY"


class RASv1BudgetInput(BaseModel):
    budget: float = Field(..., description="Monetary value")
    budget_type: "RASv1BudgetType" = Field(..., alias="budgetType")

    model_config = {'populate_by_name': True}


class RASv1BudgetOutput(BaseModel):
    budget: float = Field(..., description="Monetary value")
    budget_type: "RASv1BudgetType" = Field(..., alias="budgetType")
    effective_budget: Optional[float] = Field(None, alias="effectiveBudget", description="Monetary value")

    model_config = {'populate_by_name': True}


class RASv1CreateAdGroupOutput(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the AdGroup.")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign.")
    default_bid: float = Field(..., alias="defaultBid", description="A bid value for use when no bid is specified for keywords in the ad group. For more information about bid constraints by")
    name: str = Field(..., description="The name of the ad group.")
    retailer_id: str = Field(..., alias="retailerId", description="Id of retailer targeted by the ad group")
    state: "RASv1EntityState"

    model_config = {'populate_by_name': True}


class RASv1CreateAdGroupSuccessItem(BaseModel):
    ad_group: Optional["RASv1CreateAdGroupOutput"] = Field(None, alias="adGroup")
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="The identifier of the AdGroup.")
    index: int = Field(..., description="The index of the AdGroup in the array from the request body")

    model_config = {'populate_by_name': True}


class RASv1MutateAdGroupFailureItem(BaseModel):
    errors: Optional[list["RASv1AdGroupMutationError"]] = Field(None, description="A list of validation errors")
    index: int = Field(..., description="The index of the AdGroup in the array from the request body")

    model_config = {'populate_by_name': True}


class RASv1BulkCreateAdGroupsOutcomes(BaseModel):
    error: Optional[list["RASv1MutateAdGroupFailureItem"]] = None
    success: Optional[list["RASv1CreateAdGroupSuccessItem"]] = None

    model_config = {'populate_by_name': True}


class RASv1DateErrorReason(StrEnum):
    END_DATE_EARLIER_THAN_TODAY = "END_DATE_EARLIER_THAN_TODAY"
    END_DATE_LATER_THAN_MAXIMUM = "END_DATE_LATER_THAN_MAXIMUM"
    INVALID_DATE = "INVALID_DATE"
    START_DATE_AFTER_END_DATE = "START_DATE_AFTER_END_DATE"
    START_DATE_EARLIER_THAN_TODAY = "START_DATE_EARLIER_THAN_TODAY"
    START_DATE_LATER_THAN_MAXIMUM = "START_DATE_LATER_THAN_MAXIMUM"
    UPDATING_ENDED_CAMPAIGN_WITHOUT_EXTENSION = "UPDATING_ENDED_CAMPAIGN_WITHOUT_EXTENSION"
    UPDATING_READ_ONLY_END_DATE = "UPDATING_READ_ONLY_END_DATE"
    UPDATING_READ_ONLY_START_DATE = "UPDATING_READ_ONLY_START_DATE"


class RASv1DateError(BaseModel):
    cause: Optional["RASv1ErrorCause"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "RASv1DateErrorReason"

    model_config = {'populate_by_name': True}


class RASv1CampaignMutationErrorSelector(BaseModel):
    bidding_error: Optional["RASv1BiddingError"] = Field(None, alias="biddingError")
    budget_error: Optional["RASv1BudgetError"] = Field(None, alias="budgetError")
    date_error: Optional["RASv1DateError"] = Field(None, alias="dateError")
    duplicate_value_error: Optional["RASv1DuplicateValueError"] = Field(None, alias="duplicateValueError")
    entity_not_found_error: Optional["RASv1EntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    entity_state_error: Optional["RASv1EntityStateError"] = Field(None, alias="entityStateError")
    internal_server_error: Optional["RASv1InternalServerError"] = Field(None, alias="internalServerError")
    malformed_value_error: Optional["RASv1MalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["RASv1MissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["RASv1OtherError"] = Field(None, alias="otherError")
    parent_entity_error: Optional["RASv1ParentEntityError"] = Field(None, alias="parentEntityError")
    range_error: Optional["RASv1RangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["RASv1ThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class RASv1CampaignMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "RASv1CampaignMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class RASv1MutateCampaignFailureItem(BaseModel):
    errors: Optional[list["RASv1CampaignMutationError"]] = Field(None, description="A list of validation errors")
    index: int = Field(..., description="The index of the Campaign in the array from the request body")

    model_config = {'populate_by_name': True}


class RASv1Placement(StrEnum):
    PLACEMENT_TOP = "PLACEMENT_TOP"


class RASv1PlacementBidAdjustment(BaseModel):
    percentage: int
    placement: "RASv1Placement"

    model_config = {'populate_by_name': True}


class RASv1RequiredDynamicBidding(BaseModel):
    placement_bidding: Optional[list["RASv1PlacementBidAdjustment"]] = Field(None, alias="placementBidding")
    strategy: "RASv1BiddingStrategy"

    model_config = {'populate_by_name': True}


class RASv1TargetingType(StrEnum):
    AUTO = "AUTO"
    MANUAL = "MANUAL"


class RASv1Tag(BaseModel):
    key: str
    value: str

    model_config = {'populate_by_name': True}


class RASv1CreateCampaignOutput(BaseModel):
    budget: "RASv1BudgetOutput"
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the Campaign.")
    dynamic_bidding: "RASv1RequiredDynamicBidding" = Field(..., alias="dynamicBidding")
    end_date: Optional[str] = Field(None, alias="endDate", description="Campaign end date")
    name: str = Field(..., description="The name of the campaign.")
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="The identifier of an existing portfolio to which the campaign is associated.")
    start_date: str = Field(..., alias="startDate", description="Campaign start date. Default: today&#39;s date. The format of the date is YYYY-MM-DD.")
    state: "RASv1EntityState"
    tags: Optional[list["RASv1Tag"]] = Field(None, description="A list of advertiser-specified custom identifiers for the campaign. Each customer identifier is a key-value pair. You ca")
    targeting_type: "RASv1TargetingType" = Field(..., alias="targetingType")

    model_config = {'populate_by_name': True}


class RASv1CreateCampaignSuccessItem(BaseModel):
    campaign: Optional["RASv1CreateCampaignOutput"] = None
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="The identifier of the Campaign.")
    index: int = Field(..., description="The index of the Campaign in the array from the request body")

    model_config = {'populate_by_name': True}


class RASv1BulkCreateCampaignsOutcomes(BaseModel):
    error: Optional[list["RASv1MutateCampaignFailureItem"]] = None
    success: Optional[list["RASv1CreateCampaignSuccessItem"]] = None

    model_config = {'populate_by_name': True}


class RASv1CreateProductAdOutput(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the ad group.")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign.")
    product_ad_id: str = Field(..., alias="productAdId", description="The identifier of the ProductAd.")
    retailer_id: str = Field(..., alias="retailerId", description="Id of a retailer owning the offer to be advertised")
    retailer_offer_id: str = Field(..., alias="retailerOfferId", description="Id of the offer to be advertised, must belong to retailer identified by retailerId field")
    state: "RASv1EntityState"

    model_config = {'populate_by_name': True}


class RASv1CreateProductAdSuccessItem(BaseModel):
    index: int = Field(..., description="The index of the ProductAd in the array from the request body")
    product_ad: Optional["RASv1CreateProductAdOutput"] = Field(None, alias="productAd")
    product_ad_id: Optional[str] = Field(None, alias="productAdId", description="The identifier of the ProductAd.")

    model_config = {'populate_by_name': True}


class RASv1ProductAdMutationErrorSelector(BaseModel):
    ad_eligibility_error: Optional["RASv1AdEligibilityError"] = Field(None, alias="adEligibilityError")
    duplicate_value_error: Optional["RASv1DuplicateValueError"] = Field(None, alias="duplicateValueError")
    entity_not_found_error: Optional["RASv1EntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    entity_state_error: Optional["RASv1EntityStateError"] = Field(None, alias="entityStateError")
    internal_server_error: Optional["RASv1InternalServerError"] = Field(None, alias="internalServerError")
    malformed_value_error: Optional["RASv1MalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["RASv1MissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["RASv1OtherError"] = Field(None, alias="otherError")
    parent_entity_error: Optional["RASv1ParentEntityError"] = Field(None, alias="parentEntityError")
    range_error: Optional["RASv1RangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["RASv1ThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class RASv1ProductAdMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "RASv1ProductAdMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class RASv1MutateProductAdFailureItem(BaseModel):
    errors: Optional[list["RASv1ProductAdMutationError"]] = Field(None, description="A list of validation errors")
    index: int = Field(..., description="The index of the ProductAd in the array from the request body")

    model_config = {'populate_by_name': True}


class RASv1BulkCreateProductAdsOutcomes(BaseModel):
    error: Optional[list["RASv1MutateProductAdFailureItem"]] = None
    success: Optional[list["RASv1CreateProductAdSuccessItem"]] = None

    model_config = {'populate_by_name': True}


class RASv1TargetingClauseSetupErrorReason(StrEnum):
    AUTO_TARGETING_CLAUSE_CANNOT_BE_CREATED_MANUALLY = "AUTO_TARGETING_CLAUSE_CANNOT_BE_CREATED_MANUALLY"
    TARGETING_EXPRESSION_INVALID_VALUE = "TARGETING_EXPRESSION_INVALID_VALUE"
    TARGETING_TYPE_NOT_ALLOWED_FOR_AUTO_TARGETING_CAMPAIGN = "TARGETING_TYPE_NOT_ALLOWED_FOR_AUTO_TARGETING_CAMPAIGN"
    TYPE_CONFLICT_IN_AD_GROUP = "TYPE_CONFLICT_IN_AD_GROUP"


class RASv1TargetingClauseSetupError(BaseModel):
    """Errors related to targeting clause setup"""
    cause: Optional["RASv1ErrorCause"] = None
    marketplace: Optional["RASv1Marketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "RASv1TargetingClauseSetupErrorReason"

    model_config = {'populate_by_name': True}


class RASv1TargetMutationErrorSelector(BaseModel):
    duplicate_value_error: Optional["RASv1DuplicateValueError"] = Field(None, alias="duplicateValueError")
    entity_not_found_error: Optional["RASv1EntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    entity_state_error: Optional["RASv1EntityStateError"] = Field(None, alias="entityStateError")
    internal_server_error: Optional["RASv1InternalServerError"] = Field(None, alias="internalServerError")
    malformed_value_error: Optional["RASv1MalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["RASv1MissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["RASv1OtherError"] = Field(None, alias="otherError")
    parent_entity_error: Optional["RASv1ParentEntityError"] = Field(None, alias="parentEntityError")
    range_error: Optional["RASv1RangeError"] = Field(None, alias="rangeError")
    targeting_clause_setup_error: Optional["RASv1TargetingClauseSetupError"] = Field(None, alias="targetingClauseSetupError")
    throttled_error: Optional["RASv1ThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class RASv1TargetMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "RASv1TargetMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class RASv1MutateTargetFailureItem(BaseModel):
    errors: Optional[list["RASv1TargetMutationError"]] = Field(None, description="A list of validation errors")
    index: int = Field(..., description="The index of the Target in the array from the request body")

    model_config = {'populate_by_name': True}


class RASv1TargetType(StrEnum):
    AUTO = "AUTO"
    KEYWORD = "KEYWORD"
    PRODUCT = "PRODUCT"


class RASv1TargetLevel(StrEnum):
    AD_GROUP = "AD_GROUP"
    CAMPAIGN = "CAMPAIGN"


class RASv1KeywordMatchType(StrEnum):
    BROAD = "BROAD"
    EXACT = "EXACT"
    PHRASE = "PHRASE"


class RASv1KeywordTarget(BaseModel):
    keyword: str
    match_type: "RASv1KeywordMatchType" = Field(..., alias="matchType")

    model_config = {'populate_by_name': True}


class RASv1ProductMatchType(StrEnum):
    PRODUCT_EXACT = "PRODUCT_EXACT"


class RASv1ProductIdType(StrEnum):
    RETAILER_OFFER = "RETAILER_OFFER"


class RASv1ProductTarget(BaseModel):
    match_type: "RASv1ProductMatchType" = Field(..., alias="matchType")
    product_id: str = Field(..., alias="productId", description="Resource identifier")
    product_id_type: "RASv1ProductIdType" = Field(..., alias="productIdType")
    retailer_id: Optional[str] = Field(None, alias="retailerId", description="Resource identifier")

    model_config = {'populate_by_name': True}


class RASv1TargetDetails(BaseModel):
    auto_target: Optional["RASv1AutoTarget"] = Field(None, alias="autoTarget")
    keyword_target: Optional["RASv1KeywordTarget"] = Field(None, alias="keywordTarget")
    product_target: Optional["RASv1ProductTarget"] = Field(None, alias="productTarget")

    model_config = {'populate_by_name': True}


class RASv1CurrencyCode(StrEnum):
    USD = "USD"


class RASv1TargetBidOutput(BaseModel):
    bid: float = Field(..., description="The maximum bid for a target.")
    currency_code: "RASv1CurrencyCode" = Field(..., alias="currencyCode")

    model_config = {'populate_by_name': True}


class RASv1CreateTargetOutput(BaseModel):
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="The identifier of the ad group.")
    bid: Optional["RASv1TargetBidOutput"] = None
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign.")
    negative: bool = Field(..., description="Indicates whether the target is negative or not.")
    state: "RASv1EntityState"
    target_details: "RASv1TargetDetails" = Field(..., alias="targetDetails")
    target_id: str = Field(..., alias="targetId", description="The identifier of the Target.")
    target_level: "RASv1TargetLevel" = Field(..., alias="targetLevel")
    target_type: "RASv1TargetType" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class RASv1CreateTargetSuccessItem(BaseModel):
    index: int = Field(..., description="The index of the Target in the array from the request body")
    target: Optional["RASv1CreateTargetOutput"] = None
    target_id: Optional[str] = Field(None, alias="targetId", description="The identifier of the Target.")

    model_config = {'populate_by_name': True}


class RASv1BulkCreateTargetsOutcomes(BaseModel):
    error: Optional[list["RASv1MutateTargetFailureItem"]] = None
    success: Optional[list["RASv1CreateTargetSuccessItem"]] = None

    model_config = {'populate_by_name': True}


class RASv1MutateAdGroupSuccessItem(BaseModel):
    ad_group: Optional["RASv1AdGroupOutput"] = Field(None, alias="adGroup")
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="The identifier of the AdGroup.")
    index: int = Field(..., description="The index of the AdGroup in the array from the request body")

    model_config = {'populate_by_name': True}


class RASv1BulkMutateAdGroupsOutcomes(BaseModel):
    error: Optional[list["RASv1MutateAdGroupFailureItem"]] = None
    success: Optional[list["RASv1MutateAdGroupSuccessItem"]] = None

    model_config = {'populate_by_name': True}


class RASv1CampaignServingStatus(StrEnum):
    ACCOUNT_OUT_OF_BUDGET = "ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_STATUS_ENABLED = "CAMPAIGN_STATUS_ENABLED"
    ENDED = "ENDED"
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


class RASv1CampaignServingStatusReason(StrEnum):
    ACCOUNT_OUT_OF_BUDGET_DETAIL = "ACCOUNT_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_ARCHIVED_DETAIL = "ADVERTISER_ARCHIVED_DETAIL"
    ADVERTISER_OUT_OF_BUDGET_DETAIL = "ADVERTISER_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_PAUSED_DETAIL = "ADVERTISER_PAUSED_DETAIL"
    ADVERTISER_PAYMENT_FAILURE_DETAIL = "ADVERTISER_PAYMENT_FAILURE_DETAIL"
    ADVERTISER_POLICING_PENDING_REVIEW_DETAIL = "ADVERTISER_POLICING_PENDING_REVIEW_DETAIL"
    ADVERTISER_POLICING_SUSPENDED_DETAIL = "ADVERTISER_POLICING_SUSPENDED_DETAIL"
    CAMPAIGN_ARCHIVED_DETAIL = "CAMPAIGN_ARCHIVED_DETAIL"
    CAMPAIGN_INCOMPLETE_DETAIL = "CAMPAIGN_INCOMPLETE_DETAIL"
    CAMPAIGN_OUT_OF_BUDGET_DETAIL = "CAMPAIGN_OUT_OF_BUDGET_DETAIL"
    CAMPAIGN_PAUSED_DETAIL = "CAMPAIGN_PAUSED_DETAIL"
    CAMPAIGN_STATUS_ENABLED_DETAIL = "CAMPAIGN_STATUS_ENABLED_DETAIL"
    ENDED_DETAIL = "ENDED_DETAIL"
    OTHER = "OTHER"
    PENDING_REVIEW_DETAIL = "PENDING_REVIEW_DETAIL"
    PENDING_START_DATE_DETAIL = "PENDING_START_DATE_DETAIL"
    PORTFOLIO_ARCHIVED_DETAIL = "PORTFOLIO_ARCHIVED_DETAIL"
    PORTFOLIO_ENDED_DETAIL = "PORTFOLIO_ENDED_DETAIL"
    PORTFOLIO_OUT_OF_BUDGET_DETAIL = "PORTFOLIO_OUT_OF_BUDGET_DETAIL"
    PORTFOLIO_PAUSED_DETAIL = "PORTFOLIO_PAUSED_DETAIL"
    PORTFOLIO_PENDING_START_DATE_DETAIL = "PORTFOLIO_PENDING_START_DATE_DETAIL"
    PORTFOLIO_STATUS_ENABLED_DETAIL = "PORTFOLIO_STATUS_ENABLED_DETAIL"
    REJECTED_DETAIL = "REJECTED_DETAIL"


class RASv1CampaignServingStatusDetailItem(BaseModel):
    help_url: Optional[str] = Field(None, alias="helpUrl", description="A URL with additional information about the status identifier.")
    message: Optional[str] = Field(None, description="A human-readable description of the status identifier specified in the name field.")
    name: Optional["RASv1CampaignServingStatusReason"] = None

    model_config = {'populate_by_name': True}


class RASv1CampaignExtendedData(BaseModel):
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="Creation date in ISO 8601.")
    last_update_date_time: Optional[str] = Field(None, alias="lastUpdateDateTime", description="Last updated date in ISO 8601.")
    serving_status: Optional["RASv1CampaignServingStatus"] = Field(None, alias="servingStatus")
    serving_status_details: Optional[list["RASv1CampaignServingStatusDetailItem"]] = Field(None, alias="servingStatusDetails", description="The serving status reasons of the Campaign")

    model_config = {'populate_by_name': True}


class RASv1CampaignOutput(BaseModel):
    budget: "RASv1BudgetOutput"
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the Campaign.")
    dynamic_bidding: "RASv1RequiredDynamicBidding" = Field(..., alias="dynamicBidding")
    end_date: Optional[str] = Field(None, alias="endDate", description="Campaign end date")
    extended_data: Optional["RASv1CampaignExtendedData"] = Field(None, alias="extendedData")
    name: str = Field(..., description="The name of the campaign.")
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="The identifier of an existing portfolio to which the campaign is associated.")
    start_date: str = Field(..., alias="startDate", description="Campaign start date. Default: today&#39;s date. The format of the date is YYYY-MM-DD.")
    state: "RASv1EntityState"
    tags: Optional[list["RASv1Tag"]] = Field(None, description="A list of advertiser-specified custom identifiers for the campaign. Each customer identifier is a key-value pair. You ca")
    targeting_type: "RASv1TargetingType" = Field(..., alias="targetingType")

    model_config = {'populate_by_name': True}


class RASv1MutateCampaignSuccessItem(BaseModel):
    campaign: Optional["RASv1CampaignOutput"] = None
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="The identifier of the Campaign.")
    index: int = Field(..., description="The index of the Campaign in the array from the request body")

    model_config = {'populate_by_name': True}


class RASv1BulkMutateCampaignsOutcomes(BaseModel):
    error: Optional[list["RASv1MutateCampaignFailureItem"]] = None
    success: Optional[list["RASv1MutateCampaignSuccessItem"]] = None

    model_config = {'populate_by_name': True}


class RASv1ProductAdServingStatus(StrEnum):
    ACCOUNT_OUT_OF_BUDGET = "ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    AD_ARCHIVED = "AD_ARCHIVED"
    AD_CREATION_FAILED = "AD_CREATION_FAILED"
    AD_CREATION_OFFLINE_FAILED = "AD_CREATION_OFFLINE_FAILED"
    AD_CREATION_OFFLINE_IN_PROGRESS = "AD_CREATION_OFFLINE_IN_PROGRESS"
    AD_CREATION_OFFLINE_PENDING = "AD_CREATION_OFFLINE_PENDING"
    AD_ELIGIBLE = "AD_ELIGIBLE"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_POLICING_CREATIVE_REJECTED = "AD_GROUP_POLICING_CREATIVE_REJECTED"
    AD_GROUP_POLICING_PENDING_REVIEW = "AD_GROUP_POLICING_PENDING_REVIEW"
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    AD_INELIGIBLE = "AD_INELIGIBLE"
    AD_LANDING_PAGE_NOT_AVAILABLE = "AD_LANDING_PAGE_NOT_AVAILABLE"
    AD_MISSING_DECORATION = "AD_MISSING_DECORATION"
    AD_MISSING_IMAGE = "AD_MISSING_IMAGE"
    AD_NOT_BUYABLE = "AD_NOT_BUYABLE"
    AD_NOT_IN_BUYBOX = "AD_NOT_IN_BUYBOX"
    AD_NO_PURCHASABLE_OFFER = "AD_NO_PURCHASABLE_OFFER"
    AD_OUT_OF_STOCK = "AD_OUT_OF_STOCK"
    AD_PAUSED = "AD_PAUSED"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    AD_POLICING_SUSPENDED = "AD_POLICING_SUSPENDED"
    AD_STATUS_LIVE = "AD_STATUS_LIVE"
    CAMPAIGN_ADS_NOT_DELIVERING = "CAMPAIGN_ADS_NOT_DELIVERING"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_ENDED = "CAMPAIGN_ENDED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_PENDING_START_DATE = "CAMPAIGN_PENDING_START_DATE"
    CAMPAIGN_STATUS_ENABLED = "CAMPAIGN_STATUS_ENABLED"
    ELIGIBLE = "ELIGIBLE"
    ENDED = "ENDED"
    INELIGIBLE = "INELIGIBLE"
    LANDING_PAGE_NOT_AVAILABLE = "LANDING_PAGE_NOT_AVAILABLE"
    MISSING_DECORATION = "MISSING_DECORATION"
    MISSING_IMAGE = "MISSING_IMAGE"
    NOT_BUYABLE = "NOT_BUYABLE"
    NOT_IN_BUYBOX = "NOT_IN_BUYBOX"
    NO_INVENTORY = "NO_INVENTORY"
    NO_PURCHASABLE_OFFER = "NO_PURCHASABLE_OFFER"
    OTHER = "OTHER"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    PENDING_REVIEW = "PENDING_REVIEW"
    PENDING_START_DATE = "PENDING_START_DATE"
    PIR_RULE_EXCLUDED = "PIR_RULE_EXCLUDED"
    PORTFOLIO_ARCHIVED = "PORTFOLIO_ARCHIVED"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    PORTFOLIO_PAUSED = "PORTFOLIO_PAUSED"
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"
    PORTFOLIO_STATUS_ENABLED = "PORTFOLIO_STATUS_ENABLED"
    REJECTED = "REJECTED"
    SECURITY_SCAN_PENDING_REVIEW = "SECURITY_SCAN_PENDING_REVIEW"
    SECURITY_SCAN_REJECTED = "SECURITY_SCAN_REJECTED"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"
    TARGETING_CLAUSE_ARCHIVED = "TARGETING_CLAUSE_ARCHIVED"
    TARGETING_CLAUSE_BLOCKED = "TARGETING_CLAUSE_BLOCKED"
    TARGETING_CLAUSE_PAUSED = "TARGETING_CLAUSE_PAUSED"
    TARGETING_CLAUSE_POLICING_SUSPENDED = "TARGETING_CLAUSE_POLICING_SUSPENDED"
    TARGETING_CLAUSE_STATUS_LIVE = "TARGETING_CLAUSE_STATUS_LIVE"


class RASv1ProductAdServingStatusReason(StrEnum):
    ACCOUNT_OUT_OF_BUDGET_DETAIL = "ACCOUNT_OUT_OF_BUDGET_DETAIL"
    ADULT_PRODUCT = "ADULT_PRODUCT"
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET_DETAIL = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_ARCHIVED_DETAIL = "ADVERTISER_ARCHIVED_DETAIL"
    ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL = "ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL"
    ADVERTISER_OUT_OF_BUDGET_DETAIL = "ADVERTISER_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_PAUSED_DETAIL = "ADVERTISER_PAUSED_DETAIL"
    ADVERTISER_PAYMENT_FAILURE_DETAIL = "ADVERTISER_PAYMENT_FAILURE_DETAIL"
    ADVERTISER_POLICING_PENDING_REVIEW_DETAIL = "ADVERTISER_POLICING_PENDING_REVIEW_DETAIL"
    ADVERTISER_POLICING_SUSPENDED_DETAIL = "ADVERTISER_POLICING_SUSPENDED_DETAIL"
    ADVERTISER_STATUS_ENABLED_DETAIL = "ADVERTISER_STATUS_ENABLED_DETAIL"
    AD_ARCHIVED_DETAIL = "AD_ARCHIVED_DETAIL"
    AD_CREATION_OFFLINE_FAILED = "AD_CREATION_OFFLINE_FAILED"
    AD_CREATION_OFFLINE_IN_PROGRESS = "AD_CREATION_OFFLINE_IN_PROGRESS"
    AD_CREATION_OFFLINE_PENDING = "AD_CREATION_OFFLINE_PENDING"
    AD_GROUP_ARCHIVED_DETAIL = "AD_GROUP_ARCHIVED_DETAIL"
    AD_GROUP_INCOMPLETE_DETAIL = "AD_GROUP_INCOMPLETE_DETAIL"
    AD_GROUP_LOW_BID_DETAIL = "AD_GROUP_LOW_BID_DETAIL"
    AD_GROUP_PAUSED_DETAIL = "AD_GROUP_PAUSED_DETAIL"
    AD_GROUP_POLICING_CREATIVE_REJECTED_DETAIL = "AD_GROUP_POLICING_CREATIVE_REJECTED_DETAIL"
    AD_GROUP_POLICING_PENDING_REVIEW_DETAIL = "AD_GROUP_POLICING_PENDING_REVIEW_DETAIL"
    AD_GROUP_STATUS_ENABLED_DETAIL = "AD_GROUP_STATUS_ENABLED_DETAIL"
    AD_PAUSED_DETAIL = "AD_PAUSED_DETAIL"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    AD_POLICING_PENDING_REVIEW_DETAIL = "AD_POLICING_PENDING_REVIEW_DETAIL"
    AD_POLICING_SUSPENDED_DETAIL = "AD_POLICING_SUSPENDED_DETAIL"
    AD_STATUS_LIVE_DETAIL = "AD_STATUS_LIVE_DETAIL"
    BRAND_REMOVED = "BRAND_REMOVED"
    CAMPAIGN_ADS_NOT_DELIVERING_DETAIL = "CAMPAIGN_ADS_NOT_DELIVERING_DETAIL"
    CAMPAIGN_ARCHIVED_DETAIL = "CAMPAIGN_ARCHIVED_DETAIL"
    CAMPAIGN_INCOMPLETE_DETAIL = "CAMPAIGN_INCOMPLETE_DETAIL"
    CAMPAIGN_OUT_OF_BUDGET_DETAIL = "CAMPAIGN_OUT_OF_BUDGET_DETAIL"
    CAMPAIGN_PAUSED_DETAIL = "CAMPAIGN_PAUSED_DETAIL"
    CAMPAIGN_STATUS_ENABLED_DETAIL = "CAMPAIGN_STATUS_ENABLED_DETAIL"
    CBA_NOT_SUPPORTED = "CBA_NOT_SUPPORTED"
    CLOSED_GL = "CLOSED_GL"
    CP_INELIGIBLE = "CP_INELIGIBLE"
    CP_INELIGIBLE_ASIN = "CP_INELIGIBLE_ASIN"
    CP_INELIGIBLE_UNKNOWN = "CP_INELIGIBLE_UNKNOWN"
    CP_INELIGIBLE_VENDOR = "CP_INELIGIBLE_VENDOR"
    ELIGIBLE_DETAIL = "ELIGIBLE_DETAIL"
    ENDED_DETAIL = "ENDED_DETAIL"
    INELIGIBLE_CONDITION = "INELIGIBLE_CONDITION"
    INVENTORY_INCOMPLETE = "INVENTORY_INCOMPLETE"
    ITEM_MISSING = "ITEM_MISSING"
    LANDING_PAGE_INELIGIBLE = "LANDING_PAGE_INELIGIBLE"
    LANDING_PAGE_NOT_AVAILABLE_DETAIL = "LANDING_PAGE_NOT_AVAILABLE_DETAIL"
    MISSING_DECORATION_DETAIL = "MISSING_DECORATION_DETAIL"
    MISSING_IMAGE_DETAIL = "MISSING_IMAGE_DETAIL"
    MODERATION_ADULT_NOVELTY_PV_DETAIL = "MODERATION_ADULT_NOVELTY_PV_DETAIL"
    MODERATION_ADULT_PRODUCT_PV_DETAIL = "MODERATION_ADULT_PRODUCT_PV_DETAIL"
    MODERATION_ADULT_SOFTLINES_PV_DETAIL = "MODERATION_ADULT_SOFTLINES_PV_DETAIL"
    MODERATION_CLAIM_WEIGHTLOSS_PV_DETAIL = "MODERATION_CLAIM_WEIGHTLOSS_PV_DETAIL"
    MODERATION_CONTENT_NUDITY_PV_DETAIL = "MODERATION_CONTENT_NUDITY_PV_DETAIL"
    MODERATION_CONTENT_PROVOCATIVE_PV_DETAIL = "MODERATION_CONTENT_PROVOCATIVE_PV_DETAIL"
    MODERATION_CONTENT_SMOKING_PV_DETAIL = "MODERATION_CONTENT_SMOKING_PV_DETAIL"
    MODERATION_CRITICAL_EVENTS_PV_DETAIL = "MODERATION_CRITICAL_EVENTS_PV_DETAIL"
    MODERATION_ERROR_404_PV_DETAIL = "MODERATION_ERROR_404_PV_DETAIL"
    MODERATION_GRAPHICAL_SEXUAL_IMAGES_PV_DETAIL = "MODERATION_GRAPHICAL_SEXUAL_IMAGES_PV_DETAIL"
    MODERATION_HFSS_PRODUCT_PV_DETAIL = "MODERATION_HFSS_PRODUCT_PV_DETAIL"
    MODERATION_LANGUAGE_OFFENSIVE_PV_DETAIL = "MODERATION_LANGUAGE_OFFENSIVE_PV_DETAIL"
    MODERATION_NOT_COMPLIANT_TO_AD_POLICY_PV_DETAIL = "MODERATION_NOT_COMPLIANT_TO_AD_POLICY_PV_DETAIL"
    MODERATION_SMOKING_RELATED_PV_DETAIL = "MODERATION_SMOKING_RELATED_PV_DETAIL"
    NOT_BUYABLE_DETAIL = "NOT_BUYABLE_DETAIL"
    NOT_IN_BUYBOX_DETAIL = "NOT_IN_BUYBOX_DETAIL"
    NO_INVENTORY_DETAIL = "NO_INVENTORY_DETAIL"
    NO_PURCHASABLE_OFFER_DETAIL = "NO_PURCHASABLE_OFFER_DETAIL"
    OFFER_MISSING_DETAIL = "OFFER_MISSING_DETAIL"
    OTHER = "OTHER"
    OUT_OF_STOCK_DETAIL = "OUT_OF_STOCK_DETAIL"
    PENDING_REVIEW_DETAIL = "PENDING_REVIEW_DETAIL"
    PENDING_START_DATE_DETAIL = "PENDING_START_DATE_DETAIL"
    PIR_RULE_EXCLUDED = "PIR_RULE_EXCLUDED"
    PORTFOLIO_ARCHIVED_DETAIL = "PORTFOLIO_ARCHIVED_DETAIL"
    PORTFOLIO_ENDED_DETAIL = "PORTFOLIO_ENDED_DETAIL"
    PORTFOLIO_OUT_OF_BUDGET_DETAIL = "PORTFOLIO_OUT_OF_BUDGET_DETAIL"
    PORTFOLIO_PAUSED_DETAIL = "PORTFOLIO_PAUSED_DETAIL"
    PORTFOLIO_PENDING_START_DATE_DETAIL = "PORTFOLIO_PENDING_START_DATE_DETAIL"
    PORTFOLIO_STATUS_ENABLED_DETAIL = "PORTFOLIO_STATUS_ENABLED_DETAIL"
    REJECTED_DETAIL = "REJECTED_DETAIL"
    RESTRICTED_GL = "RESTRICTED_GL"
    SECURITY_SCAN_PENDING_REVIEW = "SECURITY_SCAN_PENDING_REVIEW"
    SECURITY_SCAN_REJECTED = "SECURITY_SCAN_REJECTED"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"
    TARGETING_CLAUSE_ARCHIVED_DETAIL = "TARGETING_CLAUSE_ARCHIVED_DETAIL"
    TARGETING_CLAUSE_BLOCKED_DETAIL = "TARGETING_CLAUSE_BLOCKED_DETAIL"
    TARGETING_CLAUSE_PAUSED_DETAIL = "TARGETING_CLAUSE_PAUSED_DETAIL"
    TARGETING_CLAUSE_POLICING_SUSPENDED_DETAIL = "TARGETING_CLAUSE_POLICING_SUSPENDED_DETAIL"
    TARGETING_CLAUSE_STATUS_LIVE_DETAIL = "TARGETING_CLAUSE_STATUS_LIVE_DETAIL"
    VARIATION_PARENT = "VARIATION_PARENT"


class RASv1ProductAdServingStatusDetailItem(BaseModel):
    help_url: Optional[str] = Field(None, alias="helpUrl", description="A URL with additional information about the status identifier.")
    message: Optional[str] = Field(None, description="A human-readable description of the status identifier specified in the name field.")
    name: Optional["RASv1ProductAdServingStatusReason"] = None

    model_config = {'populate_by_name': True}


class RASv1ProductAdExtendedData(BaseModel):
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="Creation date in ISO 8601.")
    last_update_date_time: Optional[str] = Field(None, alias="lastUpdateDateTime", description="Last updated date in ISO 8601.")
    serving_status: Optional["RASv1ProductAdServingStatus"] = Field(None, alias="servingStatus")
    serving_status_details: Optional[list["RASv1ProductAdServingStatusDetailItem"]] = Field(None, alias="servingStatusDetails", description="The serving status reasons of the ProductAd")

    model_config = {'populate_by_name': True}


class RASv1ProductAdOutput(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the ad group.")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign.")
    extended_data: Optional["RASv1ProductAdExtendedData"] = Field(None, alias="extendedData")
    product_ad_id: str = Field(..., alias="productAdId", description="The identifier of the ProductAd.")
    retailer_id: str = Field(..., alias="retailerId", description="Id of a retailer owning the offer to be advertised")
    retailer_offer_id: str = Field(..., alias="retailerOfferId", description="Id of the offer to be advertised, must belong to retailer identified by retailerId field")
    state: "RASv1EntityState"

    model_config = {'populate_by_name': True}


class RASv1MutateProductAdSuccessItem(BaseModel):
    index: int = Field(..., description="The index of the ProductAd in the array from the request body")
    product_ad: Optional["RASv1ProductAdOutput"] = Field(None, alias="productAd")
    product_ad_id: Optional[str] = Field(None, alias="productAdId", description="The identifier of the ProductAd.")

    model_config = {'populate_by_name': True}


class RASv1BulkMutateProductAdsOutcomes(BaseModel):
    error: Optional[list["RASv1MutateProductAdFailureItem"]] = None
    success: Optional[list["RASv1MutateProductAdSuccessItem"]] = None

    model_config = {'populate_by_name': True}


class RASv1TargetServingStatusReason(StrEnum):
    ACCOUNT_OUT_OF_BUDGET_DETAIL = "ACCOUNT_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_ARCHIVED_DETAIL = "ADVERTISER_ARCHIVED_DETAIL"
    ADVERTISER_OUT_OF_BUDGET_DETAIL = "ADVERTISER_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_PAUSED_DETAIL = "ADVERTISER_PAUSED_DETAIL"
    ADVERTISER_PAYMENT_FAILURE_DETAIL = "ADVERTISER_PAYMENT_FAILURE_DETAIL"
    ADVERTISER_POLICING_PENDING_REVIEW_DETAIL = "ADVERTISER_POLICING_PENDING_REVIEW_DETAIL"
    ADVERTISER_POLICING_SUSPENDED_DETAIL = "ADVERTISER_POLICING_SUSPENDED_DETAIL"
    AD_GROUP_ARCHIVED_DETAIL = "AD_GROUP_ARCHIVED_DETAIL"
    AD_GROUP_INCOMPLETE_DETAIL = "AD_GROUP_INCOMPLETE_DETAIL"
    AD_GROUP_LOW_BID_DETAIL = "AD_GROUP_LOW_BID_DETAIL"
    AD_GROUP_PAUSED_DETAIL = "AD_GROUP_PAUSED_DETAIL"
    AD_GROUP_POLICING_CREATIVE_REJECTED_DETAIL = "AD_GROUP_POLICING_CREATIVE_REJECTED_DETAIL"
    AD_GROUP_POLICING_PENDING_REVIEW_DETAIL = "AD_GROUP_POLICING_PENDING_REVIEW_DETAIL"
    AD_GROUP_STATUS_ENABLED_DETAIL = "AD_GROUP_STATUS_ENABLED_DETAIL"
    CAMPAIGN_ARCHIVED_DETAIL = "CAMPAIGN_ARCHIVED_DETAIL"
    CAMPAIGN_INCOMPLETE_DETAIL = "CAMPAIGN_INCOMPLETE_DETAIL"
    CAMPAIGN_OUT_OF_BUDGET_DETAIL = "CAMPAIGN_OUT_OF_BUDGET_DETAIL"
    CAMPAIGN_PAUSED_DETAIL = "CAMPAIGN_PAUSED_DETAIL"
    CAMPAIGN_STATUS_ENABLED_DETAIL = "CAMPAIGN_STATUS_ENABLED_DETAIL"
    ENDED_DETAIL = "ENDED_DETAIL"
    OTHER = "OTHER"
    PENDING_REVIEW_DETAIL = "PENDING_REVIEW_DETAIL"
    PENDING_START_DATE_DETAIL = "PENDING_START_DATE_DETAIL"
    PORTFOLIO_ARCHIVED_DETAIL = "PORTFOLIO_ARCHIVED_DETAIL"
    PORTFOLIO_ENDED_DETAIL = "PORTFOLIO_ENDED_DETAIL"
    PORTFOLIO_OUT_OF_BUDGET_DETAIL = "PORTFOLIO_OUT_OF_BUDGET_DETAIL"
    PORTFOLIO_PAUSED_DETAIL = "PORTFOLIO_PAUSED_DETAIL"
    PORTFOLIO_PENDING_START_DATE_DETAIL = "PORTFOLIO_PENDING_START_DATE_DETAIL"
    PORTFOLIO_STATUS_ENABLED_DETAIL = "PORTFOLIO_STATUS_ENABLED_DETAIL"
    REJECTED_DETAIL = "REJECTED_DETAIL"
    TARGETING_CLAUSE_ARCHIVED_DETAIL = "TARGETING_CLAUSE_ARCHIVED_DETAIL"
    TARGETING_CLAUSE_BLOCKED_DETAIL = "TARGETING_CLAUSE_BLOCKED_DETAIL"
    TARGETING_CLAUSE_PAUSED_DETAIL = "TARGETING_CLAUSE_PAUSED_DETAIL"
    TARGETING_CLAUSE_POLICING_SUSPENDED_DETAIL = "TARGETING_CLAUSE_POLICING_SUSPENDED_DETAIL"
    TARGETING_CLAUSE_STATUS_LIVE_DETAIL = "TARGETING_CLAUSE_STATUS_LIVE_DETAIL"


class RASv1TargetServingStatusDetailItem(BaseModel):
    help_url: Optional[str] = Field(None, alias="helpUrl", description="A URL with additional information about the status identifier.")
    message: Optional[str] = Field(None, description="A human-readable description of the status identifier specified in the name field.")
    name: Optional["RASv1TargetServingStatusReason"] = None

    model_config = {'populate_by_name': True}


class RASv1TargetServingStatus(StrEnum):
    ACCOUNT_OUT_OF_BUDGET = "ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_POLICING_CREATIVE_REJECTED = "AD_GROUP_POLICING_CREATIVE_REJECTED"
    AD_GROUP_POLICING_PENDING_REVIEW = "AD_GROUP_POLICING_PENDING_REVIEW"
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_STATUS_ENABLED = "CAMPAIGN_STATUS_ENABLED"
    ENDED = "ENDED"
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
    TARGETING_CLAUSE_ARCHIVED = "TARGETING_CLAUSE_ARCHIVED"
    TARGETING_CLAUSE_BLOCKED = "TARGETING_CLAUSE_BLOCKED"
    TARGETING_CLAUSE_PAUSED = "TARGETING_CLAUSE_PAUSED"
    TARGETING_CLAUSE_POLICING_SUSPENDED = "TARGETING_CLAUSE_POLICING_SUSPENDED"
    TARGETING_CLAUSE_STATUS_LIVE = "TARGETING_CLAUSE_STATUS_LIVE"


class RASv1TargetExtendedData(BaseModel):
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="Creation date in ISO 8601.")
    last_update_date_time: Optional[str] = Field(None, alias="lastUpdateDateTime", description="Last updated date in ISO 8601.")
    serving_status: Optional["RASv1TargetServingStatus"] = Field(None, alias="servingStatus")
    serving_status_details: Optional[list["RASv1TargetServingStatusDetailItem"]] = Field(None, alias="servingStatusDetails", description="The serving status reasons of the Target")

    model_config = {'populate_by_name': True}


class RASv1TargetOutput(BaseModel):
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="The identifier of the ad group.")
    bid: Optional["RASv1TargetBidOutput"] = None
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign.")
    extended_data: Optional["RASv1TargetExtendedData"] = Field(None, alias="extendedData")
    negative: bool = Field(..., description="Indicates whether the target is negative or not.")
    state: "RASv1EntityState"
    target_details: "RASv1TargetDetails" = Field(..., alias="targetDetails")
    target_id: str = Field(..., alias="targetId", description="The identifier of the Target.")
    target_level: "RASv1TargetLevel" = Field(..., alias="targetLevel")
    target_type: "RASv1TargetType" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class RASv1MutateTargetSuccessItem(BaseModel):
    index: int = Field(..., description="The index of the Target in the array from the request body")
    target: Optional["RASv1TargetOutput"] = None
    target_id: Optional[str] = Field(None, alias="targetId", description="The identifier of the Target.")

    model_config = {'populate_by_name': True}


class RASv1BulkMutateTargetsOutcomes(BaseModel):
    error: Optional[list["RASv1MutateTargetFailureItem"]] = None
    success: Optional[list["RASv1MutateTargetSuccessItem"]] = None

    model_config = {'populate_by_name': True}


class RASv1CampaignAccessErrorSelector(BaseModel):
    date_error: Optional["RASv1DateError"] = Field(None, alias="dateError")
    entity_not_found_error: Optional["RASv1EntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    internal_server_error: Optional["RASv1InternalServerError"] = Field(None, alias="internalServerError")
    malformed_value_error: Optional["RASv1MalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["RASv1MissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["RASv1OtherError"] = Field(None, alias="otherError")
    range_error: Optional["RASv1RangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["RASv1ThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class RASv1CampaignAccessError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "RASv1CampaignAccessErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class RASv1CampaignAccessExceptionResponseContent(BaseModel):
    """Exception resulting in accessing ad group entities"""
    code: "RASv1InvalidArgumentErrorCode"
    errors: Optional[list["RASv1CampaignAccessError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class RASv1CampaignMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating Campaign management entities"""
    code: "RASv1InvalidArgumentErrorCode"
    errors: Optional[list["RASv1CampaignMutationError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class RASv1CreateAdGroupInput(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign.")
    default_bid: float = Field(..., alias="defaultBid", description="A bid value for use when no bid is specified for keywords in the ad group. For more information about bid constraints by")
    name: str = Field(..., description="The name of the ad group.")
    retailer_id: str = Field(..., alias="retailerId", description="Id of retailer targeted by the ad group")
    state: "RASv1EntityState"

    model_config = {'populate_by_name': True}


class RASv1CreateAdGroupsRequestContent(BaseModel):
    ad_groups: list["RASv1CreateAdGroupInput"] = Field(..., alias="adGroups", description="List of AdGroups to create")

    model_config = {'populate_by_name': True}


class RASv1CreateAdGroupsResponseContent(BaseModel):
    ad_groups: "RASv1BulkCreateAdGroupsOutcomes" = Field(..., alias="adGroups")

    model_config = {'populate_by_name': True}


class RASv1CreateCampaignInput(BaseModel):
    budget: "RASv1BudgetInput"
    dynamic_bidding: "RASv1RequiredDynamicBidding" = Field(..., alias="dynamicBidding")
    end_date: Optional[str] = Field(None, alias="endDate", description="Campaign end date")
    name: str = Field(..., description="The name of the campaign.")
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="The identifier of an existing portfolio to which the campaign is associated.")
    start_date: Optional[str] = Field(None, alias="startDate", description="Campaign start date. Default: today&#39;s date. The format of the date is YYYY-MM-DD.")
    state: "RASv1EntityState"
    tags: Optional[list["RASv1Tag"]] = Field(None, description="A list of advertiser-specified custom identifiers for the campaign. Each customer identifier is a key-value pair. You ca")
    targeting_type: "RASv1TargetingType" = Field(..., alias="targetingType")

    model_config = {'populate_by_name': True}


class RASv1CreateCampaignsRequestContent(BaseModel):
    campaigns: list["RASv1CreateCampaignInput"] = Field(..., description="List of Campaigns to create")

    model_config = {'populate_by_name': True}


class RASv1CreateCampaignsResponseContent(BaseModel):
    campaigns: "RASv1BulkCreateCampaignsOutcomes"

    model_config = {'populate_by_name': True}


class RASv1CreateProductAdInput(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the ad group.")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign.")
    retailer_id: str = Field(..., alias="retailerId", description="Id of a retailer owning the offer to be advertised")
    retailer_offer_id: str = Field(..., alias="retailerOfferId", description="Id of the offer to be advertised, must belong to retailer identified by retailerId field")
    state: "RASv1EntityState"

    model_config = {'populate_by_name': True}


class RASv1CreateProductAdsRequestContent(BaseModel):
    product_ads: list["RASv1CreateProductAdInput"] = Field(..., alias="productAds", description="List of ProductAds to create")

    model_config = {'populate_by_name': True}


class RASv1CreateProductAdsResponseContent(BaseModel):
    product_ads: "RASv1BulkCreateProductAdsOutcomes" = Field(..., alias="productAds")

    model_config = {'populate_by_name': True}


class RASv1TargetBidInput(BaseModel):
    bid: float = Field(..., description="The maximum bid for a target.")

    model_config = {'populate_by_name': True}


class RASv1CreateTargetInput(BaseModel):
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="The identifier of the ad group.")
    bid: Optional["RASv1TargetBidInput"] = None
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign.")
    negative: bool = Field(..., description="Indicates whether the target is negative or not.")
    state: "RASv1EntityState"
    target_details: "RASv1TargetDetails" = Field(..., alias="targetDetails")
    target_type: "RASv1TargetType" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class RASv1CreateTargetsRequestContent(BaseModel):
    targets: list["RASv1CreateTargetInput"] = Field(..., description="List of Targets to create")

    model_config = {'populate_by_name': True}


class RASv1CreateTargetsResponseContent(BaseModel):
    targets: "RASv1BulkCreateTargetsOutcomes"

    model_config = {'populate_by_name': True}


class RASv1EntityIdFilter(BaseModel):
    """Filter entities by the list of objectIds"""
    include: list[str]

    model_config = {'populate_by_name': True}


class RASv1DeleteAdGroupsRequestContent(BaseModel):
    ad_group_id_filter: "RASv1EntityIdFilter" = Field(..., alias="adGroupIdFilter")

    model_config = {'populate_by_name': True}


class RASv1DeleteAdGroupsResponseContent(BaseModel):
    ad_groups: "RASv1BulkMutateAdGroupsOutcomes" = Field(..., alias="adGroups")

    model_config = {'populate_by_name': True}


class RASv1DeleteCampaignsRequestContent(BaseModel):
    campaign_id_filter: "RASv1EntityIdFilter" = Field(..., alias="campaignIdFilter")

    model_config = {'populate_by_name': True}


class RASv1DeleteCampaignsResponseContent(BaseModel):
    campaigns: "RASv1BulkMutateCampaignsOutcomes"

    model_config = {'populate_by_name': True}


class RASv1DeleteProductAdsRequestContent(BaseModel):
    product_ad_id_filter: "RASv1EntityIdFilter" = Field(..., alias="productAdIdFilter")

    model_config = {'populate_by_name': True}


class RASv1DeleteProductAdsResponseContent(BaseModel):
    product_ads: "RASv1BulkMutateProductAdsOutcomes" = Field(..., alias="productAds")

    model_config = {'populate_by_name': True}


class RASv1DeleteTargetsRequestContent(BaseModel):
    target_id_filter: "RASv1EntityIdFilter" = Field(..., alias="targetIdFilter")

    model_config = {'populate_by_name': True}


class RASv1DeleteTargetsResponseContent(BaseModel):
    targets: "RASv1BulkMutateTargetsOutcomes"

    model_config = {'populate_by_name': True}


class RASv1EntityProductId(BaseModel):
    retailer_id: str = Field(..., alias="retailerId", description="Id of a retailer owning the offer to be advertised")
    retailer_offer_id: str = Field(..., alias="retailerOfferId", description="Id of the offer to be advertised, must belong to retailer identified by retailerId field")

    model_config = {'populate_by_name': True}


class RASv1GatewayTimeoutExceptionResponseContent(BaseModel):
    code: Optional[str] = Field(None, description="Error code")
    message: Optional[str] = Field(None, description="Human readable response message")

    model_config = {'populate_by_name': True}


class RASv1InternalErrorErrorCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class RASv1InternalServerExceptionResponseContent(BaseModel):
    code: "RASv1InternalErrorErrorCode"
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class RASv1QueryTermMatchType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class RASv1KeywordFilter(BaseModel):
    include: Optional[list[str]] = None
    query_term_match_type: "RASv1QueryTermMatchType" = Field(..., alias="queryTermMatchType")

    model_config = {'populate_by_name': True}


class RASv1ReducedEntityIdFilter(BaseModel):
    """Filter entities by the list of objectIds"""
    include: list[str]

    model_config = {'populate_by_name': True}


class RASv1StateFilter(BaseModel):
    """Filter entities by state"""
    include: list["RASv1EntityState"]

    model_config = {'populate_by_name': True}


class RASv1NameFilter(BaseModel):
    """Filter entities by name"""
    include: Optional[list[str]] = None
    query_term_match_type: "RASv1QueryTermMatchType" = Field(..., alias="queryTermMatchType")

    model_config = {'populate_by_name': True}


class RASv1ListAdGroupsRequestContent(BaseModel):
    ad_group_id_filter: Optional["RASv1EntityIdFilter"] = Field(None, alias="adGroupIdFilter")
    campaign_id_filter: Optional["RASv1ReducedEntityIdFilter"] = Field(None, alias="campaignIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API")
    name_filter: Optional["RASv1NameFilter"] = Field(None, alias="nameFilter")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    state_filter: Optional["RASv1StateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class RASv1ListAdGroupsResponseContent(BaseModel):
    ad_groups: Optional[list["RASv1AdGroupOutput"]] = Field(None, alias="adGroups")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of entities")

    model_config = {'populate_by_name': True}


class RASv1ListCampaignsRequestContent(BaseModel):
    campaign_id_filter: Optional["RASv1EntityIdFilter"] = Field(None, alias="campaignIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API")
    name_filter: Optional["RASv1NameFilter"] = Field(None, alias="nameFilter")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    portfolio_id_filter: Optional["RASv1ReducedEntityIdFilter"] = Field(None, alias="portfolioIdFilter")
    state_filter: Optional["RASv1StateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class RASv1ListCampaignsResponseContent(BaseModel):
    campaigns: Optional[list["RASv1CampaignOutput"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of entities")

    model_config = {'populate_by_name': True}


class RASv1ListProductAdsRequestContent(BaseModel):
    ad_group_id_filter: Optional["RASv1ReducedEntityIdFilter"] = Field(None, alias="adGroupIdFilter")
    campaign_id_filter: Optional["RASv1ReducedEntityIdFilter"] = Field(None, alias="campaignIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    product_ad_id_filter: Optional["RASv1EntityIdFilter"] = Field(None, alias="productAdIdFilter")
    state_filter: Optional["RASv1StateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class RASv1ListProductAdsResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    product_ads: Optional[list["RASv1ProductAdOutput"]] = Field(None, alias="productAds")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of entities")

    model_config = {'populate_by_name': True}


class RASv1ProductIdFilter(BaseModel):
    include: list["RASv1EntityProductId"]

    model_config = {'populate_by_name': True}


class RASv1TargetLevelFilter(BaseModel):
    include: Optional[list["RASv1TargetLevel"]] = None

    model_config = {'populate_by_name': True}


class RASv1NegativeTargetFilter(BaseModel):
    include: Optional[list[bool]] = None

    model_config = {'populate_by_name': True}


class RASv1ListTargetsRequestContent(BaseModel):
    ad_group_id_filter: Optional["RASv1ReducedEntityIdFilter"] = Field(None, alias="adGroupIdFilter")
    campaign_id_filter: Optional["RASv1ReducedEntityIdFilter"] = Field(None, alias="campaignIdFilter")
    keyword_filter: Optional["RASv1KeywordFilter"] = Field(None, alias="keywordFilter")
    match_type_filter: Optional[list["RASv1KeywordMatchType"]] = Field(None, alias="matchTypeFilter", description="Only keywords with match type that is in this list will be listed")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API")
    negative_filter: Optional["RASv1NegativeTargetFilter"] = Field(None, alias="negativeFilter")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    product_id_filter: Optional["RASv1ProductIdFilter"] = Field(None, alias="productIdFilter")
    state_filter: Optional["RASv1StateFilter"] = Field(None, alias="stateFilter")
    target_id_filter: Optional["RASv1EntityIdFilter"] = Field(None, alias="targetIdFilter")
    target_level_filter: Optional["RASv1TargetLevelFilter"] = Field(None, alias="targetLevelFilter")
    target_type_filter: Optional[list["RASv1TargetType"]] = Field(None, alias="targetTypeFilter", description="Only targets of specified types will be listed")

    model_config = {'populate_by_name': True}


class RASv1ListTargetsResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    targets: Optional[list["RASv1TargetOutput"]] = None
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of entities")

    model_config = {'populate_by_name': True}


class RASv1OptionalDynamicBidding(BaseModel):
    placement_bidding: Optional[list["RASv1PlacementBidAdjustment"]] = Field(None, alias="placementBidding")
    strategy: Optional["RASv1BiddingStrategy"] = None

    model_config = {'populate_by_name': True}


class RASv1ProductAdAccessErrorSelector(BaseModel):
    entity_not_found_error: Optional["RASv1EntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    internal_server_error: Optional["RASv1InternalServerError"] = Field(None, alias="internalServerError")
    malformed_value_error: Optional["RASv1MalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["RASv1MissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["RASv1OtherError"] = Field(None, alias="otherError")
    range_error: Optional["RASv1RangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["RASv1ThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class RASv1ProductAdAccessError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "RASv1ProductAdAccessErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class RASv1ProductAdAccessExceptionResponseContent(BaseModel):
    """Exception resulting in accessing ad group entities"""
    code: "RASv1InvalidArgumentErrorCode"
    errors: Optional[list["RASv1ProductAdAccessError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class RASv1ProductAdMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating ProductAd management entities"""
    code: "RASv1InvalidArgumentErrorCode"
    errors: Optional[list["RASv1ProductAdMutationError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class RASv1ServiceUnavailableExceptionResponseContent(BaseModel):
    code: Optional[str] = Field(None, description="Error code")
    message: Optional[str] = Field(None, description="Human readable response message")

    model_config = {'populate_by_name': True}


class RASv1TargetAccessErrorSelector(BaseModel):
    entity_not_found_error: Optional["RASv1EntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    internal_server_error: Optional["RASv1InternalServerError"] = Field(None, alias="internalServerError")
    malformed_value_error: Optional["RASv1MalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["RASv1MissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["RASv1OtherError"] = Field(None, alias="otherError")
    range_error: Optional["RASv1RangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["RASv1ThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class RASv1TargetAccessError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "RASv1TargetAccessErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class RASv1TargetAccessExceptionResponseContent(BaseModel):
    """Exception resulting in accessing ad group entities"""
    code: "RASv1InvalidArgumentErrorCode"
    errors: Optional[list["RASv1TargetAccessError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class RASv1TargetMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating Target management entities"""
    code: "RASv1InvalidArgumentErrorCode"
    errors: Optional[list["RASv1TargetMutationError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class RASv1ThrottledErrorCode(StrEnum):
    THROTTLED = "THROTTLED"


class RASv1ThrottlingExceptionResponseContent(BaseModel):
    code: "RASv1ThrottledErrorCode"
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class RASv1UnauthorizedErrorCode(StrEnum):
    UNAUTHORIZED = "UNAUTHORIZED"


class RASv1UnauthorizedExceptionResponseContent(BaseModel):
    code: "RASv1UnauthorizedErrorCode"
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class RASv1UpdateAdGroupInput(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the AdGroup.")
    default_bid: Optional[float] = Field(None, alias="defaultBid", description="A bid value for use when no bid is specified for keywords in the ad group. For more information about bid constraints by")
    name: Optional[str] = Field(None, description="The name of the ad group.")
    state: Optional["RASv1EntityState"] = None

    model_config = {'populate_by_name': True}


class RASv1UpdateAdGroupsRequestContent(BaseModel):
    ad_groups: list["RASv1UpdateAdGroupInput"] = Field(..., alias="adGroups", description="List of AdGroup to update")

    model_config = {'populate_by_name': True}


class RASv1UpdateAdGroupsResponseContent(BaseModel):
    ad_groups: "RASv1BulkMutateAdGroupsOutcomes" = Field(..., alias="adGroups")

    model_config = {'populate_by_name': True}


class RASv1UpdateCampaignInput(BaseModel):
    budget: Optional["RASv1BudgetInput"] = None
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the Campaign.")
    dynamic_bidding: Optional["RASv1OptionalDynamicBidding"] = Field(None, alias="dynamicBidding")
    end_date: Optional[str] = Field(None, alias="endDate", description="Campaign end date")
    name: Optional[str] = Field(None, description="The name of the campaign.")
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="The identifier of an existing portfolio to which the campaign is associated.")
    start_date: Optional[str] = Field(None, alias="startDate", description="Campaign start date. Default: today&#39;s date. The format of the date is YYYY-MM-DD.")
    state: Optional["RASv1EntityState"] = None
    tags: Optional[list["RASv1Tag"]] = Field(None, description="A list of advertiser-specified custom identifiers for the campaign. Each customer identifier is a key-value pair. You ca")

    model_config = {'populate_by_name': True}


class RASv1UpdateCampaignsRequestContent(BaseModel):
    campaigns: list["RASv1UpdateCampaignInput"] = Field(..., description="List of Campaign to update")

    model_config = {'populate_by_name': True}


class RASv1UpdateCampaignsResponseContent(BaseModel):
    campaigns: "RASv1BulkMutateCampaignsOutcomes"

    model_config = {'populate_by_name': True}


class RASv1UpdateProductAdInput(BaseModel):
    product_ad_id: str = Field(..., alias="productAdId", description="The identifier of the ProductAd.")
    state: Optional["RASv1EntityState"] = None

    model_config = {'populate_by_name': True}


class RASv1UpdateProductAdsRequestContent(BaseModel):
    product_ads: list["RASv1UpdateProductAdInput"] = Field(..., alias="productAds", description="List of ProductAd to update")

    model_config = {'populate_by_name': True}


class RASv1UpdateProductAdsResponseContent(BaseModel):
    product_ads: "RASv1BulkMutateProductAdsOutcomes" = Field(..., alias="productAds")

    model_config = {'populate_by_name': True}


class RASv1UpdateTargetInput(BaseModel):
    bid: Optional["RASv1TargetBidInput"] = None
    state: Optional["RASv1EntityState"] = None
    target_id: str = Field(..., alias="targetId", description="The identifier of the Target.")

    model_config = {'populate_by_name': True}


class RASv1UpdateTargetsRequestContent(BaseModel):
    targets: list["RASv1UpdateTargetInput"] = Field(..., description="List of Target to update")

    model_config = {'populate_by_name': True}


class RASv1UpdateTargetsResponseContent(BaseModel):
    targets: "RASv1BulkMutateTargetsOutcomes"

    model_config = {'populate_by_name': True}

