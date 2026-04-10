"""Auto-generated Pydantic models. Do not edit manually.

Source: Portfolios_prod_3p.json
Title:  Portfolios
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class AccessDeniedErrorCode(StrEnum):
    ACCESS_DENIED = "ACCESS_DENIED"


class AccessDeniedExceptionResponseContent(BaseModel):
    code: "AccessDeniedErrorCode"
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class FeatureState(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class CampaignUnspentBudgetSharing(BaseModel):
    feature_state: "FeatureState" = Field(..., alias="featureState")

    model_config = {'populate_by_name': True}


class BudgetControls(BaseModel):
    campaign_unspent_budget_sharing: Optional["CampaignUnspentBudgetSharing"] = Field(None, alias="campaignUnspentBudgetSharing")

    model_config = {'populate_by_name': True}


class BudgetUsageError(BaseModel):
    """The Error Response Object."""
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class BudgetUsagePortfolio(BaseModel):
    budget: Optional[float] = Field(None, description="Budget amount of resource requested")
    budget_usage_percent: Optional[float] = Field(None, alias="budgetUsagePercent", description="Budget usage percentage (spend / available budget) for the given budget policy.")
    index: Optional[float] = Field(None, description="An index to maintain order of the portfolioIds")
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="ID of requested resource")
    usage_updated_timestamp: Optional[str] = Field(None, alias="usageUpdatedTimestamp", description="Last evaluation time for budget usage")

    model_config = {'populate_by_name': True}


class BudgetUsagePortfolioBatchError(BaseModel):
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")
    index: Optional[float] = Field(None, description="An index to maintain order of the portfolioIds")
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="ID of requested resource")

    model_config = {'populate_by_name': True}


class BudgetUsagePortfolioRequest(BaseModel):
    portfolio_ids: Optional[list[str]] = Field(None, alias="portfolioIds", description="A list of portfolio IDs.")

    model_config = {'populate_by_name': True}


class BudgetUsagePortfolioResponse(BaseModel):
    error: Optional[list["BudgetUsagePortfolioBatchError"]] = Field(None, description="List of budget usage percentages that failed to pull")
    success: Optional[list["BudgetUsagePortfolio"]] = Field(None, description="List of budget usage percentages that were successfully pulled")

    model_config = {'populate_by_name': True}


class PortfolioBudgetErrorReason(StrEnum):
    BUDGETING_POLICY_INVALID = "BUDGETING_POLICY_INVALID"
    BUDGET_AMOUNT_INVALID = "BUDGET_AMOUNT_INVALID"
    BUDGET_CURRENCY_DOES_NOT_MATCH_MARKETPLACE_SETTINGS = "BUDGET_CURRENCY_DOES_NOT_MATCH_MARKETPLACE_SETTINGS"
    BUDGET_LT_DEFAULT_BIDS = "BUDGET_LT_DEFAULT_BIDS"
    BUDGET_LT_KEYWORD_BIDS = "BUDGET_LT_KEYWORD_BIDS"
    BUDGET_LT_PREDEFINED_TARGET_BIDS = "BUDGET_LT_PREDEFINED_TARGET_BIDS"
    BUDGET_OUT_OF_MARKET_PLACE_RANGE = "BUDGET_OUT_OF_MARKET_PLACE_RANGE"
    BUDGET_TOO_HIGH = "BUDGET_TOO_HIGH"
    BUDGET_TOO_LOW = "BUDGET_TOO_LOW"
    MISSING_BUDGETING_POLICY = "MISSING_BUDGETING_POLICY"
    MISSING_IN_BUDGET_FLAG = "MISSING_IN_BUDGET_FLAG"


class ErrorCause(BaseModel):
    """Structure describing error cause - location in the payload and data causing error"""
    location: str = Field(..., description="Error location, JSON Path expression specifying element of API payload causing error")
    trigger: Optional[str] = Field(None, description="optional value causing error")

    model_config = {'populate_by_name': True}


class PortfolioBudgetError(BaseModel):
    cause: "ErrorCause"
    lower_limit: Optional[str] = Field(None, alias="lowerLimit")
    marketplace: Optional[str] = None
    message: str = Field(..., description="Human readable error message")
    reason: "PortfolioBudgetErrorReason"
    upper_limit: Optional[str] = Field(None, alias="upperLimit")

    model_config = {'populate_by_name': True}


class PortfolioBillingErrorReason(StrEnum):
    ADVERTISER_SUSPENDED = "ADVERTISER_SUSPENDED"
    BILLING_ACCOUNT_NOT_FOUND = "BILLING_ACCOUNT_NOT_FOUND"
    EXPIRED_PAYMENT_METHOD = "EXPIRED_PAYMENT_METHOD"
    PAYMENT_PROFILE_NOT_FOUND = "PAYMENT_PROFILE_NOT_FOUND"
    VETTING_FAILURE = "VETTING_FAILURE"


class PortfolioBillingError(BaseModel):
    """Errors related to bids"""
    cause: "ErrorCause"
    marketplace: Optional[str] = None
    message: str = Field(..., description="Human readable error message")
    reason: "PortfolioBillingErrorReason"

    model_config = {'populate_by_name': True}


class PortfolioEntityType(StrEnum):
    PORTFOLIO = "PORTFOLIO"


class PortfolioEntityNotFoundErrorReason(StrEnum):
    ENTITY_NOT_FOUND = "ENTITY_NOT_FOUND"


class PortfolioEntityNotFoundError(BaseModel):
    cause: "ErrorCause"
    entity_id: str = Field(..., alias="entityId", description="The entity id in the request")
    entity_type: "PortfolioEntityType" = Field(..., alias="entityType")
    marketplace: Optional[str] = None
    message: str = Field(..., description="Human readable error message")
    reason: "PortfolioEntityNotFoundErrorReason"

    model_config = {'populate_by_name': True}


class PortfolioValueLimitErrorReason(StrEnum):
    INVALID_ENUM_VALUE = "INVALID_ENUM_VALUE"
    TOO_HIGH = "TOO_HIGH"
    TOO_LOW = "TOO_LOW"


class PortfolioRangeError(BaseModel):
    """Errors related to range constraints violations"""
    allowed: Optional[list[str]] = Field(None, description="allowed values")
    cause: "ErrorCause"
    lower_limit: Optional[str] = Field(None, alias="lowerLimit", description="optional lower limit")
    marketplace: Optional[str] = None
    message: str = Field(..., description="Human readable error message")
    reason: "PortfolioValueLimitErrorReason"
    upper_limit: Optional[str] = Field(None, alias="upperLimit", description="optional upper limit")

    model_config = {'populate_by_name': True}


class PortfolioDuplicateValueErrorReason(StrEnum):
    DUPLICATE_VALUE = "DUPLICATE_VALUE"


class PortfolioDuplicateValueError(BaseModel):
    cause: "ErrorCause"
    marketplace: Optional[str] = None
    message: str = Field(..., description="Human readable error message")
    reason: "PortfolioDuplicateValueErrorReason"

    model_config = {'populate_by_name': True}


class PortfolioDateErrorReason(StrEnum):
    END_DATE_EARLIER_THAN_TODAY = "END_DATE_EARLIER_THAN_TODAY"
    INVALID_DATE = "INVALID_DATE"
    START_DATE_AFTER_END_DATE = "START_DATE_AFTER_END_DATE"
    START_DATE_EARLIER_THAN_TODAY = "START_DATE_EARLIER_THAN_TODAY"
    START_DATE_EQUAL_END_DATE = "START_DATE_EQUAL_END_DATE"
    START_DATE_NOT_NULL = "START_DATE_NOT_NULL"


class PortfolioDateError(BaseModel):
    cause: "ErrorCause"
    marketplace: Optional[str] = None
    message: str = Field(..., description="Human readable error message")
    reason: "PortfolioDateErrorReason"

    model_config = {'populate_by_name': True}


class PortfolioMissingValueErrorReason(StrEnum):
    MISSING_VALUE = "MISSING_VALUE"


class PortfolioMissingValueError(BaseModel):
    """Error describing missing values in API payloads"""
    cause: "ErrorCause"
    marketplace: Optional[str] = None
    message: str = Field(..., description="Human readable error message")
    reason: "PortfolioMissingValueErrorReason"

    model_config = {'populate_by_name': True}


class PortfolioMalformedValueErrorReason(StrEnum):
    FORBIDDEN_CHARS = "FORBIDDEN_CHARS"
    PATTERN_NOT_MATCHED = "PATTERN_NOT_MATCHED"
    TOO_LONG = "TOO_LONG"
    TOO_SHORT = "TOO_SHORT"


class PortfolioMalformedValueError(BaseModel):
    """Errors being used to represent malformed values e.g. containing not allowed characters, not following patterns etc"""
    cause: "ErrorCause"
    fragment: Optional[str] = Field(None, description="fragment of the value which is wrong")
    marketplace: Optional[str] = None
    message: str = Field(..., description="Human readable error message")
    reason: "PortfolioMalformedValueErrorReason"

    model_config = {'populate_by_name': True}


class PortfolioOtherErrorReason(StrEnum):
    OTHER_ERROR = "OTHER_ERROR"


class PortfolioOtherError(BaseModel):
    """Errors not related to any of the other error types"""
    cause: "ErrorCause"
    marketplace: Optional[str] = None
    message: str = Field(..., description="Human readable error message")
    reason: "PortfolioOtherErrorReason"

    model_config = {'populate_by_name': True}


class PortfolioEntityQuotaErrorReason(StrEnum):
    QUOTA_EXCEEDED = "QUOTA_EXCEEDED"


class PortfolioQuotaScope(StrEnum):
    ACCOUNT = "ACCOUNT"


class PortfolioEntityQuotaError(BaseModel):
    """Errors related to exceeding quota in portfolios service"""
    cause: "ErrorCause"
    entity_type: "PortfolioEntityType" = Field(..., alias="entityType")
    marketplace: Optional[str] = None
    message: str = Field(..., description="Human readable error message")
    quota: Optional[str] = Field(None, description="optional current quota")
    quota_scope: Optional["PortfolioQuotaScope"] = Field(None, alias="quotaScope")
    reason: "PortfolioEntityQuotaErrorReason"

    model_config = {'populate_by_name': True}


class PortfolioMutationErrorSelector(BaseModel):
    billing_error: Optional["PortfolioBillingError"] = Field(None, alias="billingError")
    budget_error: Optional["PortfolioBudgetError"] = Field(None, alias="budgetError")
    date_error: Optional["PortfolioDateError"] = Field(None, alias="dateError")
    duplicate_value_error: Optional["PortfolioDuplicateValueError"] = Field(None, alias="duplicateValueError")
    entity_not_found_error: Optional["PortfolioEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    entity_quota_error: Optional["PortfolioEntityQuotaError"] = Field(None, alias="entityQuotaError")
    malformed_value_error: Optional["PortfolioMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["PortfolioMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["PortfolioOtherError"] = Field(None, alias="otherError")
    range_error: Optional["PortfolioRangeError"] = Field(None, alias="rangeError")

    model_config = {'populate_by_name': True}


class PortfolioMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "PortfolioMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class PortfolioFailureResponseItem(BaseModel):
    errors: Optional[list["PortfolioMutationError"]] = Field(None, description="a list of validation errors")
    index: float = Field(..., description="the index of the portfolio in the array from the request body")

    model_config = {'populate_by_name': True}


class PortfolioServingStatusReason(StrEnum):
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET_DETAIL = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_ARCHIVED_DETAIL = "ADVERTISER_ARCHIVED_DETAIL"
    ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL = "ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL"
    ADVERTISER_OUT_OF_BUDGET_DETAIL = "ADVERTISER_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_OUT_OF_PREPAY_BALANCE_DETAIL = "ADVERTISER_OUT_OF_PREPAY_BALANCE_DETAIL"
    ADVERTISER_PAUSED_DETAIL = "ADVERTISER_PAUSED_DETAIL"
    ADVERTISER_PAYMENT_FAILURE_DETAIL = "ADVERTISER_PAYMENT_FAILURE_DETAIL"
    PORTFOLIO_ENDED_DETAIL = "PORTFOLIO_ENDED_DETAIL"
    PORTFOLIO_OUT_OF_BUDGET_DETAIL = "PORTFOLIO_OUT_OF_BUDGET_DETAIL"
    PORTFOLIO_PENDING_START_DATE_DETAIL = "PORTFOLIO_PENDING_START_DATE_DETAIL"
    PORTFOLIO_STATUS_ENABLED_DETAIL = "PORTFOLIO_STATUS_ENABLED_DETAIL"


class PortfolioServingStatus(StrEnum):
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"
    ADVERTISER_OUT_OF_PREPAY_BALANCE = "ADVERTISER_OUT_OF_PREPAY_BALANCE"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"
    PORTFOLIO_STATUS_ENABLED = "PORTFOLIO_STATUS_ENABLED"


class PortfolioExtendedData(BaseModel):
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="Creation date in ISO 8601.")
    last_update_date_time: Optional[str] = Field(None, alias="lastUpdateDateTime", description="Date of last update in ISO 8601.")
    serving_status: Optional["PortfolioServingStatus"] = Field(None, alias="servingStatus")
    status_reasons: Optional[list["PortfolioServingStatusReason"]] = Field(None, alias="statusReasons")

    model_config = {'populate_by_name': True}


class PolicyType(StrEnum):
    DATE_RANGE = "DATE_RANGE"
    MONTHLY_RECURRING = "MONTHLY_RECURRING"
    NO_CAP = "NO_CAP"
    OTHER = "OTHER"


class CurrencyCode(StrEnum):
    AED = "AED"
    AUD = "AUD"
    BRL = "BRL"
    CAD = "CAD"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    EGP = "EGP"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"
    JPY = "JPY"
    MXN = "MXN"
    NGN = "NGN"
    PLN = "PLN"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    TRY = "TRY"
    USD = "USD"
    ZAR = "ZAR"


class PortfolioBudget(BaseModel):
    amount: Optional[float] = Field(None, description="The amount of the budget.")
    currency_code: Optional["CurrencyCode"] = Field(None, alias="currencyCode")
    end_date: Optional[str] = Field(None, alias="endDate", description="The end date after which the budget is no longer applied in ISO 8601.")
    policy: Optional["PolicyType"] = None
    start_date: Optional[str] = Field(None, alias="startDate", description="The starting date to which the budget is applied in ISO 8601.")

    model_config = {'populate_by_name': True}


class EntityState(StrEnum):
    ENABLED = "ENABLED"


class Portfolio(BaseModel):
    budget: Optional["PortfolioBudget"] = None
    budget_controls: Optional["BudgetControls"] = Field(None, alias="budgetControls")
    extended_data: Optional["PortfolioExtendedData"] = Field(None, alias="extendedData")
    in_budget: Optional[bool] = Field(None, alias="inBudget", description="States if the portfolio is still within budget.")
    name: str = Field(..., description="The name of the portfolio.")
    portfolio_id: str = Field(..., alias="portfolioId", description="The ID of the portfolio.")
    state: "EntityState"

    model_config = {'populate_by_name': True}


class PortfolioSuccessResponseItem(BaseModel):
    index: float = Field(..., description="the index of the portfolio in the array from the request body")
    portfolio: Optional["Portfolio"] = None
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="the Portfolio ID")

    model_config = {'populate_by_name': True}


class BulkPortfolioOperationResponse(BaseModel):
    error: Optional[list["PortfolioFailureResponseItem"]] = None
    success: Optional[list["PortfolioSuccessResponseItem"]] = None

    model_config = {'populate_by_name': True}


class CreatePortfolio(BaseModel):
    budget: Optional["PortfolioBudget"] = None
    budget_controls: Optional["BudgetControls"] = Field(None, alias="budgetControls")
    name: str = Field(..., description="The name of the portfolio.")
    state: "EntityState"

    model_config = {'populate_by_name': True}


class CreatePortfoliosRequestContent(BaseModel):
    portfolios: list["CreatePortfolio"] = Field(..., description="An array of portfolio to create.")

    model_config = {'populate_by_name': True}


class CreatePortfoliosResponseContent(BaseModel):
    portfolios: "BulkPortfolioOperationResponse"

    model_config = {'populate_by_name': True}


class EntityStateFilter(BaseModel):
    """Filter entities by state"""
    include: Optional[list["EntityState"]] = None

    model_config = {'populate_by_name': True}


class InternalErrorErrorCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class InternalServerExceptionResponseContent(BaseModel):
    code: "InternalErrorErrorCode"
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class InvalidArgumentErrorCode(StrEnum):
    INVALID_ARGUMENT = "INVALID_ARGUMENT"


class QueryTermMatchType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class NameFilter(BaseModel):
    """Filter entities by name"""
    include: Optional[list[str]] = None
    query_term_match_type: Optional["QueryTermMatchType"] = Field(None, alias="queryTermMatchType")

    model_config = {'populate_by_name': True}


class ObjectIdFilter(BaseModel):
    """Filter entities by the list of objectIds"""
    include: Optional[list[str]] = None

    model_config = {'populate_by_name': True}


class ListPortfoliosRequestContent(BaseModel):
    include_extended_data_fields: Optional[bool] = Field(None, alias="includeExtendedDataFields", description="whether to get a list of targetingClauses with extended data fields (creationDate, lastUpdateDate, servingStatus).")
    name_filter: Optional["NameFilter"] = Field(None, alias="nameFilter")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    portfolio_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="portfolioIdFilter")
    state_filter: Optional["EntityStateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class ListPortfoliosResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    portfolios: Optional[list["Portfolio"]] = None
    total_results: Optional[float] = Field(None, alias="totalResults", description="The total number of entities")

    model_config = {'populate_by_name': True}


class PortfolioAccessErrorSelector(BaseModel):
    date_error: Optional["PortfolioDateError"] = Field(None, alias="dateError")
    entity_not_found_error: Optional["PortfolioEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    malformed_value_error: Optional["PortfolioMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["PortfolioMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["PortfolioOtherError"] = Field(None, alias="otherError")
    range_error: Optional["PortfolioRangeError"] = Field(None, alias="rangeError")

    model_config = {'populate_by_name': True}


class PortfolioAccessError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "PortfolioAccessErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class PortfolioAccessExceptionResponseContent(BaseModel):
    """Exception resulting in accessing portfolio entity"""
    code: "InvalidArgumentErrorCode"
    errors: Optional[list["PortfolioAccessError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SchemaValidationExceptionResponseContent(BaseModel):
    code: "InvalidArgumentErrorCode"
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class ThrottledErrorCode(StrEnum):
    THROTTLED = "THROTTLED"


class ThrottlingExceptionResponseContent(BaseModel):
    code: "ThrottledErrorCode"
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class UnauthorizedErrorCode(StrEnum):
    UNAUTHORIZED = "UNAUTHORIZED"


class UnauthorizedExceptionResponseContent(BaseModel):
    code: "UnauthorizedErrorCode"
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class UnsupportedMediaTypeErrorCode(StrEnum):
    UNSUPPORTED_MEDIA_TYPE = "UNSUPPORTED_MEDIA_TYPE"


class UnsupportedMediaTypeExceptionResponseContent(BaseModel):
    code: "UnsupportedMediaTypeErrorCode"
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class UpdatePortfolio(BaseModel):
    budget: Optional["PortfolioBudget"] = None
    budget_controls: Optional["BudgetControls"] = Field(None, alias="budgetControls")
    name: Optional[str] = Field(None, description="The name of the portfolio.")
    portfolio_id: str = Field(..., alias="portfolioId", description="The ID of the portfolio.")
    state: Optional["EntityState"] = None

    model_config = {'populate_by_name': True}


class UpdatePortfoliosRequestContent(BaseModel):
    portfolios: list["UpdatePortfolio"] = Field(..., description="An array of portfolio with updated values.")

    model_config = {'populate_by_name': True}


class UpdatePortfoliosResponseContent(BaseModel):
    portfolios: "BulkPortfolioOperationResponse"

    model_config = {'populate_by_name': True}

