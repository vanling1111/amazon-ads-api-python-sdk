"""Auto-generated Pydantic models. Do not edit manually.

Source: MarketingMixModeling_prod_3p.json
Title:  Marketing Mix Modeling
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class MmmError(BaseModel):
    code: Optional[str] = Field(None, description="Error code.")
    message: Optional[str] = Field(None, description="Human-readable error message.")

    model_config = {'populate_by_name': True}


class MmmBrandGroupOverrideIdentifiertype(StrEnum):
    ASIN = "ASIN"
    CAMPAIGN_ID = "CAMPAIGN_ID"


class MmmBrandGroupOverrideOverridetype(StrEnum):
    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"


class MmmBrandGroupOverrideStatus(StrEnum):
    APPROVED = "APPROVED"
    NOT_APPROVED = "NOT_APPROVED"
    PENDING_REVIEW = "PENDING_REVIEW"


class MmmBrandGroupOverride(BaseModel):
    brand_group_id: Optional[str] = Field(None, alias="brandGroupId", description="The unique identifier of the brand group to override.")
    identifier_type: Optional[MmmBrandGroupOverrideIdentifiertype] = Field(None, alias="identifierType", description="The type of identifier.")
    identifier_value: Optional[str] = Field(None, alias="identifierValue", description="The identifier value.")
    override_id: Optional[str] = Field(None, alias="overrideId", description="The unique identifier of the override.")
    override_type: Optional[MmmBrandGroupOverrideOverridetype] = Field(None, alias="overrideType", description="The type of override.")
    status: Optional[MmmBrandGroupOverrideStatus] = Field(None, description="The override status. |Value|Description| |---|---| |PENDING_REVIEW|Override must be reviewed by Amazon. New reports for ")

    model_config = {'populate_by_name': True}


class BulkMmmBrandGroupOverridesOperationResponseError(BaseModel):
    error: Optional["MmmError"] = None
    index: Optional[int] = Field(None, description="The index of the override in the array from the request body.")

    model_config = {'populate_by_name': True}


class BulkMmmBrandGroupOverridesOperationResponseSuccess(BaseModel):
    index: Optional[int] = Field(None, description="The index of the override in the array from the request body.")
    override: Optional["MmmBrandGroupOverride"] = None

    model_config = {'populate_by_name': True}


class BulkMmmBrandGroupOverridesOperationResponse(BaseModel):
    error: Optional[list["BulkMmmBrandGroupOverridesOperationResponseError"]] = None
    success: Optional[list["BulkMmmBrandGroupOverridesOperationResponseSuccess"]] = None

    model_config = {'populate_by_name': True}


class MmmBrandGroupPermittedmetricstypes(StrEnum):
    MEDIA_AND_SALES = "MEDIA_AND_SALES"
    MEDIA_ONLY = "MEDIA_ONLY"


class MmmBrandGroup(BaseModel):
    """The predefined brand or group of products being reported on."""
    advertiser_name: Optional[str] = Field(None, alias="advertiserName", description="Name of the advertiser associated with the brand group.")
    brand_group_id: Optional[str] = Field(None, alias="brandGroupId", description="The unique identifier of the brand group.")
    brand_group_name: Optional[str] = Field(None, alias="brandGroupName", description="The display name of the brand group.")
    country_code: Optional[str] = Field(None, alias="countryCode", description="The ISO 3166 country code of the marketplace associated with the brand group.")
    permitted_metrics_types: Optional[list[MmmBrandGroupPermittedmetricstypes]] = Field(None, alias="permittedMetricsTypes", description="The permitted metrics types for reports of this brand group.")

    model_config = {'populate_by_name': True}


class MmmBrandGroupCampaignAdproduct(StrEnum):
    AMAZON_DSP = "AMAZON_DSP"
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"
    SPONSORED_TELEVISION = "SPONSORED_TELEVISION"


class MmmBrandGroupCampaign(BaseModel):
    ad_product: Optional[MmmBrandGroupCampaignAdproduct] = Field(None, alias="adProduct", description="The ad product associated with the campaign.")
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="The unique numerical ID associated with a campaign.")
    end_date: Optional[str] = Field(None, alias="endDate", description="The end date of the campaign.")
    first_traffic_date: Optional[str] = Field(None, alias="firstTrafficDate", description="The date of the earliest traffic for the campaign.")
    last_traffic_date: Optional[str] = Field(None, alias="lastTrafficDate", description="The date of the latest traffic for the campaign.")
    name: Optional[str] = Field(None, description="The advertiser-specified name of the campaign.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The start date of the campaign.")

    model_config = {'populate_by_name': True}


class MmmBrandGroupProduct(BaseModel):
    asin: Optional[str] = Field(None, description="The Amazon Standard Identification Number (ASIN) of the product.")
    first_order_date: Optional[str] = Field(None, alias="firstOrderDate", description="The date of the earliest order of the product.")
    last_order_date: Optional[str] = Field(None, alias="lastOrderDate", description="The date of the latest order of the product.")
    product_category: Optional[str] = Field(None, alias="productCategory", description="The product category.")
    product_group: Optional[str] = Field(None, alias="productGroup", description="The product group.")
    product_subcategory: Optional[str] = Field(None, alias="productSubcategory", description="The product subcategory.")
    title: Optional[str] = Field(None, description="The product title.")

    model_config = {'populate_by_name': True}


class MmmReportConfigurationGeodimension(StrEnum):
    COUNTRY = "COUNTRY"
    DMA = "DMA"
    POSTAL_CODE = "POSTAL_CODE"


class MmmReportConfigurationMetricstype(StrEnum):
    MEDIA_AND_SALES = "MEDIA_AND_SALES"
    MEDIA_ONLY = "MEDIA_ONLY"


class MmmReportConfigurationTimeunit(StrEnum):
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"


class MmmReportConfiguration(BaseModel):
    brand_group_id: str = Field(..., alias="brandGroupId", description="Identifies the brand group being reported on.")
    geo_dimension: MmmReportConfigurationGeodimension = Field(..., alias="geoDimension", description="Geographic granularity of the report. |Value|Description| |---|---| |COUNTRY|Aggregate metrics by country.| |POSTAL_CODE")
    metrics_type: MmmReportConfigurationMetricstype = Field(..., alias="metricsType", description="The type of metrics to include in the report. |Value|Description| |---|---| |MEDIA_ONLY|Core advertising metrics only.| ")
    time_unit: MmmReportConfigurationTimeunit = Field(..., alias="timeUnit", description="Time granularity of the report. |Value|Description| |---|---| |DAILY|Aggregate metrics with daily granularity.| |WEEKLY|")

    model_config = {'populate_by_name': True}


class MmmReportStatus(StrEnum):
    CANCELED = "CANCELED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    SUCCEEDED = "SUCCEEDED"


class MmmReport(BaseModel):
    configuration: Optional["MmmReportConfiguration"] = None
    created_at: Optional[str] = Field(None, alias="createdAt", description="The date and time when the report was created.")
    description: Optional[str] = Field(None, description="A description of the report.")
    due_date: Optional[str] = Field(None, alias="dueDate", description="The due date of the report.")
    end_date: Optional[str] = Field(None, alias="endDate", description="Inclusive end of the reporting period.")
    failure_code: Optional[str] = Field(None, alias="failureCode", description="An error code indicating why the report failed. Present when the status is `FAILED`.")
    failure_message: Optional[str] = Field(None, alias="failureMessage", description="A human-readable message providing more information about the failure. Present when the status is `FAILED`.")
    report_id: Optional[str] = Field(None, alias="reportId", description="The unique identifier of the report.")
    report_name: Optional[str] = Field(None, alias="reportName", description="The display name of the report.")
    start_date: Optional[str] = Field(None, alias="startDate", description="Inclusive start of the reporting period.")
    status: Optional[MmmReportStatus] = Field(None, description="The report generation status. |Value|Description| |---|---| |PENDING|Report is created and awaiting processing.| |PROCES")
    urls: Optional[list[str]] = Field(None, description="The URLs for downloading output files. Present when the status is `SUCCEEDED`.")
    urls_expire_at: Optional[str] = Field(None, alias="urlsExpireAt", description="The expiration date of the download URLs. Present when the status is `SUCCEEDED`.")

    model_config = {'populate_by_name': True}

