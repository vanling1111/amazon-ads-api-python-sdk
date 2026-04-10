"""Auto-generated Pydantic models. Do not edit manually.

Source: BrandBenchmarks_prod_3p.json
Title:  Brand Benchmarks
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class AdvertiserReportMetadata(BaseModel):
    advertiser_id: Optional[str] = Field(None, alias="advertiserId")
    index_date: Optional[str] = Field(None, alias="indexDate")
    obfuscated_marketplace_id: Optional[str] = Field(None, alias="obfuscatedMarketplaceId")
    report_type: Optional[str] = Field(None, alias="reportType")

    model_config = {'populate_by_name': True}


class SubErrorV1(BaseModel):
    error_type: str = Field(..., alias="errorType")
    field_name: Optional[str] = Field(None, alias="fieldName")
    message: str

    model_config = {'populate_by_name': True}


class BadRequestExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["SubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class ConflictExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["SubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class ForbiddenExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["SubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class GetAdvertiserReportResponseContent(BaseModel):
    """The presigned S3 URL to allow clients to download the report."""
    download_link: Optional[str] = Field(None, alias="downloadLink")

    model_config = {'populate_by_name': True}


class InternalServerExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["SubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class ListAdvertiserReportMetadataResponseContent(BaseModel):
    """The presigned S3 URL to allow clients to download the report."""
    next_token: Optional[str] = Field(None, alias="nextToken")
    reports_metadata: Optional[list["AdvertiserReportMetadata"]] = Field(None, alias="reportsMetadata")

    model_config = {'populate_by_name': True}


class ResourceNotFoundExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["SubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class TooManyRequestsExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["SubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class UnauthorizedExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["SubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class UnsupportedMediaTypeExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["SubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}

