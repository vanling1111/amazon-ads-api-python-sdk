"""Auto-generated Pydantic models. Do not edit manually.

Source: DSPCampaignManagement_prod_3p.json
Title:  DSP Campaign Management
"""

from __future__ import annotations

from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field



class DspSupportedCurrencyV1(StrEnum):
    AED = "AED"
    ARS = "ARS"
    AUD = "AUD"
    BGN = "BGN"
    BHD = "BHD"
    BOB = "BOB"
    BRL = "BRL"
    CAD = "CAD"
    CHF = "CHF"
    CLP = "CLP"
    CNH = "CNH"
    CNY = "CNY"
    COP = "COP"
    CRC = "CRC"
    CZK = "CZK"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EGP = "EGP"
    EUR = "EUR"
    GBP = "GBP"
    GTQ = "GTQ"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KRW = "KRW"
    KWD = "KWD"
    MAD = "MAD"
    MXN = "MXN"
    MYR = "MYR"
    NGN = "NGN"
    NOK = "NOK"
    NZD = "NZD"
    PAB = "PAB"
    PEN = "PEN"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    THB = "THB"
    TND = "TND"
    TRY = "TRY"
    TWD = "TWD"
    UAH = "UAH"
    USD = "USD"
    UYU = "UYU"
    VND = "VND"
    ZAR = "ZAR"


class DspCountryV1(StrEnum):
    AE = "AE"
    AT = "AT"
    AU = "AU"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    UK = "UK"
    US = "US"


class DspAdvertiserV1(BaseModel):
    """Represents advertiser model. This model will be used for advertiser related requests & responses."""
    advertiser_id: Optional[str] = Field(None, alias="advertiserId", description="The advertiser identifier.")
    country: "DspCountryV1"
    currency: Optional["DspSupportedCurrencyV1"] = None
    is_regional: Optional[bool] = Field(None, alias="isRegional", description="Set to `true` if account is associated with a Global Advertiser Account")
    name: str = Field(..., description="The advertiser name.")
    opt_out_of_demographic_targeting_and_optimization: Optional[bool] = Field(None, alias="optOutOfDemographicTargetingAndOptimization", description="Set to `true` where advertiser opted-out of demographic signals for targeting and optimization.")
    timezone: Optional[str] = Field(None, description="The time zone.")
    url: str = Field(..., description="The URL associated with the advertiser.")

    model_config = {'populate_by_name': True}


class DspAdvertisersV1(BaseModel):
    response: Optional[list["DspAdvertiserV1"]] = None
    total_results: Optional[int] = Field(None, alias="totalResults", description="Total number of results which satisfy the filtering criteria. This will help to support pagination.")

    model_config = {'populate_by_name': True}


class DspSubErrorV1(BaseModel):
    """The sub error object."""
    error_type: Optional[str] = Field(None, alias="errorType")
    field_name: Optional[str] = Field(None, alias="fieldName")
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class DspErrorV1(BaseModel):
    """The error response object."""
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = Field(None, description="A human-readable description of the response.")
    request_id: Optional[str] = Field(None, alias="requestId", description="A value created by Amazon API Gateway that uniquely identifies your request.")

    model_config = {'populate_by_name': True}

