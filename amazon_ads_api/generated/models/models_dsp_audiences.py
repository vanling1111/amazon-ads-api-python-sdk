"""Auto-generated Pydantic models. Do not edit manually.

Source: ADSPAudiences_prod_3p.json
Title:  ADSP Audiences
"""

from __future__ import annotations

from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field



class DspAudienceRuleAttributetype(StrEnum):
    ASIN = "ASIN"


class DspAudienceRuleClause(StrEnum):
    INCLUDE = "INCLUDE"


class DspAudienceRuleOperator(StrEnum):
    ONE_OF = "ONE_OF"


class DspAudienceRule(BaseModel):
    """A rule for defining an audience.   **Rule Constraints Table**: Provides available valid combinations of parameters allowed in DspAudienceRule   | audienceType | attributeType | attributeValues | max a"""
    attribute_type: DspAudienceRuleAttributetype = Field(..., alias="attributeType", description="For a given audienceType, the type of the attributes being supplied.")
    attribute_values: list[str] = Field(..., alias="attributeValues", description="For a given audienceType and attributeType combination, the attribute values being supplied.")
    clause: DspAudienceRuleClause = Field(..., description="This parameter is used to include or exclude this particular rule. Currently only include is supported.")
    operator: DspAudienceRuleOperator = Field(..., description="For a given attributeType, the operator used for attributeValues.")

    model_config = {'populate_by_name': True}


class DspAudienceCreateRequestItemAudiencetype(StrEnum):
    PRODUCT_PURCHASES = "PRODUCT_PURCHASES"
    PRODUCT_SEARCH = "PRODUCT_SEARCH"
    PRODUCT_SIMS = "PRODUCT_SIMS"
    PRODUCT_VIEWS = "PRODUCT_VIEWS"
    WHOLE_FOODS_MARKET_PURCHASES = "WHOLE_FOODS_MARKET_PURCHASES"


class DspAudienceCreateRequestItemCountry(StrEnum):
    AE = "AE"
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
    TR = "TR"
    US = "US"


class DspAudienceCreateRequestItem(BaseModel):
    """Complete audience model to be used for creation of the audience."""
    audience_type: DspAudienceCreateRequestItemAudiencetype = Field(..., alias="audienceType", description="Type of audience to create.")
    country: Optional[DspAudienceCreateRequestItemCountry] = Field(None, description="The ISO Alpha-2 code for the country in which the audience will be available during audience discovery and targeting set")
    description: str = Field(..., description="The audience description.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="The unique UUID for this requested audience.")
    lookback: int = Field(..., description="The specified time period (in days) to include those who performed the action in the audience. Lookback Constraints Tabl")
    name: str = Field(..., description="The audience name.")
    rules: list["DspAudienceRule"] = Field(..., description="The set of rules defining an audience; these rules will be ORed.")

    model_config = {'populate_by_name': True}


class DspAudienceError(BaseModel):
    """The error object."""
    message: str

    model_config = {'populate_by_name': True}


class DspAudienceErrorItemErrorErrortype(StrEnum):
    OTHER = "OTHER"
    VALUE_INVALID = "VALUE_INVALID"
    VALUE_OUT_OF_RANGE = "VALUE_OUT_OF_RANGE"


class DspAudienceErrorItemError(BaseModel):
    """The error object."""
    error_type: DspAudienceErrorItemErrorErrortype = Field(..., alias="errorType")
    field_name: Optional[str] = Field(None, alias="fieldName")
    message: str

    model_config = {'populate_by_name': True}


class DspAudienceErrorItem(BaseModel):
    """The error response object."""
    errors: list["DspAudienceErrorItemError"]
    idempotency_key: str = Field(..., alias="idempotencyKey", description="The UUID provided in the request for creation of this audience.")
    index: int = Field(..., description="The index of the DspAudienceCreateRequestItem from the request, e.g. 1st item in the batch request will correspond to in")
    message: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class DspAudienceSuccessItem(BaseModel):
    """The success response object."""
    audience_id: str = Field(..., alias="audienceId", description="The audience identifier.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="The UUID provided in the request for creation of this audience.")
    index: int = Field(..., description="The index of the DspAudienceCreateRequestItem from the request, e.g. 1st item in the batch request will correspond to in")

    model_config = {'populate_by_name': True}


class DspAudienceResponse(BaseModel):
    """This holds an array of successful items and an array of error items from the request."""
    error: list["DspAudienceErrorItem"] = Field(..., description="The items in this array represent items in the request that failed.")
    success: list["DspAudienceSuccessItem"] = Field(..., description="The items in this array represent items in the request that were successful.")

    model_config = {'populate_by_name': True}

