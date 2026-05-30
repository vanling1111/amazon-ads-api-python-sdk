"""Auto-generated Pydantic models. Do not edit manually.

Source: Stores_prod_3p.json
Title:  Stores
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class AsinEngagementDetail(BaseModel):
    """A key-value pair map which contains the dimension and metric information. The key is either dimension name or metric name, while the value is the corresponding dimension value or metric value."""
    __root__: dict[str, Union[str, int, float]] = {}


class AsinEngagementDimension(StrEnum):
    ASIN = "ASIN"


class AsinEngagementMetric(StrEnum):
    ADD_TO_CARTS = "ADD_TO_CARTS"
    AVERAGE_IN_STOCK_PRICE = "AVERAGE_IN_STOCK_PRICE"
    AVERAGE_SALE_PRICE = "AVERAGE_SALE_PRICE"
    CLICKS = "CLICKS"
    CLICK_RATE = "CLICK_RATE"
    CONVERSION_RATE = "CONVERSION_RATE"
    IN_STOCK_RATE = "IN_STOCK_RATE"
    IN_STOCK_VIEWS = "IN_STOCK_VIEWS"
    ORDERS = "ORDERS"
    RENDERS = "RENDERS"
    TOTAL_CLICKS = "TOTAL_CLICKS"
    TOTAL_VIEWS = "TOTAL_VIEWS"
    UNITS = "UNITS"
    VIEWS = "VIEWS"


class SortOrder(StrEnum):
    ASC = "ASC"
    DESC = "DESC"


class GetAsinEngagementForStoreRequest(BaseModel):
    dimension: Optional["AsinEngagementDimension"] = None
    end_date: str = Field(..., alias="endDate", description="The end date (inclusive) in YYYY-MM-DD format for the time period from when to fetch the insights.")
    metrics: list["AsinEngagementMetric"] = Field(..., description="List of the engagement metrics to be fetched. At least one metric should be specified.")
    order_by: Optional["SortOrder"] = Field(None, alias="orderBy")
    sort_by: Optional[Any] = Field(None, alias="sortBy", description="Nullable metric to sort on. If a value is provided, it must also appear in the metrics list. If no value is provided, th")
    start_date: str = Field(..., alias="startDate", description="The start date (inclusive) in YYYY-MM-DD format for the time period from when to fetch the insights.")

    model_config = {'populate_by_name': True}


class GetAsinEngagementForStoreResponse(BaseModel):
    dimension: Optional["AsinEngagementDimension"] = None
    metrics_details: Optional[list["AsinEngagementDetail"]] = Field(None, alias="metricsDetails")

    model_config = {'populate_by_name': True}


class InsightMetric(StrEnum):
    ACTIONS_TAKEN_BY_PEERS = "ACTIONS_TAKEN_BY_PEERS"
    BOUNCE_RATE = "BOUNCE_RATE"
    COMPLETED_RECOMMENDATIONS = "COMPLETED_RECOMMENDATIONS"
    CONTRIBUTORS = "CONTRIBUTORS"
    DWELL = "DWELL"
    DWELL_TIME = "DWELL_TIME"
    NEW_TO_STORE = "NEW_TO_STORE"
    ORDERS = "ORDERS"
    PEER_DWELL = "PEER_DWELL"
    PEER_SALES_LAST_60_DAYS = "PEER_SALES_LAST_60_DAYS"
    RECOMMENDATIONS = "RECOMMENDATIONS"
    SALES = "SALES"
    SALES_LAST_60_DAYS = "SALES_LAST_60_DAYS"
    SCORE_LEVEL = "SCORE_LEVEL"
    UNITS = "UNITS"
    VIDEO_10S_PLAYED = "VIDEO_10S_PLAYED"
    VIDEO_25P_PLAYED = "VIDEO_25P_PLAYED"
    VIDEO_50P_PLAYED = "VIDEO_50P_PLAYED"
    VIDEO_75P_PLAYED = "VIDEO_75P_PLAYED"
    VIDEO_COMPLETED = "VIDEO_COMPLETED"
    VIDEO_STARTED = "VIDEO_STARTED"
    VIEWS = "VIEWS"
    VISITORS = "VISITORS"
    VISITS = "VISITS"


class TrafficSource(StrEnum):
    ADS = "ADS"
    ORGANIC = "ORGANIC"
    OTHER = "OTHER"


class InsightFilter(BaseModel):
    """The filter to restrict the return data. Users can specifiy the pages/source/tags they feel interested in for the insights. The relationship between each field is 'AND'. E.g. The user can speficy {page"""
    page_ids: Optional[list[str]] = Field(None, alias="pageIds", description="List of pages to be fetched for insight metrics. Users can first make request to the API with the same parameters but wi")
    sources: Optional[list["TrafficSource"]] = Field(None, description="List of sources to be fetched for insight metrics.")
    tags: Optional[list[str]] = Field(None, description="List of tags to be fetched for insight metrics. Users can first make request to the API with the same parameters but wit")

    model_config = {'populate_by_name': True}


class InsightDimension(StrEnum):
    DATE = "DATE"
    PAGE = "PAGE"
    SOURCE = "SOURCE"
    STORE = "STORE"
    TAG = "TAG"


class GetInsightsForStoreRequest(BaseModel):
    dimension: "InsightDimension"
    end_date: str = Field(..., alias="endDate", description="The end date (inclusive) in YYYY-MM-DD format for the time period from when to fetch the insights.")
    filter_: Optional["InsightFilter"] = Field(None, alias="filter")
    language: Optional[str] = Field(None, description="This parameter is only available for Insights Metrics request for Store Quality(SQS). The language parameter is to reque")
    max_result: Optional[int] = Field(None, alias="maxResult", description="The max number of result that will be returned in one response. The max allowed value will be 1500. If the parameter is ")
    metrics: list["InsightMetric"] = Field(..., description="List of the insight metrics to be fetched. Only one metric should be specified.")
    pagination_token: Optional[str] = Field(None, alias="paginationToken", description="The token that last request returned. It will be used to fetch next page of response.")
    start_date: str = Field(..., alias="startDate", description="The start date (inclusive) in YYYY-MM-DD format for the time period from when to fetch the insights. The earliest date w")

    model_config = {'populate_by_name': True}


class StoreQualityCompletedRecommendation(BaseModel):
    """The Object containing recommendations to improve store quality."""
    category: Optional[str] = Field(None, description="The category in which the store owners could see improvment by this recommendation.")
    example_link: Optional[str] = Field(None, alias="exampleLink", description="Link to the example store with a sample to showcase a recommended action.")
    example_text: Optional[str] = Field(None, alias="exampleText", description="The text to describe the example to showcase the recommended action.")
    observed_average_dwell_time_increase: Optional[str] = Field(None, alias="observedAverageDwellTimeIncrease", description="The percentage by which store quality could improve by this recommendation.")
    recommended_action: Optional[str] = Field(None, alias="recommendedAction", description="description of the recommendation.")

    model_config = {'populate_by_name': True}


class StoreQualityRecommendation(BaseModel):
    """The Object containing recommendations to improve store quality."""
    category: Optional[str] = Field(None, description="The category in which the store owners could see improvment by this recommendation.")
    cta_link: Optional[str] = Field(None, alias="ctaLink", description="Call to Action(CTA) link to take customer to the page where the changes can be made.")
    cta_text: Optional[str] = Field(None, alias="ctaText", description="Text describing the Call to Action(CTA).")
    example_link: Optional[str] = Field(None, alias="exampleLink", description="Link to the example store with a sample to showcase a recommended action.")
    example_text: Optional[str] = Field(None, alias="exampleText", description="The text to describe the example to showcase the recommended action.")
    observed_averag_sales_increase: Optional[str] = Field(None, alias="observedAveragSalesIncrease", description="The percentage by which store's sales could improve by this recommendation.")
    observed_average_dwell_time_increase: Optional[str] = Field(None, alias="observedAverageDwellTimeIncrease", description="The percentage by which store quality could improve by this recommendation.")
    recommended_action: Optional[str] = Field(None, alias="recommendedAction", description="description of the recommendation.")

    model_config = {'populate_by_name': True}


class InsightMetricsDetail(BaseModel):
    """A key-value pair map which contains the dimension and metric information. The key is either dimension name or metric name, while the value is the corresponding dimension value or metric value. Additio"""
    __root__: dict[str, Union[str, int, float, bool, list[str], list["StoreQualityRecommendation"], list["StoreQualityCompletedRecommendation"]]] = {}


class GetInsightsForStoreResponse(BaseModel):
    dimension: Optional["InsightDimension"] = None
    filter_: Optional["InsightFilter"] = Field(None, alias="filter")
    metrics_details: Optional[list["InsightMetricsDetail"]] = Field(None, alias="metricsDetails")
    pagination_token: Optional[str] = Field(None, alias="paginationToken", description="The token can be directly used to fetch next page of the result. The token can only been used when the token is been cre")

    model_config = {'populate_by_name': True}


class StoresAnalyticsAPIErrorResponse(BaseModel):
    """The error response object for analytics API."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}

