"""Auto-generated Pydantic models. Do not edit manually.

Source: MediaInsightsHub_prod_3p.json
Title:  Media Insights Hub
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class AccessDeniedErrorCode(StrEnum):
    ACCESS_DENIED = "ACCESS_DENIED"


class ErrorType(StrEnum):
    UNAUTHORIZED = "UNAUTHORIZED"


class SubError(BaseModel):
    error_code: Optional[int] = Field(None, alias="errorCode")
    error_message: Optional[str] = Field(None, alias="errorMessage", description="Human readable error message.")
    error_type: Optional["ErrorType"] = Field(None, alias="errorType")

    model_config = {'populate_by_name': True}


class AccessDeniedExceptionResponseContent(BaseModel):
    """AccessDeniedException 403 response."""
    code: "AccessDeniedErrorCode"
    details: Optional[str] = Field(None, description="Error details.")
    errors: Optional[list["SubError"]] = None
    message: str = Field(..., description="Human readable error message.")
    request_id: str = Field(..., alias="requestId", description="Request Id.")

    model_config = {'populate_by_name': True}


class DimensionType(StrEnum):
    GROUP = "GROUP"
    MULTIPLE = "MULTIPLE"
    SINGLE = "SINGLE"


class LogicalOperator(StrEnum):
    AND = "AND"
    OR = "OR"


class TargetingDimension(BaseModel):
    dimension_groups: Optional[list["TargetingDimension"]] = Field(None, alias="dimensionGroups", description="A list of targeting dimensions that allows you to have nested targeting dimensions. Typically, you will only use this fo")
    dimension_name: Optional[str] = Field(None, alias="dimensionName", description="The name of the dimension you are targeting.  The available dimension names are: | Dimension Name | Allowed Dimension Ty")
    dimension_type: Optional["DimensionType"] = Field(None, alias="dimensionType")
    dimension_value: Optional[str] = Field(None, alias="dimensionValue", description="The value of the dimension you are targeting.")
    dimension_values: Optional[list[str]] = Field(None, alias="dimensionValues", description="A list of values of the dimension you are targeting. The max limit varies on the dimension name.")
    inter_operator: Optional["LogicalOperator"] = Field(None, alias="interOperator")
    intra_operator: Optional["LogicalOperator"] = Field(None, alias="intraOperator")
    is_not: Optional[bool] = Field(None, alias="isNot", description="Whether to negate this dimension or not.")

    model_config = {'populate_by_name': True}


class CreateHistoricalReachCurveRequestContent(BaseModel):
    """Request to generate a historical reach curve."""
    end_date: str = Field(..., alias="endDate", description="The end date for the curve data. This is in the ISO 8601 format. For example 2023-01-31.")
    start_date: str = Field(..., alias="startDate", description="The start date for the curve data. This is in the ISO 8601 format. For example 2023-01-01.")
    targeting: list["TargetingDimension"] = Field(..., description="A list of dimensions that build the targeting expression that is used for generating a reach curve.")

    model_config = {'populate_by_name': True}


class CreateHistoricalReachCurveResponseContent(BaseModel):
    """Success response for generating a historical reach curve."""
    message: Optional[str] = Field(None, description="A message regarding the response.")
    report_id: Optional[str] = Field(None, alias="reportId", description="The report ID.")
    status: Optional[str] = Field(None, description="The status of the report. The status values are [`PENDING`, `PROCESSING`, `COMPLETED`, `FAILED`].")

    model_config = {'populate_by_name': True}


class FrequencyThresholdReach(BaseModel):
    frequency_threshold: Optional[int] = Field(None, alias="frequencyThreshold")
    reach: Optional[int] = None

    model_config = {'populate_by_name': True}


class Marketplace(StrEnum):
    AE = "AE"
    AT = "AT"
    AU = "AU"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"


class HistoricalReachCurveDataPointV2(BaseModel):
    demographic: Optional[str] = None
    end_date: Optional[str] = Field(None, alias="endDate", description="The format of the date is YYYY-MM-DD.")
    frequency_threshold_reach: Optional[list["FrequencyThresholdReach"]] = Field(None, alias="frequencyThresholdReach")
    geography: Optional["Marketplace"] = None
    impressions: Optional[int] = None
    reach_type: Optional[str] = Field(None, alias="reachType")
    start_date: Optional[str] = Field(None, alias="startDate", description="The format of the date is YYYY-MM-DD.")
    supply_package: Optional[str] = Field(None, alias="supplyPackage")

    model_config = {'populate_by_name': True}


class GetHistoricalReachCurveResponseContent(BaseModel):
    """Success response for getting the generated historical reach curve."""
    data_points: Optional[list["HistoricalReachCurveDataPointV2"]] = Field(None, alias="dataPoints", description="List of historical reach curve data points.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="The token to retrieve the next set of data points. This will be `null` if there are no data points left to retrieve.")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of data points.")

    model_config = {'populate_by_name': True}


class GetHistoricalReachCurveStatusResponseContent(BaseModel):
    """Success response for getting the status of the generation of a historical reach curve."""
    message: Optional[str] = Field(None, description="A message regarding the response.")
    report_id: Optional[str] = Field(None, alias="reportId", description="The report ID.")
    status: Optional[str] = Field(None, description="The status of the report. The status values are [`PENDING`, `PROCESSING`, `COMPLETED`, `FAILED`].")

    model_config = {'populate_by_name': True}


class ReachFrequency(BaseModel):
    """The frequency of exposures to households or individuals."""
    five_plus: Optional[int] = Field(None, alias="fivePlus", description="Number of ads viewed at least five times.")
    four_plus: Optional[int] = Field(None, alias="fourPlus", description="Number of ads viewed at least four times.")
    one_plus: Optional[int] = Field(None, alias="onePlus", description="Number of ads viewed at least once.")
    six_plus: Optional[int] = Field(None, alias="sixPlus", description="Number of ads viewed at least six times.")
    three_plus: Optional[int] = Field(None, alias="threePlus", description="Number of ads viewed at least thrice.")
    two_plus: Optional[int] = Field(None, alias="twoPlus", description="Number of ads viewed at least twice.")

    model_config = {'populate_by_name': True}


class HistoricalReachCurveDataPoint(BaseModel):
    """A data point in the Reach Curve for Historical data."""
    channel: Optional[str] = Field(None, description="Supply package for which the reach curve has been generated.")
    demographic: Optional[str] = Field(None, description="The demographic segment applied to the reach curve.")
    end_date: Optional[str] = Field(None, alias="endDate", description="The end of the time window the reach curve is based on.")
    geography: Optional["Marketplace"] = None
    impressions: Optional[int] = Field(None, description="The number of ads that were delivered.")
    reach: Optional["ReachFrequency"] = None
    reach_type: Optional[str] = Field(None, alias="reachType", description="The type of reach, for example INDIVIDUALS or HOUSEHOLDS.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The beginning of the time window the reach curve is based on.")

    model_config = {'populate_by_name': True}


class HistoricalReachCurvesMetadata(BaseModel):
    channels: Optional[list[str]] = Field(None, description="List of channels that were used for showing the ads.")
    demographics: Optional[list[str]] = Field(None, description="List of demographics of the audience that are represented in the data.")
    geography: Optional[str] = Field(None, description="Name of the locale/geography that the metadata belongs to.")
    reach_types: Optional[list[str]] = Field(None, alias="reachTypes", description="List of the different reach types available to request.")

    model_config = {'populate_by_name': True}


class InternalErrorErrorCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class InternalServerExceptionResponseContent(BaseModel):
    """InternalServerException 500 response."""
    code: "InternalErrorErrorCode"
    details: Optional[str] = Field(None, description="Error details.")
    errors: Optional[list["SubError"]] = None
    message: str = Field(..., description="Human readable error message.")
    request_id: str = Field(..., alias="requestId", description="Request Id.")

    model_config = {'populate_by_name': True}


class InvalidArgumentErrorCode(StrEnum):
    INVALID_ARGUMENT = "INVALID_ARGUMENT"


class ListHistoricalReachCurvesMetadataRequestContent(BaseModel):
    geography: Optional[str] = Field(None, description="The locales/geographies that the metadata belongs to.")
    month: Optional[str] = Field(None, description="The month that the metadata belongs to in the format MM/YYYY.")

    model_config = {'populate_by_name': True}


class ListHistoricalReachCurvesMetadataResponseContent(BaseModel):
    """Historical Reach Curves Metadata - 200 Response."""
    metadata: Optional[list["HistoricalReachCurvesMetadata"]] = Field(None, description="List of Historical Reach Curves metadata separated by geography.")
    month: Optional[str] = Field(None, description="The month that this data belongs to.")

    model_config = {'populate_by_name': True}


class Targeting(BaseModel):
    channels: Optional[list[str]] = Field(None, description="The mode that ads were delivered. For example 'STV' and 'Prime_Video'.")
    demographics: Optional[list[str]] = Field(None, description="The demographic segments of the users included in the reach curve.")
    geography: str = Field(..., description="The geography of the users included in the reach curve.")
    reach_type: Optional[str] = Field(None, alias="reachType", description="The type of reach recorded for the data. Possible values are 'INDIVIDUALS' and 'HOUSEHOLDS'.")

    model_config = {'populate_by_name': True}


class ListHistoricalReachCurvesRequestContent(BaseModel):
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to 1000.")
    month: Optional[str] = Field(None, description="The month of data that will be returned. Defaults to the most recent month of data that is available for the given geogr")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to retrieve the next set/page of data points.")
    targeting: "Targeting"

    model_config = {'populate_by_name': True}


class ListHistoricalReachCurvesResponseContent(BaseModel):
    """Historical Reach Curves 200 response."""
    historical_reach_curves: Optional[list["HistoricalReachCurveDataPoint"]] = Field(None, alias="historicalReachCurves", description="List of data points for a curve that shows historical reach. The default list size is 1000 data points.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="The token to retrieve the next set/page of data points.")
    total_results: Optional[int] = Field(None, alias="totalResults", description="Total available data points for the requested resource.")

    model_config = {'populate_by_name': True}


class NotFoundErrorCode(StrEnum):
    NOT_FOUND = "NOT_FOUND"


class ResourceNotFoundExceptionResponseContent(BaseModel):
    """Resource Not Found. 404 Response."""
    code: "NotFoundErrorCode"
    details: Optional[str] = Field(None, description="Error details.")
    errors: Optional[list["SubError"]] = None
    message: str = Field(..., description="Human readable error message.")
    request_id: str = Field(..., alias="requestId", description="Request Id.")

    model_config = {'populate_by_name': True}


class SchemaValidationExceptionResponseContent(BaseModel):
    """SchemaValidationException 400 response."""
    code: "InvalidArgumentErrorCode"
    details: Optional[str] = Field(None, description="Error details.")
    errors: Optional[list["SubError"]] = None
    message: str = Field(..., description="Human readable error message.")
    request_id: str = Field(..., alias="requestId", description="Request Id.")

    model_config = {'populate_by_name': True}


class ThrottledErrorCode(StrEnum):
    THROTTLED = "THROTTLED"


class ThrottlingExceptionResponseContent(BaseModel):
    """ThrottlingException 429 response."""
    code: "ThrottledErrorCode"
    details: Optional[str] = Field(None, description="Error details.")
    errors: Optional[list["SubError"]] = None
    message: str = Field(..., description="Human readable error message.")
    request_id: str = Field(..., alias="requestId", description="Request Id.")

    model_config = {'populate_by_name': True}


class UnauthorizedErrorCode(StrEnum):
    UNAUTHORIZED = "UNAUTHORIZED"


class UnauthorizedExceptionResponseContent(BaseModel):
    """UnauthorizedException 401 response."""
    code: "UnauthorizedErrorCode"
    details: Optional[str] = Field(None, description="Error details.")
    errors: Optional[list["SubError"]] = None
    message: str = Field(..., description="Human readable error message.")
    request_id: str = Field(..., alias="requestId", description="Request Id.")

    model_config = {'populate_by_name': True}


class UnsupportedMediaTypeErrorCode(StrEnum):
    UNSUPPORTED_MEDIA_TYPE = "UNSUPPORTED_MEDIA_TYPE"


class UnsupportedMediaTypeExceptionResponseContent(BaseModel):
    """UnsupportedMediaTypeException 415 response."""
    code: "UnsupportedMediaTypeErrorCode"
    details: Optional[str] = Field(None, description="Error details.")
    errors: Optional[list["SubError"]] = None
    message: str = Field(..., description="Human readable error message.")
    request_id: str = Field(..., alias="requestId", description="Request Id.")

    model_config = {'populate_by_name': True}

