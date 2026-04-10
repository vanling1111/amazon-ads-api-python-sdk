"""Auto-generated Pydantic models. Do not edit manually.

Source: Audiences_prod_3p.json
Title:  Audiences
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class AccessDeniedErrorCode(StrEnum):
    ACCESS_DENIED = "ACCESS_DENIED"


class AccessDeniedExceptionResponseContent(BaseModel):
    """User does not have sufficient access to perform this action."""
    code: "AccessDeniedErrorCode"
    message: str = Field(..., description="Human readable error message.")
    request_id: str = Field(..., alias="requestId", description="RequestId of the failed request.")

    model_config = {'populate_by_name': True}


class InvalidArgumentErrorCode(StrEnum):
    INVALID_ARGUMENT = "INVALID_ARGUMENT"


class AdMutationExceptionResponseContent(BaseModel):
    code: "InvalidArgumentErrorCode"
    message: str = Field(..., description="Human readable error message.")
    request_id: str = Field(..., alias="requestId", description="RequestId of the failed request.")

    model_config = {'populate_by_name': True}


class AttributeType(StrEnum):
    ASIN = "ASIN"


class ForecastBucketV1(BaseModel):
    lower_bound_inclusive: Optional[int] = Field(None, alias="lowerBoundInclusive", description="The inclusive lower bound for the bucket.  If not specified, the bucket captures all values below the upper bound.")
    upper_bound_exclusive: Optional[int] = Field(None, alias="upperBoundExclusive", description="The exclusive upper bound for the bucket.  If not specified, the bucket captures all values above the lower bound.")

    model_config = {'populate_by_name': True}


class DSPInventoryForecastV1(BaseModel):
    daily_impressions: "ForecastBucketV1" = Field(..., alias="dailyImpressions", description="The forecasted available daily impressions for the inventory type.")
    daily_reach: "ForecastBucketV1" = Field(..., alias="dailyReach", description="The forecasted unique devices reachable daily for the inventory type.")

    model_config = {'populate_by_name': True}


class STInventoryForecastV1(BaseModel):
    daily_reach: "ForecastBucketV1" = Field(..., alias="dailyReach", description="The forecasted unique devices reachable daily for the inventory type.")

    model_config = {'populate_by_name': True}


class SDInventoryForecastV1(BaseModel):
    daily_reach: "ForecastBucketV1" = Field(..., alias="dailyReach", description="The forecasted unique devices reachable daily for the inventory type.")

    model_config = {'populate_by_name': True}


class InventoryForecastV1(BaseModel):
    pass


class AudienceCommonFieldsV1ForecastsInventoryforecasts(BaseModel):
    all: Optional["InventoryForecastV1"] = None

    model_config = {'populate_by_name': True}


class AudienceCommonFieldsV1Forecasts(BaseModel):
    inventory_forecasts: "AudienceCommonFieldsV1ForecastsInventoryforecasts" = Field(..., alias="inventoryForecasts")

    model_config = {'populate_by_name': True}


class AudienceCommonFieldsV1Status(StrEnum):
    ACTIVE = "Active"
    DEACTIVATED = "Deactivated"
    DEPRECATED = "Deprecated"
    FAILED = "Failed"
    PENDING = "Pending"
    PROCESSING = "Processing"


class AudienceCommonFieldsV1(BaseModel):
    audience_id: str = Field(..., alias="audienceId", description="Audience segment identifier")
    audience_name: str = Field(..., alias="audienceName", description="Audience name")
    category: str = Field(..., description="Audience segment category")
    create_date: Optional[str] = Field(None, alias="createDate")
    description: str = Field(..., description="Audience description")
    forecasts: "AudienceCommonFieldsV1Forecasts"
    status: AudienceCommonFieldsV1Status
    sub_category: Optional[str] = Field(None, alias="subCategory", description="Audience segment sub-category")
    update_date: Optional[str] = Field(None, alias="updateDate")

    model_config = {'populate_by_name': True}


class ErrorType(StrEnum):
    OTHER = "OTHER"
    VALUE_INVALID = "VALUE_INVALID"
    VALUE_NOT_FOUND = "VALUE_NOT_FOUND"
    VALUE_OUT_OF_RANGE = "VALUE_OUT_OF_RANGE"


class DspAudienceDeleteErrorItemError(BaseModel):
    error_code: "ErrorType" = Field(..., alias="errorCode")
    error_id: int = Field(..., alias="errorId")
    error_message: str = Field(..., alias="errorMessage")
    field_name: Optional[str] = Field(None, alias="fieldName")

    model_config = {'populate_by_name': True}


class DspAudienceDeleteErrorItem(BaseModel):
    audience_id: str = Field(..., alias="audienceId", description="Identifier of audience for which delete was attempted.")
    errors: list["DspAudienceDeleteErrorItemError"]
    http_status_code: int = Field(..., alias="httpStatusCode", description="HTTP Response Code for the request")
    index: int = Field(..., description="Index of the DspAudienceDeleteRequestItem from the request. e.g. 1st item in the request will correspond to index 0 in t")
    message: str = Field(..., description="A human-readable description of the response.")
    request_id: str = Field(..., alias="requestId")

    model_config = {'populate_by_name': True}


class DspAudienceDeleteSuccessItem(BaseModel):
    """The success response object."""
    audience_id: str = Field(..., alias="audienceId", description="The audience identifier of the audience to be actioned.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="unique request token for this request.")
    index: int = Field(..., description="index of the DspAudienceEditRequestItem from the request. e.g. 1st item in the request will correspond to index 0 in the")

    model_config = {'populate_by_name': True}


class DspAudienceDeleteResponse(BaseModel):
    """Holds an array of successful items and an array of error items from the request."""
    failed: list["DspAudienceDeleteErrorItem"]
    success: list["DspAudienceDeleteSuccessItem"]

    model_config = {'populate_by_name': True}


class AudienceDeleteAccessDeniedExceptionResponseContent(BaseModel):
    """User does not have sufficient access to perform this action."""
    error_response: "DspAudienceDeleteResponse" = Field(..., alias="errorResponse")

    model_config = {'populate_by_name': True}


class AudienceDeleteAdMutationExceptionResponseContent(BaseModel):
    error_response: "DspAudienceDeleteResponse" = Field(..., alias="errorResponse")

    model_config = {'populate_by_name': True}


class AudienceDeleteBadGatewayExceptionResponseContent(BaseModel):
    """Unexpected error during processing of request."""
    error_response: "DspAudienceDeleteResponse" = Field(..., alias="errorResponse")

    model_config = {'populate_by_name': True}


class AudienceDeleteInternalServerExceptionResponseContent(BaseModel):
    """Unexpected error during processing of request."""
    error_response: "DspAudienceDeleteResponse" = Field(..., alias="errorResponse")

    model_config = {'populate_by_name': True}


class AudienceDeleteThrottlingExceptionResponseContent(BaseModel):
    """Request was denied due to request throttling."""
    error_response: "DspAudienceDeleteResponse" = Field(..., alias="errorResponse")

    model_config = {'populate_by_name': True}


class AudienceDeleteUnauthorizedExceptionResponseContent(BaseModel):
    """Caller does not have permissions to edit specified audience."""
    error_response: "DspAudienceDeleteResponse" = Field(..., alias="errorResponse")

    model_config = {'populate_by_name': True}


class AudienceSubErrorV1(BaseModel):
    """The sub error object."""
    error_type: str = Field(..., alias="errorType")
    field_name: Optional[str] = Field(None, alias="fieldName")
    message: str

    model_config = {'populate_by_name': True}


class AudienceErrorV1(BaseModel):
    """The error response object."""
    errors: Optional[list["AudienceSubErrorV1"]] = None
    message: Optional[str] = Field(None, description="A human-readable description of the response.")
    request_id: Optional[str] = Field(None, alias="requestId", description="A value created by Amazon API Gateway that uniquely identifies your request.")

    model_config = {'populate_by_name': True}


class AudienceFilterV1Operator(StrEnum):
    EQ = "EQ"
    NOT_EQ = "NOT_EQ"


class AudienceFilterV1(BaseModel):
    field: Optional[str] = Field(None, description="Field to filter by. Supported enums are 'audienceName', 'category', 'categoryPath', 'audienceId' and 'status'. The 'audi")
    operator: Optional[AudienceFilterV1Operator] = Field(None, description="Operator to apply to the specified filter.")
    values: Optional[list[str]] = None

    model_config = {'populate_by_name': True}


class AudienceType(StrEnum):
    PRODUCT_PURCHASES = "PRODUCT_PURCHASES"
    PRODUCT_SEARCH = "PRODUCT_SEARCH"
    PRODUCT_SIMS = "PRODUCT_SIMS"
    PRODUCT_VIEWS = "PRODUCT_VIEWS"


class SDAudienceFieldsV1(BaseModel):
    pass


class STAudienceFieldsV1(BaseModel):
    pass


class DSPAudienceFieldsV1FeesCurrency(StrEnum):
    AED = "AED"
    AUD = "AUD"
    BRL = "BRL"
    CAD = "CAD"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"
    JPY = "JPY"
    KSA = "KSA"
    MXN = "MXN"
    SEK = "SEK"
    TRY = "TRY"
    USD = "USD"


class DSPAudienceFieldsV1Fees(BaseModel):
    amount: Optional[int] = Field(None, description="Fee amount in base currency units, multiplied by scaling factor ('scale').")
    currency: Optional[DSPAudienceFieldsV1FeesCurrency] = Field(None, description="Base currency, such as US Dollar.")
    fee_calculation_type: Optional[str] = Field(None, alias="feeCalculationType", description="How the fee is applied.")
    impression_supply_type: Optional[str] = Field(None, alias="impressionSupplyType", description="To which supply types this fee applies to. The fee may be different for different supply types.")
    scale: Optional[int] = Field(None, description="Scale of the amount relative to the base currency unit. For instance, if the scale is 1000, the currency is USD, and the")

    model_config = {'populate_by_name': True}


class DSPAudienceFieldsV1(BaseModel):
    fees: Optional[list["DSPAudienceFieldsV1Fees"]] = Field(None, description="Fees that will apply to this segment. Not all segments have fees. Fees may differ depending on the supply type the segme")
    provider_id: Optional[str] = Field(None, alias="providerId", description="The Data Management Platform provider identifier. Only applicable to Third party audience segments.")

    model_config = {'populate_by_name': True}


class AudienceV1(BaseModel):
    pass


class BadGatewayErrorCode(StrEnum):
    BAD_GATEWAY = "BAD_GATEWAY"


class BadGatewayExceptionResponseContent(BaseModel):
    """Unexpected error during processing of request."""
    code: "BadGatewayErrorCode"
    message: str = Field(..., description="Human readable error message.")
    request_id: str = Field(..., alias="requestId", description="RequestId of the failed request.")

    model_config = {'populate_by_name': True}


class Clause(StrEnum):
    INCLUDE = "INCLUDE"


class Operator(StrEnum):
    ONE_OF = "ONE_OF"


class DSPAudienceRule(BaseModel):
    """Rule to define an audience.  **Rule Constraints Table**: Provides available valid combinations of parameters allowed in DspAudienceRule | audienceType | attributeType | attributeValues | max attribute"""
    attribute_type: "AttributeType" = Field(..., alias="attributeType")
    attribute_values: list[str] = Field(..., alias="attributeValues", description="For a given audienceType and attributeType combination, the attribute values being supplied.")
    clause: "Clause"
    operator: "Operator"

    model_config = {'populate_by_name': True}


class DspAudienceDeleteRequestItem(BaseModel):
    audience_id: str = Field(..., alias="audienceId", description="The audience identifier of the audience to be actioned.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="unique request token for this request.")

    model_config = {'populate_by_name': True}


class DspAudienceDeleteRequestContent(BaseModel):
    dsp_audience_delete_request_items: list["DspAudienceDeleteRequestItem"] = Field(..., alias="dspAudienceDeleteRequestItems", description="A list of audiences to be deleted")

    model_config = {'populate_by_name': True}


class DspAudienceDeleteResponseContent(BaseModel):
    """Holds an array of successful items and an array of error items from the request."""
    failed: list["DspAudienceDeleteErrorItem"]
    success: list["DspAudienceDeleteSuccessItem"]

    model_config = {'populate_by_name': True}


class DspAudienceEditRequestItem(BaseModel):
    """Partial audience model to be used for edit of the audience."""
    audience_id: str = Field(..., alias="audienceId", description="The audience identifier of the audience to be actioned.")
    audience_type: "AudienceType" = Field(..., alias="audienceType")
    description: Optional[str] = Field(None, description="The audience description.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="unique request token for this request.")
    lookback: Optional[int] = Field(None, description="The specified time period (in days) to include those who performed the action in the audience. Lookback Constraints Tabl")
    name: Optional[str] = Field(None, description="The audience name.")
    rules: Optional[list["DSPAudienceRule"]] = Field(None, description="Set of rules to define an audience, these rules will be ORed.")

    model_config = {'populate_by_name': True}


class DspAudienceEditRequestContent(BaseModel):
    dsp_audience_edit_request_items: list["DspAudienceEditRequestItem"] = Field(..., alias="dspAudienceEditRequestItems", description="A list of audience edit objects containing fields to be overwritten. For each object, specify fields and their values to")

    model_config = {'populate_by_name': True}


class DspAudienceErrorItemError(BaseModel):
    error_type: "ErrorType" = Field(..., alias="errorType")
    field_name: Optional[str] = Field(None, alias="fieldName")
    message: str

    model_config = {'populate_by_name': True}


class DspAudienceErrorItem(BaseModel):
    audience_id: str = Field(..., alias="audienceId", description="Identifier of audience for which edit was attempted.")
    errors: list["DspAudienceErrorItemError"]
    idempotency_key: str = Field(..., alias="idempotencyKey", description="unique request token for this request.")
    index: int = Field(..., description="Index of the DspAudienceEditRequestItem from the request. e.g. 1st item in the request will correspond to index 0 in the")
    message: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class DspAudienceSuccessItem(BaseModel):
    """The success response object."""
    audience_id: str = Field(..., alias="audienceId", description="The audience identifier of the audience to be actioned.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="unique request token for this request.")
    index: int = Field(..., description="index of the DspAudienceEditRequestItem from the request. e.g. 1st item in the request will correspond to index 0 in the")

    model_config = {'populate_by_name': True}


class DspAudienceEditResponseContent(BaseModel):
    """Holds an array of successful items and an array of error items from the request."""
    failed: list["DspAudienceErrorItem"]
    success: list["DspAudienceSuccessItem"]

    model_config = {'populate_by_name': True}


class FetchTaxonomyNodeV1(BaseModel):
    audience_count: Optional[int] = Field(None, alias="audienceCount")
    category: Optional[str] = None

    model_config = {'populate_by_name': True}


class FetchTaxonomyRequestBodyV1Adtype(StrEnum):
    DSP = "DSP"
    SD = "SD"
    ST = "ST"


class FetchTaxonomyRequestBodyV1(BaseModel):
    """The response data will have the categories that are under the given path, and main categories will be returned if no path is specified. The response data also depends on the adType specified here sinc"""
    ad_type: Optional[FetchTaxonomyRequestBodyV1Adtype] = Field(None, alias="adType")
    category_path: Optional[list[str]] = Field(None, alias="categoryPath")
    countries: Optional[list[str]] = Field(None, description="The ISO Alpha-2 country codes to search audiences from. This field must be specified if the advertiser does not have an ")

    model_config = {'populate_by_name': True}


class FetchTaxonomyResponseV1(BaseModel):
    categories: Optional[list["FetchTaxonomyNodeV1"]] = None
    category_path: Optional[list[str]] = Field(None, alias="categoryPath")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class InternalErrorErrorCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class InternalServerExceptionResponseContent(BaseModel):
    """Unexpected error during processing of request."""
    code: "InternalErrorErrorCode"
    message: str = Field(..., description="Human readable error message.")
    request_id: str = Field(..., alias="requestId", description="RequestId of the failed request.")

    model_config = {'populate_by_name': True}


class ListAudiencesRequestBodyV1Adtype(StrEnum):
    DSP = "DSP"
    SD = "SD"
    ST = "ST"


class ListAudiencesRequestBodyV1(BaseModel):
    """Resulting segments will match all specified filters"""
    ad_type: Optional[ListAudiencesRequestBodyV1Adtype] = Field(None, alias="adType")
    countries: Optional[list[str]] = Field(None, description="The ISO Alpha-2 country codes to search audiences from. This field must be specified if the advertiser does not have an ")
    filters: Optional[list["AudienceFilterV1"]] = None

    model_config = {'populate_by_name': True}


class ListAudiencesResponseV1(BaseModel):
    audiences: Optional[list["AudienceV1"]] = Field(None, description="Array of segments matching given filters sorted by create time, earliest first.")
    match_count: Optional[int] = Field(None, alias="matchCount")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class NotFoundErrorCode(StrEnum):
    NOT_FOUND = "NOT_FOUND"


class ResourceNotFoundExceptionResponseContent(BaseModel):
    """Request references a resource which does not exist."""
    code: "NotFoundErrorCode"
    message: str = Field(..., description="Human readable error message.")
    request_id: str = Field(..., alias="requestId", description="RequestId of the failed request.")

    model_config = {'populate_by_name': True}


class ThrottledErrorCode(StrEnum):
    THROTTLED = "THROTTLED"


class ThrottlingExceptionResponseContent(BaseModel):
    """Request was denied due to request throttling."""
    code: "ThrottledErrorCode"
    message: str = Field(..., description="Human readable error message.")
    request_id: str = Field(..., alias="requestId", description="RequestId of the failed request.")

    model_config = {'populate_by_name': True}


class UnauthorizedErrorCode(StrEnum):
    UNAUTHORIZED = "UNAUTHORIZED"


class UnauthorizedExceptionResponseContent(BaseModel):
    """Caller does not have permissions to edit specified audience."""
    code: "UnauthorizedErrorCode"
    message: str = Field(..., description="Human readable error message.")
    request_id: str = Field(..., alias="requestId", description="RequestId of the failed request.")

    model_config = {'populate_by_name': True}

