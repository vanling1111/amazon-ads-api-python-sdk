"""Auto-generated Pydantic models. Do not edit manually.

Source: ReachPlanningService_prod_3p.json
Title:  Reach Planning Service
"""

from __future__ import annotations

from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field



class AudienceTargetTypeV1(StrEnum):
    AUDIENCE = "AUDIENCE"


class AudienceTargetV1(BaseModel):
    audience_id: str = Field(..., alias="audienceId", description="The unique identifier for the audience. Use the [audiences](https://advertising.amazon.com/API/docs/en-us/audiences/#/Di")
    group_id: Optional[str] = Field(None, alias="groupId", description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g., '1'). To add audience")
    target_type: "AudienceTargetTypeV1" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class ErrorCode(StrEnum):
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    INVALID_MULTI_COUNTRY_LOCATION = "INVALID_MULTI_COUNTRY_LOCATION"
    MAX_CPC_TOO_LOW = "MAX_CPC_TOO_LOW"
    PERFORMANCE_CURVE_ERROR = "PERFORMANCE_CURVE_ERROR"
    REACH_CURVE_DEDUPLICATION_ERROR = "REACH_CURVE_DEDUPLICATION_ERROR"
    REACH_CURVE_ERROR = "REACH_CURVE_ERROR"
    REACH_FORECAST_NOT_FOUND = "REACH_FORECAST_NOT_FOUND"
    REQUEST_VALIDATION_ERROR = "REQUEST_VALIDATION_ERROR"
    SERVER_TIMEOUT = "SERVER_TIMEOUT"
    TARGETING_TOO_NARROW = "TARGETING_TOO_NARROW"
    UNAUTHORIZED_ERROR = "UNAUTHORIZED_ERROR"


class BadRequestExceptionResponseContent(BaseModel):
    """Bad Request."""
    code: Optional["ErrorCode"] = None
    message: Optional[str] = Field(None, description="Human readable response message.")

    model_config = {'populate_by_name': True}


class BiddingInfoV1(BaseModel):
    """The information about bidding cost."""
    max_avg_cpm: Optional[float] = Field(None, alias="maxAvgCpm", description="Maximum average CPM rate (cost per thousand impressions). If not provided, we will assume default value based on histori")
    max_cpc: Optional[float] = Field(None, alias="maxCpc", description="Maximum CPC (cost per click). If not provided, we will assume default value based on historical measurement.")
    max_v_cpm: Optional[float] = Field(None, alias="maxVCpm", description="Maximum vCPM rate (cost per thousand viewable impressions). If not provided, we will assume default value based on histo")

    model_config = {'populate_by_name': True}


class BudgetAllocationV1(BaseModel):
    reach: int = Field(..., description="The reach number of the selected data point of the reach forecast.")
    reach_forecast_id: str = Field(..., alias="reachForecastId", description="The identifier of the Reach Forecast that the specified budget is allocated to.")

    model_config = {'populate_by_name': True}


class ContentGenreTargetTypeV1(StrEnum):
    CONTENT_GENRE = "CONTENT_GENRE"


class ContentGenreV1(StrEnum):
    ACTION = "ACTION"
    ADVENTURE = "ADVENTURE"
    ANIMATION = "ANIMATION"
    BIOGRAPHY = "BIOGRAPHY"
    COMEDY = "COMEDY"
    CRIME = "CRIME"
    DOCUMENTARY = "DOCUMENTARY"
    DRAMA = "DRAMA"
    FAMILY = "FAMILY"
    FANTASY = "FANTASY"
    FILM_NOIR = "FILM_NOIR"
    GAME_SHOW = "GAME_SHOW"
    GENRE_NOT_AVAILABLE = "GENRE_NOT_AVAILABLE"
    HISTORY = "HISTORY"
    HORROR = "HORROR"
    MUSICAL = "MUSICAL"
    MYSTERY = "MYSTERY"
    NEWS = "NEWS"
    REALITY_TV = "REALITY_TV"
    ROMANCE = "ROMANCE"
    SCIENCE_FICTION = "SCIENCE_FICTION"
    SHORT = "SHORT"
    SPORT = "SPORT"
    SUPER_HERO = "SUPER_HERO"
    TALK_SHOW = "TALK_SHOW"
    THRILLER = "THRILLER"
    WAR = "WAR"
    WESTERN = "WESTERN"


