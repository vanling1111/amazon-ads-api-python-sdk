"""Auto-generated Pydantic models. Do not edit manually.

Source: DSP_Reports_v2_openapi.yaml
Title:  DSP Reports
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class DSPReportsSubError(BaseModel):
    """The sub-error object."""
    field: Optional[str] = Field(None, description="Request body field which is cause of the error.")
    error_type: str = Field(..., alias="errorType", description="Enumerated error type.")
    message: str = Field(..., description="Detailed error description")

    model_config = {'populate_by_name': True}


class DSPReportsError(BaseModel):
    """The error response object."""
    request_id: Optional[str] = Field(None, alias="requestId", description="A unique identifier of the request.")
    message: str = Field(..., description="A human-readable description of the response.")
    errors: Optional[list["DSPReportsSubError"]] = Field(None, description="A list of errors. Please check the values in this field for report validation errors.")

    model_config = {'populate_by_name': True}


class ReportMetadataV2Format(StrEnum):
    JSON = "JSON"
    CSV = "CSV"


class ReportMetadataV2Type(StrEnum):
    CAMPAIGN = "CAMPAIGN"
    INVENTORY = "INVENTORY"
    AUDIENCE = "AUDIENCE"
    PRODUCTS = "PRODUCTS"
    TECHNOLOGY = "TECHNOLOGY"
    GEOGRAPHY = "GEOGRAPHY"


class ReportMetadataV2Status(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class ReportMetadataV2(BaseModel):
    report_id: Optional[str] = Field(None, alias="reportId", description="The identifier of the report.")
    format_: Optional[ReportMetadataV2Format] = Field(None, alias="format", description="The data format of the report.")
    status_details: Optional[str] = Field(None, alias="statusDetails", description="A human-readable description of the current status.")
    location: Optional[str] = Field(None, description="The URI address of the report.")
    expiration: Optional[int] = Field(None, description="The expiration time of the URI in the location property in milliseconds. The expiration time is the interval between the")
    type_: Optional[ReportMetadataV2Type] = Field(None, alias="type", description="The type of report.")
    status: Optional[ReportMetadataV2Status] = Field(None, description="The build status of the report.")

    model_config = {'populate_by_name': True}


class CreateReportRequestBodyV2Format(StrEnum):
    JSON = "JSON"
    CSV = "CSV"


class CreateReportRequestBodyV2Type(StrEnum):
    CAMPAIGN = "CAMPAIGN"
    INVENTORY = "INVENTORY"
    AUDIENCE = "AUDIENCE"
    PRODUCTS = "PRODUCTS"
    TECHNOLOGY = "TECHNOLOGY"
    GEOGRAPHY = "GEOGRAPHY"


class CreateReportRequestBodyV2Dimensions(StrEnum):
    ORDER = "ORDER"
    LINE_ITEM = "LINE_ITEM"
    CREATIVE = "CREATIVE"
    SITE = "SITE"
    SUPPLY = "SUPPLY"
    DEAL = "DEAL"
    COUNTRY = "COUNTRY"
    STATE_COUNTY_REGION = "STATE_COUNTY_REGION"
    CITY = "CITY"
    DMA = "DMA"
    POSTAL_CODE = "POSTAL_CODE"
    OPERATING_SYSTEM = "OPERATING_SYSTEM"
    BROWSER_TYPE = "BROWSER_TYPE"
    BROWSER_VERSION = "BROWSER_VERSION"
    DEVICE_TYPE = "DEVICE_TYPE"
    ENVIRONMENT_TYPE = "ENVIRONMENT_TYPE"


class CreateReportRequestBodyV2Timeunit(StrEnum):
    DAILY = "DAILY"
    SUMMARY = "SUMMARY"


class CreateReportRequestBodyV2(BaseModel):
    advertiser_ids: Optional[list[str]] = Field(None, alias="advertiserIds", description="List of advertisers specified by identifier to include in the report. If this field is not specified, the report include")
    end_date: str = Field(..., alias="endDate", description="Date in YYYYMMDD format. The report contains only metrics generated on the specified date range between startDate and en")
    format_: Optional[CreateReportRequestBodyV2Format] = Field(None, alias="format", description="The report file format.")
    order_ids: Optional[list[str]] = Field(None, alias="orderIds", description="List of orders specified by identifier to include in the report. If this field is not specified, the report includes dat")
    metrics: Optional[str] = Field(None, description="Specify a comma-delimited string of metrics field names to include in the report. For example: 'impressions, clickThroug")
    type_: Optional[CreateReportRequestBodyV2Type] = Field(None, alias="type", description="The report type.")
    start_date: str = Field(..., alias="startDate", description="Date in YYYYMMDD format. The report contains only metrics generated on the specified date range between startDate and en")
    dimensions: Optional[list[CreateReportRequestBodyV2Dimensions]] = Field(None, description="List of dimensions to include in the report. Specify one or many comma-delimited strings of dimensions. For example: ['O")
    time_unit: Optional[CreateReportRequestBodyV2Timeunit] = Field(None, alias="timeUnit", description="Adding timeUnit determines the aggregation level (`SUMMARY` or `DAILY`) of the report data. If the timeUnit is null or e")

    model_config = {'populate_by_name': True}


class CreateReportRequestBodyV3Format(StrEnum):
    JSON = "JSON"
    CSV = "CSV"


class CreateReportRequestBodyV3Type(StrEnum):
    CAMPAIGN = "CAMPAIGN"
    INVENTORY = "INVENTORY"
    AUDIENCE = "AUDIENCE"
    PRODUCTS = "PRODUCTS"
    TECHNOLOGY = "TECHNOLOGY"
    GEOGRAPHY = "GEOGRAPHY"


class CreateReportRequestBodyV3Dimensions(StrEnum):
    ORDER = "ORDER"
    LINE_ITEM = "LINE_ITEM"
    CREATIVE = "CREATIVE"
    SITE = "SITE"
    SUPPLY = "SUPPLY"
    DEAL = "DEAL"
    COUNTRY = "COUNTRY"
    STATE_COUNTY_REGION = "STATE_COUNTY_REGION"
    CITY = "CITY"
    DMA = "DMA"
    POSTAL_CODE = "POSTAL_CODE"
    OPERATING_SYSTEM = "OPERATING_SYSTEM"
    BROWSER_TYPE = "BROWSER_TYPE"
    BROWSER_VERSION = "BROWSER_VERSION"
    DEVICE_TYPE = "DEVICE_TYPE"
    ENVIRONMENT_TYPE = "ENVIRONMENT_TYPE"


class CreateReportRequestBodyV3Timeunit(StrEnum):
    DAILY = "DAILY"
    SUMMARY = "SUMMARY"


class CreateReportRequestBodyV3(BaseModel):
    advertiser_ids: Optional[list[str]] = Field(None, alias="advertiserIds", description="List of advertisers specified by identifier to include in the report. This should not be present if accountId is adverti")
    end_date: str = Field(..., alias="endDate", description="Date in yyyy-MM-dd format. The report contains only metrics generated on the specified date range between startDate and ")
    format_: Optional[CreateReportRequestBodyV3Format] = Field(None, alias="format", description="The report file format.")
    order_ids: Optional[list[str]] = Field(None, alias="orderIds", description="List of orders specified by identifier to include in the report.")
    metrics: Optional[list[str]] = Field(None, description="Specify a list of metrics field names to include in the report. For example: ['impressions', 'clickThroughs', 'CTR', 'eC")
    type_: Optional[CreateReportRequestBodyV3Type] = Field(None, alias="type", description="The report type.")
    start_date: str = Field(..., alias="startDate", description="Date in yyyy-MM-dd format. The report contains only metrics generated on the specified date range between startDate and ")
    dimensions: Optional[list[CreateReportRequestBodyV3Dimensions]] = Field(None, description="List of dimensions to include in the report. Specify one or many comma-delimited strings of dimensions. For example: ['O")
    time_unit: Optional[CreateReportRequestBodyV3Timeunit] = Field(None, alias="timeUnit", description="Adding timeUnit determines the aggregation level (`SUMMARY` or `DAILY`) of the report data. If the timeUnit is null or e")

    model_config = {'populate_by_name': True}


class ReportMetadataV3Format(StrEnum):
    JSON = "JSON"
    CSV = "CSV"


class ReportMetadataV3Type(StrEnum):
    CAMPAIGN = "CAMPAIGN"
    INVENTORY = "INVENTORY"
    AUDIENCE = "AUDIENCE"
    PRODUCTS = "PRODUCTS"
    TECHNOLOGY = "TECHNOLOGY"
    GEOGRAPHY = "GEOGRAPHY"


class ReportMetadataV3Status(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class ReportMetadataV3(BaseModel):
    report_id: Optional[str] = Field(None, alias="reportId", description="The identifier of the report.")
    format_: Optional[ReportMetadataV3Format] = Field(None, alias="format", description="The data format of the report.")
    status_details: Optional[str] = Field(None, alias="statusDetails", description="A human-readable description of the current status.")
    location: Optional[str] = Field(None, description="The URI address of the report.")
    expiration: Optional[str] = Field(None, description="The expiration time of the URI in the location property in date-time format(yyyy-MM-ddTHH:mm:ss). The expiration time is")
    type_: Optional[ReportMetadataV3Type] = Field(None, alias="type", description="The type of report.")
    status: Optional[ReportMetadataV3Status] = Field(None, description="The build status of the report.")

    model_config = {'populate_by_name': True}

