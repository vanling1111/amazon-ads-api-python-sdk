"""Auto-generated Pydantic models. Do not edit manually.

Source: D16GDspApiActionableInsights_prod_3p.json
Title:  D16GDspApiActionableInsights
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class AdgroupFrequencyCapType(StrEnum):
    ADGROUP_FREQUENCY_CAP = "ADGROUP_FREQUENCY_CAP"


class AdGroupFrequencyCapFilter(BaseModel):
    """Filter that can be set for adgroup level frequency cap."""
    ad_group_ids: Optional[list[str]] = Field(None, alias="adGroupIds", description="List of adGroup Ids. When this list is empty, frequency savings insights from all frequency group under the advertiser w")
    campaign_ids: Optional[list[str]] = Field(None, alias="campaignIds", description="List of campaign Ids.")
    frequency_cap_type: Optional["AdgroupFrequencyCapType"] = Field(None, alias="frequencyCapType")

    model_config = {'populate_by_name': True}


class CampaignFrequencyCapType(StrEnum):
    CAMPAIGN_FREQUENCY_CAP = "CAMPAIGN_FREQUENCY_CAP"


class CampaignFrequencyCapFilter(BaseModel):
    """Filter that can be set for campaign level frequency cap."""
    campaign_ids: Optional[list[str]] = Field(None, alias="campaignIds", description="List of campaign Ids.")
    frequency_cap_type: Optional["CampaignFrequencyCapType"] = Field(None, alias="frequencyCapType")

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


class FrequencyBin(StrEnum):
    V_1 = "1"
    V_10_ = "10+"
    V_2 = "2"
    V_3 = "3"
    V_4 = "4"
    V_5 = "5"
    V_6 = "6"
    V_7 = "7"
    V_8 = "8"
    V_9 = "9"


class FrequencyCapType(StrEnum):
    ADGROUP_FREQUENCY_CAP = "ADGROUP_FREQUENCY_CAP"
    CAMPAIGN_FREQUENCY_CAP = "CAMPAIGN_FREQUENCY_CAP"
    FREQUENCY_GROUP_FREQUENCY_CAP = "FREQUENCY_GROUP_FREQUENCY_CAP"


class FrequencyGroupFrequencyCapType(StrEnum):
    FREQUENCY_GROUP_FREQUENCY_CAP = "FREQUENCY_GROUP_FREQUENCY_CAP"


class FrequencyGroupFrequencyCapFilter(BaseModel):
    """Filter that can be set for frequency group level frequency cap."""
    frequency_cap_type: Optional["FrequencyGroupFrequencyCapType"] = Field(None, alias="frequencyCapType")
    frequency_group_ids: Optional[list[str]] = Field(None, alias="frequencyGroupIds", description="List of frequency group Ids. When this list is empty, frequency savings insights from all frequency group under the adve")

    model_config = {'populate_by_name': True}


class FrequencyCapTypeFilterUnion(BaseModel):
    pass


class TimeGrain(StrEnum):
    DAILY = "DAILY"
    MONTHLY = "MONTHLY"
    WEEKLY = "WEEKLY"


class Level(StrEnum):
    AD_GROUP = "AD_GROUP"
    CAMPAIGN = "CAMPAIGN"


class FrequencyDistributionMetricName(StrEnum):
    COMBINED_ROAS = "COMBINED_ROAS"
    COMPLETION_RATE = "COMPLETION_RATE"
    CPA = "CPA"
    CPC = "CPC"
    CPD = "CPD"
    CPDPV = "CPDPV"
    CPVC = "CPVC"
    CTR = "CTR"
    DPVR = "DPVR"
    HOUSEHOLD_COMBINED_ROAS = "HOUSEHOLD_COMBINED_ROAS"
    HOUSEHOLD_COMPLETION_RATE = "HOUSEHOLD_COMPLETION_RATE"
    HOUSEHOLD_CPA = "HOUSEHOLD_CPA"
    HOUSEHOLD_CPC = "HOUSEHOLD_CPC"
    HOUSEHOLD_CPD = "HOUSEHOLD_CPD"
    HOUSEHOLD_CPDPV = "HOUSEHOLD_CPDPV"
    HOUSEHOLD_CPVC = "HOUSEHOLD_CPVC"
    HOUSEHOLD_CTR = "HOUSEHOLD_CTR"
    HOUSEHOLD_DPVR = "HOUSEHOLD_DPVR"
    HOUSEHOLD_REACH = "HOUSEHOLD_REACH"
    HOUSEHOLD_ROAS = "HOUSEHOLD_ROAS"
    HOUSEHOLD_TOTAL_CPSU = "HOUSEHOLD_TOTAL_CPSU"
    HOUSEHOLD_TOTAL_ROAS = "HOUSEHOLD_TOTAL_ROAS"
    REACH = "REACH"
    ROAS = "ROAS"
    TOTAL_CPSU = "TOTAL_CPSU"
    TOTAL_ROAS = "TOTAL_ROAS"


class FrequencyDistributionNoDataReasonCode(StrEnum):
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"
    METRIC_NOT_APPLICABLE = "METRIC_NOT_APPLICABLE"


class FrequencyDistributionMetric(BaseModel):
    """Performance metric data."""
    metric_name: Optional["FrequencyDistributionMetricName"] = Field(None, alias="metricName")
    metric_value: Optional[float] = Field(None, alias="metricValue", description="Value of the performance metric.")
    no_data_reason_code: Optional["FrequencyDistributionNoDataReasonCode"] = Field(None, alias="noDataReasonCode")

    model_config = {'populate_by_name': True}


class FrequencyDistributionItem(BaseModel):
    """Frequency distribution insight item."""
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="ID of the ad group. Only included when level is AD_GROUP.")
    advertiser_id: Optional[str] = Field(None, alias="advertiserId", description="ID of the advertiser.")
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="ID of the campaign. Always included.")
    date: Optional[str] = Field(None, description="The date for which the data is reported.")
    frequency: Optional["FrequencyBin"] = None
    level: Optional["Level"] = None
    metrics: Optional[list["FrequencyDistributionMetric"]] = Field(None, description="Performance metrics for this frequency bin.")
    time_grain: Optional["TimeGrain"] = Field(None, alias="timeGrain")

    model_config = {'populate_by_name': True}


class FrequencyDistributionRequestFilters(BaseModel):
    """Filters to apply to the frequency distribution insights."""
    ad_group_id_filter: Optional[list[str]] = Field(None, alias="adGroupIdFilter", description="List of ad group IDs to filter by. Only applicable when level is AD_GROUP.")
    advertiser_id_filter: Optional[list[str]] = Field(None, alias="advertiserIdFilter", description="List of advertiser IDs to filter by. If not provided, data for all advertisers the user has access to will be returned. ")
    campaign_id_filter: Optional[list[str]] = Field(None, alias="campaignIdFilter", description="List of campaign IDs to filter by. When level is CAMPAIGN, this filter specifies which campaigns to retrieve data for. W")
    end_date_filter: Optional[str] = Field(None, alias="endDateFilter", description="End date until which frequency distribution insights will be returned. Must be within the past 90 days. If not set, defa")
    level_filter: Optional["Level"] = Field(None, alias="levelFilter")
    metrics_filter: Optional[list["FrequencyDistributionMetricName"]] = Field(None, alias="metricsFilter", description="List of performance metrics to include in the response.")
    start_date_filter: Optional[str] = Field(None, alias="startDateFilter", description="Start date from which frequency distribution insights will be returned. Must be within the past 90 days. If not set, def")
    time_grain_filter: Optional["TimeGrain"] = Field(None, alias="timeGrainFilter")

    model_config = {'populate_by_name': True}


class FrequencyDistributionRequest(BaseModel):
    """Request object to fetch frequency distribution insights for ad groups and campaigns."""
    filters: "FrequencyDistributionRequestFilters"
    max_results: Optional[int] = Field(None, alias="maxResults", description="Maximum number of results to return per page. Minimum: 0, Maximum: 10000, Default: 10000")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to fetch additional results (if any). Subsequent calls must be made with same parameters as in the previous reques")

    model_config = {'populate_by_name': True}


class FrequencyDistributionResponse(BaseModel):
    """Response object containing frequency distribution insights."""
    frequency_distribution_insights: Optional[list["FrequencyDistributionItem"]] = Field(None, alias="frequencyDistributionInsights", description="List of frequency distribution insights.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to fetch additional results (if any). Subsequent calls must be made with same parameters as in the previous reques")

    model_config = {'populate_by_name': True}


class NoDataReasonCode(StrEnum):
    FREQUENCY_CAP_NOT_REACHED = "FREQUENCY_CAP_NOT_REACHED"
    FREQUENCY_CAP_NOT_SET = "FREQUENCY_CAP_NOT_SET"
    NOT_AVAILABLE = "NOT_AVAILABLE"


class MetricName(StrEnum):
    HOUSEHOLD_SAVINGS_REINVESTED_AMOUNT = "HOUSEHOLD_SAVINGS_REINVESTED_AMOUNT"
    INCREMENTAL_HOUSEHOLD_COUNT = "INCREMENTAL_HOUSEHOLD_COUNT"
    INCREMENTAL_USERS_COUNT = "INCREMENTAL_USERS_COUNT"
    SAVED_HOUSEHOLD_IMPRESSIONS_COUNT = "SAVED_HOUSEHOLD_IMPRESSIONS_COUNT"
    SAVED_IMPRESSIONS_COUNT = "SAVED_IMPRESSIONS_COUNT"
    SAVINGS_REINVESTED_AMOUNT = "SAVINGS_REINVESTED_AMOUNT"
    UNIQUE_HOUSEHOLD_COUNT = "UNIQUE_HOUSEHOLD_COUNT"
    UNIQUE_USERS_COUNT = "UNIQUE_USERS_COUNT"


class Metrics(BaseModel):
    currency_code: Optional[str] = Field(None, alias="currencyCode")
    metric_name: Optional["MetricName"] = Field(None, alias="metricName")
    metric_value: Optional[float] = Field(None, alias="metricValue")
    no_data_reason_code: Optional["NoDataReasonCode"] = Field(None, alias="noDataReasonCode")

    model_config = {'populate_by_name': True}


class FrequencySavingsInsights(BaseModel):
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="Represents the ID of the adgroup associated with the frequency savings insight. Will be included if adGroupFrequencyCapF")
    advertiser_id: Optional[str] = Field(None, alias="advertiserId", description="Represents the ID of the advertiser associated with the frequency savings insight.")
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="Represents the ID of the campaign associated with the insight. Will be included if campaignFrequencyCapFilter or adGroup")
    date: Optional[str] = Field(None, description="Represents the day of the insight.")
    frequency_group_id: Optional[str] = Field(None, alias="frequencyGroupId", description="Represents the ID of the frequency group associated with the insight. Will be included if frequencyGroupFrequencyCapfilt")
    metrics: Optional["Metrics"] = None

    model_config = {'populate_by_name': True}


class ListFrequencySavingsInsightsRequestFilters(BaseModel):
    advertiser_id_filter: Optional[list[str]] = Field(None, alias="advertiserIdFilter", description="List of advertiser Ids.")
    end_date_filter: Optional[str] = Field(None, alias="endDateFilter", description="end date until which frequency savings insights will be returned.")
    frequency_cap_type_filter: Optional["FrequencyCapTypeFilterUnion"] = Field(None, alias="frequencyCapTypeFilter")
    metrics_filter: Optional[list["MetricName"]] = Field(None, alias="metricsFilter", description="List of metric names you would like to be included in the results.")
    start_date_filter: Optional[str] = Field(None, alias="startDateFilter", description="start date from which frequency savings insights will be returned.")

    model_config = {'populate_by_name': True}


class ListFrequencySavingsInsightsRequestContent(BaseModel):
    """Request object to fetch frequency savings insights."""
    filters: "ListFrequencySavingsInsightsRequestFilters"
    max_results: Optional[int] = Field(None, alias="maxResults", description="max results to return per page.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to fetch additional results (if any). Subsequent calls must be made with same parameters as in the previous reques")

    model_config = {'populate_by_name': True}


class ListFrequencySavingsInsightsResponseContent(BaseModel):
    """Response object containing frequency savings insights."""
    frequency_cap_type: Optional["FrequencyCapType"] = Field(None, alias="frequencyCapType")
    frequency_savings_insights: Optional[list["FrequencySavingsInsights"]] = Field(None, alias="frequencySavingsInsights", description="List of frequency savings insights.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to fetch additional results (if any). Subsequent calls must be made with same  parameters as in the previous reque")

    model_config = {'populate_by_name': True}

