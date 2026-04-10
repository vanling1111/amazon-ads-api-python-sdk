"""Auto-generated Pydantic models. Do not edit manually.

Source: OfflineReport_prod_3p.json
Title:  Offline Report
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class AsyncReportFilter(BaseModel):
    field: Optional[str] = Field(None, description="The field name of the filter")
    values: Optional[list[str]] = Field(None, description="The values to be filtered by")

    model_config = {'populate_by_name': True}


class AsyncReportAdProduct(StrEnum):
    ALL = "ALL"
    DEMAND_SIDE_PLATFORM = "DEMAND_SIDE_PLATFORM"
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"
    SPONSORED_TELEVISION = "SPONSORED_TELEVISION"


class AsyncReportConfigurationFormat(StrEnum):
    GZIP_JSON = "GZIP_JSON"


class AsyncReportConfigurationTimeunit(StrEnum):
    DAILY = "DAILY"
    SUMMARY = "SUMMARY"


class AsyncReportConfiguration(BaseModel):
    ad_product: "AsyncReportAdProduct" = Field(..., alias="adProduct")
    columns: list[str] = Field(..., description="The list of columns to be used for report. The availability of columns depends on the selection of reportTypeId. This li")
    filters: Optional[list["AsyncReportFilter"]] = Field(None, description="The list of filters supported by a report type. The availability of filters fields depends on the selection of reportTyp")
    format_: AsyncReportConfigurationFormat = Field(..., alias="format", description="The report file format.")
    group_by: list[str] = Field(..., alias="groupBy", description="This field determines the aggregation level of the report data and also makes additional fields available for selection.")
    report_type_id: str = Field(..., alias="reportTypeId", description="The identifier of the Report Type to be generated.")
    time_unit: AsyncReportConfigurationTimeunit = Field(..., alias="timeUnit", description="The aggregation level of report data. If the timeUnit is set to `SUMMARY`, the report data is aggregated at the time per")

    model_config = {'populate_by_name': True}


class AsyncReportStatus(StrEnum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"


class AsyncReport(BaseModel):
    configuration: "AsyncReportConfiguration"
    created_at: str = Field(..., alias="createdAt", description="The date at which the report was created in ISO 8601 date time format.")
    end_date: str = Field(..., alias="endDate", description="The end date for the reporting period in YYYY-mm-dd format.")
    failure_reason: Optional[str] = Field(None, alias="failureReason", description="Present for failed reports only. The reason why a report failed to generate.")
    file_size: Optional[float] = Field(None, alias="fileSize", description="The size of the report file, in bytes.")
    generated_at: Optional[str] = Field(None, alias="generatedAt", description="The date at which the report was generated in ISO 8601 date time format.")
    name: Optional[str] = Field(None, description="Optional. The name of the generated report.")
    report_id: str = Field(..., alias="reportId", description="The identifier of the requested report.")
    start_date: str = Field(..., alias="startDate", description="The start date for the reporting period in YYYY-mm-dd format.")
    status: AsyncReportStatus = Field(..., description="The build status of the report.   - `PENDING` - Report is created and awaiting processing.   - `PROCESSING` - Report is ")
    updated_at: str = Field(..., alias="updatedAt", description="The date at which the report was last updated in ISO 8601 date time format.")
    url: Optional[str] = Field(None, description="URL of the generated report.")
    url_expires_at: Optional[str] = Field(None, alias="urlExpiresAt", description="The date at which the download URL for the generated report expires. urlExpires at this time defaults to 3600 seconds bu")

    model_config = {'populate_by_name': True}


class AsyncReportingError(BaseModel):
    """The Error Response."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    detail: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class CreateAsyncReportRequest(BaseModel):
    configuration: "AsyncReportConfiguration"
    end_date: str = Field(..., alias="endDate", description="YYYY-MM-DD format. The maximum lookback window supported depends on the selection of reportTypeId. Most report types sup")
    name: Optional[str] = Field(None, description="The name of the report.")
    start_date: str = Field(..., alias="startDate", description="YYYY-MM-DD format. The maximum lookback window supported depends on the selection of reportTypeId. Most report types sup")

    model_config = {'populate_by_name': True}


class DeleteAsyncReportResponse(BaseModel):
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    detail: Optional[str] = Field(None, description="A human-readable description of the response.")
    report_id: Optional[str] = Field(None, alias="reportId", description="The identifier of the report.")

    model_config = {'populate_by_name': True}

