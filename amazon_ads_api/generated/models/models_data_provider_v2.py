"""Auto-generated Pydantic models. Do not edit manually.

Source: DataProvider_openapi.yaml
Title:  Amazon Ads API for Data Providers.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class audienceName(BaseModel):
    """The audience name. Must be an alphanumeric string between 10 to 128 characters in length."""
    pass


class audienceDescription(BaseModel):
    """The audience description. Must be an alphanumeric, non-null string between 0 to 1000 characters in length."""
    pass


class audienceId(BaseModel):
    """The"""
    pass


class advertiserId(BaseModel):
    """The advertiser identifier."""
    pass


class metadataType(StrEnum):
    DATA_PROVIDER = "DATA_PROVIDER"


class externalAudienceId(BaseModel):
    """The user-defined audience identifier."""
    pass


class recordTtl(BaseModel):
    """Time-to-live (ttl), in seconds. The amount of time the record is associated with the audience."""
    pass


class audienceFees(BaseModel):
    pass


class dataSourceCountry(BaseModel):
    """A list of country codes describing where data in an audience is collected from. Country code is defined in https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2."""
    pass


class requestId(BaseModel):
    """The request identifier."""
    pass


class httpStatusCode(BaseModel):
    """The HTTP status code."""
    pass


class errorDescription(BaseModel):
    """A human-readable description of the error."""
    pass


class subError(BaseModel):
    pass


class tcf(BaseModel):
    """TCF(Transparency & Consent Framework) consent string that wraps privacy consent information from user."""
    pass


class gpp(BaseModel):
    """GPP(Global Privacy Platform) consent string that wraps privacy consent information from user."""
    pass


class amazonConsentAmazonadstorage(StrEnum):
    GRANTED = "GRANTED"
    DENIED = "DENIED"


class amazonConsentAmazonuserdata(StrEnum):
    GRANTED = "GRANTED"
    DENIED = "DENIED"


class amazonConsent(BaseModel):
    amazon_ad_storage: amazonConsentAmazonadstorage = Field(..., alias="amazonAdStorage", description="Set consent for advertising related storage such as cookies(web) or device identifiers(apps).")
    amazon_user_data: amazonConsentAmazonuserdata = Field(..., alias="amazonUserData", description="Set consent to use personal data for online advertising purposes.")

    model_config = {'populate_by_name': True}

