"""Auto-generated Pydantic models. Do not edit manually.

Source: DataProvider_prod_3p.json
Title:  DataProvider
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class AccessDeniedErrorCode(StrEnum):
    ACCESS_DENIED = "ACCESS_DENIED"


class InvalidArgumentErrorCode(StrEnum):
    INVALID_ARGUMENT = "INVALID_ARGUMENT"


class ValidationExceptionResponseContent(BaseModel):
    code: "InvalidArgumentErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class NotFoundErrorCode(StrEnum):
    NOT_FOUND = "NOT_FOUND"


class TargetingClausesConfiguration(BaseModel):
    """The targeting group configuration values for a specific advertiser context. This includes bid and     keyword validation values."""
    max_bid_video_advertisement: Optional[float] = Field(None, alias="maxBidVideoAdvertisement", description="The maximum bid value for a Sponsored Brands video campaign.")
    min_bid: float = Field(..., alias="minBid", description="The default minimum bid value for campaigns.")
    min_bid_video_advertisement: Optional[float] = Field(None, alias="minBidVideoAdvertisement", description="The minimum bid value for a Sponsored Brands video campaign.")
    keyword_validation_regex: Optional[str] = Field(None, alias="keywordValidationRegex", description="Regex string used to validate keywords.")
    max_keyword_length: Optional[float] = Field(None, alias="maxKeywordLength", description="The maximum allowed length of a keyword.")
    max_bid: float = Field(..., alias="maxBid", description="The default maximum bid value for campaigns.")

    model_config = {'populate_by_name': True}


class EntityToTargetingConfigurations(BaseModel):
    """A nested structure mapping advertiser contexts to targeting clause configuration values. The keys at this level are entity types, capitalized strings mapping to the advertiser's account profile. The v"""
    __root__: dict[str, "TargetingClausesConfiguration"] = {}


class ProgramToEntityToTargetingConfigurations(BaseModel):
    """A nested structure mapping advertiser contexts to targeting clause configuration values. The keys at this level are program types, two capitalized characters mapping to a specific builder. The valid p"""
    __root__: dict[str, "EntityToTargetingConfigurations"] = {}


class ResourceNotFoundExceptionResponseContent(BaseModel):
    code: "NotFoundErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class InternalErrorErrorCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class InternalServerExceptionResponseContent(BaseModel):
    code: "InternalErrorErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class ThrottledErrorCode(StrEnum):
    THROTTLED = "THROTTLED"


class ProgramType(StrEnum):
    SB = "SB"
    SP = "SP"
    SD = "SD"


class AccessDeniedExceptionResponseContent(BaseModel):
    code: "AccessDeniedErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class CountryCode(StrEnum):
    US = "US"
    CA = "CA"
    MX = "MX"
    BR = "BR"
    UK = "UK"
    DE = "DE"
    FR = "FR"
    ES = "ES"
    IN = "IN"
    IT = "IT"
    NL = "NL"
    AE = "AE"
    SA = "SA"
    SE = "SE"
    TR = "TR"
    PL = "PL"
    EG = "EG"
    JP = "JP"
    AU = "AU"
    SG = "SG"
    CN = "CN"


class EntityType(StrEnum):
    SELLER = "SELLER"
    VENDOR = "VENDOR"


class getCampaignsValidationConfigsRequestContent(BaseModel):
    """An advertiser context is a combination of specific marketplace, entity, and program type that an     advertiser belongs to. This context defines the specific configuration values the API is requesting"""
    country_codes_list: Optional[list["CountryCode"]] = Field(None, alias="countryCodesList", description="The list of countryCode enums defining the marketplaces whose configuration values are requested.         When `null` is")
    entity_types_list: Optional[list["EntityType"]] = Field(None, alias="entityTypesList", description="The list of entityType enums defining the marketplaces whose configuration values are requested.         When `null` is ")
    program_types_list: Optional[list["ProgramType"]] = Field(None, alias="programTypesList", description="The list of programType enums defining the marketplaces whose configuration values are requested.         When `null` is")

    model_config = {'populate_by_name': True}


