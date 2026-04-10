"""Auto-generated Pydantic models. Do not edit manually.

Source: BrandMetrics_prod_3p.json
Title:  Brand Metrics
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class brandMetricsErrorErrors(BaseModel):
    error_code: Optional[str] = Field(None, alias="errorCode", description="enum indicating the category of error. Example `INVALID_HEADER`.")
    error_id: Optional[int] = Field(None, alias="errorId", description="ID to indicate the granular error.")
    error_message: Optional[str] = Field(None, alias="errorMessage", description="human readable error message for each error.")

    model_config = {'populate_by_name': True}


class brandMetricsError(BaseModel):
    """The error response object."""
    code: Optional[str] = Field(None, description="http status code.")
    details: Optional[str] = Field(None, description="high level human readable message.")
    errors: Optional[list["brandMetricsErrorErrors"]] = Field(None, description="A list of the errors encountered.")
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class brandMetricsGenerateReportRequestFormat(StrEnum):
    CSV = "CSV"
    JSON = "JSON"


class brandMetricsGenerateReportRequestLookbackperiod(StrEnum):
    V_1CM = "1CM"
    V_1M = "1M"
    V_1W = "1W"


class brandMetricsGenerateReportRequest(BaseModel):
    """Request object to generate the Brand Metrics Report."""
    brand_name: Optional[str] = Field(None, alias="brandName", description="Optional. Brand Name. If no Brand Name is passed, then all data available for all brands belonging to the entity are ret")
    category_path: Optional[list[str]] = Field(None, alias="categoryPath", description="Optional. The hierarchical path that leads to a node starting with the root node. If no Category Node Name is passed, th")
    category_tree_name: Optional[str] = Field(None, alias="categoryTreeName", description="Optional. The node at the top of a browse tree. It is the start node of a tree.")
    format_: Optional[brandMetricsGenerateReportRequestFormat] = Field(None, alias="format", description="Format of the report.")
    look_back_period: Optional[brandMetricsGenerateReportRequestLookbackperiod] = Field(None, alias="lookBackPeriod", description="Currently supported values: '1w' (one week), '1m' (one month) and  '1cm' (one calendar month). This defines the period o")
    metrics: Optional[list[str]] = Field(None, description="Optional. Specify an array of string of metrics field names to include in the report. If no metric field names are speci")
    report_end_date: Optional[str] = Field(None, alias="reportEndDate", description="Optional. Retrieves metrics with metricsComputationDate between reportStartDate and reportEndDate (inclusive). The maxim")
    report_start_date: Optional[str] = Field(None, alias="reportStartDate", description="Optional. Retrieves metrics with metricsComputationDate between reportStartDate and reportEndDate (inclusive). The maxim")

    model_config = {'populate_by_name': True}


class brandMetricsGenerateReportRequestV11Format(StrEnum):
    CSV = "CSV"
    JSON = "JSON"


class brandMetricsGenerateReportRequestV11Lookbackperiod(StrEnum):
    V_1CM = "1cm"
    V_1M = "1m"
    V_1W = "1w"


class brandMetricsGenerateReportRequestV11(BaseModel):
    """Request object to generate the Brand Metrics Report."""
    brand_name: Optional[str] = Field(None, alias="brandName", description="Optional. Brand Name. If no Brand Name is passed, then all data available for all brands belonging to the entity are ret")
    category_path: Optional[list[str]] = Field(None, alias="categoryPath", description="Optional. The hierarchical path that leads to a node starting with the root node. If no Category Node Name is passed, th")
    category_tree_name: Optional[str] = Field(None, alias="categoryTreeName", description="Optional. The node at the top of a browse tree. It is the start node of a tree.")
    format_: Optional[brandMetricsGenerateReportRequestV11Format] = Field(None, alias="format", description="Format of the report.")
    look_back_period: Optional[brandMetricsGenerateReportRequestV11Lookbackperiod] = Field(None, alias="lookBackPeriod", description="Currently supported values: '1w' (one week), '1m' (one month) and  '1cm' (one calendar month). This defines the period o")
    metrics: Optional[list[str]] = Field(None, description="Optional. Specify an array of string of metrics field names to include in the report. If no metric field names are speci")
    report_end_date: Optional[str] = Field(None, alias="reportEndDate", description="Optional. Retrieves metrics with metricsComputationDate between reportStartDate and reportEndDate (inclusive). The maxim")
    report_start_date: Optional[str] = Field(None, alias="reportStartDate", description="Optional. Retrieves metrics with metricsComputationDate between reportStartDate and reportEndDate (inclusive). The maxim")

    model_config = {'populate_by_name': True}


class brandMetricsGenerateReportResponseFormat(StrEnum):
    CSV = "CSV"
    JSON = "JSON"


class brandMetricsGenerateReportResponseStatus(StrEnum):
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESSFUL = "SUCCESSFUL"


class brandMetricsGenerateReportResponse(BaseModel):
    """Response object containing Brand Metrics Report metadata."""
    expiration: int = Field(..., description="The expiration time of the URI in the location property in milliseconds. The expiration time is the interval between the")
    format_: brandMetricsGenerateReportResponseFormat = Field(..., alias="format", description="Format of the report.")
    location: Optional[str] = Field(None, description="The URI address of the report.")
    report_id: str = Field(..., alias="reportId", description="The identifier of the report.")
    status: brandMetricsGenerateReportResponseStatus = Field(..., description="The build status of the report.")
    status_details: str = Field(..., alias="statusDetails", description="A human-readable description of the current status.")

    model_config = {'populate_by_name': True}


class brandMetricsGenerateReportResponseV11Format(StrEnum):
    CSV = "CSV"
    JSON = "JSON"


class brandMetricsGenerateReportResponseV11Status(StrEnum):
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESSFUL = "SUCCESSFUL"


class brandMetricsGenerateReportResponseV11(BaseModel):
    """Response object containing Brand Metrics Report metadata."""
    expiration: int = Field(..., description="The expiration time of the URI in the location property in milliseconds. The expiration time is the interval between the")
    format_: brandMetricsGenerateReportResponseV11Format = Field(..., alias="format", description="Format of the report.")
    location: Optional[str] = Field(None, description="The URI address of the report.")
    report_id: str = Field(..., alias="reportId", description="The identifier of the report.")
    status: brandMetricsGenerateReportResponseV11Status = Field(..., description="The build status of the report.")
    status_details: str = Field(..., alias="statusDetails", description="A human-readable description of the current status.")

    model_config = {'populate_by_name': True}


class brandMetricsGetReportByIdResponseBrandsinfo(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="GCOR ID from Brand Registry.")
    name: Optional[str] = Field(None, description="Brand Name.")

    model_config = {'populate_by_name': True}


class brandMetricsGetReportByIdResponseFormat(StrEnum):
    CSV = "CSV"
    JSON = "JSON"


class brandMetricsGetReportByIdResponseStatus(StrEnum):
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESSFUL = "SUCCESSFUL"


class brandMetricsGetReportByIdResponse(BaseModel):
    """Response object containing Brand Metrics Report status metadata."""
    brands_info: Optional[list["brandMetricsGetReportByIdResponseBrandsinfo"]] = Field(None, alias="brandsInfo", description="List of first 200 brands for which the Brand Metrics report is generated. The report may contain more than 200 brands. T")
    expiration: int = Field(..., description="The expiration time of the URI in the location property in milliseconds. The expiration time is the interval between the")
    format_: brandMetricsGetReportByIdResponseFormat = Field(..., alias="format", description="Format of the report.")
    location: Optional[str] = Field(None, description="The URI address of the report. Only available if the report is generated successfully. The location is empty if the Bran")
    report_id: str = Field(..., alias="reportId", description="The identifier of the report.")
    status: brandMetricsGetReportByIdResponseStatus = Field(..., description="The build status of the report.")
    status_details: str = Field(..., alias="statusDetails", description="A human-readable description of the current status.")

    model_config = {'populate_by_name': True}

