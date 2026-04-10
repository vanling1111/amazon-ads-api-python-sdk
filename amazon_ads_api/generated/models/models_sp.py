"""Auto-generated Pydantic models. Do not edit manually.

Source: SponsoredProducts_prod_3p.json
Title:  Sponsored Products
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional

from pydantic import BaseModel, Field



class AccessDeniedException(BaseModel):
    """Returns information about an AccessDeniedException."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class TargetingExpressionType(StrEnum):
    CLOSE_MATCH = "CLOSE_MATCH"
    COMPLEMENTS = "COMPLEMENTS"
    KEYWORD_BROAD_MATCH = "KEYWORD_BROAD_MATCH"
    KEYWORD_EXACT_MATCH = "KEYWORD_EXACT_MATCH"
    KEYWORD_PHRASE_MATCH = "KEYWORD_PHRASE_MATCH"
    LOOSE_MATCH = "LOOSE_MATCH"
    SUBSTITUTES = "SUBSTITUTES"


class TargetingExpression(BaseModel):
    """The targeting expression. The `type` property specifies the targeting option. Use `CLOSE_MATCH` to match your auto targeting ads closely to the specified value. Use `LOOSE_MATCH` to match your auto ta"""
    type_: TargetingExpressionType = Field(..., alias="type")
    value: Optional[str] = Field(None, description="The targeting expression value.")

    model_config = {'populate_by_name': True}


class AdGroup(BaseModel):
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="The ad group identifier.")
    asins: list[str] = Field(..., description="The list of ad ASINs in the ad group.")
    targeting_expressions: list["TargetingExpression"] = Field(..., alias="targetingExpressions", description="The list of targeting expressions. Maximum of 100 per request.")

    model_config = {'populate_by_name': True}


class RecommendationOptionsLocale(StrEnum):
    AR_EG = "ar_EG"
    DE_DE = "de_DE"
    EN_AE = "en_AE"
    EN_AU = "en_AU"
    EN_CA = "en_CA"
    EN_GB = "en_GB"
    EN_IN = "en_IN"
    EN_SA = "en_SA"
    EN_SG = "en_SG"
    EN_US = "en_US"
    ES_ES = "es_ES"
    ES_MX = "es_MX"
    FR_FR = "fr_FR"
    IT_IT = "it_IT"
    JA_JP = "ja_JP"
    NL_NL = "nl_NL"
    PL_PL = "pl_PL"
    PT_BR = "pt_BR"
    SV_SE = "sv_SE"
    TR_TR = "tr_TR"
    ZH_CN = "zh_CN"


class RecommendationOptionsSortdimension(StrEnum):
    CLICKS = "CLICKS"
    CONVERSIONS = "CONVERSIONS"
    DEFAULT = "DEFAULT"


class RecommendationOptions(BaseModel):
    locale: Optional[RecommendationOptionsLocale] = Field(None, description="Translations are for readability and do not affect the targeting of ads. Supported marketplace to locale mappings can be")
    max_recommendations: Optional[float] = Field(None, alias="maxRecommendations", description="The max size of recommended target. Set it to 0 if you only want to rank user-defined keywords.")
    sort_dimension: Optional[RecommendationOptionsSortdimension] = Field(None, alias="sortDimension", description="The ranking metric value. Supported values: CLICKS, CONVERSIONS, DEFAULT. DEFAULT will be applied if no value passed in.")

    model_config = {'populate_by_name': True}


class AdGroupBasedRequestRecommendationtype(StrEnum):
    KEYWORDS_FOR_ADGROUP = "KEYWORDS_FOR_ADGROUP"


class AdGroupBasedRequest(BaseModel):
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="The identifier of the ad group")
    bids_enabled: Optional[bool] = Field(None, alias="bidsEnabled", description="Set this parameter to false if you do not want to retrieve bid suggestions for your keyword targets. Defaults to true.")
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="The identifier of the campaign")
    recommendation_type: Optional[AdGroupBasedRequestRecommendationtype] = Field(None, alias="recommendationType", description="The recommendationType to retrieve recommended keyword targets for an existing ad group.")

    model_config = {'populate_by_name': True}


class KeywordTargetMatchtype(StrEnum):
    BROAD = "BROAD"
    EXACT = "EXACT"
    PHRASE = "PHRASE"


class KeywordTarget(BaseModel):
    bid: Optional[float] = Field(None, description="The bid value for the keyword, in minor currency units (example: cents). The default value will be the suggested bid.")
    keyword: Optional[str] = Field(None, description="The keyword value")
    match_type: Optional[KeywordTargetMatchtype] = Field(None, alias="matchType", description="Keyword match type. The default value will be BROAD.")
    user_selected_keyword: Optional[bool] = Field(None, alias="userSelectedKeyword", description="Flag that tells if keyword was selected by the user or was recommended by KRS")

    model_config = {'populate_by_name': True}


class KeywordTargetRankRecommendationRequest(BaseModel):
    targets: Optional[list["KeywordTarget"]] = Field(None, description="A list of targets that need to be ranked")

    model_config = {'populate_by_name': True}


class AdGroupKeywordTargetRankRecommendationRequestRecommendationtype(StrEnum):
    KEYWORDS_FOR_ADGROUP = "KEYWORDS_FOR_ADGROUP"


class AdGroupKeywordTargetRankRecommendationRequest(BaseModel):
    """This request type is used to retrieve recommended keyword targets for an existing ad group. Set the recommendationType to KEYWORDS_FOR_ADGROUP to use this request type."""
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the ad group")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign")
    recommendation_type: AdGroupKeywordTargetRankRecommendationRequestRecommendationtype = Field(..., alias="recommendationType", description="The recommendationType to retrieve recommended keyword targets for an existing ad group.")

    model_config = {'populate_by_name': True}


class TargetingExpressionList(BaseModel):
    """The list of targeting expressions. Maximum of 100 per request, use pagination for more if needed."""
    pass


class AdGroupThemeBasedBidRecommendationRequestRecommendationtype(StrEnum):
    BIDS_FOR_EXISTING_AD_GROUP = "BIDS_FOR_EXISTING_AD_GROUP"


