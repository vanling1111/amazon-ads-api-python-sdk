"""Auto-generated Pydantic models. Do not edit manually.

Source: Locations_prod_3p.json
Title:  Locations
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class SubError(BaseModel):
    """The sub error object."""
    error_type: str = Field(..., alias="errorType")
    field_name: Optional[str] = Field(None, alias="fieldName")
    message: str

    model_config = {'populate_by_name': True}


class Error(BaseModel):
    """The error response object."""
    errors: Optional[list["SubError"]] = None
    message: Optional[str] = Field(None, description="A human-readable description of the response.")
    request_id: Optional[str] = Field(None, alias="requestId", description="Request Id that uniquely identifies your request.")

    model_config = {'populate_by_name': True}


class LocationFilterV1Field(StrEnum):
    CATEGORY = "category"
    LOCATIONID = "locationId"
    NAME = "name"


class LocationFilterV1(BaseModel):
    field: Optional[LocationFilterV1Field] = Field(None, description="Field to filter by. Supported enums are 'locationId', 'name', and 'category'. The 'name' filter is a fuzzy search. If 'c")
    values: Optional[list[str]] = None

    model_config = {'populate_by_name': True}


class ListLocationsRequestBodyV1(BaseModel):
    """Resulting locations will match all specified filters"""
    filters: Optional[list["LocationFilterV1"]] = None

    model_config = {'populate_by_name': True}


class LocationCategoryV1(StrEnum):
    CITY = "CITY"
    COUNTRY = "COUNTRY"
    DMA = "DMA"
    POSTAL_CODE = "POSTAL_CODE"
    STATE = "STATE"


class LocationIdV1(BaseModel):
    """The identifier of the location."""
    pass


class LocationV1(BaseModel):
    category: Optional["LocationCategoryV1"] = None
    location_id: Optional["LocationIdV1"] = Field(None, alias="locationId")
    name: Optional[str] = Field(None, description="The location name.")

    model_config = {'populate_by_name': True}

