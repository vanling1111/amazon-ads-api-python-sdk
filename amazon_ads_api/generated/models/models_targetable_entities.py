"""Auto-generated Pydantic models. Do not edit manually.

Source: TargetableEntities_prod_3p.json
Title:  Targetable Entities
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class AccessDeniedErrorCode(StrEnum):
    ACCESS_DENIED = "ACCESS_DENIED"


class AccessDeniedExceptionResponseContent(BaseModel):
    code: "AccessDeniedErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class AdProduct(StrEnum):
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"
    SPONSORED_TELEVISION = "SPONSORED_TELEVISION"


class InternalErrorErrorCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class InternalServerExceptionResponseContent(BaseModel):
    code: "InternalErrorErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class InvalidArgumentErrorCode(StrEnum):
    INVALID_ARGUMENT = "INVALID_ARGUMENT"


class InvalidArgumentExceptionResponseContent(BaseModel):
    code: "InvalidArgumentErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class Locale(StrEnum):
    AR_AE = "ar_AE"
    DE_DE = "de_DE"
    EN_AE = "en_AE"
    EN_AU = "en_AU"
    EN_CA = "en_CA"
    EN_GB = "en_GB"
    EN_IN = "en_IN"
    EN_SG = "en_SG"
    EN_US = "en_US"
    EN_ZA = "en_ZA"
    ES_ES = "es_ES"
    ES_MX = "es_MX"
    FR_CA = "fr_CA"
    FR_FR = "fr_FR"
    HI_IN = "hi_IN"
    IT_IT = "it_IT"
    JA_JP = "ja_JP"
    KO_KR = "ko_KR"
    NL_NL = "nl_NL"
    PL_PL = "pl_PL"
    PT_BR = "pt_BR"
    SV_SE = "sv_SE"
    TA_IN = "ta_IN"
    TH_TH = "th_TH"
    TR_TR = "tr_TR"
    VI_VN = "vi_VN"
    ZH_CN = "zh_CN"


class TargetType(StrEnum):
    AUDIENCE = "AUDIENCE"
    CONTENT_CATEGORY = "CONTENT_CATEGORY"
    PRODUCT_CATEGORY = "PRODUCT_CATEGORY"
    PRODUCT_CATEGORY_AUDIENCE = "PRODUCT_CATEGORY_AUDIENCE"


class ListTargetableEntitiesRequestContent(BaseModel):
    ad_product: "AdProduct" = Field(..., alias="adProduct")
    locale: Optional["Locale"] = None
    max_results: Optional[float] = Field(None, alias="maxResults", description="Number of records to include in the paginated response.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    parent_browse_node_id_filter: Optional[list[str]] = Field(None, alias="parentBrowseNodeIdFilter", description="Filter by parent browse node IDs. Returns entities whose parent category matches any of the provided IDs.")
    paths_filter: Optional[list[list[str]]] = Field(None, alias="pathsFilter", description="Get direct descendant sub paths that fall under the paths specified in the field value. The value is a list of paths, wh")
    product_category_id_filter: Optional[list[str]] = Field(None, alias="productCategoryIdFilter", description="Filter by product category IDs (browse node IDs). Returns entities matching any of the provided IDs.")
    search_query_filter: Optional[str] = Field(None, alias="searchQueryFilter", description="The query string used to filter targetable entities. Search for terms or phrases that are relevant to your advertising g")
    target_type_filter: Optional[list["TargetType"]] = Field(None, alias="targetTypeFilter", description="A list of targeting types. If an empty list is provided, it is equivalent to passing all targeting types.")

    model_config = {'populate_by_name': True}


class TargetableEntity(BaseModel):
    """A targetable entity."""
    audience_id: Optional[str] = Field(None, alias="audienceId", description="The identifier for a target of type AUDIENCE.")
    audience_resolved: Optional[str] = Field(None, alias="audienceResolved", description="The resolved name of audienceId.")
    audience_tooltip: Optional[str] = Field(None, alias="audienceTooltip", description="The tooltip description to describe the amazon audience targetable entity.")
    child_count: Optional[float] = Field(None, alias="childCount", description="The number of direct child categories.")
    content_category_id: Optional[str] = Field(None, alias="contentCategoryId", description="The identifier for a target of type CONTENT_CATEGORY.")
    content_category_resolved: Optional[str] = Field(None, alias="contentCategoryResolved", description="The resolved name of contentCategoryId.")
    parent_browse_node_id: Optional[str] = Field(None, alias="parentBrowseNodeId", description="The browse node ID of the parent category.")
    path: list[str] = Field(..., description="The location of the targetable entity in Amazon's taxonomy.")
    path_node_ids: Optional[list[str]] = Field(None, alias="pathNodeIds", description="The browse node IDs for each segment in the path hierarchy.")
    product_category_id: Optional[str] = Field(None, alias="productCategoryId", description="The identifier for a target of either type PRODUCT_CATEGORY or PRODUCT_CATEGORY_AUDIENCE.")
    product_category_resolved: Optional[str] = Field(None, alias="productCategoryResolved", description="The resolved name of productCategoryId.")
    target_type: "TargetType" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class ListTargetableEntitiesResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    targetable_entities: Optional[list["TargetableEntity"]] = Field(None, alias="targetableEntities", description="The list of targetable entities.")
    total_results: Optional[float] = Field(None, alias="totalResults", description="The total number of entities.")

    model_config = {'populate_by_name': True}


class ListTargetableEntityPathsRequestContent(BaseModel):
    ad_product: "AdProduct" = Field(..., alias="adProduct")
    locale: Optional["Locale"] = None
    paths_filter: Optional[list[list[str]]] = Field(None, alias="pathsFilter", description="Get direct descendant sub paths that fall under the paths specified in the field value. The value is a list of paths, wh")

    model_config = {'populate_by_name': True}


class ListTargetableEntityPathsResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    paths: Optional[list[list[str]]] = Field(None, description="The direct descendants of the paths specified in the request's pathsFilter field.")
    total_results: Optional[float] = Field(None, alias="totalResults", description="The total number of entities.")

    model_config = {'populate_by_name': True}


class TextInputSearchRequestContent(BaseModel):
    ad_product: "AdProduct" = Field(..., alias="adProduct")
    locale: Optional["Locale"] = None
    max_results: Optional[float] = Field(None, alias="maxResults", description="Number of records to include in the paginated response.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    parent_browse_node_id_filter: Optional[list[str]] = Field(None, alias="parentBrowseNodeIdFilter", description="Filter by parent browse node IDs. Returns entities whose parent category matches any of the provided IDs.")
    paths_filter: Optional[list[list[str]]] = Field(None, alias="pathsFilter", description="Get direct descendant sub paths that fall under the paths specified in the field value. The value is a list of paths, wh")
    product_category_id_filter: Optional[list[str]] = Field(None, alias="productCategoryIdFilter", description="Filter by product category IDs (browse node IDs). Returns entities matching any of the provided IDs.")
    search_query_filter: Optional[str] = Field(None, alias="searchQueryFilter", description="The query string used to filter targetable entities. Search for terms or phrases that are relevant to your advertising g")
    target_type_filter: Optional[list["TargetType"]] = Field(None, alias="targetTypeFilter", description="A list of targeting types. If an empty list is provided, it is equivalent to passing all targeting types.")

    model_config = {'populate_by_name': True}


class TextInputSearchResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    targetable_entities: Optional[list["TargetableEntity"]] = Field(None, alias="targetableEntities", description="The list of targetable entities.")
    total_results: Optional[float] = Field(None, alias="totalResults", description="The total number of entities.")

    model_config = {'populate_by_name': True}


class ThrottledErrorCode(StrEnum):
    THROTTLED = "THROTTLED"


class ThrottlingExceptionResponseContent(BaseModel):
    code: "ThrottledErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class UnauthorizedErrorCode(StrEnum):
    UNAUTHORIZED = "UNAUTHORIZED"


class UnauthorizedExceptionResponseContent(BaseModel):
    code: "UnauthorizedErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}

