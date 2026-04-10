"""Auto-generated Pydantic models. Do not edit manually.

Source: SponsoredDisplay_prod_3p.json
Title:  Sponsored Display
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



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


class BudgetChangeType(StrEnum):
    PERCENT = "PERCENT"


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


class ComparisonOperator(StrEnum):
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"


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


class RecurrenceType(StrEnum):
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"


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


class SDRuleType(StrEnum):
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


class SDBudgetRuleDetails(BaseModel):
    """Object representing details of a budget rule for SD campaign"""
    budget_increase_by: Optional["budgetIncreaseBy"] = Field(None, alias="budgetIncreaseBy")
    duration: Optional["RuleDuration"] = None
    name: Optional[str] = Field(None, description="The budget rule name. Required to be unique within a campaign.")
    performance_measure_condition: Optional["PerformanceMeasureCondition"] = Field(None, alias="performanceMeasureCondition")
    recurrence: Optional["Recurrence"] = None
    rule_type: Optional["SDRuleType"] = Field(None, alias="ruleType")

    model_config = {'populate_by_name': True}


class CreateSDBudgetRulesRequest(BaseModel):
    budget_rules_details: Optional[list["SDBudgetRuleDetails"]] = Field(None, alias="budgetRulesDetails", description="A list of budget rule details.")

    model_config = {'populate_by_name': True}


class DisassociateAssociatedBudgetRuleResponse(BaseModel):
    pass


class state(StrEnum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"


class SDBudgetRule(BaseModel):
    created_date: Optional[float] = Field(None, alias="createdDate", description="Epoch time of budget rule creation. Read-only.")
    last_updated_date: Optional[float] = Field(None, alias="lastUpdatedDate", description="Epoch time of budget rule update. Read-only.")
    rule_details: Optional["SDBudgetRuleDetails"] = Field(None, alias="ruleDetails")
    rule_id: str = Field(..., alias="ruleId", description="The budget rule identifier.")
    rule_state: Optional["state"] = Field(None, alias="ruleState")
    rule_status: Optional[str] = Field(None, alias="ruleStatus", description="The budget rule status. Read-only.")

    model_config = {'populate_by_name': True}


class GetSDBudgetRuleResponse(BaseModel):
    budget_rule: Optional["SDBudgetRule"] = Field(None, alias="budgetRule")

    model_config = {'populate_by_name': True}


class GetSDBudgetRulesForAdvertiserResponse(BaseModel):
    budget_rules_for_advertiser_response: Optional[list["SDBudgetRule"]] = Field(None, alias="budgetRulesForAdvertiserResponse", description="A list of rules created by the advertiser.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` ")

    model_config = {'populate_by_name': True}


class LocationPredicate(StrEnum):
    LOCATION = "location"


class LocationExpression(BaseModel):
    type_: Optional["LocationPredicate"] = Field(None, alias="type")
    value: Optional[str] = Field(None, description="The location identifier. Currently, this can correspond to either a 'city', 'state', 'dma', 'postal code', or 'country'.")

    model_config = {'populate_by_name': True}


class RecommendedHeadline(BaseModel):
    """Recommended Headline in response object. Recommended headline will be locale specific, i.e. for an asin input in ES, Recommended headline will be in ES."""
    headline: Optional[str] = Field(None, description="String that contains Recommended headline.")
    headline_id: Optional[str] = Field(None, alias="headlineId", description="Unique Id of Recommended headline.")

    model_config = {'populate_by_name': True}


class SDAPIError(BaseModel):
    """The error response object."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SDASIN(BaseModel):
    """Amazon Standard Identification Number"""
    pass


class SDLandingPageType(StrEnum):
    OFF_AMAZON_LINK = "OFF_AMAZON_LINK"


class SDLandingPageURL(BaseModel):
    """The URL where customers will land after clicking on its link. Must be provided if landingPageType field is set. This field is not supported when using asin field. ||Specifications| |------------------"""
    pass


class SDAdvertisedProduct(BaseModel):
    """Product that advertisers wants to advertise. Recommendations will be made for specified products. SDAdvertisedProduct can only contain either asins or landing pages. If landingPageUrl is used, there c"""
    asin: Optional["SDASIN"] = None
    landing_page_type: Optional["SDLandingPageType"] = Field(None, alias="landingPageType")
    landing_page_url: Optional["SDLandingPageURL"] = Field(None, alias="landingPageURL")

    model_config = {'populate_by_name': True}


class SDAudience(BaseModel):
    """The audience identifier"""
    pass


class SDAudienceCategory(StrEnum):
    IN_MARKET = "In-market"
    INTEREST = "Interest"
    LIFE_EVENT = "Life event"
    LIFESTYLE = "Lifestyle"


