"""Auto-generated Pydantic models. Do not edit manually.

Source: SponsoredBrands_v4_openapi.json
Title:  Sponsored Brands campaign management
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class timeOfDay(BaseModel):
    start_time: Optional[str] = Field(None, alias="startTime", description="The start time of intra-day budget rule window in the format 'hh:mm:ss'")
    end_time: Optional[str] = Field(None, alias="endTime", description="The end time of intra-day budget rule window in the format 'hh:mm:ss'. Required to be greater than start-time.")

    model_config = {'populate_by_name': True}


class ObjectIdFilter(BaseModel):
    """Filter entities by the list of objectIds."""
    include: Optional[list[str]] = None

    model_config = {'populate_by_name': True}


class QueryTermMatchType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class NameFilter(BaseModel):
    """Filter entities by name."""
    query_term_match_type: Optional["QueryTermMatchType"] = Field(None, alias="queryTermMatchType")
    include: Optional[list[str]] = None

    model_config = {'populate_by_name': True}


class EntityState(StrEnum):
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"
    ARCHIVED = "ARCHIVED"


class EntityStateFilter(BaseModel):
    """Filter entities by state."""
    include: Optional[list["EntityState"]] = None

    model_config = {'populate_by_name': True}


class ListSponsoredBrandsAdGroupsRequestContent(BaseModel):
    campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    state_filter: Optional["EntityStateFilter"] = Field(None, alias="stateFilter")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    ad_group_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    include_extended_data_fields: Optional[bool] = Field(None, alias="includeExtendedDataFields", description="Setting to true will slow down performance because the API needs to retrieve extra information for each campaign.")
    name_filter: Optional["NameFilter"] = Field(None, alias="nameFilter")

    model_config = {'populate_by_name': True}


class ErrorCause(BaseModel):
    """Structure describing error cause - location in the payload and data causing error."""
    location: str = Field(..., description="Error location, JSON Path expression specifying element of API payload causing error.")
    trigger: Optional[str] = Field(None, description="Optional value causing error.")

    model_config = {'populate_by_name': True}


class OtherError(BaseModel):
    """Errors not related to any of the other error types."""
    reason: str
    cause: "ErrorCause"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class DateError(BaseModel):
    """Errors related to dates."""
    reason: str = Field(..., description="Exact error reason..")
    cause: "ErrorCause"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class BiddingError(BaseModel):
    """Errors related to bids."""
    reason: str = Field(..., description="Exact error reason.")
    cause: "ErrorCause"
    upper_limit: Optional[str] = Field(None, alias="upperLimit")
    lower_limit: Optional[str] = Field(None, alias="lowerLimit")
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class RangeError(BaseModel):
    """Errors related to range constraints violations."""
    reason: str
    allowed: Optional[list[str]] = Field(None, description="Allowed values.")
    cause: "ErrorCause"
    upper_limit: Optional[str] = Field(None, alias="upperLimit", description="Optional upper limit.")
    lower_limit: Optional[str] = Field(None, alias="lowerLimit", description="Optional lower limit.")
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class AdGroupMutationErrorSelector(BaseModel):
    date_error: Optional["DateError"] = Field(None, alias="dateError")
    bidding_error: Optional["BiddingError"] = Field(None, alias="biddingError")
    range_error: Optional["RangeError"] = Field(None, alias="rangeError")
    other_error: Optional["OtherError"] = Field(None, alias="otherError")

    model_config = {'populate_by_name': True}


class AdGroupMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error.")
    error_value: "AdGroupMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class GetLandingPageMetadataResponseContent(BaseModel):
    page_type: str = Field(..., alias="pageType", description="The type of landing page, such as store page, product list (simple landing page), custom url. | Page Type    | |--------")
    canonical_url: str = Field(..., alias="canonicalUrl", description="A canonical URL is the URL that represents the best version of landing page URL from a group of duplicate landing page U")
    un_supported_reason: Optional[str] = Field(None, alias="unSupportedReason", description="A human-readable description of the unSupportedReasonCode field.")
    is_supported: Optional[bool] = Field(None, alias="isSupported", description="This field determines whether the landing page is supported for the ad product.")
    un_supported_reason_code: Optional[str] = Field(None, alias="unSupportedReasonCode", description="Enumerated code for why landing page is unsupported. | Reason Code                 | | SB_DETAIL_PAGE_UNSUPPORTED  | | S")

    model_config = {'populate_by_name': True}


class InvalidArgumentErrorSelector(BaseModel):
    range_error: Optional["RangeError"] = Field(None, alias="rangeError")
    other_error: Optional["OtherError"] = Field(None, alias="otherError")

    model_config = {'populate_by_name': True}


class InvalidArgumentError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "InvalidArgumentErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class InvalidArgumentErrorCode(StrEnum):
    INVALID_ARGUMENT = "INVALID_ARGUMENT"


class InvalidArgumentExceptionResponseContent(BaseModel):
    code: "InvalidArgumentErrorCode"
    message: str = Field(..., description="Human readable error message.")
    errors: Optional[list["InvalidArgumentError"]] = None

    model_config = {'populate_by_name': True}


class BudgetError(BaseModel):
    reason: str
    cause: "ErrorCause"
    upper_limit: Optional[str] = Field(None, alias="upperLimit")
    lower_limit: Optional[str] = Field(None, alias="lowerLimit")
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class BillingError(BaseModel):
    """Errors related to billing."""
    reason: str = Field(..., description="Exact error reason.")
    cause: "ErrorCause"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class CampaignMutationErrorSelector(BaseModel):
    date_error: Optional["DateError"] = Field(None, alias="dateError")
    bidding_error: Optional["BiddingError"] = Field(None, alias="biddingError")
    budget_error: Optional["BudgetError"] = Field(None, alias="budgetError")
    billing_error: Optional["BillingError"] = Field(None, alias="billingError")
    range_error: Optional["RangeError"] = Field(None, alias="rangeError")
    other_error: Optional["OtherError"] = Field(None, alias="otherError")

    model_config = {'populate_by_name': True}


class CampaignMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error.")
    error_value: "CampaignMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class CampaignMutationFailureResponseItem(BaseModel):
    index: float = Field(..., description="the index of the campaign in the array from the request body.")
    errors: Optional[list["CampaignMutationError"]] = Field(None, description="A list of validation errors.")

    model_config = {'populate_by_name': True}


class ProductLocation(StrEnum):
    SOLD_ON_AMAZON = "SOLD_ON_AMAZON"
    NOT_SOLD_ON_AMAZON = "NOT_SOLD_ON_AMAZON"
    SOLD_ON_DTC = "SOLD_ON_DTC"


class AudienceSegmentType(StrEnum):
    SPONSORED_ADS_AMC = "SPONSORED_ADS_AMC"
    BEHAVIOR_DYNAMIC = "BEHAVIOR_DYNAMIC"


class AudienceSegment(BaseModel):
    audience_id: Optional[str] = Field(None, alias="audienceId")
    audience_segment_type: Optional["AudienceSegmentType"] = Field(None, alias="audienceSegmentType")

    model_config = {'populate_by_name': True}


class ShopperCohortType(StrEnum):
    AUDIENCE_SEGMENT = "AUDIENCE_SEGMENT"


class ShopperCohortBidAdjustment(BaseModel):
    shopper_cohort_type: Optional["ShopperCohortType"] = Field(None, alias="shopperCohortType")
    percentage: Optional[float] = None
    audience_segments: Optional[list["AudienceSegment"]] = Field(None, alias="audienceSegments", description="Required when 'AUDIENCE_SEGMENT' is used for shopperCohortType.")

    model_config = {'populate_by_name': True}


class Placement(StrEnum):
    HOME = "HOME"
    DETAIL_PAGE = "DETAIL_PAGE"
    OTHER = "OTHER"
    TOP_OF_SEARCH = "TOP_OF_SEARCH"


class BidAdjustmentByPlacement(BaseModel):
    percentage: Optional[float] = None
    placement: Optional["Placement"] = None

    model_config = {'populate_by_name': True}


class Bidding(BaseModel):
    bid_optimization: Optional[bool] = Field(None, alias="bidOptimization", description="Whether to use automatic placement level bid optimization. If set to true, Amazon will automatically set the right place")
    shopper_cohort_bid_adjustments: Optional[list["ShopperCohortBidAdjustment"]] = Field(None, alias="shopperCohortBidAdjustments", description="Shopper cohort based bid adjustments.")
    bid_adjustments_by_placement: Optional[list["BidAdjustmentByPlacement"]] = Field(None, alias="bidAdjustmentsByPlacement", description="Placement level bid adjustment. Note that this field can only be set when 'bidOptimization' is set to false.")

    model_config = {'populate_by_name': True}


class SiteRestriction(StrEnum):
    AMAZON_BUSINESS = "AMAZON_BUSINESS"


class BudgetType(StrEnum):
    DAILY = "DAILY"
    LIFETIME = "LIFETIME"


class RuleBasedBudget(BaseModel):
    is_processing: Optional[bool] = Field(None, alias="isProcessing")
    applicable_rule_name: Optional[str] = Field(None, alias="applicableRuleName")
    value: Optional[float] = None
    applicable_rule_id: Optional[str] = Field(None, alias="applicableRuleId")

    model_config = {'populate_by_name': True}


class CampaignServingStatus(StrEnum):
    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_OUT_OF_PREPAY_BALANCE = "ADVERTISER_OUT_OF_PREPAY_BALANCE"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    CAMPAIGN_STATUS_ENABLED = "CAMPAIGN_STATUS_ENABLED"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    PORTFOLIO_STATUS_ENABLED = "PORTFOLIO_STATUS_ENABLED"
    PORTFOLIO_PAUSED = "PORTFOLIO_PAUSED"
    PORTFOLIO_ARCHIVED = "PORTFOLIO_ARCHIVED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    INELIGIBLE = "INELIGIBLE"
    ELIGIBLE = "ELIGIBLE"
    ENDED = "ENDED"
    PENDING_REVIEW = "PENDING_REVIEW"
    PENDING_START_DATE = "PENDING_START_DATE"
    REJECTED = "REJECTED"
    UNKNOWN = "UNKNOWN"


class CampaignExtendedData(BaseModel):
    """CampaignExtendedData can only be retrieved via the list API. It won't be available in the response during update/create."""
    serving_status: Optional["CampaignServingStatus"] = Field(None, alias="servingStatus")
    last_update_date: Optional[float] = Field(None, alias="lastUpdateDate", description="Date of last update in epoch time.")
    serving_status_details: Optional[list[str]] = Field(None, alias="servingStatusDetails", description="The serving status reasons of the Campaign.")
    creation_date: Optional[float] = Field(None, alias="creationDate", description="Creation date in epoch time.")

    model_config = {'populate_by_name': True}


class Tags(BaseModel):
    """A list of advertiser-specified custom identifiers for the campaign. Each customer identifier is a key-value pair. You can specify a maximum of 50 identifiers."""
    __root__: dict[str, str] = {}


class Campaign(BaseModel):
    budget_type: "BudgetType" = Field(..., alias="budgetType")
    rule_based_budget: Optional["RuleBasedBudget"] = Field(None, alias="ruleBasedBudget")
    brand_entity_id: Optional[str] = Field(None, alias="brandEntityId")
    is_multi_ad_groups_enabled: Optional[bool] = Field(None, alias="isMultiAdGroupsEnabled")
    goal: Optional[str] = Field(None, description="Goal will allow you to set goal type to help drive your campaign performance. If no goal is selected then it will defaul")
    bidding: Optional["Bidding"] = None
    end_date: Optional[str] = Field(None, alias="endDate", description="The format of the date is YYYY-MM-DD.")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign.")
    product_location: Optional["ProductLocation"] = Field(None, alias="productLocation")
    tags: Optional["Tags"] = None
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="The identifier of an existing portfolio to which the campaign is associated.")
    cost_type: Optional[str] = Field(None, alias="costType", description="The costType can be set to determines how the campaign will bid and charge. To view the bid maximums and minimums by geo")
    smart_default: Optional[list[str]] = Field(None, alias="smartDefault", description="The smartDefault specifies a list of the smart default options for the campaign.  `smartDefault` is optional for create ")
    site_restrictions: Optional[list["SiteRestriction"]] = Field(None, alias="siteRestrictions", description="Restrict the ad to a particular site. siteRestrictions is an optional field.  If this field is not set, ads from the cam")
    name: str = Field(..., description="The name of the campaign.")
    state: "EntityState"
    start_date: Optional[str] = Field(None, alias="startDate", description="The format of the date is YYYY-MM-DD.")
    budget: float
    extended_data: Optional["CampaignExtendedData"] = Field(None, alias="extendedData")
    targeted_pg_deal_id: Optional[str] = Field(None, alias="targetedPGDealId", description="DealId associated with the campaign. This field is immutable and cannot be changed after the campaign is created.")

    model_config = {'populate_by_name': True}


class CampaignMutationSuccessResponseItem(BaseModel):
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="The campaign ID.")
    index: float = Field(..., description="The index of the campaign in the array from the request body.")
    campaign: Optional["Campaign"] = None

    model_config = {'populate_by_name': True}


class BulkCampaignOperationResponse(BaseModel):
    success: Optional[list["CampaignMutationSuccessResponseItem"]] = None
    error: Optional[list["CampaignMutationFailureResponseItem"]] = None

    model_config = {'populate_by_name': True}


class UpdateSponsoredBrandsCampaignsResponseContent(BaseModel):
    campaigns: Optional["BulkCampaignOperationResponse"] = None

    model_config = {'populate_by_name': True}


class GetLandingPageMetadataRequestContent(BaseModel):
    ad_product: str = Field(..., alias="adProduct", description="An ad product is a top level offering from amazon ads as defined in our marketing, with a given feature set, and busines")
    landing_page_url: str = Field(..., alias="landingPageUrl", description="The URL of the landing page.")

    model_config = {'populate_by_name': True}


class AdGroupServingStatus(StrEnum):
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_POLICING_PENDING_REVIEW = "AD_GROUP_POLICING_PENDING_REVIEW"
    AD_GROUP_POLICING_CREATIVE_REJECTED = "AD_GROUP_POLICING_CREATIVE_REJECTED"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_OUT_OF_PREPAY_BALANCE = "ADVERTISER_OUT_OF_PREPAY_BALANCE"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    CAMPAIGN_STATUS_ENABLED = "CAMPAIGN_STATUS_ENABLED"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    PORTFOLIO_STATUS_ENABLED = "PORTFOLIO_STATUS_ENABLED"
    PORTFOLIO_PAUSED = "PORTFOLIO_PAUSED"
    PORTFOLIO_ARCHIVED = "PORTFOLIO_ARCHIVED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    INELIGIBLE = "INELIGIBLE"
    ELIGIBLE = "ELIGIBLE"
    ENDED = "ENDED"
    PENDING_REVIEW = "PENDING_REVIEW"
    PENDING_START_DATE = "PENDING_START_DATE"
    REJECTED = "REJECTED"
    UNKNOWN = "UNKNOWN"


class AdGroupExtendedData(BaseModel):
    serving_status: Optional["AdGroupServingStatus"] = Field(None, alias="servingStatus")
    last_update_date: Optional[float] = Field(None, alias="lastUpdateDate", description="Date of last update in epoch time.")
    serving_status_details: Optional[list[str]] = Field(None, alias="servingStatusDetails", description="The serving status reasons of the Ad Group.")
    creation_date: Optional[float] = Field(None, alias="creationDate", description="Creation date in epoch time.")

    model_config = {'populate_by_name': True}


