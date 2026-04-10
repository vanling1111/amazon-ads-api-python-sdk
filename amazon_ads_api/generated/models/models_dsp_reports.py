"""Auto-generated Pydantic models. Do not edit manually.

Source: DSPReports_prod_3p.json
Title:  DSP Reports
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class CreateReportRequestBodyV3Dimensions(StrEnum):
    BROWSER_TYPE = "BROWSER_TYPE"
    BROWSER_VERSION = "BROWSER_VERSION"
    CITY = "CITY"
    CONVERSION_SOURCE = "CONVERSION_SOURCE"
    COUNTRY = "COUNTRY"
    CREATIVE = "CREATIVE"
    DEAL = "DEAL"
    DEVICE_TYPE = "DEVICE_TYPE"
    DMA = "DMA"
    ENVIRONMENT_TYPE = "ENVIRONMENT_TYPE"
    LINE_ITEM = "LINE_ITEM"
    OPERATING_SYSTEM = "OPERATING_SYSTEM"
    ORDER = "ORDER"
    POSTAL_CODE = "POSTAL_CODE"
    SITE = "SITE"
    STATE_COUNTY_REGION = "STATE_COUNTY_REGION"
    SUPPLY = "SUPPLY"


class CreateReportRequestBodyV3Format(StrEnum):
    CSV = "CSV"
    JSON = "JSON"


class CreateReportRequestBodyV3Timeunit(StrEnum):
    DAILY = "DAILY"
    SUMMARY = "SUMMARY"


class CreateReportRequestBodyV3Type(StrEnum):
    AUDIENCE = "AUDIENCE"
    CAMPAIGN = "CAMPAIGN"
    CONVERSION_SOURCE = "CONVERSION_SOURCE"
    GEOGRAPHY = "GEOGRAPHY"
    INVENTORY = "INVENTORY"
    PRODUCTS = "PRODUCTS"
    TECHNOLOGY = "TECHNOLOGY"


class CreateReportRequestBodyV3(BaseModel):
    advertiser_ids: Optional[list[str]] = Field(None, alias="advertiserIds", description="List of advertisers specified by identifier to include in the report. This should not be present if accountId is adverti")
    dimensions: Optional[list[CreateReportRequestBodyV3Dimensions]] = Field(None, description="List of dimensions to include in the report. Specify one or many comma-delimited strings of dimensions. For example: ['O")
    end_date: str = Field(..., alias="endDate", description="Date in yyyy-MM-dd format. The report contains only metrics generated on the specified date range between startDate and ")
    format_: Optional[CreateReportRequestBodyV3Format] = Field(None, alias="format", description="The report file format.")
    metrics: Optional[list[str]] = Field(None, description="Specify a list of metrics field names to include in the report. For example: ['impressions', 'clickThroughs', 'CTR', 'eC")
    order_ids: Optional[list[str]] = Field(None, alias="orderIds", description="List of orders specified by identifier to include in the report.")
    start_date: str = Field(..., alias="startDate", description="Date in yyyy-MM-dd format. The report contains only metrics generated on the specified date range between startDate and ")
    time_unit: Optional[CreateReportRequestBodyV3Timeunit] = Field(None, alias="timeUnit", description="Adding timeUnit determines the aggregation level (`SUMMARY` or `DAILY`) of the report data. If the timeUnit is null or e")
    type_: Optional[CreateReportRequestBodyV3Type] = Field(None, alias="type", description="The report type.")

    model_config = {'populate_by_name': True}


class DSPReportsSubError(BaseModel):
    """The sub-error object."""
    error_type: str = Field(..., alias="errorType", description="Enumerated error type.")
    field: Optional[str] = Field(None, description="Request body field which is cause of the error.")
    message: str = Field(..., description="Detailed error description")

    model_config = {'populate_by_name': True}


class DSPReportsError(BaseModel):
    """The error response object."""
    errors: Optional[list["DSPReportsSubError"]] = Field(None, description="A list of errors. Please check the values in this field for report validation errors.")
    message: str = Field(..., description="A human-readable description of the response.")
    request_id: Optional[str] = Field(None, alias="requestId", description="A unique identifier of the request.")

    model_config = {'populate_by_name': True}


class ReportMetadataV3Format(StrEnum):
    CSV = "CSV"
    JSON = "JSON"


class ReportMetadataV3Status(StrEnum):
    FAILURE = "FAILURE"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"


class ReportMetadataV3Type(StrEnum):
    AUDIENCE = "AUDIENCE"
    CAMPAIGN = "CAMPAIGN"
    CONVERSION_SOURCE = "CONVERSION_SOURCE"
    GEOGRAPHY = "GEOGRAPHY"
    INVENTORY = "INVENTORY"
    PRODUCTS = "PRODUCTS"
    TECHNOLOGY = "TECHNOLOGY"


class ReportMetadataV3(BaseModel):
    expiration: Optional[str] = Field(None, description="The expiration time of the URI in the location property in date-time format(yyyy-MM-ddTHH:mm:ss). The expiration time is")
    format_: Optional[ReportMetadataV3Format] = Field(None, alias="format", description="The data format of the report.")
    location: Optional[str] = Field(None, description="The URI address of the report.")
    report_id: Optional[str] = Field(None, alias="reportId", description="The identifier of the report.")
    status: Optional[ReportMetadataV3Status] = Field(None, description="The build status of the report.")
    status_details: Optional[str] = Field(None, alias="statusDetails", description="A human-readable description of the current status.")
    type_: Optional[ReportMetadataV3Type] = Field(None, alias="type", description="The type of report.")

    model_config = {'populate_by_name': True}

