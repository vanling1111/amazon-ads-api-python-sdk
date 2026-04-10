"""Auto-generated Pydantic models. Do not edit manually.

Source: PersonaBuilderAPI_prod_3p.json
Title:  Persona Builder API
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class InsightMetric(BaseModel):
    affinity: float = Field(..., description="Affinity is a measure of how likely customers in the input audience are to belong to this segment. An                   ")
    overlap_percentage: float = Field(..., alias="overlapPercentage", description="Percentage of customers in the input audience who are part of this segment. For example, a value of 5                   ")

    model_config = {'populate_by_name': True}


class ActorInsight(BaseModel):
    actor: str = Field(..., description="The actor's name.")
    insight: "InsightMetric"

    model_config = {'populate_by_name': True}


class AudienceCategory(StrEnum):
    ADVERTISER_AUDIENCES = "ADVERTISER_AUDIENCES"
    COMBINED_AUDIENCES = "COMBINED_AUDIENCES"
    CUSTOM_BUILT = "CUSTOM_BUILT"
    DEMOGRAPHIC = "DEMOGRAPHIC"
    INTEREST = "INTEREST"
    IN_MARKET = "IN_MARKET"
    IN_MARKET_MULTI_COUNTRY = "IN_MARKET_MULTI_COUNTRY"
    LIFESTYLE = "LIFESTYLE"
    LIFE_EVENT = "LIFE_EVENT"
    LOOKALIKE = "LOOKALIKE"
    THIRD_PARTY = "THIRD_PARTY"


class ForecastBands(BaseModel):
    lower_bound: float = Field(..., alias="lowerBound", description="minimum number of devices reached/ minimum number of available impressions.")
    upper_bound: Optional[float] = Field(None, alias="upperBound", description="Optional: maximum number of devices reached/ maximum number of available impressions. 	               If it is not prese")

    model_config = {'populate_by_name': True}


class Forecast(BaseModel):
    daily_impressions: "ForecastBands" = Field(..., alias="dailyImpressions")
    daily_reach: "ForecastBands" = Field(..., alias="dailyReach")

    model_config = {'populate_by_name': True}


class AudienceInsight(BaseModel):
    audience_detail_page_url: Optional[str] = Field(None, alias="audienceDetailPageUrl", description="Link to the audience details page within the Amazon Advertising Console for the given audience.")
    category: str = Field(..., description="Category of the audience segment. Example: interests")
    forecast: "Forecast"
    id_: str = Field(..., alias="id", description="Identifier for the target audience.")
    insight_metrics: "InsightMetric" = Field(..., alias="insightMetrics")
    name: str = Field(..., description="Name of the target audience.")

    model_config = {'populate_by_name': True}


class AudienceV1(BaseModel):
    audience_id: str = Field(..., alias="audienceId", description="An audience identifier retrieved from the audiences/list resource.")
    group_id: str = Field(..., alias="groupId", description="A customer-provided string used to create a group of audiences. This string is only used for this single request. Amazon")
    negative: bool = Field(..., description="Whether to include (false) or exclude (true) audiences when targeting. Only one state may be used per groupId")

    model_config = {'populate_by_name': True}


class AudienceTargetingExpression(BaseModel):
    audiences: list["AudienceV1"] = Field(..., description="Specify groups of audiences to include or exclude when targeting.<ul><li>Included groups are joined by an intersection. ")

    model_config = {'populate_by_name': True}


class BandedSizeInsights(BaseModel):
    max: Optional[float] = Field(None, description="Optional: The upper bound of estimated unique customers who are in the input audience set.                     If it is ")
    min: float = Field(..., description="The lower bound of estimated unique customers who are in the input audience set.")

    model_config = {'populate_by_name': True}


class BandedSizeResponseContent(BaseModel):
    estimated_size: "BandedSizeInsights" = Field(..., alias="estimatedSize")
    last_updated_at: str = Field(..., alias="lastUpdatedAt", description="UTC timestamp in ISO 8601 format indicating when insight was last generated for the audience targeting expression.")

    model_config = {'populate_by_name': True}


class BrowseNode(BaseModel):
    browse_node_name: str = Field(..., alias="browseNodeName", description="Name of the browse node in native language of the marketplace.")

    model_config = {'populate_by_name': True}


class CountryCode(StrEnum):
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


class Currency(StrEnum):
    AED = "AED"
    AUD = "AUD"
    BRL = "BRL"
    CAD = "CAD"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"
    JPY = "JPY"
    MXN = "MXN"
    SAR = "SAR"
    SEK = "SEK"
    TRY = "TRY"
    USD = "USD"


class DateRangeInsight(BaseModel):
    end_date: str = Field(..., alias="endDate", description="UTC timestamp in ISO 8601 format indicating the end date of the insight.")
    start_date: str = Field(..., alias="startDate", description="UTC timestamp in ISO 8601 format indicating the start date of the insight.")

    model_config = {'populate_by_name': True}


class Range(BaseModel):
    max: Optional[float] = Field(None, description="Upper bound of the range (inclusive). Optional - if max does not exist then the range has no upper                     b")
    min: Optional[float] = Field(None, description="Lower bound of the range (inclusive). Optional - if min does not exist then the range has no lower                     b")

    model_config = {'populate_by_name': True}


class RangedDemographicInsight(BaseModel):
    insight_metrics: "InsightMetric" = Field(..., alias="insightMetrics")
    range: "Range"
    segment_id: str = Field(..., alias="segmentId", description="Canonical ID of the segment the demographic insight attribute maps to.")

    model_config = {'populate_by_name': True}


class PropertyOwnership(StrEnum):
    OWNING = "OWNING"
    RENTING = "RENTING"


class PropertyOwnershipInsight(BaseModel):
    attribute: "PropertyOwnership"
    insight_metrics: "InsightMetric" = Field(..., alias="insightMetrics")
    segment_id: str = Field(..., alias="segmentId", description="Canonical ID of the segment the demographic insight attribute maps to.")

    model_config = {'populate_by_name': True}


class Gender(StrEnum):
    BOTH = "BOTH"
    FEMALE = "FEMALE"
    MALE = "MALE"
    UNKNOWN = "UNKNOWN"


class GenderInsight(BaseModel):
    attribute: "Gender"
    insight_metrics: "InsightMetric" = Field(..., alias="insightMetrics")
    segment_id: Optional[str] = Field(None, alias="segmentId", description="Canonical ID of the segment the demographic insight attribute maps to.")

    model_config = {'populate_by_name': True}


class Education(StrEnum):
    BACHELORS_DEGREE = "BACHELORS_DEGREE"
    BACHELOR_DEGREE_OR_MORE = "BACHELOR_DEGREE_OR_MORE"
    GRADUATE_DEGREE = "GRADUATE_DEGREE"
    HIGH_SCHOOL = "HIGH_SCHOOL"
    SOME_COLLEGE = "SOME_COLLEGE"


class EducationInsight(BaseModel):
    attribute: "Education"
    insight_metrics: "InsightMetric" = Field(..., alias="insightMetrics")
    segment_id: str = Field(..., alias="segmentId", description="Canonical ID of the segment the demographic insight attribute maps to.")

    model_config = {'populate_by_name': True}


class IncomeDemographicInsight(BaseModel):
    currency: "Currency"
    insight_metrics: "InsightMetric" = Field(..., alias="insightMetrics")
    range: "Range"
    segment_id: str = Field(..., alias="segmentId", description="Canonical ID of the segment the demographic insight attribute maps to.")

    model_config = {'populate_by_name': True}


class DemographicInsights(BaseModel):
    age: Optional[list["RangedDemographicInsight"]] = None
    children_age: Optional[list["RangedDemographicInsight"]] = Field(None, alias="childrenAge")
    children_count: Optional[list["RangedDemographicInsight"]] = Field(None, alias="childrenCount")
    education: Optional[list["EducationInsight"]] = None
    gender: Optional[list["GenderInsight"]] = None
    income: Optional[list["IncomeDemographicInsight"]] = None
    property_ownership: Optional[list["PropertyOwnershipInsight"]] = Field(None, alias="propertyOwnership")

    model_config = {'populate_by_name': True}


class DemographicsResponseContent(BaseModel):
    demographics: "DemographicInsights"
    last_updated_at: str = Field(..., alias="lastUpdatedAt", description="UTC timestamp in ISO 8601 format indicating when insight was last generated for the input audience set.")

    model_config = {'populate_by_name': True}


class DirectorInsight(BaseModel):
    director: str = Field(..., description="The director's name.")
    insight: "InsightMetric"

    model_config = {'populate_by_name': True}


class DspSubErrorV1(BaseModel):
    error_type: str = Field(..., alias="errorType")
    field_name: Optional[str] = Field(None, alias="fieldName")
    message: str

    model_config = {'populate_by_name': True}


class DspBadRequestExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspForbiddenExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspInternalServerExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspNotFoundExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspTooManyRequestsExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspUnauthorizedExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspUnsupportedMediaTypeExceptionV1ResponseContent(BaseModel):
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class GenreInsight(BaseModel):
    genre: str = Field(..., description="A human readable genre name.")
    insight: "InsightMetric"

    model_config = {'populate_by_name': True}


class InputExpression(BaseModel):
    """The input expression should consist of audience targeting expression."""
    audience_targeting_expression: "AudienceTargetingExpression" = Field(..., alias="audienceTargetingExpression")
    country_codes: Optional[list["CountryCode"]] = Field(None, alias="countryCodes", description="Optional:      Array of strings = 1 items      The ISO Alpha-2 country codes to show insight for specified countries. Th")

    model_config = {'populate_by_name': True}


class MovieInsight(BaseModel):
    insight: "InsightMetric"
    movie: str = Field(..., description="A human readable movie name.")

    model_config = {'populate_by_name': True}


class OverlapAffinityFilter(BaseModel):
    max: Optional[float] = Field(None, description="Optional: If specified, the affinities of all returned overlapping audiences will be at most (inclusive) the provided af")
    min: Optional[float] = Field(None, description="Optional: If specified, the affinities of all returned overlapping audiences will be at least (inclusive) the provided a")

    model_config = {'populate_by_name': True}


class PrimeVideoCategory(StrEnum):
    ACTORS = "ACTORS"
    DIRECTORS = "DIRECTORS"
    GENRES = "GENRES"
    MOVIES = "MOVIES"
    SERIES = "SERIES"


class PrimeVideoInputExpression(BaseModel):
    """The input expression should consist of audience targeting expression."""
    audience_targeting_expression: "AudienceTargetingExpression" = Field(..., alias="audienceTargetingExpression")
    category_filter: Optional[list["PrimeVideoCategory"]] = Field(None, alias="categoryFilter", description="Optional: A list of prime video categories to filter insights on. By default it will return all                    prime")
    country_codes: Optional[list["CountryCode"]] = Field(None, alias="countryCodes", description="Optional:     Array of strings = 1 items     The ISO Alpha-2 country codes to show insight for specified countries. This")

    model_config = {'populate_by_name': True}


class SeriesInsight(BaseModel):
    insight: "InsightMetric"
    series: str = Field(..., description="A human readable TV Series name.")

    model_config = {'populate_by_name': True}


class PrimeVideoInsight(BaseModel):
    actors: Optional[list["ActorInsight"]] = None
    date_range: Optional["DateRangeInsight"] = Field(None, alias="dateRange")
    directors: Optional[list["DirectorInsight"]] = None
    genres: Optional[list["GenreInsight"]] = None
    movies: Optional[list["MovieInsight"]] = None
    series: Optional[list["SeriesInsight"]] = None

    model_config = {'populate_by_name': True}


class PrimeVideoResponseContent(BaseModel):
    last_updated_at: str = Field(..., alias="lastUpdatedAt", description="UTC timestamp in ISO 8601 format indicating when insight was last generated for the input expression.")
    prime_video_insights: "PrimeVideoInsight" = Field(..., alias="primeVideoInsights")

    model_config = {'populate_by_name': True}


class TopRetailCategoryInsight(BaseModel):
    id_: str = Field(..., alias="id", description="Identifier of retail category.")
    insight_metrics: "InsightMetric" = Field(..., alias="insightMetrics")
    name: str = Field(..., description="Name of retail category.")
    path: list["BrowseNode"] = Field(..., description="The hierarchical path that leads to a category node, starting with the root node.")

    model_config = {'populate_by_name': True}


class TopCategoriesPurchasedResponseContent(BaseModel):
    last_updated_at: str = Field(..., alias="lastUpdatedAt", description="UTC timestamp in ISO 8601 format indicating when insight was last generated for the input audience set.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional: If present, there are more insights than initially returned. Use this token to call the operation again       ")
    retail_categories: list["TopRetailCategoryInsight"] = Field(..., alias="retailCategories", description="Top retail categories purchased by customers in the input expression., ordered by the affinity score.                   ")

    model_config = {'populate_by_name': True}


class TopOverlappingAudiencesInputExpression(BaseModel):
    """The input expression should consist of audience targeting expression."""
    audience_targeting_expression: "AudienceTargetingExpression" = Field(..., alias="audienceTargetingExpression")
    category_filter: Optional[list["AudienceCategory"]] = Field(None, alias="categoryFilter", description="Optional: A list of audience categories to filter insights on. By default it will return all audience category types in ")
    country_codes: Optional[list["CountryCode"]] = Field(None, alias="countryCodes", description="Optional:     Array of strings = 1 items     The ISO Alpha-2 country codes to show insight for specified countries. This")
    overlap_affinity_filter: Optional["OverlapAffinityFilter"] = Field(None, alias="overlapAffinityFilter")

    model_config = {'populate_by_name': True}


class TopOverlappingAudiencesResponseContent(BaseModel):
    audiences: list["AudienceInsight"] = Field(..., description="Top audiences associated with customers in the input expression, ordered by the affinity score.                       Af")
    last_updated_at: str = Field(..., alias="lastUpdatedAt", description="UTC timestamp in ISO 8601 format indicating when insight was last generated for the input audience set.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional: If present, there are more insights than initially returned. Use this token to call the operation again and ha")

    model_config = {'populate_by_name': True}