class CampaignsConfigurations(BaseModel):
    """The campaign validation configuration values for a specific advertiser context. This includes budget     and inputted name field configuration values."""
    max_ad_group_name_length: float = Field(..., alias="maxAdGroupNameLength", description="The maximum allowed length of an ad group name.")
    min_lifetime_budget: Optional[float] = Field(None, alias="minLifetimeBudget", description="The minimum lifetime budget allowed for campaigns.")
    max_daily_budget: float = Field(..., alias="maxDailyBudget", description="The maximum daily budget allowed for campaigns.")
    max_campaign_name_length: float = Field(..., alias="maxCampaignNameLength", description="The maximum allowed length of a campaign name.")
    min_daily_budget: float = Field(..., alias="minDailyBudget", description="The minimum daily budget allowed for campaigns.")
    max_lifetime_budget: Optional[float] = Field(None, alias="maxLifetimeBudget", description="The maximum lifetime budget allowed for campaigns.")
    max_portfolio_name_length: float = Field(..., alias="maxPortfolioNameLength", description="The maximum allowed length of a portfolio name.")
    text_field_validation_regex: str = Field(..., alias="textFieldValidationRegex", description="The regex string used to validate the characters and order of characters for campaign names,         ad group names, and")

    model_config = {'populate_by_name': True}


class EntityToCampaignsConfigurations(BaseModel):
    """A nested structure mapping advertiser contexts to campaign configuration values. The keys at this level are entity types, capitalized strings mapping to the advertiser's account profile. The valid ent"""
    __root__: dict[str, "CampaignsConfigurations"] = {}


class ProgramToEntityToCampaignsConfigurations(BaseModel):
    """A nested structure mapping advertiser contexts to campaign configuration values. The keys at this level are program types, two capitalized characters mapping to a specific builder. The valid program t"""
    __root__: dict[str, "EntityToCampaignsConfigurations"] = {}


class CountryToProgramToEntityToCampaignsConfigurations(BaseModel):
    """A nested structure mapping advertiser contexts to campaign configuration values. The keys at this level are country codes, two capitalized characters mapping to a marketplace. The valid country codes """
    __root__: dict[str, "ProgramToEntityToCampaignsConfigurations"] = {}


class CountryToProgramToEntityToTargetingConfigurations(BaseModel):
    """A nested structure mapping advertiser contexts to targeting clause configuration values. The keys at this level are country codes, two capitalized characters mapping to a marketplace. The valid countr"""
    __root__: dict[str, "ProgramToEntityToTargetingConfigurations"] = {}


class getTargetingClausesValidationConfigsRequestContent(BaseModel):
    """An advertiser context is a combination of specific marketplace, entity, and program type that an     advertiser belongs to. This context defines the specific configuration values the API is requesting"""
    country_codes_list: Optional[list["CountryCode"]] = Field(None, alias="countryCodesList", description="The list of countryCode enums defining the marketplaces whose configuration values are requested.         When `null` is")
    entity_types_list: Optional[list["EntityType"]] = Field(None, alias="entityTypesList", description="The list of entityType enums defining the marketplaces whose configuration values are requested.         When `null` is ")
    program_types_list: Optional[list["ProgramType"]] = Field(None, alias="programTypesList", description="The list of programType enums defining the marketplaces whose configuration values are requested.         When `null` is")

    model_config = {'populate_by_name': True}


class getCampaignsValidationConfigsResponseContent(BaseModel):
    """The key `campaignsValidationConfigs` is mapped to this API's returned object: a nested structure mapping country code to program type to entity type to campaign configuration values. The campaign conf"""
    campaign_validation_configs: "CountryToProgramToEntityToCampaignsConfigurations" = Field(..., alias="campaignValidationConfigs")

    model_config = {'populate_by_name': True}


class getTargetingClausesValidationConfigsResponseContent(BaseModel):
    """The key `targetingClausesValidationConfigs` is mapped to this API's returned object: a nested structure mapping country code to program type to entity type to targeting clause configuration values. Th"""
    targeting_clauses_validation_configs: "CountryToProgramToEntityToTargetingConfigurations" = Field(..., alias="targetingClausesValidationConfigs")

    model_config = {'populate_by_name': True}


class ThrottlingExceptionResponseContent(BaseModel):
    code: "ThrottledErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}