class ContentGenreTargetV1(BaseModel):
    content_genre: "ContentGenreV1" = Field(..., alias="contentGenre")
    target_type: "ContentGenreTargetTypeV1" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class DspContentRatingV1(StrEnum):
    RATING_NOT_AVAILABLE = "RATING_NOT_AVAILABLE"
    SUITABLE_FOR_ADULTS = "SUITABLE_FOR_ADULTS"
    SUITABLE_FOR_ALL_AUDIENCES = "SUITABLE_FOR_ALL_AUDIENCES"
    SUITABLE_FOR_MATURE_AUDIENCES = "SUITABLE_FOR_MATURE_AUDIENCES"
    SUITABLE_FOR_MOST_AUDIENCES_WITH_PARENTAL_GUIDANCE = "SUITABLE_FOR_MOST_AUDIENCES_WITH_PARENTAL_GUIDANCE"
    SUITABLE_FOR_TEEN_AND_OLDER_AUDIENCES = "SUITABLE_FOR_TEEN_AND_OLDER_AUDIENCES"


class ContentRatingDetailsV1(BaseModel):
    pass


class ContentRatingTargetTypeV1(StrEnum):
    CONTENT_RATING = "CONTENT_RATING"


class ContentRatingTypeV1(StrEnum):
    DSP_CONTENT_RATING = "DSP_CONTENT_RATING"


class ContentRatingTargetV1(BaseModel):
    content_rating_details: "ContentRatingDetailsV1" = Field(..., alias="contentRatingDetails")
    content_rating_type: "ContentRatingTypeV1" = Field(..., alias="contentRatingType")
    target_type: "ContentRatingTargetTypeV1" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class CountryCodeV1(StrEnum):
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
    NZ = "NZ"
    SA = "SA"
    SE = "SE"
    TR = "TR"
    US = "US"


class CreateDeduplicatedReachForecastsV1RequestElement(BaseModel):
    budget_allocations: list["BudgetAllocationV1"] = Field(..., alias="budgetAllocations", description="The list of budget allocations for the Reach Forecasts to have their reach deduplicated. Total number of unique Reach Fo")

    model_config = {'populate_by_name': True}


class CreateDeduplicatedReachForecastsV1RequestContent(BaseModel):
    deduplicated_reach_forecasts: list["CreateDeduplicatedReachForecastsV1RequestElement"] = Field(..., alias="deduplicatedReachForecasts", description="A list of Deduplicate Reach Forecasts to create. Maximum 100 unique Reach Forecasts can be involved in a single request.")

    model_config = {'populate_by_name': True}


class CreateDeduplicatedReachForecastsV1ResponseElement(BaseModel):
    deduplicated_reach: int = Field(..., alias="deduplicatedReach", description="Forecasted deduplicated reach.")
    deduplicated_reach_forecast_id: str = Field(..., alias="deduplicatedReachForecastId", description="This is the unique identifier of the Deduplicated Reach Forecast resource.")

    model_config = {'populate_by_name': True}


class CreateDeduplicatedReachForecastsV1ResponseSuccess(BaseModel):
    deduplicated_reach_forecast: "CreateDeduplicatedReachForecastsV1ResponseElement" = Field(..., alias="deduplicatedReachForecast")
    index: int = Field(..., description="This is the index of the corresponding request element in the request payload.")

    model_config = {'populate_by_name': True}


class ReachPlanningServiceError(BaseModel):
    code: Optional["ErrorCode"] = None
    message: Optional[str] = Field(None, description="Human readable response message.")

    model_config = {'populate_by_name': True}