class AdGroup(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign to which the keyword is associated.")
    name: str = Field(..., description="The name of the ad group.")
    state: "EntityState"
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the keyword.")
    extended_data: Optional["AdGroupExtendedData"] = Field(None, alias="extendedData")

    model_config = {'populate_by_name': True}


class ListSponsoredBrandsAdGroupsBetaResponseContent(BaseModel):
    total_results: Optional[float] = Field(None, alias="totalResults", description="The total number of entities.")
    ad_groups: Optional[list["AdGroup"]] = Field(None, alias="adGroups")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")

    model_config = {'populate_by_name': True}


class CreateOrUpdateEntityState(StrEnum):
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


class CreateVideoCreative(BaseModel):
    asins: Optional[list[str]] = None
    consent_to_translate: Optional[bool] = Field(None, alias="consentToTranslate", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    video_asset_ids: Optional[list[str]] = Field(None, alias="videoAssetIds", description="In SB API V4, `videoMediaIds` is replaced by `videoAssetIds`. `videoAssetIds` will only allow Asset Library identifiers ")

    model_config = {'populate_by_name': True}


class CreateVideoAd(BaseModel):
    name: str = Field(..., description="The name of the ad.")
    state: "CreateOrUpdateEntityState"
    ad_group_id: str = Field(..., alias="adGroupId", description="The adGroup identifier.")
    creative: "CreateVideoCreative"

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsVideoAdsBetaRequestContent(BaseModel):
    ads: list["CreateVideoAd"]

    model_config = {'populate_by_name': True}


class LandingPageType(StrEnum):
    PRODUCT_LIST = "PRODUCT_LIST"
    STORE = "STORE"
    CUSTOM_URL = "CUSTOM_URL"
    DETAIL_PAGE = "DETAIL_PAGE"


class LandingPage(BaseModel):
    asins: Optional[list[str]] = None
    page_type: Optional["LandingPageType"] = Field(None, alias="pageType")
    url: Optional[str] = Field(None, description="URL of an existing simple landing page or Store page. Vendors may also specify the URL of a custom landing page. If a cu")

    model_config = {'populate_by_name': True}


class BrandLogoCrop(BaseModel):
    """The crop to apply to the selected Brand logo. A Brand logo must have minimum dimensions of 400x400. If a brandLogoAssetID is supplied but a crop is not, the crop will be defaulted to the whole image."""
    top: Optional[float] = None
    left: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None

    model_config = {'populate_by_name': True}


class CreateBrandVideoCreative(BaseModel):
    asins: Optional[list[str]] = None
    brand_logo_crop: Optional["BrandLogoCrop"] = Field(None, alias="brandLogoCrop")
    brand_name: Optional[str] = Field(None, alias="brandName")
    consent_to_translate: Optional[bool] = Field(None, alias="consentToTranslate", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    video_asset_ids: Optional[list[str]] = Field(None, alias="videoAssetIds")
    brand_logo_asset_id: Optional[str] = Field(None, alias="brandLogoAssetID")
    headline: Optional[str] = Field(None, description="The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maxi")

    model_config = {'populate_by_name': True}


class CreateBrandVideoAd(BaseModel):
    landing_page: "LandingPage" = Field(..., alias="landingPage")
    name: str = Field(..., description="The name of the ad.")
    state: "CreateOrUpdateEntityState"
    ad_group_id: str = Field(..., alias="adGroupId", description="The adGroup identifier.")
    creative: "CreateBrandVideoCreative"

    model_config = {'populate_by_name': True}


class SBTargetingEstimatedReachRange(BaseModel):
    min: Optional[int] = None
    max: Optional[int] = None

    model_config = {'populate_by_name': True}


class Source(BaseModel):
    """Source of Creative Recommendation Valid Sources are LANDING_PAGE_URL of store with landing page url value, and POST_ID of post organic content obtained from POSTS Advertising API, more could be added """
    type_: Optional[str] = Field(None, alias="type")
    value: Optional[str] = None

    model_config = {'populate_by_name': True}


class CreativeRecommendationsRequestContent(BaseModel):
    creative_type: str = Field(..., alias="creativeType", description="Supported are PRODUCT_COLLECTION, STORE_SPOTLIGHT, VIDEO, BRAND_VIDEO. More could be added in future.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results,")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Set a limit on the number of results returned by an operation.")
    source: "Source"

    model_config = {'populate_by_name': True}


class CustomImageCrop(BaseModel):
    """The crop to apply to the selected Custom image. A Custom image must have a 1200x628 aspect ratio, with a .01 delta for floating point precision. If a customImageAssetId is supplied but a crop is not, """
    top: Optional[float] = None
    left: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None

    model_config = {'populate_by_name': True}


class CustomImage(BaseModel):
    asset_id: Optional[str] = Field(None, alias="assetId")
    crop: Optional["CustomImageCrop"] = None
    url: Optional[str] = None

    model_config = {'populate_by_name': True}


class CreativeStatus(StrEnum):
    SUBMITTED_FOR_MODERATION = "SUBMITTED_FOR_MODERATION"
    PENDING_TRANSLATION = "PENDING_TRANSLATION"
    PENDING_MODERATION_REVIEW = "PENDING_MODERATION_REVIEW"
    APPROVED_BY_MODERATION = "APPROVED_BY_MODERATION"
    REJECTED_BY_MODERATION = "REJECTED_BY_MODERATION"
    PUBLISHED = "PUBLISHED"


class Subpage(BaseModel):
    page_title: Optional[str] = Field(None, alias="pageTitle")
    asin: Optional[str] = None
    url: Optional[str] = None

    model_config = {'populate_by_name': True}


class CreativePropertyToOptimize(StrEnum):
    HEADLINE = "HEADLINE"


class CreativeType(StrEnum):
    PRODUCT_COLLECTION = "PRODUCT_COLLECTION"
    STORE_SPOTLIGHT = "STORE_SPOTLIGHT"
    VIDEO = "VIDEO"
    BRAND_VIDEO = "BRAND_VIDEO"


class Creative(BaseModel):
    brand_logo_crop: Optional["BrandLogoCrop"] = Field(None, alias="brandLogoCrop")
    brand_name: Optional[str] = Field(None, alias="brandName")
    custom_image_asset_id: Optional[str] = Field(None, alias="customImageAssetId")
    consent_to_translate: Optional[bool] = Field(None, alias="consentToTranslate", description="If set to true and the headline and/or video asset are not in the marketplace's default language, Amazon will attempt to")
    custom_images: Optional[list["CustomImage"]] = Field(None, alias="customImages", description="Requires minimum one custom image. You can add an optional collection of custom images that can be displayed on the ad a")
    custom_image_crop: Optional["CustomImageCrop"] = Field(None, alias="customImageCrop")
    custom_image_url: Optional[str] = Field(None, alias="customImageUrl")
    type_: Optional["CreativeType"] = Field(None, alias="type")
    original_video_asset_ids: Optional[list[str]] = Field(None, alias="originalVideoAssetIds", description="The assetIds of the original videos submitted by the advertiser. If 'consentToTranslate' is set to true and translation ")
    asins: Optional[list[str]] = None
    brand_logo_url: Optional[str] = Field(None, alias="brandLogoUrl")
    subpages: Optional[list["Subpage"]] = None
    creative_properties_to_optimize: Optional[list["CreativePropertyToOptimize"]] = Field(None, alias="creativePropertiesToOptimize", description="If this property is enabled, Sponsored Brands will dynamically optimize by enhancing or generating creative properties b")
    original_headline: Optional[str] = Field(None, alias="originalHeadline", description="The original headline submitted by the advertiser.")
    video_asset_ids: Optional[list[str]] = Field(None, alias="videoAssetIds", description="In SB API V4, `videoMediaIds` is replaced by `videoAssetIds`. `videoAssetIds` will only allow Asset Library identifiers ")
    brand_logo_asset_id: Optional[str] = Field(None, alias="brandLogoAssetID")
    headline: Optional[str] = Field(None, description="The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maxi")
    creative_status: Optional["CreativeStatus"] = Field(None, alias="creativeStatus")
    creative_version: Optional[str] = Field(None, alias="creativeVersion", description="The version identifier that helps you keep track of multiple versions of a submitted (non-draft) Sponsored Brands creati")

    model_config = {'populate_by_name': True}


class AdServingStatus(StrEnum):
    AD_STATUS_LIVE = "AD_STATUS_LIVE"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    AD_POLICING_SUSPENDED = "AD_POLICING_SUSPENDED"
    AD_PAUSED = "AD_PAUSED"
    AD_ARCHIVED = "AD_ARCHIVED"
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_POLICING_PENDING_REVIEW = "AD_GROUP_POLICING_PENDING_REVIEW"
    AD_GROUP_POLICING_CREATIVE_REJECTED = "AD_GROUP_POLICING_CREATIVE_REJECTED"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_OUT_OF_PREPAY_BALANCE = "ADVERTISER_OUT_OF_PREPAY_BALANCE"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    CAMPAIGN_STATUS_ENABLED = "CAMPAIGN_STATUS_ENABLED"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    PORTFOLIO_STATUS_ENABLED = "PORTFOLIO_STATUS_ENABLED"
    PORTFOLIO_PAUSED = "PORTFOLIO_PAUSED"
    PORTFOLIO_ARCHIVED = "PORTFOLIO_ARCHIVED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    INELIGIBLE = "INELIGIBLE"
    ELIGIBLE = "ELIGIBLE"
    ENDED = "ENDED"
    PENDING_REVIEW = "PENDING_REVIEW"
    PENDING_START_DATE = "PENDING_START_DATE"
    REJECTED = "REJECTED"
    UNKNOWN = "UNKNOWN"


class AdExtendedData(BaseModel):
    serving_status: Optional["AdServingStatus"] = Field(None, alias="servingStatus")
    last_update_date: Optional[float] = Field(None, alias="lastUpdateDate", description="Date of last update in epoch time.")
    serving_status_details: Optional[list[str]] = Field(None, alias="servingStatusDetails", description="The serving status reasons of the Ad.")
    creation_date: Optional[float] = Field(None, alias="creationDate", description="Creation date in epoch time.")

    model_config = {'populate_by_name': True}


class MultiAdGroupAd(BaseModel):
    ad_id: str = Field(..., alias="adId", description="The ad identifier.")
    campaign_id: str = Field(..., alias="campaignId", description="The campaign identifier.")
    landing_page: Optional["LandingPage"] = Field(None, alias="landingPage")
    name: str = Field(..., description="The name of the ad.")
    state: "EntityState"
    ad_group_id: str = Field(..., alias="adGroupId", description="The adGroup identifier.")
    creative: Optional["Creative"] = None
    extended_data: Optional["AdExtendedData"] = Field(None, alias="extendedData")

    model_config = {'populate_by_name': True}


class AssetCrop(BaseModel):
    """Asset cropping attributes"""
    top: Optional[float] = Field(None, description="The highest pixel from which to begin cropping")
    left: Optional[float] = Field(None, description="The leftmost pixel from which to begin cropping")
    width: Optional[float] = Field(None, description="The number of pixels to crop rightwards from the value specified as left")
    height: Optional[float] = Field(None, description="The number of pixels to crop down from the value specified as top")

    model_config = {'populate_by_name': True}


class CreativeLandingPageV2(BaseModel):
    """Landing page V2, where type is String with allowed values listed, and url or asins of that type."""
    asins: Optional[list[str]] = Field(None, description="The list of asins on the landingPage If type is PRODUCT_LIST. A minimum of 3 asins are required. For the 'PRODUCT_LIST' ")
    type_: Optional[str] = Field(None, alias="type", description="Supported types are PRODUCT_LIST, STORE, DETAIL_PAGE, CUSTOM_URL. More could be added in future.")
    url: Optional[str] = Field(None, description="The url of the landingPage. When including the 'asins' property in the request, do not include this property, as they ar")

    model_config = {'populate_by_name': True}


class ExtendedProductCollectionCreative(BaseModel):
    asins: list[str] = Field(..., description="An array of ASINs associated with the creative.")
    brand_logo_crop: Optional["AssetCrop"] = Field(None, alias="brandLogoCrop")
    brand_name: str = Field(..., alias="brandName", description="The displayed brand name in the ad headline. Maximum length is 30 characters. See [the policy](https://advertising.amazo")
    landing_page: Optional["CreativeLandingPageV2"] = Field(None, alias="landingPage")
    custom_images: Optional[list["CustomImage"]] = Field(None, alias="customImages", description="An array of customImages associated with the creative.")
    consent_to_translate: Optional[bool] = Field(None, alias="consentToTranslate", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    creative_properties_to_optimize: Optional[list["CreativePropertyToOptimize"]] = Field(None, alias="creativePropertiesToOptimize", description="If this property is enabled, Sponsored Brands will dynamically optimize by enhancing or generating creative properties b")
    brand_logo_asset_id: str = Field(..., alias="brandLogoAssetId", description="The identifier of the [brand logo](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#brandlogo) ")
    headline: str = Field(..., description="The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maxi")

    model_config = {'populate_by_name': True}


class UnsupportedMediaTypeExceptionResponseContent(BaseModel):
    code: str = Field(..., description="A human-readable description of the enumerated response code in the `code` field.")
    details: str = Field(..., description="An enumerated response code.")

    model_config = {'populate_by_name': True}


class OptimizationRuleToEntityMapping(BaseModel):
    entity_type: str = Field(..., alias="entityType", description="Enum: 'CAMPAIGN'  The type of entity passed.")
    entity_id: str = Field(..., alias="entityId", description="Entity object identifier.")
    optimization_rule_id: str = Field(..., alias="optimizationRuleId", description="The identifier of the optimization rule.")

    model_config = {'populate_by_name': True}


class ThrottledErrorCode(StrEnum):
    THROTTLED = "THROTTLED"


class DayOfWeek(StrEnum):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class RecurrenceType(StrEnum):
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"


class Recurrence(BaseModel):
    type_: Optional["RecurrenceType"] = Field(None, alias="type")
    days_of_week: Optional[list["DayOfWeek"]] = Field(None, alias="daysOfWeek", description="Object representing days of the week for weekly type rule. It is not required for daily recurrence type")
    intra_day_schedule: Optional[list["timeOfDay"]] = Field(None, alias="intraDaySchedule", description="List of objects representing start and end time of desired intra-day budget rule window")

    model_config = {'populate_by_name': True}


class ComparisonOperator(StrEnum):
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"


class PerformanceMetric(StrEnum):
    ACOS = "ACOS"
    CTR = "CTR"
    CVR = "CVR"
    ROAS = "ROAS"


class PerformanceMeasureCondition(BaseModel):
    metric_name: "PerformanceMetric" = Field(..., alias="metricName")
    comparison_operator: "ComparisonOperator" = Field(..., alias="comparisonOperator")
    threshold: float = Field(..., description="The performance threshold value.")

    model_config = {'populate_by_name': True}


class SDRuleType(StrEnum):
    SCHEDULE = "SCHEDULE"
    PERFORMANCE = "PERFORMANCE"


class BudgetChangeType(StrEnum):
    PERCENT = "PERCENT"


class budgetIncreaseBy(BaseModel):
    type_: "BudgetChangeType" = Field(..., alias="type")
    value: float = Field(..., description="The budget value.")

    model_config = {'populate_by_name': True}


class EventTypeRuleDuration(BaseModel):
    """Object representing event type rule duration."""
    event_id: str = Field(..., alias="eventId", description="The event identifier. This value is available from the budget rules recommendation API.")
    end_date: Optional[str] = Field(None, alias="endDate", description="The event end date in YYYYMMDD format. Read-only.")
    event_name: Optional[str] = Field(None, alias="eventName", description="The event name. Read-only.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The event start date in YYYYMMDD format. Read-only. Note that this field is present only for announced events.")

    model_config = {'populate_by_name': True}


class DateRangeTypeRuleDuration(BaseModel):
    """Object representing date range type rule duration."""
    end_date: Optional[str] = Field(None, alias="endDate", description="The end date of the budget rule in YYYYMMDD format. The end date is inclusive. Required to be equal or greater than `sta")
    start_date: str = Field(..., alias="startDate", description="The start date of the budget rule in YYYYMMDD format. The start date is inclusive. Required to be greater than or equal ")

    model_config = {'populate_by_name': True}


class RuleDuration(BaseModel):
    event_type_rule_duration: Optional["EventTypeRuleDuration"] = Field(None, alias="eventTypeRuleDuration")
    date_range_type_rule_duration: Optional["DateRangeTypeRuleDuration"] = Field(None, alias="dateRangeTypeRuleDuration")

    model_config = {'populate_by_name': True}


class SDBudgetRuleDetails(BaseModel):
    """Object representing details of a budget rule for SD campaign"""
    duration: Optional["RuleDuration"] = None
    recurrence: Optional["Recurrence"] = None
    rule_type: Optional["SDRuleType"] = Field(None, alias="ruleType")
    budget_increase_by: Optional["budgetIncreaseBy"] = Field(None, alias="budgetIncreaseBy")
    name: Optional[str] = Field(None, description="The budget rule name. Required to be unique within a campaign.")
    performance_measure_condition: Optional["PerformanceMeasureCondition"] = Field(None, alias="performanceMeasureCondition")

    model_config = {'populate_by_name': True}


class state(StrEnum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"


class SDBudgetRule(BaseModel):
    rule_state: Optional["state"] = Field(None, alias="ruleState")
    last_updated_date: Optional[float] = Field(None, alias="lastUpdatedDate", description="Epoch time of budget rule update. Read-only.")
    created_date: Optional[float] = Field(None, alias="createdDate", description="Epoch time of budget rule creation. Read-only.")
    rule_details: Optional["SDBudgetRuleDetails"] = Field(None, alias="ruleDetails")
    rule_id: str = Field(..., alias="ruleId", description="The budget rule identifier.")
    rule_status: Optional[str] = Field(None, alias="ruleStatus", description="The budget rule status. Read-only.")

    model_config = {'populate_by_name': True}


class ConflictStateErrorCode(StrEnum):
    CONFLICT_STATE = "CONFLICT_STATE"


class ImageSpec(BaseModel):
    """Structure for Image specification"""
    resolution: Optional[str] = Field(None, description="Image resolution, default is 1200x628. New values will be added later. |   Resolution  |   Value       | |--------------")
    file_format: Optional[str] = Field(None, alias="fileFormat", description="Valid values are PNG and JPEG, default is PNG. New values will be added later. |   File Format  |   Value       | |-----")

    model_config = {'populate_by_name': True}


class ImageTaskMetadata(BaseModel):
    image_spec: Optional["ImageSpec"] = Field(None, alias="imageSpec")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Optional. An upper bound for number of image results for this set of metadata. Default value is 4.")
    theme_id: Optional[str] = Field(None, alias="themeId", description="Optional.")
    asin: str = Field(..., description="Required. The product that is shown in AI image.")
    prompt: Optional[str] = Field(None, description="Optional. Open text prompt")
    product_image_asset_id: Optional[str] = Field(None, alias="productImageAssetId", description="Optional. Source image provided by advertiser and they are registered in Asset Library")

    model_config = {'populate_by_name': True}


class SubmitImageTasksRequestContent(BaseModel):
    image_task_metadata_list: Optional[list["ImageTaskMetadata"]] = Field(None, alias="imageTaskMetadataList", description="Advertiser provided information to generate AI images. Max size of the list is 4, each element will be executed as an in")

    model_config = {'populate_by_name': True}


class ProgramType(StrEnum):
    A_PLUS = "A_PLUS"
    SB = "SB"
    POSTS = "POSTS"
    STORES = "STORES"
    BBB_STORES = "BBB_STORES"
    AMAZON_DSP = "AMAZON_DSP"
    AMAZON_CREATIVE_SERVICES = "AMAZON_CREATIVE_SERVICES"


class AccessDeniedErrorCode(StrEnum):
    ACCESS_DENIED = "ACCESS_DENIED"


class AccessDeniedExceptionResponseContent(BaseModel):
    code: "AccessDeniedErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class AssetSubType(StrEnum):
    CUSTOM_IMAGE = "CUSTOM_IMAGE"
    LOGO = "LOGO"
    PRODUCT_IMAGE = "PRODUCT_IMAGE"
    AUTHOR_IMAGE = "AUTHOR_IMAGE"


class CreativeLandingPageType(StrEnum):
    PRODUCT_LIST = "PRODUCT_LIST"
    STORE = "STORE"
    DETAIL_PAGE = "DETAIL_PAGE"
    CUSTOM_URL = "CUSTOM_URL"
    AD_LANDING_PREVIEW = "AD_LANDING_PREVIEW"
    SEARCH = "SEARCH"
    BROWSE = "BROWSE"
    ADVERTISING_LANDING_PAGE = "ADVERTISING_LANDING_PAGE"
    UNKNOWN = "UNKNOWN"


class CreativeLandingPage(BaseModel):
    """Landing page."""
    asins: Optional[list[str]] = Field(None, description="The list of asins on the landingPage If type is PRODUCT_LIST.")
    type_: Optional["CreativeLandingPageType"] = Field(None, alias="type")
    value: Optional[str] = Field(None, description="The url of the landingPage.")

    model_config = {'populate_by_name': True}


class CreativeProperties(BaseModel):
    """Creative properties"""
    brand_logo_crop: Optional["AssetCrop"] = Field(None, alias="brandLogoCrop")
    brand_name: Optional[str] = Field(None, alias="brandName", description="The displayed brand name in the ad headline. Maximum length is 30 characters. See [the policy](https://advertising.amazo")
    custom_image_asset_id: Optional[str] = Field(None, alias="customImageAssetId", description="The identifier of image/video asset from the store's asset library")
    landing_page: Optional["CreativeLandingPage"] = Field(None, alias="landingPage")
    custom_images: Optional[list["CustomImage"]] = Field(None, alias="customImages", description="An array of customImages associated with the creative.")
    consent_to_translate: Optional[bool] = Field(None, alias="consentToTranslate", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    custom_image_crop: Optional["AssetCrop"] = Field(None, alias="customImageCrop")
    custom_image_url: Optional[str] = Field(None, alias="customImageUrl")
    original_video_asset_ids: Optional[list[str]] = Field(None, alias="originalVideoAssetIds", description="The assetIds of the original videos submitted by the advertiser. If 'consentToTranslate' is set to true and translation ")
    asins: Optional[list[str]] = Field(None, description="----------------------------------------------- List types ----------------------------------------------- A list of ASI")
    brand_logo_url: Optional[str] = Field(None, alias="brandLogoUrl")
    subpages: Optional[list["Subpage"]] = Field(None, description="An array of subpages")
    creative_properties_to_optimize: Optional[list["CreativePropertyToOptimize"]] = Field(None, alias="creativePropertiesToOptimize", description="If this property is enabled, Sponsored Brands will dynamically optimize by enhancing or generating creative properties b")
    original_headline: Optional[str] = Field(None, alias="originalHeadline", description="The original headline submitted by the advertiser.")
    video_asset_ids: Optional[list[str]] = Field(None, alias="videoAssetIds", description="The assetIds of the original videos submitted by the advertiser. If 'consentToTranslate' is set to true and translation ")
    brand_logo_asset_id: Optional[str] = Field(None, alias="brandLogoAssetId", description="The identifier of image/video asset from the store's asset library")
    headline: Optional[str] = Field(None, description="If 'consentToTranslate' is set to true and translation is SUCCESSFUL then `headline` will return the translated headline")

    model_config = {'populate_by_name': True}


class SBInsightsKeywordAlertType(StrEnum):
    LOW_KEYWORD_TRAFFIC = "LOW_KEYWORD_TRAFFIC"
    LOW_BID = "LOW_BID"


class SBInsightsMatchType(StrEnum):
    EXACT = "EXACT"
    PHRASE = "PHRASE"
    BROAD = "BROAD"


class SBInsightsKeywordInsight(BaseModel):
    """Insights for keywords selected for targeting."""
    alerts: Optional[list["SBInsightsKeywordAlertType"]] = None
    search_term_impression_share: Optional[float] = Field(None, alias="searchTermImpressionShare", description="The account-level ad-attributed impression share for the search-term / keyword. Provides percentage share of all ad impr")
    match_type: Optional["SBInsightsMatchType"] = Field(None, alias="matchType")
    ad_group_index: Optional[int] = Field(None, alias="adGroupIndex", description="Correlates the ad group to the ad group array index specified in the request. Zero-based.")
    search_term_impression_rank: Optional[int] = Field(None, alias="searchTermImpressionRank", description="The account-level ad-attributed impression rank for the search-term / keyword. Provides the [1:N] place the advertiser r")
    bid: Optional[float] = Field(None, description="The associated bid. Note that this value must be less than the budget associated with the Advertiser account. For more i")
    keyword_index: Optional[int] = Field(None, alias="keywordIndex", description="Correlates the keyword to the keyword array index specified in the request. Zero-based.")
    keyword_text: Optional[str] = Field(None, alias="keywordText", description="The keyword text. Maximum of 10 words.")

    model_config = {'populate_by_name': True}


class SBInsightsObject(BaseModel):
    pass


class AssociatedCampaign(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="The campaign identifier.")
    rule_status: str = Field(..., alias="ruleStatus", description="The budget rule evaluation status for this campaign. Read-only.")
    campaign_name: str = Field(..., alias="campaignName", description="The campaign name.")

    model_config = {'populate_by_name': True}


class SBGetAssociatedCampaignsResponse(BaseModel):
    associated_campaigns: Optional[list["AssociatedCampaign"]] = Field(None, alias="associatedCampaigns", description="A list of campaigns that are associated to this budget rule.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` ")

    model_config = {'populate_by_name': True}


class TaskIdFilter(BaseModel):
    include: Optional[list[str]] = None

    model_config = {'populate_by_name': True}


class OptimizationRuleToEntityMappingSuccessResponseItem(BaseModel):
    entity_type: str = Field(..., alias="entityType")
    index: float = Field(..., description="The index of the entityId/optimizationId in the array from the request body.")
    entity_id: str = Field(..., alias="entityId", description="Entity object identifier.")
    optimization_rule_id: str = Field(..., alias="optimizationRuleId", description="The identifier of the optimization rule.")

    model_config = {'populate_by_name': True}


class OptimizationRulesError(BaseModel):
    code: str = Field(..., description="The type of the error.")
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class OptimizationRuleFailureResponseItem(BaseModel):
    index: float = Field(..., description="the index of the optimization rule id/entity Id in the array from the request body.")
    errors: Optional[list["OptimizationRulesError"]] = Field(None, description="A list of validation errors")

    model_config = {'populate_by_name': True}


class BulkDisassociationsOptimizationRuleResponse(BaseModel):
    success: Optional[list["OptimizationRuleToEntityMappingSuccessResponseItem"]] = None
    error: Optional[list["OptimizationRuleFailureResponseItem"]] = None

    model_config = {'populate_by_name': True}


class DisassociateSponsoredBrandsOptimizationRulesResponseContent(BaseModel):
    optimization_rule_disassociations: "BulkDisassociationsOptimizationRuleResponse" = Field(..., alias="optimizationRuleDisassociations")

    model_config = {'populate_by_name': True}


class AdMutationErrorSelector(BaseModel):
    range_error: Optional["RangeError"] = Field(None, alias="rangeError")
    other_error: Optional["OtherError"] = Field(None, alias="otherError")

    model_config = {'populate_by_name': True}


class AdMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error.")
    error_value: "AdMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class AdFailureResponseItem(BaseModel):
    index: float = Field(..., description="the index of the ad in the array from the request body.")
    errors: Optional[list["AdMutationError"]] = Field(None, description="A list of validation errors.")

    model_config = {'populate_by_name': True}


class AdSuccessResponseItem(BaseModel):
    ad_id: Optional[str] = Field(None, alias="adId", description="the Ad ID.")
    ad: Optional["MultiAdGroupAd"] = None
    index: float = Field(..., description="The index in the original list from the request.")

    model_config = {'populate_by_name': True}


class BulkAdOperationResponse(BaseModel):
    success: Optional[list["AdSuccessResponseItem"]] = None
    error: Optional[list["AdFailureResponseItem"]] = None

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsProductCollectionAdsBetaResponseContent(BaseModel):
    ads: Optional["BulkAdOperationResponse"] = None

    model_config = {'populate_by_name': True}


class AsinPolicyViolationType(StrEnum):
    WARNING = "WARNING"
    REJECTED = "REJECTED"


class AsinPolicyViolation(BaseModel):
    policy_description: Optional[str] = Field(None, alias="policyDescription", description="A human-readable description of the policy.")
    name: Optional[str] = Field(None, description="A policy violation code.")
    type_: Optional[AsinPolicyViolationType] = Field(None, alias="type", description="Type of policy violation.")
    policy_link_url: Optional[str] = Field(None, alias="policyLinkUrl", description="Address of the policy documentation. Follow the link to learn more about the specified policy.")

    model_config = {'populate_by_name': True}


class LandingPageInternalErrorCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class SPRuleType(StrEnum):
    SCHEDULE = "SCHEDULE"
    PERFORMANCE = "PERFORMANCE"


class SPBudgetRuleDetails(BaseModel):
    """Object representing details of a budget rule for SP campaign"""
    duration: Optional["RuleDuration"] = None
    recurrence: Optional["Recurrence"] = None
    rule_type: Optional["SPRuleType"] = Field(None, alias="ruleType")
    budget_increase_by: Optional["budgetIncreaseBy"] = Field(None, alias="budgetIncreaseBy")
    name: Optional[str] = Field(None, description="The budget rule name. Required to be unique within a campaign.")
    performance_measure_condition: Optional["PerformanceMeasureCondition"] = Field(None, alias="performanceMeasureCondition")

    model_config = {'populate_by_name': True}


class CreateSPBudgetRulesRequest(BaseModel):
    budget_rules_details: Optional[list["SPBudgetRuleDetails"]] = Field(None, alias="budgetRulesDetails", description="A list of budget rule details.")

    model_config = {'populate_by_name': True}


class TextEvidencePosition(BaseModel):
    """Position in the textComponent where the policy violation is detected."""
    start: Optional[int] = Field(None, description="Zero-based index into the text in textComponent where the text specified in violatingText starts.")
    end: Optional[int] = Field(None, description="Zero-based index into the text in textComponent where the text specified in violatingText ends.")

    model_config = {'populate_by_name': True}


class TextEvidence(BaseModel):
    """Structure of a text evidence"""
    violating_text: Optional[str] = Field(None, alias="violatingText", description="The specific text determined to violate the specified policy in reviewedText.")
    position: Optional["TextEvidencePosition"] = Field(None, description="Position in the textComponent where the policy violation is detected.")

    model_config = {'populate_by_name': True}


class TextPolicyViolationType(StrEnum):
    WARNING = "WARNING"
    REJECTED = "REJECTED"


class TextPolicyViolation(BaseModel):
    """Structure of policy violation for a text component"""
    policy_description: Optional[str] = Field(None, alias="policyDescription", description="A human-readable description of the policy.")
    name: Optional[str] = Field(None, description="A policy violation code.")
    type_: Optional[TextPolicyViolationType] = Field(None, alias="type", description="Type of policy violation.")
    policy_link_url: Optional[str] = Field(None, alias="policyLinkUrl", description="Address of the policy documentation. Follow the link to learn more about the specified policy.")
    text_evidences: Optional[list["TextEvidence"]] = Field(None, alias="textEvidences", description="List of text evidences")

    model_config = {'populate_by_name': True}


class TextComponentResponsePremoderationstatus(StrEnum):
    REJECTED = "REJECTED"
    APPROVED = "APPROVED"
    FAILED = "FAILED"
    RETRYABLE_FAILURE = "RETRYABLE_FAILURE"


class TextComponentResponseComponenttype(StrEnum):
    HEADLINE = "HEADLINE"
    BRAND_NAME = "BRAND_NAME"
    OTHER_TEXT = "OTHER_TEXT"


class TextComponentResponse(BaseModel):
    """Pre moderation result for a text component"""
    pre_moderation_status: Optional[TextComponentResponsePremoderationstatus] = Field(None, alias="preModerationStatus", description="The pre moderation status of the component.")
    component_type: Optional[TextComponentResponseComponenttype] = Field(None, alias="componentType", description="Type of the text component.")
    corrections: Optional[list[str]] = Field(None, description="A list of corrected text without any policy violation. You could consider replacing the component with one of the correc")
    policy_violations: Optional[list["TextPolicyViolation"]] = Field(None, alias="policyViolations", description="A list of policy violations for the component that were detected during pre moderation. Note that this field is present ")
    id_: Optional[str] = Field(None, alias="id", description="Id of the component. This is the same id sent as part of the request. This can be used to uniquely identify the componen")
    text: Optional[str] = Field(None, description="Text which got pre moderated.")

    model_config = {'populate_by_name': True}


class CreateProductCollectionCreative(BaseModel):
    brand_logo_crop: Optional["BrandLogoCrop"] = Field(None, alias="brandLogoCrop")
    asins: Optional[list[str]] = None
    brand_name: Optional[str] = Field(None, alias="brandName")
    custom_image_asset_id: Optional[str] = Field(None, alias="customImageAssetId")
    custom_image_crop: Optional["CustomImageCrop"] = Field(None, alias="customImageCrop")
    brand_logo_asset_id: Optional[str] = Field(None, alias="brandLogoAssetID")
    headline: Optional[str] = Field(None, description="The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maxi")

    model_config = {'populate_by_name': True}


class Ad(BaseModel):
    ad_id: Optional[str] = Field(None, alias="adId", description="The ad identifier. Note: Ads created using version 3/non-multi ad group campaigns do not have an associated adId. [Learn")
    campaign_id: str = Field(..., alias="campaignId", description="The campaign identifier.")
    landing_page: Optional["LandingPage"] = Field(None, alias="landingPage")
    name: Optional[str] = Field(None, description="The name of the ad. Note: Ads created using version 3/non-multi ad group campaigns do not have an associated name. [Lear")
    state: "EntityState"
    ad_group_id: str = Field(..., alias="adGroupId", description="The adGroup identifier.")
    creative: Optional["Creative"] = None
    extended_data: Optional["AdExtendedData"] = Field(None, alias="extendedData")

    model_config = {'populate_by_name': True}


class UpdateAd(BaseModel):
    ad_id: str = Field(..., alias="adId", description="The product ad identifier.")
    name: Optional[str] = Field(None, description="The name of the ad.")
    state: Optional["CreateOrUpdateEntityState"] = None

    model_config = {'populate_by_name': True}


class SBInsightsAdFormat(StrEnum):
    PRODUCT_COLLECTION = "PRODUCT_COLLECTION"
    STORE_SPOTLIGHT = "STORE_SPOTLIGHT"
    VIDEO = "VIDEO"
    BRAND_VIDEO = "BRAND_VIDEO"


class SBInsightsKeyword(BaseModel):
    """Keyword associated with the campaign."""
    match_type: "SBInsightsMatchType" = Field(..., alias="matchType")
    bid: float = Field(..., description="The associated bid. Note that this value must be less than the budget associated with the Advertiser account. For more i")
    keyword_text: str = Field(..., alias="keywordText", description="The keyword text. Maximum of 10 words.")

    model_config = {'populate_by_name': True}


class SBInsightsAdGroup(BaseModel):
    """The ad group settings."""
    keywords: Optional[list["SBInsightsKeyword"]] = None
    ad_format: "SBInsightsAdFormat" = Field(..., alias="adFormat")

    model_config = {'populate_by_name': True}


class SBInsightsCampaignInsightsRequestContent(BaseModel):
    ad_groups: list["SBInsightsAdGroup"] = Field(..., alias="adGroups")

    model_config = {'populate_by_name': True}


class MediaType(StrEnum):
    IMAGE_JPEG = "image/jpeg"
    IMAGE_PNG = "image/png"
    IMAGE_GIF = "image/gif"


class CreativeImageRecommendationEntry(BaseModel):
    score: Optional[float] = Field(None, description="Recommendations with higher values are more relevant")
    size_in_bytes: Optional[float] = Field(None, alias="sizeInBytes", description="The asset size in bytes")
    asset_id: Optional[str] = Field(None, alias="assetId", description="The identifier of image/video asset from the store's asset library")
    image_url: Optional[str] = Field(None, alias="imageUrl", description="The URL of the asset")
    width: Optional[float] = Field(None, description="The width of the asset in pixels")
    name: Optional[str] = Field(None, description="The fileName of the asset")
    content_type: Optional["MediaType"] = Field(None, alias="contentType")
    height: Optional[float] = Field(None, description="The height of the asset in pixels")

    model_config = {'populate_by_name': True}


class Submitted(BaseModel):
    index: Optional[float] = Field(None, description="The index of the image task in the array from the request body")
    task_id: Optional[str] = Field(None, alias="taskId", description="The identifier of image generation task")

    model_config = {'populate_by_name': True}


class ErrorDetails(BaseModel):
    error_message: Optional[str] = Field(None, alias="errorMessage")
    index: Optional[float] = Field(None, description="The index of the image task in the array from the request body")
    error_code: Optional[str] = Field(None, alias="errorCode")

    model_config = {'populate_by_name': True}


class SubmitImageTasksResponseContent(BaseModel):
    submitted: Optional[list["Submitted"]] = None
    batch_id: Optional[str] = Field(None, alias="batchId", description="As per API First guidance, batch API should return a separate list for success and errors in the response. The success/s")
    error: Optional[list["ErrorDetails"]] = None

    model_config = {'populate_by_name': True}


class CreativeRecommendationsEligibilityRequestContent(BaseModel):
    source: "Source"

    model_config = {'populate_by_name': True}


class UpdateAdGroup(BaseModel):
    name: Optional[str] = Field(None, description="The name of the ad group.")
    state: Optional["CreateOrUpdateEntityState"] = None
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the keyword.")

    model_config = {'populate_by_name': True}


class UpdateSponsoredBrandsAdGroupsBetaRequestContent(BaseModel):
    ad_groups: list["UpdateAdGroup"] = Field(..., alias="adGroups")

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsExtendedProductCollectionAdsResponseContent(BaseModel):
    ads: Optional["BulkAdOperationResponse"] = None

    model_config = {'populate_by_name': True}


class InternalServerErrorCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class VersionId(BaseModel):
    """The version identifier that helps to keep track of multiple versions of a submitted ad. In case of Sponsored Brands this is the creative version id."""
    pass


class SBInsightsCampaignInsightsResponseContent(BaseModel):
    """Response object for /sb/campaigns/insights containing a list of insights for the campaign."""
    insights: Optional[list["SBInsightsObject"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken", description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results,")

    model_config = {'populate_by_name': True}


class TextPosition(BaseModel):
    start: Optional[int] = Field(None, description="Zero-based index into the text in reviewedText where the text specified in violatingText starts.")
    end: Optional[int] = Field(None, description="Zero-based index into the text in reviewedText where the text specified in violatingText ends.")

    model_config = {'populate_by_name': True}


class ViolatingTextEvidence(BaseModel):
    violating_text_position: Optional["TextPosition"] = Field(None, alias="violatingTextPosition")
    violating_text: Optional[str] = Field(None, alias="violatingText", description="The specific text determined to violate the specified policy in reviewedText.")

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsVideoAdsBetaResponseContent(BaseModel):
    ads: Optional["BulkAdOperationResponse"] = None

    model_config = {'populate_by_name': True}


class BudgetUsagePortfolio(BaseModel):
    budget_usage_percent: Optional[float] = Field(None, alias="budgetUsagePercent", description="Budget usage percentage (spend / available budget) for the given budget policy.")
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="ID of requested resource")
    usage_updated_timestamp: Optional[str] = Field(None, alias="usageUpdatedTimestamp", description="Last evaluation time for budget usage")
    index: Optional[float] = Field(None, description="An index to maintain order of the portfolioIds")
    budget: Optional[float] = Field(None, description="Budget amount of resource requested")

    model_config = {'populate_by_name': True}


class ValueTypeRuleCriteria(BaseModel):
    comparison_operator: Optional[str] = Field(None, alias="comparisonOperator", description="Enum: 'LESS_THAN_OR_EQUAL_TO'  The comparison operator.")
    value: Optional[float] = Field(None, description="The value of the threshold associated with the attribute.")

    model_config = {'populate_by_name': True}


class RuleCondition(BaseModel):
    criteria: "ValueTypeRuleCriteria"
    attribute_name: str = Field(..., alias="attributeName", description="Enum: 'COST_PER_CLICK'  The name of the attribute.   Supported rule metrics and corresponding supported comparisonOperat")

    model_config = {'populate_by_name': True}


class OptimizationRule(BaseModel):
    optimization_rule_id: Optional[str] = Field(None, alias="optimizationRuleId", description="The identifier of the optimization rule.")
    conditions: Optional[list["RuleCondition"]] = None

    model_config = {'populate_by_name': True}


class CreateOptimizationRuleSuccessResponseItem(BaseModel):
    optimization_rule: "OptimizationRule" = Field(..., alias="optimizationRule")
    entity_type: str = Field(..., alias="entityType")
    index: float = Field(..., description="The index of the entityId in the array from the request body.")
    entity_id: str = Field(..., alias="entityId", description="Entity object identifier.")
    optimization_rule_id: str = Field(..., alias="optimizationRuleId", description="The identifier of the optimization rule.")

    model_config = {'populate_by_name': True}


class BulkCreateOptimizationRuleOperationResponse(BaseModel):
    success: Optional[list["CreateOptimizationRuleSuccessResponseItem"]] = None
    error: Optional[list["OptimizationRuleFailureResponseItem"]] = None

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsOptimizationRulesResponseContent(BaseModel):
    optimization_rules: "BulkCreateOptimizationRuleOperationResponse" = Field(..., alias="optimizationRules")

    model_config = {'populate_by_name': True}


class UpdateSponsoredBrandsAdGroupsRequestContent(BaseModel):
    ad_groups: list["UpdateAdGroup"] = Field(..., alias="adGroups")

    model_config = {'populate_by_name': True}


class SBRuleType(StrEnum):
    SCHEDULE = "SCHEDULE"
    PERFORMANCE = "PERFORMANCE"


class PerformanceMetricForSB(StrEnum):
    IS = "IS"
    NTB = "NTB"
    ROAS = "ROAS"


class PerformanceMeasureConditionForSB(BaseModel):
    metric_name: "PerformanceMetricForSB" = Field(..., alias="metricName")
    comparison_operator: "ComparisonOperator" = Field(..., alias="comparisonOperator")
    threshold: float = Field(..., description="The performance threshold value.")

    model_config = {'populate_by_name': True}


class SBBudgetRuleDetails(BaseModel):
    duration: Optional["RuleDuration"] = None
    recurrence: Optional["Recurrence"] = None
    rule_type: Optional["SBRuleType"] = Field(None, alias="ruleType")
    budget_increase_by: Optional["budgetIncreaseBy"] = Field(None, alias="budgetIncreaseBy")
    name: Optional[str] = Field(None, description="The budget rule name. Required to be unique within a campaign.")
    performance_measure_condition: Optional["PerformanceMeasureConditionForSB"] = Field(None, alias="performanceMeasureCondition")

    model_config = {'populate_by_name': True}


class SBCampaignBudgetRule(BaseModel):
    rule_state: Optional["state"] = Field(None, alias="ruleState")
    last_updated_date: Optional[float] = Field(None, alias="lastUpdatedDate", description="Epoch time of budget rule update. Read-only.")
    created_date: Optional[float] = Field(None, alias="createdDate", description="Epoch time of budget rule creation. Read-only.")
    rule_details: Optional["SBBudgetRuleDetails"] = Field(None, alias="ruleDetails")
    rule_id: str = Field(..., alias="ruleId", description="The budget rule identifier.")
    rule_status: Optional[str] = Field(None, alias="ruleStatus", description="The budget rule evaluation status. Read-only.")

    model_config = {'populate_by_name': True}


class SBListAssociatedBudgetRulesResponse(BaseModel):
    associated_rules: Optional[list["SBCampaignBudgetRule"]] = Field(None, alias="associatedRules", description="A list of associated budget rules.")

    model_config = {'populate_by_name': True}


class SBTargetingAgeRange(BaseModel):
    age_range_refinement_id: str = Field(..., alias="ageRangeRefinementId", description="Id of Age Range. Use /sb/targets/categories/{categoryRefinementId}/refinements to retrieve Age Range Refinement IDs.")
    name: Optional[str] = Field(None, description="Name of Age Range.")
    translated_name: Optional[str] = Field(None, alias="translatedName", description="Translated name of Age Range based off locale sent in request.")

    model_config = {'populate_by_name': True}


class DatePolicyViolationType(StrEnum):
    WARNING = "WARNING"
    REJECTED = "REJECTED"


class DatePolicyViolation(BaseModel):
    policy_description: Optional[str] = Field(None, alias="policyDescription", description="A human-readable description of the policy.")
    name: Optional[str] = Field(None, description="A policy violation code.")
    type_: Optional[DatePolicyViolationType] = Field(None, alias="type", description="Type of policy violation.")
    policy_link_url: Optional[str] = Field(None, alias="policyLinkUrl", description="Address of the policy documentation. Follow the link to learn more about the specified policy.")

    model_config = {'populate_by_name': True}


class TextRecommendation(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="Unique ID for generated recommendation.")
    value: Optional[str] = Field(None, description="Recommendation value.")

    model_config = {'populate_by_name': True}


class TextRecommendations(BaseModel):
    """Ordered list of recommendations in each group."""
    pass


class PrimaryHeadlineRecommendationGroups(BaseModel):
    """Ordered list of Primary Headline recommendation groups."""
    pass


class ViolatingTextContent(BaseModel):
    """Information about the specific text that violates the specified policy in the campaign."""
    reviewed_text: Optional[str] = Field(None, alias="reviewedText", description="The actual text on which the moderation was done.")
    violating_text_evidences: Optional[list["ViolatingTextEvidence"]] = Field(None, alias="violatingTextEvidences")
    moderated_component: Optional[str] = Field(None, alias="moderatedComponent", description="Moderation component which marked the policy violation.")

    model_config = {'populate_by_name': True}


class SuggestedHeadline(BaseModel):
    """Suggested Headline in response object."""
    headline_id: Optional[str] = Field(None, alias="headlineId", description="Unique Id of suggested headline.")
    headline: Optional[str] = Field(None, description="String that contains suggested headline.")

    model_config = {'populate_by_name': True}


class ThrottlingErrorCode(StrEnum):
    THROTTLED = "THROTTLED"


class ThrottlingErrorResponseContent(BaseModel):
    code: "ThrottlingErrorCode"
    request_id: str = Field(..., alias="requestId")
    message: str

    model_config = {'populate_by_name': True}


class LandingPageInvalidArgumentErrorCode(StrEnum):
    INVALID_ARGUMENT = "INVALID_ARGUMENT"


class LandingPageInvalidArgumentExceptionResponseContent(BaseModel):
    code: "LandingPageInvalidArgumentErrorCode"
    details: str = Field(..., description="A human-readable description of the code field.")

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsCampaignsResponseContent(BaseModel):
    campaigns: Optional["BulkCampaignOperationResponse"] = None

    model_config = {'populate_by_name': True}


class AdGroupFailureResponseItem(BaseModel):
    index: float = Field(..., description="the index of the adGroup in the array from the request body.")
    errors: Optional[list["AdGroupMutationError"]] = Field(None, description="A list of validation errors.")

    model_config = {'populate_by_name': True}


class CreateCampaign(BaseModel):
    budget_type: "BudgetType" = Field(..., alias="budgetType")
    brand_entity_id: Optional[str] = Field(None, alias="brandEntityId", description="Please note that brandEntityId is only required for sellers. You can get the brandEntityId by calling the [GET /brands](")
    goal: Optional[str] = Field(None, description="Goal will allow you to set goal type to help drive your campaign performance. If no goal is selected then it will defaul")
    bidding: Optional["Bidding"] = None
    end_date: Optional[str] = Field(None, alias="endDate", description="endDate is optional. If endDate is specified, startDate must be specified as well.")
    product_location: Optional["ProductLocation"] = Field(None, alias="productLocation")
    tags: Optional["Tags"] = None
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="The identifier of an existing portfolio to which the campaign is associated.")
    cost_type: Optional[str] = Field(None, alias="costType", description="The costType can be set to determines how the campaign will bid and charge. To view the bid maximums and minimums by geo")
    smart_default: Optional[list[str]] = Field(None, alias="smartDefault", description="The smartDefault specifies a list of the smart default options for the campaign.  `smartDefault` is optional for create ")
    name: str = Field(..., description="The name of the campaign.")
    state: "CreateOrUpdateEntityState"
    start_date: Optional[str] = Field(None, alias="startDate", description="startDate is optional. If startDate is not specified, current date will be used.")
    budget: float = Field(..., description="The budget of the campaign.")
    site_restrictions: Optional[list["SiteRestriction"]] = Field(None, alias="siteRestrictions", description="Restrict the ad to a particular site. siteRestrictions is an optional field.  If this field is not set, ads from the cam")
    targeted_pg_deal_id: Optional[str] = Field(None, alias="targetedPGDealId", description="DealId associated with the campaign.")

    model_config = {'populate_by_name': True}


class LandingPageInternalServerExceptionResponseContent(BaseModel):
    code: "LandingPageInternalErrorCode"
    details: str = Field(..., description="A human-readable description of the code field.")

    model_config = {'populate_by_name': True}


class AsinComponentComponenttype(StrEnum):
    LANDING_ASIN = "LANDING_ASIN"
    PRODUCT_ASIN = "PRODUCT_ASIN"


class AsinComponent(BaseModel):
    """Asin component which needs to be pre moderated."""
    component_type: AsinComponentComponenttype = Field(..., alias="componentType", description="Type of the asin component.")
    asin: str = Field(..., description="Asin id to be pre moderated.")
    id_: str = Field(..., alias="id", description="Id of the component. The same will be returned as part of the response as well. This can be used to uniquely identify th")

    model_config = {'populate_by_name': True}


class ListSponsoredBrandsAdGroupsBetaRequestContent(BaseModel):
    campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    state_filter: Optional["EntityStateFilter"] = Field(None, alias="stateFilter")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    ad_group_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    include_extended_data_fields: Optional[bool] = Field(None, alias="includeExtendedDataFields", description="Setting to true will slow down performance because the API needs to retrieve extra information for each campaign.")
    name_filter: Optional["NameFilter"] = Field(None, alias="nameFilter")

    model_config = {'populate_by_name': True}


class SBBudgetRule(BaseModel):
    rule_state: Optional["state"] = Field(None, alias="ruleState")
    last_updated_date: Optional[float] = Field(None, alias="lastUpdatedDate", description="Epoch time of budget rule update. Read-only.")
    created_date: Optional[float] = Field(None, alias="createdDate", description="Epoch time of budget rule creation. Read-only.")
    rule_details: Optional["SBBudgetRuleDetails"] = Field(None, alias="ruleDetails")
    rule_id: str = Field(..., alias="ruleId", description="The budget rule identifier.")
    rule_status: Optional[str] = Field(None, alias="ruleStatus", description="The budget rule status. Read-only.")

    model_config = {'populate_by_name': True}


class SBInsightsUnprocessableEntityExceptionResponseContent(BaseModel):
    """Returns information about an UnprocessableEntityException."""
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsCampaignsBetaRequestContent(BaseModel):
    campaigns: list["CreateCampaign"]

    model_config = {'populate_by_name': True}


class InternalServerErrorResponseContent(BaseModel):
    code: "InternalServerErrorCode"
    request_id: str = Field(..., alias="requestId")
    message: str

    model_config = {'populate_by_name': True}


class GetSBBudgetRulesForAdvertiserResponse(BaseModel):
    budget_rules_for_advertiser_response: Optional[list["SBBudgetRule"]] = Field(None, alias="budgetRulesForAdvertiserResponse", description="A list of rules created by the advertiser.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` ")

    model_config = {'populate_by_name': True}


class UpdateOptimizationRuleSuccessResponseItem(BaseModel):
    optimization_rule: "OptimizationRule" = Field(..., alias="optimizationRule")
    index: float = Field(..., description="The index of the entityId in the array from the request body.")
    optimization_rule_id: str = Field(..., alias="optimizationRuleId", description="The identifier of the optimization rule.")

    model_config = {'populate_by_name': True}


class VideoEvidence(BaseModel):
    """Structure of a video evidence"""
    start: Optional[int] = Field(None, description="The start position (in seconds) of the content that violates the specified policy within the video.")
    end: Optional[int] = Field(None, description="The end position (in seconds) of the content that violates the specified policy within the video.")

    model_config = {'populate_by_name': True}


class VideoPolicyViolationType(StrEnum):
    WARNING = "WARNING"
    REJECTED = "REJECTED"


class VideoPolicyViolation(BaseModel):
    """Structure of policy violation for a video component"""
    policy_description: Optional[str] = Field(None, alias="policyDescription", description="A human-readable description of the policy.")
    video_evidences: Optional[list["VideoEvidence"]] = Field(None, alias="videoEvidences", description="List of evidences for the policy violations detected on the video component.")
    name: Optional[str] = Field(None, description="A policy violation code.")
    type_: Optional[VideoPolicyViolationType] = Field(None, alias="type", description="Type of policy violation.")
    policy_link_url: Optional[str] = Field(None, alias="policyLinkUrl", description="Address of the policy documentation. Follow the link to learn more about the specified policy.")

    model_config = {'populate_by_name': True}


class VideoComponentResponsePremoderationstatus(StrEnum):
    REJECTED = "REJECTED"
    APPROVED = "APPROVED"
    FAILED = "FAILED"
    RETRYABLE_FAILURE = "RETRYABLE_FAILURE"


class VideoComponentResponseComponenttype(StrEnum):
    SPONSORED_BRANDS_VIDEO = "SPONSORED_BRANDS_VIDEO"
    OTHER_VIDEO = "OTHER_VIDEO"


class VideoComponentResponse(BaseModel):
    """Pre moderation result for a video component"""
    pre_moderation_status: Optional[VideoComponentResponsePremoderationstatus] = Field(None, alias="preModerationStatus", description="The pre moderation status of the component.")
    component_type: Optional[VideoComponentResponseComponenttype] = Field(None, alias="componentType", description="Type of the video component.")
    landing_page: Optional["LandingPage"] = Field(None, alias="landingPage")
    policy_violations: Optional[list["VideoPolicyViolation"]] = Field(None, alias="policyViolations", description="A list of policy violations for the component that were detected during pre moderation. Note that this field is present ")
    id_: Optional[str] = Field(None, alias="id", description="Id of the component. This is the same id sent as part of the request. This can be used to uniquely identify the componen")
    url: Optional[str] = Field(None, description="Publicly accessible url of the video that got pre moderated.")

    model_config = {'populate_by_name': True}


class AsinComponentResponsePremoderationstatus(StrEnum):
    REJECTED = "REJECTED"
    APPROVED = "APPROVED"
    FAILED = "FAILED"
    RETRYABLE_FAILURE = "RETRYABLE_FAILURE"


class AsinComponentResponseComponenttype(StrEnum):
    LANDING_ASIN = "LANDING_ASIN"
    PRODUCT_ASIN = "PRODUCT_ASIN"


class AsinComponentResponse(BaseModel):
    """Pre-moderation result for an Asin component"""
    pre_moderation_status: Optional[AsinComponentResponsePremoderationstatus] = Field(None, alias="preModerationStatus", description="The pre-moderation status of the component.")
    component_type: Optional[AsinComponentResponseComponenttype] = Field(None, alias="componentType", description="Type of Asin component.")
    policy_violations: Optional[list["AsinPolicyViolation"]] = Field(None, alias="policyViolations", description="A list of policy violations for the component that were detected during pre moderation. Note that this field is present ")
    asin: Optional[str] = Field(None, description="Pre-moderated Asin Id.")
    id_: Optional[str] = Field(None, alias="id", description="Id of the component. This is the same id sent as part of the request. This can be used to uniquely identify the componen")

    model_config = {'populate_by_name': True}


class DateComponentResponsePremoderationstatus(StrEnum):
    REJECTED = "REJECTED"
    APPROVED = "APPROVED"
    FAILED = "FAILED"
    RETRYABLE_FAILURE = "RETRYABLE_FAILURE"


class DateComponentResponseComponenttype(StrEnum):
    CAMPAIGN_DATES = "CAMPAIGN_DATES"


class DateComponentResponse(BaseModel):
    """Pre-moderation result for a date component"""
    pre_moderation_status: Optional[DateComponentResponsePremoderationstatus] = Field(None, alias="preModerationStatus", description="The pre-moderation status of the component.")
    component_type: Optional[DateComponentResponseComponenttype] = Field(None, alias="componentType", description="Type of the date component.")
    end_date: Optional[str] = Field(None, alias="endDate", description="End date of the component.")
    policy_violations: Optional[list["DatePolicyViolation"]] = Field(None, alias="policyViolations", description="A list of policy violations for the component that were detected during pre moderation. Note that this field is present ")
    id_: Optional[str] = Field(None, alias="id", description="Id of the component. This is the same id sent as part of the request. This can be used to uniquely identify the componen")
    start_date: Optional[str] = Field(None, alias="startDate", description="Start date of the component.")

    model_config = {'populate_by_name': True}


class ImageEvidence(BaseModel):
    """Structure of a image evidence"""
    top_left_y: Optional[int] = Field(None, alias="topLeftY", description="The top left Y-coordinate of the content that violates the specfied policy within the image.")
    top_left_x: Optional[int] = Field(None, alias="topLeftX", description="The top left X-coordinate of the content that violates the specfied policy within the image.")
    width: Optional[int] = Field(None, description="The width of the content that violates the specfied policy within the image.")
    height: Optional[int] = Field(None, description="The height of the content that violates the specfied policy within the image.")

    model_config = {'populate_by_name': True}


class ImagePolicyViolationType(StrEnum):
    WARNING = "WARNING"
    REJECTED = "REJECTED"


class ImagePolicyViolation(BaseModel):
    """Structure of policy violation for a image component"""
    policy_description: Optional[str] = Field(None, alias="policyDescription", description="A human-readable description of the policy.")
    image_evidences: Optional[list["ImageEvidence"]] = Field(None, alias="imageEvidences", description="List of evidences for the policy violations detected on the image component.")
    name: Optional[str] = Field(None, description="A policy violation code.")
    type_: Optional[ImagePolicyViolationType] = Field(None, alias="type", description="Type of policy violation.")
    policy_link_url: Optional[str] = Field(None, alias="policyLinkUrl", description="Address of the policy documentation. Follow the link to learn more about the specified policy.")
    text_evidences: Optional[list["TextEvidence"]] = Field(None, alias="textEvidences", description="Policy violation on an image can be detected on the ocr detected text on the image as well. This list of text evidences ")

    model_config = {'populate_by_name': True}


class ImageComponentResponsePremoderationstatus(StrEnum):
    REJECTED = "REJECTED"
    APPROVED = "APPROVED"
    FAILED = "FAILED"
    RETRYABLE_FAILURE = "RETRYABLE_FAILURE"


class ImageComponentResponseComponenttype(StrEnum):
    BRAND_LOGO = "BRAND_LOGO"
    CUSTOM_IMAGE = "CUSTOM_IMAGE"
    OTHER_IMAGE = "OTHER_IMAGE"


class ImageComponentResponse(BaseModel):
    """Pre moderation result for a image component"""
    pre_moderation_status: Optional[ImageComponentResponsePremoderationstatus] = Field(None, alias="preModerationStatus", description="The pre moderation status of the component.")
    component_type: Optional[ImageComponentResponseComponenttype] = Field(None, alias="componentType", description="Type of the image component.")
    landing_page: Optional["LandingPage"] = Field(None, alias="landingPage")
    policy_violations: Optional[list["ImagePolicyViolation"]] = Field(None, alias="policyViolations", description="A list of policy violations for the component that were detected during pre moderation. Note that this field is present ")
    id_: Optional[str] = Field(None, alias="id", description="Id of the component. This is the same id sent as part of the request. This can be used to uniquely identify the componen")
    url: Optional[str] = Field(None, description="Publicly accessible url of the image that got pre moderated.")

    model_config = {'populate_by_name': True}


class PreModerationResponseAdprogram(StrEnum):
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_BRANDS_SPOTLIGHT = "SPONSORED_BRANDS_SPOTLIGHT"
    SPONSORED_BRANDS_VIDEO = "SPONSORED_BRANDS_VIDEO"
    STORES = "STORES"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    DSP = "DSP"
    DSP_REC = "DSP_REC"
    DSP_IMAGE = "DSP_IMAGE"
    DSP_THIRD_PARTY = "DSP_THIRD_PARTY"


class PreModerationResponseLocale(StrEnum):
    AR_AE = "ar-AE"
    ZH_CN = "zh-CN"
    NL_NL = "nl-NL"
    EN_AU = "en-AU"
    EN_CA = "en-CA"
    EN_IN = "en-IN"
    EN_GB = "en-GB"
    EN_US = "en-US"
    FR_CA = "fr-CA"
    FR_FR = "fr-FR"
    DE_DE = "de-DE"
    IT_IT = "it-IT"
    JA_JP = "ja-JP"
    KO_KR = "ko-KR"
    PT_BR = "pt-BR"
    ES_ES = "es-ES"
    ES_US = "es-US"
    ES_MX = "es-MX"
    TR_TR = "tr-TR"


class PreModerationResponse(BaseModel):
    """Information regarding the policy violations if present for the components, sent for pre moderation."""
    record_id: Optional[str] = Field(None, alias="recordId", description="Id of the brand/advertiser.")
    asin_components: Optional[list["AsinComponentResponse"]] = Field(None, alias="asinComponents", description="Pre moderation result of the asin components. It will have information regarding the policy violations present if any.")
    pre_moderation_id: Optional[str] = Field(None, alias="preModerationId", description="Unique Id for the moderation Request.")
    ad_program: Optional[PreModerationResponseAdprogram] = Field(None, alias="adProgram", description="Type of Ad program to which the pre moderation components belong to.")
    locale: Optional[PreModerationResponseLocale] = Field(None, description="Locale value that was passed in request.")
    image_components: Optional[list["ImageComponentResponse"]] = Field(None, alias="imageComponents", description="Pre moderation result of the image components. It will have information regarding the policy violations present if any.")
    date_components: Optional[list["DateComponentResponse"]] = Field(None, alias="dateComponents", description="Pre moderation result of the date components. It will have information regarding the policy violations present if any.")
    text_components: Optional[list["TextComponentResponse"]] = Field(None, alias="textComponents", description="Pre moderation result of the text components. It will have information regarding the policy violations present if any.")
    video_components: Optional[list["VideoComponentResponse"]] = Field(None, alias="videoComponents", description="Pre moderation result of the video components. It will have information regarding the policy violations present if any.")

    model_config = {'populate_by_name': True}


class SBTargetingPriceRange(BaseModel):
    """A range of prices. We use this to retrieve the number of targetable ASINs that falls within this price range."""
    min: Optional[float] = None
    max: Optional[float] = None

    model_config = {'populate_by_name': True}


class BudgetRuleResponse(BaseModel):
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the error, if unsuccessful")
    rule_id: Optional[str] = Field(None, alias="ruleId", description="The rule identifier.")
    associated_campaign_ids: Optional[list[str]] = Field(None, alias="associatedCampaignIds")

    model_config = {'populate_by_name': True}


class UpdateBudgetRulesResponse(BaseModel):
    responses: Optional[list["BudgetRuleResponse"]] = None

    model_config = {'populate_by_name': True}


class CreateAdGroup(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign to which the keyword is associated.")
    name: str = Field(..., description="The name of the ad group.")
    state: "CreateOrUpdateEntityState"

    model_config = {'populate_by_name': True}


class CreateProductCollectionAd(BaseModel):
    landing_page: "LandingPage" = Field(..., alias="landingPage")
    name: str = Field(..., description="The name of the ad.")
    state: "CreateOrUpdateEntityState"
    ad_group_id: str = Field(..., alias="adGroupId", description="The adGroup identifier.")
    creative: "CreateProductCollectionCreative"

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsProductCollectionAdsBetaRequestContent(BaseModel):
    ads: list["CreateProductCollectionAd"]

    model_config = {'populate_by_name': True}


class RequiredRecommendationsType(StrEnum):
    PRIMARY_HEADLINE = "PRIMARY_HEADLINE"
    SECONDARY_HEADLINE = "SECONDARY_HEADLINE"


class RequiredRecommendations(BaseModel):
    max_recommendation_groups: Optional[int] = Field(None, alias="maxRecommendationGroups", description="Maximum number of recommendations groups that API should return for given type. (recommendations are not guaranteed).")
    type_: RequiredRecommendationsType = Field(..., alias="type", description="Type of recommendations.")

    model_config = {'populate_by_name': True}


class CreativeRecommendationsAccessDeniedErrorCode(StrEnum):
    ACCESS_DENIED = "ACCESS_DENIED"


class CreativeRecommendationsAccessDeniedError(BaseModel):
    code: Optional[CreativeRecommendationsAccessDeniedErrorCode] = Field(None, description="Access denied error code.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class ListSponsoredBrandsOptimizationRulesResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    total_count: Optional[float] = Field(None, alias="totalCount", description="The total number of entities.")
    optimization_rules: list["OptimizationRule"] = Field(..., alias="optimizationRules")

    model_config = {'populate_by_name': True}


class StorePage(BaseModel):
    display_name: Optional[str] = Field(None, alias="displayName", description="Display Name of the store page shown on a store spotlight campaign.")
    primary_asin: Optional[str] = Field(None, alias="primaryAsin", description="Selected asin from the store page which is displayed on the store spotlight campaign.")

    model_config = {'populate_by_name': True}


class HeadlineSuggestionRequestAdformat(StrEnum):
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_BRANDS_SPOTLIGHT = "SPONSORED_BRANDS_SPOTLIGHT"


class HeadlineSuggestionRequest(BaseModel):
    """Request structure of headline suggestion API."""
    asins: Optional[list[str]] = Field(None, description="An array of ASINs associated with the creative. Note do not pass an empty array, this results in an error.")
    store_pages: Optional[list["StorePage"]] = Field(None, alias="storePages", description="An array of Store Pages associated with SB Spotlight Creative.")
    max_num_suggestions: Optional[float] = Field(None, alias="maxNumSuggestions", description="Maximum number of suggestions that API should return. Response will [0, maxNumSuggestions] suggestions (suggestions are ")
    ad_format: Optional[HeadlineSuggestionRequestAdformat] = Field(None, alias="adFormat")

    model_config = {'populate_by_name': True}


class CostControlMetric(StrEnum):
    COST_PER_CLICK = "COST_PER_CLICK"


class SBOptimizationRecommendationRequestContent(BaseModel):
    cost_control_metric: "CostControlMetric" = Field(..., alias="costControlMetric")
    landing_pages: list["LandingPage"] = Field(..., alias="landingPages")

    model_config = {'populate_by_name': True}


class SBOptimizationRecommendationResponseContent(BaseModel):
    minimum_value: float = Field(..., alias="minimumValue", description="Minimum accepted value for cost control metric.")
    cost_control_metric: "CostControlMetric" = Field(..., alias="costControlMetric")
    recommended_value: float = Field(..., alias="recommendedValue", description="Recommended value for cost control metric.")

    model_config = {'populate_by_name': True}


class DeleteSponsoredBrandsAdsResponseContent(BaseModel):
    ads: Optional["BulkAdOperationResponse"] = None

    model_config = {'populate_by_name': True}


class VideoCreative(BaseModel):
    consent_to_translate: Optional[bool] = Field(None, alias="consentToTranslate", description="If set to true and the heaadline and/or video are not in the marketplace's default language, Amazon will attempt to tran")
    video_asset_ids: list[str] = Field(..., alias="videoAssetIds", description="The assetIds of the original videos submitted by the advertiser. If 'consentToTranslate' is set to true and translation ")

    model_config = {'populate_by_name': True}


class GoalTypeFilter(BaseModel):
    """Filter entities by goal type."""
    include: Optional[list[str]] = None

    model_config = {'populate_by_name': True}


class ListSponsoredBrandsCampaignsBetaRequestContent(BaseModel):
    campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    portfolio_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="portfolioIdFilter")
    state_filter: Optional["EntityStateFilter"] = Field(None, alias="stateFilter")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    goal_type_filter: Optional["GoalTypeFilter"] = Field(None, alias="goalTypeFilter")
    include_extended_data_fields: Optional[bool] = Field(None, alias="includeExtendedDataFields", description="Setting to true will slow down performance because the API needs to retrieve extra information for each campaign.")
    name_filter: Optional["NameFilter"] = Field(None, alias="nameFilter")

    model_config = {'populate_by_name': True}


class BudgetUsageCampaignBatchError(BaseModel):
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="ID of requested resource")
    index: Optional[float] = Field(None, description="An index to maintain order of the campaignIds")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class ShopperSegment(StrEnum):
    NEW_TO_BRAND_PURCHASE = "NEW_TO_BRAND_PURCHASE"


class BidAdjustmentByShopperSegment(BaseModel):
    percentage: Optional[float] = None
    shopper_segment: Optional["ShopperSegment"] = Field(None, alias="shopperSegment")

    model_config = {'populate_by_name': True}


class UpdateOptimizationRule(BaseModel):
    optimization_rule_id: Optional[str] = Field(None, alias="optimizationRuleId", description="The identifier of the optimization rule.")
    conditions: Optional[list["RuleCondition"]] = None

    model_config = {'populate_by_name': True}


class UpdateSponsoredBrandsOptimizationRulesRequestContent(BaseModel):
    optimization_rules: list["UpdateOptimizationRule"] = Field(..., alias="optimizationRules")

    model_config = {'populate_by_name': True}


class SevenDaysMissedOpportunities(BaseModel):
    """Missed Opportunities in the trailing seven days."""
    estimated_missed_sales_lower: Optional[float] = Field(None, alias="estimatedMissedSalesLower", description="Lower bound of the estimated Missed Sales. This will be in local currency.")
    estimated_missed_sales_upper: Optional[float] = Field(None, alias="estimatedMissedSalesUpper", description="Upper bound of the estimated Missed Sales. This will be in local currency.")
    end_date: Optional[str] = Field(None, alias="endDate", description="End date of the Missed Opportunities date range (YYYY-MM-DD) in local time.")
    estimated_missed_impressions_lower: Optional[float] = Field(None, alias="estimatedMissedImpressionsLower", description="Lower bound of the estimated Missed Impressions.")
    estimated_missed_clicks_lower: Optional[float] = Field(None, alias="estimatedMissedClicksLower", description="Lower bound of the estimated Missed Clicks.")
    estimated_missed_clicks_upper: Optional[float] = Field(None, alias="estimatedMissedClicksUpper", description="Upper bound of the estimated Missed Clicks.")
    estimated_missed_impressions_upper: Optional[float] = Field(None, alias="estimatedMissedImpressionsUpper", description="Upper bound of the estimated Missed Impressions.")
    start_date: Optional[str] = Field(None, alias="startDate", description="Start date of the Missed Opportunities date range (YYYY-MM-DD) in local time.")
    percent_time_in_budget: Optional[float] = Field(None, alias="percentTimeInBudget", description="Percentage of time the campaign is active with a budget.")

    model_config = {'populate_by_name': True}


class BudgetRecommendation(BaseModel):
    """Budget recomendation for campagins."""
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of a campaign.")
    suggested_budget: float = Field(..., alias="suggestedBudget", description="Recommended budget for the campaign.")
    index: float = Field(..., description="Correlate the recommendation to the campaign index in the request. Zero-based.")
    seven_days_missed_opportunities: "SevenDaysMissedOpportunities" = Field(..., alias="sevenDaysMissedOpportunities")

    model_config = {'populate_by_name': True}


class BudgetRecommendationError(BaseModel):
    """Error that occurred when generating budget recommendations."""
    code: str = Field(..., description="A human-readable description of the enumerated response code in the `code` field.")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of a campaign.")
    index: float = Field(..., description="Correlate the recommendation to the campaign index in the request. Zero-based.")
    details: str = Field(..., description="An enumerated response code.")

    model_config = {'populate_by_name': True}


class GetBudgetRecommendationsResponseContent(BaseModel):
    success: list["BudgetRecommendation"] = Field(..., description="List of successful budget recommendations for campaigns.")
    error: list["BudgetRecommendationError"] = Field(..., description="List of errors that occurred when generating budget recommendations.")

    model_config = {'populate_by_name': True}


class CreateSDBudgetRulesRequest(BaseModel):
    budget_rules_details: Optional[list["SDBudgetRuleDetails"]] = Field(None, alias="budgetRulesDetails", description="A list of budget rule details.")

    model_config = {'populate_by_name': True}


class SDHeadlineRecommendationAccessDeniedExceptionCode(StrEnum):
    ACCESS_DENIED = "ACCESS_DENIED"


class SDHeadlineRecommendationAccessDeniedException(BaseModel):
    code: Optional[SDHeadlineRecommendationAccessDeniedExceptionCode] = Field(None, description="AccessDeniedErrorCode.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class ViolatingAsinEvidence(BaseModel):
    asin: Optional[str] = Field(None, description="ASIN which has the ad policy violation.")

    model_config = {'populate_by_name': True}


class ViolatingAsinContent(BaseModel):
    violating_asin_evidences: Optional[list["ViolatingAsinEvidence"]] = Field(None, alias="violatingAsinEvidences")
    moderated_component: Optional[str] = Field(None, alias="moderatedComponent", description="Moderation component which marked the policy violation.")

    model_config = {'populate_by_name': True}


class CreateStoreSpotlightCreative(BaseModel):
    brand_logo_crop: Optional["BrandLogoCrop"] = Field(None, alias="brandLogoCrop")
    brand_name: Optional[str] = Field(None, alias="brandName")
    subpages: Optional[list["Subpage"]] = None
    consent_to_translate: Optional[bool] = Field(None, alias="consentToTranslate", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    creative_properties_to_optimize: Optional[list["CreativePropertyToOptimize"]] = Field(None, alias="creativePropertiesToOptimize", description="If this property is enabled, Sponsored Brands will dynamically optimize by enhancing or generating creative properties b")
    brand_logo_asset_id: Optional[str] = Field(None, alias="brandLogoAssetID")
    headline: Optional[str] = Field(None, description="The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maxi")

    model_config = {'populate_by_name': True}


class CreateStoreSpotlightAd(BaseModel):
    landing_page: "LandingPage" = Field(..., alias="landingPage")
    name: str = Field(..., description="The name of the ad.")
    state: "CreateOrUpdateEntityState"
    ad_group_id: str = Field(..., alias="adGroupId", description="The adGroup identifier.")
    creative: "CreateStoreSpotlightCreative"

    model_config = {'populate_by_name': True}


class UpdateSponsoredBrandsAdsBetaRequestContent(BaseModel):
    ads: list["UpdateAd"]

    model_config = {'populate_by_name': True}


class IdType(StrEnum):
    AD_ID = "AD_ID"


class SBInsightsThrottlingExceptionResponseContent(BaseModel):
    """Returns information about a ThrottlingException."""
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class BrandLogo(BaseModel):
    """Properties associated with Brand Logo."""
    brand_logo_crop: Optional["AssetCrop"] = Field(None, alias="brandLogoCrop")
    brand_logo_url: Optional[str] = Field(None, alias="brandLogoUrl")
    brand_logo_asset_id: Optional[str] = Field(None, alias="brandLogoAssetId", description="The identifier of image/video asset from the store's asset library")

    model_config = {'populate_by_name': True}


class ListCreativesResultEntry(BaseModel):
    """----------------------------------------------- Structure types ----------------------------------------------- Creative"""
    ad_id: Optional[str] = Field(None, alias="adId", description="The unique ID of a Sponsored Brands ad.")
    creation_time: Optional[float] = Field(None, alias="creationTime")
    creative_type: Optional["CreativeType"] = Field(None, alias="creativeType")
    creative_version: Optional[str] = Field(None, alias="creativeVersion", description="The version identifier that helps you keep track of multiple versions of a submitted (non-draft) Sponsored Brands creati")
    creative_status: Optional["CreativeStatus"] = Field(None, alias="creativeStatus")
    creative_properties: Optional["CreativeProperties"] = Field(None, alias="creativeProperties")
    last_update_time: Optional[float] = Field(None, alias="lastUpdateTime")

    model_config = {'populate_by_name': True}


class ListCreativesResponseContent(BaseModel):
    total_results: Optional[float] = Field(None, alias="totalResults", description="The total number of results returned by an operation.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results,")
    creatives: Optional[list["ListCreativesResultEntry"]] = Field(None, description="A list of creatives")

    model_config = {'populate_by_name': True}


class DeleteSponsoredBrandsAdsRequestContent(BaseModel):
    ad_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="adIdFilter")

    model_config = {'populate_by_name': True}


class Id(BaseModel):
    """The unique identifier of the ad which can be obtained after the ad is created using create APIs."""
    pass


class GetSDBudgetRuleResponse(BaseModel):
    budget_rule: Optional["SDBudgetRule"] = Field(None, alias="budgetRule")

    model_config = {'populate_by_name': True}


class StoreSpotlightCreative(BaseModel):
    brand_logo_crop: Optional["AssetCrop"] = Field(None, alias="brandLogoCrop")
    brand_name: str = Field(..., alias="brandName", description="The displayed brand name in the ad headline. Maximum length is 30 characters. See [the policy](https://advertising.amazo")
    subpages: list["Subpage"] = Field(..., description="An array of subpages")
    landing_page: Optional["CreativeLandingPageV2"] = Field(None, alias="landingPage")
    consent_to_translate: Optional[bool] = Field(None, alias="consentToTranslate", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    creative_properties_to_optimize: Optional[list["CreativePropertyToOptimize"]] = Field(None, alias="creativePropertiesToOptimize", description="If this property is enabled, Sponsored Brands will dynamically optimize by enhancing or generating creative properties b")
    brand_logo_asset_id: str = Field(..., alias="brandLogoAssetId", description="The identifier of the [brand logo](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#brandlogo) ")
    headline: str = Field(..., description="The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maxi")

    model_config = {'populate_by_name': True}


class SDHeadlineRecommendationIdentifierNotfoundExceptionCode(StrEnum):
    IDENTIFIER_NOT_FOUND = "IDENTIFIER_NOT_FOUND"


class SDHeadlineRecommendationIdentifierNotfoundException(BaseModel):
    code: Optional[SDHeadlineRecommendationIdentifierNotfoundExceptionCode] = Field(None, description="IdentiferNotFoundErrorCode.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class AdGroupSuccessResponseItem(BaseModel):
    ad_group: Optional["AdGroup"] = Field(None, alias="adGroup")
    index: float = Field(..., description="the index of the adGroup in the array from the request body.")
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="the adGroup ID.")

    model_config = {'populate_by_name': True}


class BulkAdGroupOperationResponse(BaseModel):
    success: Optional[list["AdGroupSuccessResponseItem"]] = None
    error: Optional[list["AdGroupFailureResponseItem"]] = None

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsAdGroupsBetaResponseContent(BaseModel):
    ad_groups: Optional["BulkAdGroupOperationResponse"] = Field(None, alias="adGroups")

    model_config = {'populate_by_name': True}


class CreativeImageRecommendationResponseContent(BaseModel):
    total_results: Optional[float] = Field(None, alias="totalResults", description="The total number of results returned by an operation.")
    recommendations: Optional[list["CreativeImageRecommendationEntry"]] = Field(None, description="Recommendations are sorted on relevancy score, i.e. more relevant image has lesser array index value")

    model_config = {'populate_by_name': True}


class BrandVideoCreative(BaseModel):
    asins: list[str] = Field(..., description="An array of ASINs associated with the creative.")
    brand_logo_crop: Optional["AssetCrop"] = Field(None, alias="brandLogoCrop")
    brand_name: str = Field(..., alias="brandName", description="The displayed brand name in the ad headline. Maximum length is 30 characters. See [the policy](https://advertising.amazo")
    landing_page: Optional["CreativeLandingPageV2"] = Field(None, alias="landingPage")
    consent_to_translate: Optional[bool] = Field(None, alias="consentToTranslate", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    video_asset_ids: list[str] = Field(..., alias="videoAssetIds", description="The assetIds of the original videos submitted by the advertiser. If 'consentToTranslate' is set to true and translation ")
    brand_logo_asset_id: str = Field(..., alias="brandLogoAssetId", description="The identifier of the [brand logo](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#brandlogo) ")
    headline: str = Field(..., description="The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maxi")

    model_config = {'populate_by_name': True}


class CreateBrandVideoCreativeRequestContent(BaseModel):
    ad_id: str = Field(..., alias="adId", description="The unique ID of a Sponsored Brands ad.")
    creative: "BrandVideoCreative"

    model_config = {'populate_by_name': True}


class StatusFilter(BaseModel):
    include: Optional[list[str]] = None

    model_config = {'populate_by_name': True}


class ListImageTasksRequestContent(BaseModel):
    status_filter: Optional["StatusFilter"] = Field(None, alias="statusFilter")
    max_results: Optional[float] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results,")
    task_id_filter: Optional["TaskIdFilter"] = Field(None, alias="taskIdFilter")
    batch_id: str = Field(..., alias="batchId")

    model_config = {'populate_by_name': True}


class BudgetUsageError(BaseModel):
    """The Error Response Object."""
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class NotFoundErrorCode(StrEnum):
    NOT_FOUND = "NOT_FOUND"


class VideoComponentComponenttype(StrEnum):
    SPONSORED_BRANDS_VIDEO = "SPONSORED_BRANDS_VIDEO"
    OTHER_VIDEO = "OTHER_VIDEO"


class VideoComponent(BaseModel):
    """Video component which needs to be pre moderated. A publicly accessible videoUrl must be sent."""
    component_type: VideoComponentComponenttype = Field(..., alias="componentType", description="Type of the video component.")
    landing_page: Optional["LandingPage"] = Field(None, alias="landingPage")
    id_: str = Field(..., alias="id", description="Id of the component. The same will be returned as part of the response as well. This can be used to uniquely identify th")
    url: str = Field(..., description="Url of the video to be pre moderated. The url must be publicly accessible.")

    model_config = {'populate_by_name': True}


class UpdateSponsoredBrandsAdsBetaResponseContent(BaseModel):
    ads: Optional["BulkAdOperationResponse"] = None

    model_config = {'populate_by_name': True}


class ModerationResultsNotFoundErrorCode(StrEnum):
    NOT_FOUND = "NOT_FOUND"


class ModerationResultsNotFoundError(BaseModel):
    code: Optional[ModerationResultsNotFoundErrorCode] = Field(None, description="Not found error code.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class DisassociateSponsoredBrandsOptimizationRulesRequestContent(BaseModel):
    optimization_rule_disassociations: list["OptimizationRuleToEntityMapping"] = Field(..., alias="optimizationRuleDisassociations")

    model_config = {'populate_by_name': True}


class SBTargetingLocale(StrEnum):
    AR_AE = "ar_AE"
    DE_DE = "de_DE"
    EN_AE = "en_AE"
    EN_AU = "en_AU"
    EN_CA = "en_CA"
    EN_GB = "en_GB"
    EN_IN = "en_IN"
    EN_SG = "en_SG"
    EN_US = "en_US"
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


class LandingPageThrottledErrorCode(StrEnum):
    THROTTLED = "THROTTLED"


class CreateSponsoredBrandsCampaignsRequestContent(BaseModel):
    campaigns: list["CreateCampaign"]

    model_config = {'populate_by_name': True}


class ImageResult(BaseModel):
    image_alt_text: Optional[str] = Field(None, alias="imageAltText", description="Alt text for this image")
    image_url: Optional[str] = Field(None, alias="imageUrl")

    model_config = {'populate_by_name': True}


class ImageTask(BaseModel):
    image_url_expiration: Optional[float] = Field(None, alias="imageUrlExpiration", description="The timestamp after which the imageUrl will be invalid. The number represents Unix epoch seconds with optional milliseco")
    image_results: Optional[list["ImageResult"]] = Field(None, alias="imageResults")
    message: Optional[str] = Field(None, description="Image task status details.")
    task_id: Optional[str] = Field(None, alias="taskId")
    status: Optional[str] = Field(None, description="Image task status. Valid values are PENDING, COMPLETED and FAILED")

    model_config = {'populate_by_name': True}


class ListImageTasksResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results,")
    image_task_list: Optional[list["ImageTask"]] = Field(None, alias="imageTaskList")
    batch_id: Optional[str] = Field(None, alias="batchId")
    total_count: Optional[float] = Field(None, alias="totalCount")

    model_config = {'populate_by_name': True}


class NotFoundExceptionResponseContent(BaseModel):
    code: "NotFoundErrorCode"
    message: str

    model_config = {'populate_by_name': True}


class GetSDBudgetRulesForAdvertiserResponse(BaseModel):
    budget_rules_for_advertiser_response: Optional[list["SDBudgetRule"]] = Field(None, alias="budgetRulesForAdvertiserResponse", description="A list of rules created by the advertiser.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` ")

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsCampaignsBetaResponseContent(BaseModel):
    campaigns: Optional["BulkCampaignOperationResponse"] = None

    model_config = {'populate_by_name': True}


class AccessDeniedErrorResponseContent(BaseModel):
    code: "AccessDeniedErrorCode"
    request_id: str = Field(..., alias="requestId")
    message: str

    model_config = {'populate_by_name': True}


class DateComponentComponenttype(StrEnum):
    CAMPAIGN_DATE = "CAMPAIGN_DATE"


class DateComponent(BaseModel):
    """Date component which needs to be pre moderated. Either startDate or endDate must be populated, or both can be populated."""
    component_type: DateComponentComponenttype = Field(..., alias="componentType", description="Type of the date component.")
    end_date: Optional[str] = Field(None, alias="endDate", description="End date of the component in yyyy-MM-dd HH:mm:ss format")
    id_: str = Field(..., alias="id", description="Id of the component. The same will be returned as part of the response as well. This can be used to uniquely identify th")
    start_date: Optional[str] = Field(None, alias="startDate", description="Start date of the component in yyyy-MM-dd HH:mm:ss format")

    model_config = {'populate_by_name': True}


class SBKeywordRecommendationThemeKeyword(BaseModel):
    recommendation_id: Optional[str] = Field(None, alias="recommendationId", description="Unique ID for each recommendation.")
    value: Optional[str] = Field(None, description="Recommended keyword value.")

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsBrandVideoAdsBetaResponseContent(BaseModel):
    ads: Optional["BulkAdOperationResponse"] = None

    model_config = {'populate_by_name': True}


class Theme(BaseModel):
    """Structure for theme details"""
    theme_for_display: str = Field(..., alias="themeForDisplay")
    theme_id: str = Field(..., alias="themeId")

    model_config = {'populate_by_name': True}


class ImageCrop(BaseModel):
    top_left_y: Optional[int] = Field(None, alias="topLeftY", description="Policy violated region's top left Y-axis pixel value.")
    top_left_x: Optional[int] = Field(None, alias="topLeftX", description="Policy violated region's top left X-axis pixel value.")
    width: Optional[int] = Field(None, description="Policy violated region's width in pixel.")
    height: Optional[int] = Field(None, description="Policy violated region's height in pixel.")

    model_config = {'populate_by_name': True}


class SBTargetingInternalServerExceptionResponseContent(BaseModel):
    """Returns information about an InternalServerException."""
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class ListCreativesRequestContent(BaseModel):
    creative_type_filter: Optional[list["CreativeType"]] = Field(None, alias="creativeTypeFilter", description="Filters creatives by optional creative type. By default, you can list all creative versions regardless of creative type.")
    ad_id: str = Field(..., alias="adId", description="The unique ID of a Sponsored Brands ad.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results,")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Set a limit on the number of results returned by an operation.")
    creative_version_filter: Optional[list[str]] = Field(None, alias="creativeVersionFilter", description="Filters creatives by optional creative version. This means you can either list all creative versions without specific cr")
    creative_status_filter: Optional[list["CreativeStatus"]] = Field(None, alias="creativeStatusFilter", description="Filters creatives by optional creative status. By default, you can list all creative versions regardless of creative sta")

    model_config = {'populate_by_name': True}


class SBKeywordRecommendationThemeType(StrEnum):
    KEYWORDS_RELATED_TO_YOUR_BRAND = "KEYWORDS_RELATED_TO_YOUR_BRAND"
    KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES = "KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES"


class SBKeywordRecommendationThemeSuggestion(BaseModel):
    keywords: Optional[list["SBKeywordRecommendationThemeKeyword"]] = None
    type_: Optional["SBKeywordRecommendationThemeType"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class DeleteSponsoredBrandsAdGroupsBetaRequestContent(BaseModel):
    ad_group_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="adGroupIdFilter")

    model_config = {'populate_by_name': True}


class CreateExtendedProductCollectionCreative(BaseModel):
    brand_logo_crop: Optional["BrandLogoCrop"] = Field(None, alias="brandLogoCrop")
    asins: Optional[list[str]] = None
    brand_name: Optional[str] = Field(None, alias="brandName")
    custom_images: Optional[list["CustomImage"]] = Field(None, alias="customImages", description="Requires minimum one custom image. You can add an optional collection of custom images that can be displayed on the ad a")
    consent_to_translate: Optional[bool] = Field(None, alias="consentToTranslate", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    creative_properties_to_optimize: Optional[list["CreativePropertyToOptimize"]] = Field(None, alias="creativePropertiesToOptimize", description="If this property is enabled, Sponsored Brands will dynamically optimize by enhancing or generating creative properties b")
    brand_logo_asset_id: Optional[str] = Field(None, alias="brandLogoAssetID")
    headline: Optional[str] = None

    model_config = {'populate_by_name': True}


class DeleteSponsoredBrandsCampaignsBetaRequestContent(BaseModel):
    campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="campaignIdFilter")

    model_config = {'populate_by_name': True}


class UpdateCampaign(BaseModel):
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="The identifier of an existing portfolio to which the campaign is associated.")
    bidding: Optional["Bidding"] = None
    end_date: Optional[str] = Field(None, alias="endDate", description="endDate is optional. If endDate is specified, startDate must be specified as well. Note: This property is nullable. If n")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign.")
    name: Optional[str] = Field(None, description="The name of the campaign.")
    state: Optional["CreateOrUpdateEntityState"] = None
    start_date: Optional[str] = Field(None, alias="startDate", description="startDate can only be changed if the current startDate is in the future.")
    budget: Optional[float] = Field(None, description="The budget of the campaign. See https://advertising.amazon.com/help?entityId=ENTITYJDATFOIA05Q7#GE5QEBS6QRJJAT3A")
    tags: Optional["Tags"] = None

    model_config = {'populate_by_name': True}


class UpdateSponsoredBrandsCampaignsRequestContent(BaseModel):
    campaigns: list["UpdateCampaign"]

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandStoreSpotlightAdsRequestContent(BaseModel):
    ads: list["CreateStoreSpotlightAd"]

    model_config = {'populate_by_name': True}


class UnauthorizedErrorCode(StrEnum):
    UNAUTHORIZED = "UNAUTHORIZED"


class UnauthorizedExceptionResponseContent(BaseModel):
    code: "UnauthorizedErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class SBTargetingBrand(BaseModel):
    brand_refinement_id: str = Field(..., alias="brandRefinementId", description="Id of brand. Use /sb/targets/categories/{categoryRefinementId}/refinements to retrieve Brand Refinement IDs.")
    name: Optional[str] = Field(None, description="Name of brand.")

    model_config = {'populate_by_name': True}


class NextToken(BaseModel):
    """Operations that return paginated results include a pagination token in this field. To retrieve the next page of results, call the same operation and specify this token in the request. If the `NextToke"""
    pass


class SDListAssociatedBudgetRulesResponse(BaseModel):
    associated_rules: Optional[list["SDBudgetRule"]] = Field(None, alias="associatedRules", description="A list of associated budget rules.")

    model_config = {'populate_by_name': True}


class RecommendedHeadline(BaseModel):
    """Recommended Headline in response object. Recommended headline will be locale specific, i.e. for an asin input in ES, Recommended headline will be in ES."""
    headline_id: Optional[str] = Field(None, alias="headlineId", description="Unique Id of Recommended headline.")
    headline: Optional[str] = Field(None, description="String that contains Recommended headline.")

    model_config = {'populate_by_name': True}


class SDHeadlineRecommendationResponse(BaseModel):
    """Response structure of SD headline recommendation API."""
    request_id: Optional[str] = Field(None, alias="requestId", description="An identifier for request made which is generated by server.")
    recommendations: Optional[list["RecommendedHeadline"]] = Field(None, description="Recommendations are sorted, i.e., more suitable headline has lesser array index value.")

    model_config = {'populate_by_name': True}


class CreateBrandVideoCreativeResponseContent(BaseModel):
    """Create creative response"""
    ad_id: Optional[str] = Field(None, alias="adId", description="The unique ID of a Sponsored Brands ad.")
    creative_version: Optional[str] = Field(None, alias="creativeVersion", description="The version identifier that helps you keep track of multiple versions of a submitted (non-draft) Sponsored Brands creati")

    model_config = {'populate_by_name': True}


class SBTargetingIntegerRange(BaseModel):
    min: Optional[int] = None
    max: Optional[int] = None

    model_config = {'populate_by_name': True}


class SBTargetingCategory(BaseModel):
    """Category details."""
    asin_count_range: Optional["SBTargetingIntegerRange"] = Field(None, alias="asinCountRange")
    is_targetable: Optional[bool] = Field(None, alias="isTargetable", description="If the category is targetable or not.")
    parent_category_refinement_id: Optional[str] = Field(None, alias="parentCategoryRefinementId", description="The category refinement id of the parent category. Missing parentCategoryRefinementId signifies this is a root category.")
    estimated_reach: Optional["SBTargetingEstimatedReachRange"] = Field(None, alias="estimatedReach")
    name: Optional[str] = Field(None, description="Name of category.")
    translated_name: Optional[str] = Field(None, alias="translatedName", description="Translated name of the category.")
    category_refinement_id: Optional[str] = Field(None, alias="categoryRefinementId", description="The category refinement id. Please use /sb/targets/categories or /sb/recommendations/targets/category to retrieve catego")

    model_config = {'populate_by_name': True}


class SBTargetingGetTargetableCategoriesResponseContent(BaseModel):
    """Response object for /sb/targets/categories containing all targetable categories for the advertiser's marketplace."""
    next_token: Optional[str] = Field(None, alias="nextToken", description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results,")
    category_tree: Optional[list["SBTargetingCategory"]] = Field(None, alias="categoryTree", description="List of categories.")

    model_config = {'populate_by_name': True}


class SBKeywordRecommendationThemes(BaseModel):
    theme_type: Optional["SBKeywordRecommendationThemeType"] = Field(None, alias="themeType")

    model_config = {'populate_by_name': True}


class CreateExtendedProductCollectionCreativeResponseContent(BaseModel):
    """Create creative response"""
    ad_id: Optional[str] = Field(None, alias="adId", description="The unique ID of a Sponsored Brands ad.")
    creative_version: Optional[str] = Field(None, alias="creativeVersion", description="The version identifier that helps you keep track of multiple versions of a submitted (non-draft) Sponsored Brands creati")

    model_config = {'populate_by_name': True}


class ModerationResultsInternalServerErrorCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class ModerationResultsInternalServerError(BaseModel):
    code: Optional[ModerationResultsInternalServerErrorCode] = Field(None, description="Internal error code.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class SPBudgetRule(BaseModel):
    rule_state: Optional["state"] = Field(None, alias="ruleState")
    last_updated_date: Optional[float] = Field(None, alias="lastUpdatedDate", description="Epoch time of budget rule update. Read-only.")
    created_date: Optional[float] = Field(None, alias="createdDate", description="Epoch time of budget rule creation. Read-only.")
    rule_details: Optional["SPBudgetRuleDetails"] = Field(None, alias="ruleDetails")
    rule_id: str = Field(..., alias="ruleId", description="The budget rule identifier.")
    rule_status: Optional[str] = Field(None, alias="ruleStatus", description="The budget rule status. Read-only.")

    model_config = {'populate_by_name': True}


class CreativeRecommendationsThrottlingErrorCode(StrEnum):
    THROTTLED = "THROTTLED"


class CreativeRecommendationsThrottlingError(BaseModel):
    code: Optional[CreativeRecommendationsThrottlingErrorCode] = Field(None, description="Throttled error code.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class CreateStoreSpotlightCreativeRequestContent(BaseModel):
    ad_id: str = Field(..., alias="adId", description="The unique ID of a Sponsored Brands ad.")
    creative: "StoreSpotlightCreative"

    model_config = {'populate_by_name': True}


class VideoPosition(BaseModel):
    start: Optional[int] = Field(None, description="Start time of the video having the policy violation.")
    end: Optional[int] = Field(None, description="End time of the video having the policy violation.")

    model_config = {'populate_by_name': True}


class ViolatingVideoEvidence(BaseModel):
    violating_video_position: Optional["VideoPosition"] = Field(None, alias="violatingVideoPosition")

    model_config = {'populate_by_name': True}


class ViolatingVideoContent(BaseModel):
    violating_video_evidences: Optional[list["ViolatingVideoEvidence"]] = Field(None, alias="violatingVideoEvidences")
    moderated_component: Optional[str] = Field(None, alias="moderatedComponent", description="Moderation component which marked the policy violation.")
    reviewed_video_url: Optional[str] = Field(None, alias="reviewedVideoUrl", description="URL of the video which has the ad policy violation.")

    model_config = {'populate_by_name': True}


class ViolatingImageEvidence(BaseModel):
    violating_image_crop: Optional["ImageCrop"] = Field(None, alias="violatingImageCrop")

    model_config = {'populate_by_name': True}


class ViolatingImageContent(BaseModel):
    violating_image_evidences: Optional[list["ViolatingImageEvidence"]] = Field(None, alias="violatingImageEvidences")
    moderated_component: Optional[str] = Field(None, alias="moderatedComponent", description="Moderation component which marked the policy violation.")
    reviewed_image_url: Optional[str] = Field(None, alias="reviewedImageUrl", description="URL of the image which has the ad policy violation.")

    model_config = {'populate_by_name': True}


class PolicyViolation(BaseModel):
    policy_description: Optional[str] = Field(None, alias="policyDescription", description="A human-readable description of the policy.")
    violating_text_contents: Optional[list["ViolatingTextContent"]] = Field(None, alias="violatingTextContents")
    violating_image_contents: Optional[list["ViolatingImageContent"]] = Field(None, alias="violatingImageContents")
    policy_link_url: Optional[str] = Field(None, alias="policyLinkUrl", description="Address of the policy documentation. Follow the link to learn more about the specified policy.")
    violating_video_contents: Optional[list["ViolatingVideoContent"]] = Field(None, alias="violatingVideoContents")
    violating_asin_contents: Optional[list["ViolatingAsinContent"]] = Field(None, alias="violatingAsinContents")

    model_config = {'populate_by_name': True}


class ListSponsoredBrandsAdGroupsResponseContent(BaseModel):
    total_results: Optional[float] = Field(None, alias="totalResults", description="The total number of entities.")
    ad_groups: Optional[list["AdGroup"]] = Field(None, alias="adGroups")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")

    model_config = {'populate_by_name': True}


class CreativeRecommendationProperties(BaseModel):
    """Nested Creative Properties Structure for fetching Creative Recommendations."""
    asins: Optional[list[str]] = Field(None, description="----------------------------------------------- List types ----------------------------------------------- A list of ASI")
    brand_name: Optional[str] = Field(None, alias="brandName", description="The displayed brand name in the ad headline. Maximum length is 30 characters. See [the policy](https://advertising.amazo")
    subpages: Optional[list["Subpage"]] = Field(None, description="An array of subpages")
    landing_page: Optional["CreativeLandingPageV2"] = Field(None, alias="landingPage")
    custom_images: Optional[list["CustomImage"]] = Field(None, alias="customImages", description="An array of customImages associated with the creative.")
    video_asset_ids: Optional[list[str]] = Field(None, alias="videoAssetIds", description="An array of videoAssetIds associated with the creative. Advertisers can get video assetIds from Asset Library /assets/se")
    recommended_creative_id: Optional[str] = Field(None, alias="recommendedCreativeId", description="a Unique Id identifying the creative Recommendation")
    brand_logo: Optional["BrandLogo"] = Field(None, alias="brandLogo")
    headline: Optional[str] = Field(None, description="The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maxi")

    model_config = {'populate_by_name': True}


class SBKeywordRecommendationLandingPage(BaseModel):
    url: Optional[str] = Field(None, description="The URL of the Stores page, or, Vendors may also specify the URL of a custom landing page.")

    model_config = {'populate_by_name': True}


class ThrottlingExceptionResponseContent(BaseModel):
    code: "ThrottledErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class SBTargetingThrottlingExceptionResponseContent(BaseModel):
    """Returns information about a ThrottlingException."""
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class LandingPageThrottlingExceptionResponseContent(BaseModel):
    code: "LandingPageThrottledErrorCode"
    details: str = Field(..., description="A human-readable description of the code field.")

    model_config = {'populate_by_name': True}


class SDHeadlineRecommendationSchemaValidationExceptionCode(StrEnum):
    INVALID_ARGUMENT = "INVALID_ARGUMENT"


class SDHeadlineRecommendationSchemaValidationException(BaseModel):
    code: Optional[SDHeadlineRecommendationSchemaValidationExceptionCode] = Field(None, description="InvalidArgumentErrorCode.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class DeleteSponsoredBrandsAdGroupsRequestContent(BaseModel):
    ad_group_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="adGroupIdFilter")

    model_config = {'populate_by_name': True}


class CreateBudgetRulesResponse(BaseModel):
    responses: Optional[list["BudgetRuleResponse"]] = None

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsProductCollectionAdsResponseContent(BaseModel):
    ads: Optional["BulkAdOperationResponse"] = None

    model_config = {'populate_by_name': True}


class DeleteSponsoredBrandsCampaignsResponseContent(BaseModel):
    campaigns: Optional["BulkCampaignOperationResponse"] = None

    model_config = {'populate_by_name': True}


class HeadlineSuggestionResponse(BaseModel):
    """Response structure of headline suggestion API."""
    request_id: Optional[str] = Field(None, alias="requestId", description="An identifier for request made which is generated by server.")
    suggestions: Optional[list["SuggestedHeadline"]] = Field(None, description="Suggestions are sorted, i.e., more suitable headline has lesser array index value")

    model_config = {'populate_by_name': True}


class BulkAssociationsOptimizationRuleResponse(BaseModel):
    success: Optional[list["OptimizationRuleToEntityMappingSuccessResponseItem"]] = None
    error: Optional[list["OptimizationRuleFailureResponseItem"]] = None

    model_config = {'populate_by_name': True}


class CreateStoreSpotlightCreativeResponseContent(BaseModel):
    """Create creative response"""
    ad_id: Optional[str] = Field(None, alias="adId", description="The unique ID of a Sponsored Brands ad.")
    creative_version: Optional[str] = Field(None, alias="creativeVersion", description="The version identifier that helps you keep track of multiple versions of a submitted (non-draft) Sponsored Brands creati")

    model_config = {'populate_by_name': True}


class SDHeadlineRecommendationRequestAdformat(StrEnum):
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"


class SDHeadlineRecommendationRequest(BaseModel):
    """Request structure of SD headline recommendation API."""
    asins: Optional[list[str]] = Field(None, description="An array of ASINs associated with the creative.")
    max_num_recommendations: Optional[float] = Field(None, alias="maxNumRecommendations", description="Maximum number of recommendations that API should return. Response will [0, maxNumRecommendations] recommendations (reco")
    ad_format: Optional[SDHeadlineRecommendationRequestAdformat] = Field(None, alias="adFormat")

    model_config = {'populate_by_name': True}


class ListSponsoredBrandsCampaignsResponseContent(BaseModel):
    campaigns: Optional[list["Campaign"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    total_count: Optional[float] = Field(None, alias="totalCount", description="The total number of entities.")

    model_config = {'populate_by_name': True}


class NotFoundErrorResponseContent(BaseModel):
    code: "NotFoundErrorCode"
    request_id: str = Field(..., alias="requestId")
    message: str

    model_config = {'populate_by_name': True}


class BudgetUsagePortfolioBatchError(BaseModel):
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="ID of requested resource")
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    index: Optional[float] = Field(None, description="An index to maintain order of the portfolioIds")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class BudgetUsagePortfolioResponse(BaseModel):
    success: Optional[list["BudgetUsagePortfolio"]] = Field(None, description="List of budget usage percentages that were successfully pulled")
    error: Optional[list["BudgetUsagePortfolioBatchError"]] = Field(None, description="List of budget usage percentages that failed to pull")

    model_config = {'populate_by_name': True}


class GetSPBudgetRuleResponse(BaseModel):
    budget_rule: Optional["SPBudgetRule"] = Field(None, alias="budgetRule")

    model_config = {'populate_by_name': True}


class SBTargetingGenre(BaseModel):
    genre_refinement_id: str = Field(..., alias="genreRefinementId", description="Id of Genre. Use /sb/targets/categories/{categoryRefinementId}/refinements to retrieve Genre Refinement IDs.")
    name: Optional[str] = Field(None, description="Name of Genre.")
    translated_name: Optional[str] = Field(None, alias="translatedName", description="Translated name of Genre based off locale sent in request.")

    model_config = {'populate_by_name': True}


class SBTargetingGetRefinementsForCategoryResponseContent(BaseModel):
    """Response object for /sb/targets/categories/{categoryRefinementId}/refinements containing information on Brand Nodes, Age Range Nodes, and Genre Nodes.     Response is paginated with pagination occurri"""
    age_ranges: Optional[list["SBTargetingAgeRange"]] = Field(None, alias="ageRanges", description="List of Age Ranges. Use /sb/targets/categories/{categoryRefinementId}/refinements to retrieve Age Ranges. Age Ranges are")
    brands: Optional[list["SBTargetingBrand"]] = Field(None, description="List of Brands.")
    genres: Optional[list["SBTargetingGenre"]] = Field(None, description="List of Genres. Use /sb/targets/categories/{categoryRefinementId}/refinements to retrieve Genre Node IDs. Genres are onl")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results,")

    model_config = {'populate_by_name': True}


class ListSponsoredBrandsAdsResponseContent(BaseModel):
    ads: Optional[list["Ad"]] = None
    total_results: Optional[float] = Field(None, alias="totalResults", description="The total number of entities.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")

    model_config = {'populate_by_name': True}


class ListSponsoredBrandsCampaignsRequestContent(BaseModel):
    campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    portfolio_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="portfolioIdFilter")
    state_filter: Optional["EntityStateFilter"] = Field(None, alias="stateFilter")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    goal_type_filter: Optional["GoalTypeFilter"] = Field(None, alias="goalTypeFilter")
    include_extended_data_fields: Optional[bool] = Field(None, alias="includeExtendedDataFields", description="Setting to true will slow down performance because the API needs to retrieve extra information for each campaign.")
    name_filter: Optional["NameFilter"] = Field(None, alias="nameFilter")

    model_config = {'populate_by_name': True}


class SBInsightsUnauthorizedExceptionResponseContent(BaseModel):
    """Returns information about an UnauthorizedException."""
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class ModerationError(BaseModel):
    """The Error Response Object."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SecondaryHeadlineRecommendationGroups(BaseModel):
    """Ordered list of Secondary Headline recommendation groups."""
    pass


class CreativeRecommendationResultEntry(BaseModel):
    """Creative Recommendation Result."""
    creative_type: Optional[str] = Field(None, alias="creativeType", description="Supported are PRODUCT_COLLECTION, STORE_SPOTLIGHT, VIDEO, BRAND_VIDEO. More could be added in future.")
    creative_properties: Optional["CreativeRecommendationProperties"] = Field(None, alias="creativeProperties")

    model_config = {'populate_by_name': True}


class CreativeRecommendationsResponseContent(BaseModel):
    total_results: Optional[float] = Field(None, alias="totalResults", description="The total number of results returned by an operation.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results,")
    creatives: Optional[list["CreativeRecommendationResultEntry"]] = Field(None, description="A list of creatives")

    model_config = {'populate_by_name': True}


class InternalErrorErrorCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class CreateSponsoredBrandsAdGroupsBetaRequestContent(BaseModel):
    ad_groups: list["CreateAdGroup"] = Field(..., alias="adGroups")

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandStoreSpotlightAdsResponseContent(BaseModel):
    ads: Optional["BulkAdOperationResponse"] = None

    model_config = {'populate_by_name': True}


class UpdateSponsoredBrandsAdsRequestContent(BaseModel):
    ads: list["UpdateAd"]

    model_config = {'populate_by_name': True}


class DeleteSponsoredBrandsCampaignsBetaResponseContent(BaseModel):
    campaigns: Optional["BulkCampaignOperationResponse"] = None

    model_config = {'populate_by_name': True}


class SDGetAssociatedCampaignsResponse(BaseModel):
    associated_campaigns: Optional[list["AssociatedCampaign"]] = Field(None, alias="associatedCampaigns", description="A list of campaigns that are associated to this budget rule.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` ")

    model_config = {'populate_by_name': True}


class SBTargetingSupplySource(StrEnum):
    AMAZON = "AMAZON"
    STREAMING_VIDEO = "STREAMING_VIDEO"


class SDHeadlineRecommendationMarsThrottlingExceptionCode(StrEnum):
    THROTTLED = "THROTTLED"


class SDHeadlineRecommendationMarsThrottlingException(BaseModel):
    code: Optional[SDHeadlineRecommendationMarsThrottlingExceptionCode] = Field(None, description="ThrottledErrorCode.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class InternalServerExceptionResponseContent(BaseModel):
    code: "InternalErrorErrorCode"
    message: str = Field(..., description="Human readable error message.")

    model_config = {'populate_by_name': True}


class TextComponentComponenttype(StrEnum):
    HEADLINE = "HEADLINE"
    BRAND_NAME = "BRAND_NAME"
    OTHER_TEXT = "OTHER_TEXT"


class TextComponent(BaseModel):
    """Text component which needs to be pre moderated"""
    component_type: TextComponentComponenttype = Field(..., alias="componentType", description="Type of text component.")
    id_: str = Field(..., alias="id", description="Id of the component. The same will be returned as part of the response as well. This can be used to uniquely identify th")
    text: str = Field(..., description="Text which needs to be moderated.")

    model_config = {'populate_by_name': True}


class ProductCollectionCreative(BaseModel):
    asins: list[str] = Field(..., description="An array of ASINs associated with the creative.")
    brand_logo_crop: Optional["AssetCrop"] = Field(None, alias="brandLogoCrop")
    brand_name: str = Field(..., alias="brandName", description="The displayed brand name in the ad headline. Maximum length is 30 characters. See [the policy](https://advertising.amazo")
    custom_image_asset_id: Optional[str] = Field(None, alias="customImageAssetId", description="The identifier of the Custom image from the Store assets library. See [the policy](https://advertising.amazon.com/resour")
    custom_image_crop: Optional["AssetCrop"] = Field(None, alias="customImageCrop")
    brand_logo_asset_id: str = Field(..., alias="brandLogoAssetId", description="The identifier of the [brand logo](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#brandlogo) ")
    headline: str = Field(..., description="The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maxi")

    model_config = {'populate_by_name': True}


class CreateExtendedProductCollectionCreativeRequestContent(BaseModel):
    ad_id: str = Field(..., alias="adId", description="The unique ID of a Sponsored Brands ad.")
    creative: "ExtendedProductCollectionCreative"

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsAdGroupsResponseContent(BaseModel):
    ad_groups: Optional["BulkAdGroupOperationResponse"] = Field(None, alias="adGroups")

    model_config = {'populate_by_name': True}


class ImageComponentComponenttype(StrEnum):
    BRAND_LOGO = "BRAND_LOGO"
    CUSTOM_IMAGE = "CUSTOM_IMAGE"
    OTHER_IMAGE = "OTHER_IMAGE"


class ImageComponent(BaseModel):
    """Image component which needs to be pre moderated. A publicly accessible imageUrl must be sent."""
    component_type: ImageComponentComponenttype = Field(..., alias="componentType", description="Type of the image component.")
    landing_page: Optional["LandingPage"] = Field(None, alias="landingPage")
    id_: str = Field(..., alias="id", description="Id of the component. The same will be returned as part of the response as well. This can be used to uniquely identify th")
    url: str = Field(..., description="Url of the image to be pre moderated. The url must be publicly accessible.")

    model_config = {'populate_by_name': True}


class PreModerationRequestAdprogram(StrEnum):
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_BRANDS_SPOTLIGHT = "SPONSORED_BRANDS_SPOTLIGHT"
    SPONSORED_BRANDS_VIDEO = "SPONSORED_BRANDS_VIDEO"
    STORES = "STORES"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    DSP = "DSP"
    DSP_REC = "DSP_REC"
    DSP_IMAGE = "DSP_IMAGE"
    DSP_THIRD_PARTY = "DSP_THIRD_PARTY"


class PreModerationRequestLocale(StrEnum):
    AR_AE = "ar-AE"
    ZH_CN = "zh-CN"
    NL_NL = "nl-NL"
    EN_AU = "en-AU"
    EN_CA = "en-CA"
    EN_IN = "en-IN"
    EN_GB = "en-GB"
    EN_US = "en-US"
    FR_CA = "fr-CA"
    FR_FR = "fr-FR"
    DE_DE = "de-DE"
    IT_IT = "it-IT"
    JA_JP = "ja-JP"
    KO_KR = "ko-KR"
    PT_BR = "pt-BR"
    ES_ES = "es-ES"
    ES_US = "es-US"
    ES_MX = "es-MX"
    TR_TR = "tr-TR"


class PreModerationRequest(BaseModel):
    """Components details that needs to be sent for pre moderation."""
    record_id: Optional[str] = Field(None, alias="recordId", description="Id of the brand/advertiser.")
    asin_components: Optional[list["AsinComponent"]] = Field(None, alias="asinComponents", description="Asin components which needs to be pre moderated.")
    ad_program: PreModerationRequestAdprogram = Field(..., alias="adProgram", description="Type of Ad program to which this pre moderation components belong to.")
    locale: PreModerationRequestLocale = Field(..., description="Specifying locale will translate the premoderation message into that locale's associated language.     | Locale | Langua")
    image_components: Optional[list["ImageComponent"]] = Field(None, alias="imageComponents", description="Image components which needs to be pre moderated.")
    date_components: Optional[list["DateComponent"]] = Field(None, alias="dateComponents", description="Date components which needs to be pre moderated.")
    text_components: Optional[list["TextComponent"]] = Field(None, alias="textComponents", description="Text components which needs to be pre moderated.")
    video_components: Optional[list["VideoComponent"]] = Field(None, alias="videoComponents", description="Video components which needs to be pre moderated.")

    model_config = {'populate_by_name': True}


class ModerationStatus(StrEnum):
    APPROVED = "APPROVED"
    IN_PROGRESS = "IN_PROGRESS"
    REJECTED = "REJECTED"
    FAILED = "FAILED"


class ModerationResult(BaseModel):
    version_id: Optional["VersionId"] = Field(None, alias="versionId")
    id_type: Optional["IdType"] = Field(None, alias="idType")
    moderation_status: Optional["ModerationStatus"] = Field(None, alias="moderationStatus")
    policy_violations: Optional[list["PolicyViolation"]] = Field(None, alias="policyViolations", description="A list of policy violations for a campaign that has failed moderation. Note that this field is present in the response o")
    eta_for_moderation: Optional[str] = Field(None, alias="etaForModeration", description="Expected date and time by which moderation will be complete. The format is ISO 8601 in UTC time zone. Note that this fie")
    id_: Optional["Id"] = Field(None, alias="id")

    model_config = {'populate_by_name': True}


class AcceptHeader(StrEnum):
    APPLICATION_VND_SBADCREATIVERESOURCE_V4_JSON = "application/vnd.sbAdCreativeResource.v4+json"
    APPLICATION_VND_SBCREATIVEIMAGERECOMMENDATIONRESOURCE_V4_JSON = "application/vnd.sbCreativeImageRecommendationResource.v4+json"
    APPLICATION_VND_SBCREATIVERECOMMENDATIONRESOURCE_V4_JSON = "application/vnd.sbCreativeRecommendationResource.v4+json"


class UpdateSponsoredBrandsCampaignsBetaResponseContent(BaseModel):
    campaigns: Optional["BulkCampaignOperationResponse"] = None

    model_config = {'populate_by_name': True}


class CreateExtendedProductCollectionAd(BaseModel):
    landing_page: "LandingPage" = Field(..., alias="landingPage")
    name: str = Field(..., description="The name of the ad.")
    state: "CreateOrUpdateEntityState"
    ad_group_id: str = Field(..., alias="adGroupId", description="The adGroup identifier.")
    creative: "CreateExtendedProductCollectionCreative"

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsExtendedProductCollectionAdsRequestContent(BaseModel):
    ads: list["CreateExtendedProductCollectionAd"] = Field(..., description="An array of Product Collection ad objects to create. Maximum length of the array is 10 objects.")

    model_config = {'populate_by_name': True}


class SBInsightsBadRequestExceptionResponseContent(BaseModel):
    """Returns information about a BadRequestException."""
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class UpdateSDBudgetRulesRequest(BaseModel):
    """Request object for updating budget rule for SD campaign"""
    budget_rules_details: Optional[list["SDBudgetRule"]] = Field(None, alias="budgetRulesDetails", description="A list of budget rule details.")

    model_config = {'populate_by_name': True}


class SPCampaignBudgetRule(BaseModel):
    rule_state: Optional["state"] = Field(None, alias="ruleState")
    last_updated_date: Optional[float] = Field(None, alias="lastUpdatedDate", description="Epoch time of budget rule update. Read-only.")
    created_date: Optional[float] = Field(None, alias="createdDate", description="Epoch time of budget rule creation. Read-only.")
    rule_details: Optional["SPBudgetRuleDetails"] = Field(None, alias="ruleDetails")
    rule_id: str = Field(..., alias="ruleId", description="The budget rule identifier.")
    rule_status: Optional[str] = Field(None, alias="ruleStatus", description="The budget rule evaluation status. Read-only.")

    model_config = {'populate_by_name': True}


class SPListAssociatedBudgetRulesResponse(BaseModel):
    associated_rules: Optional[list["SPCampaignBudgetRule"]] = Field(None, alias="associatedRules", description="A list of associated budget rules.")

    model_config = {'populate_by_name': True}


class DeleteSponsoredBrandsAdsBetaRequestContent(BaseModel):
    ad_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="adIdFilter")

    model_config = {'populate_by_name': True}


class UpdateSponsoredBrandsAdsResponseContent(BaseModel):
    ads: Optional["BulkAdOperationResponse"] = None

    model_config = {'populate_by_name': True}


class CreativeRecommendationsEligibilityResponseContent(BaseModel):
    is_eligible: Optional[bool] = Field(None, alias="isEligible", description="Returns false if there is no creative recommendation possible with the given landing page.")
    creative_types: Optional[list[str]] = Field(None, alias="creativeTypes", description="Supported are PRODUCT_COLLECTION, STORE_SPOTLIGHT, VIDEO, BRAND_VIDEO. More could be added in future.")

    model_config = {'populate_by_name': True}


class CreativeImageRecommendationRequestContent(BaseModel):
    asins: list[str] = Field(..., description="----------------------------------------------- List types ----------------------------------------------- A list of ASI")
    asset_sub_type: Optional["AssetSubType"] = Field(None, alias="assetSubType")
    max_num_recommendations: Optional[float] = Field(None, alias="maxNumRecommendations", description="Maximum number of recommendations that API should return. Response will [0, recommendations] recommendations (recommenda")
    asset_programs: Optional[list["ProgramType"]] = Field(None, alias="assetPrograms", description="Filter assets by program types. For example, if only [A_PLUS] assets are requested then only assets that were used as A+")
    locale: Optional[str] = Field(None, description="(Optional) locale of creative headline and ASIN titles. If locale is not provided, default locale of marketplace is used")
    headline: Optional[str] = Field(None, description="The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maxi")

    model_config = {'populate_by_name': True}


class DeleteSponsoredBrandsAdGroupsResponseContent(BaseModel):
    ad_groups: Optional["BulkAdGroupOperationResponse"] = Field(None, alias="adGroups")

    model_config = {'populate_by_name': True}


class SPGetAssociatedCampaignsResponse(BaseModel):
    associated_campaigns: Optional[list["AssociatedCampaign"]] = Field(None, alias="associatedCampaigns", description="A list of campaigns that are associated to this budget rule.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` ")

    model_config = {'populate_by_name': True}


class DeleteSponsoredBrandsAdGroupsBetaResponseContent(BaseModel):
    ad_groups: Optional["BulkAdGroupOperationResponse"] = Field(None, alias="adGroups")

    model_config = {'populate_by_name': True}


class CreateProductCollectionCreativeResponseContent(BaseModel):
    """Create creative response"""
    ad_id: Optional[str] = Field(None, alias="adId", description="The unique ID of a Sponsored Brands ad.")
    creative_version: Optional[str] = Field(None, alias="creativeVersion", description="The version identifier that helps you keep track of multiple versions of a submitted (non-draft) Sponsored Brands creati")

    model_config = {'populate_by_name': True}


class ModerationResultsAdProgramType(StrEnum):
    SB_PRODUCT_COLLECTION = "SB_PRODUCT_COLLECTION"
    SB_STORE_SPOTLIGHT = "SB_STORE_SPOTLIGHT"
    SB_VIDEO = "SB_VIDEO"
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"


class CreativeRecommendationsBadRequestErrorCode(StrEnum):
    BAD_REQUEST = "BAD_REQUEST"


class CreativeRecommendationsBadRequestError(BaseModel):
    code: Optional[CreativeRecommendationsBadRequestErrorCode] = Field(None, description="Bad request error code.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class SBTargetingUnprocessableEntityExceptionResponseContent(BaseModel):
    """Returns information about an UnprocessableEntityException."""
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SBTargetingAccessDeniedExceptionResponseContent(BaseModel):
    """Returns information about an AccessDeniedException."""
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class UpdateSponsoredBrandsAdGroupsBetaResponseContent(BaseModel):
    ad_groups: Optional["BulkAdGroupOperationResponse"] = Field(None, alias="adGroups")

    model_config = {'populate_by_name': True}


class AssociateSponsoredBrandsOptimizationRulesRequestContent(BaseModel):
    optimization_rule_associations: list["OptimizationRuleToEntityMapping"] = Field(..., alias="optimizationRuleAssociations")

    model_config = {'populate_by_name': True}


class BulkUpdateOptimizationRuleOperationResponse(BaseModel):
    success: Optional[list["UpdateOptimizationRuleSuccessResponseItem"]] = None
    error: Optional[list["OptimizationRuleFailureResponseItem"]] = None

    model_config = {'populate_by_name': True}


class UpdateSponsoredBrandsOptimizationRulesResponseContent(BaseModel):
    optimization_rules: "BulkUpdateOptimizationRuleOperationResponse" = Field(..., alias="optimizationRules")

    model_config = {'populate_by_name': True}


class CreativeRecommendationsRequestAdformat(StrEnum):
    SPONSORED_BRANDS_VIDEO = "SPONSORED_BRANDS_VIDEO"


class CreativeRecommendationsRequest(BaseModel):
    """Request structure of creative recommendations API."""
    asins: list[str] = Field(..., description="An array of ASINs associated with the creative. Note, do not pass an empty array, this results in an error.")
    ad_format: CreativeRecommendationsRequestAdformat = Field(..., alias="adFormat", description="Ad format of the creative.")
    required_recommendations: list["RequiredRecommendations"] = Field(..., alias="requiredRecommendations", description="Required recommendations details.")

    model_config = {'populate_by_name': True}


class OptimizationRuleIdFilter(BaseModel):
    """Filter optimization rules by the list of optimization rule ids."""
    include: Optional[list[str]] = None

    model_config = {'populate_by_name': True}


class ConflictStateExceptionResponseContent(BaseModel):
    code: "ConflictStateErrorCode"
    message: str

    model_config = {'populate_by_name': True}


class CreativeRecommendationsNotFoundErrorCode(StrEnum):
    NOT_FOUND = "NOT_FOUND"


class CreativeRecommendationsNotFoundError(BaseModel):
    code: Optional[CreativeRecommendationsNotFoundErrorCode] = Field(None, description="Not found error code.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class UpdateSponsoredBrandsAdGroupsResponseContent(BaseModel):
    ad_groups: Optional["BulkAdGroupOperationResponse"] = Field(None, alias="adGroups")

    model_config = {'populate_by_name': True}


class GetSPBudgetRulesForAdvertiserResponse(BaseModel):
    budget_rules_for_advertiser_response: Optional[list["SPBudgetRule"]] = Field(None, alias="budgetRulesForAdvertiserResponse", description="A list of rules created by the advertiser.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` ")

    model_config = {'populate_by_name': True}


class CreativeRecommendationsInternalServerErrorCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class CreativeRecommendationsInternalServerError(BaseModel):
    code: Optional[CreativeRecommendationsInternalServerErrorCode] = Field(None, description="Internal error code.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class SBTargetingUnauthorizedExceptionResponseContent(BaseModel):
    """Returns information about an UnauthorizedException."""
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SBInsightsInternalServerExceptionResponseContent(BaseModel):
    """Returns information about an InternalServerException."""
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class DeleteSponsoredBrandsAdsBetaResponseContent(BaseModel):
    ads: Optional["BulkAdOperationResponse"] = None

    model_config = {'populate_by_name': True}


class BudgetUsagePortfolioRequest(BaseModel):
    portfolio_ids: Optional[list[str]] = Field(None, alias="portfolioIds", description="A list of portfolio IDs.")

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsVideoAdsRequestContent(BaseModel):
    ads: list["CreateVideoAd"]

    model_config = {'populate_by_name': True}


class SBTargetingGetTargetableASINCountsResponseContent(BaseModel):
    """Response object for /sb/targets/products/count to get number of targetable asins for refinements provided by the user"""
    asin_counts: Optional["SBTargetingIntegerRange"] = Field(None, alias="asinCounts")

    model_config = {'populate_by_name': True}


class ModerationResultsResponse(BaseModel):
    moderation_results: Optional[list["ModerationResult"]] = Field(None, alias="moderationResults")
    next_token: Optional["NextToken"] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class GetBudgetRecommendationsRequestContent(BaseModel):
    campaign_ids: list[str] = Field(..., alias="campaignIds", description="List of CampaignIds")

    model_config = {'populate_by_name': True}


class BudgetUsageCampaignRequest(BaseModel):
    campaign_ids: Optional[list[str]] = Field(None, alias="campaignIds", description="A list of campaign IDs")

    model_config = {'populate_by_name': True}


class CreateProductCollectionCreativeRequestContent(BaseModel):
    ad_id: str = Field(..., alias="adId", description="The unique ID of a Sponsored Brands ad.")
    creative: "ProductCollectionCreative"

    model_config = {'populate_by_name': True}


class ModerationResultsAccessDeniedErrorCode(StrEnum):
    ACCESS_DENIED = "ACCESS_DENIED"


class ModerationResultsAccessDeniedError(BaseModel):
    code: Optional[ModerationResultsAccessDeniedErrorCode] = Field(None, description="Access denied error code.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class SBTargetingRatingRange(BaseModel):
    """Rating range is restricted to integers between 0 and 5, inclusive. Min must be less than or equal to max. We use this to retrieve the number of targetable ASINs that falls within this rating range."""
    min: Optional[int] = None
    max: Optional[int] = None

    model_config = {'populate_by_name': True}


class ListSponsoredBrandsAdsBetaResponseContent(BaseModel):
    ads: Optional[list["Ad"]] = None
    total_results: Optional[float] = Field(None, alias="totalResults", description="The total number of entities.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")

    model_config = {'populate_by_name': True}


class SBTargetingGetNegativeBrandsResponseContent(BaseModel):
    """Response object for /sb/negativeTargets/brands/recommendations containing list of brands for negative targeting."""
    brands: Optional[list["SBTargetingBrand"]] = Field(None, description="List of Brands.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results,")

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsProductCollectionAdsRequestContent(BaseModel):
    ads: list["CreateProductCollectionAd"]

    model_config = {'populate_by_name': True}


class EntityFilter(BaseModel):
    """Filter optimization rules by entityId and entityType"""
    entity_type: Optional[str] = Field(None, alias="entityType", description="Enum: 'CAMPAIGN'  The type of entity passed.")
    entity_id: Optional[str] = Field(None, alias="entityId", description="Entity object identifier.")

    model_config = {'populate_by_name': True}


class ListSponsoredBrandsOptimizationRulesRequestContent(BaseModel):
    entity_filter: Optional["EntityFilter"] = Field(None, alias="entityFilter")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    optimization_rule_id_filter: Optional["OptimizationRuleIdFilter"] = Field(None, alias="optimizationRuleIdFilter")

    model_config = {'populate_by_name': True}


class ListSponsoredBrandsAdsRequestContent(BaseModel):
    campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    state_filter: Optional["EntityStateFilter"] = Field(None, alias="stateFilter")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    ad_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="adIdFilter")
    ad_group_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    name_filter: Optional["NameFilter"] = Field(None, alias="nameFilter")

    model_config = {'populate_by_name': True}


class InvalidArgumentErrorResponseContent(BaseModel):
    code: "InvalidArgumentErrorCode"
    request_id: str = Field(..., alias="requestId")
    message: str

    model_config = {'populate_by_name': True}


class CreateAssociatedBudgetRulesRequest(BaseModel):
    budget_rule_ids: Optional[list[str]] = Field(None, alias="budgetRuleIds", description="A list of budget rule identifiers.")

    model_config = {'populate_by_name': True}


class ModerationResultsThrottlingErrorCode(StrEnum):
    THROTTLED = "THROTTLED"


class ModerationResultsThrottlingError(BaseModel):
    code: Optional[ModerationResultsThrottlingErrorCode] = Field(None, description="Throttled error code.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class ListSponsoredBrandsCampaignsBetaResponseContent(BaseModel):
    campaigns: Optional[list["Campaign"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    total_count: Optional[float] = Field(None, alias="totalCount", description="The total number of entities.")

    model_config = {'populate_by_name': True}


class ModerationResultsBadRequestErrorCode(StrEnum):
    BAD_REQUEST = "BAD_REQUEST"


class ModerationResultsBadRequestError(BaseModel):
    code: Optional[ModerationResultsBadRequestErrorCode] = Field(None, description="Bad request error code.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class CreativeRecommendationByIdResponseContent(BaseModel):
    """Creative Recommendation by Id Response."""
    creative_type: Optional[str] = Field(None, alias="creativeType", description="Supported are PRODUCT_COLLECTION, STORE_SPOTLIGHT, VIDEO, BRAND_VIDEO. More could be added in future.")
    creative_properties: Optional["CreativeRecommendationProperties"] = Field(None, alias="creativeProperties")

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandStoreSpotlightAdsBetaResponseContent(BaseModel):
    ads: Optional["BulkAdOperationResponse"] = None

    model_config = {'populate_by_name': True}


class UpdateSponsoredBrandsCampaignsBetaRequestContent(BaseModel):
    campaigns: list["UpdateCampaign"]

    model_config = {'populate_by_name': True}


class ListSponsoredBrandsAdsBetaRequestContent(BaseModel):
    campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    state_filter: Optional["EntityStateFilter"] = Field(None, alias="stateFilter")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")
    ad_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="adIdFilter")
    ad_group_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    name_filter: Optional["NameFilter"] = Field(None, alias="nameFilter")

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandStoreSpotlightAdsBetaRequestContent(BaseModel):
    ads: list["CreateStoreSpotlightAd"]

    model_config = {'populate_by_name': True}


class BudgetUsageCampaign(BaseModel):
    budget_usage_percent: Optional[float] = Field(None, alias="budgetUsagePercent", description="Budget usage percentage (spend / available budget) for the given budget policy.")
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="ID of requested resource")
    usage_updated_timestamp: Optional[str] = Field(None, alias="usageUpdatedTimestamp", description="Last evaluation time for budget usage")
    index: Optional[float] = Field(None, description="An index to maintain order of the campaignIds")
    budget: Optional[float] = Field(None, description="Budget amount of resource requested")

    model_config = {'populate_by_name': True}


class BudgetUsageCampaignResponse(BaseModel):
    success: Optional[list["BudgetUsageCampaign"]] = Field(None, description="List of budget usage percentages that were successfully pulled")
    error: Optional[list["BudgetUsageCampaignBatchError"]] = Field(None, description="List of budget usage percentages that failed to pull")

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsBrandVideoAdsResponseContent(BaseModel):
    ads: Optional["BulkAdOperationResponse"] = None

    model_config = {'populate_by_name': True}


class CreateVideoCreativeResponseContent(BaseModel):
    """Create creative response"""
    ad_id: Optional[str] = Field(None, alias="adId", description="The unique ID of a Sponsored Brands ad.")
    creative_version: Optional[str] = Field(None, alias="creativeVersion", description="The version identifier that helps you keep track of multiple versions of a submitted (non-draft) Sponsored Brands creati")

    model_config = {'populate_by_name': True}


class ModerationResultsRequest(BaseModel):
    version_id_filter: Optional[list["VersionId"]] = Field(None, alias="versionIdFilter", description="Filter by specific version id of the ad. The API will return the ad's all versions moderation status if this field is em")
    id_type: "IdType" = Field(..., alias="idType")
    ad_program_type: "ModerationResultsAdProgramType" = Field(..., alias="adProgramType")
    next_token: Optional["NextToken"] = Field(None, alias="nextToken")
    max_results: int = Field(..., alias="maxResults", description="Sets a limit on the number of results returned by an operation.")
    moderation_status_filter: Optional[list["ModerationStatus"]] = Field(None, alias="moderationStatusFilter", description="Filter by specific moderation status.")
    id_: "Id" = Field(..., alias="id")

    model_config = {'populate_by_name': True}


class SBRuleDuration(BaseModel):
    date_range_type_rule_duration: "DateRangeTypeRuleDuration" = Field(..., alias="dateRangeTypeRuleDuration")

    model_config = {'populate_by_name': True}


class CreateVideoCreativeRequestContent(BaseModel):
    ad_id: str = Field(..., alias="adId", description="The unique ID of a Sponsored Brands ad.")
    creative: "VideoCreative"

    model_config = {'populate_by_name': True}


class GetSBBudgetRuleResponse(BaseModel):
    budget_rule: Optional["SBBudgetRule"] = Field(None, alias="budgetRule")

    model_config = {'populate_by_name': True}


class CreateOptimizationRule(BaseModel):
    entity_type: Optional[str] = Field(None, alias="entityType", description="Enum: 'CAMPAIGN'  The type of entity passed.")
    entity_id: Optional[str] = Field(None, alias="entityId", description="Entity object identifier.")
    conditions: Optional[list["RuleCondition"]] = None

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsOptimizationRulesRequestContent(BaseModel):
    optimization_rules: list["CreateOptimizationRule"] = Field(..., alias="optimizationRules")

    model_config = {'populate_by_name': True}


class AssociatedBudgetRuleResponse(BaseModel):
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the error, if unsuccessful")
    rule_id: Optional[str] = Field(None, alias="ruleId", description="The budget rule identifier.")

    model_config = {'populate_by_name': True}


class DeleteSponsoredBrandsCampaignsRequestContent(BaseModel):
    campaign_id_filter: Optional["ObjectIdFilter"] = Field(None, alias="campaignIdFilter")

    model_config = {'populate_by_name': True}


class SBKeywordRecommendationThemeRequest(BaseModel):
    themes: Optional[list["SBKeywordRecommendationThemes"]] = None
    max_num_suggestions: Optional[int] = Field(None, alias="maxNumSuggestions", description="Maximum number of suggestions to return for each theme. Max value is 1000. If not provided, default to 100.")
    landing_pages: Optional[list["SBKeywordRecommendationLandingPage"]] = Field(None, alias="landingPages")

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsBrandVideoAdsRequestContent(BaseModel):
    ads: list["CreateBrandVideoAd"]

    model_config = {'populate_by_name': True}


class CreateSBBudgetRulesRequest(BaseModel):
    budget_rules_details: Optional[list["SBBudgetRuleDetails"]] = Field(None, alias="budgetRulesDetails", description="A list of budget rule details.")

    model_config = {'populate_by_name': True}


class UnauthorizedErrorResponseContent(BaseModel):
    code: "UnauthorizedErrorCode"
    request_id: str = Field(..., alias="requestId")
    message: str

    model_config = {'populate_by_name': True}


class SBTargetingBadRequestExceptionResponseContent(BaseModel):
    """Returns information about a BadRequestException."""
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsVideoAdsResponseContent(BaseModel):
    ads: Optional["BulkAdOperationResponse"] = None

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsBrandVideoAdsBetaRequestContent(BaseModel):
    ads: list["CreateBrandVideoAd"]

    model_config = {'populate_by_name': True}


class AssociateSponsoredBrandsOptimizationRulesResponseContent(BaseModel):
    optimization_rule_associations: "BulkAssociationsOptimizationRuleResponse" = Field(..., alias="optimizationRuleAssociations")

    model_config = {'populate_by_name': True}


class UpdateSBBudgetRulesRequest(BaseModel):
    budget_rules_details: Optional[list["SBBudgetRule"]] = Field(None, alias="budgetRulesDetails", description="A list of budget rule details.")

    model_config = {'populate_by_name': True}


class CreateAssociatedBudgetRulesResponse(BaseModel):
    responses: Optional[list["AssociatedBudgetRuleResponse"]] = None

    model_config = {'populate_by_name': True}


class BudgetRuleError(BaseModel):
    """The Error Response Object."""
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class ListThemesRequestContent(BaseModel):
    max_results: Optional[float] = Field(None, alias="maxResults", description="Optional. The max limit for the number of themes it can return.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional. The pagination token to retrieve the next page of results.")

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsAdGroupsRequestContent(BaseModel):
    ad_groups: list["CreateAdGroup"] = Field(..., alias="adGroups")

    model_config = {'populate_by_name': True}


class UpdateSPBudgetRulesRequest(BaseModel):
    """Request object for updating budget rule for SP campaign"""
    budget_rules_details: Optional[list["SPBudgetRule"]] = Field(None, alias="budgetRulesDetails", description="A list of budget rule details.")

    model_config = {'populate_by_name': True}


class CreativeRecommendationsResponse(BaseModel):
    primary_headlines: Optional["PrimaryHeadlineRecommendationGroups"] = Field(None, alias="primaryHeadlines")
    secondary_headlines: Optional["SecondaryHeadlineRecommendationGroups"] = Field(None, alias="secondaryHeadlines")

    model_config = {'populate_by_name': True}


class SBTargetingGetTargetableASINCountsRequestContent(BaseModel):
    age_ranges: Optional[list[str]] = Field(None, alias="ageRanges", description="List of Age Range Refinement Ids.")
    brands: Optional[list[str]] = Field(None, description="List of Brand Refinement Ids.")
    genres: Optional[list[str]] = Field(None, description="List of Genre Refinement Ids.")
    is_prime_shipping: Optional[bool] = Field(None, alias="isPrimeShipping", description="Indicates if products have prime shipping. Leave empty to include both prime shipping and non-prime shipping products.")
    rating_range: Optional["SBTargetingRatingRange"] = Field(None, alias="ratingRange")
    category: str = Field(..., description="The category refinement id. Please use /sb/targets/categories or /sb/recommendations/targets/category to retrieve catego")
    price_range: Optional["SBTargetingPriceRange"] = Field(None, alias="priceRange")

    model_config = {'populate_by_name': True}


class ListThemesResponseContent(BaseModel):
    themes: Optional[list["Theme"]] = Field(None, description="List of themes")
    next_token: Optional[str] = Field(None, alias="nextToken", description="If nextToken is not null, it means there are more results.")
    total_count: Optional[float] = Field(None, alias="totalCount")

    model_config = {'populate_by_name': True}


class DisassociateAssociatedBudgetRuleResponse(BaseModel):
    pass


class SDHeadlineRecommendationInternalServerExceptionCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class SDHeadlineRecommendationInternalServerException(BaseModel):
    code: Optional[SDHeadlineRecommendationInternalServerExceptionCode] = Field(None, description="InternalErrorCode.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class SBForecastingProductExpression(BaseModel):
    """Expression settings for the target."""
    type_: Optional[str] = Field(None, alias="type", description="The expression type associated with the target. Valid value: ASIN_CATEGORY_SAME_AS, ASIN_BRAND_SAME_AS, ASIN_PRICE_LESS_")
    value: Optional[str] = Field(None, description="The expression value associated with targets.")

    model_config = {'populate_by_name': True}


class SBForecastingProductTarget(BaseModel):
    """The target associated with the ad group."""
    expressions: Optional[list["SBForecastingProductExpression"]] = None
    bid: Optional[float] = Field(None, description="The associated bid. Note that this value must be less than the budget associated with the Advertiser account.")

    model_config = {'populate_by_name': True}


class SBForecastingNegativeProductExpression(BaseModel):
    """Negative expression settings for the target."""
    type_: Optional[str] = Field(None, alias="type", description="The negative expression type associated with the target. Valid value: ASIN_BRAND_SAME_AS, ASIN_SAME_AS.")
    value: Optional[str] = Field(None, description="The expression value associated with targets.")

    model_config = {'populate_by_name': True}


class SBForecastingNegativeProductTarget(BaseModel):
    """The negative target associated with the ad group."""
    expressions: Optional[list["SBForecastingNegativeProductExpression"]] = None

    model_config = {'populate_by_name': True}


class SBForecastingNegativeKeyword(BaseModel):
    """Negative keyword associated with the campaign."""
    keyword_text: Optional[str] = Field(None, alias="keywordText", description="The keyword text. Maximum of 10 words.")
    match_type: Optional[str] = Field(None, alias="matchType", description="The negative match type. Valid value: NEGATIVE_EXACT, NEGATIVE_PHRASE. For more information, see [negative keyword match")

    model_config = {'populate_by_name': True}


class SBForecastingKeyword(BaseModel):
    """Keyword associated with the campaign."""
    keyword_text: Optional[str] = Field(None, alias="keywordText", description="The keyword text. Maximum of 10 words.")
    match_type: Optional[str] = Field(None, alias="matchType", description="The match type. Valid value: EXACT, PHRASE, BROAD. For more information, see [match types](https://advertising.amazon.co")
    bid: Optional[float] = Field(None, description="The associated bid. Note that this value must be less than the budget associated with the Advertiser account.")

    model_config = {'populate_by_name': True}


class SBForecastingTheme(BaseModel):
    """The theme."""
    theme_type: Optional[str] = Field(None, alias="themeType", description="The theme target type. Valid value: KEYWORDS_RELATED_TO_YOUR_BRAND, KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES.   KEYWORDS_R")
    bid: Optional[float] = Field(None, description="The associated bid. Note that this value must be less than the budget associated with the Advertiser account.")

    model_config = {'populate_by_name': True}


class SBForecastingLandingPageObject(BaseModel):
    landing_page_url: Optional[str] = Field(None, alias="landingPageUrl", description="Landing page information.")

    model_config = {'populate_by_name': True}


class SBForecastingAdGroup(BaseModel):
    """The ad group settings."""
    targets: Optional[list["SBForecastingProductTarget"]] = None
    negative_targets: Optional[list["SBForecastingNegativeProductTarget"]] = Field(None, alias="negativeTargets")
    landing_pages: Optional[list["SBForecastingLandingPageObject"]] = Field(None, alias="landingPages")
    themes: Optional[list["SBForecastingTheme"]] = None
    keywords: Optional[list["SBForecastingKeyword"]] = None
    negative_keywords: Optional[list["SBForecastingNegativeKeyword"]] = Field(None, alias="negativeKeywords")
    creative_asins: Optional[list[str]] = Field(None, alias="creativeAsins")

    model_config = {'populate_by_name': True}


class SBForecastingRequestCampaignObject(BaseModel):
    """The campaign settings."""
    budget: float = Field(..., description="The amount of the budget.")
    budget_type: str = Field(..., alias="budgetType", description="Budget can be set to DAILY or LIFETIME.   |BudgetType|Description| |-----------|-----------| |DAILY| The amount that you")
    forecast_type: str = Field(..., alias="forecastType", description="The forecast type. can be set to WEEKLY or MONTHLY.   **If have not set the forecastType during campaign creation then u")
    start_date: Optional[str] = Field(None, alias="startDate", description="The YYYY-MM-DD start date for the campaign. If this field is not set to a value, the current date is used.")
    end_date: Optional[str] = Field(None, alias="endDate", description="The YYYY-MM-DD end date for the campaign. Must be greater than the value for `startDate`. If not specified, the campaign")
    goal: Optional[str] = Field(None, description="Goal will allow you to set goal type to help drive your campaign performance.   **If have not set the goal during campai")
    ad_groups: list["SBForecastingAdGroup"] = Field(..., alias="adGroups")

    model_config = {'populate_by_name': True}


class SBCampaignPerformanceForecastsRequestContent(BaseModel):
    campaigns: list["SBForecastingRequestCampaignObject"]

    model_config = {'populate_by_name': True}


class SBForecastingMetricValue(BaseModel):
    """The forecast min and max value."""
    min: Optional[float] = Field(None, description="The forecast min value.")
    max: Optional[float] = Field(None, description="The forecast max value.")

    model_config = {'populate_by_name': True}


class SBForecastingMetric(BaseModel):
    """The forecast metric."""
    metric: Optional[str] = Field(None, description="The forecast metric name. Currently supported metrics are IMPRESSION and CLICK.")
    value: Optional["SBForecastingMetricValue"] = None

    model_config = {'populate_by_name': True}


class SBForecastingSuccessCampaign(BaseModel):
    forecasts: Optional[list["SBForecastingMetric"]] = None
    forecast_timestamp: Optional[str] = Field(None, alias="forecastTimestamp", description="The forecast timestamp.")

    model_config = {'populate_by_name': True}


class SBForecastingSuccessObject(BaseModel):
    index: Optional[int] = Field(None, description="Correlates the campaign to the campaign list index specified in the request. Zero-based.")
    campaign: Optional["SBForecastingSuccessCampaign"] = None

    model_config = {'populate_by_name': True}


class SBForecastingErrorObject(BaseModel):
    index: Optional[int] = Field(None, description="Correlates the campaign to the campaign list index specified in the request. Zero-based.")
    code: Optional[str] = Field(None, description="The forecast error code.")
    description: Optional[str] = Field(None, description="The forecast error description.")

    model_config = {'populate_by_name': True}


class SBForecastingResponseCampaignObject(BaseModel):
    successes: Optional[list["SBForecastingSuccessObject"]] = None
    errors: Optional[list["SBForecastingErrorObject"]] = None

    model_config = {'populate_by_name': True}


class SBCampaignPerformanceForecastsResponseContent(BaseModel):
    """Response object for /sb/forecasts containing a list of performance forecast for the campaign."""
    campaigns: Optional["SBForecastingResponseCampaignObject"] = None

    model_config = {'populate_by_name': True}


class SBForecastingAccessDeniedExceptionResponseContent(BaseModel):
    """Returns information about an AccessDeniedException."""
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SBForecastingBadRequestExceptionResponseContent(BaseModel):
    """Returns information about a BadRequestException."""
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SBForecastingInternalServerExceptionResponseContent(BaseModel):
    """Returns information about a InternalServerException."""
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SBForecastingThrottlingExceptionResponseContent(BaseModel):
    """Returns information about a ThrottlingException."""
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SBForecastingUnauthorizedExceptionResponseContent(BaseModel):
    """Returns information about an UnauthorizedException."""
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SBForecastingUnprocessableEntityExceptionResponseContent(BaseModel):
    """Returns information about an UnprocessableEntityException."""
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class StartMigrationJobRequestContent(BaseModel):
    campaign_ids: list[str] = Field(..., alias="campaignIds", description="Provide list of campaign ids that needs to be migrated")
    is_staged_migration: Optional[bool] = Field(None, alias="isStagedMigration", description="Set this flag to true if you want generate new campaign ID based on V3 campaign ID. These campaigns will not be visible ")
    new_campaign_state: Optional[str] = Field(None, alias="newCampaignState", description="This is optional parameter. By default, the new migrated campaigns will have the original status of V3 campaigns. If thi")
    enable_theme_targeting: bool = Field(..., alias="enableThemeTargeting", description="By default, theme targeting is set true if no value is provide. To disable theme targeting, set this flag to false.")
    brand_entity_id: Optional[str] = Field(None, alias="brandEntityId", description="Please note that brandEntityId is only required for sellers. You can get the brandEntityId by calling the <a href = http")

    model_config = {'populate_by_name': True}


class StartMigrationJobResponseContent(BaseModel):
    job_id: Optional[str] = Field(None, alias="jobId", description="This jobId can be used to track migration status through /sb/v4/legacyCampaigns/migrationJob/status and results of each ")

    model_config = {'populate_by_name': True}


class MigrationJobResultsRequestContent(BaseModel):
    job_id: str = Field(..., alias="jobId")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")

    model_config = {'populate_by_name': True}


class CampaignMigrationFinalStatus(BaseModel):
    legacy_campaign_id: Optional[str] = Field(None, alias="legacyCampaignId", description="Entity object identifier.")
    new_campaign_id: Optional[str] = Field(None, alias="newCampaignId")
    migration_status: Optional[str] = Field(None, alias="migrationStatus", description="Enumerated status code for migration job status | Status                                             |  Description | |-")
    migration_status_reason: Optional[str] = Field(None, alias="migrationStatusReason", description="Status reason for the given migration status")

    model_config = {'populate_by_name': True}


class MigrationJobResultsResponseContent(BaseModel):
    job_id: Optional[str] = Field(None, alias="jobId")
    migration_job_status: Optional[str] = Field(None, alias="migrationJobStatus", description="Enumerated status code for migration job status | Status                                             |  Description | |-")
    campaigns: Optional[list["CampaignMigrationFinalStatus"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")

    model_config = {'populate_by_name': True}


class MigrationJobStatusRequestContent(BaseModel):
    job_id: str = Field(..., alias="jobId")

    model_config = {'populate_by_name': True}


class MigrationJobStatusResponseContent(BaseModel):
    job_id: Optional[str] = Field(None, alias="jobId")
    migration_job_status: Optional[str] = Field(None, alias="migrationJobStatus", description="Enumerated status code for migration job status | Status                                             |  Description | |-")
    migration_job_status_reason: Optional[str] = Field(None, alias="migrationJobStatusReason", description="Status reason for the migration job status")

    model_config = {'populate_by_name': True}


class MigrationResultsRequestContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")

    model_config = {'populate_by_name': True}


class MigrationResultsResponseContent(BaseModel):
    campaigns: Optional[list["CampaignMigrationFinalStatus"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next response page.")

    model_config = {'populate_by_name': True}


class CreateAutoCollectionCreative(BaseModel):
    asin_exclusions: Optional[list[str]] = Field(None, alias="asinExclusions")
    brand_logo_asset_id: Optional[str] = Field(None, alias="brandLogoAssetID")
    brand_logo_crop: Optional["BrandLogoCrop"] = Field(None, alias="brandLogoCrop")
    brand_name: str = Field(..., alias="brandName")

    model_config = {'populate_by_name': True}


class CreateAutoCollectionAd(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="Entity object identifier.")
    creative: "CreateAutoCollectionCreative"
    name: str
    state: "CreateOrUpdateEntityState"

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsAutoCollectionAdsRequestContent(BaseModel):
    ads: list["CreateAutoCollectionAd"]

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsAutoCollectionAdsResponseContent(BaseModel):
    ads: Optional["BulkAdOperationResponse"] = None

    model_config = {'populate_by_name': True}


class UpdateAutoCollectionAd(BaseModel):
    ad_id: str = Field(..., alias="adId", description="Entity object identifier.")
    creative: "CreateAutoCollectionCreative"

    model_config = {'populate_by_name': True}


class UpdateSponsoredBrandsAutoCollectionAdsRequestContent(BaseModel):
    """Updates the ad settings for an automatic collection by creating a new version"""
    ads: list["UpdateAutoCollectionAd"] = Field(..., description="List of Automatic Collection Ad Updates")

    model_config = {'populate_by_name': True}


class CreativeMutationErrorSelector(BaseModel):
    other_error: Optional["OtherError"] = Field(None, alias="otherError")
    range_error: Optional["RangeError"] = Field(None, alias="rangeError")

    model_config = {'populate_by_name': True}


class CreativeMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error.")
    error_value: "CreativeMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class CreativeFailureResponseItem(BaseModel):
    errors: Optional[list["CreativeMutationError"]] = Field(None, description="A list of validation errors.")
    index: float = Field(..., description="the index of the creative in the array from the request body.")

    model_config = {'populate_by_name': True}


class CreativeSuccessResponseItem(BaseModel):
    ad_id: str = Field(..., alias="adId", description="Entity object identifier.")
    creative_version: Optional[str] = Field(None, alias="creativeVersion")
    index: float = Field(..., description="The index in the original list from the request.")

    model_config = {'populate_by_name': True}


class BulkCreativeResponse(BaseModel):
    error: Optional[list["CreativeFailureResponseItem"]] = None
    success: Optional[list["CreativeSuccessResponseItem"]] = None

    model_config = {'populate_by_name': True}


class UpdateSponsoredBrandsAutoCollectionAdsResponseContent(BaseModel):
    creatives: Optional["BulkCreativeResponse"] = None

    model_config = {'populate_by_name': True}


class BrandCollectionLandingPageType(StrEnum):
    PRODUCT_LIST = "PRODUCT_LIST"
    STORE = "STORE"


class BrandCollectionLandingPage(BaseModel):
    page_type: Optional["BrandCollectionLandingPageType"] = Field(None, alias="pageType")
    url: Optional[str] = Field(None, description="URL of an existing simple landing page or Store page for brand collection ads. If the pageType is PRODUCT_LIST, the land")

    model_config = {'populate_by_name': True}


class CreateManualCollectionCreative(BaseModel):
    asins: list[str]
    brand_logo_asset_id: Optional[str] = Field(None, alias="brandLogoAssetID")
    brand_logo_crop: Optional["BrandLogoCrop"] = Field(None, alias="brandLogoCrop")
    brand_name: str = Field(..., alias="brandName")
    landing_page: Optional["BrandCollectionLandingPage"] = Field(None, alias="landingPage")

    model_config = {'populate_by_name': True}


class CreateManualCollectionAd(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="Entity object identifier.")
    creative: "CreateManualCollectionCreative"
    name: str
    state: "CreateOrUpdateEntityState"

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsManualCollectionAdsRequestContent(BaseModel):
    ads: list["CreateManualCollectionAd"]

    model_config = {'populate_by_name': True}


class CreateSponsoredBrandsManualCollectionAdsResponseContent(BaseModel):
    ads: Optional["BulkAdOperationResponse"] = None

    model_config = {'populate_by_name': True}


class UpdateManualCollectionAd(BaseModel):
    ad_id: str = Field(..., alias="adId", description="Entity object identifier.")
    creative: "CreateManualCollectionCreative"

    model_config = {'populate_by_name': True}


class UpdateSponsoredBrandsManualCollectionAdsRequestContent(BaseModel):
    """Updates the ad settings for a manual collection by creating a new version"""
    ads: list["UpdateManualCollectionAd"] = Field(..., description="List of Manual Collection Ad Updates")

    model_config = {'populate_by_name': True}


class UpdateSponsoredBrandsManualCollectionAdsResponseContent(BaseModel):
    creatives: Optional["BulkCreativeResponse"] = None

    model_config = {'populate_by_name': True}

