"""Auto-generated Pydantic models. Do not edit manually.

Source: AmazonAttribution_prod_3p.json
Title:  Amazon Attribution
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class advertiser(BaseModel):
    advertiser_id: Optional[str] = Field(None, alias="advertiserId")
    advertiser_name: Optional[str] = Field(None, alias="advertiserName")

    model_config = {'populate_by_name': True}


class AdvertiserResponse(BaseModel):
    advertisers: Optional[list["advertiser"]] = None

    model_config = {'populate_by_name': True}


class attributionTagMap(BaseModel):
    """An object representing the association between a publisher identifier and an attribution tag."""
    __root__: dict[str, str] = {}


class AttributionTagResponse(BaseModel):
    advertiser_attribution_tag_map: Optional[dict[str, "attributionTagMap"]] = Field(None, alias="advertiserAttributionTagMap", description="A list of advertisers and associated attribution tags.")

    model_config = {'populate_by_name': True}


class MaaSError(BaseModel):
    """The error response object."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response. Possible value of code is '200', '207', '400', '401', '429', '403', or '500'.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class Publisher(BaseModel):
    id_: Optional[dict[str, Any]] = Field(None, alias="id", description="The identifier of a publisher.")
    macro_enabled: Optional[bool] = Field(None, alias="macroEnabled", description="Set to 'true' if Amazon Attribution provides macro tags for the given publisher.")
    name: Optional[str] = Field(None, description="The name of the publisher.")

    model_config = {'populate_by_name': True}


class PublishersResponse(BaseModel):
    publisher: Optional[list["Publisher"]] = Field(None, description="A list of publishers.")

    model_config = {'populate_by_name': True}


class ReportEntry(BaseModel):
    """Report entry object in GetReport reports list."""
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="An ad group external identifier. Applies to `PERFORMANCE` and `PRODUCTS` reportType.")
    advertiser_name: Optional[str] = Field(None, alias="advertiserName", description="Name of advertiser. Applies to `PERFORMANCE` and `PRODUCTS` reportType.")
    brand_name: Optional[str] = Field(None, alias="brandName", description="Name of the advertiser's brand. Applies only to `PRODUCTS` reportType.")
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="A campaign external identifier. Applies to `PERFORMANCE` and `PRODUCTS` reportType.")
    creative_id: Optional[str] = Field(None, alias="creativeId", description="A creative external identifier. Applies only to `PERFORMANCE` reportType")
    date: Optional[str] = Field(None, description="Date on which the events took place. Applies to `PERFORMANCE` and `PRODUCTS` reportType.")
    marketplace: Optional[str] = Field(None, description="The Amazon-owned site the product is sold on. Applies only to `PRODUCTS` reportType.")
    product_asin: Optional[str] = Field(None, alias="productAsin", description="A unique block of letters and/or numbers that identify all products sold on Amazon. Applies only to `PRODUCTS` reportTyp")
    product_category: Optional[str] = Field(None, alias="productCategory", description="A classification for the type of product being sold which determines its place in the Amazon retail catalog. Contains ca")
    product_conversion_type: Optional[str] = Field(None, alias="productConversionType", description="The conversion type describes whether the conversion happened on a promoted or a brand halo ASIN. Applies only to `PRODU")
    product_group: Optional[str] = Field(None, alias="productGroup", description="A distinct product grouping distinguishing products like watches from video games from toys. Contains groups of products")
    product_name: Optional[str] = Field(None, alias="productName", description="The name of the product. Applies only to `PRODUCTS` reportType.")
    product_subcategory: Optional[str] = Field(None, alias="productSubcategory", description="A classification for the type of product being sold which determines its place in the Amazon retail catalog. Contains su")
    publisher: Optional[str] = Field(None, description="The publisher name. Applies to `PERFORMANCE` and `PRODUCTS` reportType")

    model_config = {'populate_by_name': True}


class ReportRequestBodyGroupby(StrEnum):
    ADGROUP = "ADGROUP"
    CAMPAIGN = "CAMPAIGN"
    CREATIVE = "CREATIVE"


class ReportRequestBody(BaseModel):
    """Report request body.  Two types of reports are available: Performance or Products - choose by including the `reportType` property. Performance report may be aggregated at any of three levels: campaign"""
    advertiser_ids: Optional[str] = Field(None, alias="advertiserIds", description="One or more advertiser Ids to filter reporting by. If requesting reporting for multiple advertiser Ids, input via a comm")
    count: Optional[int] = Field(None, description="The number of entries to include in the report.")
    cursor_id: Optional[str] = Field(None, alias="cursorId", description="The value of `cursorId` must be set to `null` without `''`, or set to `''` for the first request. For each following req")
    end_date: Optional[str] = Field(None, alias="endDate", description="The end date for the report, form as 'YYYYMMDD'")
    group_by: Optional[ReportRequestBodyGroupby] = Field(None, alias="groupBy", description="For Performance report only - controls level of aggregation. Value can be `CAMPAIGN`, `ADGROUP`, or `CREATIVE`. Default ")
    metrics: Optional[str] = Field(None, description="A comma-delimited list of metrics to include in the report. In the report, each metric’s value reflects the events which")
    report_type: Optional[str] = Field(None, alias="reportType", description="The type of report. Either `PERFORMANCE` or `PRODUCTS`. It is an optional parameter. If not used in request body, defaul")
    start_date: Optional[str] = Field(None, alias="startDate", description="The start date for the report, in 'YYYYMMDD' format. For reportType `PRODUCTS`, startDate can only be within last 90 day")

    model_config = {'populate_by_name': True}


class ReportResponse(BaseModel):
    cursor_id: Optional[str] = Field(None, alias="cursorId", description="The identifier of the pagination cursor.")
    reports: Optional[list["ReportEntry"]] = None
    size: Optional[int] = Field(None, description="The size of the report.")

    model_config = {'populate_by_name': True}

