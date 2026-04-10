"""Auto-generated Pydantic models. Do not edit manually.

Source: Profiles_prod_3p.json
Title:  Profiles
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class ProfileAccountType(StrEnum):
    AGENCY = "agency"
    SELLER = "seller"
    VENDOR = "vendor"


class ProfileAccountInfoSubtype(StrEnum):
    AMAZON_ATTRIBUTION = "AMAZON_ATTRIBUTION"
    KDP_AUTHOR = "KDP_AUTHOR"


class ProfileAccountInfo(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="Identifier for sellers and vendors. Note that this value is not unique and may be the same across marketplace.")
    marketplace_string_id: Optional[str] = Field(None, alias="marketplaceStringId", description="The identifier of the marketplace to which the account is associated.")
    name: Optional[str] = Field(None, description="Account Name. Not currently populated for sellers.")
    sub_type: Optional[ProfileAccountInfoSubtype] = Field(None, alias="subType", description="The account subtype.")
    type_: Optional["ProfileAccountType"] = Field(None, alias="type")
    valid_payment_method: Optional[bool] = Field(None, alias="validPaymentMethod", description="Only present for Vendors, this returns whether the Advertiser has set up a valid payment method or not.")

    model_config = {'populate_by_name': True}


class ProfileCountryCode(StrEnum):
    AE = "AE"
    AU = "AU"
    CA = "CA"
    DE = "DE"
    ES = "ES"
    FR = "FR"
    IT = "IT"
    JP = "JP"
    UK = "UK"
    US = "US"


class ProfileCurrencycode(StrEnum):
    AED = "AED"
    AUD = "AUD"
    CAD = "CAD"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"
    USD = "USD"


class ProfileTimezone(StrEnum):
    AMERICA_LOS_ANGELES = "America/Los_Angeles"
    ASIA_DUBAI = "Asia/Dubai"
    ASIA_TOKYO = "Asia/Tokyo"
    AUSTRALIA_SYDNEY = "Australia/Sydney"
    EUROPE_LONDON = "Europe/London"
    EUROPE_PARIS = "Europe/Paris"


class Profile(BaseModel):
    account_info: Optional["ProfileAccountInfo"] = Field(None, alias="accountInfo")
    country_code: Optional["ProfileCountryCode"] = Field(None, alias="countryCode")
    currency_code: Optional[ProfileCurrencycode] = Field(None, alias="currencyCode", description="The currency used for all monetary values for entities under this profile. |Region|`countryCode`|Country Name|`currencyC")
    daily_budget: Optional[float] = Field(None, alias="dailyBudget", description="Note that this field applies to Sponsored Product campaigns for seller type accounts only. Not supported for vendor type")
    profile_id: Optional[int] = Field(None, alias="profileId")
    timezone: Optional[ProfileTimezone] = Field(None, description="The time zone used for all date-based campaign management and reporting. |Region|`countryCode`|Country Name|`timezone`| ")

    model_config = {'populate_by_name': True}


class SPError(BaseModel):
    code: Optional[str] = Field(None, description="An enumerated error for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the error.")

    model_config = {'populate_by_name': True}

