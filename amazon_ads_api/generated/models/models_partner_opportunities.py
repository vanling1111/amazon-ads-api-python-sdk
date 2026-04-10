"""Auto-generated Pydantic models. Do not edit manually.

Source: PartnerOpportunities_prod_3p.json
Title:  Partner Opportunities
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class Locale(StrEnum):
    AR_AE = "ar_AE"
    CS_CZ = "cs_CZ"
    DE_DE = "de_DE"
    EN_AU = "en_AU"
    EN_CA = "en_CA"
    EN_GB = "en_GB"
    EN_IN = "en_IN"
    EN_SG = "en_SG"
    EN_US = "en_US"
    ES_CO = "es_CO"
    ES_ES = "es_ES"
    ES_MX = "es_MX"
    ES_US = "es_US"
    FR_CA = "fr_CA"
    FR_FR = "fr_FR"
    HE_IL = "he_IL"
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
    ZH_TW = "zh_TW"


class PartnerOpportunitiesApplicationMarketplace(StrEnum):
    AE = "AE"
    AU = "AU"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    UK = "UK"
    US = "US"


class PartnerOpportunitiesApplicationStatusStatus(StrEnum):
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    PUBLISHED = "PUBLISHED"
    REJECTED = "REJECTED"
    SUCCESS = "SUCCESS"


class PartnerOpportunitiesApplicationStatus(BaseModel):
    campaign_id: str = Field(..., alias="campaignId")
    recommendation_id: str = Field(..., alias="recommendationId")
    status: PartnerOpportunitiesApplicationStatusStatus

    model_config = {'populate_by_name': True}


class PartnerOpportunitiesApplicationStatusErrorDtoV1Code(StrEnum):
    PO_APPLICATION_STATUS_BAD_REQUEST = "PO_APPLICATION_STATUS_BAD_REQUEST"
    PO_APPLICATION_STATUS_INTERNAL_SERVER_ERROR = "PO_APPLICATION_STATUS_INTERNAL_SERVER_ERROR"


class PartnerOpportunitiesApplicationStatusErrorDtoV1(BaseModel):
    code: PartnerOpportunitiesApplicationStatusErrorDtoV1Code
    message: str

    model_config = {'populate_by_name': True}


class PartnerOpportunitiesApplicationStatusRequestDtoV1Advertisertype(StrEnum):
    SELLER = "SELLER"
    VENDOR = "VENDOR"


class PartnerOpportunitiesApplicationStatusRequestDtoV1(BaseModel):
    advertiser_type: PartnerOpportunitiesApplicationStatusRequestDtoV1Advertisertype = Field(..., alias="advertiserType", description="Entity Type  Provided in opportunity data as 'advertiserType'.")
    encrypted_advertiser_id: str = Field(..., alias="encryptedAdvertiserId", description="The encrypted advertiser ID.  Provided in opportunity data.")
    entity_id: str = Field(..., alias="entityId", description="Entity ID  Provided in opportunity data.")
    marketplace: "PartnerOpportunitiesApplicationMarketplace"
    recommendation_ids: list[str] = Field(..., alias="recommendationIds", description="A list of recommendation IDs for which status will be retrieved.  Provided in opportunity data.")

    model_config = {'populate_by_name': True}


class PartnerOpportunitiesApplicationStatusResponseDtoV1(BaseModel):
    statuses: list["PartnerOpportunitiesApplicationStatus"]

    model_config = {'populate_by_name': True}


class PartnerOpportunitiesApplyErrorFailures(BaseModel):
    code: str
    message: str
    recommendation_id: str = Field(..., alias="recommendationId")

    model_config = {'populate_by_name': True}


class PartnerOpportunitiesApplyErrorSuccesses(BaseModel):
    recommendation_id: str = Field(..., alias="recommendationId")

    model_config = {'populate_by_name': True}


class PartnerOpportunitiesApplyErrorDtoV1Code(StrEnum):
    PO_APPLY_ALREADY_APPLIED = "PO_APPLY_ALREADY_APPLIED"
    PO_APPLY_BAD_REQUEST = "PO_APPLY_BAD_REQUEST"
    PO_APPLY_INTERNAL_SERVER_ERROR = "PO_APPLY_INTERNAL_SERVER_ERROR"
    PO_APPLY_IN_TERMINAL_STATUS = "PO_APPLY_IN_TERMINAL_STATUS"
    PO_APPLY_UNPROCESSABLE_ERROR = "PO_APPLY_UNPROCESSABLE_ERROR"


class PartnerOpportunitiesApplyErrorDtoV1(BaseModel):
    code: PartnerOpportunitiesApplyErrorDtoV1Code
    failures: list["PartnerOpportunitiesApplyErrorFailures"]
    message: str
    successes: list["PartnerOpportunitiesApplyErrorSuccesses"]

    model_config = {'populate_by_name': True}


class PartnerOpportunitiesApplyRequestDtoV1Advertisertype(StrEnum):
    SELLER = "SELLER"
    VENDOR = "VENDOR"


class PartnerOpportunitiesApplyRequestDtoV1(BaseModel):
    advertiser_type: PartnerOpportunitiesApplyRequestDtoV1Advertisertype = Field(..., alias="advertiserType", description="Entity Type  Provided in opportunity data as 'advertiserType'.")
    encrypted_advertiser_id: str = Field(..., alias="encryptedAdvertiserId", description="The encrypted advertiser ID.  Provided in opportunity data.")
    entity_id: str = Field(..., alias="entityId", description="Entity ID  Provided in opportunity data.")
    marketplace: "PartnerOpportunitiesApplicationMarketplace"
    recommendation_ids: list[str] = Field(..., alias="recommendationIds", description="A list of recommendation IDs to apply for the given opportunity.")

    model_config = {'populate_by_name': True}


class PartnerOpportunitiesOpportunityDataMetadataV1(BaseModel):
    row_count: float = Field(..., alias="rowCount", description="Number of rows present in the latest partner opportunity data file.")
    updated_date: str = Field(..., alias="updatedDate", description="Date the opportunity data file was generated/updated, in ISO 8601 format.")

    model_config = {'populate_by_name': True}


class PartnerOpportunitiesOpportunityV1Audience(StrEnum):
    PARTNER = "PARTNER"
    PARTNER_MANAGED_ADVERTISERS = "PARTNER_MANAGED_ADVERTISERS"
    PARTNER_MANAGED_AD_BUSINESS = "PARTNER_MANAGED_AD_BUSINESS"


class PartnerOpportunitiesOpportunityV1Objective(StrEnum):
    AWARENESS = "AWARENESS"
    BRAND_ENGAGEMENT = "BRAND_ENGAGEMENT"
    RETENTION = "RETENTION"
    SALES = "SALES"


class PartnerOpportunitiesOpportunityV1Objectivetype(StrEnum):
    ADVERTISER_INSIGHTS = "ADVERTISER_INSIGHTS"
    AD_API_ENDPOINT_ADOPTION = "AD_API_ENDPOINT_ADOPTION"
    AMAZON_ACCOUNT_TEAM_RECOMMENDATIONS = "AMAZON_ACCOUNT_TEAM_RECOMMENDATIONS"
    BENCHMARKING_INSIGHTS = "BENCHMARKING_INSIGHTS"
    CAMPAIGN_OPTIMIZATION = "CAMPAIGN_OPTIMIZATION"
    CATEGORY_INSIGHTS = "CATEGORY_INSIGHTS"
    CLICK_CREDITS = "CLICK_CREDITS"
    DEALS = "DEALS"
    MARKETPLACE_EXPANSION = "MARKETPLACE_EXPANSION"
    NEW_TO_BRAND_INSIGHTS = "NEW_TO_BRAND_INSIGHTS"
    PARTNER_GROWTH = "PARTNER_GROWTH"
    PATH_TO_PURCHASE_INSIGHTS = "PATH_TO_PURCHASE_INSIGHTS"
    READY_TO_LAUNCH_CAMPAIGNS = "READY_TO_LAUNCH_CAMPAIGNS"
    RETAIL_INSIGHTS = "RETAIL_INSIGHTS"
    SHARE_OF_VOICE_INSIGHTS = "SHARE_OF_VOICE_INSIGHTS"
    UNLAUNCHED_ASINS = "UNLAUNCHED_ASINS"


class PartnerOpportunitiesOpportunityV1Product(StrEnum):
    AMAZON_DSP = "AMAZON_DSP"
    AMAZON_LIVE = "AMAZON_LIVE"
    CROSS_PRODUCT = "CROSS_PRODUCT"
    POSTS = "POSTS"
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_BRANDS_VIDEO = "SPONSORED_BRANDS_VIDEO"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    SPONSORED_DISPLAY_VIDEO = "SPONSORED_DISPLAY_VIDEO"
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"
    SPONSORED_TV = "SPONSORED_TV"
    STORES = "STORES"
    VIDEO_ADS = "VIDEO_ADS"


class PartnerOpportunitiesOpportunityV1(BaseModel):
    audience: PartnerOpportunitiesOpportunityV1Audience = Field(..., description="The intended audience of the opportunity. For example, it might be targeted towards optimizing partner metrics or the me")
    call_to_action: str = Field(..., alias="callToAction", description="An explanation of why it's recommended to take the actions detailed in the opportunity's data file.")
    created_date: str = Field(..., alias="createdDate", description="When the opportunity was created, in ISO 8601 format. This should never change.")
    data_metadata: "PartnerOpportunitiesOpportunityDataMetadataV1" = Field(..., alias="dataMetadata", description="Contains the most recent data file information for the opportunity.  Can be used to track the availability of a partner ")
    data_url: str = Field(..., alias="dataUrl", description="The URL through which an opportunity's data file (in CSV format) can be downloaded.  A simple GET request is all that is")
    description: str = Field(..., description="A detailed description of the opportunity and how it is pertinent to partners. May provide a summary of the underlying d")
    objective: Optional[PartnerOpportunitiesOpportunityV1Objective] = Field(None, description="The objective of the opportunity. For example, an objective might be to drive sales, raise brand awareness, etc.  Deprec")
    objective_type: PartnerOpportunitiesOpportunityV1Objectivetype = Field(..., alias="objectiveType", description="The objective type of the opportunity. For example, an objective type might be around providing the unlaunched ASINs you")
    partner_opportunity_id: str = Field(..., alias="partnerOpportunityId", description="The unique ID for the opportunity.")
    product: PartnerOpportunitiesOpportunityV1Product = Field(..., description="The Amazon Advertising product to which the opportunity corresponds, like Amazon DSP, Video Ads, etc.")
    title: str = Field(..., description="The title of the opportunity.")
    updated_date: str = Field(..., alias="updatedDate", description="When the opportunity was last updated, in ISO 8601 format.")

    model_config = {'populate_by_name': True}


class PartnerOpportunitiesOpportunitiesPageV1(BaseModel):
    first_token: Optional[str] = Field(None, alias="firstToken", description="Pagination token back to the first page/element.")
    last_token: Optional[str] = Field(None, alias="lastToken", description="Pagination token to the last page.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Pagination token to the next page.")
    opportunities: list["PartnerOpportunitiesOpportunityV1"] = Field(..., description="The list of partner opportunities.")
    prev_token: Optional[str] = Field(None, alias="prevToken", description="Pagination token back to the previous page.")
    total_results: float = Field(..., alias="totalResults", description="Total results contained in the list of opportunities.")

    model_config = {'populate_by_name': True}


class PartnerOpportunitiesOpportunityObjectiveTypeFilterSummaryV1Value(StrEnum):
    ADVERTISER_INSIGHTS = "ADVERTISER_INSIGHTS"
    AD_API_ENDPOINT_ADOPTION = "AD_API_ENDPOINT_ADOPTION"
    AMAZON_ACCOUNT_TEAM_RECOMMENDATIONS = "AMAZON_ACCOUNT_TEAM_RECOMMENDATIONS"
    BENCHMARKING_INSIGHTS = "BENCHMARKING_INSIGHTS"
    CAMPAIGN_OPTIMIZATION = "CAMPAIGN_OPTIMIZATION"
    CATEGORY_INSIGHTS = "CATEGORY_INSIGHTS"
    CLICK_CREDITS = "CLICK_CREDITS"
    DEALS = "DEALS"
    MARKETPLACE_EXPANSION = "MARKETPLACE_EXPANSION"
    NEW_TO_BRAND_INSIGHTS = "NEW_TO_BRAND_INSIGHTS"
    PARTNER_GROWTH = "PARTNER_GROWTH"
    PATH_TO_PURCHASE_INSIGHTS = "PATH_TO_PURCHASE_INSIGHTS"
    READY_TO_LAUNCH_CAMPAIGNS = "READY_TO_LAUNCH_CAMPAIGNS"
    RETAIL_INSIGHTS = "RETAIL_INSIGHTS"
    SHARE_OF_VOICE_INSIGHTS = "SHARE_OF_VOICE_INSIGHTS"
    UNLAUNCHED_ASINS = "UNLAUNCHED_ASINS"


class PartnerOpportunitiesOpportunityObjectiveTypeFilterSummaryV1(BaseModel):
    count: float
    value: PartnerOpportunitiesOpportunityObjectiveTypeFilterSummaryV1Value

    model_config = {'populate_by_name': True}


class PartnerOpportunitiesOpportunityProductFilterSummaryV1Value(StrEnum):
    AMAZON_DSP = "AMAZON_DSP"
    AMAZON_LIVE = "AMAZON_LIVE"
    CROSS_PRODUCT = "CROSS_PRODUCT"
    POSTS = "POSTS"
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_BRANDS_VIDEO = "SPONSORED_BRANDS_VIDEO"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    SPONSORED_DISPLAY_VIDEO = "SPONSORED_DISPLAY_VIDEO"
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"
    SPONSORED_TV = "SPONSORED_TV"
    STORES = "STORES"
    VIDEO_ADS = "VIDEO_ADS"


class PartnerOpportunitiesOpportunityProductFilterSummaryV1(BaseModel):
    count: float
    value: PartnerOpportunitiesOpportunityProductFilterSummaryV1Value

    model_config = {'populate_by_name': True}


class PartnerOpportunitiesOpportunityAudienceFilterSummaryV1Value(StrEnum):
    PARTNER = "PARTNER"
    PARTNER_MANAGED_ADVERTISERS = "PARTNER_MANAGED_ADVERTISERS"
    PARTNER_MANAGED_AD_BUSINESS = "PARTNER_MANAGED_AD_BUSINESS"


class PartnerOpportunitiesOpportunityAudienceFilterSummaryV1(BaseModel):
    count: float
    value: PartnerOpportunitiesOpportunityAudienceFilterSummaryV1Value

    model_config = {'populate_by_name': True}


class PartnerOpportunitiesOpportunitiesSummaryV1(BaseModel):
    available_audiences: list["PartnerOpportunitiesOpportunityAudienceFilterSummaryV1"] = Field(..., alias="availableAudiences", description="All available opportunity audience values with the number of opportunities for each.")
    available_objective_types: list["PartnerOpportunitiesOpportunityObjectiveTypeFilterSummaryV1"] = Field(..., alias="availableObjectiveTypes", description="All available opportunity objective values with the number of opportunities for each.")
    available_products: list["PartnerOpportunitiesOpportunityProductFilterSummaryV1"] = Field(..., alias="availableProducts", description="All available opportunity product values with the number of opportunities for each.")
    opportunities_count: float = Field(..., alias="opportunitiesCount", description="Total number of opportunities for the partner.")
    opportunities_with_data_count: float = Field(..., alias="opportunitiesWithDataCount", description="Number of actionable opportunities with data for the partner.")
    unique_advertiser_approximate_count: float = Field(..., alias="uniqueAdvertiserApproximateCount", description="Approximate number of unique advertisers across all opportunities for the partner.")

    model_config = {'populate_by_name': True}

