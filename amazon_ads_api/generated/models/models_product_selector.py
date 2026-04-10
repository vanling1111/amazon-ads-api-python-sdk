"""Auto-generated Pydantic models. Do not edit manually.

Source: ProductSelector_prod_3p.json
Title:  Product Selector
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class priceToPay(BaseModel):
    """The price customer would pay for the buying option"""
    amount: Optional[float] = Field(None, description="Price amount")
    currency: Optional[str] = Field(None, description="Currency of the price")

    model_config = {'populate_by_name': True}


class basisPrice(BaseModel):
    """The basis price before the savings are calculated"""
    amount: Optional[float] = Field(None, description="Price amount")
    currency: Optional[str] = Field(None, description="Currency of the price")

    model_config = {'populate_by_name': True}


class ProductMetadataModelGlobalstoresetting(BaseModel):
    """This denotes the fields related to [GlobalStore Program](https://sellercentral.amazon.com/help/hub/reference/external/202139180)."""
    catalog_source_country_code: Optional[str] = Field(None, alias="catalogSourceCountryCode", description="Country code of source marketplace where seller has listed the product. Possible source country codes include US, UK, DE")

    model_config = {'populate_by_name': True}


class ProductMetadataModel(BaseModel):
    asin: Optional[str] = Field(None, description="ASIN of the item")
    availability: Optional[str] = Field(None, description="Stock availability:   * IN_STOCK - The item is in stock.   * IN_STOCK_SCARCE - The item is in stock, but stock levels ar")
    basis_price: Optional["basisPrice"] = Field(None, alias="basisPrice")
    best_seller_rank: Optional[str] = Field(None, alias="bestSellerRank", description="Best seller rank position in the category")
    brand: Optional[str] = Field(None, description="Brand name of the item")
    category: Optional[str] = Field(None, description="Category (browse node) name of the ASIN")
    created_date: Optional[str] = Field(None, alias="createdDate", description="Date the item was first available on Amazon")
    eligibility_status: Optional[str] = Field(None, alias="eligibilityStatus", description="Eligibility status for advertising:   * ELIGIBLE - Eligible for advertising   * INELIGIBLE - Ineligible for advertising")
    global_store_setting: Optional["ProductMetadataModelGlobalstoresetting"] = Field(None, alias="globalStoreSetting", description="This denotes the fields related to [GlobalStore Program](https://sellercentral.amazon.com/help/hub/reference/external/20")
    image_url: Optional[str] = Field(None, alias="imageUrl", description="Url to the product image")
    ineligibility_codes: Optional[list[str]] = Field(None, alias="ineligibilityCodes", description="List of ineligible status identifier")
    ineligibility_reasons: Optional[list[str]] = Field(None, alias="ineligibilityReasons", description="List of reasons that made this item ineligible to be advertised")
    price_to_pay: Optional["priceToPay"] = Field(None, alias="priceToPay")
    sku: Optional[str] = Field(None, description="sku of the item")
    title: Optional[str] = Field(None, description="Product title of the item")
    variation_list: Optional[list[str]] = Field(None, alias="variationList", description="List of ASIN variations of the current item")

    model_config = {'populate_by_name': True}


class ProductMetadataRequestAdtype(StrEnum):
    SB = "SB"
    SD = "SD"
    SP = "SP"


class ProductMetadataRequestSortby(StrEnum):
    CREATED_DATE = "CREATED_DATE"
    SUGGESTED = "SUGGESTED"


class ProductMetadataRequestSortorder(StrEnum):
    ASC = "ASC"
    DESC = "DESC"


class ProductMetadataRequest(BaseModel):
    ad_type: Optional[ProductMetadataRequestAdtype] = Field(None, alias="adType", description="Program type. Required if checks advertising eligibility:   * SP - Sponsored Product   * SB - Sponsored Brand   * SD - S")
    asins: Optional[list[str]] = Field(None, description="Specific asins to search for in the advertiser's inventory. Cannot use together with skus or searchStr input types.")
    check_eligibility: Optional[bool] = Field(None, alias="checkEligibility", description="Whether advertising eligibility info is required")
    check_item_details: Optional[bool] = Field(None, alias="checkItemDetails", description="Whether item details such as name, image, and price is required.")
    cursor_token: Optional[str] = Field(None, alias="cursorToken", description="Pagination token used for the suggested sort type or for author merchant")
    is_global_store_selection: Optional[bool] = Field(None, alias="isGlobalStoreSelection", description="This will return only GlobalStore listings related to [GlobalStore Program](https://sellercentral.amazon.com/help/hub/re")
    locale: Optional[str] = Field(None, description="Optional locale for detail and eligibility response strings. Default to the marketplace locale.")
    page_index: int = Field(..., alias="pageIndex", description="Index of the page to be returned; For author, this value will be ignored, should use cursorToken instead. For seller and")
    page_size: int = Field(..., alias="pageSize", description="Number of items to be returned on this page index.")
    search_str: Optional[str] = Field(None, alias="searchStr", description="Specific string in the item title to search for in the advertiser's inventory. Case insensitive. Cannot use together wit")
    skus: Optional[list[str]] = Field(None, description="Specific SKUs to search for in the advertiser's inventory. Currently only support SP program type for sellers. Cannot us")
    sort_by: Optional[ProductMetadataRequestSortby] = Field(None, alias="sortBy", description="Sort option for the result. Currently only support SP program type for sellers:   * SUGGESTED - Suggested products are t")
    sort_order: Optional[ProductMetadataRequestSortorder] = Field(None, alias="sortOrder", description="Sort order (has to be DESC for the suggested sort type):   * ASC - Ascending, from A to Z   * DESC - Descending, from Z ")

    model_config = {'populate_by_name': True}


class ProductMetadataResponse(BaseModel):
    product_metadata_list: Optional[list["ProductMetadataModel"]] = Field(None, alias="ProductMetadataList")
    cursor_token: Optional[str] = Field(None, alias="cursorToken", description="Pagination token for later requests with specific sort type to use as the page index instead. Empty cursorToken means no")

    model_config = {'populate_by_name': True}


class error(BaseModel):
    """Error response object."""
    code: Optional[str] = Field(None, description="Enumerated error type.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}

