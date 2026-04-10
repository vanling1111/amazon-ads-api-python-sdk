"""Auto-generated Pydantic models. Do not edit manually.

Source: SponsoredBrandsCategoryBenchmark_prod_3p.json
Title:  Sponsored Brands Category Benchmark
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class acosMetric(BaseModel):
    """Advertising cost of sales (ACOS) is the percentage of sales spent on advertising (total spend / total sales). A lower ACOS infers higher efficiency of your advertising investment relative to your adve"""
    bottom_25pct: Optional[float] = Field(None, alias="bottom-25pct", description="The value at which 25% of the lower-performing values lie below. For ACOS, since lower ACOS indicates higher performance")
    median: Optional[float] = Field(None, description="The middle value of the data set. Half of the values lie below the median and half lie above the median. It is also know")
    top_25pct: Optional[float] = Field(None, alias="top-25pct", description="The value at which 25% of the top performing values lie above. For ACOS, since lower ACOS indicates higher performance, ")
    value: Optional[float] = Field(None, description="ACOS of your ad")

    model_config = {'populate_by_name': True}


class brandListResponseBrands(BaseModel):
    name: Optional[str] = None

    model_config = {'populate_by_name': True}


class brandListResponse(BaseModel):
    """A list of brands advertiser has access to"""
    brands: Optional[list["brandListResponseBrands"]] = None
    next_page_token: Optional[str] = Field(None, alias="nextPageToken")

    model_config = {'populate_by_name': True}


class impressionMetric(BaseModel):
    """An impression occurs whenever an ad is displayed. The impressions metric is a count of how many times your ad has been served to a user. A higher impression value infers more users are seeing your ads"""
    bottom_25pct: Optional[float] = Field(None, alias="bottom-25pct", description="The value at which 25% of the lower-performing values lie below. For impressions, 25% of peer values will be below the b")
    median: Optional[float] = Field(None, description="The middle value of the data set. Half of the values lie below the median and half lie above the median. It is also know")
    top_25pct: Optional[float] = Field(None, alias="top-25pct", description="The value at which 25% of the top performing values lie above. For impressions, 25% of values will be above the top 25% ")
    value: Optional[float] = Field(None, description="Number of impressions of your ad")

    model_config = {'populate_by_name': True}


class roasMetric(BaseModel):
    """Return on advertising spend (ROAS) divides the total sales by the total ad spend (total ad sales / total ad spend). A higher ROAS infers higher efficiency of your advertising investment relative to yo"""
    bottom_25pct: Optional[float] = Field(None, alias="bottom-25pct", description="The value at which 25% of the lower-performing values lie below. For ROAS, 25% of peer values will be below the bottom 2")
    median: Optional[float] = Field(None, description="The middle value of the data set. Half of the values lie below the median and half lie above the median. It is also know")
    top_25pct: Optional[float] = Field(None, alias="top-25pct", description="The value at which 25% of the top performing values lie above. For ROAS, 25% of values will be above the top 25% value. ")
    value: Optional[float] = Field(None, description="ROAS of your ad")

    model_config = {'populate_by_name': True}


class ctrMetric(BaseModel):
    """Click Through Rate (CTR): The percentage of shoppers who see your ad and also click it, calculated as clicks divided by impressions (clicks / impressions). A higher CTR infers more users are intereste"""
    bottom_25pct: Optional[float] = Field(None, alias="bottom-25pct", description="The value at which 25% of the lower-performing values lie below. For CTR, 25% of peer values will be below the bottom 25")
    median: Optional[float] = Field(None, description="The middle value of the data set. Half of the values lie below the median and half lie above the median. It is also know")
    top_25pct: Optional[float] = Field(None, alias="top-25pct", description="The value at which 25% of the top performing values lie above. For CTR, 25% of values will be above the top 25% value. I")
    value: Optional[float] = Field(None, description="CTR of your ad")

    model_config = {'populate_by_name': True}


class brandsAndCategoriesItem(BaseModel):
    """Each item contains the metrics for a single brand-category combination"""
    acos: Optional["acosMetric"] = None
    brand_name: Optional[str] = Field(None, alias="brandName")
    category_id: Optional[str] = Field(None, alias="categoryId", description="This is the same as browse node ID")
    category_name: Optional[str] = Field(None, alias="categoryName")
    ctr: Optional["ctrMetric"] = None
    end_date: Optional[str] = Field(None, alias="endDate")
    impressions: Optional["impressionMetric"] = None
    roas: Optional["roasMetric"] = None
    start_date: Optional[str] = Field(None, alias="startDate")

    model_config = {'populate_by_name': True}


class endDateParam(BaseModel):
    """End of the data range (inclusive) in YYYY-MM-DD format (all <a href='https://en.wikipedia.org/wiki/ISO_8601#Dates'>ISO_8601</a> date formats are also supported). The date will be in the Coordinated Un"""
    pass


class errorResponse(BaseModel):
    """Response of an error which contains a message"""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class granularityParam(StrEnum):
    DAY = "DAY"
    MONTH = "MONTH"
    WEEK = "WEEK"


class metricsParam(BaseModel):
    """Metrics to be included in the response."""
    pass


class nextPageTokenParam(BaseModel):
    """Pagination token."""
    pass


class programTypeParam(StrEnum):
    SB = "SB"


class reportResponse(BaseModel):
    """Response model of an entire benchmark report"""
    brands_and_categories: Optional[list["brandsAndCategoriesItem"]] = Field(None, alias="brandsAndCategories")
    next_page_token: Optional[str] = Field(None, alias="nextPageToken")

    model_config = {'populate_by_name': True}


class startDateParam(BaseModel):
    """Beginning of the data range (inclusive) in YYYY-MM-DD format (all <a href='https://en.wikipedia.org/wiki/ISO_8601#Dates'>ISO_8601</a> date formats are also supported). The startDate cannot be earlier """
    pass


class timeSeriesItem(BaseModel):
    """An item in the time series array which represents the data for a single point"""
    acos: Optional["acosMetric"] = None
    ctr: Optional["ctrMetric"] = None
    end_date: Optional[str] = Field(None, alias="endDate")
    impressions: Optional["impressionMetric"] = None
    roas: Optional["roasMetric"] = None
    start_date: Optional[str] = Field(None, alias="startDate")

    model_config = {'populate_by_name': True}


class timeSeriesResponse(BaseModel):
    """Response model of time series data"""
    category: Optional[str] = None
    next_page_token: Optional[str] = Field(None, alias="nextPageToken")
    time_series: Optional[list["timeSeriesItem"]] = Field(None, alias="timeSeries")

    model_config = {'populate_by_name': True}


class windowParam(StrEnum):
    DAY = "DAY"
    MONTH = "MONTH"
    WEEK = "WEEK"

