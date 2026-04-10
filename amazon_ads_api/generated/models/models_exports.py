"""Auto-generated Pydantic models. Do not edit manually.

Source: AmazonAdsAPIExports_prod_3p.json
Title:  Amazon Ads API Exports
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class BaseUniversalApiExportRequestAdproductfilter(StrEnum):
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"


class BaseUniversalApiExportRequestStatefilter(StrEnum):
    ARCHIVED = "ARCHIVED"
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


class BaseUniversalApiExportRequest(BaseModel):
    ad_product_filter: Optional[list[BaseUniversalApiExportRequestAdproductfilter]] = Field(None, alias="adProductFilter", description="Filters the entities returned in export only to selected ad products. In case the filter is not provided, it returns ent")
    state_filter: Optional[list[BaseUniversalApiExportRequestStatefilter]] = Field(None, alias="stateFilter", description="Filters the entities returned in export only to selected states. In case the filter is not provided, it returns only `EN")

    model_config = {'populate_by_name': True}


class TargetsUniversalApiExportRequest(BaseModel):
    pass


class UniversalApiErrorErrorcode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"
    TIMED_OUT = "TIMED_OUT"


class UniversalApiError(BaseModel):
    error_code: Optional[UniversalApiErrorErrorcode] = Field(None, alias="errorCode", description="- INTERNAL_ERROR: The export has failed with an internal error. If the issue persists, please contact customer support. ")
    message: str = Field(..., description="A human-readable description of the error.")

    model_config = {'populate_by_name': True}


class UniversalApiExportResponseStatus(StrEnum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PROCESSING = "PROCESSING"


class UniversalApiExportResponse(BaseModel):
    created_at: Optional[str] = Field(None, alias="createdAt", description="Date of when the export request was created.")
    error: Optional["UniversalApiError"] = None
    export_id: str = Field(..., alias="exportId", description="The export identifier.")
    file_size: Optional[float] = Field(None, alias="fileSize", description="Byte size of the generated file.")
    generated_at: Optional[str] = Field(None, alias="generatedAt", description="Date of when the export was finished generating.")
    status: UniversalApiExportResponseStatus = Field(..., description="The generation status of the export. - PROCESSING: Export is currently in progress. - COMPLETED: Export has completed su")
    url: Optional[str] = Field(None, description="A URL for the export. It’s only available if status is COMPLETED.")
    url_expires_at: Optional[str] = Field(None, alias="urlExpiresAt", description="Date at which the download URL for the generated export expires.")

    model_config = {'populate_by_name': True}

