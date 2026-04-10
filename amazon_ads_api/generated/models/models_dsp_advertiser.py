"""Auto-generated Pydantic models. Do not edit manually.

Source: DSP_Advertiser_v3_openapi.yaml
Title:  Amazon Ads API for DSP
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class DspTimezoneV1(BaseModel):
    """The advertiser timezone. - America/Anchorage - America/Caracas - America/Chicago - America/Denver - America/Halifax - America/Los_Angeles - America/New_York - America/Sao_Paulo - America/St_Johns - As"""
    pass


class DspCountryV1(StrEnum):
    US = "US"
    CA = "CA"
    MX = "MX"
    JP = "JP"
    AU = "AU"
    IN = "IN"
    UK = "UK"
    GB = "GB"
    DE = "DE"
    FR = "FR"
    IT = "IT"
    ES = "ES"
    AT = "AT"
    AE = "AE"
    SA = "SA"
    BR = "BR"
    NL = "NL"
    SE = "SE"
    SG = "SG"
    TR = "TR"


class DspSupportedCurrencyV1(StrEnum):
    USD = "USD"
    CAD = "CAD"
    JPY = "JPY"
    GBP = "GBP"
    EUR = "EUR"
    INR = "INR"
    MXN = "MXN"
    AED = "AED"
    SAR = "SAR"
    BRL = "BRL"
    AUD = "AUD"
    SEK = "SEK"
    SGD = "SGD"
    TRY = "TRY"


class DspAdvertiserV1(BaseModel):
    """The DSP Advertiser object"""
    advertiser_id: Optional[str] = Field(None, alias="advertiserId", description="The advertiser identifier.")
    name: Optional[str] = Field(None, description="The advertiser name.")
    currency: Optional["DspSupportedCurrencyV1"] = None
    url: Optional[str] = Field(None, description="The URL of the advertiser’s website.")
    country: Optional["DspCountryV1"] = None
    timezone: Optional["DspTimezoneV1"] = None

    model_config = {'populate_by_name': True}


class DspAdvertisersV1(BaseModel):
    """List of advertisers along with total number of advertisers which satisfy the filtering criteria."""
    total_results: Optional[int] = Field(None, alias="totalResults", description="Total number of advertisers which satisfy the filtering criteria. This number is given to support pagination and tell th")
    response: Optional[list["DspAdvertiserV1"]] = Field(None, description="List of advertisers with complete information.")

    model_config = {'populate_by_name': True}


class DspSubErrorV1(BaseModel):
    """Error Object"""
    error_type: str = Field(..., alias="errorType", description="Enumerated error type.")
    field: Optional[str] = Field(None, description="Request body field which is cause of the error.")
    message: str = Field(..., description="Detailed error description")

    model_config = {'populate_by_name': True}


class DspErrorV1(BaseModel):
    """Error response object."""
    message: str = Field(..., description="A human-readable description of the response.")
    request_id: Optional[str] = Field(None, alias="requestId", description="A value will be used to identify your request uniquely.")
    errors: Optional[list["DspSubErrorV1"]] = Field(None, description="List of errors. Useful in case of validation errors")

    model_config = {'populate_by_name': True}

