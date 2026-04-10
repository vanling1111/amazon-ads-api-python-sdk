"""Auto-generated Pydantic models. Do not edit manually.

Source: Rule-BasedAudiences_prod_3p.json
Title:  Rule-Based Audiences
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class CountryCodeEnum(StrEnum):
    AE = "AE"
    AU = "AU"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    ES = "ES"
    FR = "FR"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    SA = "SA"
    SE = "SE"
    TR = "TR"
    UK = "UK"
    US = "US"


class SimpleDataType(BaseModel):
    pass


class ComplexDataType(BaseModel):
    pass


class DataTypes(BaseModel):
    pass


class QueryBasedAudienceInputParam(BaseModel):
    """'Optional. Defines the parameters that can be referenced by workflow. definition. If workflow references a parameter not defined here the compilation fails.'"""
    pass


class AMCQueryBasedAudiencesRequest(BaseModel):
    """Request for create audience."""
    advertiser_id: str = Field(..., alias="advertiserId", description="Advertiser ID for which an audience is created and activated.")
    audience_description: Optional[str] = Field(None, alias="audienceDescription", description="Customer provided description for audience.")
    audience_name: str = Field(..., alias="audienceName", description="Customer provided name for audience. This has 'AMC ' prepended in DSP.")
    country_code: Optional["CountryCodeEnum"] = Field(None, alias="countryCode")
    input_parameters: Optional["QueryBasedAudienceInputParam"] = Field(None, alias="inputParameters")
    parameter_values: Optional[dict[str, Any]] = Field(None, alias="parameterValues", description="Custom parameters specified in the query.")
    query: Optional[str] = Field(None, description="Customer created query to run on AMC instance.")
    refresh_rate_days: Optional[int] = Field(None, alias="refreshRateDays", description="Customer's desired frequency for refreshing their audience in days. The rate could be set to 0 to force the audience to ")
    time_window_end: str = Field(..., alias="timeWindowEnd", description="Ending date of data to query. This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss'Z'.")
    time_window_relative: Optional[bool] = Field(None, alias="timeWindowRelative", description="If true, the time window is moved for each refresh so that the query uses more recent data. Defaults to false.")
    time_window_start: str = Field(..., alias="timeWindowStart", description="Starting date of data to query. This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss'Z'.")
    workflow_id: Optional[str] = Field(None, alias="workflowId", description="Reference to an AMC workflow")

    model_config = {'populate_by_name': True}


class AMCLookalikeAudiencesRequest(BaseModel):
    pass


class AudienceExecutionState(StrEnum):
    DEACTIVATED = "DEACTIVATED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"


class QueryBasedAudienceExecutionState(BaseModel):
    pass


class AMCQueryBasedAudiencesResponse(BaseModel):
    """Response on a successful audience creation."""
    audience_execution_description: str = Field(..., alias="audienceExecutionDescription", description="Human readable status message.")
    audience_execution_id: str = Field(..., alias="audienceExecutionId", description="Identifier that uniquely represents an AMCQueryBasedAudiencesExecutionMetadata.")
    status: "QueryBasedAudienceExecutionState"

    model_config = {'populate_by_name': True}


class AMCLookalikeAudiencesResponse(BaseModel):
    pass


class AMCQueryBasedAudiencesExecutionMetadata(BaseModel):
    """Query based audience execution metadata information."""
    advertiser_id: str = Field(..., alias="advertiserId", description="AdvertiserId to create and activate appropriate audience.")
    audience_description: Optional[str] = Field(None, alias="audienceDescription", description="Customer provided description for audience.")
    audience_execution_id: Optional[str] = Field(None, alias="audienceExecutionId", description="Identifier that uniquely represents an AMCQueryBasedAudiencesExecutionMetadata.")
    audience_name: str = Field(..., alias="audienceName", description="Customer provided name for audience. This has 'AMC ' prepended in DSP.")
    country_code: Optional["CountryCodeEnum"] = Field(None, alias="countryCode")
    create_time: str = Field(..., alias="createTime", description="Timestamp for the first time query was submitted.This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss'Z'.")
    dsp_audience_id: Optional[str] = Field(None, alias="dspAudienceId", description="Audience ID of audience in DSP.")
    instance_id: str = Field(..., alias="instanceId", description="AMC instance identifier.")
    last_refreshed_time: Optional[str] = Field(None, alias="lastRefreshedTime", description="Timestamp of the most recent refresh of the audiences created. Initially it is set to the timestamp of a successful audi")
    query: str = Field(..., description="Customer created query to run on AMC instance.")
    refresh_rate_days: Optional[int] = Field(None, alias="refreshRateDays", description="Customer's desired frequency for refreshing their audience in days.The rate could be set to 0 to force the audience to b")
    status: Optional["QueryBasedAudienceExecutionState"] = None
    status_reason: Optional[str] = Field(None, alias="statusReason", description="Description of why the audience is in its state.")
    time_window_end: str = Field(..., alias="timeWindowEnd", description="Ending date of data to query.This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss'Z'.")
    time_window_relative: Optional[bool] = Field(None, alias="timeWindowRelative", description="If true, time window is moved for each refresh so that the query uses more recent data. Defaults to false.")
    time_window_start: str = Field(..., alias="timeWindowStart", description="Starting date of data to query.This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss'Z'.")

    model_config = {'populate_by_name': True}


class AMCQueryBasedAudiencesExecutionMetadataList(BaseModel):
    execution_metadata: Optional[list["AMCQueryBasedAudiencesExecutionMetadata"]] = Field(None, alias="executionMetadata", description="List of all the executions for a given instanceId.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to use in subsequent request to retrieve next page of results. Field will be null if all results have been returne")

    model_config = {'populate_by_name': True}


class AMCQueryBasedAudiencesExecutionMetadataV11(BaseModel):
    """Query based audience execution metadata information."""
    advertiser_id: str = Field(..., alias="advertiserId", description="Advertiser ID to create and activate appropriate audience.")
    audience_count: Optional[int] = Field(None, alias="audienceCount", description="Approximate number of audience members.")
    audience_description: Optional[str] = Field(None, alias="audienceDescription", description="Customer provided description for audience.")
    audience_execution_id: Optional[str] = Field(None, alias="audienceExecutionId", description="Identifier that uniquely represents an AMCQueryBasedAudiencesExecutionMetadata.")
    audience_name: str = Field(..., alias="audienceName", description="Customer provided name for audience. This has 'AMC ' prepended in DSP.")
    country_code: Optional["CountryCodeEnum"] = Field(None, alias="countryCode")
    create_time: str = Field(..., alias="createTime", description="Timestamp for the first time query was submitted. This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss'Z'.")
    dsp_audience_id: Optional[str] = Field(None, alias="dspAudienceId", description="Audience ID of audience in DSP.")
    dsp_canonical_id: Optional[str] = Field(None, alias="dspCanonicalId", description="Canonical ID of the created audience in DSP.")
    instance_id: str = Field(..., alias="instanceId", description="AMC instance identifier.")
    last_refreshed_time: Optional[str] = Field(None, alias="lastRefreshedTime", description="Timestamp of the most recent refresh of the audiences created. Initially it is set to the timestamp of a successful audi")
    query: str = Field(..., description="Customer created query to run on AMC instance.")
    refresh_rate_days: Optional[int] = Field(None, alias="refreshRateDays", description="Customer's desired frequency for refreshing their audience in days. The rate could be set to 0 to force the audience to ")
    status: Optional["QueryBasedAudienceExecutionState"] = None
    status_reason: Optional[str] = Field(None, alias="statusReason", description="Description of why the audience is in its state.")
    time_window_end: str = Field(..., alias="timeWindowEnd", description="Ending date of data to query. This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss'Z'.")
    time_window_relative: Optional[bool] = Field(None, alias="timeWindowRelative", description="If true, time window is moved for each refresh so that the query uses more recent data. Defaults to false.")
    time_window_start: str = Field(..., alias="timeWindowStart", description="Starting date of data to query. This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss'Z'.")

    model_config = {'populate_by_name': True}


class AMCQueryBasedAudiencesExecutionMetadataListV11(BaseModel):
    execution_metadata: Optional[list["AMCQueryBasedAudiencesExecutionMetadataV11"]] = Field(None, alias="executionMetadata", description="List of all the executions for a given instanceId.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to use in subsequent request to retrieve next page of results. Field will be null if all results have been returne")

    model_config = {'populate_by_name': True}


class AdvertiserType(StrEnum):
    DISPLAY = "DISPLAY"
    SPONSORED_ADS = "SPONSORED_ADS"


class AMCQueryBasedAudiencesExecutionMetadataV12(BaseModel):
    """Query based audience execution metadata information."""
    advertiser_id: str = Field(..., alias="advertiserId", description="Advertiser ID to create and activate appropriate audience.")
    advertiser_type: Optional["AdvertiserType"] = Field(None, alias="advertiserType")
    audience_count: Optional[int] = Field(None, alias="audienceCount", description="Approximate number of audience members.")
    audience_description: Optional[str] = Field(None, alias="audienceDescription", description="Customer provided description for audience.")
    audience_execution_id: Optional[str] = Field(None, alias="audienceExecutionId", description="Identifier that uniquely represents an AMCQueryBasedAudiencesExecutionMetadata.")
    audience_name: str = Field(..., alias="audienceName", description="Customer provided name for audience. This has 'AMC ' prepended in DSP.")
    audience_type: Optional[str] = Field(None, alias="audienceType", description="The type of the audience: RULE_BASED or LOOKALIKE.")
    country_code: Optional["CountryCodeEnum"] = Field(None, alias="countryCode")
    create_time: str = Field(..., alias="createTime", description="Timestamp for the first time query was submitted. This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss'Z'.")
    deletable: Optional[bool] = Field(None, description="Whether the customer can delete this audience at this time.")
    dsp_audience_id: Optional[str] = Field(None, alias="dspAudienceId", description="Audience ID of audience in DSP.")
    dsp_canonical_id: Optional[str] = Field(None, alias="dspCanonicalId", description="CanonicalId of the created audience in DSP.")
    input_parameters: Optional["QueryBasedAudienceInputParam"] = Field(None, alias="inputParameters")
    instance_id: str = Field(..., alias="instanceId", description="AMC instance identifier.")
    last_refreshed_time: Optional[str] = Field(None, alias="lastRefreshedTime", description="Timestamp of the most recent refresh of the audiences created. Initially it is set to the timestamp of a successful audi")
    lookalike_audience_expected_reach: Optional[str] = Field(None, alias="lookalikeAudienceExpectedReach", description="Preference of more broad versus more similar audiences. The available options are MOST_SIMILAR, SIMILAR, BALANCED, BROAD")
    no3p_trackers: Optional[bool] = Field(None, alias="no3pTrackers", description="Is this audience not allowed to use 3P tracking")
    parameter_values: Optional[dict[str, Any]] = Field(None, alias="parameterValues", description="Custom parameters specified in the query.")
    query: str = Field(..., description="Customer created query to run on AMC instance.")
    refresh_rate_days: Optional[int] = Field(None, alias="refreshRateDays", description="Customer's desired frequency for refreshing their audience in days. The rate could be set to 0 to force the audience to ")
    status: Optional["QueryBasedAudienceExecutionState"] = None
    status_reason: Optional[str] = Field(None, alias="statusReason", description="Description of why the audience is in its state.")
    time_window_end: str = Field(..., alias="timeWindowEnd", description="Ending date of data to query. This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss'Z'.")
    time_window_relative: Optional[bool] = Field(None, alias="timeWindowRelative", description="If true, time window is moved for each refresh so that the query uses more recent data. Defaults to false.")
    time_window_start: str = Field(..., alias="timeWindowStart", description="Starting date of data to query. This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss'Z'.")
    workflow_id: Optional[str] = Field(None, alias="workflowId", description="Reference to an AMC workflow")

    model_config = {'populate_by_name': True}


class AMCQueryBasedAudiencesExecutionMetadataListV12(BaseModel):
    execution_metadata: Optional[list["AMCQueryBasedAudiencesExecutionMetadataV12"]] = Field(None, alias="executionMetadata", description="List of all the executions for a given instanceId.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to use in subsequent request to retrieve next page of results. Field will be null if all results have been returne")

    model_config = {'populate_by_name': True}


class AMCQueryBasedAudiencesUpdateRequest(BaseModel):
    """Request to update an audience, replacing its configuration with the one provided. Some attributes are not modifiable at this time, but are required because they may become modifiable in the future."""
    advertiser_id: str = Field(..., alias="advertiserId", description="Advertiser ID for which an audience is created and activated. This must be the same as the existing value.")
    audience_description: Optional[str] = Field(None, alias="audienceDescription", description="Customer provided description for audience. This must be the same as the existing value, and must be provided if and onl")
    audience_name: str = Field(..., alias="audienceName", description="Customer provided name for audience. This has 'AMC ' prepended in DSP. This must be the same as the existing value.")
    audience_type: str = Field(..., alias="audienceType", description="The type of the audience: RULE_BASED or LOOKALIKE. This must be the same as the existing value.")
    country_code: Optional["CountryCodeEnum"] = Field(None, alias="countryCode")
    input_parameters: Optional["QueryBasedAudienceInputParam"] = Field(None, alias="inputParameters")
    lookalike_audience_expected_reach: Optional[str] = Field(None, alias="lookalikeAudienceExpectedReach", description="Preference of more broad versus more similar Lookalike audiences. The available options are MOST_SIMILAR, SIMILAR, BALAN")
    parameter_values: Optional[dict[str, Any]] = Field(None, alias="parameterValues", description="Custom parameters specified in the query.")
    query: Optional[str] = Field(None, description="Customer created query to run on AMC instance.")
    time_window_end: str = Field(..., alias="timeWindowEnd", description="Ending date of data to query. This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss'Z'.")
    time_window_relative: Optional[bool] = Field(None, alias="timeWindowRelative", description="If true, the time window is moved for each refresh so that the query uses more recent data. Defaults to false.")
    time_window_start: str = Field(..., alias="timeWindowStart", description="Starting date of data to query. This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss'Z'.")
    workflow_id: Optional[str] = Field(None, alias="workflowId", description="Reference to an AMC workflow")

    model_config = {'populate_by_name': True}


class AMCQueryBasedAudiencesUpdateResponse(BaseModel):
    """Response on a successful update of an audience."""
    audience_execution_description: str = Field(..., alias="audienceExecutionDescription", description="Human readable status message.")
    audience_execution_id: str = Field(..., alias="audienceExecutionId", description="Identifier that uniquely represents an AMCQueryBasedAudiencesExecutionMetadata.")
    status: "QueryBasedAudienceExecutionState"

    model_config = {'populate_by_name': True}


class AudienceError(BaseModel):
    """Error response object."""
    code: Optional[str] = Field(None, description="HTTP status code of the response.")
    details: Optional[str] = Field(None, description="Human-readable description of the response.")
    request_id: Optional[str] = Field(None, alias="requestId", description="Value created by Amazon API Gateway that uniquely identifies your request")

    model_config = {'populate_by_name': True}


class LookalikeAudienceErrorResponse(BaseModel):
    pass


class QueryBasedAudienceErrorResponse(BaseModel):
    pass