class CreateDeduplicatedReachForecastsV1ResponseError(BaseModel):
    error: "ReachPlanningServiceError"
    index: int = Field(..., description="This is the index of the corresponding request element in the request payload.")

    model_config = {'populate_by_name': True}


class CreateDeduplicatedReachForecastsV1ResponseContent(BaseModel):
    error: list["CreateDeduplicatedReachForecastsV1ResponseError"]
    success: list["CreateDeduplicatedReachForecastsV1ResponseSuccess"]

    model_config = {'populate_by_name': True}


class IABCategoryTargetTypeV1(StrEnum):
    IAB_CATEGORY = "IAB_CATEGORY"


class IABCategoryTargetV1(BaseModel):
    iab_content_category: str = Field(..., alias="iabContentCategory", description="The IAB content category to target. To get the list of valid values, see https://advertising.amazon.com/API/docs/en-us/d")
    target_type: "IABCategoryTargetTypeV1" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class ProductCategoryTargetTypeV1(StrEnum):
    PRODUCT_CATEGORY = "PRODUCT_CATEGORY"


class ProductCategoryTargetV1(BaseModel):
    asin_category: str = Field(..., alias="asinCategory", description="The product category to target.")
    target_type: "ProductCategoryTargetTypeV1" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class ThemeTargetMatchTypeV1(StrEnum):
    KEYWORDS_RELATED_TO_YOUR_BRAND = "KEYWORDS_RELATED_TO_YOUR_BRAND"
    KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES = "KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES"


class ThemeTargetTypeV1(StrEnum):
    THEME = "THEME"


class ThemeTargetV1(BaseModel):
    match_type: "ThemeTargetMatchTypeV1" = Field(..., alias="matchType")
    target_type: "ThemeTargetTypeV1" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class ProductTargetTypeV1(StrEnum):
    PRODUCT = "PRODUCT"


class ProductTargetV1(BaseModel):
    asin: str = Field(..., description="The product asin to target.")
    target_type: "ProductTargetTypeV1" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class DeviceTargetTypeV1(StrEnum):
    DEVICE = "DEVICE"


class DeviceTypeV1(StrEnum):
    CONNECTED_DEVICE = "CONNECTED_DEVICE"
    CONNECTED_TV = "CONNECTED_TV"
    DESKTOP = "DESKTOP"
    MOBILE = "MOBILE"


class DeviceTargetV1(BaseModel):
    device_type: "DeviceTypeV1" = Field(..., alias="deviceType")
    target_type: "DeviceTargetTypeV1" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class UserLocationSignalV1(StrEnum):
    CURRENT = "CURRENT"
    HOME = "HOME"
    MULTIPLE_SIGNALS = "MULTIPLE_SIGNALS"


class LocationTargetTypeV1(StrEnum):
    LOCATION = "LOCATION"


class LocationTargetV1(BaseModel):
    geo_location: str = Field(..., alias="geoLocation", description="The location to target. Use the [GeoLocation API](https://advertising.amazon.com/API/docs/en-us/dsp-campaigns#tag/Discov")
    target_type: "LocationTargetTypeV1" = Field(..., alias="targetType")
    user_location_signal: Optional["UserLocationSignalV1"] = Field(None, alias="userLocationSignal")

    model_config = {'populate_by_name': True}


class InventorySourceTypeV1(StrEnum):
    DEAL = "DEAL"
    PUBLISHER = "PUBLISHER"


class InventorySourceTargetTypeV1(StrEnum):
    INVENTORY_SOURCE = "INVENTORY_SOURCE"


class InventorySourceTargetV1(BaseModel):
    inventory_source_id: str = Field(..., alias="inventorySourceId", description="The identifier of the inventory source. These can be obtained from the inventory sources discovery endpoint.")
    inventory_source_type: "InventorySourceTypeV1" = Field(..., alias="inventorySourceType")
    target_type: "InventorySourceTargetTypeV1" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class KeywordTargetTypeV1(StrEnum):
    KEYWORD = "KEYWORD"


