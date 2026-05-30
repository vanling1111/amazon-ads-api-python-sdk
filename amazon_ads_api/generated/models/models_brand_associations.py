"""Auto-generated Pydantic models. Do not edit manually.

Source: BrandAidV2_prod_3p.json
Title:  BrandAidV2
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class BadGatewayResponseContent(BaseModel):
    code: str
    message: str

    model_config = {'populate_by_name': True}


class ErrorCode(StrEnum):
    BAD_REQUEST = "BAD_REQUEST"
    CONTENT_TOO_LARGE = "CONTENT_TOO_LARGE"
    FORBIDDEN = "FORBIDDEN"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    NOT_FOUND = "NOT_FOUND"
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"
    UNAUTHORIZED = "UNAUTHORIZED"


class BadRequestResponseContent(BaseModel):
    code: "ErrorCode"
    message: str

    model_config = {'populate_by_name': True}


class BrandStatus(StrEnum):
    MERGED = "MERGED"
    NOT_APPROVED = "NOT_APPROVED"
    PENDING_REVIEW = "PENDING_REVIEW"
    REGISTERED = "REGISTERED"
    SUSPENDED = "SUSPENDED"


class BrandLogo(BaseModel):
    """<p>Metadata for a brand logo.</p>"""
    brand_logo_asset_id: Optional[str] = Field(None, alias="brandLogoAssetId", description="<p>Advertising Asset Library Id for a brand logo.</p>")

    model_config = {'populate_by_name': True}


class Brand(BaseModel):
    brand_id: str = Field(..., alias="brandId", description="<p>The unique identifier for a brand.</p>")
    brand_logos: Optional[list["BrandLogo"]] = Field(None, alias="brandLogos", description="<p>Logos of the brand.</p>")
    brand_name: str = Field(..., alias="brandName", description="<p>Display name of the brand.</p>")
    brand_status: "BrandStatus" = Field(..., alias="brandStatus")
    brand_websites: Optional[list[str]] = Field(None, alias="brandWebsites", description="<p>Websites of the brand.</p>")

    model_config = {'populate_by_name': True}


class BrandAdvertiserAssociationStatus(StrEnum):
    APPROVED = "APPROVED"
    NOT_APPROVED = "NOT_APPROVED"
    PENDING_REVIEW = "PENDING_REVIEW"


class BrandAdvertiserRelationshipType(StrEnum):
    ADVERTISER = "ADVERTISER"
    OWNER = "OWNER"
    RESELLER = "RESELLER"


class BrandAdvertiserAssociation(BaseModel):
    advertiser_account_id: str = Field(..., alias="advertiserAccountId", description="<p>The identifier of the advertiser account in the relationship.</p>")
    association_status: "BrandAdvertiserAssociationStatus" = Field(..., alias="associationStatus")
    brand_association_id: str = Field(..., alias="brandAssociationId", description="<p>The unique identifier for a brand advertiser association.</p>")
    brand_id: str = Field(..., alias="brandId", description="<p>The identifier of the brand in the relationship.</p>")
    relationship: "BrandAdvertiserRelationshipType"

    model_config = {'populate_by_name': True}


class BrandMultiStatusSuccess(BaseModel):
    brand: "Brand"
    index: float

    model_config = {'populate_by_name': True}


class ContentTooLargeResponseContent(BaseModel):
    code: "ErrorCode"
    message: str

    model_config = {'populate_by_name': True}


class Error(BaseModel):
    code: "ErrorCode"
    field_location: Optional[str] = Field(None, alias="fieldLocation")
    message: str

    model_config = {'populate_by_name': True}


class ErrorsIndex(BaseModel):
    errors: list["Error"]
    index: float

    model_config = {'populate_by_name': True}


class ForbiddenResponseContent(BaseModel):
    code: "ErrorCode"
    message: str

    model_config = {'populate_by_name': True}


class GatewayTimeoutResponseContent(BaseModel):
    code: str
    message: str

    model_config = {'populate_by_name': True}


class InternalServerErrorResponseContent(BaseModel):
    code: str
    message: str

    model_config = {'populate_by_name': True}


class NotFoundResponseContent(BaseModel):
    code: "ErrorCode"
    message: str

    model_config = {'populate_by_name': True}


class QueryBrandAdvertiserAssociationRequestContent(BaseModel):
    max_results: Optional[float] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class QueryBrandAdvertiserAssociationResponseContent(BaseModel):
    brand_advertiser_associations: Optional[list["BrandAdvertiserAssociation"]] = Field(None, alias="brandAdvertiserAssociations")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class RetrieveBrandRequestContent(BaseModel):
    brand_ids: Optional[list[str]] = Field(None, alias="brandIds")

    model_config = {'populate_by_name': True}


class RetrieveBrandResponseContent(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    success: Optional[list["BrandMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class ServiceUnavailableErrorResponseContent(BaseModel):
    code: str
    message: str

    model_config = {'populate_by_name': True}


class TooManyRequestsResponseContent(BaseModel):
    code: "ErrorCode"
    message: str

    model_config = {'populate_by_name': True}


class UnauthorizedResponseContent(BaseModel):
    code: "ErrorCode"
    message: str

    model_config = {'populate_by_name': True}

