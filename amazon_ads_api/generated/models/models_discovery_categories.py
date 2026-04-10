"""Auto-generated Pydantic models. Do not edit manually.

Source: Discovery-AdvertisedProductCategories-V1_prod_3p.json
Title:  Discovery - Advertised Product Categories - V1
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field



class DspSubError(BaseModel):
    error_code: str = Field(..., alias="errorCode")
    error_id: Optional[str] = Field(None, alias="errorId")
    error_message: str = Field(..., alias="errorMessage")

    model_config = {'populate_by_name': True}


class DspBadRequestExceptionResponseContent(BaseModel):
    errors: Optional[list["DspSubError"]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspConflictExceptionResponseContent(BaseModel):
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


class DspListAdvertisedProductCategoriesRequestContent(BaseModel):
    max_results: Optional[int] = Field(None, alias="maxResults", description="Sets the maximum number of objects in the returned array. Use in conjunction with the nextToken parameter to control pag")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results,")

    model_config = {'populate_by_name': True}


class DspProductCategory(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="The category identifier.")
    name: Optional[str] = Field(None, description="The category name.")
    parent_id: Optional[str] = Field(None, alias="parentId", description="The identifier of the parent category. This is not present in the object if the category is a parent category.")

    model_config = {'populate_by_name': True}


class DspListAdvertisedProductCategoriesResponseContent(BaseModel):
    categories: Optional[list["DspProductCategory"]] = Field(None, description="List of the Product Categories.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="A token representing the state of the pagination for the results. Use this token in subsequent requests to fetch the nex")

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

