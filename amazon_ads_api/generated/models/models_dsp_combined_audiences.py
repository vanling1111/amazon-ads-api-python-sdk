"""Auto-generated Pydantic models. Do not edit manually.

Source: CombinedAudienceAPI_prod_3p.json
Title:  Combined Audience API
"""

from __future__ import annotations

from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field



class AUDIENCESTATUS(StrEnum):
    ACTIVE = "Active"
    DEACTIVATED = "Deactivated"
    DEPRECATED = "Deprecated"
    FAILED = "Failed"
    PROCESSING = "Processing"


class AudienceV1(BaseModel):
    audience_id: str = Field(..., alias="audienceId", description="An audience identifier retrieved from the audiences/list resource.")
    group_id: str = Field(..., alias="groupId", description="A customer-provided string used to create a group of audiences. This string is only used for this single request. Amazon")
    negative: bool = Field(..., description="Whether to include (false) or exclude (true) audiences when targeting. Only one state may be used per groupId.")

    model_config = {'populate_by_name': True}


class AudienceTargetingExpression(BaseModel):
    audiences: list["AudienceV1"] = Field(..., description="Specify groups of audiences to include or exclude when targeting.<ul><li>Included groups are joined by an intersection. ")

    model_config = {'populate_by_name': True}


class CURRENCY(StrEnum):
    AED = "AED"
    AUD = "AUD"
    BRL = "BRL"
    CAD = "CAD"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"
    JPY = "JPY"
    MXN = "MXN"
    SAR = "SAR"
    SEK = "SEK"
    TRY = "TRY"
    USD = "USD"


class Expression(BaseModel):
    """The expression should consist of audience targeting expression."""
    audience_targeting_expression: Optional["AudienceTargetingExpression"] = Field(None, alias="audienceTargetingExpression")

    model_config = {'populate_by_name': True}


class CreateCombinedAudienceRequestBody(BaseModel):
    description: str = Field(..., description="The combined audience description.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="The unique UUID for this requested audience.")
    input_expression: "Expression" = Field(..., alias="inputExpression")
    name: str = Field(..., description="The combined audience name.")

    model_config = {'populate_by_name': True}


class CreateCombinedAudienceResponseContent(BaseModel):
    audience_id: str = Field(..., alias="audienceId", description="The audience identifier.")

    model_config = {'populate_by_name': True}


class DspSubErrorV1(BaseModel):
    error_type: str = Field(..., alias="errorType")
    field_name: Optional[str] = Field(None, alias="fieldName")
    message: str

    model_config = {'populate_by_name': True}


class DspBadRequestExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspConflictExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspForbiddenExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspInternalServerExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspNotFoundExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspTooManyRequestsExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspUnauthorizedExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspUnsupportedMediaTypeExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class ForecastBucket(BaseModel):
    """Bucket containing lower and upper bounds for forecast."""
    lower_bound_inclusive: Optional[float] = Field(None, alias="lowerBoundInclusive", description="minimum number of devices reached/ minimum number of available impressions.")
    upper_bound_exclusive: Optional[float] = Field(None, alias="upperBoundExclusive", description="maximum number of devices reached/ maximum number of available impressions.")

    model_config = {'populate_by_name': True}


class ExternalAudienceForecast(BaseModel):
    """Forecast for an audience."""
    daily_impressions: Optional["ForecastBucket"] = Field(None, alias="dailyImpressions")
    daily_reach: Optional["ForecastBucket"] = Field(None, alias="dailyReach")

    model_config = {'populate_by_name': True}


class Fee(BaseModel):
    """Fee applied to a segment."""
    amount: Optional[float] = Field(None, description="Fee amount in base currency units, multiplied by scaling factor ('scale').")
    currency: Optional["CURRENCY"] = None
    fee_calculation_type: Optional[str] = Field(None, alias="feeCalculationType", description="How the fee is applied.")
    impression_supply_type: Optional[str] = Field(None, alias="impressionSupplyType", description="To which supply types this fee applies to. The fee may be different for different supply types.")
    scale: Optional[float] = Field(None, description="Scale of the amount relative to the base currency unit. For instance, if the scale is 1000, the currency is USD, and the")

    model_config = {'populate_by_name': True}


class GetCombinedAudienceDetailsResponseContent(BaseModel):
    audience_id: str = Field(..., alias="audienceId", description="Audience segment identifier.")
    audience_name: str = Field(..., alias="audienceName", description="Audience name.")
    category: str = Field(..., description="Audience segment category.")
    create_date: str = Field(..., alias="createDate", description="Audience creation date.")
    description: str = Field(..., description="Audience description.")
    expression: "Expression"
    fees: Optional[list["Fee"]] = Field(None, description="Fees that will apply to this segment. Not all segments have fees. Fees may differ depending on the supply type the segme")
    forecast: Optional["ExternalAudienceForecast"] = None
    status: "AUDIENCESTATUS"
    sub_category: Optional[str] = Field(None, alias="subCategory", description="Audience segment sub-category.")
    update_date: Optional[str] = Field(None, alias="updateDate", description="Audience update date.")

    model_config = {'populate_by_name': True}

