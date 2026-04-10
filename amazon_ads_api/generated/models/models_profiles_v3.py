"""Auto-generated Pydantic models. Do not edit manually.

Source: Profiles_v3_openapi.yaml
Title:  Amazon Ads API - Profiles
"""

from __future__ import annotations

from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field



class AccountType(StrEnum):
    VENDOR = "vendor"
    SELLER = "seller"
    AGENCY = "agency"


class AccountInfoSubtype(StrEnum):
    KDP_AUTHOR = "KDP_AUTHOR"
    AMAZON_ATTRIBUTION = "AMAZON_ATTRIBUTION"


class AccountInfo(BaseModel):
    marketplace_string_id: Optional[str] = Field(None, alias="marketplaceStringId", description="The identifier of the marketplace to which the account is associated.")
    id_: Optional[str] = Field(None, alias="id", description="Identifier for sellers and vendors. Note that this value is not unique and may be the same across marketplace.")
    type_: Optional["AccountType"] = Field(None, alias="type")
    name: Optional[str] = Field(None, description="Account name.")
    sub_type: Optional[AccountInfoSubtype] = Field(None, alias="subType", description="The account subtype.")
    valid_payment_method: Optional[bool] = Field(None, alias="validPaymentMethod", description="Only present for Vendors, this returns whether the Advertiser has set up a valid payment method or not.")

    model_config = {'populate_by_name': True}


class countryCode(StrEnum):
    BR = "BR"
    CA = "CA"
    MX = "MX"
    US = "US"
    AE = "AE"
    BE = "BE"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    IE = "IE"
    IN = "IN"
    IT = "IT"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    TR = "TR"
    UK = "UK"
    AU = "AU"
    JP = "JP"
    SG = "SG"
    ZA = "ZA"


class ProfileCurrencycode(StrEnum):
    BRL = "BRL"
    CAD = "CAD"
    MXN = "MXN"
    USD = "USD"
    AED = "AED"
    EUR = "EUR"
    EGP = "EGP"
    INR = "INR"
    PLN = "PLN"
    SAR = "SAR"
    SEK = "SEK"
    TRY = "TRY"
    GBP = "GBP"
    AUD = "AUD"
    JPY = "JPY"
    SGD = "SGD"
    ZAR = "ZAR"


class ProfileTimezone(StrEnum):
    AFRICA_CAIRO = "Africa/Cairo"
    AMERICA_SAO_PAULO = "America/Sao_Paulo"
    AMERICA_LOS_ANGELES = "America/Los_Angeles"
    ASIA_DUBAI = "Asia/Dubai"
    ASIA_KOLKATA = "Asia/Kolkata"
    ASIA_RIYADH = "Asia/Riyadh"
    ASIA_SINGAPORE = "Asia/Singapore"
    ASIA_TOKYO = "Asia/Tokyo"
    AUSTRALIA_SYDNEY = "Australia/Sydney"
    EUROPE_AMSTERDAM = "Europe/Amsterdam"
    EUROPE_DUBLIN = "Europe/Dublin"
    EUROPE_ISTANBUL = "Europe/Istanbul"
    EUROPE_LONDON = "Europe/London"
    EUROPE_PARIS = "Europe/Paris"
    EUROPE_STOCKHOLM = "Europe/Stockholm"
    EUROPE_WARSAW = "Europe/Warsaw"
    EUROPE_BRUSSELS = "Europe/Brussels"
    AFRICA_JOHANNESBURG = "Africa/Johannesburg"


class Profile(BaseModel):
    profile_id: Optional[int] = Field(None, alias="profileId")
    country_code: Optional["countryCode"] = Field(None, alias="countryCode")
    currency_code: Optional[ProfileCurrencycode] = Field(None, alias="currencyCode", description="The currency used for all monetary values for entities under this profile. |Region|`countryCode`|Country Name|`currencyC")
    daily_budget: Optional[float] = Field(None, alias="dailyBudget", description="Note that this field applies to Sponsored Product campaigns for seller type accounts only. Not supported for vendor type")
    timezone: Optional[ProfileTimezone] = Field(None, description="The time zone used for all date-based campaign management and reporting. |Region|`countryCode`|Country Name|`timezone`| ")
    account_info: Optional["AccountInfo"] = Field(None, alias="accountInfo")

    model_config = {'populate_by_name': True}


class ProfileResponse(BaseModel):
    profile_id: Optional[int] = Field(None, alias="profileId")
    code: Optional[str] = None
    details: Optional[str] = None

    model_config = {'populate_by_name': True}

