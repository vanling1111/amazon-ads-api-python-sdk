"""Auto-generated Pydantic models. Do not edit manually.

Source: Recommendations_prod_3p.json
Title:  Recommendations
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class APIError(BaseModel):
    """Error response object providing information on API error."""
    code: str = Field(..., description="HTTP status code of the response.")
    message: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class APISuccess(BaseModel):
    """Response object providing information on API success."""
    code: str = Field(..., description="HTTP status code of the response.")
    message: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class AdProduct(StrEnum):
    SB = "SB"
    SD = "SD"
    SP = "SP"
    ST = "ST"


class ApplyRecommendationFailure(BaseModel):
    error: "APIError"
    index: float = Field(..., description="Index of the recommendation in the array from the request body.")
    recommendation_id: str = Field(..., alias="recommendationId", description="Recommendation identifier.")

    model_config = {'populate_by_name': True}


class SevenDaysEstimatedOpportunities(BaseModel):
    """Seven days of estimated opportunities."""
    end_date: str = Field(..., alias="endDate", description="End date of the opportunities date range in YYYY-MM-DDTHH:mm:ssZ format.")
    estimated_incremental_clicks_lower: Optional[int] = Field(None, alias="estimatedIncrementalClicksLower", description="Lower bound of estimated incremental clicks that could be gained if all recommendations are applied.")
    estimated_incremental_clicks_upper: Optional[int] = Field(None, alias="estimatedIncrementalClicksUpper", description="Upper bound of estimated incremental clicks that could be gained if all recommendations are applied.")
    start_date: str = Field(..., alias="startDate", description="Start date of the opportunities date range in YYYY-MM-DDTHH:mm:ssZ format.")

    model_config = {'populate_by_name': True}


class RecommendationReason(StrEnum):
    AT_BID_FALLBACK = "AT_BID_FALLBACK"
    AT_NOT_ALL_MATCH_TYPE_ENABLED = "AT_NOT_ALL_MATCH_TYPE_ENABLED"
    MT_BID_FALLBACK = "MT_BID_FALLBACK"
    MT_IRRELEVANT_KEYWORD_IMPRESSIONS = "MT_IRRELEVANT_KEYWORD_IMPRESSIONS"
    MT_KEYWORDS_HAVE_LOW_IMPRESSIONS = "MT_KEYWORDS_HAVE_LOW_IMPRESSIONS"
    MT_KEYWORD_FALLBACK = "MT_KEYWORD_FALLBACK"
    MT_NOT_ENOUGH_TOP_IMPRESSIONS = "MT_NOT_ENOUGH_TOP_IMPRESSIONS"


class RecommendationReasons(BaseModel):
    """List of reasons why the recommendation was created"""
    pass


class ConsolidatedRecommendation(BaseModel):
    """Data for a group of recommendations."""
    recommendation_reasons: Optional["RecommendationReasons"] = Field(None, alias="recommendationReasons")
    seven_days_estimated_opportunities: Optional["SevenDaysEstimatedOpportunities"] = Field(None, alias="sevenDaysEstimatedOpportunities")

    model_config = {'populate_by_name': True}


class GroupingType(StrEnum):
    ADD_TARGETS_CONTEXTUAL = "ADD_TARGETS_CONTEXTUAL"
    CAMPAIGN_INCREASE_CLICKS = "CAMPAIGN_INCREASE_CLICKS"
    DECREASE_BID_CONTEXTUAL = "DECREASE_BID_CONTEXTUAL"
    INCREASE_BID_CONTEXTUAL = "INCREASE_BID_CONTEXTUAL"
    INCREASE_BUDGET_CONTEXTUAL = "INCREASE_BUDGET_CONTEXTUAL"
    INCREASE_CLICKTHROUGH_RATE = "INCREASE_CLICKTHROUGH_RATE"
    INCREASE_CONVERSION_RATE = "INCREASE_CONVERSION_RATE"
    IN_SEASON_ASIN = "IN_SEASON_ASIN"
    NEW_ASIN = "NEW_ASIN"
    NEW_CAMPAIGN_ATTRIBUTED_ORDERS = "NEW_CAMPAIGN_ATTRIBUTED_ORDERS"
    NEW_CAMPAIGN_CLICKS = "NEW_CAMPAIGN_CLICKS"
    NEW_CAMPAIGN_GROW_BIS_IMAGE_GENERAL = "NEW_CAMPAIGN_GROW_BIS_IMAGE_GENERAL"
    NEW_CAMPAIGN_GROW_BIS_IMAGE_SPECIFIC = "NEW_CAMPAIGN_GROW_BIS_IMAGE_SPECIFIC"
    NEW_CAMPAIGN_GROW_BRAND_IMPRESSION_SHARE = "NEW_CAMPAIGN_GROW_BRAND_IMPRESSION_SHARE"
    NEW_CAMPAIGN_NEW_TO_BRAND_ORDERS = "NEW_CAMPAIGN_NEW_TO_BRAND_ORDERS"
    NEW_CAMPAIGN_PRE_COMPUTED_RECOMMENDATION_BUNDLE = "NEW_CAMPAIGN_PRE_COMPUTED_RECOMMENDATION_BUNDLE"
    NEW_CAMPAIGN_SPB_GOAL_BASED = "NEW_CAMPAIGN_SPB_GOAL_BASED"
    OPTIMIZE_ATTRIBUTED_ORDERS = "OPTIMIZE_ATTRIBUTED_ORDERS"
    OPTIMIZE_BRANDED_SEARCHES = "OPTIMIZE_BRANDED_SEARCHES"
    OPTIMIZE_CLICKS = "OPTIMIZE_CLICKS"
    OPTIMIZE_COST_PER_BRANDED_SEARCH = "OPTIMIZE_COST_PER_BRANDED_SEARCH"
    OPTIMIZE_COST_PER_CLICK = "OPTIMIZE_COST_PER_CLICK"
    OPTIMIZE_COST_PER_DETAIL_PAGE_VIEW = "OPTIMIZE_COST_PER_DETAIL_PAGE_VIEW"
    OPTIMIZE_COST_PER_NEW_TO_BRAND_ORDERS = "OPTIMIZE_COST_PER_NEW_TO_BRAND_ORDERS"
    OPTIMIZE_DETAIL_PAGE_VIEWS = "OPTIMIZE_DETAIL_PAGE_VIEWS"
    OPTIMIZE_NEW_TO_BRAND_ORDERS = "OPTIMIZE_NEW_TO_BRAND_ORDERS"
    OPTIMIZE_ROAS = "OPTIMIZE_ROAS"
    OPTIMIZE_SPB_GOAL_BASED = "OPTIMIZE_SPB_GOAL_BASED"
    ST_NE_NEW_CAMPAIGN_CREATION = "ST_NE_NEW_CAMPAIGN_CREATION"
    UNDERPERFORMING_CAMPAIGN_INCREASE_CLICKS = "UNDERPERFORMING_CAMPAIGN_INCREASE_CLICKS"


class KeywordSortingDimension(StrEnum):
    CLICK = "CLICK"
    CONVERSION = "CONVERSION"


class EstimatedImpactOpportunityLostToCompetitorsPercentage(BaseModel):
    """Estimated impact of the recommendation on percentage of opportunity lost to competitors."""
    incremental_lower_bound: float = Field(..., alias="incrementalLowerBound", description="Lower bound of the estimated change in percentage of customers who purchased from another category brand when the create")
    incremental_upper_bound: float = Field(..., alias="incrementalUpperBound", description="Upper bound of the estimated change in percentage of customers who purchased from another category brand when the create")

    model_config = {'populate_by_name': True}


class EstimatedImpactOpportunityLostPurchaseJourney(BaseModel):
    """Estimated impact of the recommendation on lost purchase journey opportunities."""
    incremental_lower_bound: float = Field(..., alias="incrementalLowerBound", description="Lower bound of the estimated change in customers with no further engagement with brand when the create grow brand impres")
    incremental_upper_bound: float = Field(..., alias="incrementalUpperBound", description="Upper bound of the estimated change in customers with no further engagement with brand when the create grow brand impres")

    model_config = {'populate_by_name': True}


class EstimatedImpactOpportunityLostToCompetitorsSales(BaseModel):
    """Estimated impact of the recommendation on opportunity of sales lost to competitors."""
    incremental_lower_bound: float = Field(..., alias="incrementalLowerBound", description="Lower bound of the estimated change in competitor revenue generated from customers purchasing from competing brand when ")
    incremental_upper_bound: float = Field(..., alias="incrementalUpperBound", description="Upper bound of the estimated change in competitor revenue generated from customers purchasing from competing brand when ")

    model_config = {'populate_by_name': True}


class EstimatedImpactTopOfSearchImpressionShare(BaseModel):
    """Estimated impact of the recommendation on top of search impression share."""
    incremental_lower_bound: float = Field(..., alias="incrementalLowerBound", description="Lower bound of the estimated change in top of search impression share when the create grow brand impression share campai")
    incremental_upper_bound: float = Field(..., alias="incrementalUpperBound", description="Upper bound of the estimated change in top of search impression share when the create grow brand impression share campai")

    model_config = {'populate_by_name': True}


class EstimatedImpactCost(BaseModel):
    """Estimated impact of the recommendation on cost."""
    forecasted_current_lower_bound: Optional[float] = Field(None, alias="forecastedCurrentLowerBound", description="Lower bound of the forecasted cost for the campaign, based on the current campaign settings and data from similar advert")
    forecasted_current_upper_bound: Optional[float] = Field(None, alias="forecastedCurrentUpperBound", description="Upper bound of the forecasted cost for the campaign, based on the current campaign settings and data from similar advert")
    forecasted_recommended_lower_bound: Optional[float] = Field(None, alias="forecastedRecommendedLowerBound", description="Lower bound of the forecasted cost for the campaign, if the recommendation is adopted, based on data from similar advert")
    forecasted_recommended_upper_bound: Optional[float] = Field(None, alias="forecastedRecommendedUpperBound", description="Upper bound of the forecasted cost for the campaign, if the recommendation is adopted, based on data from similar advert")
    incremental_lower_bound: Optional[float] = Field(None, alias="incrementalLowerBound", description="Lower bound of the estimated change in cost seen for similar advertisers within the time period indicated when the recom")
    incremental_upper_bound: Optional[float] = Field(None, alias="incrementalUpperBound", description="Upper bound of the estimated change in cost seen for similar advertisers within the time period indicated when the recom")

    model_config = {'populate_by_name': True}


class EstimatedImpactImpressions(BaseModel):
    """Estimated impact of the recommendation on impressions."""
    forecasted_current_lower_bound: Optional[float] = Field(None, alias="forecastedCurrentLowerBound", description="Lower bound of the forecasted number of impressions for the campaign, based on the current campaign settings and data fr")
    forecasted_current_upper_bound: Optional[float] = Field(None, alias="forecastedCurrentUpperBound", description="Upper bound of the forecasted number of impressions for the campaign, based on the current campaign settings and data fr")
    forecasted_recommended_lower_bound: Optional[float] = Field(None, alias="forecastedRecommendedLowerBound", description="Lower bound of the forecasted number of impressions for the campaign, if the recommendation is adopted, based on data fr")
    forecasted_recommended_upper_bound: Optional[float] = Field(None, alias="forecastedRecommendedUpperBound", description="Upper bound of the forecasted number of impressions for the campaign, if the recommendation is adopted, based on data fr")
    incremental_lower_bound: Optional[float] = Field(None, alias="incrementalLowerBound", description="Lower bound of the estimated change in impressions seen for similar advertisers within the time period indicated when th")
    incremental_upper_bound: Optional[float] = Field(None, alias="incrementalUpperBound", description="Upper bound of the estimated change in impressions seen for similar advertisers within the time period indicated when th")

    model_config = {'populate_by_name': True}


class EstimatedImpactCohortTopOfSearchImpressionShare(BaseModel):
    """Estimated impact of the recommendation on brand cohort top of search impression share."""
    incremental_lower_bound: float = Field(..., alias="incrementalLowerBound", description="Upper bound of the estimated change in cohort top of search impression share when the create grow brand impression share")
    incremental_upper_bound: float = Field(..., alias="incrementalUpperBound", description="Upper bound of the estimated change in cohort top of search impression share when the create grow brand impression share")

    model_config = {'populate_by_name': True}


class EstimatedImpactOpportunityLostToCompetitors(BaseModel):
    """Estimated impact of the recommendation on opportunity lost to competitors."""
    incremental_lower_bound: float = Field(..., alias="incrementalLowerBound", description="Lower bound of the estimated change in customers who purchased from another category brand when the create grow brand im")
    incremental_upper_bound: float = Field(..., alias="incrementalUpperBound", description="Upper bound of the estimated change in customers who purchased from another category brand when the create grow brand im")

    model_config = {'populate_by_name': True}


class EstimatedImpactIncrementalSalesIncrementalCostRatio(BaseModel):
    """Estimated impact of the recommendation on incremental sales and incremental cost ratio."""
    incremental_lower_bound: float = Field(..., alias="incrementalLowerBound", description="Lower bound of the estimated change in incremental sales to incremental cost ratio seen for similar advertisers within t")
    incremental_upper_bound: float = Field(..., alias="incrementalUpperBound", description="Upper bound of the estimated change in incremental sales to incremental cost ratio seen for similar advertisers within t")

    model_config = {'populate_by_name': True}


class EstimatedImpactSales(BaseModel):
    """Estimated impact of the recommendation on sales."""
    forecasted_current_lower_bound: Optional[float] = Field(None, alias="forecastedCurrentLowerBound", description="Lower bound of the forecasted sales for the campaign, based on the current campaign settings and data from similar adver")
    forecasted_current_upper_bound: Optional[float] = Field(None, alias="forecastedCurrentUpperBound", description="Upper bound of the forecasted sales for the campaign, based on the current campaign settings and data from similar adver")
    forecasted_recommended_lower_bound: Optional[float] = Field(None, alias="forecastedRecommendedLowerBound", description="Lower bound of the forecasted sales for the campaign, if the recommendation is adopted, based on data from similar adver")
    forecasted_recommended_upper_bound: Optional[float] = Field(None, alias="forecastedRecommendedUpperBound", description="Upper bound of the forecasted sales for the campaign, if the recommendation is adopted, based on data from similar adver")
    incremental_lower_bound: Optional[float] = Field(None, alias="incrementalLowerBound", description="Lower bound of the estimated change in sales seen for similar advertisers within the time period indicated when the reco")
    incremental_upper_bound: Optional[float] = Field(None, alias="incrementalUpperBound", description="Upper bound of the estimated change in sales seen for similar advertisers within the time period indicated when the reco")

    model_config = {'populate_by_name': True}


class EstimatedImpactRoas(BaseModel):
    """Estimated impact of the recommendation on ROAS."""
    forecasted_current_lower_bound: Optional[float] = Field(None, alias="forecastedCurrentLowerBound", description="Lower bound of the forecasted ROAS for the campaign, based on the current campaign settings and data from similar advert")
    forecasted_current_upper_bound: Optional[float] = Field(None, alias="forecastedCurrentUpperBound", description="Upper bound of the forecasted ROAS for the campaign, based on the current campaign settings and data from similar advert")
    forecasted_recommended_lower_bound: Optional[float] = Field(None, alias="forecastedRecommendedLowerBound", description="Lower bound of the forecasted ROAS for the campaign, if the recommendation is adopted, based on data from similar advert")
    forecasted_recommended_upper_bound: Optional[float] = Field(None, alias="forecastedRecommendedUpperBound", description="Upper bound of the forecasted ROAS for the campaign, if the recommendation is adopted, based on data from similar advert")
    incremental_lower_bound: Optional[float] = Field(None, alias="incrementalLowerBound", description="Lower bound of the estimated change in ROAS seen for similar advertisers within the time period indicated when the recom")
    incremental_upper_bound: Optional[float] = Field(None, alias="incrementalUpperBound", description="Upper bound of the estimated change in ROAS seen for similar advertisers within the time period indicated when the recom")

    model_config = {'populate_by_name': True}


class EstimatedImpactClicks(BaseModel):
    """Estimated impact of the recommendation on clicks."""
    forecasted_current_lower_bound: Optional[float] = Field(None, alias="forecastedCurrentLowerBound", description="Lower bound of the forecasted number of clicks for the campaign, based on the current campaign settings and data from si")
    forecasted_current_upper_bound: Optional[float] = Field(None, alias="forecastedCurrentUpperBound", description="Upper bound of the forecasted number of clicks for the campaign, based on the current campaign settings and data from si")
    forecasted_recommended_lower_bound: Optional[float] = Field(None, alias="forecastedRecommendedLowerBound", description="Lower bound of the forecasted number of clicks for the campaign, if the recommendation is adopted, based on data from si")
    forecasted_recommended_upper_bound: Optional[float] = Field(None, alias="forecastedRecommendedUpperBound", description="Upper bound of the forecasted number of clicks for the campaign, if the recommendation is adopted, based on data from si")
    incremental_lower_bound: Optional[float] = Field(None, alias="incrementalLowerBound", description="Lower bound of the estimated change in clicks seen for similar advertisers within the time period indicated when the rec")
    incremental_upper_bound: Optional[float] = Field(None, alias="incrementalUpperBound", description="Upper bound of the estimated change in clicks seen for similar advertisers within the time period indicated when the rec")

    model_config = {'populate_by_name': True}


class CampaignEstimatedImpact(BaseModel):
    """Estimated impact at the campaign level."""
    clicks: Optional["EstimatedImpactClicks"] = None
    cohort_top_of_search_impression_share: Optional["EstimatedImpactCohortTopOfSearchImpressionShare"] = Field(None, alias="cohortTopOfSearchImpressionShare")
    cost: Optional["EstimatedImpactCost"] = None
    impressions: Optional["EstimatedImpactImpressions"] = None
    incremental_sales_incremental_cost_ratio: Optional["EstimatedImpactIncrementalSalesIncrementalCostRatio"] = Field(None, alias="incrementalSalesIncrementalCostRatio")
    opportunity_lost_purchase_journey: Optional["EstimatedImpactOpportunityLostPurchaseJourney"] = Field(None, alias="opportunityLostPurchaseJourney")
    opportunity_lost_to_competitors: Optional["EstimatedImpactOpportunityLostToCompetitors"] = Field(None, alias="opportunityLostToCompetitors")
    opportunity_lost_to_competitors_percentage: Optional["EstimatedImpactOpportunityLostToCompetitorsPercentage"] = Field(None, alias="opportunityLostToCompetitorsPercentage")
    opportunity_lost_to_competitors_sales: Optional["EstimatedImpactOpportunityLostToCompetitorsSales"] = Field(None, alias="opportunityLostToCompetitorsSales")
    roas: Optional["EstimatedImpactRoas"] = None
    sales: Optional["EstimatedImpactSales"] = None
    time_period_in_days: int = Field(..., alias="timePeriodInDays", description="Time period of the estimated impact in days.")
    top_of_search_impression_share: Optional["EstimatedImpactTopOfSearchImpressionShare"] = Field(None, alias="topOfSearchImpressionShare")

    model_config = {'populate_by_name': True}


class EstimatedImpact(BaseModel):
    """Estimated impact of the recommendation."""
    campaign: Optional["CampaignEstimatedImpact"] = None

    model_config = {'populate_by_name': True}


class PublishedBy(StrEnum):
    AMAZON_ADS_ACCOUNT_TEAM = "AMAZON_ADS_ACCOUNT_TEAM"


class PublishMetadata(BaseModel):
    """Metadata for publishing the recommendation."""
    published_by: "PublishedBy" = Field(..., alias="publishedBy")
    published_to_amazon_ad_console: bool = Field(..., alias="publishedToAmazonAdConsole", description="Indicates if recommendation was published to Amazon Ad Console.")

    model_config = {'populate_by_name': True}


class RecommendationStatus(StrEnum):
    APPLY_FAILED = "APPLY_FAILED"
    APPLY_IN_PROGRESS = "APPLY_IN_PROGRESS"
    APPLY_SUCCESS = "APPLY_SUCCESS"
    PUBLISHED = "PUBLISHED"
    REJECTED = "REJECTED"


class TargetingMatchType(StrEnum):
    BROAD = "BROAD"
    EXACT = "EXACT"
    GROUP = "GROUP"
    NEGATIVE_BROAD = "NEGATIVE_BROAD"
    NEGATIVE_EXACT = "NEGATIVE_EXACT"
    NEGATIVE_PHRASE = "NEGATIVE_PHRASE"
    PHRASE = "PHRASE"
    TARGETING_EXPRESSION = "TARGETING_EXPRESSION"
    TARGETING_EXPRESSION_PREDEFINED = "TARGETING_EXPRESSION_PREDEFINED"
    THEME = "THEME"


class SevenDaysMissedOpportunities(BaseModel):
    """Seven days of missed opportunities."""
    end_date: Optional[str] = Field(None, alias="endDate", description="End date of the date range in local time and YYYY-MM-DD format for which missed opportunity metrics are provided.")
    estimated_missed_clicks_lower: Optional[int] = Field(None, alias="estimatedMissedClicksLower", description="Lower bound of estimated missed clicks.")
    estimated_missed_clicks_upper: Optional[int] = Field(None, alias="estimatedMissedClicksUpper", description="Upper bound of estimated missed clicks.")
    estimated_missed_impressions_lower: Optional[int] = Field(None, alias="estimatedMissedImpressionsLower", description="Lower bound of estimated missed impressions.")
    estimated_missed_impressions_upper: Optional[int] = Field(None, alias="estimatedMissedImpressionsUpper", description="Upper bound of estimated missed impressions.")
    estimated_missed_sales_lower: Optional[float] = Field(None, alias="estimatedMissedSalesLower", description="Lower bound of estimated missed sales. Provided in local currency.")
    estimated_missed_sales_upper: Optional[float] = Field(None, alias="estimatedMissedSalesUpper", description="Upper bound of estimated missed sales. Provided in local currency.")
    percent_time_in_budget: Optional[float] = Field(None, alias="percentTimeInBudget", description="Percentage of time the campaign is active with a budget.")
    start_date: Optional[str] = Field(None, alias="startDate", description="Start date of the date range in local time and YYYY-MM-DD format for which missed opportunity metrics are provided.")

    model_config = {'populate_by_name': True}


class BudgetRecommendation(BaseModel):
    """Budget recommendation of the campaign to which this recommendation is associated."""
    seven_days_missed_opportunities: "SevenDaysMissedOpportunities" = Field(..., alias="sevenDaysMissedOpportunities")

    model_config = {'populate_by_name': True}


class AsinContext(BaseModel):
    """Underlying asin context behind generating the recommendation."""
    season_end_date: Optional[str] = Field(None, alias="seasonEndDate", description="Date in which the products in the advertiser's category historically traffic-increase has cooled off.")
    season_start_date: Optional[str] = Field(None, alias="seasonStartDate", description="Date in which the products in the advertiser's category have historically started to see an increase in traffic.")
    trailing4_weeks_clickthrough_rate: Optional[float] = Field(None, alias="trailing4WeeksClickthroughRate", description="Past 4 weeks clickthrough rate of target product type.")
    trailing4_weeks_conversion_rate: Optional[float] = Field(None, alias="trailing4WeeksConversionRate", description="Past 4 weeks conversion rate of target product type.")

    model_config = {'populate_by_name': True}


class Benchmark(BaseModel):
    """The value of a campaign performance metric relative to peer campaigns, where peer campaigns are identified using an unsupervised learning model that groups campaigns into mutually exclusive clusters o"""
    benchmark_value: Optional[float] = Field(None, alias="benchmarkValue", description="The benchmark for the campaign for a given metric. This value is based on the performance of similar campaigns for the g")
    percent_difference: Optional[float] = Field(None, alias="percentDifference", description="The percent difference relative to the benchmark value.")
    period: Optional[float] = Field(None, description="The time period in days over which the metric value was determined.")

    model_config = {'populate_by_name': True}


class BenchmarkContext(BaseModel):
    """Benchmark Context for the recommendation.   | Benchmark | Description | |---|---| | Impressions | Impressions received by the campaign over the specified time period | | Roas | Return on ad spend (RoA"""
    ad_spend: Optional["Benchmark"] = Field(None, alias="adSpend")
    attributed_orders: Optional["Benchmark"] = Field(None, alias="attributedOrders")
    branded_searches: Optional["Benchmark"] = Field(None, alias="brandedSearches")
    budget_utilization: Optional["Benchmark"] = Field(None, alias="budgetUtilization")
    clickthrough_rate: Optional["Benchmark"] = Field(None, alias="clickthroughRate")
    cost_per_branded_search: Optional["Benchmark"] = Field(None, alias="costPerBrandedSearch")
    cost_per_detail_page_view: Optional["Benchmark"] = Field(None, alias="costPerDetailPageView")
    detail_page_views: Optional["Benchmark"] = Field(None, alias="detailPageViews")
    impressions: Optional["Benchmark"] = None
    roas: Optional["Benchmark"] = None

    model_config = {'populate_by_name': True}


class SummaryCode(StrEnum):
    ADD_TARGETS_CONTEXTUAL_SUMMARY = "ADD_TARGETS_CONTEXTUAL_SUMMARY"
    DECREASE_BID_CONTEXTUAL_SUMMARY = "DECREASE_BID_CONTEXTUAL_SUMMARY"
    INCREASE_BID_CONTEXTUAL_SUMMARY = "INCREASE_BID_CONTEXTUAL_SUMMARY"
    INCREASE_BUDGET_CONTEXTUAL_SUMMARY = "INCREASE_BUDGET_CONTEXTUAL_SUMMARY"


class Summary(BaseModel):
    """An explanation of the campaign performance vis-a-vis relevant benchmarks, and why the recommendation was generated."""
    code: Optional[SummaryCode] = Field(None, description="Summary Codes.   | Code | Message | |---|---| | DECREASE_BID_CONTEXTUAL_SUMMARY | You have Sponsored Products campaigns ")
    message: Optional[str] = Field(None, description="A localized description of the summary.")

    model_config = {'populate_by_name': True}


class DiagnosticContext(BaseModel):
    """Underlying diagnostic context behind generating the recommendation."""
    asin_age: Optional[float] = Field(None, alias="asinAge", description="The number of days since the ASIN was added to the advertiser’s catalog.")
    benchmark_context: Optional["BenchmarkContext"] = Field(None, alias="benchmarkContext")
    diagnostic_date: Optional[str] = Field(None, alias="diagnosticDate", description="The date on which the campaign was diagnosed.")
    summary: Optional["Summary"] = None

    model_config = {'populate_by_name': True}


class RecommendationContext(BaseModel):
    """Context of the recommendation."""
    asin_context: Optional["AsinContext"] = Field(None, alias="asinContext")
    diagnostic_context: Optional["DiagnosticContext"] = Field(None, alias="diagnosticContext")

    model_config = {'populate_by_name': True}


class BiddingStrategy(StrEnum):
    AUTO_FOR_SALES = "AUTO_FOR_SALES"
    LEGACY_FOR_SALES = "LEGACY_FOR_SALES"
    MANUAL = "MANUAL"
    RULE_BASED = "RULE_BASED"


class RuleBasedBidding(BaseModel):
    """Rule based bidding for the campaign to which this recommendation is associated."""
    campaign_optimization_id: Optional[str] = Field(None, alias="campaignOptimizationId", description="Identifier of the campaign optimization.")
    current_bidding_strategy: Optional["BiddingStrategy"] = Field(None, alias="currentBiddingStrategy")
    current_rule_roas: Optional[float] = Field(None, alias="currentRuleRoas", description="Current threshold of the RoAS performance metric.")
    recommended_bidding_strategy: "BiddingStrategy" = Field(..., alias="recommendedBiddingStrategy")
    recommended_rule_roas: float = Field(..., alias="recommendedRuleRoas", description="Recommended threshold of the RoAS performance metric.")

    model_config = {'populate_by_name': True}


class BudgetRuleIncreaseBy(BaseModel):
    value: float = Field(..., description="Budget of the rule.")

    model_config = {'populate_by_name': True}


class BudgetRulePerformanceMeasureCondition(BaseModel):
    threshold: float = Field(..., description="Threshold of the performance metric.")

    model_config = {'populate_by_name': True}


class BudgetRuleEventTypeDuration(BaseModel):
    end_date: Optional[str] = Field(None, alias="endDate", description="End date of the event in YYYY-MM-DD format.")
    event_id: str = Field(..., alias="eventId", description="Identifier of the event.")
    start_date: Optional[str] = Field(None, alias="startDate", description="Start date of the event in YYYY-MM-DD format. Note that this field is present only for announced events.")

    model_config = {'populate_by_name': True}


class BudgetRuleDateRangeTypeDuration(BaseModel):
    end_date: Optional[str] = Field(None, alias="endDate", description="End date of the budget rule in YYYY-MM-DD format. The end date is inclusive.")
    start_date: str = Field(..., alias="startDate", description="Start date of the budget rule in YYYY-MM-DD format. The start date is inclusive.")

    model_config = {'populate_by_name': True}


class BudgetRuleDuration(BaseModel):
    date_range_type_duration: Optional["BudgetRuleDateRangeTypeDuration"] = Field(None, alias="dateRangeTypeDuration")
    event_type_duration: Optional["BudgetRuleEventTypeDuration"] = Field(None, alias="eventTypeDuration")

    model_config = {'populate_by_name': True}


class BudgetRuleDetails(BaseModel):
    budget_increase_by: Optional["BudgetRuleIncreaseBy"] = Field(None, alias="budgetIncreaseBy")
    duration: Optional["BudgetRuleDuration"] = None
    performance_measure_condition: Optional["BudgetRulePerformanceMeasureCondition"] = Field(None, alias="performanceMeasureCondition")
    rule_name: Optional[str] = Field(None, alias="ruleName", description="Name of the budget rule.")
    rule_type: Optional[str] = Field(None, alias="ruleType", description="Type of budget rule.")

    model_config = {'populate_by_name': True}


class BudgetRule(BaseModel):
    """Budget rule of the campaign to which this recommendation is associated."""
    rule_details: "BudgetRuleDetails" = Field(..., alias="ruleDetails")
    rule_id: Optional[str] = Field(None, alias="ruleId", description="Identifier of the budget rule.")

    model_config = {'populate_by_name': True}


class RecommendationType(StrEnum):
    AD_GROUP_BID_OPTIMIZATION = "AD_GROUP_BID_OPTIMIZATION"
    AD_GROUP_DEFAULT_BID = "AD_GROUP_DEFAULT_BID"
    AD_GROUP_STATE = "AD_GROUP_STATE"
    AMAZON_BUSINESS_BID_BOOST = "AMAZON_BUSINESS_BID_BOOST"
    AUDIENCE_COHORT_BID_BOOST = "AUDIENCE_COHORT_BID_BOOST"
    AUDIENCE_TARGETING_BID = "AUDIENCE_TARGETING_BID"
    AUDIENCE_TARGETING_STATE = "AUDIENCE_TARGETING_STATE"
    CAMPAIGN_BIDDING_RULE = "CAMPAIGN_BIDDING_RULE"
    CAMPAIGN_BIDDING_STRATEGY = "CAMPAIGN_BIDDING_STRATEGY"
    CAMPAIGN_BUDGET = "CAMPAIGN_BUDGET"
    CAMPAIGN_BUDGET_RULE = "CAMPAIGN_BUDGET_RULE"
    CAMPAIGN_END_DATE = "CAMPAIGN_END_DATE"
    CAMPAIGN_PRODUCT_PLACEMENT = "CAMPAIGN_PRODUCT_PLACEMENT"
    CAMPAIGN_STATE = "CAMPAIGN_STATE"
    CAMPAIGN_TOP_PLACEMENT = "CAMPAIGN_TOP_PLACEMENT"
    KEYWORD_BID = "KEYWORD_BID"
    KEYWORD_STATE = "KEYWORD_STATE"
    NEGATIVE_AUDIENCE_TARGETING_STATE = "NEGATIVE_AUDIENCE_TARGETING_STATE"
    NEGATIVE_KEYWORD_STATE = "NEGATIVE_KEYWORD_STATE"
    NEGATIVE_PRODUCT_TARGETING_STATE = "NEGATIVE_PRODUCT_TARGETING_STATE"
    NEW_AD_GROUP = "NEW_AD_GROUP"
    NEW_AUDIENCE_TARGETING = "NEW_AUDIENCE_TARGETING"
    NEW_CAMPAIGN = "NEW_CAMPAIGN"
    NEW_CAMPAIGN_BIDDING_RULE = "NEW_CAMPAIGN_BIDDING_RULE"
    NEW_CAMPAIGN_BUDGET_RULE = "NEW_CAMPAIGN_BUDGET_RULE"
    NEW_KEYWORD = "NEW_KEYWORD"
    NEW_NEGATIVE_AUDIENCE_TARGETING = "NEW_NEGATIVE_AUDIENCE_TARGETING"
    NEW_NEGATIVE_KEYWORD = "NEW_NEGATIVE_KEYWORD"
    NEW_NEGATIVE_PRODUCT_TARGETING = "NEW_NEGATIVE_PRODUCT_TARGETING"
    NEW_PRODUCT_AD = "NEW_PRODUCT_AD"
    NEW_PRODUCT_TARGETING = "NEW_PRODUCT_TARGETING"
    NEW_VIDEO_CAMPAIGN = "NEW_VIDEO_CAMPAIGN"
    PRODUCT_AD_STATE = "PRODUCT_AD_STATE"
    PRODUCT_TARGETING_BID = "PRODUCT_TARGETING_BID"
    PRODUCT_TARGETING_STATE = "PRODUCT_TARGETING_STATE"


class Recommendation(BaseModel):
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="Identifier of the ad group to which this recommendation is associated.")
    ad_id: Optional[str] = Field(None, alias="adId", description="Identifier of the product ad to which this recommendation is associated.")
    ad_product: "AdProduct" = Field(..., alias="adProduct")
    apply_failure_reason: Optional[str] = Field(None, alias="applyFailureReason", description="A human-readable description of why the recommendation failed to apply.")
    asin: Optional[str] = Field(None, description="ASIN associated with the product. Defined for vendors only.")
    asin_group_template_id: Optional[str] = Field(None, alias="asinGroupTemplateId", description="Identifier of the asin group template to which this recommendation is associated.")
    budget_recommendation: Optional["BudgetRecommendation"] = Field(None, alias="budgetRecommendation")
    budget_rule: Optional["BudgetRule"] = Field(None, alias="budgetRule")
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="Identifier of the campaign to which this recommendation is associated.")
    campaign_template_id: Optional[str] = Field(None, alias="campaignTemplateId", description="Identifier of the campaign template to which this recommendation is associated.")
    consolidated_recommendation: Optional["ConsolidatedRecommendation"] = Field(None, alias="consolidatedRecommendation")
    current_value: Optional[str] = Field(None, alias="currentValue", description="Current value of the campaign entity to which this recommendation is associated. Will be null if the recommendation is f")
    estimated_impact: Optional["EstimatedImpact"] = Field(None, alias="estimatedImpact")
    grouping_type: Optional["GroupingType"] = Field(None, alias="groupingType")
    keyword_sorting_dimension: Optional["KeywordSortingDimension"] = Field(None, alias="keywordSortingDimension")
    keyword_sorting_rank: Optional[int] = Field(None, alias="keywordSortingRank", description="Sorting rank for new keyword recommendations.")
    publish_metadata: Optional["PublishMetadata"] = Field(None, alias="publishMetadata")
    recommendation_context: Optional["RecommendationContext"] = Field(None, alias="recommendationContext")
    recommendation_id: str = Field(..., alias="recommendationId", description="Recommendation identifier.")
    recommendation_type: "RecommendationType" = Field(..., alias="recommendationType")
    recommended_value: Optional[str] = Field(None, alias="recommendedValue", description="Recommended value of the campaign entity to which this recommendation is associated.")
    resolved_targeting: Optional[str] = Field(None, alias="resolvedTargeting", description="Resolved targeting expression to which this recommendation is associated.")
    rule_based_bidding: Optional["RuleBasedBidding"] = Field(None, alias="ruleBasedBidding")
    sku: Optional[str] = Field(None, description="SKU associated with the product. Defined for seller accounts only.")
    status: "RecommendationStatus"
    target_id: Optional[str] = Field(None, alias="targetId", description="Identifier of the target to which this recommendation is associated.")
    targeting: Optional[str] = Field(None, description="Targeting expression to which this recommendation is associated.")
    targeting_match_type: Optional["TargetingMatchType"] = Field(None, alias="targetingMatchType")

    model_config = {'populate_by_name': True}


class ApplyRecommendationSuccess(BaseModel):
    index: float = Field(..., description="Index of the recommendation in the array from the request body.")
    recommendation: "Recommendation"
    recommendation_id: str = Field(..., alias="recommendationId", description="Recommendation identifier.")
    success: "APISuccess"

    model_config = {'populate_by_name': True}


class ApplyRecommendationsRequest(BaseModel):
    recommendation_ids: list[str] = Field(..., alias="recommendationIds", description="Recommendation identifier.")

    model_config = {'populate_by_name': True}


class ApplyRecommendationsResponse(BaseModel):
    failures: list["ApplyRecommendationFailure"]
    successes: list["ApplyRecommendationSuccess"]

    model_config = {'populate_by_name': True}


class FilterField(StrEnum):
    AD_PRODUCT = "AD_PRODUCT"
    CAMPAIGN_ID = "CAMPAIGN_ID"
    GROUPING_TYPE = "GROUPING_TYPE"
    RECOMMENDATION_ID = "RECOMMENDATION_ID"
    RECOMMENDATION_TYPE = "RECOMMENDATION_TYPE"
    STATUS = "STATUS"


class FilterOperator(StrEnum):
    EXACT = "EXACT"


class ListRecommendationsFilter(BaseModel):
    field: "FilterField"
    include: Optional[bool] = Field(None, description="Flag to specify if the filter should be included or excluded.")
    operator: "FilterOperator"
    values: list[str]

    model_config = {'populate_by_name': True}


class Locale(StrEnum):
    AR_AE = "ar_AE"
    CS_CZ = "cs_CZ"
    DE_DE = "de_DE"
    EN_AE = "en_AE"
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


class ListRecommendationsRequest(BaseModel):
    filters: Optional[list["ListRecommendationsFilter"]] = None
    locale: Optional["Locale"] = Field(None, description="This will control the language of preference returned for the summary field.")
    max_results: Optional[int] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to retrieve the next page of results.")

    model_config = {'populate_by_name': True}


class ListRecommendationsResponse(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to retrieve the next page of results.")
    recommendations: list["Recommendation"]
    total_results: int = Field(..., alias="totalResults", description="Total number of results.")

    model_config = {'populate_by_name': True}


class UpdateBudgetRuleDurationDateRange(BaseModel):
    end_date: Optional[str] = Field(None, alias="endDate", description="End date of the budget rule in YYYY-MM-DD format. The end date is inclusive.")

    model_config = {'populate_by_name': True}


class UpdateBudgetRuleDuration(BaseModel):
    date_range_type_duration: Optional["UpdateBudgetRuleDurationDateRange"] = Field(None, alias="dateRangeTypeDuration")

    model_config = {'populate_by_name': True}


class UpdateBudgetRuleDetails(BaseModel):
    budget_increase_by: Optional["BudgetRuleIncreaseBy"] = Field(None, alias="budgetIncreaseBy")
    duration: Optional["UpdateBudgetRuleDuration"] = None
    performance_measure_condition: Optional["BudgetRulePerformanceMeasureCondition"] = Field(None, alias="performanceMeasureCondition")
    rule_name: Optional[str] = Field(None, alias="ruleName", description="Name of the budget rule. Required to be unique within a campaign.")

    model_config = {'populate_by_name': True}


class UpdateBudgetRule(BaseModel):
    """Can only be updated for recommendations with recommendationType NEW_CAMPAIGN_BUDGET_RULE or CAMPAIGN_BUDGET_RULE."""
    rule_details: "UpdateBudgetRuleDetails" = Field(..., alias="ruleDetails")

    model_config = {'populate_by_name': True}


class UpdateRuleBasedBidding(BaseModel):
    """Can only be updated for recommendations with recommendationType NEW_CAMPAIGN_BIDDING_RULE or CAMPAIGN_BIDDING_RULE."""
    recommended_rule_roas: float = Field(..., alias="recommendedRuleRoas")

    model_config = {'populate_by_name': True}


class UpdateRecommendationRequest(BaseModel):
    budget_rule: Optional["UpdateBudgetRule"] = Field(None, alias="budgetRule")
    recommended_value: Optional[str] = Field(None, alias="recommendedValue", description="Recommended value of the recommendation. Type of data expected for each recommendation type: | Recommendation type | Dat")
    rule_based_bidding: Optional["UpdateRuleBasedBidding"] = Field(None, alias="ruleBasedBidding")

    model_config = {'populate_by_name': True}

