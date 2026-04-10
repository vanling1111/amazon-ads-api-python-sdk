"""Auto-generated Pydantic models. Do not edit manually.

Source: AdvertisingTestAccount_prod_3p.json
Title:  AdvertisingTestAccount
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional

from pydantic import BaseModel, Field



class CreateAccountRequestAccounttype(StrEnum):
    AUTHOR = "AUTHOR"
    VENDOR = "VENDOR"


class CreateAccountRequestCountrycode(StrEnum):
    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    UK = "UK"
    US = "US"


class CreateAccountRequest(BaseModel):
    account_meta_data: Optional[Any] = Field(None, alias="accountMetaData")
    account_type: CreateAccountRequestAccounttype = Field(..., alias="accountType", description="Type of test account.")
    country_code: CreateAccountRequestCountrycode = Field(..., alias="countryCode", description="Country code of the test  account.")

    model_config = {'populate_by_name': True}


class CreateAccountResponse(BaseModel):
    request_id: Optional[str] = Field(None, alias="requestId", description="request id.")

    model_config = {'populate_by_name': True}


class GetAccountInformationResponse(BaseModel):
    pass


class error(BaseModel):
    """Error response object."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}

