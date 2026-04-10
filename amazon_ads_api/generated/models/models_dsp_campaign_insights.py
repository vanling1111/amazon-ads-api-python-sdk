"""Auto-generated Pydantic models. Do not edit manually.

Source: D16GDspApiCampaignInsightsV1_prod_3p.json
Title:  D16GDspApiCampaignInsightsV1
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class PerformancePlusShopperTrait(BaseModel):
    cost: Optional[float] = None
    impression_share: float = Field(..., alias="impressionShare")
    impressions: Optional[int] = None
    median_time_to_convert_in_hours_per_trait: Optional[float] = Field(None, alias="medianTimeToConvertInHoursPerTrait")
    off_amazon_conversions: Optional[int] = Field(None, alias="offAmazonConversions")
    shopper_trait_description: str = Field(..., alias="shopperTraitDescription")
    shopper_trait_index: int = Field(..., alias="shopperTraitIndex")
    shopper_trait_name: str = Field(..., alias="shopperTraitName")
    total_purchases: Optional[int] = Field(None, alias="totalPurchases")

    model_config = {'populate_by_name': True}


class PerformancePlusTargetingTactic(StrEnum):
    ALL = "All"
    CUSTOMER_ACQUISITION = "Customer Acquisition"
    PROSPECTING = "Prospecting"
    REMARKETING = "Remarketing"
    RETENTION = "Retention"
    UNIFIED_CONSIDERATION = "Unified Consideration"


class TimeToConvertBucket(BaseModel):
    conversion_share: float = Field(..., alias="conversionShare")
    range: str

    model_config = {'populate_by_name': True}


class PerformancePlusShopperTraitInsight(BaseModel):
    median_time_to_convert_in_hours: float = Field(..., alias="medianTimeToConvertInHours")
    performance_plus_shopper_traits: list["PerformancePlusShopperTrait"] = Field(..., alias="performancePlusShopperTraits")
    performance_plus_targeting_tactic: "PerformancePlusTargetingTactic" = Field(..., alias="performancePlusTargetingTactic")
    time_to_convert_buckets: list["TimeToConvertBucket"] = Field(..., alias="timeToConvertBuckets")

    model_config = {'populate_by_name': True}


class InsightsUnion(BaseModel):
    pass


class CampaignInsight(BaseModel):
    ad_group_id: Optional[str] = Field(None, alias="adGroupId")
    insights: "InsightsUnion"

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


class ErrorResponse(BaseModel):
    ad_group_id: Optional[str] = Field(None, alias="adGroupId")
    campaign_id: str = Field(..., alias="campaignId")
    error_code: int = Field(..., alias="errorCode")
    error_message: str = Field(..., alias="errorMessage")
    index: int

    model_config = {'populate_by_name': True}


class InsightType(StrEnum):
    PERFORMANCE_PLUS_SHOPPER_TRAIT = "PERFORMANCE_PLUS_SHOPPER_TRAIT"


class InsightRequest(BaseModel):
    ad_group_id: Optional[str] = Field(None, alias="adGroupId")
    campaign_id: str = Field(..., alias="campaignId")
    insight_type: "InsightType" = Field(..., alias="insightType")

    model_config = {'populate_by_name': True}


class ListDspCampaignInsightsRequestContent(BaseModel):
    requests: list["InsightRequest"]

    model_config = {'populate_by_name': True}


class SuccessInsightsResponse(BaseModel):
    campaign_id: str = Field(..., alias="campaignId")
    campaign_insights: list["CampaignInsight"] = Field(..., alias="campaignInsights")
    index: int
    insight_date: Optional[str] = Field(None, alias="insightDate")

    model_config = {'populate_by_name': True}


class ListDspCampaignInsightsResponseContent(BaseModel):
    error: Optional[list["ErrorResponse"]] = None
    success: Optional[list["SuccessInsightsResponse"]] = None

    model_config = {'populate_by_name': True}