class KeywordTargetMatchTypeV1(StrEnum):
    BROAD = "BROAD"
    EXACT = "EXACT"
    PHRASE = "PHRASE"


class KeywordTargetV1(BaseModel):
    keyword: str
    match_type: "KeywordTargetMatchTypeV1" = Field(..., alias="matchType")
    target_type: "KeywordTargetTypeV1" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class PlanningTargetDetailsV1(BaseModel):
    pass


class PlanningTargetV1(BaseModel):
    negative: bool = Field(..., description="Whether to target (false) or exclude (true) the given target.")
    target_details: "PlanningTargetDetailsV1" = Field(..., alias="targetDetails")

    model_config = {'populate_by_name': True}


class FrequencyCapTypeV1(StrEnum):
    CUSTOM = "CUSTOM"
    UNCAPPED = "UNCAPPED"


class FrequencyCapTimeUnitV1(StrEnum):
    DAYS = "DAYS"
    MONTHS = "MONTHS"
    WEEKS = "WEEKS"


class FrequencyCapV1(BaseModel):
    """The limit of how many times ads appear to the same viewer."""
    max_impressions: Optional[int] = Field(None, alias="maxImpressions", description="The maximum number of times an ad is displayed.")
    time_unit: Optional["FrequencyCapTimeUnitV1"] = Field(None, alias="timeUnit")
    time_unit_count: Optional[int] = Field(None, alias="timeUnitCount", description="The count of time units.")
    type_: Optional["FrequencyCapTypeV1"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class DeliveryTypeV1(StrEnum):
    GUARANTEED = "GUARANTEED"
    NON_GUARANTEED = "NON_GUARANTEED"


class SupplyV1(StrEnum):
    DSP_ALEXA_DISPLAY = "DSP_ALEXA_DISPLAY"
    DSP_AUDIO = "DSP_AUDIO"
    DSP_DISPLAY = "DSP_DISPLAY"
    DSP_FIRE_TABLET = "DSP_FIRE_TABLET"
    DSP_FIRE_TV = "DSP_FIRE_TV"
    DSP_FIRE_TV_FIRE_TABLET_ALEXA_DISPLAY = "DSP_FIRE_TV_FIRE_TABLET_ALEXA_DISPLAY"
    DSP_OLV = "DSP_OLV"
    DSP_PRIME_VIDEO = "DSP_PRIME_VIDEO"
    DSP_STREAMING_TV = "DSP_STREAMING_TV"
    DSP_TWITCH_DISPLAY = "DSP_TWITCH_DISPLAY"
    DSP_TWITCH_VIDEO = "DSP_TWITCH_VIDEO"
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_BRANDS_VIDEO = "SPONSORED_BRANDS_VIDEO"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"


class ReachTypeV1(StrEnum):
    HOUSEHOLDS = "HOUSEHOLDS"


class CreateReachForecastsV1RequestElement(BaseModel):
    advertised_product_category_ids: Optional[list[str]] = Field(None, alias="advertisedProductCategoryIds", description="The identifiers of the advertised product categories for the forecast. Use the DSP [ListAdvertisedProductCategories API]")
    country_code: "CountryCodeV1" = Field(..., alias="countryCode")
    delivery_type: "DeliveryTypeV1" = Field(..., alias="deliveryType")
    end_date: str = Field(..., alias="endDate", description="The forecast end date in YYYY-MM-DD format.")
    frequency_cap: Optional["FrequencyCapV1"] = Field(None, alias="frequencyCap")
    reach_type: "ReachTypeV1" = Field(..., alias="reachType")
    start_date: str = Field(..., alias="startDate", description="The forecast start date in YYYY-MM-DD format.")
    supply_package: Optional[list["SupplyV1"]] = Field(None, alias="supplyPackage", description="The combination of Ads supply.")
    targets: Optional[list["PlanningTargetV1"]] = Field(None, description="The list of targets for the forecast. Targets of the same targetType and of the same negative boolean are combined using")

    model_config = {'populate_by_name': True}


class CreateReachForecastsV1RequestContent(BaseModel):
    common_targets: Optional[list["PlanningTargetV1"]] = Field(None, alias="commonTargets", description="The list of common targets to be applied to all reach forecasts to be created in this request. The common targets will b")
    reach_forecasts: list["CreateReachForecastsV1RequestElement"] = Field(..., alias="reachForecasts", description="A list of reach forecast to be created.")

    model_config = {'populate_by_name': True}


class ReachCurveDataPointV1(BaseModel):
    impressions: int = Field(..., description="The number of on-target impressions.")
    reach: int = Field(..., description="The forecasted on-target reached.")
    spend: float = Field(..., description="The forecasted spend in requested currency based on the estimated average CPM.")

    model_config = {'populate_by_name': True}


class CurrencyCodeV1(StrEnum):
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


class ReachForecastStatusV1(StrEnum):
    EXPIRED = "EXPIRED"
    SUCCESS = "SUCCESS"


class CreateReachForecastsV1ResponseElement(BaseModel):
    available_impressions: Optional[int] = Field(None, alias="availableImpressions", description="The number of impressions available for you to purchase after considering contention (G - booked demand) among the match")
    avg_cpm: Optional[float] = Field(None, alias="avgCpm", description="The CPM rate (cost per thousand impressions).")
    country_code: "CountryCodeV1" = Field(..., alias="countryCode")
    cpc: Optional[float] = Field(None, description="The CPC rate (cost per click).")
    creation_date_time: str = Field(..., alias="creationDateTime", description="The date time that the reach forecast was created.")
    currency_code: "CurrencyCodeV1" = Field(..., alias="currencyCode")
    data_points: list["ReachCurveDataPointV1"] = Field(..., alias="dataPoints", description="The list of data points for the reach curve.")
    matching_impressions: Optional[int] = Field(None, alias="matchingImpressions", description="The number of impressions that match your targeting")
    max_cpm: Optional[float] = Field(None, alias="maxCpm", description="The maximum CPM rate (cost per thousand impressions).")
    reach_forecast_id: str = Field(..., alias="reachForecastId", description="This is the unique identifier of the Reach Forecast resource.")
    status: "ReachForecastStatusV1"

    model_config = {'populate_by_name': True}


class CreateReachForecastsV1ResponseSuccess(BaseModel):
    index: int = Field(..., description="This is the index of the corresponding request element in the request payload.")
    reach_forecast: "CreateReachForecastsV1ResponseElement" = Field(..., alias="reachForecast")

    model_config = {'populate_by_name': True}


class CreateReachForecastsV1ResponseError(BaseModel):
    error: "ReachPlanningServiceError"
    index: int = Field(..., description="This is the index of the corresponding request element in the request payload.")

    model_config = {'populate_by_name': True}


class CreateReachForecastsV1ResponseContent(BaseModel):
    error: list["CreateReachForecastsV1ResponseError"]
    success: list["CreateReachForecastsV1ResponseSuccess"]

    model_config = {'populate_by_name': True}


class ForbiddenExceptionResponseContent(BaseModel):
    """Forbidden."""
    code: Optional["ErrorCode"] = None
    message: Optional[str] = Field(None, description="Human readable response message.")

    model_config = {'populate_by_name': True}


class PerformanceCurveDataPointV1(BaseModel):
    cpc: Optional[float] = Field(None, description="Cost Per Click")
    cpdpv: Optional[float] = Field(None, description="Cost Per Detail Page View")
    cpvc: Optional[float] = Field(None, description="Cost Per Video Completion")
    ctr: Optional[float] = Field(None, description="Click-Through Rate")
    ecpm: Optional[float] = Field(None, description="Effective Cost Per Mille")
    prediction: float = Field(..., description="Prediction for the performance metric requested in the input.")
    spend: float = Field(..., description="The monetary spend to achieve the provided prediction (in the currency specified).")
    vcr: Optional[float] = Field(None, description="Video Completion Rate")

    model_config = {'populate_by_name': True}


class PerformanceMetricV1(StrEnum):
    CLICK = "CLICK"
    DETAIL_PAGE_VIEW = "DETAIL_PAGE_VIEW"
    VIDEO_COMPLETION = "VIDEO_COMPLETION"


class GeneratePerformanceForecastV1ResponseElement(BaseModel):
    """Performance curve for a specific metric"""
    country_code: "CountryCodeV1" = Field(..., alias="countryCode")
    creation_date_time: str = Field(..., alias="creationDateTime", description="The date time that the performance forecast was created.")
    currency_code: "CurrencyCodeV1" = Field(..., alias="currencyCode")
    data_points: list["PerformanceCurveDataPointV1"] = Field(..., alias="dataPoints", description="List of data points for the curve")
    performance_metric: "PerformanceMetricV1" = Field(..., alias="performanceMetric")

    model_config = {'populate_by_name': True}


class GeneratePerformanceForecastsV1RequestElement(BaseModel):
    advertised_product_category_ids: Optional[list[str]] = Field(None, alias="advertisedProductCategoryIds", description="The identifiers of the advertised product categories for the forecast. Use the DSP [ListAdvertisedProductCategories API]")
    bidding_info: Optional["BiddingInfoV1"] = Field(None, alias="biddingInfo")
    country_code: "CountryCodeV1" = Field(..., alias="countryCode")
    delivery_type: "DeliveryTypeV1" = Field(..., alias="deliveryType")
    end_date: str = Field(..., alias="endDate", description="The forecast end date in YYYY-MM-DD format.")
    frequency_cap: Optional["FrequencyCapV1"] = Field(None, alias="frequencyCap")
    performance_metric: "PerformanceMetricV1" = Field(..., alias="performanceMetric")
    reach_type: "ReachTypeV1" = Field(..., alias="reachType")
    start_date: str = Field(..., alias="startDate", description="The forecast start date in YYYY-MM-DD format.")
    supply_package: Optional[list["SupplyV1"]] = Field(None, alias="supplyPackage", description="The combination of Ads supply.")
    targets: Optional[list["PlanningTargetV1"]] = None

    model_config = {'populate_by_name': True}


class GeneratePerformanceForecastsV1RequestContent(BaseModel):
    performance_forecasts: list["GeneratePerformanceForecastsV1RequestElement"] = Field(..., alias="performanceForecasts")

    model_config = {'populate_by_name': True}


class GeneratePerformanceForecastsV1ResponseError(BaseModel):
    error: "ReachPlanningServiceError"
    index: int = Field(..., description="This is the index of the corresponding request element in the request payload.")

    model_config = {'populate_by_name': True}


class GeneratePerformanceForecastsV1ResponseSuccess(BaseModel):
    index: int = Field(..., description="This is the index of the corresponding request element in the request payload.")
    performance_forecast: "GeneratePerformanceForecastV1ResponseElement" = Field(..., alias="performanceForecast")

    model_config = {'populate_by_name': True}


class GeneratePerformanceForecastsV1ResponseContent(BaseModel):
    error: list["GeneratePerformanceForecastsV1ResponseError"]
    success: list["GeneratePerformanceForecastsV1ResponseSuccess"] = Field(..., description="List of performance curves for each requested performance metric.")

    model_config = {'populate_by_name': True}


class InternalServerErrorExceptionResponseContent(BaseModel):
    """Internal Server Error."""
    code: Optional["ErrorCode"] = None
    message: Optional[str] = Field(None, description="Human readable response message.")

    model_config = {'populate_by_name': True}


class ListReachForecastTargetsV1RequestContent(BaseModel):
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value for navigating to the next response page.")
    reach_forecast_id: str = Field(..., alias="reachForecastId", description="This is the unique identifier of the Reach Forecast resource.")

    model_config = {'populate_by_name': True}


class ListReachForecastTargetsV1ResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value for navigating to the next response page.")
    targets: list["PlanningTargetV1"]

    model_config = {'populate_by_name': True}


class ListReachForecastsV1RequestContent(BaseModel):
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value for navigating to the next response page.")
    reach_forecast_ids: list[str] = Field(..., alias="reachForecastIds", description="The IDs of Reach Forecasts to be retrived.")

    model_config = {'populate_by_name': True}


class ListReachForecastsV1ResponseElement(BaseModel):
    advertised_product_category_ids: Optional[list[str]] = Field(None, alias="advertisedProductCategoryIds", description="The identifiers of the advertised product categories for the forecast. Use the DSP [ListAdvertisedProductCategories API]")
    available_impressions: Optional[int] = Field(None, alias="availableImpressions", description="The number of impressions available for you to purchase after considering contention (G - booked demand) among the match")
    avg_cpm: Optional[float] = Field(None, alias="avgCpm", description="The CPM rate (cost per thousand impressions).")
    country_code: "CountryCodeV1" = Field(..., alias="countryCode")
    cpc: Optional[float] = Field(None, description="The CPC rate (cost per click).")
    creation_date_time: str = Field(..., alias="creationDateTime", description="The date time that the reach forecast was created.")
    currency_code: "CurrencyCodeV1" = Field(..., alias="currencyCode")
    data_points: list["ReachCurveDataPointV1"] = Field(..., alias="dataPoints", description="The list of data points for the reach curve.")
    delivery_type: "DeliveryTypeV1" = Field(..., alias="deliveryType")
    end_date: str = Field(..., alias="endDate", description="The forecast end date in YYYY-MM-DD format.")
    frequency_cap: Optional["FrequencyCapV1"] = Field(None, alias="frequencyCap")
    matching_impressions: Optional[int] = Field(None, alias="matchingImpressions", description="The number of impressions that match your targeting")
    max_cpm: Optional[float] = Field(None, alias="maxCpm", description="The maximum CPM rate (cost per thousand impressions).")
    reach_forecast_id: str = Field(..., alias="reachForecastId", description="This is the unique identifier of the Reach Forecast resource.")
    reach_type: "ReachTypeV1" = Field(..., alias="reachType")
    start_date: str = Field(..., alias="startDate", description="The forecast start date in YYYY-MM-DD format.")
    status: "ReachForecastStatusV1"
    supply_package: Optional[list["SupplyV1"]] = Field(None, alias="supplyPackage", description="The combination of Ads supply.")

    model_config = {'populate_by_name': True}


class ListReachForecastsV1ResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value for navigating to the next response page.")
    reach_forecasts: list["ListReachForecastsV1ResponseElement"] = Field(..., alias="reachForecasts")

    model_config = {'populate_by_name': True}


class NotFoundExceptionResponseContent(BaseModel):
    """Not Found."""
    code: Optional["ErrorCode"] = None
    message: Optional[str] = Field(None, description="Human readable response message.")

    model_config = {'populate_by_name': True}


class ServerTimeoutExceptionResponseContent(BaseModel):
    """Server Timeout."""
    code: Optional["ErrorCode"] = None
    message: Optional[str] = Field(None, description="Human readable response message.")

    model_config = {'populate_by_name': True}


class TooManyRequestsExceptionResponseContent(BaseModel):
    """Too Many Requests."""
    code: Optional["ErrorCode"] = None
    message: Optional[str] = Field(None, description="Human readable response message.")

    model_config = {'populate_by_name': True}


class UnauthorizedExceptionResponseContent(BaseModel):
    """Unauthorized."""
    code: Optional["ErrorCode"] = None
    message: Optional[str] = Field(None, description="Human readable response message.")

    model_config = {'populate_by_name': True}

