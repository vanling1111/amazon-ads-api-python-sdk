"""Auto-generated Pydantic models. Do not edit manually.

Source: D16GFMApiFrequencyGroupV1_prod_3p.json
Title:  D16GFMApiFrequencyGroupV1
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class AdvertiserIdFilter(BaseModel):
    """Filter frequency groups by the list of advertiser ids."""
    include: Optional[list[str]] = None

    model_config = {'populate_by_name': True}


class FrequencyGroupTimeUnitV1(StrEnum):
    DAYS = "DAYS"
    HOURS = "HOURS"
    MINUTES = "MINUTES"
    OTHER = "OTHER"


class CreateFrequencyGroupRequestContentV1(BaseModel):
    advertiser_id: Optional[str] = Field(None, alias="advertiserId", description="The advertiser identifier of the advertiser who is creating the frequency groups. Used to prevent illegal operations on ")
    entity_id: Optional[str] = Field(None, alias="entityId", description="The identifier of the entity who is creating the frequency groups. Used to prevent illegal operations on a FrequencyGrou")
    entity_name: Optional[str] = Field(None, alias="entityName", description="The name of the entity who owns the frequency group")
    frequency_group_name: str = Field(..., alias="frequencyGroupName", description="The frequency group name.")
    max_impressions: float = Field(..., alias="maxImpressions", description="The maximum number of times an ad is displayed.")
    time_unit: "FrequencyGroupTimeUnitV1" = Field(..., alias="timeUnit")
    time_unit_count: float = Field(..., alias="timeUnitCount", description="The time unit count.")

    model_config = {'populate_by_name': True}


class FrequencyGroupStatusV1(StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class CreateFrequencyGroupResponseContentV1(BaseModel):
    advertiser_id: Optional[str] = Field(None, alias="advertiserId", description="The advertiser identifier of the advertiser who is creating the frequency groups. Used to prevent illegal operations on ")
    entity_id: Optional[str] = Field(None, alias="entityId", description="The identifier of the entity who is creating the frequency groups. Used to prevent illegal operations on a FrequencyGrou")
    entity_name: Optional[str] = Field(None, alias="entityName", description="The name of the entity who owns the frequency group")
    frequency_group_id: Optional[str] = Field(None, alias="frequencyGroupId", description="The frequency group identifier. Immutable field.")
    frequency_group_name: Optional[str] = Field(None, alias="frequencyGroupName", description="The frequency group name.")
    max_impressions: Optional[float] = Field(None, alias="maxImpressions", description="The maximum number of times an ad is displayed.")
    status: Optional["FrequencyGroupStatusV1"] = None
    time_unit: Optional["FrequencyGroupTimeUnitV1"] = Field(None, alias="timeUnit")
    time_unit_count: Optional[float] = Field(None, alias="timeUnitCount", description="The time unit count.")

    model_config = {'populate_by_name': True}


class CreateFrequencyGroupsV1(BaseModel):
    frequency_groups: Optional[list["CreateFrequencyGroupRequestContentV1"]] = Field(None, alias="frequencyGroups")

    model_config = {'populate_by_name': True}


class CreatedFrequencyGroupsV1(BaseModel):
    frequency_groups: Optional[list["CreateFrequencyGroupResponseContentV1"]] = Field(None, alias="frequencyGroups")

    model_config = {'populate_by_name': True}


class DspSubError(BaseModel):
    error_code: str = Field(..., alias="errorCode")
    error_id: Optional[str] = Field(None, alias="errorId")
    error_message: str = Field(..., alias="errorMessage")

    model_config = {'populate_by_name': True}


class DspBadRequestExceptionResponseContent(BaseModel):
    errors: Optional[list["DspSubError"]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspForbiddenExceptionResponseContent(BaseModel):
    errors: Optional[list["DspSubError"]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspInternalServerExceptionResponseContent(BaseModel):
    errors: Optional[list["DspSubError"]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspNotFoundExceptionResponseContent(BaseModel):
    errors: Optional[list["DspSubError"]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspTooManyRequestsExceptionResponseContent(BaseModel):
    errors: Optional[list["DspSubError"]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspUnauthorizedExceptionResponseContent(BaseModel):
    errors: Optional[list["DspSubError"]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspUnsupportedMediaTypeExceptionResponseContent(BaseModel):
    errors: Optional[list["DspSubError"]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class GetFrequencyGroupRequestContentV1(BaseModel):
    advertiser_id: Optional[str] = Field(None, alias="advertiserId", description="The advertiser identifier of the advertiser who is creating the frequency groups. Used to prevent illegal operations on ")
    entity_id: Optional[str] = Field(None, alias="entityId", description="The identifier of the entity who is creating the frequency groups. Used to prevent illegal operations on a FrequencyGrou")
    entity_name: Optional[str] = Field(None, alias="entityName", description="The name of the entity who owns the frequency group")
    frequency_group_id: Optional[str] = Field(None, alias="frequencyGroupId", description="The frequency group identifier. Immutable field.")
    frequency_group_name: Optional[str] = Field(None, alias="frequencyGroupName", description="The frequency group name.")
    max_impressions: Optional[float] = Field(None, alias="maxImpressions", description="The maximum number of times an ad is displayed.")
    status: Optional["FrequencyGroupStatusV1"] = None
    time_unit: Optional["FrequencyGroupTimeUnitV1"] = Field(None, alias="timeUnit")
    time_unit_count: Optional[float] = Field(None, alias="timeUnitCount", description="The time unit count.")

    model_config = {'populate_by_name': True}


class FrequencyGroups(BaseModel):
    frequency_groups: Optional[list["GetFrequencyGroupRequestContentV1"]] = Field(None, alias="frequencyGroups")
    next_token: Optional[str] = Field(None, alias="nextToken")
    total_results: Optional[float] = Field(None, alias="totalResults", description="The total number of results returned by an operation.")

    model_config = {'populate_by_name': True}


class ListFrequencyGroupsRequestContentV1(BaseModel):
    advertiser_id_filter: Optional["AdvertiserIdFilter"] = Field(None, alias="advertiserIdFilter")
    frequency_group_ids: Optional[list[str]] = Field(None, alias="frequencyGroupIds", description="The frequency group identifiers.")
    frequency_group_name_filter: Optional[str] = Field(None, alias="frequencyGroupNameFilter", description="Filters frequency groups by frequency group name.")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Sets the maximum number of objects in the returned array. Use in conjunction with the `nextToken` parameter to control p")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token from a previous request. Use in conjunction with the `maxResults` parameter to control the pagination of the retur")
    status_filter: Optional["FrequencyGroupStatusV1"] = Field(None, alias="statusFilter")

    model_config = {'populate_by_name': True}


class PatchFrequencyGroupRequestContentV1(BaseModel):
    frequency_group_name: Optional[str] = Field(None, alias="frequencyGroupName", description="The frequency group name.")
    max_impressions: Optional[float] = Field(None, alias="maxImpressions", description="The maximum number of times an ad is displayed.")
    status: Optional["FrequencyGroupStatusV1"] = None
    time_unit: Optional["FrequencyGroupTimeUnitV1"] = Field(None, alias="timeUnit")
    time_unit_count: Optional[float] = Field(None, alias="timeUnitCount", description="The time unit count.")

    model_config = {'populate_by_name': True}

