"""Auto-generated Pydantic models. Do not edit manually.

Source: RetailerIdentityAPIforRetailAdService_prod_3p.json
Title:  Retailer Identity API for Retail Ad Service
"""

from __future__ import annotations

from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field



class ErrorMessage(BaseModel):
    """Human readable response message"""
    pass


class ErrorCode(BaseModel):
    """Error code"""
    pass


class Error(BaseModel):
    code: Optional["ErrorCode"] = None
    message: Optional["ErrorMessage"] = None

    model_config = {'populate_by_name': True}


class RetailerStatus(StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    RETIRED = "RETIRED"


class Retailer(BaseModel):
    domain: Optional[str] = Field(None, description="The domain of the Retailer.")
    name: Optional[str] = Field(None, description="The name of the Retailer.")
    retailer_id: Optional[str] = Field(None, alias="retailerId", description="The identifier of the Retailer.")
    status: Optional[RetailerStatus] = Field(None, description="Status of the Retailer.")

    model_config = {'populate_by_name': True}


class IdentityListRetailersResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    retailers: Optional[list["Retailer"]] = None
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of entities")

    model_config = {'populate_by_name': True}


class RetailerIdFilter(BaseModel):
    """Filter entities by the list of RetailerIds"""
    include: list[str]

    model_config = {'populate_by_name': True}


class ListRetailersRequestContent(BaseModel):
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    retailer_id_filter: Optional["RetailerIdFilter"] = Field(None, alias="retailerIdFilter")

    model_config = {'populate_by_name': True}