class SDAudienceRecommendation(BaseModel):
    """A recommended standard Amazon audience to target ads on"""
    audience: Optional["SDAudience"] = None
    name: Optional[str] = Field(None, description="The Amazon audience name")
    rank: Optional[int] = Field(None, description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation")

    model_config = {'populate_by_name': True}


class SDAudienceCategoryRecommendations(BaseModel):
    """List of recommended standard Amazon audience targets of a specific audience category"""
    audiences: Optional[list["SDAudienceRecommendation"]] = Field(None, description="List of recommended standard Amazon audience targets")
    category: Optional["SDAudienceCategory"] = None

    model_config = {'populate_by_name': True}


class SDAudienceRecommendations(BaseModel):
    audiences: Optional[list["SDAudienceCategoryRecommendations"]] = Field(None, description="List of recommended audience targets, broken down by audience category")

    model_config = {'populate_by_name': True}


class SDBidOptimizationV32(StrEnum):
    CLICKS = "clicks"
    CONVERSIONS = "conversions"
    REACH = "reach"


class SDBidRecommendationV31(BaseModel):
    """A recommended bid range to use for a target."""
    range_lower: float = Field(..., alias="rangeLower", description="The lowest recommended bid to use to win an ad placement for this target.")
    range_upper: float = Field(..., alias="rangeUpper", description="The highest recommended bid to use to win an ad placement for this target.")
    recommended: float = Field(..., description="The recommended bid to use to win an ad placement for this target.")

    model_config = {'populate_by_name': True}


class SDBrandSafetyDenyListDomainType(StrEnum):
    APP = "APP"
    CREATOR = "CREATOR"
    WEBSITE = "WEBSITE"


class SDBrandSafetyDenyListDomain(BaseModel):
    name: str = Field(..., description="The website or app identifier. This can be in the form of full domain (eg. 'example.com' or 'example.net'), or mobile ap")
    type_: "SDBrandSafetyDenyListDomainType" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class SDBrandSafetyDenyListDomainState(StrEnum):
    ARCHIVED = "ARCHIVED"
    ENABLED = "ENABLED"


class SDBrandSafetyDenyListDomainUpdateResultStatus(StrEnum):
    FAILURE = "FAILURE"
    SUCCESS = "SUCCESS"


class SDBrandSafetyDenyListProcessedDomain(BaseModel):
    created_at: Optional[str] = Field(None, alias="createdAt", description="The date time the domain was created at. Format: YYYY-MM-ddT:HH:mm:ssZ")
    domain_id: Optional[int] = Field(None, alias="domainId", description="The identifier of the Brand Safety List domain.")
    last_modified: Optional[str] = Field(None, alias="lastModified", description="The date time the domain was last modified. Format: YYYY-MM-ddT:HH:mm:ssZ")
    name: Optional[str] = Field(None, description="The website or app identifier. This can be in the form of full domain (eg. 'example.com' or 'example.net'), or mobile ap")
    state: Optional["SDBrandSafetyDenyListDomainState"] = None
    type_: Optional["SDBrandSafetyDenyListDomainType"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class SDBrandSafetyGetResponsePagination(BaseModel):
    """Response pagination info for Brand Safety Deny List GET requests"""
    limit: Optional[int] = Field(None, description="The maximum number of deny list domains returned from GET request.")
    offset: Optional[int] = Field(None, description="The number of deny list domains skipped.")
    total: Optional[int] = Field(None, description="The total number of deny list domains created by the advertiser.")

    model_config = {'populate_by_name': True}


class SDBrandSafetyGetResponse(BaseModel):
    """Response for Brand Safety Deny List GET requests"""
    domains: Optional[list["SDBrandSafetyDenyListProcessedDomain"]] = Field(None, description="List of Brand Safety Deny List Domains")
    pagination: Optional["SDBrandSafetyGetResponsePagination"] = None

    model_config = {'populate_by_name': True}


class SDBrandSafetyRequestStatusStatus(StrEnum):
    COMPLETED = "COMPLETED"
    FAILURE = "FAILURE"
    IN_PROGRESS = "IN_PROGRESS"


class SDBrandSafetyRequestStatus(BaseModel):
    request_id: Optional[str] = Field(None, alias="requestId", description="Request ID")
    status: Optional[SDBrandSafetyRequestStatusStatus] = Field(None, description="The status of the request")
    status_details: Optional[str] = Field(None, alias="statusDetails", description="Details related to the request status")
    timestamp: Optional[str] = Field(None, description="Request timestamp")

    model_config = {'populate_by_name': True}


class SDBrandSafetyListRequestStatusResponse(BaseModel):
    """List of all requests' status."""
    request_status_list: Optional[list["SDBrandSafetyRequestStatus"]] = Field(None, alias="requestStatusList", description="List of all requests' status.")

    model_config = {'populate_by_name': True}


class SDBrandSafetyPostRequest(BaseModel):
    """POST Request for Brand Safety"""
    domains: list["SDBrandSafetyDenyListDomain"]

    model_config = {'populate_by_name': True}


class SDBrandSafetyRequestResult(BaseModel):
    details: Optional[str] = Field(None, description="A human-readable description of the response.")
    domain_id: Optional[int] = Field(None, alias="domainId", description="The identifier of the Brand Safety Deny List Domain.")
    name: Optional[str] = Field(None, description="The website or app identifier.")
    status: Optional["SDBrandSafetyDenyListDomainUpdateResultStatus"] = None

    model_config = {'populate_by_name': True}


class SDBrandSafetyRequestResultsResponse(BaseModel):
    results: Optional[list["SDBrandSafetyRequestResult"]] = Field(None, description="A list of results for the given requestId")

    model_config = {'populate_by_name': True}


class SDBrandSafetyRequestStatusResponse(BaseModel):
    """The status of the request."""
    request_status: Optional["SDBrandSafetyRequestStatus"] = Field(None, alias="requestStatus")

    model_config = {'populate_by_name': True}


class SDBrandSafetyUpdateResponse(BaseModel):
    """Response for Brand Safety POST and DELETE requests"""
    request_id: Optional[str] = Field(None, alias="requestId", description="The identifier of the request")

    model_config = {'populate_by_name': True}


class SDSevenDaysMissedOpportunities(BaseModel):
    end_date: Optional[str] = Field(None, alias="endDate", description="End date of the missed opportunities date range (YYYY-MM-DD).")
    estimated_missed_clicks_lower: Optional[int] = Field(None, alias="estimatedMissedClicksLower", description="Lower bound of the estimated missed clicks.")
    estimated_missed_clicks_upper: Optional[int] = Field(None, alias="estimatedMissedClicksUpper", description="Upper bound of the estimated missed clicks.")
    estimated_missed_impressions_lower: Optional[int] = Field(None, alias="estimatedMissedImpressionsLower", description="Lower bound of the estimated missed impressions.")
    estimated_missed_impressions_upper: Optional[int] = Field(None, alias="estimatedMissedImpressionsUpper", description="Upper bound of the estimated missed impressions.")
    estimated_missed_sales_lower: Optional[float] = Field(None, alias="estimatedMissedSalesLower", description="Lower bound of the estimated missed sales. This will be in local currency.")
    estimated_missed_sales_upper: Optional[float] = Field(None, alias="estimatedMissedSalesUpper", description="Upper bound of the estimated missed sales. This will be in local currency.")
    estimated_missed_viewable_impressions_lower: Optional[int] = Field(None, alias="estimatedMissedViewableImpressionsLower", description="Lower bound of the estimated missed viewable impressions for vCPM campaigns.")
    estimated_missed_viewable_impressions_upper: Optional[int] = Field(None, alias="estimatedMissedViewableImpressionsUpper", description="Upper bound of the estimated missed viewable impressions for vCPM campaigns.")
    percent_time_in_budget: Optional[float] = Field(None, alias="percentTimeInBudget", description="Percentage of time the campaign is active with a budget.")
    start_date: Optional[str] = Field(None, alias="startDate", description="Start date of the missed opportunities date range (YYYY-MM-DD).")

    model_config = {'populate_by_name': True}


class SDBudgetRecommendation(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="Campaign id.")
    index: int = Field(..., description="Correlate the recommendation to the campaign index in the request. Zero-based.")
    seven_days_missed_opportunities: "SDSevenDaysMissedOpportunities" = Field(..., alias="sevenDaysMissedOpportunities")
    suggested_budget: float = Field(..., alias="suggestedBudget", description="Recommended budget for the campaign. This will be in local currency.")

    model_config = {'populate_by_name': True}


class SDBudgetRecommendationError(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="Campaign id.")
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")
    index: int = Field(..., description="Correlate the recommendation to the campaign index in the request. Zero-based.")

    model_config = {'populate_by_name': True}


class SDBudgetRecommendationsRequest(BaseModel):
    """Request for budget recommendations."""
    campaign_ids: list[str] = Field(..., alias="campaignIds", description="A list of campaign ids for which to get budget recommendations and missed opportunities.")

    model_config = {'populate_by_name': True}


class SDBudgetRecommendationsResponse(BaseModel):
    budget_recommendations_error_results: list["SDBudgetRecommendationError"] = Field(..., alias="budgetRecommendationsErrorResults", description="List of errors that occurred when generating budget recommendation.")
    budget_recommendations_success_results: list["SDBudgetRecommendation"] = Field(..., alias="budgetRecommendationsSuccessResults", description="List of successful budget recommendation for campaigns.")

    model_config = {'populate_by_name': True}


class SDCategory(BaseModel):
    """The category identifier"""
    pass


class SDCategoryRecommendationTargetableasincountrange(BaseModel):
    """The range of ASINs available within the category catalogue"""
    range_lower: Optional[int] = Field(None, alias="rangeLower")
    range_upper: Optional[int] = Field(None, alias="rangeUpper")

    model_config = {'populate_by_name': True}


class SDCategoryRecommendation(BaseModel):
    """A recommended category to target ads on"""
    category: Optional["SDCategory"] = None
    name: Optional[str] = Field(None, description="The category name")
    path: Optional[list[str]] = Field(None, description="The path of the category within the category catalogue")
    rank: Optional[int] = Field(None, description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation")
    targetable_asin_count_range: Optional["SDCategoryRecommendationTargetableasincountrange"] = Field(None, alias="targetableAsinCountRange", description="The range of ASINs available within the category catalogue")

    model_config = {'populate_by_name': True}


class SDCategoryRecommendationV33Targetableasincountrange(BaseModel):
    """The range of ASINs available within the category catalogue"""
    range_lower: Optional[int] = Field(None, alias="rangeLower")
    range_upper: Optional[int] = Field(None, alias="rangeUpper")

    model_config = {'populate_by_name': True}


class SDCategoryRecommendationV33(BaseModel):
    """A recommended category to target ads on"""
    category: Optional["SDCategory"] = None
    name: Optional[str] = Field(None, description="The category name")
    path: Optional[list[str]] = Field(None, description="The path of the category within the category catalogue")
    rank: Optional[int] = Field(None, description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation")
    targetable_asin_count_range: Optional["SDCategoryRecommendationV33Targetableasincountrange"] = Field(None, alias="targetableAsinCountRange", description="The range of ASINs available within the category catalogue")
    translated_name: Optional[str] = Field(None, alias="translatedName", description="The translated category name by requested locale, field will not be provided if locale is not provided or campaign local")
    translated_path: Optional[list[str]] = Field(None, alias="translatedPath", description="The translated path of the category within the category catalogue by requested locale, field will not be provided if loc")

    model_config = {'populate_by_name': True}


class SDCategoryRecommendations(BaseModel):
    categories: Optional[list["SDCategoryRecommendation"]] = Field(None, description="List of recommended category targets")

    model_config = {'populate_by_name': True}


class SDCategoryRecommendationsV33(BaseModel):
    categories: Optional[list["SDCategoryRecommendationV33"]] = Field(None, description="List of recommended category targets")

    model_config = {'populate_by_name': True}


class SDContentCategory(BaseModel):
    """The content category value"""
    pass


class SDContentCategoryRecommendations(BaseModel):
    """A recommended content category to target ads on"""
    content_category: Optional["SDContentCategory"] = Field(None, alias="contentCategory")
    name: Optional[str] = Field(None, description="The content category name")
    rank: Optional[int] = Field(None, description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation")

    model_config = {'populate_by_name': True}


class SDContentTargetingPredicateV31Type(StrEnum):
    CONTENTCATEGORYSAMEAS = "contentCategorySameAs"


class SDContentTargetingPredicateV31(BaseModel):
    """A predicate to match against in the content targeting expression."""
    type_: SDContentTargetingPredicateV31Type = Field(..., alias="type")
    value: str = Field(..., description="The value to be targeted.")

    model_config = {'populate_by_name': True}


class SDCostTypeV31(StrEnum):
    CPC = "cpc"
    VCPM = "vcpm"


class SDCreativeType(StrEnum):
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class SDErrorResponse(BaseModel):
    code: Optional[str] = Field(None, description="The HTTP status code of the response")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SDGetAssociatedCampaignsResponse(BaseModel):
    associated_campaigns: Optional[list["AssociatedCampaign"]] = Field(None, alias="associatedCampaigns", description="A list of campaigns that are associated to this budget rule.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` ")

    model_config = {'populate_by_name': True}


class SDGoalProduct(BaseModel):
    """A product an advertisers wants to advertise. Recommendations will be made for specified goal products."""
    asin: "SDASIN"

    model_config = {'populate_by_name': True}


class SDHeadlineRecommendationAccessDeniedExceptionCode(StrEnum):
    ACCESS_DENIED = "ACCESS_DENIED"


class SDHeadlineRecommendationAccessDeniedException(BaseModel):
    code: Optional[SDHeadlineRecommendationAccessDeniedExceptionCode] = Field(None, description="AccessDeniedErrorCode.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class SDHeadlineRecommendationIdentifierNotfoundExceptionCode(StrEnum):
    IDENTIFIER_NOT_FOUND = "IDENTIFIER_NOT_FOUND"


class SDHeadlineRecommendationIdentifierNotfoundException(BaseModel):
    code: Optional[SDHeadlineRecommendationIdentifierNotfoundExceptionCode] = Field(None, description="IdentiferNotFoundErrorCode.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class SDHeadlineRecommendationInternalServerExceptionCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class SDHeadlineRecommendationInternalServerException(BaseModel):
    code: Optional[SDHeadlineRecommendationInternalServerExceptionCode] = Field(None, description="InternalErrorCode.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class SDHeadlineRecommendationMarsThrottlingExceptionCode(StrEnum):
    THROTTLED = "THROTTLED"


class SDHeadlineRecommendationMarsThrottlingException(BaseModel):
    code: Optional[SDHeadlineRecommendationMarsThrottlingExceptionCode] = Field(None, description="ThrottledErrorCode.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class SDHeadlineRecommendationRequestAdformat(StrEnum):
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"


class SDHeadlineRecommendationRequest(BaseModel):
    """Request structure of SD headline recommendation API."""
    ad_format: Optional[SDHeadlineRecommendationRequestAdformat] = Field(None, alias="adFormat")
    asins: Optional[list[str]] = Field(None, description="An array of ASINs associated with the creative.")
    max_num_recommendations: Optional[float] = Field(None, alias="maxNumRecommendations", description="Maximum number of recommendations that API should return. Response will [0, maxNumRecommendations] recommendations (reco")

    model_config = {'populate_by_name': True}


class SDHeadlineRecommendationResponse(BaseModel):
    """Response structure of SD headline recommendation API."""
    recommendations: Optional[list["RecommendedHeadline"]] = Field(None, description="Recommendations are sorted, i.e., more suitable headline has lesser array index value.")
    request_id: Optional[str] = Field(None, alias="requestId", description="An identifier for request made which is generated by server.")

    model_config = {'populate_by_name': True}


class SDHeadlineRecommendationSchemaValidationExceptionCode(StrEnum):
    INVALID_ARGUMENT = "INVALID_ARGUMENT"


class SDHeadlineRecommendationSchemaValidationException(BaseModel):
    code: Optional[SDHeadlineRecommendationSchemaValidationExceptionCode] = Field(None, description="InvalidArgumentErrorCode.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class SDListAssociatedBudgetRulesResponse(BaseModel):
    associated_rules: Optional[list["SDBudgetRule"]] = Field(None, alias="associatedRules", description="A list of associated budget rules.")

    model_config = {'populate_by_name': True}


class SDLocale(StrEnum):
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


class SDProductRecommendation(BaseModel):
    """A recommended product to target ads on"""
    asin: Optional["SDASIN"] = None
    rank: Optional[int] = Field(None, description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation")

    model_config = {'populate_by_name': True}


class SDProductRecommendationV32(BaseModel):
    """A recommended product to target ads on"""
    advertised_asins: Optional[list["SDASIN"]] = Field(None, alias="advertisedAsins", description="The top advertised products this recommendation is made for.")
    asin: Optional["SDASIN"] = None
    rank: Optional[int] = Field(None, description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation")

    model_config = {'populate_by_name': True}


class SDProductRecommendationsV31(BaseModel):
    products: Optional[list["SDProductRecommendation"]] = Field(None, description="List of recommended product targets")

    model_config = {'populate_by_name': True}


class SDProductRecommendationsV32(BaseModel):
    products: Optional[list["SDProductRecommendationV32"]] = Field(None, description="List of recommended product targets")

    model_config = {'populate_by_name': True}


class SDProductTargetingRecommendationsSuccess(BaseModel):
    """Recommendation results for product targeting."""
    code: Optional[str] = Field(None, description="HTTP status code 200 indicating a successful response for product recommendations.")
    name: Optional[str] = Field(None, description="The theme name specified in the request.")
    recommendations: Optional[list["SDProductRecommendationV32"]] = Field(None, description="A list of recommended products.")

    model_config = {'populate_by_name': True}


class SDProductTargetingThemeExpressionType(StrEnum):
    ASINBRANDSAMEAS = "asinBrandSameAs"
    ASINGLANCEVIEWSGREATERTHAN = "asinGlanceViewsGreaterThan"
    ASINPRICEGREATERTHAN = "asinPriceGreaterThan"
    ASINREVIEWRATINGLESSTHAN = "asinReviewRatingLessThan"


class SDProductTargetingThemeExpression(BaseModel):
    """The expression used to define the product targeting theme."""
    type_: SDProductTargetingThemeExpressionType = Field(..., alias="type", description="The product targeting grammar used to define the targeting theme. Note asinAsBestSeller is currently not supported.")

    model_config = {'populate_by_name': True}


class SDProductTargetingRecommendationsSuccessV34(BaseModel):
    """Recommendation results for product targeting."""
    code: Optional[str] = Field(None, description="HTTP status code 200 indicating a successful response for product recommendations.")
    expression: Optional[list["SDProductTargetingThemeExpression"]] = Field(None, description="A list of expressions defining the product targeting theme. The list will define an AND operator on different expression")
    name: Optional[str] = Field(None, description="The theme name specified in the request.")
    recommendations: Optional[list["SDProductRecommendationV32"]] = Field(None, description="A list of recommended products.")

    model_config = {'populate_by_name': True}


class SDProductTargetingTheme(BaseModel):
    """Product targeting theme definitions."""
    expression: list["SDProductTargetingThemeExpression"] = Field(..., description="A list of expressions defining the product targeting theme. The list will define an AND operator on different expression")
    name: str = Field(..., description="This is the meaningful theme name which will be used as a unique identifier across various themes in the same request. T")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsFailure(BaseModel):
    """A targeting recommendation failure record."""
    code: Optional[str] = Field(None, description="HTTP status code indicating a failure response for targeting recomendations.")
    error_message: Optional[str] = Field(None, alias="errorMessage", description="A human friendly error message indicating the failure reasons.")
    name: Optional[str] = Field(None, description="The theme name specified in the request. If the themes field is not provided in the request, the value of this field wil")

    model_config = {'populate_by_name': True}


class SDProductThemeRecommendations(BaseModel):
    """A list of product targeting theme recommendations."""
    pass


class SDTargetingRecommendationsFailureV34(BaseModel):
    """A targeting recommendation failure record."""
    code: Optional[str] = Field(None, description="HTTP status code indicating a failure response for targeting recomendations.")
    error_message: Optional[str] = Field(None, alias="errorMessage", description="A human friendly error message indicating the failure reasons.")
    expression: Optional[list["SDProductTargetingThemeExpression"]] = Field(None, description="A list of expressions that failed to be applied in the product targeting theme.")
    name: Optional[str] = Field(None, description="The theme name specified in the request. If the themes field is not provided in the request, the value of this field wil")

    model_config = {'populate_by_name': True}


class SDProductThemeRecommendationsV34(BaseModel):
    """A list of product targeting theme recommendations."""
    pass


class SDRecommendationType(StrEnum):
    PRODUCT = "PRODUCT"


class SDRecommendationTypeV31(StrEnum):
    CATEGORY = "CATEGORY"
    PRODUCT = "PRODUCT"


class SDRecommendationTypeV32(StrEnum):
    AUDIENCE = "AUDIENCE"
    CATEGORY = "CATEGORY"
    PRODUCT = "PRODUCT"


class SDRecommendationTypeV33(StrEnum):
    AUDIENCE = "AUDIENCE"
    CATEGORY = "CATEGORY"
    CONTENT_CATEGORY = "CONTENT_CATEGORY"
    PRODUCT = "PRODUCT"


class SDTactic(StrEnum):
    T00001 = "T00001"
    T00010 = "T00010"
    T00020 = "T00020"
    REMARKETING = "remarketing"


class SDTacticV31(StrEnum):
    T00001 = "T00001"
    T00010 = "T00010"
    T00020 = "T00020"
    T00030 = "T00030"
    REMARKETING = "remarketing"


class SDTargetingPredicateBaseV31Type(StrEnum):
    ASINAGERANGESAMEAS = "asinAgeRangeSameAs"
    ASINBRANDSAMEAS = "asinBrandSameAs"
    ASINCATEGORYSAMEAS = "asinCategorySameAs"
    ASINGENRESAMEAS = "asinGenreSameAs"
    ASINISPRIMESHIPPINGELIGIBLE = "asinIsPrimeShippingEligible"
    ASINPRICEBETWEEN = "asinPriceBetween"
    ASINPRICEGREATERTHAN = "asinPriceGreaterThan"
    ASINPRICELESSTHAN = "asinPriceLessThan"
    ASINREVIEWRATINGBETWEEN = "asinReviewRatingBetween"
    ASINREVIEWRATINGGREATERTHAN = "asinReviewRatingGreaterThan"
    ASINREVIEWRATINGLESSTHAN = "asinReviewRatingLessThan"
    AUDIENCESAMEAS = "audienceSameAs"
    EXACTPRODUCT = "exactProduct"
    LOOKBACK = "lookback"
    NEGATIVE = "negative"
    RELATEDPRODUCT = "relatedProduct"
    SIMILARPRODUCT = "similarProduct"


class SDTargetingPredicateBaseV31(BaseModel):
    """A predicate to match against inside the TargetingPredicateNested component (only applicable to Audience targeting - T00030).  * All IDs passed for category and brand-targeting predicates must be valid"""
    type_: SDTargetingPredicateBaseV31Type = Field(..., alias="type")
    value: Optional[str] = Field(None, description="The value to be targeted.")

    model_config = {'populate_by_name': True}


class SDTargetingPredicateNestedV31Type(StrEnum):
    AUDIENCE = "audience"
    PURCHASES = "purchases"
    VIEWS = "views"


class SDTargetingPredicateNestedV31(BaseModel):
    """A behavioral event and list of targeting predicates that represents an Audience to target (only applicable to Audience targeting - T00030).  * For auto ASIN-grain targeting, the value array must conta"""
    type_: SDTargetingPredicateNestedV31Type = Field(..., alias="type")
    value: list["SDTargetingPredicateBaseV31"]

    model_config = {'populate_by_name': True}


class SDTargetingPredicateV31Type(StrEnum):
    ASINAGERANGESAMEAS = "asinAgeRangeSameAs"
    ASINBRANDSAMEAS = "asinBrandSameAs"
    ASINCATEGORYSAMEAS = "asinCategorySameAs"
    ASINGENRESAMEAS = "asinGenreSameAs"
    ASINISPRIMESHIPPINGELIGIBLE = "asinIsPrimeShippingEligible"
    ASINPRICEBETWEEN = "asinPriceBetween"
    ASINPRICEGREATERTHAN = "asinPriceGreaterThan"
    ASINPRICELESSTHAN = "asinPriceLessThan"
    ASINREVIEWRATINGBETWEEN = "asinReviewRatingBetween"
    ASINREVIEWRATINGGREATERTHAN = "asinReviewRatingGreaterThan"
    ASINREVIEWRATINGLESSTHAN = "asinReviewRatingLessThan"
    ASINSAMEAS = "asinSameAs"
    SIMILARPRODUCT = "similarProduct"


class SDTargetingPredicateV31(BaseModel):
    """A predicate to match against in the Targeting Expression (only applicable to Product targeting - T00020).  * All IDs passed for category and brand-targeting predicates must be valid IDs in the Amazon """
    type_: SDTargetingPredicateV31Type = Field(..., alias="type")
    value: Optional[str] = Field(None, description="The value to be targeted.")

    model_config = {'populate_by_name': True}


class SDTargetExpressionV31(BaseModel):
    pass


class SDTargetExpressionV32(BaseModel):
    pass


class SDTargetingExpressionV31(BaseModel):
    """The targeting expression to match against.  ------- Applicable to Product targeting (T00020) ------- * A 'TargetingExpression' in a Product targeting Campaign can only contain 'TargetingPredicate' com"""
    pass


class SDTargetingClauseV31Expressiontype(StrEnum):
    AUTO = "auto"
    MANUAL = "manual"


class SDTargetingClauseV31(BaseModel):
    """The targeting clause"""
    expression: "SDTargetingExpressionV31"
    expression_type: SDTargetingClauseV31Expressiontype = Field(..., alias="expressionType", description="Tactic T00020 ad groups only allow manual targeting.")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsRequestV31Targetingclauses(BaseModel):
    targeting_clause: "SDTargetingClauseV31" = Field(..., alias="targetingClause")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsRequestV31(BaseModel):
    """Request for targeting bid recommendations."""
    products: Optional[list["SDGoalProduct"]] = Field(None, description="A list of products to tailor bid recommendations for category and audience based targeting clauses.")
    targeting_clauses: list["SDTargetingBidRecommendationsRequestV31Targetingclauses"] = Field(..., alias="targetingClauses", description="A list of targeting clauses to receive bid recommendations for.")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsRequestV32Targetingclauses(BaseModel):
    targeting_clause: "SDTargetingClauseV31" = Field(..., alias="targetingClause")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsRequestV32(BaseModel):
    """Request for targeting bid recommendations."""
    bid_optimization: "SDBidOptimizationV32" = Field(..., alias="bidOptimization")
    cost_type: "SDCostTypeV31" = Field(..., alias="costType")
    products: Optional[list["SDGoalProduct"]] = Field(None, description="A list of products to tailor bid recommendations for category and audience based targeting clauses.")
    targeting_clauses: list["SDTargetingBidRecommendationsRequestV32Targetingclauses"] = Field(..., alias="targetingClauses", description="A list of targeting clauses to receive bid recommendations for.")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsRequestV33Targetingclauses(BaseModel):
    targeting_clause: "SDTargetingClauseV31" = Field(..., alias="targetingClause")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsRequestV33(BaseModel):
    """Request for targeting bid recommendations."""
    bid_optimization: "SDBidOptimizationV32" = Field(..., alias="bidOptimization")
    cost_type: "SDCostTypeV31" = Field(..., alias="costType")
    creative_type: Optional["SDCreativeType"] = Field(None, alias="creativeType")
    products: Optional[list["SDGoalProduct"]] = Field(None, description="A list of products to tailor bid recommendations for category and audience based targeting clauses.")
    targeting_clauses: list["SDTargetingBidRecommendationsRequestV33Targetingclauses"] = Field(..., alias="targetingClauses", description="A list of targeting clauses to receive bid recommendations for.")

    model_config = {'populate_by_name': True}


class SDTargetingExpressionV32(BaseModel):
    """The targeting expression to match against.  ------- Applicable to contextual targeting (T00020) ------- * A 'TargetingExpression' in a contextual targeting campaign can only contain 'TargetingPredicat"""
    pass


class SDTargetingClauseV32Expressiontype(StrEnum):
    AUTO = "auto"
    MANUAL = "manual"


class SDTargetingClauseV32(BaseModel):
    """The targeting clause"""
    expression: "SDTargetingExpressionV32"
    expression_type: SDTargetingClauseV32Expressiontype = Field(..., alias="expressionType", description="Tactic T00020 ad groups only allow manual targeting.")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsRequestV34Targetingclauses(BaseModel):
    targeting_clause: "SDTargetingClauseV32" = Field(..., alias="targetingClause")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsRequestV34(BaseModel):
    """Request for targeting bid recommendations."""
    bid_optimization: "SDBidOptimizationV32" = Field(..., alias="bidOptimization")
    cost_type: "SDCostTypeV31" = Field(..., alias="costType")
    creative_type: Optional["SDCreativeType"] = Field(None, alias="creativeType")
    products: Optional[list["SDGoalProduct"]] = Field(None, description="A list of products to tailor bid recommendations for category and audience based targeting clauses. This array must cont")
    targeting_clauses: list["SDTargetingBidRecommendationsRequestV34Targetingclauses"] = Field(..., alias="targetingClauses", description="A list of targeting clauses to receive bid recommendations for.")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsResponseItemFailureV31(BaseModel):
    """Failed bid recommendation response."""
    code: str = Field(..., description="The HTTP status code of this item.")
    details: str = Field(..., description="A human-readable description of this item on error.")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsResponseItemSuccessV31(BaseModel):
    """A recommended bid range to use for a target."""
    pass


class SDTargetingBidRecommendationsResponseV31(BaseModel):
    """Response to a request for targeting bid recommendations."""
    bid_recommendations: Any = Field(..., alias="bidRecommendations")
    cost_type: "SDCostTypeV31" = Field(..., alias="costType")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsResponseV32(BaseModel):
    """Response to a request for targeting bid recommendations."""
    bid_optimization: "SDBidOptimizationV32" = Field(..., alias="bidOptimization")
    bid_recommendations: Any = Field(..., alias="bidRecommendations")
    cost_type: "SDCostTypeV31" = Field(..., alias="costType")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendations(BaseModel):
    """A collection of targeting recommendations. Results will be sorted with strongest recommendations in the beginning."""
    products: Optional[list["SDProductRecommendation"]] = Field(None, description="List of recommended product targets")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsProducts(BaseModel):
    """A list of products for which to get targeting recommendations"""
    pass


class SDTargetingRecommendationsProductsV31(BaseModel):
    """A list of products for which to get targeting recommendations. This array can only contain either asins or landing pages. If landingPageUrl is used,  there can only be one item in the array for each r"""
    pass


class SDTargetingRecommendationsRequest(BaseModel):
    """Request for targeting recommendations"""
    products: list["SDGoalProduct"] = Field(..., description="A list of products for which to get targeting recommendations")
    tactic: "SDTactic"
    type_filter: list["SDRecommendationType"] = Field(..., alias="typeFilter", description="A filter to indicate which types of recommendations to request.")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsTypeFilterV31(BaseModel):
    """A filter to indicate which types of recommendations to request."""
    pass


class SDTargetingRecommendationsRequestV31(BaseModel):
    """Request for targeting recommendations"""
    products: "SDTargetingRecommendationsProducts"
    tactic: "SDTacticV31"
    type_filter: "SDTargetingRecommendationsTypeFilterV31" = Field(..., alias="typeFilter")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsThemes(BaseModel):
    """The themes used to refine the recommendations. Currently only product targeting themes are supported."""
    product: Optional[list["SDProductTargetingTheme"]] = Field(None, description="A list of themes for product targeting recommendations. If this list is empty, the service will return all the current a")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsRequestV32(BaseModel):
    """Request for targeting recommendations"""
    products: "SDTargetingRecommendationsProducts"
    tactic: "SDTacticV31"
    themes: Optional["SDTargetingRecommendationsThemes"] = None
    type_filter: "SDTargetingRecommendationsTypeFilterV31" = Field(..., alias="typeFilter")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsTypeFilterV32(BaseModel):
    """A filter to indicate which types of recommendations to request."""
    pass


class SDTargetingRecommendationsRequestV33(BaseModel):
    """Request for targeting recommendations"""
    products: "SDTargetingRecommendationsProducts"
    tactic: "SDTacticV31"
    themes: Optional["SDTargetingRecommendationsThemes"] = None
    type_filter: "SDTargetingRecommendationsTypeFilterV32" = Field(..., alias="typeFilter")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsRequestV34(BaseModel):
    """Request for targeting recommendations"""
    products: "SDTargetingRecommendationsProducts"
    tactic: "SDTacticV31"
    themes: Optional["SDTargetingRecommendationsThemes"] = None
    type_filter: "SDTargetingRecommendationsTypeFilterV32" = Field(..., alias="typeFilter")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsTypeFilterV33(BaseModel):
    """A filter to indicate which types of recommendations to request."""
    pass


class SDTargetingRecommendationsRequestV35Categorytype(StrEnum):
    PURCHASES = "purchases"
    VIEWS = "views"


class SDTargetingRecommendationsRequestV35(BaseModel):
    """Request for targeting recommendations"""
    category_type: Optional[SDTargetingRecommendationsRequestV35Categorytype] = Field(None, alias="categoryType", description="This field is optional unless the field locationExpression is present in the request. It is used for category audience t")
    location_expression: Optional[list["LocationExpression"]] = Field(None, alias="locationExpression", description="This optional field is used to specify the locations used in SD location targeting for non-Amazon sellers only at the mo")
    products: "SDTargetingRecommendationsProductsV31"
    tactic: "SDTacticV31"
    themes: Optional["SDTargetingRecommendationsThemes"] = None
    type_filter: "SDTargetingRecommendationsTypeFilterV33" = Field(..., alias="typeFilter")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsResponse(BaseModel):
    """Response to a request for targeting recommendations"""
    recommendations: Optional["SDTargetingRecommendations"] = None

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsV31(BaseModel):
    """A collection of targeting recommendations. Results will be sorted with strongest recommendations in the beginning."""
    pass


class SDTargetingRecommendationsResponseV31(BaseModel):
    """Response to a request for targeting recommendations"""
    recommendations: Optional["SDTargetingRecommendationsV31"] = None

    model_config = {'populate_by_name': True}


class SDThemeRecommendations(BaseModel):
    products: Optional["SDProductThemeRecommendations"] = None

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsV32(BaseModel):
    """For v3.2 the service will continue to return the recommendations returned for v3.1 in products field, and return recommendations for product targeting themes in themes field."""
    pass


class SDTargetingRecommendationsResponseV32(BaseModel):
    """Response body for targeting recommendations v3.2."""
    recommendations: Optional["SDTargetingRecommendationsV32"] = None

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsV33(BaseModel):
    """For v3.3 the service will continue to return the recommendations returned for v3.2, and return audience recommendations if requested."""
    pass


class SDTargetingRecommendationsResponseV33(BaseModel):
    """Response to a request for targeting recommendations"""
    recommendations: Optional["SDTargetingRecommendationsV33"] = None

    model_config = {'populate_by_name': True}


class SDThemeRecommendationsV34(BaseModel):
    products: Optional["SDProductThemeRecommendationsV34"] = None

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsV34(BaseModel):
    """For v3.4 the service will continue to return the recommendations returned for v3.2, return audience recommendations if requested, and return the theme expression used in product targeting if requested"""
    audiences: Optional[list["SDAudienceCategoryRecommendations"]] = Field(None, description="List of recommended audience targets, broken down by audience category")
    categories: Optional[list["SDCategoryRecommendationV33"]] = Field(None, description="List of recommended category targets")
    products: Optional[list["SDProductRecommendationV32"]] = Field(None, description="List of recommended product targets")
    themes: Optional["SDThemeRecommendationsV34"] = None

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsResponseV34(BaseModel):
    """Response to a request for targeting recommendations"""
    recommendations: Optional["SDTargetingRecommendationsV34"] = None

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsV35(BaseModel):
    """For v3.5 the service will continue to return the recommendations returned for v3.4, return Entertainment targeting recommendations if requested and return asin-less recommendations if a landing page U"""
    audiences: Optional[list["SDAudienceCategoryRecommendations"]] = Field(None, description="List of recommended audience targets, broken down by audience category")
    categories: Optional[list["SDCategoryRecommendationV33"]] = Field(None, description="List of recommended category targets")
    content_categories: Optional[list["SDContentCategoryRecommendations"]] = Field(None, alias="contentCategories", description="List of recommended entertainment targets")
    products: Optional[list["SDProductRecommendationV32"]] = Field(None, description="List of recommended product targets")
    themes: Optional["SDThemeRecommendationsV34"] = None

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsResponseV35(BaseModel):
    """Response to a request for targeting recommendations"""
    recommendations: Optional["SDTargetingRecommendationsV35"] = None

    model_config = {'populate_by_name': True}


class SdDefaultError(BaseModel):
    """The error response object"""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SnapshotRequestStatefilter(StrEnum):
    ARCHIVED = "archived"
    ENABLED = "enabled"
    ENABLED__PAUSED = "enabled, paused"
    ENABLED_ARCHIVED = "enabled,archived"
    ENABLED_PAUSED_ARCHIVED = "enabled,paused,archived"
    PAUSED = "paused"
    PAUSED_ARCHIVED = "paused,archived"


class SnapshotRequestTacticfilter(StrEnum):
    T00010 = "T00010"
    T00010_T00020 = "T00010,T00020"
    T00010_T00020_REMARKETING = "T00010,T00020,remarketing"
    T00010_REMARKETING = "T00010,remarketing"
    T00020 = "T00020"
    T00020_REMARKETING = "T00020,remarketing"
    REMARKETING = "remarketing"


class SnapshotRequest(BaseModel):
    state_filter: Optional[SnapshotRequestStatefilter] = Field(None, alias="stateFilter", description="Optional. Restricts results to entities with state within the specified comma-separated list. The stateFilter not presen")
    tactic_filter: Optional[SnapshotRequestTacticfilter] = Field(None, alias="tacticFilter", description="Optional. Restricts results to entities with the advertising tactic associated with the campaign within the specified co")

    model_config = {'populate_by_name': True}


class SnapshotResponseRecordtype(StrEnum):
    ADGROUPS = "adGroups"
    CAMPAIGNS = "campaigns"
    NEGATIVETARGETS = "negativeTargets"
    PRODUCTADS = "productAds"
    TARGETS = "targets"


class SnapshotResponseStatus(StrEnum):
    FAILURE = "FAILURE"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"


class SnapshotResponse(BaseModel):
    expiration: Optional[float] = Field(None, description="The epoch time for expiration of the snapshot file. It's only available if status is SUCCESS.")
    file_size: Optional[float] = Field(None, alias="fileSize", description="The size of the snapshot file in bytes. It's only available if status is SUCCESS.")
    location: Optional[str] = Field(None, description="The URI for the snapshot. It's only available if status is SUCCESS.")
    record_type: Optional[SnapshotResponseRecordtype] = Field(None, alias="recordType", description="The record type of the snapshot file.")
    snapshot_id: Optional[str] = Field(None, alias="snapshotId", description="The identifier of the snapshot that was requested.")
    status: Optional[SnapshotResponseStatus] = Field(None, description="The status of the generation of the snapshot.")
    status_details: Optional[str] = Field(None, alias="statusDetails", description="Status information of the call if SUCCESS or FAILURE status, optional for IN_PROCESS.")

    model_config = {'populate_by_name': True}


class UpdateBudgetRulesResponse(BaseModel):
    responses: Optional[list["BudgetRuleResponse"]] = None

    model_config = {'populate_by_name': True}


class UpdateSDBudgetRulesRequest(BaseModel):
    """Request object for updating budget rule for SD campaign"""
    budget_rules_details: Optional[list["SDBudgetRule"]] = Field(None, alias="budgetRulesDetails", description="A list of budget rule details.")

    model_config = {'populate_by_name': True}

