"""Auto-generated Pydantic models. Do not edit manually.

Source: AdGroupTargeting-ProductCategory_prod_3p.json
Title:  Ad Group Targeting - Product Category
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



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


class DspCreateAdGroupProductCategoryTargetV1(BaseModel):
    asin_category: str = Field(..., alias="asinCategory", description="The product category to target.")
    negative: bool = Field(..., description="Whether to include (false) or exclude (true) the given target.")

    model_config = {'populate_by_name': True}


class DspCreateAdGroupProductCategoryTargetsRequestContentV1(BaseModel):
    product_category_targets: list["DspCreateAdGroupProductCategoryTargetV1"] = Field(..., alias="productCategoryTargets", description="A list of targets.")

    model_config = {'populate_by_name': True}


class DspDeleteAdGroupProductCategoryTargetV1(BaseModel):
    asin_category: str = Field(..., alias="asinCategory", description="The product category to target.")
    negative: bool = Field(..., description="Whether to include (false) or exclude (true) the given target.")

    model_config = {'populate_by_name': True}


class DspDeleteAdGroupProductCategoryTargetsRequestContentV1(BaseModel):
    product_category_targets: list["DspDeleteAdGroupProductCategoryTargetV1"] = Field(..., alias="productCategoryTargets", description="A list of targets.")

    model_config = {'populate_by_name': True}


class DspForbiddenExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspGetAdGroupProductCategoryTargetV1(BaseModel):
    asin_category: str = Field(..., alias="asinCategory", description="The product category to target.")
    negative: bool = Field(..., description="Whether to include (false) or exclude (true) the given target.")

    model_config = {'populate_by_name': True}


class DspGetAdGroupProductCategoryTargetsResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results,")
    product_category_targets: list["DspGetAdGroupProductCategoryTargetV1"] = Field(..., alias="productCategoryTargets", description="A list of targets.")

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