class AdGroupThemeBasedBidRecommendationRequest(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The ad group identifier.")
    campaign_id: str = Field(..., alias="campaignId", description="The campaign identifier.")
    recommendation_type: AdGroupThemeBasedBidRecommendationRequestRecommendationtype = Field(..., alias="recommendationType", description="The bid recommendation type.")
    targeting_expressions: "TargetingExpressionList" = Field(..., alias="targetingExpressions")

    model_config = {'populate_by_name': True}


class TargetingExpressionV4Type(StrEnum):
    CLOSE_MATCH = "CLOSE_MATCH"
    COMPLEMENTS = "COMPLEMENTS"
    KEYWORD_BROAD_MATCH = "KEYWORD_BROAD_MATCH"
    KEYWORD_EXACT_MATCH = "KEYWORD_EXACT_MATCH"
    KEYWORD_GROUP = "KEYWORD_GROUP"
    KEYWORD_PHRASE_MATCH = "KEYWORD_PHRASE_MATCH"
    LOOSE_MATCH = "LOOSE_MATCH"
    PAT_ASIN = "PAT_ASIN"
    PAT_CATEGORY = "PAT_CATEGORY"
    PAT_CATEGORY_REFINEMENT = "PAT_CATEGORY_REFINEMENT"
    SUBSTITUTES = "SUBSTITUTES"


class TargetingExpressionV4(BaseModel):
    """The targeting expression. The `type` property specifies the targeting option. Use `CLOSE_MATCH` to match your auto targeting ads closely to the specified value. Use `LOOSE_MATCH` to match your auto ta"""
    type_: TargetingExpressionV4Type = Field(..., alias="type")
    value: Optional[str] = Field(None, description="The targeting expression value.")

    model_config = {'populate_by_name': True}


class TargetingExpressionListV4(BaseModel):
    """The list of targeting expressions. Maximum of 100 per request, use pagination for more if needed."""
    pass


class AdGroupThemeBasedBidRecommendationRequestV4Recommendationtype(StrEnum):
    BIDS_FOR_EXISTING_AD_GROUP = "BIDS_FOR_EXISTING_AD_GROUP"


class AdGroupThemeBasedBidRecommendationRequestV4(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The ad group identifier.")
    campaign_id: str = Field(..., alias="campaignId", description="The campaign identifier.")
    recommendation_type: AdGroupThemeBasedBidRecommendationRequestV4Recommendationtype = Field(..., alias="recommendationType", description="The bid recommendation type.")
    targeting_expressions: "TargetingExpressionListV4" = Field(..., alias="targetingExpressions")

    model_config = {'populate_by_name': True}


class AdGroupThemeBasedBidRecommendationRequestV5Recommendationtype(StrEnum):
    BIDS_FOR_EXISTING_AD_GROUP = "BIDS_FOR_EXISTING_AD_GROUP"


class AdGroupThemeBasedBidRecommendationRequestV5(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The ad group identifier.")
    campaign_id: str = Field(..., alias="campaignId", description="The campaign identifier.")
    include_analysis: Optional[bool] = Field(None, alias="includeAnalysis", description="Flag to include new bid analyzer data.")
    recommendation_type: AdGroupThemeBasedBidRecommendationRequestV5Recommendationtype = Field(..., alias="recommendationType", description="The bid recommendation type.")
    targeting_expressions: "TargetingExpressionListV4" = Field(..., alias="targetingExpressions")

    model_config = {'populate_by_name': True}


class PlacementAdjustmentPredicate(StrEnum):
    PLACEMENT_PRODUCT_PAGE = "PLACEMENT_PRODUCT_PAGE"
    PLACEMENT_REST_OF_SEARCH = "PLACEMENT_REST_OF_SEARCH"
    PLACEMENT_TOP = "PLACEMENT_TOP"


class PlacementAdjustment(BaseModel):
    """Specifies bid adjustments based on the placement location. Use `PLACEMENT_TOP` for the top of the search page. Use `PLACEMENT_REST_OF_SEARCH` for the rest of the search page. Use `PLACEMENT_PRODUCT_PA"""
    percentage: Optional[int] = None
    predicate: Optional[PlacementAdjustmentPredicate] = None

    model_config = {'populate_by_name': True}


class Adjustment(BaseModel):
    placement_adjustment: Optional["PlacementAdjustment"] = Field(None, alias="placementAdjustment")

    model_config = {'populate_by_name': True}


class AgeRange(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="Id of Age Range. This field is REQUIRED if the Age Range object is being used as an input. Use the GetRefinementsForCate")
    name: Optional[str] = Field(None, description="Name of Age Range. This field is OPTIONAL if the Age Range object is being used as an input.")

    model_config = {'populate_by_name': True}


class AgeRangeLoP(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="Id of Age Range. Use the POST /sp/targets/category/{categoryId}/refinements endpoint to retrieve Age Range Node IDs.")
    name: Optional[str] = Field(None, description="Name of Age Range.")
    translated_name: Optional[str] = Field(None, alias="translatedName", description="Translated name of Age Range based off locale sent in request.")

    model_config = {'populate_by_name': True}


class AgeRanges(BaseModel):
    """List of Age Ranges. Use the GetRefinementsForCategory to retrieve Age Ranges. Age Ranges are only available for categories related to children's toys and games."""
    pass


class AgeRangesLoP(BaseModel):
    """List of Age Ranges in a language of preference (LoP). Use the POST /sp/targets/category/{categoryId}/refinements endpoint to retrieve Age Ranges. Age Ranges are only available for categories related t"""
    pass


class AsinsBasedRequestBiddingstrategy(StrEnum):
    AUTO_FOR_SALES = "AUTO_FOR_SALES"
    LEGACY_FOR_SALES = "LEGACY_FOR_SALES"
    MANUAL = "MANUAL"
    RULE_BASED = "RULE_BASED"


class AsinsBasedRequestRecommendationtype(StrEnum):
    KEYWORDS_FOR_ASINS = "KEYWORDS_FOR_ASINS"


class AsinsBasedRequest(BaseModel):
    bidding_strategy: Optional[AsinsBasedRequestBiddingstrategy] = Field(None, alias="biddingStrategy", description="The bid recommendations returned will depend on the bidding strategy. <br> LEGACY_FOR_SALES - Dynamic Bids (Down only) <")
    bids_enabled: Optional[bool] = Field(None, alias="bidsEnabled", description="Set this parameter to false if you do not want to retrieve bid suggestions for your keyword targets. Defaults to true.")
    recommendation_type: Optional[AsinsBasedRequestRecommendationtype] = Field(None, alias="recommendationType", description="The recommendationType to retrieve recommended keyword targets for a list of ASINs.")

    model_config = {'populate_by_name': True}


class AsinsKeywordTargetRankRecommendationRequestRecommendationtype(StrEnum):
    KEYWORDS_FOR_ASINS = "KEYWORDS_FOR_ASINS"


class AsinsKeywordTargetRankRecommendationRequest(BaseModel):
    """This request type is used to retrieve recommended keyword targets for ASINs. Set the recommendationType to KEYWORDS_FOR_ASINS to use this request type."""
    asins: list[str] = Field(..., description="An array list of Asins")
    recommendation_type: AsinsKeywordTargetRankRecommendationRequestRecommendationtype = Field(..., alias="recommendationType", description="The recommendationType to retrieve recommended keyword targets for a list of ASINs.")

    model_config = {'populate_by_name': True}


class BiddingStrategy(StrEnum):
    AUTO_FOR_SALES = "AUTO_FOR_SALES"
    LEGACY_FOR_SALES = "LEGACY_FOR_SALES"
    MANUAL = "MANUAL"
    RULE_BASED = "RULE_BASED"


class AsinsThemeBasedBidRecommendationRequestBidding(BaseModel):
    """Bidding control configuration for the campaign."""
    adjustments: Optional[list["PlacementAdjustment"]] = Field(None, description="Placement adjustment configuration for the campaign.")
    strategy: "BiddingStrategy"

    model_config = {'populate_by_name': True}


class AsinsThemeBasedBidRecommendationRequestRecommendationtype(StrEnum):
    BIDS_FOR_NEW_AD_GROUP = "BIDS_FOR_NEW_AD_GROUP"


class AsinsThemeBasedBidRecommendationRequest(BaseModel):
    asins: list[str] = Field(..., description="The list of ad ASINs in the ad group.")
    bidding: "AsinsThemeBasedBidRecommendationRequestBidding" = Field(..., description="Bidding control configuration for the campaign.")
    recommendation_type: AsinsThemeBasedBidRecommendationRequestRecommendationtype = Field(..., alias="recommendationType", description="The bid recommendation type.")
    targeting_expressions: "TargetingExpressionList" = Field(..., alias="targetingExpressions")

    model_config = {'populate_by_name': True}


class ProductDetailsGlobalstoresetting(BaseModel):
    """This denotes the fields related to [GlobalStore Program](https://sellercentral.amazon.com/help/hub/reference/external/202139180)."""
    catalog_source_country_code: Optional[str] = Field(None, alias="catalogSourceCountryCode", description="Country code of source marketplace where seller has listed the product. Possible source country codes include US, UK, DE")

    model_config = {'populate_by_name': True}


class ProductDetails(BaseModel):
    asin: Optional[str] = Field(None, description="The identifier of the product.")
    global_store_setting: Optional["ProductDetailsGlobalstoresetting"] = Field(None, alias="globalStoreSetting", description="This denotes the fields related to [GlobalStore Program](https://sellercentral.amazon.com/help/hub/reference/external/20")

    model_config = {'populate_by_name': True}


class AsinsThemeBasedBidRecommendationRequestV4Bidding(BaseModel):
    """Bidding control configuration for the campaign."""
    adjustments: Optional[list["PlacementAdjustment"]] = Field(None, description="Placement adjustment configuration for the campaign.")
    strategy: "BiddingStrategy"

    model_config = {'populate_by_name': True}


class AsinsThemeBasedBidRecommendationRequestV4Recommendationtype(StrEnum):
    BIDS_FOR_NEW_AD_GROUP = "BIDS_FOR_NEW_AD_GROUP"


class AsinsThemeBasedBidRecommendationRequestV4(BaseModel):
    asins: list[str] = Field(..., description="The list of ad ASINs in the ad group.")
    bidding: "AsinsThemeBasedBidRecommendationRequestV4Bidding" = Field(..., description="Bidding control configuration for the campaign.")
    product_details_list: Optional[list["ProductDetails"]] = Field(None, alias="productDetailsList", description="The list of products in the request, required for GlobalStore ASINs.")
    recommendation_type: AsinsThemeBasedBidRecommendationRequestV4Recommendationtype = Field(..., alias="recommendationType", description="The bid recommendation type.")
    targeting_expressions: "TargetingExpressionListV4" = Field(..., alias="targetingExpressions")

    model_config = {'populate_by_name': True}


class AsinsThemeBasedBidRecommendationRequestV5Bidding(BaseModel):
    """Bidding control configuration for the campaign."""
    adjustments: Optional[list["PlacementAdjustment"]] = Field(None, description="Placement adjustment configuration for the campaign.")
    strategy: "BiddingStrategy"

    model_config = {'populate_by_name': True}


class AsinsThemeBasedBidRecommendationRequestV5Recommendationtype(StrEnum):
    BIDS_FOR_NEW_AD_GROUP = "BIDS_FOR_NEW_AD_GROUP"


class AsinsThemeBasedBidRecommendationRequestV5(BaseModel):
    asins: list[str] = Field(..., description="The list of ad ASINs in the ad group.")
    bidding: "AsinsThemeBasedBidRecommendationRequestV5Bidding" = Field(..., description="Bidding control configuration for the campaign.")
    include_analysis: Optional[bool] = Field(None, alias="includeAnalysis", description="Flag to include new bid analyzer data.")
    product_details_list: Optional[list["ProductDetails"]] = Field(None, alias="productDetailsList", description="The list of products in the request, required for GlobalStore ASINs.")
    recommendation_type: AsinsThemeBasedBidRecommendationRequestV5Recommendationtype = Field(..., alias="recommendationType", description="The bid recommendation type.")
    targeting_expressions: "TargetingExpressionListV4" = Field(..., alias="targetingExpressions")

    model_config = {'populate_by_name': True}


class AssociatedBudgetRuleResponse(BaseModel):
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the error, if unsuccessful")
    rule_id: Optional[str] = Field(None, alias="ruleId", description="The budget rule identifier.")

    model_config = {'populate_by_name': True}


class AssociatedCampaign(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="The campaign identifier.")
    campaign_name: str = Field(..., alias="campaignName", description="The campaign name.")
    rule_status: str = Field(..., alias="ruleStatus", description="The budget rule evaluation status for this campaign. Read-only.")

    model_config = {'populate_by_name': True}


class AudienceSegmentAudiencesegmenttype(StrEnum):
    BEHAVIOR_DYNAMIC = "BEHAVIOR_DYNAMIC"
    SPONSORED_ADS_AMC = "SPONSORED_ADS_AMC"


class AudienceSegment(BaseModel):
    audience_id: str = Field(..., alias="audienceId", description="Unique identifier for the audience segment.")
    audience_segment_type: AudienceSegmentAudiencesegmenttype = Field(..., alias="audienceSegmentType", description="Type of audience segment.")

    model_config = {'populate_by_name': True}


class BadRequestException(BaseModel):
    """Returns information about a BadRequestException."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class Clicks(BaseModel):
    """Clicks benchmark."""
    lower: Optional[int] = Field(None, description="lower bound.")
    upper: Optional[int] = Field(None, description="upper bound.")

    model_config = {'populate_by_name': True}


class Impressions(BaseModel):
    """Impressions benchmark."""
    lower: Optional[int] = Field(None, description="lower bound.")
    upper: Optional[int] = Field(None, description="upper bound.")

    model_config = {'populate_by_name': True}


class Conversions(BaseModel):
    """Conversions benchmark."""
    lower: Optional[int] = Field(None, description="lower bound.")
    upper: Optional[int] = Field(None, description="upper bound.")

    model_config = {'populate_by_name': True}


class Values(BaseModel):
    """Metrics benchmark values."""
    clicks: Optional["Clicks"] = None
    conversions: Optional["Conversions"] = None
    impressions: Optional["Impressions"] = None

    model_config = {'populate_by_name': True}


class BenchmarkBenchmarkstatus(StrEnum):
    FAILED = "failed"
    PARTIAL = "partial"
    SUCCESS = "success"


class Benchmark(BaseModel):
    """Forecasted impact metrics for next 7 days or during special days."""
    benchmark_status: Optional[BenchmarkBenchmarkstatus] = Field(None, alias="benchmarkStatus", description="Specifies the processing status of the benchmark. Success - If all fields in values property (impressions, clicks, conve")
    values: Optional["Values"] = None

    model_config = {'populate_by_name': True}


class BidAnalysisImpactMetrics(BaseModel):
    estimated_impression_avg: int = Field(..., alias="estimatedImpressionAvg", description="Number indicating the average of the estimated impressions")
    estimated_impression_lower: int = Field(..., alias="estimatedImpressionLower", description="Number indicating a lower bound of the estimated impressions")
    estimated_impression_upper: int = Field(..., alias="estimatedImpressionUpper", description="Number indicating an upper bound of the estimated impressions")

    model_config = {'populate_by_name': True}


class BidAnalysisType(StrEnum):
    ALTERNATIVE = "ALTERNATIVE"
    SUGGESTED = "SUGGESTED"
    SUGGESTED_LOWER = "SUGGESTED_LOWER"
    SUGGESTED_UPPER = "SUGGESTED_UPPER"


class BidAnalysis(BaseModel):
    bid: float
    impact_metrics: "BidAnalysisImpactMetrics" = Field(..., alias="impactMetrics")
    type_: BidAnalysisType = Field(..., alias="type", description="The type of bids in bid analyses. <br>`SUGGESTED_UPPER` - The upper bound for the suggested bid. <br>`SUGGESTED_LOWER` -")

    model_config = {'populate_by_name': True}


class BidAnalyses(BaseModel):
    pass


class BidAnalysesPerPlacement(BaseModel):
    all: "BidAnalyses" = Field(..., alias="ALL")
    placement_product_page: "BidAnalyses" = Field(..., alias="PLACEMENT_PRODUCT_PAGE")
    placement_rest_of_search: "BidAnalyses" = Field(..., alias="PLACEMENT_REST_OF_SEARCH")
    placement_top: "BidAnalyses" = Field(..., alias="PLACEMENT_TOP")

    model_config = {'populate_by_name': True}


class BidAnalysesPerTargetingExpression(BaseModel):
    bid_analyses: "BidAnalysesPerPlacement" = Field(..., alias="bidAnalyses")
    targeting_expression: "TargetingExpressionV4" = Field(..., alias="targetingExpression")

    model_config = {'populate_by_name': True}


class BidPlacementAdjustmentPredicate(StrEnum):
    PLACEMENT_PRODUCT_PAGE = "PLACEMENT_PRODUCT_PAGE"
    PLACEMENT_REST_OF_SEARCH = "PLACEMENT_REST_OF_SEARCH"
    PLACEMENT_TOP = "PLACEMENT_TOP"


class BidPlacementAdjustment(BaseModel):
    """Specifies bid adjustments based on the placement location. Use `PLACEMENT_TOP` for the top of the search page. Use `PLACEMENT_REST_OF_SEARCH` for the rest of the search page. Use `PLACEMENT_PRODUCT_PA"""
    percentage: Optional[int] = None
    predicate: Optional[BidPlacementAdjustmentPredicate] = None

    model_config = {'populate_by_name': True}


class BidRecommendationError(BaseModel):
    code: str = Field(..., description="A machine-readable error code.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class BidValue(BaseModel):
    """Bid value of the bid recommendations."""
    suggested_bid: float = Field(..., alias="suggestedBid", description="The suggested bid.")

    model_config = {'populate_by_name': True}


class BidRecommendationPerTargetingExpression(BaseModel):
    bid_values: list["BidValue"] = Field(..., alias="bidValues")
    targeting_expression: "TargetingExpression" = Field(..., alias="targetingExpression")

    model_config = {'populate_by_name': True}


class BidRecommendationPerTargetingExpressionV4(BaseModel):
    bid_values: list["BidValue"] = Field(..., alias="bidValues")
    targeting_expression: "TargetingExpressionV4" = Field(..., alias="targetingExpression")

    model_config = {'populate_by_name': True}


class BidRecommendationPerTargetingExpressionV5(BaseModel):
    bid_values: list["BidValue"] = Field(..., alias="bidValues")
    suggested_bid_impact_metrics: Optional[Any] = Field(None, alias="suggestedBidImpactMetrics")
    targeting_expression: "TargetingExpressionV4" = Field(..., alias="targetingExpression")

    model_config = {'populate_by_name': True}


class BidSuggestion(BaseModel):
    """Suggested bid range in major and minor currency units (example: dollars and cents)."""
    bid_rec_id: Optional[str] = Field(None, alias="bidRecId", description="The bid recommendation id")
    range_end: Optional[float] = Field(None, alias="rangeEnd", description="The bid range end")
    range_start: Optional[float] = Field(None, alias="rangeStart", description="The bid range start")
    suggested: Optional[float] = Field(None, description="The suggested bid")

    model_config = {'populate_by_name': True}


class BidValues(BaseModel):
    """Suggested bid range"""
    range_end: Optional[float] = Field(None, alias="rangeEnd", description="The bid range end")
    range_start: Optional[float] = Field(None, alias="rangeStart", description="The bid range start")
    suggested: Optional[float] = Field(None, description="The suggested bid")

    model_config = {'populate_by_name': True}


class Bidding(BaseModel):
    """The bidding control configuration for the new campaign."""
    adjustments: Optional[list["Adjustment"]] = Field(None, description="Placement adjustment configuration for the campaign.")
    strategy: BiddingStrategy = Field(..., description="The bidding strategy selected for the campaign. Use LEGACY_FOR_SALES to lower your bid in real time when your ad may be ")

    model_config = {'populate_by_name': True}


class BiddingStrategyRecommendationAction(StrEnum):
    UPDATE = "UPDATE"


class BiddingStrategyRecommendationSuggestedbiddingstrategy(StrEnum):
    AUTO_FOR_SALES = "AUTO_FOR_SALES"
    LEGACY_FOR_SALES = "LEGACY_FOR_SALES"
    MANUAL = "MANUAL"


class BiddingStrategyRecommendation(BaseModel):
    """Contains suggested recommendation for the campaign bidding strategy."""
    action: Optional[BiddingStrategyRecommendationAction] = Field(None, description="Type of suggested action.")
    suggested_bidding_strategy: Optional[BiddingStrategyRecommendationSuggestedbiddingstrategy] = Field(None, alias="suggestedBiddingStrategy", description="The suggested bidding strategy value for the campaign. | Value | Strategy name | Description | |----------------|-------")

    model_config = {'populate_by_name': True}


class Brand(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="Id of brand. This field is REQUIRED if the Brand object is being used as an input. Use the GetRefinementsForCategory to ")
    name: Optional[str] = Field(None, description="Name of brand. This field is OPTIONAL if the Brand object is being used as an input.")

    model_config = {'populate_by_name': True}


class BrandLoP(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="Id of brand.")
    name: Optional[str] = Field(None, description="Name of brand.")

    model_config = {'populate_by_name': True}


class Brands(BaseModel):
    """List of Brands."""
    pass


class BrandsLoP(BaseModel):
    """List of Brands."""
    pass


class BudgetChangeType(StrEnum):
    PERCENT = "PERCENT"


class BudgetRecommendationAction(StrEnum):
    DECREASE = "DECREASE"
    INCREASE = "INCREASE"


class BudgetRecommendation(BaseModel):
    """Contains suggested recommendation for the campaign budget."""
    action: Optional[BudgetRecommendationAction] = Field(None, description="Type of suggested action.")
    suggested_budget: Optional[float] = Field(None, alias="suggestedBudget", description="The suggested budget value for the campaign.")

    model_config = {'populate_by_name': True}


class SPTORBudgetRecommendationError(BaseModel):
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class BudgetRecommendationError(BaseModel):
    error: "SPTORBudgetRecommendationError" = Field(..., alias="Error")
    campaign_id: str = Field(..., alias="campaignId", description="encrypted campaignId")
    index: int = Field(..., description="Correlate the recommendation to the campaign index in the request. Zero-based")

    model_config = {'populate_by_name': True}


class BudgetRuleRecommendation(BaseModel):
    rule_id: Optional[str] = Field(None, alias="ruleId", description="rule id for the recomemendation")
    rule_name: Optional[str] = Field(None, alias="ruleName", description="rule name for the recomemendation")
    suggested_budget_increase_percent: Optional[float] = Field(None, alias="suggestedBudgetIncreasePercent", description="suggested increase percent")

    model_config = {'populate_by_name': True}


class SevenDaysMissedOpportunities(BaseModel):
    end_date: Optional[str] = Field(None, alias="endDate", description="End date of the date range for which missed opportunity metrics are provided (YYYYMMDD). Local time")
    estimated_missed_clicks_lower: Optional[int] = Field(None, alias="estimatedMissedClicksLower", description="Lower bound estimate of the additional clicks the campaign might have generated if it had not run out of budget during t")
    estimated_missed_clicks_upper: Optional[int] = Field(None, alias="estimatedMissedClicksUpper", description="Upper bound estimate of the additional clicks the campaign might have generated if it had not run out of budget during t")
    estimated_missed_impressions_lower: Optional[int] = Field(None, alias="estimatedMissedImpressionsLower", description="Lower bound estimate of the additional impressions the campaign might have generated if it had not run out of budget dur")
    estimated_missed_impressions_upper: Optional[int] = Field(None, alias="estimatedMissedImpressionsUpper", description="Upper bound estimate of the additional impressions the campaign might have generated if it had not run out of budget dur")
    estimated_missed_sales_lower: Optional[float] = Field(None, alias="estimatedMissedSalesLower", description="Lower bound estimate of the additional sales the campaign might have generated if it had not run out of budget during th")
    estimated_missed_sales_upper: Optional[float] = Field(None, alias="estimatedMissedSalesUpper", description="Upper bound estimate of the additional sales the campaign might have generated if it had not run out of budget during th")
    percent_time_in_budget: Optional[float] = Field(None, alias="percentTimeInBudget", description="percentage of time the campaign is active with a budget. Provided as a decimal ranging from 0 to 1 (e.g. 0.76 means the ")
    start_date: Optional[str] = Field(None, alias="startDate", description="Starting date of the date range for which missed opportunity metrics are provided (YYYYMMDD). Local time")

    model_config = {'populate_by_name': True}


class BudgetRecommendationForExistingCampaign(BaseModel):
    budget_rule_recommendation: "BudgetRuleRecommendation" = Field(..., alias="budgetRuleRecommendation")
    campaign_id: str = Field(..., alias="campaignId", description="encrypted campaignId")
    index: int = Field(..., description="Correlate the recommendation to the campaign index in the request. Zero-based")
    seven_days_missed_opportunities: "SevenDaysMissedOpportunities" = Field(..., alias="sevenDaysMissedOpportunities")
    suggested_budget: float = Field(..., alias="suggestedBudget", description="recommended budget for the campaign.")

    model_config = {'populate_by_name': True}


class BudgetRecommendationNewCampaignsErrorMessage(BaseModel):
    pass


class BudgetRecommendationNewCampaignsException(BaseModel):
    message: Optional["BudgetRecommendationNewCampaignsErrorMessage"] = None

    model_config = {'populate_by_name': True}


class BudgetRecommendationRequest(BaseModel):
    campaign_ids: list[str] = Field(..., alias="campaignIds", description="List of campaigns.")

    model_config = {'populate_by_name': True}


class BudgetRecommendationResponse(BaseModel):
    budget_recommendations_error_results: list["BudgetRecommendationError"] = Field(..., alias="budgetRecommendationsErrorResults", description="List of errors that occured when generating bduget recommendation.")
    budget_recommendations_success_results: list["BudgetRecommendationForExistingCampaign"] = Field(..., alias="budgetRecommendationsSuccessResults", description="List of successful budget recomendation for campagins.")

    model_config = {'populate_by_name': True}


class BudgetRuleError(BaseModel):
    """The Error Response Object."""
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class BudgetRuleResponse(BaseModel):
    associated_campaign_ids: Optional[list[str]] = Field(None, alias="associatedCampaignIds")
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the error, if unsuccessful")
    rule_id: Optional[str] = Field(None, alias="ruleId", description="The rule identifier.")

    model_config = {'populate_by_name': True}


class BudgetRulesRelations(BaseModel):
    budget_rule_id: str = Field(..., alias="budgetRuleId", description="The rule identifier.")
    campaign_id: str = Field(..., alias="campaignId", description="The campaign identifier.")

    model_config = {'populate_by_name': True}


class BudgetUsageCampaign(BaseModel):
    budget: Optional[float] = Field(None, description="Budget amount of resource requested")
    budget_usage_percent: Optional[float] = Field(None, alias="budgetUsagePercent", description="Budget usage percentage (spend / available budget) for the given budget policy.")
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="ID of requested resource")
    index: Optional[float] = Field(None, description="An index to maintain order of the campaignIds")
    usage_updated_timestamp: Optional[str] = Field(None, alias="usageUpdatedTimestamp", description="Last evaluation time for budget usage")

    model_config = {'populate_by_name': True}


class BudgetUsageCampaignBatchError(BaseModel):
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="ID of requested resource")
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")
    index: Optional[float] = Field(None, description="An index to maintain order of the campaignIds")

    model_config = {'populate_by_name': True}


class BudgetUsageCampaignRequest(BaseModel):
    campaign_ids: Optional[list[str]] = Field(None, alias="campaignIds", description="A list of campaign IDs")

    model_config = {'populate_by_name': True}


class BudgetUsageCampaignResponse(BaseModel):
    error: Optional[list["BudgetUsageCampaignBatchError"]] = Field(None, description="List of budget usage percentages that failed to pull")
    success: Optional[list["BudgetUsageCampaign"]] = Field(None, description="List of budget usage percentages that were successfully pulled")

    model_config = {'populate_by_name': True}


class BudgetUsageError(BaseModel):
    """The Error Response Object."""
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class BulkBudgetRulesAssociationRequest(BaseModel):
    budget_rules_associations: Optional[list["BudgetRulesRelations"]] = Field(None, alias="budgetRulesAssociations", description="A list of budget rule campaign details.")

    model_config = {'populate_by_name': True}


class BulkBudgetRulesRelationsResponse(BaseModel):
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="The campaign identifier.")
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the error, if unsuccessful")
    index: Optional[int] = Field(None, description="The index of the request in the bulk request.")
    rule_id: Optional[str] = Field(None, alias="ruleId", description="The budget rule identifier.")

    model_config = {'populate_by_name': True}


class BulkBudgetRulesAssociationResponseBudgetrulesassociations(BaseModel):
    error_list: Optional[list["BulkBudgetRulesRelationsResponse"]] = Field(None, alias="errorList")
    success_list: Optional[list["BulkBudgetRulesRelationsResponse"]] = Field(None, alias="successList")

    model_config = {'populate_by_name': True}


class BulkBudgetRulesAssociationResponse(BaseModel):
    budget_rules_associations: Optional["BulkBudgetRulesAssociationResponseBudgetrulesassociations"] = Field(None, alias="budgetRulesAssociations")

    model_config = {'populate_by_name': True}


class BulkBudgetRulesDisAssociationRequest(BaseModel):
    budget_rules_dis_associations: Optional[list["BudgetRulesRelations"]] = Field(None, alias="budgetRulesDisAssociations", description="A list of budget rule campaign details.")

    model_config = {'populate_by_name': True}


class BulkBudgetRulesDisAssociationResponseBudgetrulesdisassociations(BaseModel):
    error_list: Optional[list["BulkBudgetRulesRelationsResponse"]] = Field(None, alias="errorList")
    success_list: Optional[list["BulkBudgetRulesRelationsResponse"]] = Field(None, alias="successList")

    model_config = {'populate_by_name': True}


class BulkBudgetRulesDisAssociationResponse(BaseModel):
    budget_rules_dis_associations: Optional["BulkBudgetRulesDisAssociationResponseBudgetrulesdisassociations"] = Field(None, alias="budgetRulesDisAssociations")

    model_config = {'populate_by_name': True}


class RecommendationType(StrEnum):
    BIDDING_STRATEGY = "BIDDING_STRATEGY"
    BUDGET_STRATEGY = "BUDGET_STRATEGY"
    KEYWORD = "KEYWORD"
    KEYWORD_GROUP = "KEYWORD_GROUP"
    PLACEMENT_BIDDING = "PLACEMENT_BIDDING"
    SHOPPER_COHORT = "SHOPPER_COHORT"


class Campaign(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign.")
    recommendation_type: "RecommendationType" = Field(..., alias="recommendationType")

    model_config = {'populate_by_name': True}


class RuleName(BaseModel):
    """The campaign optimization rule name."""
    pass


class RecurrenceType(StrEnum):
    DAILY = "DAILY"


class RuleStatus(StrEnum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"


class ComparisonOperator(StrEnum):
    EQUAL_TO = "EQUAL_TO"
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"


class RuleConditionMetric(StrEnum):
    AVERAGE_BID = "AVERAGE_BID"
    ROAS = "ROAS"


class RuleCondition(BaseModel):
    comparison_operator: "ComparisonOperator" = Field(..., alias="comparisonOperator")
    metric_name: "RuleConditionMetric" = Field(..., alias="metricName")
    threshold: float = Field(..., description="The performance threshold value.")

    model_config = {'populate_by_name': True}


class RuleConditionList(BaseModel):
    pass


class RuleCampaignId(BaseModel):
    """campaignId"""
    pass


class RuleCreationDate(BaseModel):
    """Time of campaign optimization rule creation in ISO 8061. Read-only."""
    pass


class campaignOptimizationId(BaseModel):
    """The persistent rule identifier."""
    pass


class RuleAction(StrEnum):
    ADOPT = "ADOPT"


class RuleType(StrEnum):
    BID = "BID"
    KEYWORD = "KEYWORD"
    PRODUCT = "PRODUCT"


class CampaignOptimizationRule(BaseModel):
    campaign_ids: Optional[list["RuleCampaignId"]] = Field(None, alias="campaignIds")
    campaign_optimization_id: "campaignOptimizationId" = Field(..., alias="campaignOptimizationId")
    created_date: Optional["RuleCreationDate"] = Field(None, alias="createdDate")
    recurrence: Optional["RecurrenceType"] = None
    rule_action: Optional["RuleAction"] = Field(None, alias="ruleAction")
    rule_condition: Optional["RuleConditionList"] = Field(None, alias="ruleCondition")
    rule_name: Optional["RuleName"] = Field(None, alias="ruleName")
    rule_status: Optional["RuleStatus"] = Field(None, alias="ruleStatus")
    rule_type: Optional["RuleType"] = Field(None, alias="ruleType")

    model_config = {'populate_by_name': True}


class CampaignOptimizationRuleError(BaseModel):
    """The Error Response Object."""
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class PlacementBiddingRecommendationAction(StrEnum):
    ADD = "ADD"
    DECREASE = "DECREASE"
    INCREASE = "INCREASE"
    REMOVE = "REMOVE"


class PlacementBiddingRecommendationPlacementtype(StrEnum):
    PLACEMENT_PRODUCT_PAGE = "PLACEMENT_PRODUCT_PAGE"
    PLACEMENT_REST_OF_SEARCH = "PLACEMENT_REST_OF_SEARCH"
    PLACEMENT_TOP = "PLACEMENT_TOP"


class PlacementBiddingRecommendation(BaseModel):
    """Contains suggested recommendation for a placement bid adjustment."""
    action: Optional[PlacementBiddingRecommendationAction] = Field(None, description="Type of suggested action.")
    incremental_impressions_lower_percent: Optional[int] = Field(None, alias="incrementalImpressionsLowerPercent", description="Lower bound of the estimated incremental impressions that could be gained if this optimization used")
    incremental_impressions_upper_percent: Optional[int] = Field(None, alias="incrementalImpressionsUpperPercent", description="Upper bound of the estimated incremental impressions that could be gained if this optimization used")
    placement_type: Optional[PlacementBiddingRecommendationPlacementtype] = Field(None, alias="placementType", description="The placement type.")
    suggested_bid_adjustment: Optional[int] = Field(None, alias="suggestedBidAdjustment", description="The suggested bid adjustment percent value for this placement type.")

    model_config = {'populate_by_name': True}


class TargetingGroupBidRecommendationAction(StrEnum):
    ADD = "ADD"
    DECREASE = "DECREASE"
    INCREASE = "INCREASE"
    REMOVE = "REMOVE"


class TargetingGroupBidRecommendationTargetinggroupexpression(StrEnum):
    CLOSE_MATCH = "CLOSE_MATCH"
    COMPLEMENTS = "COMPLEMENTS"
    LOOSE_MATCH = "LOOSE_MATCH"
    SUBSTITUTES = "SUBSTITUTES"


class TargetingGroupBidRecommendation(BaseModel):
    """Contains suggested recommendation for the auto targeting group."""
    action: Optional[TargetingGroupBidRecommendationAction] = Field(None, description="Type of suggested action.")
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="The ad group identifier.")
    suggested_bid: Optional[float] = Field(None, alias="suggestedBid", description="The suggested bid value associated with this targeting.")
    target_id: Optional[str] = Field(None, alias="targetId", description="The target identifier.")
    targeting_group_expression: Optional[TargetingGroupBidRecommendationTargetinggroupexpression] = Field(None, alias="targetingGroupExpression", description="The type of targeting group expression. | Value | Description | | --- | --- | | `LOOSE_MATCH` | This will show your ad t")

    model_config = {'populate_by_name': True}


class SevenDaysEstimatedOpportunities(BaseModel):
    end_date: Optional[str] = Field(None, alias="endDate", description="End date of the opportunities date range in YYYY-MM-DDTHH:mm:ssZ format.")
    estimated_incremental_clicks_lower: Optional[int] = Field(None, alias="estimatedIncrementalClicksLower", description="Lower bound of the estimated incremental clicks that could be gained if all optimizations are made.")
    estimated_incremental_clicks_upper: Optional[int] = Field(None, alias="estimatedIncrementalClicksUpper", description="Upper bound of the estimated incremental clicks that could be gained if all optimizations are made.")
    start_date: Optional[str] = Field(None, alias="startDate", description="Start date of the opportunities date range in YYYY-MM-DDTHH:mm:ssZ format.")

    model_config = {'populate_by_name': True}


class KeywordTargetingRecommendationAction(StrEnum):
    ADD = "ADD"
    DECREASE = "DECREASE"
    INCREASE = "INCREASE"
    REMOVE = "REMOVE"
    UPDATE = "UPDATE"


class KeywordTargetingRecommendationMatchtype(StrEnum):
    BROAD = "BROAD"
    EXACT = "EXACT"
    GROUP = "GROUP"
    PHRASE = "PHRASE"


class KeywordTargetingRecommendation(BaseModel):
    """Contains suggested recommendation for the keyword targeting."""
    action: Optional[KeywordTargetingRecommendationAction] = Field(None, description="Type of action for the keyword targeting.")
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="The ad group identifier.")
    keyword_id: Optional[str] = Field(None, alias="keywordId", description="The identifier of the keyword targeting.")
    keyword_text: Optional[str] = Field(None, alias="keywordText", description="The keyword text.")
    match_type: Optional[KeywordTargetingRecommendationMatchtype] = Field(None, alias="matchType", description="Keyword match type. | Value | Description | | --- | --- | | `BROAD` | Use BROAD to broadly match your keyword targeting ")
    suggested_bid: Optional[float] = Field(None, alias="suggestedBid", description="The suggested bid value associated with this keyword targeting clause.")

    model_config = {'populate_by_name': True}


class CampaignRecommendation(BaseModel):
    """This object contains a set of recommendations for a campaign across bid, budget, targeting."""
    bidding_strategy_recommendation: Optional["BiddingStrategyRecommendation"] = Field(None, alias="biddingStrategyRecommendation")
    budget_recommendation: Optional["BudgetRecommendation"] = Field(None, alias="budgetRecommendation")
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="The identifier of the campaign.")
    keyword_targeting_recommendations: Optional[list["KeywordTargetingRecommendation"]] = Field(None, alias="keywordTargetingRecommendations")
    placement_bidding_recommendations: Optional[list["PlacementBiddingRecommendation"]] = Field(None, alias="placementBiddingRecommendations")
    seven_days_estimated_opportunities: Optional["SevenDaysEstimatedOpportunities"] = Field(None, alias="sevenDaysEstimatedOpportunities")
    targeting_group_bid_recommendations: Optional[list["TargetingGroupBidRecommendation"]] = Field(None, alias="targetingGroupBidRecommendations")

    model_config = {'populate_by_name': True}


class CategoryItem(BaseModel):
    can_be_targeted: Optional[bool] = Field(None, alias="canBeTargeted", description="A flag which indicates if the current node may be targeted")
    id_: Optional[str] = Field(None, alias="id", description="The category id of the current node")
    name: Optional[str] = Field(None, description="The name of the category")
    parent: Optional[str] = Field(None, description="The category id of the parent node")
    path: Optional[str] = Field(None, description="The path of the category, which contains the current category and all parent categories")

    model_config = {'populate_by_name': True}


class IntegerRange(BaseModel):
    max: Optional[int] = None
    min: Optional[int] = None

    model_config = {'populate_by_name': True}


class CategoryItemWithAsinCounts(BaseModel):
    asin_counts: Optional["IntegerRange"] = Field(None, alias="asinCounts", description="An integer range between min and max")
    category_path: Optional[str] = Field(None, alias="categoryPath", description="The path of the category, which contains the current category and all parent categories")
    id_: Optional[str] = Field(None, alias="id", description="The category id of the current node")
    name: Optional[str] = Field(None, description="The name of the category")
    parent_category_id: Optional[str] = Field(None, alias="parentCategoryId", description="The category id of the parent node")

    model_config = {'populate_by_name': True}


class CategoryItemWithAsinCountsLoP(BaseModel):
    asin_counts: Optional["IntegerRange"] = Field(None, alias="asinCounts", description="The number of asins belonging to the category.")
    category_path: Optional[str] = Field(None, alias="categoryPath", description="The path of the category, which contains the current category and all parent categories")
    id_: Optional[str] = Field(None, alias="id", description="The category id of the current node")
    name: Optional[str] = Field(None, description="The name of the category")
    parent_category_id: Optional[str] = Field(None, alias="parentCategoryId", description="The category id of the parent node")
    translated_category_path: Optional[str] = Field(None, alias="translatedCategoryPath", description="The translated path of the category, which contains the current category and all parent categories.")
    translated_name: Optional[str] = Field(None, alias="translatedName", description="The translated name of the category.")

    model_config = {'populate_by_name': True}


class CategoryRecommendations(BaseModel):
    """Response object for the GetCategoryRecommendationsForAsins API."""
    categories: Optional[list["CategoryItem"]] = Field(None, description="List of category recommendations")

    model_config = {'populate_by_name': True}


class CategoryRecommendationsWithAsinCounts(BaseModel):
    """Response object for the GetCategoryRecommendationsForAsins API."""
    categories: Optional[list["CategoryItemWithAsinCounts"]] = Field(None, description="List of category recommendations")

    model_config = {'populate_by_name': True}


class CategoryRecommendationsWithAsinCountsLoP(BaseModel):
    """Response object for the GetCategoryRecommendationsForAsins API."""
    categories: Optional[list["CategoryItemWithAsinCountsLoP"]] = Field(None, description="List of category recommendations")

    model_config = {'populate_by_name': True}


class CountryCodes(BaseModel):
    """A list of country codes. Supported country codes: | Country Code |  Country            | |-------------|----------------------| | US          | United States        | | CA          | Canada           """
    pass


class CountryKeyword(BaseModel):
    bid: Optional[float] = Field(None, description="The bid value for the keyword, in minor currency units (example: cents). The default value will be the suggested bid.")
    user_selected_keyword: Optional[bool] = Field(None, alias="userSelectedKeyword", description="Flag that tells if keyword was selected by the user or was recommended by KRS")
    value: Optional[str] = Field(None, description="The keyword value")

    model_config = {'populate_by_name': True}


class CountryTargetMatchtype(StrEnum):
    BROAD = "BROAD"
    EXACT = "EXACT"
    PHRASE = "PHRASE"


class CountryTarget(BaseModel):
    country_keywords: Optional[dict[str, "CountryKeyword"]] = Field(None, alias="countryKeywords", description="Map represents the same keyword in a different countries and locales. Key is a 2-letter country code, value is a keyword")
    match_type: Optional[CountryTargetMatchtype] = Field(None, alias="matchType", description="Keyword match type. The default value will be BROAD.")

    model_config = {'populate_by_name': True}


class CreateAssociatedBudgetRulesRequest(BaseModel):
    budget_rule_ids: Optional[list[str]] = Field(None, alias="budgetRuleIds", description="A list of budget rule identifiers.")

    model_config = {'populate_by_name': True}


class CreateAssociatedBudgetRulesResponse(BaseModel):
    responses: Optional[list["AssociatedBudgetRuleResponse"]] = None

    model_config = {'populate_by_name': True}


class CreateBudgetRulesResponse(BaseModel):
    responses: Optional[list["BudgetRuleResponse"]] = None

    model_config = {'populate_by_name': True}


class timeOfDay(BaseModel):
    end_time: Optional[str] = Field(None, alias="endTime", description="The end time of intra-day budget rule window in the format 'hh:mm:ss'. Required to be greater than start-time.")
    start_time: Optional[str] = Field(None, alias="startTime", description="The start time of intra-day budget rule window in the format 'hh:mm:ss'")

    model_config = {'populate_by_name': True}


class DayOfWeek(StrEnum):
    FRIDAY = "FRIDAY"
    MONDAY = "MONDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"
    THURSDAY = "THURSDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"


class Recurrence(BaseModel):
    days_of_week: Optional[list["DayOfWeek"]] = Field(None, alias="daysOfWeek", description="Object representing days of the week for weekly type rule. It is not required for daily recurrence type")
    intra_day_schedule: Optional[list["timeOfDay"]] = Field(None, alias="intraDaySchedule", description="List of objects representing start and end time of desired intra-day budget rule window")
    type_: Optional["RecurrenceType"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class PerformanceMetric(StrEnum):
    ACOS = "ACOS"
    CTR = "CTR"
    CVR = "CVR"
    ROAS = "ROAS"


class PerformanceMeasureCondition(BaseModel):
    comparison_operator: "ComparisonOperator" = Field(..., alias="comparisonOperator")
    metric_name: "PerformanceMetric" = Field(..., alias="metricName")
    threshold: float = Field(..., description="The performance threshold value.")

    model_config = {'populate_by_name': True}


class SPRuleType(StrEnum):
    PERFORMANCE = "PERFORMANCE"
    SCHEDULE = "SCHEDULE"


class budgetIncreaseBy(BaseModel):
    type_: "BudgetChangeType" = Field(..., alias="type")
    value: float = Field(..., description="The budget value.")

    model_config = {'populate_by_name': True}


class EventTypeRuleDuration(BaseModel):
    """Object representing event type rule duration."""
    end_date: Optional[str] = Field(None, alias="endDate", description="The event end date in YYYYMMDD format. Read-only.")
    event_id: str = Field(..., alias="eventId", description="The event identifier. This value is available from the budget rules recommendation API.")
    event_name: Optional[str] = Field(None, alias="eventName", description="The event name. Read-only.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The event start date in YYYYMMDD format. Read-only. Note that this field is present only for announced events.")

    model_config = {'populate_by_name': True}


class DateRangeTypeRuleDuration(BaseModel):
    """Object representing date range type rule duration."""
    end_date: Optional[str] = Field(None, alias="endDate", description="The end date of the budget rule in YYYYMMDD format. The end date is inclusive. Required to be equal or greater than `sta")
    start_date: str = Field(..., alias="startDate", description="The start date of the budget rule in YYYYMMDD format. The start date is inclusive. Required to be greater than or equal ")

    model_config = {'populate_by_name': True}


class RuleDuration(BaseModel):
    date_range_type_rule_duration: Optional["DateRangeTypeRuleDuration"] = Field(None, alias="dateRangeTypeRuleDuration")
    event_type_rule_duration: Optional["EventTypeRuleDuration"] = Field(None, alias="eventTypeRuleDuration")

    model_config = {'populate_by_name': True}


class SPBudgetRuleDetails(BaseModel):
    """Object representing details of a budget rule for SP campaign"""
    budget_increase_by: Optional["budgetIncreaseBy"] = Field(None, alias="budgetIncreaseBy")
    duration: Optional["RuleDuration"] = None
    name: Optional[str] = Field(None, description="The budget rule name. Required to be unique within a campaign.")
    performance_measure_condition: Optional["PerformanceMeasureCondition"] = Field(None, alias="performanceMeasureCondition")
    recurrence: Optional["Recurrence"] = None
    rule_type: Optional["SPRuleType"] = Field(None, alias="ruleType")

    model_config = {'populate_by_name': True}


class CreateSPBudgetRulesRequest(BaseModel):
    budget_rules_details: Optional[list["SPBudgetRuleDetails"]] = Field(None, alias="budgetRulesDetails", description="A list of budget rule details.")

    model_config = {'populate_by_name': True}


class CreateSPCampaignOptimizationRulesRequest(BaseModel):
    campaign_ids: list["RuleCampaignId"] = Field(..., alias="campaignIds", description="A list of campaign ids")
    recurrence: "RecurrenceType"
    rule_action: "RuleAction" = Field(..., alias="ruleAction")
    rule_condition: Optional["RuleConditionList"] = Field(None, alias="ruleCondition")
    rule_name: Optional["RuleName"] = Field(None, alias="ruleName")
    rule_type: "RuleType" = Field(..., alias="ruleType")

    model_config = {'populate_by_name': True}


class CreateSPCampaignOptimizationRulesResponse(BaseModel):
    campaign_optimization_id: Optional["campaignOptimizationId"] = Field(None, alias="campaignOptimizationId")
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the error, if unsuccessful")

    model_config = {'populate_by_name': True}


class DeleteSPCampaignOptimizationRuleResponse(BaseModel):
    campaign_optimization_id: Optional["campaignOptimizationId"] = Field(None, alias="campaignOptimizationId")
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the error, if unsuccessful")

    model_config = {'populate_by_name': True}


class DisassociateAssociatedBudgetRuleResponse(BaseModel):
    pass


class ForecastEstimates(BaseModel):
    end_date: Optional[str] = Field(None, alias="endDate", description="End date of the opportunities date range in YYYY-MM-DDTHH:mm:ssZ format.")
    estimated_ad_spend_lower: Optional[float] = Field(None, alias="estimatedAdSpendLower", description="Lower estimated ad spend for the campaign.")
    estimated_ad_spend_upper: Optional[float] = Field(None, alias="estimatedAdSpendUpper", description="Upper estimated ad spend for the campaign.")
    estimated_incremental_clicks_lower: Optional[int] = Field(None, alias="estimatedIncrementalClicksLower", description="Lower bound of the estimated incremental clicks that could be gained if all optimizations are made.")
    estimated_incremental_clicks_upper: Optional[int] = Field(None, alias="estimatedIncrementalClicksUpper", description="Upper bound of the estimated incremental clicks that could be gained if all optimizations are made.")
    estimated_incremental_conversions_lower: Optional[int] = Field(None, alias="estimatedIncrementalConversionsLower", description="Lower estimated incremental number of conversions for the campaign.")
    estimated_incremental_conversions_upper: Optional[int] = Field(None, alias="estimatedIncrementalConversionsUpper", description="Upper estimated incremental number of conversions for the campaign.")
    estimated_incremental_impressions_lower: Optional[int] = Field(None, alias="estimatedIncrementalImpressionsLower", description="Lower estimated incremental number of impressions for the campaign.")
    estimated_incremental_impressions_upper: Optional[int] = Field(None, alias="estimatedIncrementalImpressionsUpper", description="Upper estimated incremental number of impressions for the campaign.")
    estimated_incremental_sales_lower: Optional[float] = Field(None, alias="estimatedIncrementalSalesLower", description="Lower estimated incremental sales for the campaign.")
    estimated_incremental_sales_upper: Optional[float] = Field(None, alias="estimatedIncrementalSalesUpper", description="Upper estimated incremental sales for the campaign.")
    start_date: Optional[str] = Field(None, alias="startDate", description="Start date of the opportunities date range in YYYY-MM-DDTHH:mm:ssZ format.")

    model_config = {'populate_by_name': True}


class Genre(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="Id of Genre. This field is REQUIRED if the Genre object is being used as an input. Use the GetRefinementsForCategory to ")
    name: Optional[str] = Field(None, description="Name of Genre. This field is OPTIONAL if the Genre object is being used as an input.")

    model_config = {'populate_by_name': True}


class GenreLoP(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="Id of Genre. Use the POST /sp/targets/category/{categoryId}/refinements endpoint to retrieve Genre Node IDs.")
    name: Optional[str] = Field(None, description="Name of Genre.")
    translated_name: Optional[str] = Field(None, alias="translatedName", description="Translated name of the Genre based off locale send in the query parameter.")

    model_config = {'populate_by_name': True}


class Genres(BaseModel):
    """List of Genres. Use the GetRefinementsForCategory to retrieve Genre Node IDs. Genres are only available for categories related to books."""
    pass


class GenresLoP(BaseModel):
    """List of Genres in a language of preference (LoP). Use the POST /sp/targets/category/{categoryId}/refinements endpoint to retrieve Genre Node IDs. Genres are only available for categories related to bo"""
    pass


class GetCampaignRecommendationsRequestV2(BaseModel):
    campaigns: list["Campaign"] = Field(..., description="List of campaigns with specific recommendation types requested.")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Optional. Limits the number of items to return in the response.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional. Token to retrieve subsequent page of results.")

    model_config = {'populate_by_name': True}


class GetCampaignRecommendationsResponse(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="An identifier to fetch next set of campaign recommendations records in the result set if available. This will be null wh")
    recommendations: list["CampaignRecommendation"] = Field(..., description="List of campaign recommendations.")

    model_config = {'populate_by_name': True}


class ShopperCohortBiddingRecommendationAction(StrEnum):
    ADD = "ADD"
    REMOVE = "REMOVE"
    UPDATE = "UPDATE"


class ShopperCohortBiddingRecommendationShoppercohorttype(StrEnum):
    AUDIENCE_SEGMENT = "AUDIENCE_SEGMENT"


class ShopperCohortBiddingRecommendation(BaseModel):
    action: ShopperCohortBiddingRecommendationAction = Field(..., description="Recommended action for shopper cohort bidding.")
    audience_segments: list["AudienceSegment"] = Field(..., alias="audienceSegments", description="List of audience segments for this recommendation.")
    percentage: int = Field(..., description="Bid adjustment percentage (basis points, e.g., 900 = 9%).")
    shopper_cohort_type: ShopperCohortBiddingRecommendationShoppercohorttype = Field(..., alias="shopperCohortType", description="Type of shopper cohort.")

    model_config = {'populate_by_name': True}


class RecommendationDetails(BaseModel):
    """Contains one or more recommendation details of different types."""
    bidding_strategy_recommendation: Optional["BiddingStrategyRecommendation"] = Field(None, alias="biddingStrategyRecommendation")
    budget_recommendation: Optional["BudgetRecommendation"] = Field(None, alias="budgetRecommendation")
    keyword_targeting_recommendations: Optional[list["KeywordTargetingRecommendation"]] = Field(None, alias="keywordTargetingRecommendations", description="List of keyword targeting recommendations.")
    placement_bidding_recommendations: Optional[list["PlacementBiddingRecommendation"]] = Field(None, alias="placementBiddingRecommendations", description="List of placement bid recommendations.")
    shopper_cohort_bidding_recommendation: Optional["ShopperCohortBiddingRecommendation"] = Field(None, alias="shopperCohortBiddingRecommendation")
    targeting_group_bid_recommendations: Optional[list["TargetingGroupBidRecommendation"]] = Field(None, alias="targetingGroupBidRecommendations", description="List of targeting group bid recommendations.")

    model_config = {'populate_by_name': True}


class Recommendation(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign.")
    forecast_estimates: Optional["ForecastEstimates"] = Field(None, alias="forecastEstimates")
    recommendation_details: "RecommendationDetails" = Field(..., alias="recommendationDetails")
    recommendation_type: "RecommendationType" = Field(..., alias="recommendationType")

    model_config = {'populate_by_name': True}


class GetCampaignRecommendationsResponseV2(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="An identifier to fetch next set of recommendations records in the result set if available. This will be null when at the")
    recommendations: list["Recommendation"] = Field(..., description="List of recommendations.")

    model_config = {'populate_by_name': True}


class GetCategoryRecommendationsForAsinsRequest(BaseModel):
    """Request object to retrieve Category Recommendations based on the input ASINs."""
    asins: Optional[list[str]] = Field(None, description="List of input ASINs. This API does not check if the ASINs are valid ASINs.")
    include_ancestor: Optional[bool] = Field(None, alias="includeAncestor", description="Enable this if you would like to retrieve categories which are ancestor nodes of the original recommended categories. Th")

    model_config = {'populate_by_name': True}


class GetProductRecommendationsRequest(BaseModel):
    """Request structure to get ASIN recommendations for a set of input ASINs."""
    ad_asins: list[str] = Field(..., alias="adAsins", description="List of input ASINs.")
    count: Optional[int] = Field(None, description="Count of objects requested in the response. The count will be applied on the objects returned under `recommendations` ar")
    cursor: Optional[str] = Field(None, description="A optional cursor value that can be used to fetch next or previous set of records.")
    locale: Optional[str] = Field(None, description="Theme names and descriptions will be provided in the language for your supported locale. Available options are en_US (U.")

    model_config = {'populate_by_name': True}


class state(StrEnum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"


class SPBudgetRule(BaseModel):
    created_date: Optional[float] = Field(None, alias="createdDate", description="Epoch time of budget rule creation. Read-only.")
    last_updated_date: Optional[float] = Field(None, alias="lastUpdatedDate", description="Epoch time of budget rule update. Read-only.")
    rule_details: Optional["SPBudgetRuleDetails"] = Field(None, alias="ruleDetails")
    rule_id: str = Field(..., alias="ruleId", description="The budget rule identifier.")
    rule_state: Optional["state"] = Field(None, alias="ruleState")
    rule_status: Optional[str] = Field(None, alias="ruleStatus", description="The budget rule status. Read-only.")

    model_config = {'populate_by_name': True}


class GetSPBudgetRuleResponse(BaseModel):
    budget_rule: Optional["SPBudgetRule"] = Field(None, alias="budgetRule")

    model_config = {'populate_by_name': True}


class GetSPBudgetRulesForAdvertiserResponse(BaseModel):
    budget_rules_for_advertiser_response: Optional[list["SPBudgetRule"]] = Field(None, alias="budgetRulesForAdvertiserResponse", description="A list of rules created by the advertiser.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` ")

    model_config = {'populate_by_name': True}


class GetSPCampaignOptimizationRuleResponse(BaseModel):
    campaign_optimization_rule: Optional["CampaignOptimizationRule"] = Field(None, alias="CampaignOptimizationRule")

    model_config = {'populate_by_name': True}


class PriceRange(BaseModel):
    """A range of prices. We use this to retrieve the number of targetable ASINs that falls within this price range."""
    max: Optional[float] = None
    min: Optional[float] = None

    model_config = {'populate_by_name': True}


class RatingRange(BaseModel):
    """Rating range is restricted to integers between 0 and 5, inclusive. Min must be less than or equal to max. We use this to retrieve the number of targetable ASINs that falls within this rating range."""
    max: Optional[int] = None
    min: Optional[int] = None

    model_config = {'populate_by_name': True}


class GetTargetableAsinCountsRequest(BaseModel):
    age_ranges: Optional["AgeRanges"] = Field(None, alias="ageRanges")
    brands: Optional["Brands"] = None
    category: str = Field(..., description="The category node id. Please use the GetTargetableCategories API or GetCategoryRecommendationsForASINs API to retrieve c")
    genres: Optional["Genres"] = None
    is_prime_shipping: Optional[bool] = Field(None, alias="isPrimeShipping", description="Indicates if products have prime shipping")
    price_range: Optional["PriceRange"] = Field(None, alias="priceRange")
    rating_range: Optional["RatingRange"] = Field(None, alias="ratingRange")

    model_config = {'populate_by_name': True}


class GlobalRankedKeywordTargetsForAdGroupRequest(BaseModel):
    """This request type is used to retrieve recommended keyword targets for an existing ad group. Set the recommendationType to KEYWORDS_FOR_ADGROUP to use this request type."""
    targets: Optional[list["CountryTarget"]] = Field(None, description="A list of targets that need to be ranked")

    model_config = {'populate_by_name': True}


class GlobalRankedKeywordTargetsForAsinsRequest(BaseModel):
    """This request type is used to retrieve recommended keyword targets for ASINs. Set the recommendationType to KEYWORDS_FOR_ASINS to use this request type."""
    products: Optional[list[dict[str, "ProductDetails"]]] = Field(None, description="It represents an array list of countryProducts. CountryProducts is a map representing same product in a different market")
    targets: Optional[list["CountryTarget"]] = Field(None, description="An array list of countryTargets. CountryTarget is an object with CountryKeywords map representing same keyword in a diff")

    model_config = {'populate_by_name': True}


class ThemedBidMatchtype(StrEnum):
    BROAD = "BROAD"
    EXACT = "EXACT"
    PHRASE = "PHRASE"


class ThemedBid(BaseModel):
    bid: Optional[float] = Field(None, description="The bid value for the keyword, in minor currency units (example: cents). The default value will be the suggested bid.")
    match_type: Optional[ThemedBidMatchtype] = Field(None, alias="matchType", description="Keyword match type. The default value will be BROAD.")
    rank: Optional[float] = Field(None, description="The keyword target rank.")
    suggested_bid: Optional["BidValues"] = Field(None, alias="suggestedBid")
    theme: Optional[str] = Field(None, description="The theme of the bid recommendation. The default theme is CONVERSION_OPPORTUNITIES.")

    model_config = {'populate_by_name': True}


class RankedTargetWithThemedBids(BaseModel):
    bid_info: Optional[list["ThemedBid"]] = Field(None, alias="bidInfo", description="A list of keyword bid info")
    keyword: Optional[str] = Field(None, description="The keyword value")
    rec_id: Optional[str] = Field(None, alias="recId", description="The recommended keyword target id")
    search_term_impression_rank: Optional[float] = Field(None, alias="searchTermImpressionRank", description="The account-level ad-attributed impression rank for the search-term/keyword. Provides [1:N] place the advertiser ranks a")
    search_term_impression_share: Optional[float] = Field(None, alias="searchTermImpressionShare", description="The account-level ad-attributed impression share for the search-term/keyword. Provides percentage share of all ad impres")
    translation: Optional[str] = Field(None, description="The translation of keyword if a locale is passed in")
    user_selected_keyword: Optional[bool] = Field(None, alias="userSelectedKeyword", description="Flag that tells if keyword was selected by the user or was recommended by KRS")

    model_config = {'populate_by_name': True}


class RankedTargetWithThemedBidsList(BaseModel):
    pass


class RangeMetricValue(BaseModel):
    """Describes lower and upper bounds of the range. <br> Note: This object is nullable"""
    lower: Optional[int] = None
    upper: Optional[int] = None

    model_config = {'populate_by_name': True}


class ImpactMetric(BaseModel):
    """The impact metrics are given in the same order of suggested bids. <br> Note: This object is nullable"""
    values: Optional[list["RangeMetricValue"]] = None

    model_config = {'populate_by_name': True}


class ImpactMetrics(BaseModel):
    """For the CONVERSION_OPPORTUNITIES theme, the impact metrics are weekly clicks and orders received for similar products. For other event-based themes, the impact metrics are clicks and orders received f"""
    clicks: Optional["ImpactMetric"] = None
    orders: Optional["ImpactMetric"] = None

    model_config = {'populate_by_name': True}


class RankedTargetWithThemedBidsResponse(BaseModel):
    impact_metrics: Optional[list["ImpactMetrics"]] = Field(None, alias="impactMetrics", description="A list of impact metrics which anticipates the number of clicks and orders you will receive if you target all targeting ")
    keyword_target_list: Optional["RankedTargetWithThemedBidsList"] = Field(None, alias="keywordTargetList")

    model_config = {'populate_by_name': True}


class GlobalRankedTargetWithThemedBidsResponse(BaseModel):
    country_codes: Optional[dict[str, "RankedTargetWithThemedBidsResponse"]] = Field(None, alias="countryCodes")

    model_config = {'populate_by_name': True}


class InitialBudgetRecommendationRequestTargetingtype(StrEnum):
    AUTO = "auto"
    MANUAL = "manual"


class InitialBudgetRecommendationRequest(BaseModel):
    ad_groups: list["AdGroup"] = Field(..., alias="adGroups", description="The ad group information for this new campaign.")
    bidding: "Bidding"
    end_date: Optional[str] = Field(None, alias="endDate", description="The end date of the campaign in YYYYMMDD format.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The start date of the campaign in YYYYMMDD format.")
    targeting_type: InitialBudgetRecommendationRequestTargetingtype = Field(..., alias="targetingType", description="Specifies the targeting type.")

    model_config = {'populate_by_name': True}


class SpecialEvent(BaseModel):
    benchmark: Optional["Benchmark"] = None
    budget_modifier: Optional[float] = Field(None, alias="budgetModifier", description="Deprecated. The factor used to boost the recommended budget.")
    daily_budget: Optional[float] = Field(None, alias="dailyBudget", description="Recommended daily budget for the new campaign during the special event period.")
    end_date: Optional[str] = Field(None, alias="endDate", description="The end date of the special event in YYYYMMDD format.")
    event_key: Optional[str] = Field(None, alias="eventKey", description="The key of the special event.")
    event_name: Optional[str] = Field(None, alias="eventName", description="The name of the special event.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The start date of the special event in YYYYMMDD format.")

    model_config = {'populate_by_name': True}


class InitialBudgetRecommendationResponse(BaseModel):
    benchmark: "Benchmark"
    daily_budget: float = Field(..., alias="dailyBudget", description="Recommended daily budget for the new campaign. Note: value -1 means we don’t have enough information to provide a recomm")
    recommendation_id: Optional[str] = Field(None, alias="recommendationId", description="Unique identifier for each recommendation.")
    special_events: list["SpecialEvent"] = Field(..., alias="specialEvents", description="A list of special events around the start and end date of the campaign.")

    model_config = {'populate_by_name': True}


class InternalServerException(BaseModel):
    """Returns information about an InternalServerException."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class KeywordBidInfoMatchtype(StrEnum):
    BROAD = "BROAD"
    EXACT = "EXACT"
    PHRASE = "PHRASE"


class KeywordBidInfo(BaseModel):
    bid: Optional[float] = Field(None, description="The bid value for the keyword, in minor currency units (example: cents). The default value will be the suggested bid.")
    match_type: Optional[KeywordBidInfoMatchtype] = Field(None, alias="matchType", description="Keyword match type. The default value will be BROAD.")
    rank: Optional[float] = Field(None, description="The keyword target rank")
    suggested_bid: Optional["BidSuggestion"] = Field(None, alias="suggestedBid")

    model_config = {'populate_by_name': True}


class KeywordGroup(BaseModel):
    """Keyword group. Represents a high level keyword targeting intent. e.g. the keyword group 'gift' can target relevant search queries containing the word gift"""
    description: Optional[str] = Field(None, description="Detailed Keyword group description.")
    id_: str = Field(..., alias="id", description="Unique Identifier for the keyword group. To be passed during targeting clause creation.")
    impact_summary: Optional[str] = Field(None, alias="impactSummary", description="Summary of impacts.")
    sample_keywords: Optional[list[str]] = Field(None, alias="sampleKeywords", description="Sample keywords that match the group.")
    text: str = Field(..., description="Keyword group text. Can be used for display purposes.")

    model_config = {'populate_by_name': True}


class KeywordGroupsRecommendationsRequest(BaseModel):
    """Keyword groups request."""
    asins: list[str] = Field(..., description="List of ASINs.")
    country_code: Optional[str] = Field(None, alias="countryCode", description="The country code representing the origin country of the input ASIN list, it will be used for generating keyword group re")
    next_token: Optional[str] = Field(None, alias="nextToken", description="If the last response included this field then there are more items to retrieve.")

    model_config = {'populate_by_name': True}


class KeywordGroupsRecommendationsResponse(BaseModel):
    """Keyword group recommendations response."""
    country_code: Optional[str] = Field(None, alias="countryCode", description="The country code representing the origin country of the input ASIN list, used for generating keyword group recommendatio")
    keyword_groups: list["KeywordGroup"] = Field(..., alias="keywordGroups", description="Keyword group recommendations for input list of ASINs.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="If present then there is more data to retrieve. To retrieve, resend request with token.")

    model_config = {'populate_by_name': True}


class KeywordTargetResponse(BaseModel):
    rank: Optional[float] = Field(None, description="The keyword target rank")
    suggested_bid: Optional["BidSuggestion"] = Field(None, alias="suggestedBid")
    translation: Optional[str] = Field(None, description="The translation of keyword if a locale is passed in")

    model_config = {'populate_by_name': True}


class MultiCountryTargetingExpressionType(StrEnum):
    CLOSE_MATCH = "CLOSE_MATCH"
    COMPLEMENTS = "COMPLEMENTS"
    KEYWORD_BROAD_MATCH = "KEYWORD_BROAD_MATCH"
    KEYWORD_EXACT_MATCH = "KEYWORD_EXACT_MATCH"
    KEYWORD_GROUP = "KEYWORD_GROUP"
    KEYWORD_PHRASE_MATCH = "KEYWORD_PHRASE_MATCH"
    LOOSE_MATCH = "LOOSE_MATCH"
    PAT_ASIN = "PAT_ASIN"
    PAT_CATEGORY = "PAT_CATEGORY"
    PAT_CATEGORY_REFINEMENT = "PAT_CATEGORY_REFINEMENT"
    SUBSTITUTES = "SUBSTITUTES"


class MultiCountryTargetingExpression(BaseModel):
    """The targeting expression. The `type` property specifies the targeting option. Use `CLOSE_MATCH` to match your auto targeting ads closely to the specified value. Use `LOOSE_MATCH` to match your auto ta"""
    country_values: Optional[Any] = Field(None, alias="countryValues")
    type_: "MultiCountryTargetingExpressionType" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class MultiCountryTargetingExpressionList(BaseModel):
    """The list of targeting expressions. Maximum of 100 per request per country, use pagination for more if needed."""
    pass


class MultiCountryAdGroupThemeBasedBidRecommendationRequestRecommendationtype(StrEnum):
    BIDS_FOR_EXISTING_AD_GROUP = "BIDS_FOR_EXISTING_AD_GROUP"


class MultiCountryAdGroupThemeBasedBidRecommendationRequest(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The ad group identifier.")
    campaign_id: str = Field(..., alias="campaignId", description="The campaign identifier.")
    country_codes: Optional["CountryCodes"] = Field(None, alias="countryCodes")
    include_analysis: Optional[bool] = Field(None, alias="includeAnalysis", description="Flag to include new bid analyzer data.")
    recommendation_type: MultiCountryAdGroupThemeBasedBidRecommendationRequestRecommendationtype = Field(..., alias="recommendationType", description="The bid recommendation type.")
    targeting_expressions: "MultiCountryTargetingExpressionList" = Field(..., alias="targetingExpressions")

    model_config = {'populate_by_name': True}


class MultiCountryProduct(BaseModel):
    """This field provides the details for multi country product."""
    __root__: dict[str, "ProductDetails"] = {}


class MultiCountryAsinsThemeBasedBidRecommendationRequestBidding(BaseModel):
    """Bidding control configuration for the campaign."""
    adjustments: Optional[list["BidPlacementAdjustment"]] = Field(None, description="Placement adjustment configuration for the campaign.")
    strategy: "BiddingStrategy"

    model_config = {'populate_by_name': True}


class MultiCountryAsinsThemeBasedBidRecommendationRequestRecommendationtype(StrEnum):
    BIDS_FOR_NEW_AD_GROUP = "BIDS_FOR_NEW_AD_GROUP"


class MultiCountryAsinsThemeBasedBidRecommendationRequest(BaseModel):
    bidding: "MultiCountryAsinsThemeBasedBidRecommendationRequestBidding" = Field(..., description="Bidding control configuration for the campaign.")
    country_codes: "CountryCodes" = Field(..., alias="countryCodes")
    include_analysis: Optional[bool] = Field(None, alias="includeAnalysis", description="Flag to include new bid analyzer data.")
    products: Optional[list["MultiCountryProduct"]] = Field(None, description="This represents the list of products in the request.")
    recommendation_type: MultiCountryAsinsThemeBasedBidRecommendationRequestRecommendationtype = Field(..., alias="recommendationType", description="The bid recommendation type.")
    targeting_expressions: "MultiCountryTargetingExpressionList" = Field(..., alias="targetingExpressions")

    model_config = {'populate_by_name': True}


class MultiCountryBidAnalysesPerTargetingExpression(BaseModel):
    country_bid_analyses: Optional[Any] = Field(None, alias="countryBidAnalyses")
    expression: "MultiCountryTargetingExpression"

    model_config = {'populate_by_name': True}


class MultiCountryBidRecommendationError(BaseModel):
    code: Optional[str] = Field(None, description="Machine readable error code.")
    country_codes: Optional[list[str]] = Field(None, alias="countryCodes", description="Countries where error have occurred")
    message: Optional[str] = Field(None, description="Human readable 1 liner error message")

    model_config = {'populate_by_name': True}


class SuggestedBidValues(BaseModel):
    pass


class MultiCountryBidRecommendationPerTargetingExpression(BaseModel):
    country_suggested_bids: Any = Field(..., alias="countrySuggestedBids")
    expression: "MultiCountryTargetingExpression"

    model_config = {'populate_by_name': True}


class Theme(StrEnum):
    BFCM_HOLIDAY = "BFCM_HOLIDAY"
    CONVERSION_OPPORTUNITIES = "CONVERSION_OPPORTUNITIES"
    FALL_PRIME_DEAL_EVENT = "FALL_PRIME_DEAL_EVENT"
    PRIME_DAY = "PRIME_DAY"


class MultiCountryThemeBasedBidRecommendation(BaseModel):
    bid_analyses_for_targeting_expressions: Optional[list["MultiCountryBidAnalysesPerTargetingExpression"]] = Field(None, alias="bidAnalysesForTargetingExpressions", description="The bid analyses for targeting expressions listed in the request.")
    bid_recommendations_for_targeting_expressions: list["MultiCountryBidRecommendationPerTargetingExpression"] = Field(..., alias="bidRecommendationsForTargetingExpressions", description="The bid recommendations for targeting expressions listed in the request.")
    theme: "Theme"

    model_config = {'populate_by_name': True}


class MultiCountryThemeBasedBidRecommendationCompleteFailureResponse(BaseModel):
    errors: list["MultiCountryBidRecommendationError"] = Field(..., description="List of errors occurred while processing multi country request.")

    model_config = {'populate_by_name': True}


class MultiCountryThemeBasedBidRecommendationResponse(BaseModel):
    """A list of multi country bid recommendation themes and associated bid recommendations."""
    bid_recommendations: list["MultiCountryThemeBasedBidRecommendation"] = Field(..., alias="bidRecommendations")
    errors: Optional[list["MultiCountryBidRecommendationError"]] = Field(None, description="List of errors occurred while processing multi country request.")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerRuleActionOperator(StrEnum):
    INCREMENT = "INCREMENT"


class OptimizationRulesAPISwaggerActionDetailsActionunit(StrEnum):
    PERCENT = "PERCENT"


class OptimizationRulesAPISwaggerActionDetails(BaseModel):
    """Details of a rule action."""
    action_operator: "OptimizationRulesAPISwaggerRuleActionOperator" = Field(..., alias="actionOperator")
    action_unit: OptimizationRulesAPISwaggerActionDetailsActionunit = Field(..., alias="actionUnit")
    value: float = Field(..., description="An integer between 1 & 100, representing the percent increase on base bid.")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerActionType(StrEnum):
    ADOPT = "ADOPT"


class OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignRequest(BaseModel):
    """Request body for create campaign to optimization rules association. Maximum 100 rules can be associated to each campaign."""
    optimization_rule_ids: list[str] = Field(..., alias="optimizationRuleIds", description="An array of rule identifiers.")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerSingleOptimizationRuleAssociationResponse(BaseModel):
    """Response object for operations involving associating a single optimization rule."""
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the error, if unsuccessful.")
    optimization_rule_id: Optional[str] = Field(None, alias="optimizationRuleId", description="The rule identifier.")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignResponse(BaseModel):
    """Response object for create campaign to optimization rules association."""
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    responses: Optional[list["OptimizationRulesAPISwaggerSingleOptimizationRuleAssociationResponse"]] = None

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class OptimizationRulesAPISwaggerEntityFieldFilter(BaseModel):
    """Filter type and value pair."""
    filter_type: Optional["OptimizationRulesAPISwaggerFilterType"] = Field(None, alias="filterType")
    values: Optional[list[str]] = None

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerCampaignFilter(BaseModel):
    """Filter on campaigns. This filter only returns associated Bid and Targeting rules, and it does not return budget rules."""
    campaign_id: Optional["OptimizationRulesAPISwaggerEntityFieldFilter"] = Field(None, alias="campaignId")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerComparisonOperator(StrEnum):
    EQUAL_TO = "EQUAL_TO"
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"


class OptimizationRulesAPISwaggerRuleSubCategory(StrEnum):
    SCHEDULE = "SCHEDULE"


class OptimizationRulesAPISwaggerRuleStatus(StrEnum):
    ENABLED = "ENABLED"
    ENDED = "ENDED"
    PAUSED = "PAUSED"
    SCHEDULED = "SCHEDULED"


class OptimizationRulesAPISwaggerRuleCategory(StrEnum):
    BID = "BID"


class OptimizationRulesAPISwaggerDayOfTheWeek(StrEnum):
    FRIDAY = "FRIDAY"
    MONDAY = "MONDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"
    THURSDAY = "THURSDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"


class OptimizationRulesAPISwaggerRuleRecurrenceType(StrEnum):
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"


class OptimizationRulesAPISwaggerDuration(BaseModel):
    """The duration of an optimization rule based on special events (example: Prime Day) or custom date ranges."""
    end_time: Optional[str] = Field(None, alias="endTime", description="Time of optimization rule completion in ISO 8061.")
    event_id: Optional[str] = Field(None, alias="eventId", description="Identifier for the event during which the rule is applied.")
    event_name: Optional[str] = Field(None, alias="eventName", description="Name of the event during which the rule is applied.")
    start_time: Optional[str] = Field(None, alias="startTime", description="Time of optimization rule creation in ISO 8061. Not Required only when eventId present.")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerRuleRecurrenceTimesofday(BaseModel):
    """List of times of the day."""
    end_time: str = Field(..., alias="endTime", description="Time of the day in HH:00.")
    start_time: str = Field(..., alias="startTime", description="Time of the day in HH:00.")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerRuleRecurrence(BaseModel):
    """The recurrence of the optimization rule application."""
    days_of_week: Optional[list["OptimizationRulesAPISwaggerDayOfTheWeek"]] = Field(None, alias="daysOfWeek", description="A list of days of the week.")
    duration: "OptimizationRulesAPISwaggerDuration"
    times_of_day: Optional[list["OptimizationRulesAPISwaggerRuleRecurrenceTimesofday"]] = Field(None, alias="timesOfDay", description="List of times of the day.")
    type_: "OptimizationRulesAPISwaggerRuleRecurrenceType" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerValueTypeRuleCriteria(BaseModel):
    """Represents a criteria by comparing with the rule attribute value."""
    comparison_operator: "OptimizationRulesAPISwaggerComparisonOperator" = Field(..., alias="comparisonOperator")
    value: float

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerRangeTypeRuleCriteria(BaseModel):
    """Represents the range of rule attribute value. NOT SUPPORTED right now"""
    max_value: float = Field(..., alias="maxValue")
    min_value: float = Field(..., alias="minValue")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerRuleCriteria(BaseModel):
    pass


class OptimizationRulesAPISwaggerRuleAttribute(StrEnum):
    ROAS = "ROAS"


class OptimizationRulesAPISwaggerRuleCondition(BaseModel):
    attribute_name: Optional["OptimizationRulesAPISwaggerRuleAttribute"] = Field(None, alias="attributeName")
    criteria: Optional["OptimizationRulesAPISwaggerRuleCriteria"] = None

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerRuleAction(BaseModel):
    """Action to be taken by the rule."""
    action_details: "OptimizationRulesAPISwaggerActionDetails" = Field(..., alias="actionDetails")
    action_type: "OptimizationRulesAPISwaggerActionType" = Field(..., alias="actionType")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerOptimizationRuleWithoutRuleId(BaseModel):
    action: "OptimizationRulesAPISwaggerRuleAction"
    conditions: Optional[list["OptimizationRulesAPISwaggerRuleCondition"]] = None
    recurrence: "OptimizationRulesAPISwaggerRuleRecurrence"
    rule_category: "OptimizationRulesAPISwaggerRuleCategory" = Field(..., alias="ruleCategory")
    rule_name: Optional[str] = Field(None, alias="ruleName", description="The rule name.")
    rule_sub_category: "OptimizationRulesAPISwaggerRuleSubCategory" = Field(..., alias="ruleSubCategory")
    status: Optional["OptimizationRulesAPISwaggerRuleStatus"] = None

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerCreateOptimizationRulesRequest(BaseModel):
    """Request object for creating one or multiple optimization rules."""
    optimization_rules: list["OptimizationRulesAPISwaggerOptimizationRuleWithoutRuleId"] = Field(..., alias="optimizationRules")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerRuleSubCategoryV2(StrEnum):
    PERFORMANCE = "PERFORMANCE"
    SCHEDULE = "SCHEDULE"


class OptimizationRulesAPISwaggerRuleAttributeV2(StrEnum):
    ACOS = "ACOS"
    CLICKS = "CLICKS"
    CPC = "CPC"
    CTR = "CTR"
    CVR = "CVR"
    IMPRESSIONS = "IMPRESSIONS"
    ORDERS = "ORDERS"
    ROAS = "ROAS"
    SALES = "SALES"
    SPEND = "SPEND"


class OptimizationRulesAPISwaggerRuleConditionV2(BaseModel):
    attribute_name: Optional["OptimizationRulesAPISwaggerRuleAttributeV2"] = Field(None, alias="attributeName")
    criteria: Optional["OptimizationRulesAPISwaggerRuleCriteria"] = Field(None, description="Only Value Type Criteria is supported right now.")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerRuleCategoryV2(StrEnum):
    BID = "BID"
    BUDGET = "BUDGET"
    TARGETING = "TARGETING"


class OptimizationRulesAPISwaggerExpressionType(StrEnum):
    BROAD = "BROAD"
    EXACT = "EXACT"
    EXPANDED = "EXPANDED"
    PHRASE = "PHRASE"


class OptimizationRulesAPISwaggerTargetingType(StrEnum):
    KEYWORD = "KEYWORD"
    PRODUCT = "PRODUCT"


class OptimizationRulesAPISwaggerRuleTargeting(BaseModel):
    expression_types: list["OptimizationRulesAPISwaggerExpressionType"] = Field(..., alias="expressionTypes")
    lookback_days: int = Field(..., alias="lookbackDays", description="The number of days of data to look back on for the rule.")
    targeting_type: "OptimizationRulesAPISwaggerTargetingType" = Field(..., alias="targetingType")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerOptimizationRuleWithoutRuleIdV2(BaseModel):
    action: Optional["OptimizationRulesAPISwaggerRuleAction"] = None
    conditions: Optional[list["OptimizationRulesAPISwaggerRuleConditionV2"]] = None
    recurrence: Optional["OptimizationRulesAPISwaggerRuleRecurrence"] = None
    rule_category: "OptimizationRulesAPISwaggerRuleCategoryV2" = Field(..., alias="ruleCategory")
    rule_name: str = Field(..., alias="ruleName", description="The rule name.")
    rule_sub_category: "OptimizationRulesAPISwaggerRuleSubCategoryV2" = Field(..., alias="ruleSubCategory")
    status: "OptimizationRulesAPISwaggerRuleStatus"
    targeting: Optional[list["OptimizationRulesAPISwaggerRuleTargeting"]] = None

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerCreateOptimizationRulesRequestV2(BaseModel):
    """Request object for creating one or multiple optimization rules.  Budget rules are not supported for this operation."""
    optimization_rules: list["OptimizationRulesAPISwaggerOptimizationRuleWithoutRuleIdV2"] = Field(..., alias="optimizationRules")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerOptimizationRuleV2(BaseModel):
    pass


class OptimizationRulesAPISwaggerSingleOptimizationRuleResponseV2(BaseModel):
    """Response object for operations involving a single optimization rule."""
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the error, if unsuccessful.")
    optimization_rule: Optional["OptimizationRulesAPISwaggerOptimizationRuleV2"] = Field(None, alias="optimizationRule")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerOptimizationRulesResponseV2(BaseModel):
    """Response object for CreateOptimizationRules and UpdateOptimizationRules API."""
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    responses: Optional[list["OptimizationRulesAPISwaggerSingleOptimizationRuleResponseV2"]] = None

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerCreateOptimizationRulesResponseV2(BaseModel):
    """Response object for CreateOptimizationRules API."""
    pass


class OptimizationRulesAPISwaggerOptimizationRule(BaseModel):
    pass


class OptimizationRulesAPISwaggerOptimizationRuleFilter(BaseModel):
    """Filter on optimization rules."""
    optimization_rule_id: Optional["OptimizationRulesAPISwaggerEntityFieldFilter"] = Field(None, alias="optimizationRuleId")
    rule_category: Optional["OptimizationRulesAPISwaggerEntityFieldFilter"] = Field(None, alias="ruleCategory")
    rule_sub_category: Optional["OptimizationRulesAPISwaggerEntityFieldFilter"] = Field(None, alias="ruleSubCategory")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerOptimizationRuleFilterV2(BaseModel):
    """Filter on optimization rules."""
    optimization_rule_id: Optional["OptimizationRulesAPISwaggerEntityFieldFilter"] = Field(None, alias="optimizationRuleId")
    rule_category: Optional["OptimizationRulesAPISwaggerEntityFieldFilter"] = Field(None, alias="ruleCategory")
    rule_name: Optional["OptimizationRulesAPISwaggerEntityFieldFilter"] = Field(None, alias="ruleName")
    rule_status: Optional["OptimizationRulesAPISwaggerEntityFieldFilter"] = Field(None, alias="ruleStatus")
    rule_sub_category: Optional["OptimizationRulesAPISwaggerEntityFieldFilter"] = Field(None, alias="ruleSubCategory")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerOptimizationRulesError(BaseModel):
    """Error response object."""
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    message: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerSingleOptimizationRuleResponse(BaseModel):
    """Response object for operations involving a single optimization rule."""
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the error, if unsuccessful.")
    optimization_rule: Optional["OptimizationRulesAPISwaggerOptimizationRule"] = Field(None, alias="optimizationRule")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerOptimizationRulesResponse(BaseModel):
    """Response object for CreateOptimizationRules and UpdateOptimizationRules API."""
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    responses: Optional[list["OptimizationRulesAPISwaggerSingleOptimizationRuleResponse"]] = None

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerSearchOptimizationRulesRequest(BaseModel):
    """Request object for searching or getting optimization rules."""
    campaign_filter: Optional["OptimizationRulesAPISwaggerCampaignFilter"] = Field(None, alias="campaignFilter")
    next_token: Optional[str] = Field(None, alias="nextToken")
    optimization_rule_filter: Optional["OptimizationRulesAPISwaggerOptimizationRuleFilter"] = Field(None, alias="optimizationRuleFilter")
    page_size: Optional[float] = Field(None, alias="pageSize")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerSortableField(StrEnum):
    NAME = "NAME"


class OptimizationRulesAPISwaggerSearchOptimizationRulesRequestV2(BaseModel):
    """Request object for searching or getting optimization rules."""
    campaign_filter: Optional["OptimizationRulesAPISwaggerCampaignFilter"] = Field(None, alias="campaignFilter")
    max_results: Optional[float] = Field(None, alias="maxResults", description="The maximum number of optimization rules to fetch.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="To retrieve the next page of results, call the same operation and specify this token in the request. If the field is emp")
    optimization_rule_filter: Optional["OptimizationRulesAPISwaggerOptimizationRuleFilterV2"] = Field(None, alias="optimizationRuleFilter")
    sort_by: Optional[list["OptimizationRulesAPISwaggerSortableField"]] = Field(None, alias="sortBy", description="Sort conditions applied to the response.")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerSearchOptimizationRulesResponse(BaseModel):
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    next_token: Optional[str] = Field(None, alias="nextToken")
    optimization_rules: Optional[list["OptimizationRulesAPISwaggerOptimizationRule"]] = Field(None, alias="optimizationRules")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerSearchOptimizationRulesResponseV2(BaseModel):
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    next_token: Optional[str] = Field(None, alias="nextToken")
    optimization_rules: Optional[list["OptimizationRulesAPISwaggerOptimizationRuleV2"]] = Field(None, alias="optimizationRules")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerUpdateOptimizationRulesRequest(BaseModel):
    """Request object for updating one or multiple optimization rules."""
    optimization_rules: list["OptimizationRulesAPISwaggerOptimizationRule"] = Field(..., alias="optimizationRules")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerUpdateOptimizationRulesRequestV2(BaseModel):
    """Request object for updating one or multiple optimization rules. Budget rules are not supported for this operation."""
    optimization_rules: list["OptimizationRulesAPISwaggerOptimizationRuleV2"] = Field(..., alias="optimizationRules")

    model_config = {'populate_by_name': True}


class OptimizationRulesAPISwaggerUpdateOptimizationRulesResponseV2(BaseModel):
    """Response object for UpdateOptimizationRules API."""
    pass


class ProductDetailsList(BaseModel):
    """The list of products in the request."""
    pass


class ProductRecommendation(BaseModel):
    """Recommended asin and related information."""
    recommended_asin: Optional[str] = Field(None, alias="recommendedAsin", description="Recommended ASIN")
    themes: Optional[list[str]] = Field(None, description="List of themes associated with this recommended ASIN.")

    model_config = {'populate_by_name': True}


class ProductRecommendationsByASIN(BaseModel):
    """Product recommendations supplemented with relevant information."""
    next_cursor: Optional[str] = Field(None, alias="nextCursor", description="An identifier to fetch next set of `ProductRecommendation` records in the result set if available. This will be null whe")
    previous_cursor: Optional[str] = Field(None, alias="previousCursor", description="Optional parameter that links to the previous result set served. This parameter will be null on the first request.")
    recommendations: Optional[list["ProductRecommendation"]] = Field(None, description="An array of `ProductRecommendation` objects.")

    model_config = {'populate_by_name': True}


class ThemeRecommendation(BaseModel):
    """Recommended asins grouped by theme attribute."""
    description: Optional[str] = Field(None, description="A theme name representing the context around the recommended list of ASINs.")
    recommended_asins: Optional[list[str]] = Field(None, alias="recommendedAsins", description="List of recommended ASINs under current theme.")
    theme: Optional[str] = Field(None, description="A theme name representing the context around the recommended list of ASINs.")

    model_config = {'populate_by_name': True}


class ProductRecommendationsByTheme(BaseModel):
    """Product recommendations grouped by theme attribute."""
    next_cursor: Optional[str] = Field(None, alias="nextCursor", description="An identifier to fetch next set of `ThemeRecommendation` records in the result set if available. This will be null when ")
    previous_cursor: Optional[str] = Field(None, alias="previousCursor", description="Optional parameter that links to the previous result set served to the requester.")
    recommendations: Optional[list["ThemeRecommendation"]] = Field(None, description="An array of `ThemeRecommendation` objects")

    model_config = {'populate_by_name': True}


class RankedKeywordTargetsForAdGroupRequestRecommendationtype(StrEnum):
    KEYWORDS_FOR_ADGROUP = "KEYWORDS_FOR_ADGROUP"


class RankedKeywordTargetsForAdGroupRequest(BaseModel):
    """This request type is used to retrieve recommended keyword targets for an existing ad group. Set the recommendationType to KEYWORDS_FOR_ADGROUP to use this request type."""
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the ad group")
    bids_enabled: Optional[bool] = Field(None, alias="bidsEnabled", description="Set this parameter to false if you do not want to retrieve bid suggestions for your keyword targets. Defaults to true.")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign")
    recommendation_type: RankedKeywordTargetsForAdGroupRequestRecommendationtype = Field(..., alias="recommendationType", description="The recommendationType to retrieve recommended keyword targets for an existing ad group.")

    model_config = {'populate_by_name': True}


class RankedKeywordTargetsForAsinsRequestBiddingstrategy(StrEnum):
    AUTO_FOR_SALES = "AUTO_FOR_SALES"
    LEGACY_FOR_SALES = "LEGACY_FOR_SALES"
    MANUAL = "MANUAL"
    RULE_BASED = "RULE_BASED"


class RankedKeywordTargetsForAsinsRequestRecommendationtype(StrEnum):
    KEYWORDS_FOR_ASINS = "KEYWORDS_FOR_ASINS"


class RankedKeywordTargetsForAsinsRequest(BaseModel):
    """This request type is used to retrieve recommended keyword targets for ASINs. Set the recommendationType to KEYWORDS_FOR_ASINS to use this request type."""
    asins: list[str] = Field(..., description="An array list of Asins")
    bidding_strategy: Optional[RankedKeywordTargetsForAsinsRequestBiddingstrategy] = Field(None, alias="biddingStrategy", description="The bid recommendations returned will depend on the bidding strategy. <br> LEGACY_FOR_SALES - Dynamic Bids (Down only) <")
    bids_enabled: Optional[bool] = Field(None, alias="bidsEnabled", description="Set this parameter to false if you do not want to retrieve bid suggestions for your keyword targets. Defaults to true.")
    product_details_list: Optional["ProductDetailsList"] = Field(None, alias="productDetailsList")
    recommendation_type: RankedKeywordTargetsForAsinsRequestRecommendationtype = Field(..., alias="recommendationType", description="The recommendationType to retrieve recommended keyword targets for a list of ASINs.")

    model_config = {'populate_by_name': True}


class RecKeywordTarget(BaseModel):
    bid_info: Optional[list["KeywordBidInfo"]] = Field(None, alias="bidInfo", description="A list of keyword bid info")
    keyword: Optional[str] = Field(None, description="The keyword value")
    rec_id: Optional[str] = Field(None, alias="recId", description="The recommended keyword target id")
    search_term_impression_rank: Optional[float] = Field(None, alias="searchTermImpressionRank", description="The account-level ad-attributed impression rank for the search-term/keyword. Provides [1:N] place the advertiser ranks a")
    search_term_impression_share: Optional[float] = Field(None, alias="searchTermImpressionShare", description="The account-level ad-attributed impression share for the search-term/keyword. Provides percentage share of all ad impres")
    translation: Optional[str] = Field(None, description="The translation of keyword if a locale is passed in")
    user_selected_keyword: Optional[bool] = Field(None, alias="userSelectedKeyword", description="Flag that tells if keyword was selected by the user or was recommended by KRS")

    model_config = {'populate_by_name': True}


class RankedTargetResponse(BaseModel):
    keyword_target_list: Optional[list["RecKeywordTarget"]] = Field(None, alias="keywordTargetList", description="A list of ranked keyword targets")

    model_config = {'populate_by_name': True}


class Refinements(BaseModel):
    """Response object for the GetRefinementsForCategory API, containing information on Brand Nodes, Age Range Nodes, and Genre Nodes."""
    age_ranges: Optional["AgeRanges"] = Field(None, alias="ageRanges")
    brands: Optional["Brands"] = None
    genres: Optional["Genres"] = None

    model_config = {'populate_by_name': True}


class RefinementsLoP(BaseModel):
    """Response object for the POST /sp/targets/category/{categoryId}/refinements endpoint, containing information on Brand Nodes, Age Range Nodes, and Genre Nodes."""
    age_ranges: Optional["AgeRangesLoP"] = Field(None, alias="ageRanges")
    brands: Optional["BrandsLoP"] = None
    genres: Optional["GenresLoP"] = None

    model_config = {'populate_by_name': True}


class RuleState(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class RuleNotification(BaseModel):
    campaign_id: Optional["RuleCampaignId"] = Field(None, alias="campaignId")
    campaign_optimization_id: Optional["campaignOptimizationId"] = Field(None, alias="campaignOptimizationId")
    notification_string: Optional[str] = Field(None, alias="notificationString", description="Explains why the rule state is disabled")
    rule_state: Optional["RuleState"] = Field(None, alias="ruleState")

    model_config = {'populate_by_name': True}


class RuleNotificationError(BaseModel):
    error: Optional["CampaignOptimizationRuleError"] = Field(None, alias="Error")
    campaign_id: Optional["RuleCampaignId"] = Field(None, alias="campaignId")

    model_config = {'populate_by_name': True}


class RuleRecommendationMetrics(BaseModel):
    """Performance Metrics supported by the rule recommendation"""
    roas: Optional[float] = Field(None, description="return on ad spend value")

    model_config = {'populate_by_name': True}


class RuleRecommendation(BaseModel):
    campaign_id: Optional["RuleCampaignId"] = Field(None, alias="campaignId")
    performance_metrics: Optional["RuleRecommendationMetrics"] = Field(None, alias="performanceMetrics")
    performance_metrics_exists: Optional[bool] = Field(None, alias="performanceMetricsExists", description="If true, performance metrics for the campaign are available in performanceMetrics response field.")

    model_config = {'populate_by_name': True}


class RuleRecommendationError(BaseModel):
    error: Optional["CampaignOptimizationRuleError"] = Field(None, alias="Error")
    campaign_id: Optional["RuleCampaignId"] = Field(None, alias="campaignId")

    model_config = {'populate_by_name': True}


class SPBudgetRulesRecommendationError(BaseModel):
    """The Error Response Object."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SPBudgetRulesRecommendationEvent(BaseModel):
    end_date: Optional[str] = Field(None, alias="endDate", description="The end date in YYYYMMDD format.")
    event_id: Optional[str] = Field(None, alias="eventId", description="The event identifier.")
    event_name: Optional[str] = Field(None, alias="eventName", description="The event name.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The start date in YYYYMMDD format.")
    suggested_budget_increase_percent: Optional[float] = Field(None, alias="suggestedBudgetIncreasePercent", description="The suggested budget increase expressed as a percent.")

    model_config = {'populate_by_name': True}


class SPBudgetRulesRecommendationEventRequest(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="The campaign identifier.")

    model_config = {'populate_by_name': True}


class SPBudgetRulesRecommendationEventResponse(BaseModel):
    """Special events with date range and suggested budget increase."""
    recommended_budget_rule_events: Optional[list["SPBudgetRulesRecommendationEvent"]] = Field(None, alias="recommendedBudgetRuleEvents", description="A list of recommended special events with date range and suggested budget increase.")

    model_config = {'populate_by_name': True}


class SPCampaignBudgetRule(BaseModel):
    created_date: Optional[float] = Field(None, alias="createdDate", description="Epoch time of budget rule creation. Read-only.")
    last_updated_date: Optional[float] = Field(None, alias="lastUpdatedDate", description="Epoch time of budget rule update. Read-only.")
    rule_details: Optional["SPBudgetRuleDetails"] = Field(None, alias="ruleDetails")
    rule_id: str = Field(..., alias="ruleId", description="The budget rule identifier.")
    rule_state: Optional["state"] = Field(None, alias="ruleState")
    rule_status: Optional[str] = Field(None, alias="ruleStatus", description="The budget rule evaluation status. Read-only.")

    model_config = {'populate_by_name': True}


class SPCampaignOptimizationNotificationAPIRequest(BaseModel):
    campaign_ids: list["RuleCampaignId"] = Field(..., alias="campaignIds", description="A list of campaign ids")

    model_config = {'populate_by_name': True}


class SPCampaignOptimizationNotificationAPIResponse(BaseModel):
    campaign_optimization_notifications: Optional[list["RuleNotification"]] = Field(None, alias="CampaignOptimizationNotifications", description="List of successful campaign optimization notifications for campaigns.")
    campaign_optimization_recommendations_error: Optional[list["RuleNotificationError"]] = Field(None, alias="CampaignOptimizationRecommendationsError", description="List of errors that occured when generating campaign optimization notifications.")

    model_config = {'populate_by_name': True}


class SPCampaignOptimizationRecommendationAPIResponse(BaseModel):
    campaign_optimization_recommendations: Optional[list["RuleRecommendation"]] = Field(None, alias="CampaignOptimizationRecommendations", description="List of campaigns eligible for optimization rule.")
    campaign_optimization_recommendations_error: Optional[list["RuleRecommendationError"]] = Field(None, alias="CampaignOptimizationRecommendationsError", description="List of campaigns not eligible for optimization rule.")

    model_config = {'populate_by_name': True}


class SPCampaignOptimizationRecommendationsAPIRequest(BaseModel):
    campaign_ids: list["RuleCampaignId"] = Field(..., alias="campaignIds", description="A list of campaign ids")
    require_performance_metrics: Optional[bool] = Field(None, alias="requirePerformanceMetrics", description="If set to false, eligible campaigns without a recommendation for performanceMetrics are also provided in response.Check ")

    model_config = {'populate_by_name': True}


class SPGetAllRuleEventRequest(BaseModel):
    pass


class SPIndividualEvent(BaseModel):
    end_date: Optional[str] = Field(None, alias="endDate", description="The end date in ISO-8601 format.")
    event_id: Optional[str] = Field(None, alias="eventId", description="The event identifier.")
    event_name: Optional[str] = Field(None, alias="eventName", description="The event name.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The start date in ISO-8601 format.")

    model_config = {'populate_by_name': True}


class SPGroupedEvent(BaseModel):
    end_date: Optional[str] = Field(None, alias="endDate", description="The end date in ISO-8601 format.")
    grouped_event_id: Optional[str] = Field(None, alias="groupedEventId", description="The grouped event identifier.")
    grouped_event_name: Optional[str] = Field(None, alias="groupedEventName", description="The grouped event name.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The start date in ISO-8601 format.")

    model_config = {'populate_by_name': True}


class SPGetAllRuleEventResponse(BaseModel):
    """All Special individual and grouped events with date range."""
    events: Optional[list["SPIndividualEvent"]] = Field(None, description="A list of individual events with date range.")
    grouped_events: Optional[list["SPGroupedEvent"]] = Field(None, alias="groupedEvents", description="A list of grouped events with date range.")

    model_config = {'populate_by_name': True}


class SPGetAssociatedCampaignsResponse(BaseModel):
    associated_campaigns: Optional[list["AssociatedCampaign"]] = Field(None, alias="associatedCampaigns", description="A list of campaigns that are associated to this budget rule.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` ")

    model_config = {'populate_by_name': True}


class SPGetRuleEventError(BaseModel):
    """The Error Response Object."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SPKeywordGroupsExceptionErrorsErrorcode(StrEnum):
    DEPENDENCY_FAILURE = "DEPENDENCY_FAILURE"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    INVALID_REQUEST = "INVALID_REQUEST"
    NOT_FOUND = "NOT_FOUND"
    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
    RATE_EXCEEDED = "RATE_EXCEEDED"
    TIMEOUT = "TIMEOUT"
    UNAUTHENTICATED = "UNAUTHENTICATED"
    UNAUTHORIZED = "UNAUTHORIZED"
    UNAVAILABLE = "UNAVAILABLE"
    UNSUPPORTED_MEDIA = "UNSUPPORTED_MEDIA"


class SPKeywordGroupsExceptionErrors(BaseModel):
    error_code: Optional[SPKeywordGroupsExceptionErrorsErrorcode] = Field(None, alias="errorCode", description="Error Code. For informational purpose only.")
    error_id: Optional[int] = Field(None, alias="errorId", description="ID to indicate the granular error. Rely only on this to programmatically handle errors.")
    error_message: Optional[str] = Field(None, alias="errorMessage", description="human readable error message for each error.")

    model_config = {'populate_by_name': True}


class SPKeywordGroupsException(BaseModel):
    """Custom Exception message."""
    details: Optional[str] = Field(None, description="Human Readable message.")
    errors: Optional[list["SPKeywordGroupsExceptionErrors"]] = None
    http_status_code: Optional[str] = Field(None, alias="httpStatusCode", description="http status code.")
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class SPListAssociatedBudgetRulesResponse(BaseModel):
    associated_rules: Optional[list["SPCampaignBudgetRule"]] = Field(None, alias="associatedRules", description="A list of associated budget rules.")

    model_config = {'populate_by_name': True}


class SPTargetingCountryErrors(BaseModel):
    """The Error Response Object."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    country_codes: Optional[list[str]] = Field(None, alias="countryCodes", description="List of country codes this error returned for.")
    message: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SPTargetingError(BaseModel):
    """The Error Response Object."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SearchBrandsRequest(BaseModel):
    """Request object for SearchBrands API."""
    keyword: str

    model_config = {'populate_by_name': True}


class SponsoredProductsAccessDeniedErrorCode(StrEnum):
    ACCESS_DENIED = "ACCESS_DENIED"


class SponsoredProductsAccessDeniedExceptionCode(StrEnum):
    ACCESS_DENIED = "ACCESS_DENIED"


class SponsoredProductsAccessDeniedExceptionResponseContent(BaseModel):
    code: "SponsoredProductsAccessDeniedErrorCode"
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsErrorCause(BaseModel):
    """Structure describing error cause - location in the payload and data causing error"""
    location: str = Field(..., description="Error location, JSON Path expression specifying element of API payload causing error")
    trigger: Optional[str] = Field(None, description="optional value causing error")

    model_config = {'populate_by_name': True}


class SponsoredProductsMarketplace(StrEnum):
    AE = "AE"
    AU = "AU"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
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


class SponsoredProductsAdEligibilityErrorReason(StrEnum):
    AD_INELIGIBLE = "AD_INELIGIBLE"


class SponsoredProductsAdEligibilityError(BaseModel):
    """Errors related to ad eligibility"""
    cause: Optional["SponsoredProductsErrorCause"] = None
    marketplace: Optional["SponsoredProductsMarketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsAdEligibilityErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsAdGroupServingStatusReason(StrEnum):
    ADVERTISER_ARCHIVED_DETAIL = "ADVERTISER_ARCHIVED_DETAIL"
    ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL = "ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL"
    ADVERTISER_OUT_OF_BUDGET_DETAIL = "ADVERTISER_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_PAUSED_DETAIL = "ADVERTISER_PAUSED_DETAIL"
    ADVERTISER_PAYMENT_FAILURE_DETAIL = "ADVERTISER_PAYMENT_FAILURE_DETAIL"
    ADVERTISER_POLICING_PENDING_REVIEW_DETAIL = "ADVERTISER_POLICING_PENDING_REVIEW_DETAIL"
    ADVERTISER_POLICING_SUSPENDED_DETAIL = "ADVERTISER_POLICING_SUSPENDED_DETAIL"
    AD_GROUP_ARCHIVED_DETAIL = "AD_GROUP_ARCHIVED_DETAIL"
    AD_GROUP_INCOMPLETE_DETAIL = "AD_GROUP_INCOMPLETE_DETAIL"
    AD_GROUP_LOW_BID_DETAIL = "AD_GROUP_LOW_BID_DETAIL"
    AD_GROUP_PAUSED_DETAIL = "AD_GROUP_PAUSED_DETAIL"
    AD_GROUP_POLICING_CREATIVE_REJECTED_DETAIL = "AD_GROUP_POLICING_CREATIVE_REJECTED_DETAIL"
    AD_GROUP_POLICING_PENDING_REVIEW_DETAIL = "AD_GROUP_POLICING_PENDING_REVIEW_DETAIL"
    AD_GROUP_STATUS_ENABLED_DETAIL = "AD_GROUP_STATUS_ENABLED_DETAIL"
    CAMPAIGN_ARCHIVED_DETAIL = "CAMPAIGN_ARCHIVED_DETAIL"
    CAMPAIGN_INCOMPLETE_DETAIL = "CAMPAIGN_INCOMPLETE_DETAIL"
    CAMPAIGN_OUT_OF_BUDGET_DETAIL = "CAMPAIGN_OUT_OF_BUDGET_DETAIL"
    CAMPAIGN_PAUSED_DETAIL = "CAMPAIGN_PAUSED_DETAIL"
    CAMPAIGN_STATUS_ENABLED_DETAIL = "CAMPAIGN_STATUS_ENABLED_DETAIL"
    ENDED_DETAIL = "ENDED_DETAIL"
    OTHER = "OTHER"
    PENDING_REVIEW_DETAIL = "PENDING_REVIEW_DETAIL"
    PENDING_START_DATE_DETAIL = "PENDING_START_DATE_DETAIL"
    PORTFOLIO_ARCHIVED_DETAIL = "PORTFOLIO_ARCHIVED_DETAIL"
    PORTFOLIO_ENDED_DETAIL = "PORTFOLIO_ENDED_DETAIL"
    PORTFOLIO_OUT_OF_BUDGET_DETAIL = "PORTFOLIO_OUT_OF_BUDGET_DETAIL"
    PORTFOLIO_PAUSED_DETAIL = "PORTFOLIO_PAUSED_DETAIL"
    PORTFOLIO_PENDING_START_DATE_DETAIL = "PORTFOLIO_PENDING_START_DATE_DETAIL"
    PORTFOLIO_STATUS_ENABLED_DETAIL = "PORTFOLIO_STATUS_ENABLED_DETAIL"
    REJECTED_DETAIL = "REJECTED_DETAIL"


class SponsoredProductsAdGroupServingStatusDetail(BaseModel):
    help_url: Optional[str] = Field(None, alias="helpUrl", description="A URL with additional information about the status identifier.")
    message: Optional[str] = Field(None, description="A human-readable description of the status identifier specified in the name field.")
    name: Optional["SponsoredProductsAdGroupServingStatusReason"] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsAdGroupServingStatus(StrEnum):
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_POLICING_CREATIVE_REJECTED = "AD_GROUP_POLICING_CREATIVE_REJECTED"
    AD_GROUP_POLICING_PENDING_REVIEW = "AD_GROUP_POLICING_PENDING_REVIEW"
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_STATUS_ENABLED = "CAMPAIGN_STATUS_ENABLED"
    ENDED = "ENDED"
    OTHER = "OTHER"
    PENDING_REVIEW = "PENDING_REVIEW"
    PENDING_START_DATE = "PENDING_START_DATE"
    PORTFOLIO_ARCHIVED = "PORTFOLIO_ARCHIVED"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    PORTFOLIO_PAUSED = "PORTFOLIO_PAUSED"
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"
    PORTFOLIO_STATUS_ENABLED = "PORTFOLIO_STATUS_ENABLED"
    REJECTED = "REJECTED"


class SponsoredProductsAdGroupExtendedData(BaseModel):
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="Creation date in ISO 8601.")
    last_update_date_time: Optional[str] = Field(None, alias="lastUpdateDateTime", description="Last updated date in ISO 8601.")
    serving_status: Optional["SponsoredProductsAdGroupServingStatus"] = Field(None, alias="servingStatus")
    serving_status_details: Optional[list["SponsoredProductsAdGroupServingStatusDetail"]] = Field(None, alias="servingStatusDetails", description="The serving status reasons of the AdGroup")

    model_config = {'populate_by_name': True}


class SponsoredProductsEntityState(StrEnum):
    ARCHIVED = "ARCHIVED"
    ENABLED = "ENABLED"
    ENABLING = "ENABLING"
    OTHER = "OTHER"
    PAUSED = "PAUSED"
    PROPOSED = "PROPOSED"
    USER_DELETED = "USER_DELETED"


class SponsoredProductsAdGroup(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the keyword.")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign to which the keyword is associated.")
    default_bid: float = Field(..., alias="defaultBid", description="A bid value for use when no bid is specified for keywords in the ad group. For more information about bid constraints by")
    extended_data: Optional["SponsoredProductsAdGroupExtendedData"] = Field(None, alias="extendedData")
    global_ad_group_id: Optional[str] = Field(None, alias="globalAdGroupId", description="The global adGroup identifier that manages this marketplace adGroup.")
    name: str = Field(..., description="The name of the ad group.")
    state: "SponsoredProductsEntityState"

    model_config = {'populate_by_name': True}


class SponsoredProductsMissingValueErrorReason(StrEnum):
    MISSING_VALUE = "MISSING_VALUE"


class SponsoredProductsMissingValueError(BaseModel):
    """Error describing missing values in API payloads"""
    cause: Optional["SponsoredProductsErrorCause"] = None
    marketplace: Optional["SponsoredProductsMarketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsMissingValueErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsValueLimitErrorReason(StrEnum):
    INVALID_ENUM_VALUE = "INVALID_ENUM_VALUE"
    NOT_IN_LIST = "NOT_IN_LIST"
    TOO_HIGH = "TOO_HIGH"
    TOO_LOW = "TOO_LOW"


class SponsoredProductsRangeError(BaseModel):
    """Errors related to range constraints violations"""
    allowed: Optional[list[str]] = Field(None, description="allowed values")
    cause: Optional["SponsoredProductsErrorCause"] = None
    lower_limit: Optional[str] = Field(None, alias="lowerLimit", description="optional lower limit")
    marketplace: Optional["SponsoredProductsMarketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsValueLimitErrorReason"
    upper_limit: Optional[str] = Field(None, alias="upperLimit", description="optional upper limit")

    model_config = {'populate_by_name': True}


class SponsoredProductsInternalServerErrorReason(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class SponsoredProductsInternalServerError(BaseModel):
    """Error that represents non-retryable API service error. Sending the same request will result in another error."""
    cause: Optional["SponsoredProductsErrorCause"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsInternalServerErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsOtherErrorReason(StrEnum):
    OTHER_ERROR = "OTHER_ERROR"


class SponsoredProductsOtherError(BaseModel):
    """Errors not related to any of the other error types"""
    cause: Optional["SponsoredProductsErrorCause"] = None
    marketplace: Optional["SponsoredProductsMarketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsOtherErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsThrottledErrorReason(StrEnum):
    THROTTLED = "THROTTLED"


class SponsoredProductsThrottledError(BaseModel):
    """Error that represents failure due to API caller exceeding allowed service limits."""
    cause: Optional["SponsoredProductsErrorCause"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsThrottledErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsMalformedValueErrorReason(StrEnum):
    BLANK = "BLANK"
    FORBIDDEN_CHARS = "FORBIDDEN_CHARS"
    LEADING_OR_TRAILING_WHITESPACE = "LEADING_OR_TRAILING_WHITESPACE"
    PATTERN_NOT_MATCHED = "PATTERN_NOT_MATCHED"
    TOO_LONG = "TOO_LONG"
    TOO_SHORT = "TOO_SHORT"


class SponsoredProductsMalformedValueError(BaseModel):
    """Errors being used to represent malformed values e.g. containing not allowed characters, not following patters etc"""
    cause: Optional["SponsoredProductsErrorCause"] = None
    fragment: Optional[str] = Field(None, description="fragment of the value which is wrong")
    marketplace: Optional["SponsoredProductsMarketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsMalformedValueErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsInvalidInputErrorReason(StrEnum):
    INVALID_TOKEN = "INVALID_TOKEN"


class SponsoredProductsInvalidInputError(BaseModel):
    """Errors related to ad eligibility"""
    cause: Optional["SponsoredProductsErrorCause"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsInvalidInputErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsEntityNotFoundErrorReason(StrEnum):
    ENTITY_NOT_FOUND = "ENTITY_NOT_FOUND"


class SponsoredProductsEntityType(StrEnum):
    AD_GROUP = "AD_GROUP"
    CAMPAIGN = "CAMPAIGN"
    CAMPAIGN_NEGATIVE_KEYWORD = "CAMPAIGN_NEGATIVE_KEYWORD"
    CAMPAIGN_NEGATIVE_TARGETING_CLAUSE = "CAMPAIGN_NEGATIVE_TARGETING_CLAUSE"
    KEYWORD = "KEYWORD"
    NEGATIVE_KEYWORD = "NEGATIVE_KEYWORD"
    NEGATIVE_TARGETING_CLAUSE = "NEGATIVE_TARGETING_CLAUSE"
    PRODUCT_AD = "PRODUCT_AD"
    TARGETING_CLAUSE = "TARGETING_CLAUSE"


class SponsoredProductsEntityNotFoundError(BaseModel):
    cause: Optional["SponsoredProductsErrorCause"] = None
    entity_id: str = Field(..., alias="entityId", description="The entity id in the request")
    entity_type: "SponsoredProductsEntityType" = Field(..., alias="entityType")
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsEntityNotFoundErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsAdGroupAccessErrorSelector(BaseModel):
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    invalid_input_error: Optional["SponsoredProductsInvalidInputError"] = Field(None, alias="invalidInputError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class SponsoredProductsAdGroupAccessError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsAdGroupAccessErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsInvalidArgumentErrorCode(StrEnum):
    INVALID_ARGUMENT = "INVALID_ARGUMENT"


class SponsoredProductsAdGroupAccessExceptionResponseContent(BaseModel):
    """Exception resulting in accessing campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsAdGroupAccessError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsApplicableMarketplacesErrorReason(StrEnum):
    APPLICABLE_MARKETPLACES_MISMATCH_ERROR = "APPLICABLE_MARKETPLACES_MISMATCH_ERROR"


class SponsoredProductsApplicableMarketplacesError(BaseModel):
    """Errors related to ad eligibility"""
    cause: Optional["SponsoredProductsErrorCause"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsApplicableMarketplacesErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsBiddingErrorReason(StrEnum):
    BID_AUDIENCES_MORE_THAN_ALLOWED = "BID_AUDIENCES_MORE_THAN_ALLOWED"
    BID_GT_BUDGET = "BID_GT_BUDGET"
    BID_INVALID_AUDIENCE_ID = "BID_INVALID_AUDIENCE_ID"
    BID_INVALID_AUDIENCE_SEGMENT_TYPE = "BID_INVALID_AUDIENCE_SEGMENT_TYPE"
    BID_INVALID_PLACEMENT = "BID_INVALID_PLACEMENT"
    BID_INVALID_SHOPPER_COHORT_TYPE = "BID_INVALID_SHOPPER_COHORT_TYPE"
    BID_MISSING_AUDIENCES = "BID_MISSING_AUDIENCES"
    BID_OUT_OF_MARKET_PLACE_RANGE = "BID_OUT_OF_MARKET_PLACE_RANGE"
    BID_SHOPPER_COHORTS_MORE_THAN_ALLOWED = "BID_SHOPPER_COHORTS_MORE_THAN_ALLOWED"


class SponsoredProductsBiddingError(BaseModel):
    """Errors related to bids"""
    cause: Optional["SponsoredProductsErrorCause"] = None
    lower_limit: Optional[str] = Field(None, alias="lowerLimit")
    marketplace: Optional["SponsoredProductsMarketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsBiddingErrorReason"
    upper_limit: Optional[str] = Field(None, alias="upperLimit")

    model_config = {'populate_by_name': True}


class SponsoredProductsDuplicateValueErrorReason(StrEnum):
    DUPLICATE_VALUE = "DUPLICATE_VALUE"
    MARKETPLACE_ATTRIBUTES_REPEATED = "MARKETPLACE_ATTRIBUTES_REPEATED"
    NAME_NOT_UNIQUE = "NAME_NOT_UNIQUE"


class SponsoredProductsDuplicateValueError(BaseModel):
    cause: Optional["SponsoredProductsErrorCause"] = None
    marketplace: Optional["SponsoredProductsMarketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsDuplicateValueErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsQuotaScope(StrEnum):
    ACCOUNT = "ACCOUNT"
    PARENT_ENTITY = "PARENT_ENTITY"


class SponsoredProductsQuotaErrorReason(StrEnum):
    NON_ARCHIVED_QUOTA_EXCEEDED = "NON_ARCHIVED_QUOTA_EXCEEDED"
    QUOTA_EXCEEDED = "QUOTA_EXCEEDED"


class SponsoredProductsEntityQuotaError(BaseModel):
    """Errors related to exceeding quota in campaign management service"""
    cause: Optional["SponsoredProductsErrorCause"] = None
    entity_type: "SponsoredProductsEntityType" = Field(..., alias="entityType")
    message: str = Field(..., description="Human readable error message")
    quota: Optional[str] = Field(None, description="optional current quota")
    quota_scope: Optional["SponsoredProductsQuotaScope"] = Field(None, alias="quotaScope")
    reason: "SponsoredProductsQuotaErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsEntityStateErrorReason(StrEnum):
    ARCHIVED_ENTITY_CANNOT_BE_MODIFIED = "ARCHIVED_ENTITY_CANNOT_BE_MODIFIED"
    AUTO_TARGETING_CLAUSE_CANNOT_BE_ARCHIVED_MANUALLY = "AUTO_TARGETING_CLAUSE_CANNOT_BE_ARCHIVED_MANUALLY"
    INVALID_STATE_TRANSITION = "INVALID_STATE_TRANSITION"
    INVALID_TARGET_STATE = "INVALID_TARGET_STATE"
    MARKETPLACE_STATE_CANNOT_BE_ARCHIVED = "MARKETPLACE_STATE_CANNOT_BE_ARCHIVED"
    PARENT_ARCHIVED_FORBIDS_UPDATES = "PARENT_ARCHIVED_FORBIDS_UPDATES"
    PARENT_ENTITY_FORBIDS_CREATION = "PARENT_ENTITY_FORBIDS_CREATION"
    PARENT_STATUS_FORBIDS_UPDATES_AND_CREATES = "PARENT_STATUS_FORBIDS_UPDATES_AND_CREATES"


class SponsoredProductsEntityStateError(BaseModel):
    """entity state update errors"""
    cause: Optional["SponsoredProductsErrorCause"] = None
    entity_type: "SponsoredProductsEntityType" = Field(..., alias="entityType")
    marketplace: Optional["SponsoredProductsMarketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsEntityStateErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsParentEntityErrorReason(StrEnum):
    PARENT_ENTITY_ARCHIVED = "PARENT_ENTITY_ARCHIVED"
    PARENT_ENTITY_DOES_NOT_TARGET_THESE_MARKETPLACES = "PARENT_ENTITY_DOES_NOT_TARGET_THESE_MARKETPLACES"
    PARENT_ENTITY_NOT_FOUND = "PARENT_ENTITY_NOT_FOUND"


class SponsoredProductsParentEntityError(BaseModel):
    """Errors related to parent entity"""
    cause: Optional["SponsoredProductsErrorCause"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsParentEntityErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsBillingErrorReason(StrEnum):
    ADVERTISER_BILLING_SETUP_INCOMPLETE = "ADVERTISER_BILLING_SETUP_INCOMPLETE"
    ADVERTISER_SUSPENDED = "ADVERTISER_SUSPENDED"
    BILLING_ACCOUNT_NOT_FOUND = "BILLING_ACCOUNT_NOT_FOUND"
    EXPIRED_PAYMENT_METHOD = "EXPIRED_PAYMENT_METHOD"
    PAYMENT_PROFILE_NOT_FOUND = "PAYMENT_PROFILE_NOT_FOUND"
    VETTING_FAILURE = "VETTING_FAILURE"


class SponsoredProductsBillingError(BaseModel):
    """Errors related to bids"""
    cause: Optional["SponsoredProductsErrorCause"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsBillingErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsAdGroupMutationErrorSelector(BaseModel):
    applicable_marketplaces_error: Optional["SponsoredProductsApplicableMarketplacesError"] = Field(None, alias="applicableMarketplacesError")
    bidding_error: Optional["SponsoredProductsBiddingError"] = Field(None, alias="biddingError")
    billing_error: Optional["SponsoredProductsBillingError"] = Field(None, alias="billingError")
    duplicate_value_error: Optional["SponsoredProductsDuplicateValueError"] = Field(None, alias="duplicateValueError")
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    entity_quota_error: Optional["SponsoredProductsEntityQuotaError"] = Field(None, alias="entityQuotaError")
    entity_state_error: Optional["SponsoredProductsEntityStateError"] = Field(None, alias="entityStateError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    parent_entity_error: Optional["SponsoredProductsParentEntityError"] = Field(None, alias="parentEntityError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class SponsoredProductsAdGroupMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsAdGroupMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsAdGroupFailureResponseItem(BaseModel):
    errors: Optional[list["SponsoredProductsAdGroupMutationError"]] = Field(None, description="A list of validation errors")
    index: int = Field(..., description="the index of the adGroup in the array from the request body")

    model_config = {'populate_by_name': True}


class SponsoredProductsAdGroupMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsAdGroupMutationError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsAdGroupSuccessResponseItem(BaseModel):
    ad_group: Optional["SponsoredProductsAdGroup"] = Field(None, alias="adGroup")
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="the adGroup ID")
    index: int = Field(..., description="the index of the adGroup in the array from the request body")

    model_config = {'populate_by_name': True}


class SponsoredProductsAdServingStatus(StrEnum):
    ACCOUNT_OUT_OF_BUDGET = "ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    AD_ARCHIVED = "AD_ARCHIVED"
    AD_CREATION_FAILED = "AD_CREATION_FAILED"
    AD_CREATION_OFFLINE_FAILED = "AD_CREATION_OFFLINE_FAILED"
    AD_CREATION_OFFLINE_IN_PROGRESS = "AD_CREATION_OFFLINE_IN_PROGRESS"
    AD_CREATION_OFFLINE_PENDING = "AD_CREATION_OFFLINE_PENDING"
    AD_ELIGIBLE = "AD_ELIGIBLE"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_POLICING_CREATIVE_REJECTED = "AD_GROUP_POLICING_CREATIVE_REJECTED"
    AD_GROUP_POLICING_PENDING_REVIEW = "AD_GROUP_POLICING_PENDING_REVIEW"
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    AD_INELIGIBLE = "AD_INELIGIBLE"
    AD_LANDING_PAGE_NOT_AVAILABLE = "AD_LANDING_PAGE_NOT_AVAILABLE"
    AD_MISSING_DECORATION = "AD_MISSING_DECORATION"
    AD_MISSING_IMAGE = "AD_MISSING_IMAGE"
    AD_NOT_BUYABLE = "AD_NOT_BUYABLE"
    AD_NOT_IN_BUYBOX = "AD_NOT_IN_BUYBOX"
    AD_NO_PURCHASABLE_OFFER = "AD_NO_PURCHASABLE_OFFER"
    AD_OUT_OF_STOCK = "AD_OUT_OF_STOCK"
    AD_PAUSED = "AD_PAUSED"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    AD_POLICING_SUSPENDED = "AD_POLICING_SUSPENDED"
    AD_STATUS_LIVE = "AD_STATUS_LIVE"
    CAMPAIGN_ADS_NOT_DELIVERING = "CAMPAIGN_ADS_NOT_DELIVERING"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_ENDED = "CAMPAIGN_ENDED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_PENDING_START_DATE = "CAMPAIGN_PENDING_START_DATE"
    CAMPAIGN_STATUS_ENABLED = "CAMPAIGN_STATUS_ENABLED"
    ELIGIBLE = "ELIGIBLE"
    ENDED = "ENDED"
    INELIGIBLE = "INELIGIBLE"
    LANDING_PAGE_NOT_AVAILABLE = "LANDING_PAGE_NOT_AVAILABLE"
    MISSING_DECORATION = "MISSING_DECORATION"
    MISSING_IMAGE = "MISSING_IMAGE"
    NOT_BUYABLE = "NOT_BUYABLE"
    NOT_IN_BUYBOX = "NOT_IN_BUYBOX"
    NO_INVENTORY = "NO_INVENTORY"
    NO_PURCHASABLE_OFFER = "NO_PURCHASABLE_OFFER"
    OTHER = "OTHER"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    PENDING_REVIEW = "PENDING_REVIEW"
    PENDING_START_DATE = "PENDING_START_DATE"
    PIR_RULE_EXCLUDED = "PIR_RULE_EXCLUDED"
    PORTFOLIO_ARCHIVED = "PORTFOLIO_ARCHIVED"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    PORTFOLIO_PAUSED = "PORTFOLIO_PAUSED"
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"
    PORTFOLIO_STATUS_ENABLED = "PORTFOLIO_STATUS_ENABLED"
    REJECTED = "REJECTED"
    SECURITY_SCAN_PENDING_REVIEW = "SECURITY_SCAN_PENDING_REVIEW"
    SECURITY_SCAN_REJECTED = "SECURITY_SCAN_REJECTED"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"
    TARGETING_CLAUSE_ARCHIVED = "TARGETING_CLAUSE_ARCHIVED"
    TARGETING_CLAUSE_BLOCKED = "TARGETING_CLAUSE_BLOCKED"
    TARGETING_CLAUSE_PAUSED = "TARGETING_CLAUSE_PAUSED"
    TARGETING_CLAUSE_POLICING_SUSPENDED = "TARGETING_CLAUSE_POLICING_SUSPENDED"
    TARGETING_CLAUSE_STATUS_LIVE = "TARGETING_CLAUSE_STATUS_LIVE"


class SponsoredProductsAdServingStatusReason(StrEnum):
    ACCOUNT_OUT_OF_BUDGET_DETAIL = "ACCOUNT_OUT_OF_BUDGET_DETAIL"
    ADULT_PRODUCT = "ADULT_PRODUCT"
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET_DETAIL = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_ARCHIVED_DETAIL = "ADVERTISER_ARCHIVED_DETAIL"
    ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL = "ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL"
    ADVERTISER_OUT_OF_BUDGET_DETAIL = "ADVERTISER_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_PAUSED_DETAIL = "ADVERTISER_PAUSED_DETAIL"
    ADVERTISER_PAYMENT_FAILURE_DETAIL = "ADVERTISER_PAYMENT_FAILURE_DETAIL"
    ADVERTISER_POLICING_PENDING_REVIEW_DETAIL = "ADVERTISER_POLICING_PENDING_REVIEW_DETAIL"
    ADVERTISER_POLICING_SUSPENDED_DETAIL = "ADVERTISER_POLICING_SUSPENDED_DETAIL"
    ADVERTISER_STATUS_ENABLED_DETAIL = "ADVERTISER_STATUS_ENABLED_DETAIL"
    AD_ARCHIVED_DETAIL = "AD_ARCHIVED_DETAIL"
    AD_CREATION_OFFLINE_FAILED = "AD_CREATION_OFFLINE_FAILED"
    AD_CREATION_OFFLINE_IN_PROGRESS = "AD_CREATION_OFFLINE_IN_PROGRESS"
    AD_CREATION_OFFLINE_PENDING = "AD_CREATION_OFFLINE_PENDING"
    AD_GROUP_ARCHIVED_DETAIL = "AD_GROUP_ARCHIVED_DETAIL"
    AD_GROUP_INCOMPLETE_DETAIL = "AD_GROUP_INCOMPLETE_DETAIL"
    AD_GROUP_LOW_BID_DETAIL = "AD_GROUP_LOW_BID_DETAIL"
    AD_GROUP_PAUSED_DETAIL = "AD_GROUP_PAUSED_DETAIL"
    AD_GROUP_POLICING_CREATIVE_REJECTED_DETAIL = "AD_GROUP_POLICING_CREATIVE_REJECTED_DETAIL"
    AD_GROUP_POLICING_PENDING_REVIEW_DETAIL = "AD_GROUP_POLICING_PENDING_REVIEW_DETAIL"
    AD_GROUP_STATUS_ENABLED_DETAIL = "AD_GROUP_STATUS_ENABLED_DETAIL"
    AD_PAUSED_DETAIL = "AD_PAUSED_DETAIL"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    AD_POLICING_PENDING_REVIEW_DETAIL = "AD_POLICING_PENDING_REVIEW_DETAIL"
    AD_POLICING_SUSPENDED_DETAIL = "AD_POLICING_SUSPENDED_DETAIL"
    AD_STATUS_LIVE_DETAIL = "AD_STATUS_LIVE_DETAIL"
    ASIN_QUARANTINED = "ASIN_QUARANTINED"
    BRAND_REMOVED = "BRAND_REMOVED"
    CAMPAIGN_ADS_NOT_DELIVERING_DETAIL = "CAMPAIGN_ADS_NOT_DELIVERING_DETAIL"
    CAMPAIGN_ARCHIVED_DETAIL = "CAMPAIGN_ARCHIVED_DETAIL"
    CAMPAIGN_INCOMPLETE_DETAIL = "CAMPAIGN_INCOMPLETE_DETAIL"
    CAMPAIGN_OUT_OF_BUDGET_DETAIL = "CAMPAIGN_OUT_OF_BUDGET_DETAIL"
    CAMPAIGN_PAUSED_DETAIL = "CAMPAIGN_PAUSED_DETAIL"
    CAMPAIGN_STATUS_ENABLED_DETAIL = "CAMPAIGN_STATUS_ENABLED_DETAIL"
    CBA_NOT_SUPPORTED = "CBA_NOT_SUPPORTED"
    CLOSED_GL = "CLOSED_GL"
    CP_INELIGIBLE = "CP_INELIGIBLE"
    CP_INELIGIBLE_ASIN = "CP_INELIGIBLE_ASIN"
    CP_INELIGIBLE_UNKNOWN = "CP_INELIGIBLE_UNKNOWN"
    CP_INELIGIBLE_VENDOR = "CP_INELIGIBLE_VENDOR"
    ELIGIBLE_DETAIL = "ELIGIBLE_DETAIL"
    ENDED_DETAIL = "ENDED_DETAIL"
    INELIGIBLE_CONDITION = "INELIGIBLE_CONDITION"
    INVENTORY_INCOMPLETE = "INVENTORY_INCOMPLETE"
    ITEM_MISSING = "ITEM_MISSING"
    LANDING_PAGE_INELIGIBLE = "LANDING_PAGE_INELIGIBLE"
    LANDING_PAGE_NOT_AVAILABLE_DETAIL = "LANDING_PAGE_NOT_AVAILABLE_DETAIL"
    MISSING_DECORATION_DETAIL = "MISSING_DECORATION_DETAIL"
    MISSING_IMAGE_DETAIL = "MISSING_IMAGE_DETAIL"
    MODERATION_ADULT_NOVELTY_PV_DETAIL = "MODERATION_ADULT_NOVELTY_PV_DETAIL"
    MODERATION_ADULT_PRODUCT_PV_DETAIL = "MODERATION_ADULT_PRODUCT_PV_DETAIL"
    MODERATION_ADULT_SOFTLINES_PV_DETAIL = "MODERATION_ADULT_SOFTLINES_PV_DETAIL"
    MODERATION_CLAIM_WEIGHTLOSS_PV_DETAIL = "MODERATION_CLAIM_WEIGHTLOSS_PV_DETAIL"
    MODERATION_CONTENT_NUDITY_PV_DETAIL = "MODERATION_CONTENT_NUDITY_PV_DETAIL"
    MODERATION_CONTENT_PROVOCATIVE_PV_DETAIL = "MODERATION_CONTENT_PROVOCATIVE_PV_DETAIL"
    MODERATION_CONTENT_SMOKING_PV_DETAIL = "MODERATION_CONTENT_SMOKING_PV_DETAIL"
    MODERATION_CRITICAL_EVENTS_PV_DETAIL = "MODERATION_CRITICAL_EVENTS_PV_DETAIL"
    MODERATION_ERROR_404_PV_DETAIL = "MODERATION_ERROR_404_PV_DETAIL"
    MODERATION_GRAPHICAL_SEXUAL_IMAGES_PV_DETAIL = "MODERATION_GRAPHICAL_SEXUAL_IMAGES_PV_DETAIL"
    MODERATION_HFSS_PRODUCT_PV_DETAIL = "MODERATION_HFSS_PRODUCT_PV_DETAIL"
    MODERATION_LANGUAGE_OFFENSIVE_PV_DETAIL = "MODERATION_LANGUAGE_OFFENSIVE_PV_DETAIL"
    MODERATION_NOT_COMPLIANT_TO_AD_POLICY_PV_DETAIL = "MODERATION_NOT_COMPLIANT_TO_AD_POLICY_PV_DETAIL"
    MODERATION_SMOKING_RELATED_PV_DETAIL = "MODERATION_SMOKING_RELATED_PV_DETAIL"
    NOT_BUYABLE_DETAIL = "NOT_BUYABLE_DETAIL"
    NOT_IN_BUYBOX_DETAIL = "NOT_IN_BUYBOX_DETAIL"
    NO_INVENTORY_DETAIL = "NO_INVENTORY_DETAIL"
    NO_PURCHASABLE_OFFER_DETAIL = "NO_PURCHASABLE_OFFER_DETAIL"
    OFFER_MISSING_DETAIL = "OFFER_MISSING_DETAIL"
    OTHER = "OTHER"
    OUT_OF_STOCK_DETAIL = "OUT_OF_STOCK_DETAIL"
    PENDING_REVIEW_DETAIL = "PENDING_REVIEW_DETAIL"
    PENDING_START_DATE_DETAIL = "PENDING_START_DATE_DETAIL"
    PIR_RULE_EXCLUDED = "PIR_RULE_EXCLUDED"
    PORTFOLIO_ARCHIVED_DETAIL = "PORTFOLIO_ARCHIVED_DETAIL"
    PORTFOLIO_ENDED_DETAIL = "PORTFOLIO_ENDED_DETAIL"
    PORTFOLIO_OUT_OF_BUDGET_DETAIL = "PORTFOLIO_OUT_OF_BUDGET_DETAIL"
    PORTFOLIO_PAUSED_DETAIL = "PORTFOLIO_PAUSED_DETAIL"
    PORTFOLIO_PENDING_START_DATE_DETAIL = "PORTFOLIO_PENDING_START_DATE_DETAIL"
    PORTFOLIO_STATUS_ENABLED_DETAIL = "PORTFOLIO_STATUS_ENABLED_DETAIL"
    REJECTED_DETAIL = "REJECTED_DETAIL"
    RESTRICTED_GL = "RESTRICTED_GL"
    SECURITY_SCAN_PENDING_REVIEW = "SECURITY_SCAN_PENDING_REVIEW"
    SECURITY_SCAN_REJECTED = "SECURITY_SCAN_REJECTED"
    SKU_DEFECTIVE = "SKU_DEFECTIVE"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"
    TARGETING_CLAUSE_ARCHIVED_DETAIL = "TARGETING_CLAUSE_ARCHIVED_DETAIL"
    TARGETING_CLAUSE_BLOCKED_DETAIL = "TARGETING_CLAUSE_BLOCKED_DETAIL"
    TARGETING_CLAUSE_PAUSED_DETAIL = "TARGETING_CLAUSE_PAUSED_DETAIL"
    TARGETING_CLAUSE_POLICING_SUSPENDED_DETAIL = "TARGETING_CLAUSE_POLICING_SUSPENDED_DETAIL"
    TARGETING_CLAUSE_STATUS_LIVE_DETAIL = "TARGETING_CLAUSE_STATUS_LIVE_DETAIL"
    VARIATION_PARENT = "VARIATION_PARENT"


class SponsoredProductsAdServingStatusDetail(BaseModel):
    help_url: Optional[str] = Field(None, alias="helpUrl", description="A URL with additional information about the status identifier.")
    message: Optional[str] = Field(None, description="A human-readable description of the status identifier specified in the name field.")
    name: Optional["SponsoredProductsAdServingStatusReason"] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsQueryTermMatchType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SponsoredProductsAsinFilter(BaseModel):
    include: Optional[list[str]] = None
    query_term_match_type: Optional["SponsoredProductsQueryTermMatchType"] = Field(None, alias="queryTermMatchType")

    model_config = {'populate_by_name': True}


class SponsoredProductsAsinOwnershipErrorReason(StrEnum):
    ASIN_NOT_OWNED_BY_AUTHOR = "ASIN_NOT_OWNED_BY_AUTHOR"


class SponsoredProductsAsinOwnershipError(BaseModel):
    """Errors related to author asin ownership"""
    cause: Optional["SponsoredProductsErrorCause"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsAsinOwnershipErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsAudienceSegmentType(StrEnum):
    BEHAVIOR_DYNAMIC = "BEHAVIOR_DYNAMIC"
    SPONSORED_ADS_AMC = "SPONSORED_ADS_AMC"


class SponsoredProductsAudienceSegment(BaseModel):
    audience_id: str = Field(..., alias="audienceId", description="`audienceId` is specified based on the `audienceSegmentType` used.")
    audience_segment_type: Optional["SponsoredProductsAudienceSegmentType"] = Field(None, alias="audienceSegmentType")

    model_config = {'populate_by_name': True}


class SponsoredProductsBiddingStrategy(StrEnum):
    AUTO_FOR_SALES = "AUTO_FOR_SALES"
    LEGACY_FOR_SALES = "LEGACY_FOR_SALES"
    MANUAL = "MANUAL"
    OTHER = "OTHER"
    RULE_BASED = "RULE_BASED"


class SponsoredProductsBudgetType(StrEnum):
    DAILY = "DAILY"
    OTHER = "OTHER"


class SponsoredProductsBudget(BaseModel):
    budget: float = Field(..., description="Monetary value")
    budget_type: "SponsoredProductsBudgetType" = Field(..., alias="budgetType")
    effective_budget: Optional[float] = Field(None, alias="effectiveBudget", description="Monetary value")

    model_config = {'populate_by_name': True}


class SponsoredProductsBudgetErrorReason(StrEnum):
    BUDGETING_POLICY_INVALID = "BUDGETING_POLICY_INVALID"
    BUDGET_CURRENCY_DOES_NOT_MATCH_MARKETPLACE_SETTINGS = "BUDGET_CURRENCY_DOES_NOT_MATCH_MARKETPLACE_SETTINGS"
    BUDGET_LT_DEFAULT_BIDS = "BUDGET_LT_DEFAULT_BIDS"
    BUDGET_LT_KEYWORD_BIDS = "BUDGET_LT_KEYWORD_BIDS"
    BUDGET_LT_PREDEFINED_TARGET_BIDS = "BUDGET_LT_PREDEFINED_TARGET_BIDS"
    BUDGET_OUT_OF_MARKET_PLACE_RANGE = "BUDGET_OUT_OF_MARKET_PLACE_RANGE"
    BUDGET_TOO_HIGH = "BUDGET_TOO_HIGH"
    BUDGET_TOO_LOW = "BUDGET_TOO_LOW"
    MISSING_BUDGETING_POLICY = "MISSING_BUDGETING_POLICY"
    MISSING_IN_BUDGET_FLAG = "MISSING_IN_BUDGET_FLAG"


class SponsoredProductsBudgetError(BaseModel):
    cause: Optional["SponsoredProductsErrorCause"] = None
    lower_limit: Optional[str] = Field(None, alias="lowerLimit")
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsBudgetErrorReason"
    upper_limit: Optional[str] = Field(None, alias="upperLimit")

    model_config = {'populate_by_name': True}


class SponsoredProductsBulkAdGroupOperationResponse(BaseModel):
    error: Optional[list["SponsoredProductsAdGroupFailureResponseItem"]] = None
    success: Optional[list["SponsoredProductsAdGroupSuccessResponseItem"]] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeKeywordMutationErrorSelector(BaseModel):
    billing_error: Optional["SponsoredProductsBillingError"] = Field(None, alias="billingError")
    duplicate_value_error: Optional["SponsoredProductsDuplicateValueError"] = Field(None, alias="duplicateValueError")
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    entity_quota_error: Optional["SponsoredProductsEntityQuotaError"] = Field(None, alias="entityQuotaError")
    entity_state_error: Optional["SponsoredProductsEntityStateError"] = Field(None, alias="entityStateError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    parent_entity_error: Optional["SponsoredProductsParentEntityError"] = Field(None, alias="parentEntityError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeKeywordMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsCampaignNegativeKeywordMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeKeywordFailureResponseItem(BaseModel):
    errors: Optional[list["SponsoredProductsCampaignNegativeKeywordMutationError"]] = Field(None, description="A list of validation errors")
    index: int = Field(..., description="the index of the campaign in the array from the request body")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeMatchType(StrEnum):
    NEGATIVE_BROAD = "NEGATIVE_BROAD"
    NEGATIVE_EXACT = "NEGATIVE_EXACT"
    NEGATIVE_PHRASE = "NEGATIVE_PHRASE"
    OTHER = "OTHER"


class SponsoredProductsKeywordServingStatusReason(StrEnum):
    ACCOUNT_OUT_OF_BUDGET_DETAIL = "ACCOUNT_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_ARCHIVED_DETAIL = "ADVERTISER_ARCHIVED_DETAIL"
    ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL = "ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL"
    ADVERTISER_OUT_OF_BUDGET_DETAIL = "ADVERTISER_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_PAUSED_DETAIL = "ADVERTISER_PAUSED_DETAIL"
    ADVERTISER_PAYMENT_FAILURE_DETAIL = "ADVERTISER_PAYMENT_FAILURE_DETAIL"
    ADVERTISER_POLICING_PENDING_REVIEW_DETAIL = "ADVERTISER_POLICING_PENDING_REVIEW_DETAIL"
    ADVERTISER_POLICING_SUSPENDED_DETAIL = "ADVERTISER_POLICING_SUSPENDED_DETAIL"
    AD_GROUP_ARCHIVED_DETAIL = "AD_GROUP_ARCHIVED_DETAIL"
    AD_GROUP_INCOMPLETE_DETAIL = "AD_GROUP_INCOMPLETE_DETAIL"
    AD_GROUP_LOW_BID_DETAIL = "AD_GROUP_LOW_BID_DETAIL"
    AD_GROUP_PAUSED_DETAIL = "AD_GROUP_PAUSED_DETAIL"
    AD_GROUP_POLICING_CREATIVE_REJECTED_DETAIL = "AD_GROUP_POLICING_CREATIVE_REJECTED_DETAIL"
    AD_GROUP_POLICING_PENDING_REVIEW_DETAIL = "AD_GROUP_POLICING_PENDING_REVIEW_DETAIL"
    AD_GROUP_STATUS_ENABLED_DETAIL = "AD_GROUP_STATUS_ENABLED_DETAIL"
    CAMPAIGN_ARCHIVED_DETAIL = "CAMPAIGN_ARCHIVED_DETAIL"
    CAMPAIGN_INCOMPLETE_DETAIL = "CAMPAIGN_INCOMPLETE_DETAIL"
    CAMPAIGN_OUT_OF_BUDGET_DETAIL = "CAMPAIGN_OUT_OF_BUDGET_DETAIL"
    CAMPAIGN_PAUSED_DETAIL = "CAMPAIGN_PAUSED_DETAIL"
    CAMPAIGN_STATUS_ENABLED_DETAIL = "CAMPAIGN_STATUS_ENABLED_DETAIL"
    ENDED_DETAIL = "ENDED_DETAIL"
    OTHER = "OTHER"
    PENDING_REVIEW_DETAIL = "PENDING_REVIEW_DETAIL"
    PENDING_START_DATE_DETAIL = "PENDING_START_DATE_DETAIL"
    PORTFOLIO_ARCHIVED_DETAIL = "PORTFOLIO_ARCHIVED_DETAIL"
    PORTFOLIO_ENDED_DETAIL = "PORTFOLIO_ENDED_DETAIL"
    PORTFOLIO_OUT_OF_BUDGET_DETAIL = "PORTFOLIO_OUT_OF_BUDGET_DETAIL"
    PORTFOLIO_PAUSED_DETAIL = "PORTFOLIO_PAUSED_DETAIL"
    PORTFOLIO_PENDING_START_DATE_DETAIL = "PORTFOLIO_PENDING_START_DATE_DETAIL"
    PORTFOLIO_STATUS_ENABLED_DETAIL = "PORTFOLIO_STATUS_ENABLED_DETAIL"
    REJECTED_DETAIL = "REJECTED_DETAIL"
    TARGETING_CLAUSE_ARCHIVED_DETAIL = "TARGETING_CLAUSE_ARCHIVED_DETAIL"
    TARGETING_CLAUSE_BLOCKED_DETAIL = "TARGETING_CLAUSE_BLOCKED_DETAIL"
    TARGETING_CLAUSE_PAUSED_DETAIL = "TARGETING_CLAUSE_PAUSED_DETAIL"
    TARGETING_CLAUSE_POLICING_SUSPENDED_DETAIL = "TARGETING_CLAUSE_POLICING_SUSPENDED_DETAIL"
    TARGETING_CLAUSE_STATUS_LIVE_DETAIL = "TARGETING_CLAUSE_STATUS_LIVE_DETAIL"


class SponsoredProductsKeywordServingStatusDetail(BaseModel):
    help_url: Optional[str] = Field(None, alias="helpUrl", description="A URL with additional information about the status identifier.")
    message: Optional[str] = Field(None, description="A human-readable description of the status identifier specified in the name field.")
    name: Optional["SponsoredProductsKeywordServingStatusReason"] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsKeywordServingStatus(StrEnum):
    ACCOUNT_OUT_OF_BUDGET = "ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_POLICING_CREATIVE_REJECTED = "AD_GROUP_POLICING_CREATIVE_REJECTED"
    AD_GROUP_POLICING_PENDING_REVIEW = "AD_GROUP_POLICING_PENDING_REVIEW"
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_STATUS_ENABLED = "CAMPAIGN_STATUS_ENABLED"
    ENDED = "ENDED"
    OTHER = "OTHER"
    PENDING_REVIEW = "PENDING_REVIEW"
    PENDING_START_DATE = "PENDING_START_DATE"
    PORTFOLIO_ARCHIVED = "PORTFOLIO_ARCHIVED"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    PORTFOLIO_PAUSED = "PORTFOLIO_PAUSED"
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"
    PORTFOLIO_STATUS_ENABLED = "PORTFOLIO_STATUS_ENABLED"
    REJECTED = "REJECTED"
    TARGETING_CLAUSE_ARCHIVED = "TARGETING_CLAUSE_ARCHIVED"
    TARGETING_CLAUSE_BLOCKED = "TARGETING_CLAUSE_BLOCKED"
    TARGETING_CLAUSE_PAUSED = "TARGETING_CLAUSE_PAUSED"
    TARGETING_CLAUSE_POLICING_SUSPENDED = "TARGETING_CLAUSE_POLICING_SUSPENDED"
    TARGETING_CLAUSE_STATUS_LIVE = "TARGETING_CLAUSE_STATUS_LIVE"


class SponsoredProductsCampaignNegativeKeywordExtendedData(BaseModel):
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="Creation date in ISO 8601.")
    last_update_date_time: Optional[str] = Field(None, alias="lastUpdateDateTime", description="Last updated date in ISO 8601.")
    serving_status: Optional["SponsoredProductsKeywordServingStatus"] = Field(None, alias="servingStatus")
    serving_status_details: Optional[list["SponsoredProductsKeywordServingStatusDetail"]] = Field(None, alias="servingStatusDetails", description="The serving status reasons of the Keyword")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeKeyword(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign to which the keyword is associated.")
    extended_data: Optional["SponsoredProductsCampaignNegativeKeywordExtendedData"] = Field(None, alias="extendedData")
    global_keyword_id: Optional[str] = Field(None, alias="globalKeywordId", description="The global keyword identifier that manages this marketplace keyword.")
    keyword_id: str = Field(..., alias="keywordId", description="The identifier of the keyword.")
    keyword_text: str = Field(..., alias="keywordText", description="The keyword text.")
    match_type: "SponsoredProductsNegativeMatchType" = Field(..., alias="matchType")
    state: "SponsoredProductsEntityState"

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeKeywordSuccessResponseItem(BaseModel):
    campaign_negative_keyword: Optional["SponsoredProductsCampaignNegativeKeyword"] = Field(None, alias="campaignNegativeKeyword")
    campaign_negative_keyword_id: Optional[str] = Field(None, alias="campaignNegativeKeywordId", description="the campaignNegativeKeyword ID")
    index: int = Field(..., description="the index of the campaign in the array from the request body")

    model_config = {'populate_by_name': True}


class SponsoredProductsBulkCampaignNegativeKeywordOperationResponse(BaseModel):
    error: Optional[list["SponsoredProductsCampaignNegativeKeywordFailureResponseItem"]] = None
    success: Optional[list["SponsoredProductsCampaignNegativeKeywordSuccessResponseItem"]] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetingClauseSetupErrorReason(StrEnum):
    AUTO_TARGETING_CLAUSE_CANNOT_BE_CREATED_MANUALLY = "AUTO_TARGETING_CLAUSE_CANNOT_BE_CREATED_MANUALLY"
    TARGETING_EXPRESSION_INVALID_VALUE = "TARGETING_EXPRESSION_INVALID_VALUE"
    TARGETING_TYPE_NOT_ALLOWED_FOR_AUTO_TARGETING_CAMPAIGN = "TARGETING_TYPE_NOT_ALLOWED_FOR_AUTO_TARGETING_CAMPAIGN"
    TYPE_CONFLICT_IN_AD_GROUP = "TYPE_CONFLICT_IN_AD_GROUP"


class SponsoredProductsTargetingClauseSetupError(BaseModel):
    """Errors related to targeting clause setup"""
    cause: Optional["SponsoredProductsErrorCause"] = None
    marketplace: Optional["SponsoredProductsMarketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsTargetingClauseSetupErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeTargetsMutationErrorSelector(BaseModel):
    billing_error: Optional["SponsoredProductsBillingError"] = Field(None, alias="billingError")
    duplicate_value_error: Optional["SponsoredProductsDuplicateValueError"] = Field(None, alias="duplicateValueError")
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    entity_quota_error: Optional["SponsoredProductsEntityQuotaError"] = Field(None, alias="entityQuotaError")
    entity_state_error: Optional["SponsoredProductsEntityStateError"] = Field(None, alias="entityStateError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    parent_entity_error: Optional["SponsoredProductsParentEntityError"] = Field(None, alias="parentEntityError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    targeting_clause_setup_error: Optional["SponsoredProductsTargetingClauseSetupError"] = Field(None, alias="targetingClauseSetupError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeTargetsMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsCampaignNegativeTargetsMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeTargetingClauseFailureResponseItem(BaseModel):
    errors: Optional[list["SponsoredProductsCampaignNegativeTargetsMutationError"]] = Field(None, description="A list of validation errors")
    index: int = Field(..., description="the index of the CampaignNegativeTargets in the array from the request body")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeTargetingExpressionPredicateType(StrEnum):
    ASIN_BRAND_SAME_AS = "ASIN_BRAND_SAME_AS"
    ASIN_SAME_AS = "ASIN_SAME_AS"
    OTHER = "OTHER"


class SponsoredProductsNegativeTargetingExpressionPredicate(BaseModel):
    type_: Optional["SponsoredProductsNegativeTargetingExpressionPredicateType"] = Field(None, alias="type")
    value: Optional[str] = Field(None, description="The expression value")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeTargetingClauseExtendedData(BaseModel):
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="Creation date in ISO 8601.")
    last_update_date_time: Optional[str] = Field(None, alias="lastUpdateDateTime", description="Last updated date in ISO 8601.")
    serving_status: Optional["SponsoredProductsKeywordServingStatus"] = Field(None, alias="servingStatus")
    serving_status_details: Optional[list["SponsoredProductsKeywordServingStatusDetail"]] = Field(None, alias="servingStatusDetails", description="The serving status reasons of the CampaignNegativeTargetingClause")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeTargetingClause(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign to which this target is associated.")
    expression: list["SponsoredProductsNegativeTargetingExpressionPredicate"] = Field(..., description="The CampaignNegativeTargetingClause expression.")
    extended_data: Optional["SponsoredProductsCampaignNegativeTargetingClauseExtendedData"] = Field(None, alias="extendedData")
    global_target_id: Optional[str] = Field(None, alias="globalTargetId", description="The global target identifier that manages this marketplace target.")
    resolved_expression: list["SponsoredProductsNegativeTargetingExpressionPredicate"] = Field(..., alias="resolvedExpression", description="The resolved CampaignNegativeTargetingClause expression.")
    state: "SponsoredProductsEntityState"
    target_id: str = Field(..., alias="targetId", description="The target identifier")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeTargetingClauseSuccessResponseItem(BaseModel):
    campaign_negative_targeting_clause_id: Optional[str] = Field(None, alias="campaignNegativeTargetingClauseId", description="the CampaignNegativeTargets ID")
    campaign_negative_targeting_clauses: Optional["SponsoredProductsCampaignNegativeTargetingClause"] = Field(None, alias="campaignNegativeTargetingClauses")
    index: int = Field(..., description="the index of the CampaignNegativeTargets in the array from the request body")

    model_config = {'populate_by_name': True}


class SponsoredProductsBulkCampaignNegativeTargetingClauseOperationResponse(BaseModel):
    error: Optional[list["SponsoredProductsCampaignNegativeTargetingClauseFailureResponseItem"]] = None
    success: Optional[list["SponsoredProductsCampaignNegativeTargetingClauseSuccessResponseItem"]] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsDateErrorReason(StrEnum):
    END_DATE_EARLIER_THAN_TODAY = "END_DATE_EARLIER_THAN_TODAY"
    END_DATE_LATER_THAN_MAXIMUM = "END_DATE_LATER_THAN_MAXIMUM"
    INVALID_DATE = "INVALID_DATE"
    START_DATE_AFTER_END_DATE = "START_DATE_AFTER_END_DATE"
    START_DATE_EARLIER_THAN_TODAY = "START_DATE_EARLIER_THAN_TODAY"
    START_DATE_LATER_THAN_MAXIMUM = "START_DATE_LATER_THAN_MAXIMUM"
    UPDATING_ENDED_CAMPAIGN_WITHOUT_EXTENSION = "UPDATING_ENDED_CAMPAIGN_WITHOUT_EXTENSION"
    UPDATING_READ_ONLY_END_DATE = "UPDATING_READ_ONLY_END_DATE"
    UPDATING_READ_ONLY_START_DATE = "UPDATING_READ_ONLY_START_DATE"


class SponsoredProductsDateError(BaseModel):
    cause: Optional["SponsoredProductsErrorCause"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsDateErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsCurrencyErrorReason(StrEnum):
    CANNOT_UPDATE_CURRENCY = "CANNOT_UPDATE_CURRENCY"
    CURRENCY_NOT_MATCHING_PREFERRED_CURRENCY = "CURRENCY_NOT_MATCHING_PREFERRED_CURRENCY"
    CURRENCY_NOT_SUPPORTED = "CURRENCY_NOT_SUPPORTED"
    PREFERRED_CURRENCY_NOT_SET = "PREFERRED_CURRENCY_NOT_SET"


class SponsoredProductsCurrencyError(BaseModel):
    """Errors related to currency"""
    cause: Optional["SponsoredProductsErrorCause"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsCurrencyErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignMutationErrorSelector(BaseModel):
    bidding_error: Optional["SponsoredProductsBiddingError"] = Field(None, alias="biddingError")
    billing_error: Optional["SponsoredProductsBillingError"] = Field(None, alias="billingError")
    budget_error: Optional["SponsoredProductsBudgetError"] = Field(None, alias="budgetError")
    currency_error: Optional["SponsoredProductsCurrencyError"] = Field(None, alias="currencyError")
    date_error: Optional["SponsoredProductsDateError"] = Field(None, alias="dateError")
    duplicate_value_error: Optional["SponsoredProductsDuplicateValueError"] = Field(None, alias="duplicateValueError")
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    entity_quota_error: Optional["SponsoredProductsEntityQuotaError"] = Field(None, alias="entityQuotaError")
    entity_state_error: Optional["SponsoredProductsEntityStateError"] = Field(None, alias="entityStateError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    parent_entity_error: Optional["SponsoredProductsParentEntityError"] = Field(None, alias="parentEntityError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsCampaignMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignMutationFailureResponseItem(BaseModel):
    errors: Optional[list["SponsoredProductsCampaignMutationError"]] = Field(None, description="A list of validation errors")
    index: int = Field(..., description="the index of the campaign in the array from the request body")

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetingType(StrEnum):
    AUTO = "AUTO"
    MANUAL = "MANUAL"


class SponsoredProductsOffAmazonBudgetControlStrategy(StrEnum):
    MAXIMIZE_REACH = "MAXIMIZE_REACH"
    MINIMIZE_SPEND = "MINIMIZE_SPEND"


class SponsoredProductsOffAmazonSettings(BaseModel):
    off_amazon_budget_control_strategy: Optional["SponsoredProductsOffAmazonBudgetControlStrategy"] = Field(None, alias="offAmazonBudgetControlStrategy")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignServingStatusReason(StrEnum):
    ACCOUNT_OUT_OF_BUDGET_DETAIL = "ACCOUNT_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_ARCHIVED_DETAIL = "ADVERTISER_ARCHIVED_DETAIL"
    ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL = "ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL"
    ADVERTISER_OUT_OF_BUDGET_DETAIL = "ADVERTISER_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_PAUSED_DETAIL = "ADVERTISER_PAUSED_DETAIL"
    ADVERTISER_PAYMENT_FAILURE_DETAIL = "ADVERTISER_PAYMENT_FAILURE_DETAIL"
    ADVERTISER_POLICING_PENDING_REVIEW_DETAIL = "ADVERTISER_POLICING_PENDING_REVIEW_DETAIL"
    ADVERTISER_POLICING_SUSPENDED_DETAIL = "ADVERTISER_POLICING_SUSPENDED_DETAIL"
    CAMPAIGN_ARCHIVED_DETAIL = "CAMPAIGN_ARCHIVED_DETAIL"
    CAMPAIGN_INCOMPLETE_DETAIL = "CAMPAIGN_INCOMPLETE_DETAIL"
    CAMPAIGN_OUT_OF_BUDGET_DETAIL = "CAMPAIGN_OUT_OF_BUDGET_DETAIL"
    CAMPAIGN_PAUSED_DETAIL = "CAMPAIGN_PAUSED_DETAIL"
    CAMPAIGN_STATUS_ENABLED_DETAIL = "CAMPAIGN_STATUS_ENABLED_DETAIL"
    ENDED_DETAIL = "ENDED_DETAIL"
    OTHER = "OTHER"
    PENDING_REVIEW_DETAIL = "PENDING_REVIEW_DETAIL"
    PENDING_START_DATE_DETAIL = "PENDING_START_DATE_DETAIL"
    PORTFOLIO_ARCHIVED_DETAIL = "PORTFOLIO_ARCHIVED_DETAIL"
    PORTFOLIO_ENDED_DETAIL = "PORTFOLIO_ENDED_DETAIL"
    PORTFOLIO_OUT_OF_BUDGET_DETAIL = "PORTFOLIO_OUT_OF_BUDGET_DETAIL"
    PORTFOLIO_PAUSED_DETAIL = "PORTFOLIO_PAUSED_DETAIL"
    PORTFOLIO_PENDING_START_DATE_DETAIL = "PORTFOLIO_PENDING_START_DATE_DETAIL"
    PORTFOLIO_STATUS_ENABLED_DETAIL = "PORTFOLIO_STATUS_ENABLED_DETAIL"
    REJECTED_DETAIL = "REJECTED_DETAIL"


class SponsoredProductsCampaignServingStatusDetail(BaseModel):
    help_url: Optional[str] = Field(None, alias="helpUrl", description="A URL with additional information about the status identifier.")
    message: Optional[str] = Field(None, description="A human-readable description of the status identifier specified in the name field.")
    name: Optional["SponsoredProductsCampaignServingStatusReason"] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignServingStatus(StrEnum):
    ACCOUNT_OUT_OF_BUDGET = "ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_STATUS_ENABLED = "CAMPAIGN_STATUS_ENABLED"
    ENDED = "ENDED"
    OTHER = "OTHER"
    PENDING_REVIEW = "PENDING_REVIEW"
    PENDING_START_DATE = "PENDING_START_DATE"
    PORTFOLIO_ARCHIVED = "PORTFOLIO_ARCHIVED"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    PORTFOLIO_PAUSED = "PORTFOLIO_PAUSED"
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"
    PORTFOLIO_STATUS_ENABLED = "PORTFOLIO_STATUS_ENABLED"
    REJECTED = "REJECTED"


class SponsoredProductsCampaignExtendedData(BaseModel):
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="Creation date in ISO 8601.")
    last_update_date_time: Optional[str] = Field(None, alias="lastUpdateDateTime", description="Last updated date in ISO 8601.")
    serving_status: Optional["SponsoredProductsCampaignServingStatus"] = Field(None, alias="servingStatus")
    serving_status_details: Optional[list["SponsoredProductsCampaignServingStatusDetail"]] = Field(None, alias="servingStatusDetails", description="The serving status reasons of the Campaign")

    model_config = {'populate_by_name': True}


class SponsoredProductsMarketplaceBudgetAllocation(StrEnum):
    AUTO = "AUTO"
    MANUAL = "MANUAL"


class SponsoredProductsShopperCohortType(StrEnum):
    AUDIENCE_SEGMENT = "AUDIENCE_SEGMENT"


class SponsoredProductsShopperCohortBidding(BaseModel):
    audience_segments: Optional[list["SponsoredProductsAudienceSegment"]] = Field(None, alias="audienceSegments", description="A list of Audience Segments. Shoppers belonging to these segments will be selected for applying the bid adjustments. Thi")
    percentage: Optional[int] = None
    shopper_cohort_type: "SponsoredProductsShopperCohortType" = Field(..., alias="shopperCohortType")

    model_config = {'populate_by_name': True}


class SponsoredProductsPlacement(StrEnum):
    PLACEMENT_PRODUCT_PAGE = "PLACEMENT_PRODUCT_PAGE"
    PLACEMENT_REST_OF_SEARCH = "PLACEMENT_REST_OF_SEARCH"
    PLACEMENT_TOP = "PLACEMENT_TOP"
    SITE_AMAZON_BUSINESS = "SITE_AMAZON_BUSINESS"


class SponsoredProductsPlacementBidding(BaseModel):
    percentage: Optional[int] = None
    placement: Optional["SponsoredProductsPlacement"] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsDynamicBidding(BaseModel):
    placement_bidding: Optional[list["SponsoredProductsPlacementBidding"]] = Field(None, alias="placementBidding")
    shopper_cohort_bidding: Optional[list["SponsoredProductsShopperCohortBidding"]] = Field(None, alias="shopperCohortBidding", description="Specifies Shopper Cohorts based bid adjustment controls. `shopperCohortBidding` is optional for both Create and Update r")
    strategy: "SponsoredProductsBiddingStrategy"

    model_config = {'populate_by_name': True}


class SponsoredProductsTags(BaseModel):
    """A list of advertiser-specified custom identifiers for the campaign. Each customer identifier is a key-value pair. You can specify a maximum of 50 identifiers."""
    __root__: dict[str, str] = {}


class SponsoredProductsSiteRestriction(StrEnum):
    AMAZON_BUSINESS = "AMAZON_BUSINESS"
    AMAZON_HAUL = "AMAZON_HAUL"


class SponsoredProductsCampaign(BaseModel):
    auto_manage_campaign: Optional[bool] = Field(None, alias="autoManageCampaign")
    budget: "SponsoredProductsBudget"
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign.")
    dynamic_bidding: Optional["SponsoredProductsDynamicBidding"] = Field(None, alias="dynamicBidding")
    end_date: Optional[str] = Field(None, alias="endDate", description="The format of the date is YYYY-MM-DD.")
    extended_data: Optional["SponsoredProductsCampaignExtendedData"] = Field(None, alias="extendedData")
    global_campaign_id: Optional[str] = Field(None, alias="globalCampaignId", description="The global campaign identifier that manages this marketplace campaign.")
    marketplace_budget_allocation: Optional["SponsoredProductsMarketplaceBudgetAllocation"] = Field(None, alias="marketplaceBudgetAllocation")
    name: str = Field(..., description="The name of the campaign.")
    off_amazon_settings: Optional["SponsoredProductsOffAmazonSettings"] = Field(None, alias="offAmazonSettings")
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="The identifier of an existing portfolio to which the campaign is associated.")
    site_restrictions: Optional[list["SponsoredProductsSiteRestriction"]] = Field(None, alias="siteRestrictions")
    start_date: str = Field(..., alias="startDate", description="The format of the date is YYYY-MM-DD.")
    state: "SponsoredProductsEntityState"
    tags: Optional["SponsoredProductsTags"] = None
    targeting_type: "SponsoredProductsTargetingType" = Field(..., alias="targetingType")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignMutationSuccessResponseItem(BaseModel):
    campaign: Optional["SponsoredProductsCampaign"] = None
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="the campaign ID")
    index: int = Field(..., description="the index of the campaign in the array from the request body")

    model_config = {'populate_by_name': True}


class SponsoredProductsBulkCampaignOperationResponse(BaseModel):
    error: Optional[list["SponsoredProductsCampaignMutationFailureResponseItem"]] = None
    success: Optional[list["SponsoredProductsCampaignMutationSuccessResponseItem"]] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsLocaleErrorReason(StrEnum):
    INVALID_LOCALE = "INVALID_LOCALE"


class SponsoredProductsLocaleError(BaseModel):
    cause: Optional["SponsoredProductsErrorCause"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsLocaleErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsKeywordMutationErrorSelector(BaseModel):
    bidding_error: Optional["SponsoredProductsBiddingError"] = Field(None, alias="biddingError")
    billing_error: Optional["SponsoredProductsBillingError"] = Field(None, alias="billingError")
    duplicate_value_error: Optional["SponsoredProductsDuplicateValueError"] = Field(None, alias="duplicateValueError")
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    entity_quota_error: Optional["SponsoredProductsEntityQuotaError"] = Field(None, alias="entityQuotaError")
    entity_state_error: Optional["SponsoredProductsEntityStateError"] = Field(None, alias="entityStateError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    locale_error: Optional["SponsoredProductsLocaleError"] = Field(None, alias="localeError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    parent_entity_error: Optional["SponsoredProductsParentEntityError"] = Field(None, alias="parentEntityError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    targeting_clause_setup_error: Optional["SponsoredProductsTargetingClauseSetupError"] = Field(None, alias="targetingClauseSetupError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class SponsoredProductsKeywordMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsKeywordMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsKeywordFailureResponseItem(BaseModel):
    errors: Optional[list["SponsoredProductsKeywordMutationError"]] = Field(None, description="A list of validation errors")
    index: int = Field(..., description="the index of the keyword in the array from the request body")

    model_config = {'populate_by_name': True}


class SponsoredProductsKeywordExtendedData(BaseModel):
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="Creation date in ISO 8601.")
    last_update_date_time: Optional[str] = Field(None, alias="lastUpdateDateTime", description="Last updated date in ISO 8601.")
    serving_status: Optional["SponsoredProductsKeywordServingStatus"] = Field(None, alias="servingStatus")
    serving_status_details: Optional[list["SponsoredProductsKeywordServingStatusDetail"]] = Field(None, alias="servingStatusDetails", description="The serving status reasons of the Keyword")

    model_config = {'populate_by_name': True}


class SponsoredProductsMatchType(StrEnum):
    BROAD = "BROAD"
    EXACT = "EXACT"
    OTHER = "OTHER"
    PHRASE = "PHRASE"


class SponsoredProductsKeyword(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the ad group to which this keyword is associated.")
    bid: Optional[float] = Field(None, description="Bid associated with this keyword. Applicable to biddable match types only. Keywords that do not have bid values in listK")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign to which the keyword is associated.")
    extended_data: Optional["SponsoredProductsKeywordExtendedData"] = Field(None, alias="extendedData")
    global_keyword_id: Optional[str] = Field(None, alias="globalKeywordId", description="The global keyword identifier that manages this marketplace keyword.")
    keyword_id: str = Field(..., alias="keywordId", description="The identifier of the keyword.")
    keyword_text: str = Field(..., alias="keywordText", description="The keyword text.")
    match_type: "SponsoredProductsMatchType" = Field(..., alias="matchType")
    native_language_keyword: Optional[str] = Field(None, alias="nativeLanguageKeyword", description="The unlocalized keyword text in the preferred locale of the advertiser.")
    native_language_locale: Optional[str] = Field(None, alias="nativeLanguageLocale", description="The locale preference of the advertiser. For example, if the advertiser’s preferred language is Simplified Chinese, set ")
    state: "SponsoredProductsEntityState"

    model_config = {'populate_by_name': True}


class SponsoredProductsKeywordSuccessResponseItem(BaseModel):
    index: int = Field(..., description="the index of the keyword in the array from the request body")
    keyword: Optional["SponsoredProductsKeyword"] = None
    keyword_id: Optional[str] = Field(None, alias="keywordId", description="the keyword ID")

    model_config = {'populate_by_name': True}


class SponsoredProductsBulkKeywordOperationResponse(BaseModel):
    error: Optional[list["SponsoredProductsKeywordFailureResponseItem"]] = None
    success: Optional[list["SponsoredProductsKeywordSuccessResponseItem"]] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeKeywordExtendedData(BaseModel):
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="Creation date in ISO 8601.")
    last_update_date_time: Optional[str] = Field(None, alias="lastUpdateDateTime", description="Last updated date in ISO 8601.")
    serving_status: Optional["SponsoredProductsKeywordServingStatus"] = Field(None, alias="servingStatus")
    serving_status_details: Optional[list["SponsoredProductsKeywordServingStatusDetail"]] = Field(None, alias="servingStatusDetails", description="The serving status reasons of the Keyword")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeKeyword(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the ad group to which this keyword is associated.")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign to which the keyword is associated.")
    extended_data: Optional["SponsoredProductsNegativeKeywordExtendedData"] = Field(None, alias="extendedData")
    global_keyword_id: Optional[str] = Field(None, alias="globalKeywordId", description="The global keyword identifier that manages this marketplace keyword.")
    keyword_id: str = Field(..., alias="keywordId", description="The identifier of the keyword.")
    keyword_text: str = Field(..., alias="keywordText", description="The keyword text.")
    match_type: "SponsoredProductsNegativeMatchType" = Field(..., alias="matchType")
    native_language_keyword: Optional[str] = Field(None, alias="nativeLanguageKeyword", description="The unlocalized keyword text in the preferred locale of the advertiser")
    native_language_locale: Optional[str] = Field(None, alias="nativeLanguageLocale", description="The locale preference of the advertiser.")
    state: "SponsoredProductsEntityState"

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeKeywordSuccessResponseItem(BaseModel):
    index: int = Field(..., description="the index of the negativeKeyword in the array from the request body")
    negative_keyword: Optional["SponsoredProductsNegativeKeyword"] = Field(None, alias="negativeKeyword")
    negative_keyword_id: Optional[str] = Field(None, alias="negativeKeywordId", description="the negativeKeyword ID")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeKeywordMutationErrorSelector(BaseModel):
    billing_error: Optional["SponsoredProductsBillingError"] = Field(None, alias="billingError")
    duplicate_value_error: Optional["SponsoredProductsDuplicateValueError"] = Field(None, alias="duplicateValueError")
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    entity_quota_error: Optional["SponsoredProductsEntityQuotaError"] = Field(None, alias="entityQuotaError")
    entity_state_error: Optional["SponsoredProductsEntityStateError"] = Field(None, alias="entityStateError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    parent_entity_error: Optional["SponsoredProductsParentEntityError"] = Field(None, alias="parentEntityError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    targeting_clause_setup_error: Optional["SponsoredProductsTargetingClauseSetupError"] = Field(None, alias="targetingClauseSetupError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeKeywordMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsNegativeKeywordMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeKeywordFailureResponseItem(BaseModel):
    errors: Optional[list["SponsoredProductsNegativeKeywordMutationError"]] = Field(None, description="A list of validation errors")
    index: int = Field(..., description="the index of the negativeKeyword in the array from the request body")

    model_config = {'populate_by_name': True}


class SponsoredProductsBulkNegativeKeywordOperationResponse(BaseModel):
    error: Optional[list["SponsoredProductsNegativeKeywordFailureResponseItem"]] = None
    success: Optional[list["SponsoredProductsNegativeKeywordSuccessResponseItem"]] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeTargetingClauseExtendedData(BaseModel):
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="Creation date in ISO 8601.")
    last_update_date_time: Optional[str] = Field(None, alias="lastUpdateDateTime", description="Last updated date in ISO 8601.")
    serving_status: Optional["SponsoredProductsKeywordServingStatus"] = Field(None, alias="servingStatus")
    serving_status_details: Optional[list["SponsoredProductsKeywordServingStatusDetail"]] = Field(None, alias="servingStatusDetails", description="The serving status reasons of the NegativeTargetingClause")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeTargetingClause(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the ad group to which this target is associated.")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign to which this target is associated.")
    expression: list["SponsoredProductsNegativeTargetingExpressionPredicate"] = Field(..., description="The NegativeTargeting expression.")
    extended_data: Optional["SponsoredProductsNegativeTargetingClauseExtendedData"] = Field(None, alias="extendedData")
    global_target_id: Optional[str] = Field(None, alias="globalTargetId", description="The global target identifier that manages this marketplace target.")
    resolved_expression: list["SponsoredProductsNegativeTargetingExpressionPredicate"] = Field(..., alias="resolvedExpression", description="The resolved NegativeTargeting expression.")
    state: "SponsoredProductsEntityState"
    target_id: str = Field(..., alias="targetId", description="The target identifier")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeTargetingClauseSuccessResponseItem(BaseModel):
    index: int = Field(..., description="the index of the NegativeTargetingClause in the array from the request body")
    negative_targeting_clause: Optional["SponsoredProductsNegativeTargetingClause"] = Field(None, alias="negativeTargetingClause")
    target_id: Optional[str] = Field(None, alias="targetId", description="the NegativeTargetingClause ID")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeTargetMutationErrorSelector(BaseModel):
    billing_error: Optional["SponsoredProductsBillingError"] = Field(None, alias="billingError")
    duplicate_value_error: Optional["SponsoredProductsDuplicateValueError"] = Field(None, alias="duplicateValueError")
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    entity_quota_error: Optional["SponsoredProductsEntityQuotaError"] = Field(None, alias="entityQuotaError")
    entity_state_error: Optional["SponsoredProductsEntityStateError"] = Field(None, alias="entityStateError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    parent_entity_error: Optional["SponsoredProductsParentEntityError"] = Field(None, alias="parentEntityError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    targeting_clause_setup_error: Optional["SponsoredProductsTargetingClauseSetupError"] = Field(None, alias="targetingClauseSetupError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeTargetMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsNegativeTargetMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeTargetingClauseFailureResponseItem(BaseModel):
    errors: Optional[list["SponsoredProductsNegativeTargetMutationError"]] = Field(None, description="A list of validation errors")
    index: int = Field(..., description="the index of the NegativeTargetingClause in the array from the request body")

    model_config = {'populate_by_name': True}


class SponsoredProductsBulkNegativeTargetingClauseOperationResponse(BaseModel):
    error: Optional[list["SponsoredProductsNegativeTargetingClauseFailureResponseItem"]] = None
    success: Optional[list["SponsoredProductsNegativeTargetingClauseSuccessResponseItem"]] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsUnsupportedOperationErrorReason(StrEnum):
    UNSUPPORTED_OPERATION = "UNSUPPORTED_OPERATION"


class SponsoredProductsUnsupportedOperationError(BaseModel):
    """Errors being used to represent an unsupported operation e.g. Seller are not supported to create custom text product ads."""
    cause: Optional["SponsoredProductsErrorCause"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsUnsupportedOperationErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsProductIdentifierErrorReason(StrEnum):
    INVALID_ASIN = "INVALID_ASIN"
    INVALID_SKU = "INVALID_SKU"


class SponsoredProductsProductIdentifierError(BaseModel):
    """Errors related to product identifiers"""
    cause: Optional["SponsoredProductsErrorCause"] = None
    marketplace: Optional["SponsoredProductsMarketplace"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsProductIdentifierErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsProductAdMutationErrorSelector(BaseModel):
    ad_eligibility_error: Optional["SponsoredProductsAdEligibilityError"] = Field(None, alias="adEligibilityError")
    asin_ownership_error: Optional["SponsoredProductsAsinOwnershipError"] = Field(None, alias="asinOwnershipError")
    billing_error: Optional["SponsoredProductsBillingError"] = Field(None, alias="billingError")
    duplicate_value_error: Optional["SponsoredProductsDuplicateValueError"] = Field(None, alias="duplicateValueError")
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    entity_quota_error: Optional["SponsoredProductsEntityQuotaError"] = Field(None, alias="entityQuotaError")
    entity_state_error: Optional["SponsoredProductsEntityStateError"] = Field(None, alias="entityStateError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    parent_entity_error: Optional["SponsoredProductsParentEntityError"] = Field(None, alias="parentEntityError")
    product_identifier_error: Optional["SponsoredProductsProductIdentifierError"] = Field(None, alias="productIdentifierError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")
    unsupported_operation_error: Optional["SponsoredProductsUnsupportedOperationError"] = Field(None, alias="unsupportedOperationError")

    model_config = {'populate_by_name': True}


class SponsoredProductsProductAdMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsProductAdMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsProductAdFailureResponseItem(BaseModel):
    errors: Optional[list["SponsoredProductsProductAdMutationError"]] = Field(None, description="A list of validation errors")
    index: int = Field(..., description="the index of the product ad in the array from the request body")

    model_config = {'populate_by_name': True}


class SponsoredProductsProductAdExtendedData(BaseModel):
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="Creation date in ISO 8601.")
    last_update_date_time: Optional[str] = Field(None, alias="lastUpdateDateTime", description="Last updated date in ISO 8601.")
    serving_status: Optional["SponsoredProductsAdServingStatus"] = Field(None, alias="servingStatus")
    serving_status_details: Optional[list["SponsoredProductsAdServingStatusDetail"]] = Field(None, alias="servingStatusDetails", description="The serving status reasons of the Ad")

    model_config = {'populate_by_name': True}


class SponsoredProductsGlobalStoreSetting(BaseModel):
    catalog_source_country_code: Optional[str] = Field(None, alias="catalogSourceCountryCode", description="Country code of source marketplace where seller has listed the product. Possible source country codes include US, UK, DE")

    model_config = {'populate_by_name': True}


class SponsoredProductsProductAd(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The ad group identifier.")
    ad_id: str = Field(..., alias="adId", description="The product ad identifier.")
    asin: Optional[str] = Field(None, description="The ASIN associated with the product. Defined for vendors only.")
    campaign_id: str = Field(..., alias="campaignId", description="The campaign identifier.")
    custom_text: Optional[str] = Field(None, alias="customText", description="The custom text that is associated with this ad. Defined for custom text ads only.")
    extended_data: Optional["SponsoredProductsProductAdExtendedData"] = Field(None, alias="extendedData")
    global_ad_id: Optional[str] = Field(None, alias="globalAdId", description="The global ad identifier that manages this marketplace ad.")
    global_store_setting: Optional["SponsoredProductsGlobalStoreSetting"] = Field(None, alias="globalStoreSetting")
    sku: Optional[str] = Field(None, description="The SKU associated with the product. Defined for seller accounts only.")
    state: "SponsoredProductsEntityState"

    model_config = {'populate_by_name': True}


class SponsoredProductsProductAdSuccessResponseItem(BaseModel):
    ad_id: Optional[str] = Field(None, alias="adId", description="the ProductAd ID")
    index: int = Field(..., description="The index in the original list from the request.")
    product_ad: Optional["SponsoredProductsProductAd"] = Field(None, alias="productAd")

    model_config = {'populate_by_name': True}


class SponsoredProductsBulkProductAdOperationResponse(BaseModel):
    error: Optional[list["SponsoredProductsProductAdFailureResponseItem"]] = None
    success: Optional[list["SponsoredProductsProductAdSuccessResponseItem"]] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsExpressionTypeErrorReason(StrEnum):
    UNSUPPORTED_EXPRESSION_TYPE = "UNSUPPORTED_EXPRESSION_TYPE"


class SponsoredProductsExpressionTypeError(BaseModel):
    cause: Optional["SponsoredProductsErrorCause"] = None
    message: str = Field(..., description="Human readable error message")
    reason: "SponsoredProductsExpressionTypeErrorReason"

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetMutationErrorSelector(BaseModel):
    bidding_error: Optional["SponsoredProductsBiddingError"] = Field(None, alias="biddingError")
    billing_error: Optional["SponsoredProductsBillingError"] = Field(None, alias="billingError")
    duplicate_value_error: Optional["SponsoredProductsDuplicateValueError"] = Field(None, alias="duplicateValueError")
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    entity_quota_error: Optional["SponsoredProductsEntityQuotaError"] = Field(None, alias="entityQuotaError")
    entity_state_error: Optional["SponsoredProductsEntityStateError"] = Field(None, alias="entityStateError")
    expression_type_error: Optional["SponsoredProductsExpressionTypeError"] = Field(None, alias="expressionTypeError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    parent_entity_error: Optional["SponsoredProductsParentEntityError"] = Field(None, alias="parentEntityError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    targeting_clause_setup_error: Optional["SponsoredProductsTargetingClauseSetupError"] = Field(None, alias="targetingClauseSetupError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetMutationError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsTargetMutationErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetingClauseFailureResponseItem(BaseModel):
    errors: Optional[list["SponsoredProductsTargetMutationError"]] = Field(None, description="A list of validation errors")
    index: int = Field(..., description="the index of the targetingClause in the array from the request body")

    model_config = {'populate_by_name': True}


class SponsoredProductsExpressionType(StrEnum):
    AUTO = "AUTO"
    MANUAL = "MANUAL"
    OTHER = "OTHER"


class SponsoredProductsTargetingClauseExtendedData(BaseModel):
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="Creation date in ISO 8601.")
    last_update_date_time: Optional[str] = Field(None, alias="lastUpdateDateTime", description="Last updated date in ISO 8601.")
    serving_status: Optional["SponsoredProductsKeywordServingStatus"] = Field(None, alias="servingStatus")
    serving_status_details: Optional[list["SponsoredProductsKeywordServingStatusDetail"]] = Field(None, alias="servingStatusDetails", description="The serving status reasons of the TargetingClause")

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetingExpressionPredicateType(StrEnum):
    ASIN_ACCESSORY_RELATED = "ASIN_ACCESSORY_RELATED"
    ASIN_AGE_RANGE_SAME_AS = "ASIN_AGE_RANGE_SAME_AS"
    ASIN_BRAND_SAME_AS = "ASIN_BRAND_SAME_AS"
    ASIN_CATEGORY_SAME_AS = "ASIN_CATEGORY_SAME_AS"
    ASIN_EXPANDED_FROM = "ASIN_EXPANDED_FROM"
    ASIN_GENRE_SAME_AS = "ASIN_GENRE_SAME_AS"
    ASIN_IS_PRIME_SHIPPING_ELIGIBLE = "ASIN_IS_PRIME_SHIPPING_ELIGIBLE"
    ASIN_PRICE_BETWEEN = "ASIN_PRICE_BETWEEN"
    ASIN_PRICE_GREATER_THAN = "ASIN_PRICE_GREATER_THAN"
    ASIN_PRICE_LESS_THAN = "ASIN_PRICE_LESS_THAN"
    ASIN_REVIEW_RATING_BETWEEN = "ASIN_REVIEW_RATING_BETWEEN"
    ASIN_REVIEW_RATING_GREATER_THAN = "ASIN_REVIEW_RATING_GREATER_THAN"
    ASIN_REVIEW_RATING_LESS_THAN = "ASIN_REVIEW_RATING_LESS_THAN"
    ASIN_SAME_AS = "ASIN_SAME_AS"
    ASIN_SUBSTITUTE_RELATED = "ASIN_SUBSTITUTE_RELATED"
    KEYWORD_GROUP_SAME_AS = "KEYWORD_GROUP_SAME_AS"
    OTHER = "OTHER"
    QUERY_BROAD_REL_MATCHES = "QUERY_BROAD_REL_MATCHES"
    QUERY_HIGH_REL_MATCHES = "QUERY_HIGH_REL_MATCHES"


class SponsoredProductsTargetingExpressionPredicate(BaseModel):
    type_: Optional["SponsoredProductsTargetingExpressionPredicateType"] = Field(None, alias="type")
    value: Optional[str] = Field(None, description="The expression value")

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetingClause(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the ad group to which this target is associated.")
    bid: Optional[float] = Field(None, description="The bid for ads sourced using the target. Targets that do not have bid values in listTargetingClauses will inherit the d")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign to which this target is associated.")
    expression: list["SponsoredProductsTargetingExpressionPredicate"] = Field(..., description="The targeting expression.")
    expression_type: "SponsoredProductsExpressionType" = Field(..., alias="expressionType")
    extended_data: Optional["SponsoredProductsTargetingClauseExtendedData"] = Field(None, alias="extendedData")
    global_target_id: Optional[str] = Field(None, alias="globalTargetId", description="The global target identifier that manages this marketplace target.")
    resolved_expression: list["SponsoredProductsTargetingExpressionPredicate"] = Field(..., alias="resolvedExpression", description="The resolved targeting expression.")
    state: "SponsoredProductsEntityState"
    target_id: str = Field(..., alias="targetId", description="The target identifier")

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetingClauseSuccessResponseItem(BaseModel):
    index: int = Field(..., description="the index of the targetingClause in the array from the request body")
    target_id: Optional[str] = Field(None, alias="targetId", description="the targetingClause ID")
    targeting_clause: Optional["SponsoredProductsTargetingClause"] = Field(None, alias="targetingClause")

    model_config = {'populate_by_name': True}


class SponsoredProductsBulkTargetingClauseOperationResponse(BaseModel):
    error: Optional[list["SponsoredProductsTargetingClauseFailureResponseItem"]] = None
    success: Optional[list["SponsoredProductsTargetingClauseSuccessResponseItem"]] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignAccessErrorSelector(BaseModel):
    date_error: Optional["SponsoredProductsDateError"] = Field(None, alias="dateError")
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    invalid_input_error: Optional["SponsoredProductsInvalidInputError"] = Field(None, alias="invalidInputError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignAccessError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsCampaignAccessErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignAccessExceptionResponseContent(BaseModel):
    """Exception resulting in accessing campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsCampaignAccessError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsCampaignMutationError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeKeywordAccessErrorSelector(BaseModel):
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    invalid_input_error: Optional["SponsoredProductsInvalidInputError"] = Field(None, alias="invalidInputError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeKeywordAccessError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsCampaignNegativeKeywordAccessErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeKeywordAccessExceptionResponseContent(BaseModel):
    """Exception resulting in accessing campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsCampaignNegativeKeywordAccessError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeKeywordMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsCampaignNegativeKeywordMutationError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeTargetsAccessErrorSelector(BaseModel):
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    invalid_input_error: Optional["SponsoredProductsInvalidInputError"] = Field(None, alias="invalidInputError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeTargetsAccessError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsCampaignNegativeTargetsAccessErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeTargetsAccessExceptionResponseContent(BaseModel):
    """Exception resulting in accessing campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsCampaignNegativeTargetsAccessError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsCampaignNegativeTargetsMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsCampaignNegativeTargetsMutationError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateOrUpdateEntityState(StrEnum):
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"
    PROPOSED = "PROPOSED"


class SponsoredProductsCreateAdGroup(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign to which the keyword is associated.")
    default_bid: float = Field(..., alias="defaultBid", description="A bid value for use when no bid is specified for keywords in the ad group. For more information about bid constraints by")
    name: str = Field(..., description="The name of the ad group.")
    state: "SponsoredProductsCreateOrUpdateEntityState"

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateOrUpdateBiddingStrategy(StrEnum):
    AUTO_FOR_SALES = "AUTO_FOR_SALES"
    LEGACY_FOR_SALES = "LEGACY_FOR_SALES"
    MANUAL = "MANUAL"
    RULE_BASED = "RULE_BASED"


class SponsoredProductsCreateOrUpdateDynamicBidding(BaseModel):
    """Specifies bidding controls. DynamicBidding is optional for both Create and Update requests. For Create Campaign requests, if you don't specify dynamicBidding, default strategy of `LEGACY_FOR_SALES` wi"""
    placement_bidding: Optional[list["SponsoredProductsPlacementBidding"]] = Field(None, alias="placementBidding")
    shopper_cohort_bidding: Optional[list["SponsoredProductsShopperCohortBidding"]] = Field(None, alias="shopperCohortBidding", description="Specifies Shopper Cohorts based bid adjustment controls. `shopperCohortBidding` is optional for both Create and Update r")
    strategy: Optional["SponsoredProductsCreateOrUpdateBiddingStrategy"] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateOrUpdateOffAmazonBudgetControlStrategy(StrEnum):
    MAXIMIZE_REACH = "MAXIMIZE_REACH"
    MINIMIZE_SPEND = "MINIMIZE_SPEND"


class SponsoredProductsCreateOrUpdateOffAmazonSettings(BaseModel):
    """Settings that apply to ads served off Amazon. `OffAmazonSettings` is optional for both Create and Update requests. This field is upcoming and is not ready for use."""
    off_amazon_budget_control_strategy: Optional["SponsoredProductsCreateOrUpdateOffAmazonBudgetControlStrategy"] = Field(None, alias="offAmazonBudgetControlStrategy")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateOrUpdateBudgetType(StrEnum):
    DAILY = "DAILY"


class SponsoredProductsCreateOrUpdateBudget(BaseModel):
    budget: float = Field(..., description="Monetary value")
    budget_type: "SponsoredProductsCreateOrUpdateBudgetType" = Field(..., alias="budgetType")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateCampaign(BaseModel):
    auto_manage_campaign: Optional[bool] = Field(None, alias="autoManageCampaign")
    budget: "SponsoredProductsCreateOrUpdateBudget"
    dynamic_bidding: Optional["SponsoredProductsCreateOrUpdateDynamicBidding"] = Field(None, alias="dynamicBidding")
    end_date: Optional[str] = Field(None, alias="endDate", description="The format of the date is YYYY-MM-DD.")
    name: str = Field(..., description="The name of the campaign.")
    off_amazon_settings: Optional["SponsoredProductsCreateOrUpdateOffAmazonSettings"] = Field(None, alias="offAmazonSettings")
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="The identifier of an existing portfolio to which the campaign is associated.")
    site_restrictions: Optional[list["SponsoredProductsSiteRestriction"]] = Field(None, alias="siteRestrictions", description="Restrict the ad to a particular site. siteRestrictions is an optional field. If this field is not set, ads from the camp")
    start_date: Optional[str] = Field(None, alias="startDate", description="Default: today's date. The format of the date is YYYY-MM-DD.")
    state: "SponsoredProductsCreateOrUpdateEntityState"
    tags: Optional["SponsoredProductsTags"] = None
    targeting_type: "SponsoredProductsTargetingType" = Field(..., alias="targetingType")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateOrUpdateNegativeMatchType(StrEnum):
    NEGATIVE_BROAD = "NEGATIVE_BROAD"
    NEGATIVE_EXACT = "NEGATIVE_EXACT"
    NEGATIVE_PHRASE = "NEGATIVE_PHRASE"


class SponsoredProductsCreateCampaignNegativeKeyword(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign to which the keyword is associated.")
    keyword_text: str = Field(..., alias="keywordText", description="The keyword text.")
    match_type: "SponsoredProductsCreateOrUpdateNegativeMatchType" = Field(..., alias="matchType")
    state: "SponsoredProductsCreateOrUpdateEntityState"

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicateType(StrEnum):
    ASIN_BRAND_SAME_AS = "ASIN_BRAND_SAME_AS"
    ASIN_SAME_AS = "ASIN_SAME_AS"


class SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicate(BaseModel):
    type_: "SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicateType" = Field(..., alias="type")
    value: Optional[str] = Field(None, description="The expression value")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateCampaignNegativeTargetingClause(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign to which this target is associated. CampaignNegativeTargetingClauses are only available f")
    expression: list["SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicate"] = Field(..., description="The NegativeTargeting expression.")
    state: "SponsoredProductsCreateOrUpdateEntityState"

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateExpressionType(StrEnum):
    MANUAL = "MANUAL"


class SponsoredProductsCreateOrUpdateMatchType(StrEnum):
    BROAD = "BROAD"
    EXACT = "EXACT"
    PHRASE = "PHRASE"


class SponsoredProductsCreateKeyword(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the ad group to which this keyword is associated.")
    bid: Optional[float] = Field(None, description="Bid associated with this keyword. Applicable to biddable match types only. For more information about bid constraints by")
    campaign_id: str = Field(..., alias="campaignId", description="The identifer of the campaign to which the keyword is associated.")
    keyword_text: str = Field(..., alias="keywordText", description="The keyword text.")
    match_type: "SponsoredProductsCreateOrUpdateMatchType" = Field(..., alias="matchType")
    native_language_keyword: Optional[str] = Field(None, alias="nativeLanguageKeyword", description="The unlocalized keyword text in the preferred locale of the advertiser.")
    native_language_locale: Optional[str] = Field(None, alias="nativeLanguageLocale", description="The locale preference of the advertiser. For example, if the advertiser’s preferred language is Simplified Chinese, set ")
    state: "SponsoredProductsCreateOrUpdateEntityState"

    model_config = {'populate_by_name': True}


class SponsoredProductsKeywordMatchType(StrEnum):
    BROAD = "BROAD"
    EXACT = "EXACT"
    PHRASE = "PHRASE"


class SponsoredProductsCreateKeywordTarget(BaseModel):
    """A keyword target."""
    bid: Optional[float] = Field(None, description="Bid associated with the target. For more information about bid constraints by marketplace, see [bid limits](https://adve")
    keyword: str = Field(..., description="The keyword text.")
    match_type: "SponsoredProductsKeywordMatchType" = Field(..., alias="matchType")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateNegativeKeyword(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the ad group to which this keyword is associated.")
    campaign_id: str = Field(..., alias="campaignId", description="The identifer of the campaign to which the keyword is associated.")
    keyword_text: str = Field(..., alias="keywordText", description="The keyword text.")
    match_type: "SponsoredProductsCreateOrUpdateNegativeMatchType" = Field(..., alias="matchType")
    native_language_keyword: Optional[str] = Field(None, alias="nativeLanguageKeyword", description="The unlocalized keyword text in the preferred locale of the advertiser")
    native_language_locale: Optional[str] = Field(None, alias="nativeLanguageLocale", description="The locale preference of the advertiser.")
    state: "SponsoredProductsCreateOrUpdateEntityState"

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateNegativeTargetingClause(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the ad group to which this target is associated.")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign to which this target is associated.")
    expression: list["SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicate"] = Field(..., description="The NegativeTargeting expression.")
    state: "SponsoredProductsCreateOrUpdateEntityState"

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateProductAd(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The ad group identifier.")
    asin: Optional[str] = Field(None, description="The ASIN associated with the product. Defined for vendors only.")
    campaign_id: str = Field(..., alias="campaignId", description="The campaign identifier.")
    custom_text: Optional[str] = Field(None, alias="customText", description="The custom text to use for creating a custom text ad for the associated ASIN. Defined only for KDP Authors and Book Vend")
    global_store_setting: Optional["SponsoredProductsGlobalStoreSetting"] = Field(None, alias="globalStoreSetting")
    sku: Optional[str] = Field(None, description="The SKU associated with the product. Defined for seller accounts only.")
    state: "SponsoredProductsCreateOrUpdateEntityState"

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetingExpressionMatchType(StrEnum):
    PRODUCT_EXACT = "PRODUCT_EXACT"
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"


class SponsoredProductsCreateProductTarget(BaseModel):
    """A product target."""
    bid: Optional[float] = Field(None, description="Bid associated with the target. For more information about bid constraints by marketplace, see [bid limits](https://adve")
    match_type: "SponsoredProductsTargetingExpressionMatchType" = Field(..., alias="matchType")
    target: str = Field(..., description="The product ASIN of the target.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsAdGroupsRequestContent(BaseModel):
    ad_groups: list["SponsoredProductsCreateAdGroup"] = Field(..., alias="adGroups", description="An array of adGroups.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsAdGroupsResponseContent(BaseModel):
    ad_groups: "SponsoredProductsBulkAdGroupOperationResponse" = Field(..., alias="adGroups")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsCampaignNegativeKeywordsRequestContent(BaseModel):
    campaign_negative_keywords: list["SponsoredProductsCreateCampaignNegativeKeyword"] = Field(..., alias="campaignNegativeKeywords", description="An array of campaignNegativeKeywords.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsCampaignNegativeKeywordsResponseContent(BaseModel):
    campaign_negative_keywords: "SponsoredProductsBulkCampaignNegativeKeywordOperationResponse" = Field(..., alias="campaignNegativeKeywords")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsCampaignNegativeTargetingClausesRequestContent(BaseModel):
    campaign_negative_targeting_clauses: list["SponsoredProductsCreateCampaignNegativeTargetingClause"] = Field(..., alias="campaignNegativeTargetingClauses", description="An array of Campaign Negative TargetingClauses.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsCampaignNegativeTargetingClausesResponseContent(BaseModel):
    campaign_negative_targeting_clauses: "SponsoredProductsBulkCampaignNegativeTargetingClauseOperationResponse" = Field(..., alias="campaignNegativeTargetingClauses")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsCampaignsRequestContent(BaseModel):
    campaigns: list["SponsoredProductsCreateCampaign"] = Field(..., description="An array of campaigns.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsCampaignsResponseContent(BaseModel):
    campaigns: "SponsoredProductsBulkCampaignOperationResponse"

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsKeywordsRequestContent(BaseModel):
    keywords: list["SponsoredProductsCreateKeyword"] = Field(..., description="An array of keywords.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsKeywordsResponseContent(BaseModel):
    keywords: "SponsoredProductsBulkKeywordOperationResponse"

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsNegativeKeywordsRequestContent(BaseModel):
    negative_keywords: list["SponsoredProductsCreateNegativeKeyword"] = Field(..., alias="negativeKeywords", description="An array of negativeKeywords.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsNegativeKeywordsResponseContent(BaseModel):
    negative_keywords: "SponsoredProductsBulkNegativeKeywordOperationResponse" = Field(..., alias="negativeKeywords")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsNegativeTargetingClausesRequestContent(BaseModel):
    negative_targeting_clauses: list["SponsoredProductsCreateNegativeTargetingClause"] = Field(..., alias="negativeTargetingClauses", description="An array of negativeTargeting.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsNegativeTargetingClausesResponseContent(BaseModel):
    negative_targeting_clauses: "SponsoredProductsBulkNegativeTargetingClauseOperationResponse" = Field(..., alias="negativeTargetingClauses")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsProductAdsRequestContent(BaseModel):
    product_ads: list["SponsoredProductsCreateProductAd"] = Field(..., alias="productAds", description="An array of ads.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsProductAdsResponseContent(BaseModel):
    product_ads: "SponsoredProductsBulkProductAdOperationResponse" = Field(..., alias="productAds")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateTargetingExpressionPredicateType(StrEnum):
    ASIN_AGE_RANGE_SAME_AS = "ASIN_AGE_RANGE_SAME_AS"
    ASIN_BRAND_SAME_AS = "ASIN_BRAND_SAME_AS"
    ASIN_CATEGORY_SAME_AS = "ASIN_CATEGORY_SAME_AS"
    ASIN_EXPANDED_FROM = "ASIN_EXPANDED_FROM"
    ASIN_GENRE_SAME_AS = "ASIN_GENRE_SAME_AS"
    ASIN_IS_PRIME_SHIPPING_ELIGIBLE = "ASIN_IS_PRIME_SHIPPING_ELIGIBLE"
    ASIN_PRICE_BETWEEN = "ASIN_PRICE_BETWEEN"
    ASIN_PRICE_GREATER_THAN = "ASIN_PRICE_GREATER_THAN"
    ASIN_PRICE_LESS_THAN = "ASIN_PRICE_LESS_THAN"
    ASIN_REVIEW_RATING_BETWEEN = "ASIN_REVIEW_RATING_BETWEEN"
    ASIN_REVIEW_RATING_GREATER_THAN = "ASIN_REVIEW_RATING_GREATER_THAN"
    ASIN_REVIEW_RATING_LESS_THAN = "ASIN_REVIEW_RATING_LESS_THAN"
    ASIN_SAME_AS = "ASIN_SAME_AS"
    KEYWORD_GROUP_SAME_AS = "KEYWORD_GROUP_SAME_AS"


class SponsoredProductsCreateTargetingExpressionPredicate(BaseModel):
    type_: "SponsoredProductsCreateTargetingExpressionPredicateType" = Field(..., alias="type")
    value: Optional[str] = Field(None, description="The expression value")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateTargetingClause(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the ad group to which this target is associated.")
    bid: Optional[float] = Field(None, description="The bid for ads sourced using the target. Targets that do not have bid values in listTargetingClauses will inherit the d")
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign to which this target is associated.")
    expression: list["SponsoredProductsCreateTargetingExpressionPredicate"] = Field(..., description="The targeting expression.")
    expression_type: "SponsoredProductsCreateExpressionType" = Field(..., alias="expressionType")
    state: "SponsoredProductsCreateOrUpdateEntityState"

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsTargetingClausesRequestContent(BaseModel):
    targeting_clauses: list["SponsoredProductsCreateTargetingClause"] = Field(..., alias="targetingClauses", description="An array of targetingClauses.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateSponsoredProductsTargetingClausesResponseContent(BaseModel):
    targeting_clauses: "SponsoredProductsBulkTargetingClauseOperationResponse" = Field(..., alias="targetingClauses")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateTarget(BaseModel):
    """Target created in the target promotion group."""
    manual_targeting_ad_group_id: Optional[str] = Field(None, alias="manualTargetingAdGroupId", description="The adGroupId of the manual-targeting campaign where the target belongs.")
    target_id: Optional[str] = Field(None, alias="targetId", description="The id of the target that got created.")
    target_promotion_group_id: Optional[str] = Field(None, alias="targetPromotionGroupId", description="The id of the target promotion group.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateTargetErrorSelector(BaseModel):
    pass


class SponsoredProductsCreateTargetError(BaseModel):
    """Response object of failed target promotion group target."""
    error_type: Optional[str] = Field(None, alias="errorType", description="The type of the error.")
    error_value: Optional["SponsoredProductsCreateTargetErrorSelector"] = Field(None, alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsError(BaseModel):
    error_code: Optional[str] = Field(None, alias="errorCode")
    error_message: Optional[str] = Field(None, alias="errorMessage")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateTargetPromotionGroupTargetsBatchError(BaseModel):
    """Response object of failed target promotion group target."""
    index: Optional[str] = Field(None, description="index of the item in the request.")
    sub_errors: Optional[list["SponsoredProductsError"]] = Field(None, alias="subErrors", description="A list of the errors encountered.")

    model_config = {'populate_by_name': True}


class SponsoredProductsProductTargetV2(BaseModel):
    """A product target."""
    destination_ad_group_id: Optional[str] = Field(None, alias="destinationAdGroupId", description="The adGroupId of the destination manual-targeting adGroup where the target belongs.")
    expression_type: Optional[str] = Field(None, alias="expressionType", description="The the expression type (for PRODUCT). One of PRODUCT_EXACT, PRODUCT_SIMILAR")
    target: Optional[str] = Field(None, description="The product ASIN of the target.")
    target_id: Optional[str] = Field(None, alias="targetId", description="The id of the product target.")
    target_promotion_group_id: Optional[str] = Field(None, alias="targetPromotionGroupId", description="The id of the target promotion group.")

    model_config = {'populate_by_name': True}


class SponsoredProductsKeywordTargetV2(BaseModel):
    """A keyword target."""
    destination_ad_group_id: Optional[str] = Field(None, alias="destinationAdGroupId", description="The adGroupId of the destination manual-targeting adGroup where the target belongs.")
    keyword_id: Optional[str] = Field(None, alias="keywordId", description="The id of the keyword target.")
    keyword_text: Optional[str] = Field(None, alias="keywordText", description="The keyword text.")
    match_type: Optional[str] = Field(None, alias="matchType", description="The match type (for KEYWORDs). One of EXACT, PHRASE, BROAD")
    target_promotion_group_id: Optional[str] = Field(None, alias="targetPromotionGroupId", description="The id of the target promotion group.")

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetPromotionGroupTargetDetails(BaseModel):
    pass


class SponsoredProductsCreateTargetPromotionGroupTargetsBatchSuccess(BaseModel):
    """Response object of successfully created target promotion group target."""
    index: Optional[str] = Field(None, description="index of the item in the request.")
    target_details: Optional["SponsoredProductsTargetPromotionGroupTargetDetails"] = Field(None, alias="targetDetails")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateTargetPromotionGroupTargetsFailureResponseItem(BaseModel):
    """Response object of failed target promotion group target."""
    errors: Optional[list["SponsoredProductsCreateTargetError"]] = Field(None, description="Response object of failed target promotion group target.")
    expression_type: Optional[str] = Field(None, alias="expressionType", description="The expression type of the target that was requested to be created.")
    target: Optional[str] = Field(None, description="The target that was requested to be created.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateTargetRequest(BaseModel):
    """Request object for the target promotion group's target."""
    bid: Optional[float] = Field(None, description="Bid associated with the target. For more information about bid constraints by marketplace, see [bid limits](https://adve")
    expression_type: str = Field(..., alias="expressionType", description="The match type (for KEYWORDs) or the expression type (for PRODUCT). One of QUERY_BROAD_MATCHES,     QUERY_EXACT_MATCHES,")
    target: str = Field(..., description="The keyword or the product ASIN to be targeted.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateTargetPromotionGroupTargetsRequestContent(BaseModel):
    """Request object for creating target promotion group targets in a target promotion group."""
    target_promotion_group_id: str = Field(..., alias="targetPromotionGroupId", description="The id of the target promotion group where the targets are being added.")
    targets: Optional[list["SponsoredProductsCreateTargetRequest"]] = Field(None, description="List of targets to be added to the target promotion group.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateTargetPromotionGroupTargetsSuccessResponseItem(BaseModel):
    """Response object of successfully created target promotion group target."""
    expression_type: Optional[str] = Field(None, alias="expressionType", description="The expression type of the target that was requested to be created.")
    target: Optional[str] = Field(None, description="The target that was requested to be created.")
    target_details: Optional["SponsoredProductsCreateTarget"] = Field(None, alias="targetDetails")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateTargetPromotionGroupTargetsResponseContent(BaseModel):
    """Response object for creating target promotion group targets."""
    errors: Optional[list["SponsoredProductsCreateTargetPromotionGroupTargetsFailureResponseItem"]] = Field(None, description="List of targets that failed to create.")
    success: Optional[list["SponsoredProductsCreateTargetPromotionGroupTargetsSuccessResponseItem"]] = Field(None, description="List of successfully created targets.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateTargetRequestV2(BaseModel):
    """Request object for target promotion group's target."""
    pass


class SponsoredProductsCreateTargetPromotionGroupTargetsV2RequestContent(BaseModel):
    """Request object for creating target promotion group targets in a target promotion group."""
    target_promotion_group_id: str = Field(..., alias="targetPromotionGroupId", description="The id of the target promotion group where the targets are being added.")
    targets: Optional[list["SponsoredProductsCreateTargetRequestV2"]] = Field(None, description="List of targets to be added to the target promotion group.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateTargetPromotionGroupTargetsV2ResponseContent(BaseModel):
    """Response object for creating target promotion group targets."""
    error: Optional[list["SponsoredProductsCreateTargetPromotionGroupTargetsBatchError"]] = None
    success: Optional[list["SponsoredProductsCreateTargetPromotionGroupTargetsBatchSuccess"]] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsExistingCampaignDetails(BaseModel):
    """The request object for creating a new target promotion group with existing campaigns. Please note that the adGroupIds provided need to contain the same Ad ASINs/SKUs combination as the Auto-Targeting """
    keyword_campaign_ad_group_ids: Optional[list[str]] = Field(None, alias="keywordCampaignAdGroupIds", description="AdGroupIds of existing manual campaigns to be used as part of the Target Promotion Group for     promoting keyword targe")
    product_campaign_ad_group_ids: Optional[list[str]] = Field(None, alias="productCampaignAdGroupIds", description="AdGroupIds of existing manual campaigns to be used as part of the Target Promotion Group for     promoting product targe")

    model_config = {'populate_by_name': True}


class SponsoredProductsNewCampaignBudget(BaseModel):
    """The budget for the campaigns in the target promotion group."""
    budget: float = Field(..., description="The value of the budget.")
    budget_type: str = Field(..., alias="budgetType", description="DAILY.")

    model_config = {'populate_by_name': True}


class SponsoredProductsNewCampaignPlacementBidding(BaseModel):
    """The product placement."""
    percentage: int = Field(..., description="The bidding placement percentage.")
    placement: str = Field(..., description="The bidding placement. One of PLACEMENT_TOP, PLACEMENT_PRODUCT_PAGE, PLACEMENT_REST_OF_SEARCH.")

    model_config = {'populate_by_name': True}


class SponsoredProductsNewCampaignDynamicBidding(BaseModel):
    """Specifies bidding controls."""
    placement_bidding: Optional[list["SponsoredProductsNewCampaignPlacementBidding"]] = Field(None, alias="placementBidding", description="The product placement.")
    strategy: str = Field(..., description="One of LEGACY_FOR_SALES, AUTO_FOR_SALES, MANUAL, RULE_BASED.")

    model_config = {'populate_by_name': True}


class SponsoredProductsNewCampaignDetails(BaseModel):
    """The request object for creating a new target promotion group with new campaigns."""
    budget: "SponsoredProductsNewCampaignBudget"
    default_bid: float = Field(..., alias="defaultBid", description="The default bid value that gets applied if no bid is provided for the target. For more information about bid constraints")
    dynamic_bidding: Optional["SponsoredProductsNewCampaignDynamicBidding"] = Field(None, alias="dynamicBidding")
    end_date: Optional[str] = Field(None, alias="endDate", description="The end date of the new target promotion group entities. The format of the date is YYYY-MM-DD.")
    name_prefix: str = Field(..., alias="namePrefix", description="The name prefix to be used for the entities under the target promotion group. e.g. if the namePrefix     is ABC, we will")
    start_date: Optional[str] = Field(None, alias="startDate", description="The start date of the new target promotion group entities. Default is today's date. The format of the date is YYYY-MM-DD")
    tags: Optional["SponsoredProductsTags"] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateTargetPromotionGroupsRequestContent(BaseModel):
    """Request object for creating a Target Promotion Group."""
    ad_group_id: str = Field(..., alias="adGroupId", description="The adGroupId of the Ad Group of an Auto-Targeting campaign that will be part of the Target Promotion Group.")
    ad_ids: Optional[list[str]] = Field(None, alias="adIds", description="The list of adIds (optional) of the Ad Group of the Auto-Targeting campaign, that will be part of the Target Promotion G")
    existing_campaign_details: Optional["SponsoredProductsExistingCampaignDetails"] = Field(None, alias="existingCampaignDetails")
    new_campaign_details: Optional["SponsoredProductsNewCampaignDetails"] = Field(None, alias="newCampaignDetails")

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetPromotionGroup(BaseModel):
    """A Target Promotion Group that groups an Auto-Targeting Campaign/AdGroup with a Manual-Targeting Keyword Campaign/AdGroup, and a Manual-Targeting Product Campaign/AdGroup"""
    auto_targeting_campaign_ad_group_id: Optional[str] = Field(None, alias="autoTargetingCampaignAdGroupId", description="The Id of the auto-targeting AdGroup associated with the target promotion group")
    auto_targeting_campaign_ad_ids: Optional[list[str]] = Field(None, alias="autoTargetingCampaignAdIds", description="The list of Product Ad Ids in the Auto-Targeting campaign's Ad Group that's tied to the Target Promotion Group.")
    keyword_campaign_ad_group_ids: Optional[list[str]] = Field(None, alias="keywordCampaignAdGroupIds", description="The Ids of the manual keyword-targeting AdGroups associated with the target promotion group")
    product_campaign_ad_group_ids: Optional[list[str]] = Field(None, alias="productCampaignAdGroupIds", description="The Ids of the manual product-targeting AdGroups associated with the target promotion group")
    state: Optional[str] = Field(None, description="The state of the target promotion group.")
    target_promotion_group_id: Optional[str] = Field(None, alias="targetPromotionGroupId", description="The id of the target promotion group.")
    target_promotion_group_name: Optional[str] = Field(None, alias="targetPromotionGroupName", description="The name of the target promotion group.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateTargetPromotionGroupsResponseContent(BaseModel):
    """Response object for creating a target promotion group."""
    target_promotion_group: Optional["SponsoredProductsTargetPromotionGroup"] = Field(None, alias="targetPromotionGroup")

    model_config = {'populate_by_name': True}


class SponsoredProductsExistingAdGroup(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The id of the Ad Group.")

    model_config = {'populate_by_name': True}


class SponsoredProductsNewAdGroup(BaseModel):
    ad_group_name: str = Field(..., alias="adGroupName", description="The name of the new ad group.")
    default_bid: float = Field(..., alias="defaultBid", description="The default bid value that gets applied if no bid is provided for the target. For more information about bid constraints")
    targeting_types: list[str] = Field(..., alias="targetingTypes", description="List of targeting types to be used for targets in the ad group. Supported types are KEYWORD and PRODUCT.")

    model_config = {'populate_by_name': True}


class SponsoredProductsNewCampaign(BaseModel):
    ad_groups: list["SponsoredProductsNewAdGroup"] = Field(..., alias="adGroups", description="List of ad groups to be created inside the new campaign.")
    budget: "SponsoredProductsNewCampaignBudget"
    campaign_name: str = Field(..., alias="campaignName", description="The campaign name.")
    dynamic_bidding: Optional["SponsoredProductsNewCampaignDynamicBidding"] = Field(None, alias="dynamicBidding")
    end_date: Optional[str] = Field(None, alias="endDate", description="The end date of the new target promotion group entities. The format of the date is YYYY-MM-DD.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The start date of the new target promotion group entities. Default is today's date. The format of the date is YYYY-MM-DD")
    tags: Optional["SponsoredProductsTags"] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateTargetPromotionGroupsV2RequestContent(BaseModel):
    """Request object for creating a Target Promotion Group."""
    ad_group_id: str = Field(..., alias="adGroupId", description="The adGroupId of the source Ad Group that will be part of the Target Promotion Group.")
    ad_ids: Optional[list[str]] = Field(None, alias="adIds", description="The list of adIds (optional) of the source Ad Group, that will be part of the Target Promotion Group. If this     list i")
    existing_campaign_details: Optional[list["SponsoredProductsExistingAdGroup"]] = Field(None, alias="existingCampaignDetails", description="List of existing manual campaign ad groups to be added in the Target Promotion Group. It must contain one keyword ad gro")
    new_campaign_details: Optional[list["SponsoredProductsNewCampaign"]] = Field(None, alias="newCampaignDetails", description="List of new destination manual campaigns to be created as part of the Target Promotion Group. It must contain setting fo")
    target_promotion_group_name: str = Field(..., alias="targetPromotionGroupName", description="The name of the target promotion group that will be created.")

    model_config = {'populate_by_name': True}


class SponsoredProductsResponseAdGroup(BaseModel):
    """Ad groups where targets can be promoted."""
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="The id of the ad group in the campaign.")

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetPromotionGroupV2(BaseModel):
    """A Target Promotion Group that groups a source AdGroup with one or more destination Manual Keyword/Product Targeting AdGroup(s)"""
    ad_ids: Optional[list[str]] = Field(None, alias="adIds", description="The list of Product Ad Ids in the source Ad Group that's tied to the Target Promotion Group.")
    destination_ad_groups: Optional[list["SponsoredProductsResponseAdGroup"]] = Field(None, alias="destinationAdGroups", description="The destination manual targeting AdGroups associated with the target promotion group.")
    source_ad_group_id: Optional[str] = Field(None, alias="sourceAdGroupId", description="The Id of the source AdGroup associated with the target promotion group")
    source_campaign_id: Optional[str] = Field(None, alias="sourceCampaignId", description="The campaign Id of the source AdGroup associated with the target promotion group")
    state: Optional[str] = Field(None, description="The state of the target promotion group.")
    target_promotion_group_id: Optional[str] = Field(None, alias="targetPromotionGroupId", description="The id of the target promotion group.")
    target_promotion_group_name: Optional[str] = Field(None, alias="targetPromotionGroupName", description="The name of the target promotion group.")

    model_config = {'populate_by_name': True}


class SponsoredProductsCreateTargetPromotionGroupsV2ResponseContent(BaseModel):
    """Response object for creating a target promotion group."""
    target_promotion_group: Optional["SponsoredProductsTargetPromotionGroupV2"] = Field(None, alias="targetPromotionGroup")

    model_config = {'populate_by_name': True}


class SponsoredProductsObjectIdFilter(BaseModel):
    """Filter entities by the list of objectIds"""
    include: list[str]

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsAdGroupsRequestContent(BaseModel):
    ad_group_id_filter: "SponsoredProductsObjectIdFilter" = Field(..., alias="adGroupIdFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsAdGroupsResponseContent(BaseModel):
    ad_groups: "SponsoredProductsBulkAdGroupOperationResponse" = Field(..., alias="adGroups")

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsCampaignNegativeKeywordsRequestContent(BaseModel):
    campaign_negative_keyword_id_filter: "SponsoredProductsObjectIdFilter" = Field(..., alias="campaignNegativeKeywordIdFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsCampaignNegativeKeywordsResponseContent(BaseModel):
    campaign_negative_keywords: "SponsoredProductsBulkCampaignNegativeKeywordOperationResponse" = Field(..., alias="campaignNegativeKeywords")

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsCampaignNegativeTargetingClausesRequestContent(BaseModel):
    campaign_negative_target_id_filter: "SponsoredProductsObjectIdFilter" = Field(..., alias="campaignNegativeTargetIdFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsCampaignNegativeTargetingClausesResponseContent(BaseModel):
    campaign_negative_targeting_clauses: "SponsoredProductsBulkCampaignNegativeTargetingClauseOperationResponse" = Field(..., alias="campaignNegativeTargetingClauses")

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsCampaignsRequestContent(BaseModel):
    campaign_id_filter: "SponsoredProductsObjectIdFilter" = Field(..., alias="campaignIdFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsCampaignsResponseContent(BaseModel):
    campaigns: "SponsoredProductsBulkCampaignOperationResponse"

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsKeywordsRequestContent(BaseModel):
    keyword_id_filter: "SponsoredProductsObjectIdFilter" = Field(..., alias="keywordIdFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsKeywordsResponseContent(BaseModel):
    keywords: "SponsoredProductsBulkKeywordOperationResponse"

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsNegativeKeywordsRequestContent(BaseModel):
    negative_keyword_id_filter: "SponsoredProductsObjectIdFilter" = Field(..., alias="negativeKeywordIdFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsNegativeKeywordsResponseContent(BaseModel):
    negative_keywords: "SponsoredProductsBulkNegativeKeywordOperationResponse" = Field(..., alias="negativeKeywords")

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsNegativeTargetingClausesRequestContent(BaseModel):
    negative_target_id_filter: "SponsoredProductsObjectIdFilter" = Field(..., alias="negativeTargetIdFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsNegativeTargetingClausesResponseContent(BaseModel):
    negative_targeting_clauses: "SponsoredProductsBulkNegativeTargetingClauseOperationResponse" = Field(..., alias="negativeTargetingClauses")

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsProductAdsRequestContent(BaseModel):
    ad_id_filter: "SponsoredProductsObjectIdFilter" = Field(..., alias="adIdFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsProductAdsResponseContent(BaseModel):
    product_ads: "SponsoredProductsBulkProductAdOperationResponse" = Field(..., alias="productAds")

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsTargetingClausesRequestContent(BaseModel):
    target_id_filter: "SponsoredProductsObjectIdFilter" = Field(..., alias="targetIdFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsDeleteSponsoredProductsTargetingClausesResponseContent(BaseModel):
    targeting_clauses: "SponsoredProductsBulkTargetingClauseOperationResponse" = Field(..., alias="targetingClauses")

    model_config = {'populate_by_name': True}


class SponsoredProductsEntityStateFilter(BaseModel):
    """Filter entities by state. To filter live entities, only 'ENABLED', 'PAUSED' and 'ARCHIVED' can be used"""
    include: list["SponsoredProductsEntityState"]

    model_config = {'populate_by_name': True}


class SponsoredProductsExpressionTypeFilter(BaseModel):
    """Filter entities by ExpressionType"""
    include: list["SponsoredProductsExpressionType"]

    model_config = {'populate_by_name': True}


class SponsoredProductsExpressionTypeWithoutOther(StrEnum):
    AUTO = "AUTO"
    MANUAL = "MANUAL"


class SponsoredProductsGetTargetPromotionGroupsRecommendationsRequestContent(BaseModel):
    ad_group_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    ad_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="adIdFilter")
    campaign_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to 1000.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token for fetching the next page")

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetType(StrEnum):
    ASIN = "ASIN"
    KEYWORD = "KEYWORD"


class SponsoredProductsRecommendationReason(BaseModel):
    """Provides a reason for why this target is being recommended for harvesting"""
    data: Optional[str] = Field(None, description="The data supporting the recommendation reason")
    reason: Optional[str] = Field(None, description="The reason for the recommendation")

    model_config = {'populate_by_name': True}


class SponsoredProductsRecommendedTarget(BaseModel):
    ad_asin: Optional[str] = Field(None, alias="adAsin", description="The ASIN of the product being advertised")
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="The ID of an ad group for which the targets are recommended")
    ad_id: Optional[str] = Field(None, alias="adId", description="The ID of an ad for which the targets are recommended")
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="The ID of a campaign for which the targets are recommended")
    recommendation_reasons: Optional[list["SponsoredProductsRecommendationReason"]] = Field(None, alias="recommendationReasons", description="Provides a list of reasons for why this target is being recommended for harvesting")
    recommended_target: Optional[str] = Field(None, alias="recommendedTarget", description="The keyword or ASIN that is being targeted")
    target_type: Optional["SponsoredProductsTargetType"] = Field(None, alias="targetType")

    model_config = {'populate_by_name': True}


class SponsoredProductsGetTargetPromotionGroupsRecommendationsResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token for fetching the next page")
    targets: list["SponsoredProductsRecommendedTarget"] = Field(..., description="List of optimized targets for the request, as recommended by Amazon heuristics")
    total_results: int = Field(..., alias="totalResults", description="Total number of records available")

    model_config = {'populate_by_name': True}


class SponsoredProductsInternalErrorErrorCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class SponsoredProductsInternalServerErrorCode(StrEnum):
    INTERNAL_SERVER_EXCEPTION = "INTERNAL_SERVER_EXCEPTION"


class SponsoredProductsInternalServerExceptionCode(StrEnum):
    INTERNAL_SERVER_EXCEPTION = "INTERNAL_SERVER_EXCEPTION"


class SponsoredProductsInternalServerExceptionResponseContent(BaseModel):
    code: "SponsoredProductsInternalErrorErrorCode"
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsKeywordAccessErrorSelector(BaseModel):
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    invalid_input_error: Optional["SponsoredProductsInvalidInputError"] = Field(None, alias="invalidInputError")
    locale_error: Optional["SponsoredProductsLocaleError"] = Field(None, alias="localeError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class SponsoredProductsKeywordAccessError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsKeywordAccessErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsKeywordAccessExceptionResponseContent(BaseModel):
    """Exception resulting in accessing campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsKeywordAccessError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsKeywordMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsKeywordMutationError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsKeywordTextFilter(BaseModel):
    """Filter by keywordText"""
    include: Optional[list[str]] = None
    query_term_match_type: "SponsoredProductsQueryTermMatchType" = Field(..., alias="queryTermMatchType")

    model_config = {'populate_by_name': True}


class SponsoredProductsReducedObjectIdFilter(BaseModel):
    """Filter entities by the list of objectIds"""
    include: list[str]

    model_config = {'populate_by_name': True}


class SponsoredProductsNameFilter(BaseModel):
    """Filter entities by name"""
    include: Optional[list[str]] = None
    query_term_match_type: Optional["SponsoredProductsQueryTermMatchType"] = Field(None, alias="queryTermMatchType")

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsAdGroupsRequestContent(BaseModel):
    ad_group_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    campaign_id_filter: Optional["SponsoredProductsReducedObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    campaign_targeting_type_filter: Optional["SponsoredProductsTargetingType"] = Field(None, alias="campaignTargetingTypeFilter")
    include_extended_data_fields: Optional[bool] = Field(None, alias="includeExtendedDataFields", description="Whether to get entity with extended data fields such as creationDate, lastUpdateDate, servingStatus")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API")
    name_filter: Optional["SponsoredProductsNameFilter"] = Field(None, alias="nameFilter")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    state_filter: Optional["SponsoredProductsEntityStateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsAdGroupsResponseContent(BaseModel):
    ad_groups: Optional[list["SponsoredProductsAdGroup"]] = Field(None, alias="adGroups")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of entities")

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsCampaignNegativeKeywordsRequestContent(BaseModel):
    campaign_id_filter: Optional["SponsoredProductsReducedObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    campaign_negative_keyword_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="campaignNegativeKeywordIdFilter")
    campaign_negative_keyword_text_filter: Optional["SponsoredProductsKeywordTextFilter"] = Field(None, alias="campaignNegativeKeywordTextFilter")
    include_extended_data_fields: Optional[bool] = Field(None, alias="includeExtendedDataFields", description="Whether to get entity with extended data fields such as creationDate, lastUpdateDate, servingStatus")
    match_type_filter: Optional[list["SponsoredProductsNegativeMatchType"]] = Field(None, alias="matchTypeFilter", description="Restricts results to resources with the selected matchType")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    state_filter: Optional["SponsoredProductsEntityStateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsCampaignNegativeKeywordsResponseContent(BaseModel):
    campaign_negative_keywords: Optional[list["SponsoredProductsCampaignNegativeKeyword"]] = Field(None, alias="campaignNegativeKeywords")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of entities")

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsCampaignNegativeTargetingClausesRequestContent(BaseModel):
    asin_filter: Optional["SponsoredProductsAsinFilter"] = Field(None, alias="asinFilter")
    campaign_id_filter: Optional["SponsoredProductsReducedObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    campaign_negative_target_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="campaignNegativeTargetIdFilter")
    include_extended_data_fields: Optional[bool] = Field(None, alias="includeExtendedDataFields", description="Whether to get entity with extended data fields such as creationDate, lastUpdateDate, servingStatus")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    state_filter: Optional["SponsoredProductsEntityStateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsCampaignNegativeTargetingClausesResponseContent(BaseModel):
    campaign_negative_targeting_clauses: Optional[list["SponsoredProductsCampaignNegativeTargetingClause"]] = Field(None, alias="campaignNegativeTargetingClauses")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of entities")

    model_config = {'populate_by_name': True}


class SponsoredProductsMarketplaceBudgetAllocationFilter(BaseModel):
    """Filter campaigns by MarketplaceBudgetAllocation setting. By default, only MANUAL campaigns are returned. This filter is not functional yet, will be functional soon."""
    include: list["SponsoredProductsMarketplaceBudgetAllocation"]

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsCampaignsRequestContent(BaseModel):
    campaign_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    include_extended_data_fields: Optional[bool] = Field(None, alias="includeExtendedDataFields", description="Whether to get entity with extended data fields such as creationDate, lastUpdateDate, servingStatus")
    marketplace_budget_allocation_filter: Optional["SponsoredProductsMarketplaceBudgetAllocationFilter"] = Field(None, alias="marketplaceBudgetAllocationFilter")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API")
    name_filter: Optional["SponsoredProductsNameFilter"] = Field(None, alias="nameFilter")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    portfolio_id_filter: Optional["SponsoredProductsReducedObjectIdFilter"] = Field(None, alias="portfolioIdFilter")
    state_filter: Optional["SponsoredProductsEntityStateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsCampaignsResponseContent(BaseModel):
    campaigns: Optional[list["SponsoredProductsCampaign"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of entities")

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsKeywordsRequestContent(BaseModel):
    ad_group_id_filter: Optional["SponsoredProductsReducedObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    campaign_id_filter: Optional["SponsoredProductsReducedObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    include_extended_data_fields: Optional[bool] = Field(None, alias="includeExtendedDataFields", description="Whether to get entity with extended data fields such as creationDate, lastUpdateDate, servingStatus")
    keyword_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="keywordIdFilter")
    keyword_text_filter: Optional["SponsoredProductsKeywordTextFilter"] = Field(None, alias="keywordTextFilter")
    locale: Optional[str] = Field(None, description="Restricts results to keywords associated with locale")
    match_type_filter: Optional[list["SponsoredProductsMatchType"]] = Field(None, alias="matchTypeFilter", description="Only the keyword with match type that is in this list will be listed")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    state_filter: Optional["SponsoredProductsEntityStateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsKeywordsResponseContent(BaseModel):
    keywords: Optional[list["SponsoredProductsKeyword"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of entities")

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsNegativeKeywordsRequestContent(BaseModel):
    ad_group_id_filter: Optional["SponsoredProductsReducedObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    campaign_id_filter: Optional["SponsoredProductsReducedObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    include_extended_data_fields: Optional[bool] = Field(None, alias="includeExtendedDataFields", description="Whether to get entity with extended data fields such as creationDate, lastUpdateDate, servingStatus")
    locale: Optional[str] = Field(None, description="Restricts results to negativeKeywords that match the specified locale.")
    match_type_filter: Optional[list["SponsoredProductsNegativeMatchType"]] = Field(None, alias="matchTypeFilter", description="Only the negativeKeyword with the match type that is in this list will be listed")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API")
    negative_keyword_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="negativeKeywordIdFilter")
    negative_keyword_text_filter: Optional["SponsoredProductsKeywordTextFilter"] = Field(None, alias="negativeKeywordTextFilter")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    state_filter: Optional["SponsoredProductsEntityStateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsNegativeKeywordsResponseContent(BaseModel):
    negative_keywords: Optional[list["SponsoredProductsNegativeKeyword"]] = Field(None, alias="negativeKeywords")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of entities")

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsNegativeTargetingClausesRequestContent(BaseModel):
    ad_group_id_filter: Optional["SponsoredProductsReducedObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    asin_filter: Optional["SponsoredProductsAsinFilter"] = Field(None, alias="asinFilter")
    campaign_id_filter: Optional["SponsoredProductsReducedObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    include_extended_data_fields: Optional[bool] = Field(None, alias="includeExtendedDataFields", description="Whether to get entity with extended data fields such as creationDate, lastUpdateDate, servingStatus")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API")
    negative_target_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="negativeTargetIdFilter")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    state_filter: Optional["SponsoredProductsEntityStateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsNegativeTargetingClausesResponseContent(BaseModel):
    negative_targeting_clauses: Optional[list["SponsoredProductsNegativeTargetingClause"]] = Field(None, alias="negativeTargetingClauses")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of entities")

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsProductAdsRequestContent(BaseModel):
    ad_group_id_filter: Optional["SponsoredProductsReducedObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    ad_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="adIdFilter")
    campaign_id_filter: Optional["SponsoredProductsReducedObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    include_extended_data_fields: Optional[bool] = Field(None, alias="includeExtendedDataFields", description="Whether to get entity with extended data fields such as creationDate, lastUpdateDate, servingStatus")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    state_filter: Optional["SponsoredProductsEntityStateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsProductAdsResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    product_ads: Optional[list["SponsoredProductsProductAd"]] = Field(None, alias="productAds")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of entities")

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsTargetingClausesRequestContent(BaseModel):
    ad_group_id_filter: Optional["SponsoredProductsReducedObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    asin_filter: Optional["SponsoredProductsAsinFilter"] = Field(None, alias="asinFilter")
    campaign_id_filter: Optional["SponsoredProductsReducedObjectIdFilter"] = Field(None, alias="campaignIdFilter")
    expression_type_filter: Optional["SponsoredProductsExpressionTypeFilter"] = Field(None, alias="expressionTypeFilter")
    include_extended_data_fields: Optional[bool] = Field(None, alias="includeExtendedDataFields", description="Whether to get entity with extended data fields such as creationDate, lastUpdateDate, servingStatus")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Number of records to include in the paginated response. Defaults to max page size for given API")
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    state_filter: Optional["SponsoredProductsEntityStateFilter"] = Field(None, alias="stateFilter")
    target_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="targetIdFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsListSponsoredProductsTargetingClausesResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    targeting_clauses: Optional[list["SponsoredProductsTargetingClause"]] = Field(None, alias="targetingClauses")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of entities")

    model_config = {'populate_by_name': True}


class SponsoredProductsListTargetPromotionGroupTargetsRequestContent(BaseModel):
    """Request object for querying target promotion group targets."""
    ad_group_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults", description="The maximum number of results requested.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next or previous response page")
    target_promotion_group_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="targetPromotionGroupIdFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsTarget(BaseModel):
    """Target promotion group's target."""
    expression_type: Optional[str] = Field(None, alias="expressionType", description="The match type (for KEYWORDs) or the expression type (for PRODUCT). One of QUERY_BROAD_MATCHES,     QUERY_EXACT_MATCHES,")
    manual_targeting_ad_group_id: Optional[str] = Field(None, alias="manualTargetingAdGroupId", description="The adGroupId of the manual-targeting campaign where the target belongs.")
    target: Optional[str] = Field(None, description="The keyword text or the product ASIN of the target.")
    target_id: Optional[str] = Field(None, alias="targetId", description="The id of the target.")
    target_promotion_group_id: Optional[str] = Field(None, alias="targetPromotionGroupId", description="The id of the target promotion group.")

    model_config = {'populate_by_name': True}


class SponsoredProductsListTargetPromotionGroupTargetsResponseContent(BaseModel):
    """Response object for querying target promotion group targets."""
    next_token: Optional[str] = Field(None, alias="nextToken", description="To retrieve the next page of results, call the same operation and specify this token in the     request. If the nextToke")
    targets: Optional[list["SponsoredProductsTarget"]] = None
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of results available.")

    model_config = {'populate_by_name': True}


class SponsoredProductsListTargetPromotionGroupTargetsV2RequestContent(BaseModel):
    """Request object for querying target promotion group targets."""
    ad_group_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults", description="The maximum number of results requested.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next or previous response page")
    target_promotion_group_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="targetPromotionGroupIdFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsListTargetPromotionGroupTargetsV2ResponseContent(BaseModel):
    """Response object for querying target promotion group targets."""
    next_token: Optional[str] = Field(None, alias="nextToken", description="To retrieve the next page of results, call the same operation and specify this token in the     request. If the nextToke")
    targets: Optional[list["SponsoredProductsTargetPromotionGroupTargetDetails"]] = None
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of results available.")

    model_config = {'populate_by_name': True}


class SponsoredProductsListTargetPromotionGroupsRequestContent(BaseModel):
    """Request object for querying target promotion groups."""
    ad_group_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="adGroupIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults", description="The maximum number of results requested.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next or previous response page")
    target_promotion_group_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="targetPromotionGroupIdFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsListTargetPromotionGroupsResponseContent(BaseModel):
    """Response object for querying target promotion groups."""
    next_token: Optional[str] = Field(None, alias="nextToken", description="To retrieve the next page of results, call the same operation and specify this token in the     request. If the nextToke")
    target_promotion_groups: Optional[list["SponsoredProductsTargetPromotionGroup"]] = Field(None, alias="targetPromotionGroups")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of results available.")

    model_config = {'populate_by_name': True}


class SponsoredProductsListTargetPromotionGroupsV2RequestContent(BaseModel):
    """Request object for querying target promotion groups."""
    destination_ad_group_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="destinationAdGroupIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults", description="The maximum number of results requested.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token value allowing to navigate to the next or previous response page")
    source_ad_group_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="sourceAdGroupIdFilter")
    target_promotion_group_id_filter: Optional["SponsoredProductsObjectIdFilter"] = Field(None, alias="targetPromotionGroupIdFilter")

    model_config = {'populate_by_name': True}


class SponsoredProductsListTargetPromotionGroupsV2ResponseContent(BaseModel):
    """Response object for querying target promotion groups."""
    next_token: Optional[str] = Field(None, alias="nextToken", description="To retrieve the next page of results, call the same operation and specify this token in the     request. If the nextToke")
    target_promotion_groups: Optional[list["SponsoredProductsTargetPromotionGroupV2"]] = Field(None, alias="targetPromotionGroups")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of results available.")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeKeywordAccessErrorSelector(BaseModel):
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    invalid_input_error: Optional["SponsoredProductsInvalidInputError"] = Field(None, alias="invalidInputError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeKeywordAccessError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsNegativeKeywordAccessErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeKeywordAccessExceptionResponseContent(BaseModel):
    """Exception resulting in accessing campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsNegativeKeywordAccessError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeKeywordMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsNegativeKeywordMutationError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeTargetAccessErrorSelector(BaseModel):
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    invalid_input_error: Optional["SponsoredProductsInvalidInputError"] = Field(None, alias="invalidInputError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeTargetAccessError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsNegativeTargetAccessErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeTargetAccessExceptionResponseContent(BaseModel):
    """Exception resulting in accessing campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsNegativeTargetAccessError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsNegativeTargetMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsNegativeTargetMutationError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsNotImplementedExceptionCode(StrEnum):
    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"


class SponsoredProductsNotImplementedExceptionResponseContent(BaseModel):
    """Operation is not implemented."""
    code: Optional["SponsoredProductsNotImplementedExceptionCode"] = None
    message: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SponsoredProductsProductAdAccessErrorSelector(BaseModel):
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    invalid_input_error: Optional["SponsoredProductsInvalidInputError"] = Field(None, alias="invalidInputError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class SponsoredProductsProductAdAccessError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsProductAdAccessErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsProductAdAccessExceptionResponseContent(BaseModel):
    """Exception resulting in accessing campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsProductAdAccessError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsProductAdMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsProductAdMutationError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsSchemaValidationExceptionCode(StrEnum):
    INVALID_SCHEMA = "INVALID_SCHEMA"


class SponsoredProductsSchemaValidationExceptionResponseContent(BaseModel):
    """Request failed schema validation."""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    message: str = Field(..., description="Human-readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsServiceUnavailableExceptionCode(StrEnum):
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"


class SponsoredProductsServiceUnavailableExceptionErrorCode(StrEnum):
    SERVICE_UNAVAILABLE_EXCEPTION = "SERVICE_UNAVAILABLE_EXCEPTION"


class SponsoredProductsServiceUnavailableExceptionResponseContent(BaseModel):
    """Server unable to process request. Please retry later."""
    code: "SponsoredProductsServiceUnavailableExceptionErrorCode"
    message: str

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetAccessErrorSelector(BaseModel):
    entity_not_found_error: Optional["SponsoredProductsEntityNotFoundError"] = Field(None, alias="entityNotFoundError")
    internal_server_error: Optional["SponsoredProductsInternalServerError"] = Field(None, alias="internalServerError")
    invalid_input_error: Optional["SponsoredProductsInvalidInputError"] = Field(None, alias="invalidInputError")
    malformed_value_error: Optional["SponsoredProductsMalformedValueError"] = Field(None, alias="malformedValueError")
    missing_value_error: Optional["SponsoredProductsMissingValueError"] = Field(None, alias="missingValueError")
    other_error: Optional["SponsoredProductsOtherError"] = Field(None, alias="otherError")
    range_error: Optional["SponsoredProductsRangeError"] = Field(None, alias="rangeError")
    throttled_error: Optional["SponsoredProductsThrottledError"] = Field(None, alias="throttledError")

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetAccessError(BaseModel):
    error_type: str = Field(..., alias="errorType", description="The type of the error")
    error_value: "SponsoredProductsTargetAccessErrorSelector" = Field(..., alias="errorValue")

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetAccessExceptionResponseContent(BaseModel):
    """Exception resulting in accessing campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsTargetAccessError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetMutationExceptionResponseContent(BaseModel):
    """Exception resulting in mutating campaign management entities"""
    code: "SponsoredProductsInvalidArgumentErrorCode"
    errors: Optional[list["SponsoredProductsTargetMutationError"]] = None
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsTargetingExpressionPredicateTypeWithoutOther(StrEnum):
    ASIN_ACCESSORY_RELATED = "ASIN_ACCESSORY_RELATED"
    ASIN_AGE_RANGE_SAME_AS = "ASIN_AGE_RANGE_SAME_AS"
    ASIN_BRAND_SAME_AS = "ASIN_BRAND_SAME_AS"
    ASIN_CATEGORY_SAME_AS = "ASIN_CATEGORY_SAME_AS"
    ASIN_EXPANDED_FROM = "ASIN_EXPANDED_FROM"
    ASIN_GENRE_SAME_AS = "ASIN_GENRE_SAME_AS"
    ASIN_IS_PRIME_SHIPPING_ELIGIBLE = "ASIN_IS_PRIME_SHIPPING_ELIGIBLE"
    ASIN_PRICE_BETWEEN = "ASIN_PRICE_BETWEEN"
    ASIN_PRICE_GREATER_THAN = "ASIN_PRICE_GREATER_THAN"
    ASIN_PRICE_LESS_THAN = "ASIN_PRICE_LESS_THAN"
    ASIN_REVIEW_RATING_BETWEEN = "ASIN_REVIEW_RATING_BETWEEN"
    ASIN_REVIEW_RATING_GREATER_THAN = "ASIN_REVIEW_RATING_GREATER_THAN"
    ASIN_REVIEW_RATING_LESS_THAN = "ASIN_REVIEW_RATING_LESS_THAN"
    ASIN_SAME_AS = "ASIN_SAME_AS"
    ASIN_SUBSTITUTE_RELATED = "ASIN_SUBSTITUTE_RELATED"
    KEYWORD_GROUP_SAME_AS = "KEYWORD_GROUP_SAME_AS"
    QUERY_BROAD_REL_MATCHES = "QUERY_BROAD_REL_MATCHES"
    QUERY_HIGH_REL_MATCHES = "QUERY_HIGH_REL_MATCHES"


class SponsoredProductsTargetingExpressionPredicateWithoutOther(BaseModel):
    type_: "SponsoredProductsTargetingExpressionPredicateTypeWithoutOther" = Field(..., alias="type")
    value: Optional[str] = Field(None, description="The expression value")

    model_config = {'populate_by_name': True}


class SponsoredProductsThrottledErrorCode(StrEnum):
    THROTTLED = "THROTTLED"


class SponsoredProductsThrottlingExceptionCode(StrEnum):
    THROTTLED = "THROTTLED"


class SponsoredProductsThrottlingExceptionResponseContent(BaseModel):
    code: "SponsoredProductsThrottledErrorCode"
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsUnauthenticatedExceptionCode(StrEnum):
    UNAUTHENTICATED = "UNAUTHENTICATED"


class SponsoredProductsUnauthenticatedExceptionResponseContent(BaseModel):
    """Unauthenticated. Request failed because user is not authenticated."""
    code: Optional["SponsoredProductsUnauthenticatedExceptionCode"] = None
    message: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SponsoredProductsUnauthorizedErrorCode(StrEnum):
    UNAUTHORIZED = "UNAUTHORIZED"


class SponsoredProductsUnauthorizedExceptionResponseContent(BaseModel):
    code: "SponsoredProductsUnauthorizedErrorCode"
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsUnsupportedMediaTypeErrorCode(StrEnum):
    UNSUPPORTED_MEDIA_TYPE = "UNSUPPORTED_MEDIA_TYPE"


class SponsoredProductsUnsupportedMediaTypeExceptionResponseContent(BaseModel):
    code: "SponsoredProductsUnsupportedMediaTypeErrorCode"
    message: str = Field(..., description="Human readable error message")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateAdGroup(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The identifier of the keyword.")
    default_bid: Optional[float] = Field(None, alias="defaultBid", description="A bid value for use when no bid is specified for keywords in the ad group. For more information about bid constraints by")
    name: Optional[str] = Field(None, description="The name of the ad group.")
    state: Optional["SponsoredProductsCreateOrUpdateEntityState"] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateCampaign(BaseModel):
    budget: Optional["SponsoredProductsCreateOrUpdateBudget"] = None
    campaign_id: str = Field(..., alias="campaignId", description="The identifier of the campaign.")
    dynamic_bidding: Optional["SponsoredProductsCreateOrUpdateDynamicBidding"] = Field(None, alias="dynamicBidding")
    end_date: Optional[str] = Field(None, alias="endDate", description="The format of the date is YYYY-MM-DD.")
    name: Optional[str] = Field(None, description="The name of the campaign.")
    off_amazon_settings: Optional["SponsoredProductsCreateOrUpdateOffAmazonSettings"] = Field(None, alias="offAmazonSettings")
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="The identifier of an existing portfolio to which the campaign is associated.")
    site_restrictions: Optional[list["SponsoredProductsSiteRestriction"]] = Field(None, alias="siteRestrictions", description="Restrict the ad to a particular site. siteRestrictions is an optional field. If this field is not set, ads from the camp")
    start_date: Optional[str] = Field(None, alias="startDate", description="The format of the date is YYYY-MM-DD.")
    state: Optional["SponsoredProductsCreateOrUpdateEntityState"] = None
    tags: Optional["SponsoredProductsTags"] = None
    targeting_type: Optional["SponsoredProductsTargetingType"] = Field(None, alias="targetingType")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateCampaignNegativeKeyword(BaseModel):
    keyword_id: str = Field(..., alias="keywordId", description="The identifier of the keyword.")
    state: Optional["SponsoredProductsCreateOrUpdateEntityState"] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateCampaignNegativeTargetingClause(BaseModel):
    expression: Optional[list["SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicate"]] = Field(None, description="The NegativeTargeting expression.")
    state: Optional["SponsoredProductsCreateOrUpdateEntityState"] = None
    target_id: str = Field(..., alias="targetId", description="The target identifier")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateKeyword(BaseModel):
    bid: Optional[float] = Field(None, description="Bid associated with this keyword. Applicable to biddable match types only. For more information about bid constraints by")
    keyword_id: str = Field(..., alias="keywordId", description="The identifier of the keyword.")
    state: Optional["SponsoredProductsCreateOrUpdateEntityState"] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateNegativeKeyword(BaseModel):
    keyword_id: str = Field(..., alias="keywordId", description="The identifier of the keyword.")
    state: Optional["SponsoredProductsCreateOrUpdateEntityState"] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateNegativeTargetingClause(BaseModel):
    expression: Optional[list["SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicate"]] = Field(None, description="The NegativeTargeting expression.")
    state: Optional["SponsoredProductsCreateOrUpdateEntityState"] = None
    target_id: str = Field(..., alias="targetId", description="The target identifier")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateProductAd(BaseModel):
    ad_id: str = Field(..., alias="adId", description="The product ad identifier.")
    state: Optional["SponsoredProductsCreateOrUpdateEntityState"] = None

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsAdGroupsRequestContent(BaseModel):
    ad_groups: list["SponsoredProductsUpdateAdGroup"] = Field(..., alias="adGroups", description="An array of adGroups with updated values.")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsAdGroupsResponseContent(BaseModel):
    ad_groups: "SponsoredProductsBulkAdGroupOperationResponse" = Field(..., alias="adGroups")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsCampaignNegativeKeywordsRequestContent(BaseModel):
    campaign_negative_keywords: list["SponsoredProductsUpdateCampaignNegativeKeyword"] = Field(..., alias="campaignNegativeKeywords", description="An array of campaignNegativeKeywords with updated values.")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsCampaignNegativeKeywordsResponseContent(BaseModel):
    campaign_negative_keywords: "SponsoredProductsBulkCampaignNegativeKeywordOperationResponse" = Field(..., alias="campaignNegativeKeywords")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsCampaignNegativeTargetingClausesRequestContent(BaseModel):
    campaign_negative_targeting_clauses: list["SponsoredProductsUpdateCampaignNegativeTargetingClause"] = Field(..., alias="campaignNegativeTargetingClauses", description="An array of Campaign Negative TargetingClauses with updated values.")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsCampaignNegativeTargetingClausesResponseContent(BaseModel):
    campaign_negative_targeting_clauses: "SponsoredProductsBulkCampaignNegativeTargetingClauseOperationResponse" = Field(..., alias="campaignNegativeTargetingClauses")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsCampaignsRequestContent(BaseModel):
    campaigns: list["SponsoredProductsUpdateCampaign"] = Field(..., description="An array of campaigns with updated values. Note: targetingType cannot be updated")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsCampaignsResponseContent(BaseModel):
    campaigns: "SponsoredProductsBulkCampaignOperationResponse"

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsKeywordsRequestContent(BaseModel):
    keywords: list["SponsoredProductsUpdateKeyword"] = Field(..., description="An array of keywords with updated values.")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsKeywordsResponseContent(BaseModel):
    keywords: "SponsoredProductsBulkKeywordOperationResponse"

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsNegativeKeywordsRequestContent(BaseModel):
    negative_keywords: list["SponsoredProductsUpdateNegativeKeyword"] = Field(..., alias="negativeKeywords", description="An array of negativeKeywords with updated values.")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsNegativeKeywordsResponseContent(BaseModel):
    negative_keywords: "SponsoredProductsBulkNegativeKeywordOperationResponse" = Field(..., alias="negativeKeywords")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsNegativeTargetingClausesRequestContent(BaseModel):
    negative_targeting_clauses: list["SponsoredProductsUpdateNegativeTargetingClause"] = Field(..., alias="negativeTargetingClauses", description="An array of negativeTargeting with updated values.")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsNegativeTargetingClausesResponseContent(BaseModel):
    negative_targeting_clauses: "SponsoredProductsBulkNegativeTargetingClauseOperationResponse" = Field(..., alias="negativeTargetingClauses")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsProductAdsRequestContent(BaseModel):
    product_ads: list["SponsoredProductsUpdateProductAd"] = Field(..., alias="productAds", description="An array of ads with updated values.")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsProductAdsResponseContent(BaseModel):
    product_ads: "SponsoredProductsBulkProductAdOperationResponse" = Field(..., alias="productAds")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateTargetingClause(BaseModel):
    bid: Optional[float] = Field(None, description="The bid for ads sourced using the target. Targets that do not have bid values in listTargetingClauses will inherit the d")
    expression: Optional[list["SponsoredProductsTargetingExpressionPredicateWithoutOther"]] = Field(None, description="The targeting expression.")
    expression_type: Optional["SponsoredProductsExpressionTypeWithoutOther"] = Field(None, alias="expressionType")
    state: Optional["SponsoredProductsCreateOrUpdateEntityState"] = None
    target_id: str = Field(..., alias="targetId", description="The target identifier")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsTargetingClausesRequestContent(BaseModel):
    targeting_clauses: list["SponsoredProductsUpdateTargetingClause"] = Field(..., alias="targetingClauses", description="An array of targetingClauses with updated values.")

    model_config = {'populate_by_name': True}


class SponsoredProductsUpdateSponsoredProductsTargetingClausesResponseContent(BaseModel):
    targeting_clauses: "SponsoredProductsBulkTargetingClauseOperationResponse" = Field(..., alias="targetingClauses")

    model_config = {'populate_by_name': True}


class TargetableAsinCounts(BaseModel):
    """Response object to get number of targetable asins for refinements provided by the user"""
    asin_counts: Optional["IntegerRange"] = Field(None, alias="asinCounts")

    model_config = {'populate_by_name': True}


class TargetableCategories(BaseModel):
    """Response object containing all targetable categories for the advertiser's marketplace. ID is the category ID. NA is the name. CH is the list of child categories. TA is if the category is targetable. A"""
    category_tree: Optional[str] = Field(None, alias="categoryTree")

    model_config = {'populate_by_name': True}


class TargetableCategoriesLoP(BaseModel):
    """Response object containing all targetable categories for the advertiser's marketplace in a language of preference (LoP) provide by the locale query parameter. ID is the category ID. NA is the name. TN"""
    category_tree: Optional[str] = Field(None, alias="categoryTree")

    model_config = {'populate_by_name': True}


class ThemeBasedBidRecommendation(BaseModel):
    bid_recommendations_for_targeting_expressions: list["BidRecommendationPerTargetingExpression"] = Field(..., alias="bidRecommendationsForTargetingExpressions", description="The bid recommendations for targeting expressions listed in the request.")
    impact_metrics: Optional["ImpactMetrics"] = Field(None, alias="impactMetrics")
    theme: "Theme"

    model_config = {'populate_by_name': True}


class ThemeBasedBidRecommendationResponse(BaseModel):
    """A list of bid recommendation themes and associated bid recommendations."""
    bid_recommendations: list["ThemeBasedBidRecommendation"] = Field(..., alias="bidRecommendations")

    model_config = {'populate_by_name': True}


class ThemeBasedBidRecommendationV4(BaseModel):
    bid_recommendations_for_targeting_expressions: list["BidRecommendationPerTargetingExpressionV4"] = Field(..., alias="bidRecommendationsForTargetingExpressions", description="The bid recommendations for targeting expressions listed in the request.")
    theme: "Theme"

    model_config = {'populate_by_name': True}


class ThemeBasedBidRecommendationResponseV4(BaseModel):
    """A list of bid recommendation themes and associated bid recommendations."""
    bid_recommendations: list["ThemeBasedBidRecommendationV4"] = Field(..., alias="bidRecommendations")

    model_config = {'populate_by_name': True}


class ThemeBasedBidRecommendationV5(BaseModel):
    bid_analyses_for_targeting_expressions: Optional[list["BidAnalysesPerTargetingExpression"]] = Field(None, alias="bidAnalysesForTargetingExpressions", description="The bid analyses for targeting expressions listed in the request.")
    bid_recommendations_for_targeting_expressions: list["BidRecommendationPerTargetingExpressionV5"] = Field(..., alias="bidRecommendationsForTargetingExpressions", description="The bid recommendations for targeting expressions listed in the request.")
    theme: "Theme"

    model_config = {'populate_by_name': True}


class ThemeBasedBidRecommendationResponseV5(BaseModel):
    """A list of bid recommendation themes and associated bid recommendations."""
    bid_recommendations: list["ThemeBasedBidRecommendationV5"] = Field(..., alias="bidRecommendations")

    model_config = {'populate_by_name': True}


class ThrottlingException(BaseModel):
    """Returns information about a ThrottlingException."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class UnauthorizedException(BaseModel):
    """Returns information about an UnauthorizedException."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class UnprocessableEntityException(BaseModel):
    """Returns information about UnprocessableEntityException."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class UpdateBudgetRulesResponse(BaseModel):
    responses: Optional[list["BudgetRuleResponse"]] = None

    model_config = {'populate_by_name': True}


class UpdateSPBudgetRulesRequest(BaseModel):
    """Request object for updating budget rule for SP campaign"""
    budget_rules_details: Optional[list["SPBudgetRule"]] = Field(None, alias="budgetRulesDetails", description="A list of budget rule details.")

    model_config = {'populate_by_name': True}


class UpdateSPCampaignOptimizationRuleResponse(BaseModel):
    campaign_optimization_id: Optional["campaignOptimizationId"] = Field(None, alias="campaignOptimizationId")
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the error, if unsuccessful")

    model_config = {'populate_by_name': True}


class UpdateSPCampaignOptimizationRulesRequest(BaseModel):
    """Request object for updating campaign optimization rule"""
    campaign_ids: list["RuleCampaignId"] = Field(..., alias="campaignIds", description="A list of campaign ids")
    campaign_optimization_id: "campaignOptimizationId" = Field(..., alias="campaignOptimizationId")
    recurrence: "RecurrenceType"
    rule_action: "RuleAction" = Field(..., alias="ruleAction")
    rule_condition: Optional["RuleConditionList"] = Field(None, alias="ruleCondition")
    rule_name: Optional["RuleName"] = Field(None, alias="ruleName")
    rule_type: "RuleType" = Field(..., alias="ruleType")

    model_config = {'populate_by_name': True}


class ValidationException(BaseModel):
    """Returns information about a ValidationException."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}

