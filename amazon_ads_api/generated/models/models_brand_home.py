"""Auto-generated Pydantic models. Do not edit manually.

Source: BrandHome_prod_3p.json
Title:  Brand Home
"""

from __future__ import annotations

from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field



class AuthorizationExceptionResponse(BaseModel):
    code: str
    message: str

    model_config = {'populate_by_name': True}


class BadRequestExceptionResponse(BaseModel):
    """Invalid input values. Ex bad marketplaceId, missing required inputs, or requester does not have permission for API and/or resource."""
    code: str
    message: str

    model_config = {'populate_by_name': True}


class ConflictExceptionResponse(BaseModel):
    """Conflict detected"""
    code: str
    message: str

    model_config = {'populate_by_name': True}


class ForbiddenExceptionResponse(BaseModel):
    code: str
    message: str

    model_config = {'populate_by_name': True}


class IdentifierType(StrEnum):
    ASIN = "ASIN"
    BRAND_AID_ID = "BRAND_AID_ID"
    ENTITY_ID = "ENTITY_ID"
    GCOR = "GCOR"
    NODE = "NODE"
    STORE = "STORE"


class ListPagesRequest(BaseModel):
    """Request Object for ListPages API"""
    identifier: str = Field(..., description="Identifier for requested store. Currently supported: store's brand-/sub-entityId and storeId.")
    identifier_type: "IdentifierType" = Field(..., alias="identifierType")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Optional: Max number of entries returned in a call. Supported values are 1-30 inclusive. Defaults to 30.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional: Pagination input token. If provided, returns the next paginated result of size <= `maxResults`.")

    model_config = {'populate_by_name': True}


class State(StrEnum):
    APPROVED = "APPROVED"
    CANCELED = "CANCELED"
    DRAFT = "DRAFT"
    LIVE = "LIVE"
    PENDING = "PENDING"
    REJECTED = "REJECTED"
    SCHEDULED = "SCHEDULED"


class StorePageInfo(BaseModel):
    store_page_id: Optional[str] = Field(None, alias="storePageId", description="The ID of the store page")
    store_page_name: Optional[str] = Field(None, alias="storePageName", description="The name of the store page")
    store_page_status: Optional["State"] = Field(None, alias="storePageStatus")
    store_page_url: Optional[str] = Field(None, alias="storePageUrl", description="The URL of the store page")

    model_config = {'populate_by_name': True}


class ListPagesResponse(BaseModel):
    """Response Object for ListPages API"""
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional: Pagination input token. If provided, returns the next paginated result of size <= `maxResults`.")
    store_pages: Optional[list["StorePageInfo"]] = Field(None, alias="storePages", description="Paginated list of `StorePageInfos`'s. Result list size <= maxResults.")

    model_config = {'populate_by_name': True}


class ListStoresRequest(BaseModel):
    """Request Object for ListStores API"""
    identifier: Optional[str] = Field(None, description="Optional: Identifier for requested entity. Currently supported: Advertiser entityId.")
    identifier_type: Optional["IdentifierType"] = Field(None, alias="identifierType")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Optional: Max number of entries returned in a call. Supported values are 1-30 inclusive. Defaults to 30.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional: Pagination input token. If provided, returns the next paginated result of size <= `maxResults`.")

    model_config = {'populate_by_name': True}


class StoreId(BaseModel):
    """The Store Identifier."""
    pass


class StoreInfo(BaseModel):
    brand_entity_id: Optional[str] = Field(None, alias="brandEntityId", description="The ID of the Brand Entity associated with the store")
    store_id: Optional["StoreId"] = Field(None, alias="storeId")
    store_name: Optional[str] = Field(None, alias="storeName", description="The name of the store")
    store_status: Optional["State"] = Field(None, alias="storeStatus")

    model_config = {'populate_by_name': True}


class ListStoresResponse(BaseModel):
    """Response Object for ListStores API"""
    next_token: Optional[str] = Field(None, alias="nextToken", description="Nullable. The next token to be used for paginated querying.")
    stores: list["StoreInfo"] = Field(..., description="Paginated list of `StoreInfo`'s. Result list size <= maxResults. If advertiser has no stores, returns empty list.")

    model_config = {'populate_by_name': True}


class NotFoundExceptionResponse(BaseModel):
    """Requested resource not found"""
    code: str
    message: str

    model_config = {'populate_by_name': True}


class ThrottlingExceptionResponse(BaseModel):
    """Throttling"""
    code: str
    message: str

    model_config = {'populate_by_name': True}

