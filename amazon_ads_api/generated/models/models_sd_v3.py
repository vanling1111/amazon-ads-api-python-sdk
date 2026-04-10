"""Auto-generated Pydantic models. Do not edit manually.

Source: SponsoredDisplay_v3_openapi.yaml
Title:  Amazon Ads API for Sponsored Display
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class TacticReport(StrEnum):
    T00020 = "T00020"
    T00030 = "T00030"


class Segment(StrEnum):
    MATCHEDTARGET = "matchedTarget"


class Tactic(StrEnum):
    T00020 = "T00020"
    T00030 = "T00030"


class CreativeType(StrEnum):
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class BaseCampaignBudgettype(StrEnum):
    DAILY = "daily"


class BaseCampaignCosttype(StrEnum):
    CPC = "cpc"
    VCPM = "vcpm"


class BaseCampaignState(StrEnum):
    ENABLED = "enabled"
    PAUSED = "paused"
    ARCHIVED = "archived"


class BaseCampaign(BaseModel):
    name: Optional[str] = Field(None, description="The name of the campaign.")
    budget_type: Optional[BaseCampaignBudgettype] = Field(None, alias="budgetType", description="The time period over which the amount specified in the `budget` property is allocated.")
    budget: Optional[float] = Field(None, description="The amount of the budget.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The YYYYMMDD start date of the campaign. The date must be today or in the future.")
    end_date: Optional[str] = Field(None, alias="endDate", description="The YYYYMMDD end date of the campaign.")
    cost_type: Optional[BaseCampaignCosttype] = Field(None, alias="costType", description="Determines how the campaign will bid and charge. |Name|Description| |----|----------| |cpc |[Default] The performance of")
    state: Optional[BaseCampaignState] = Field(None, description="The state of the campaign.")
    portfolio_id: Optional[int] = Field(None, alias="portfolioId", description="Identifier of the portfolio that will be associated with the campaign. If null then the campaign will be disassociated f")

    model_config = {'populate_by_name': True}


class CampaignId(BaseModel):
    """The identifier of the campaign."""
    pass


class RuleBasedBudget(BaseModel):
    is_processing: Optional[bool] = Field(None, alias="isProcessing")
    applicable_rule_name: Optional[str] = Field(None, alias="applicableRuleName")
    value: Optional[float] = None
    applicable_rule_id: Optional[str] = Field(None, alias="applicableRuleId")

    model_config = {'populate_by_name': True}


class Campaign(BaseModel):
    pass


class CreateCampaign(BaseModel):
    pass


class UpdateCampaign(BaseModel):
    pass


class CampaignResponse(BaseModel):
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    description: Optional[str] = Field(None, description="A human-readable description of the response.")
    campaign_id: Optional["CampaignId"] = Field(None, alias="campaignId")

    model_config = {'populate_by_name': True}


class CampaignResponseExBudgettype(StrEnum):
    DAILY = "daily"


class CampaignResponseExState(StrEnum):
    ENABLED = "enabled"
    PAUSED = "paused"
    ARCHIVED = "archived"


class CampaignResponseExServingstatus(StrEnum):
    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ACCOUNT_OUT_OF_BUDGET = "ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    PENDING_START_DATE = "PENDING_START_DATE"
    ENDED = "ENDED"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    INELIGIBLE = "INELIGIBLE"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET"


class CampaignResponseExCosttype(StrEnum):
    CPC = "cpc"
    VCPM = "vcpm"


class CampaignResponseEx(BaseModel):
    campaign_id: Optional[float] = Field(None, alias="campaignId", description="The identifier of the campaign.")
    name: Optional[str] = Field(None, description="The name of the campaign.")
    tactic: Optional["Tactic"] = None
    budget_type: Optional[CampaignResponseExBudgettype] = Field(None, alias="budgetType", description="The time period over which the amount specified in the `budget` property is allocated.")
    budget: Optional[float] = Field(None, description="The amount of the budget.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The YYYYMMDD start date of the campaign. The date must be today or in the future.")
    end_date: Optional[str] = Field(None, alias="endDate", description="The YYYYMMDD end date of the campaign.")
    state: Optional[CampaignResponseExState] = Field(None, description="The state of the campaign.")
    portfolio_id: Optional[int] = Field(None, alias="portfolioId", description="Identifier of the portfolio that will be associated with the campaign. If null then the campaign will be disassociated f")
    serving_status: Optional[CampaignResponseExServingstatus] = Field(None, alias="servingStatus", description="The status of the campaign.")
    cost_type: Optional[CampaignResponseExCosttype] = Field(None, alias="costType", description="Determines how the campaign will bid and charge. |Name|Description| |----|----------|-----------| |cpc |[Default] The pe")
    creation_date: Optional[int] = Field(None, alias="creationDate", description="Epoch date the campaign was created.")
    last_updated_date: Optional[int] = Field(None, alias="lastUpdatedDate", description="Epoch date of the last update to any property associated with the campaign.")
    rule_based_budget: Optional["RuleBasedBudget"] = Field(None, alias="ruleBasedBudget")

    model_config = {'populate_by_name': True}


class BaseAdGroupBidoptimization(StrEnum):
    REACH = "reach"
    CLICKS = "clicks"
    CONVERSIONS = "conversions"


class BaseAdGroupState(StrEnum):
    ENABLED = "enabled"
    PAUSED = "paused"
    ARCHIVED = "archived"


class BaseAdGroup(BaseModel):
    name: Optional[str] = Field(None, description="The name of the ad group.")
    campaign_id: Optional["CampaignId"] = Field(None, alias="campaignId")
    default_bid: Optional[float] = Field(None, alias="defaultBid", description="The amount of the default bid associated with the ad group. Used if no bid is specified.")
    bid_optimization: Optional[BaseAdGroupBidoptimization] = Field(None, alias="bidOptimization", description="Bid Optimization for the Adgroup. Default behavior is to optimize for clicks. |Name|CostType|Description| |----|--------")
    state: Optional[BaseAdGroupState] = Field(None, description="The state of the ad group.")

    model_config = {'populate_by_name': True}


class AdGroupId(BaseModel):
    """The identifier of the ad group."""
    pass


class AdGroup(BaseModel):
    pass


class CreateAdGroup(BaseModel):
    pass


class UpdateAdGroup(BaseModel):
    pass


class AdGroupResponse(BaseModel):
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    description: Optional[str] = Field(None, description="A human-readable description of the response.")
    ad_group_id: Optional["AdGroupId"] = Field(None, alias="adGroupId")

    model_config = {'populate_by_name': True}


class CreativeTypeInCreativeResponse(StrEnum):
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class AdGroupResponseExState(StrEnum):
    ENABLED = "enabled"
    PAUSED = "paused"
    ARCHIVED = "archived"


class AdGroupResponseExServingstatus(StrEnum):
    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ACCOUNT_OUT_OF_BUDGET = "ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    PENDING_START_DATE = "PENDING_START_DATE"
    ENDED = "ENDED"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    ADGROUP_POLICING_PENDING_REVIEW = "ADGROUP_POLICING_PENDING_REVIEW"
    ADGROUP_POLICING_CREATIVE_REJECTED = "ADGROUP_POLICING_CREATIVE_REJECTED"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    INELIGIBLE = "INELIGIBLE"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET"


class AdGroupResponseExBidoptimization(StrEnum):
    REACH = "reach"
    CLICKS = "clicks"
    CONVERSIONS = "conversions"


class AdGroupResponseEx(BaseModel):
    """Object containing an extended set of data fields for an Ad Group."""
    ad_group_id: Optional[float] = Field(None, alias="adGroupId", description="The identifier of the ad group.")
    name: Optional[str] = Field(None, description="The name of the ad group.")
    campaign_id: Optional[float] = Field(None, alias="campaignId", description="The identifier of the campaign that this ad group is associated with.")
    default_bid: Optional[float] = Field(None, alias="defaultBid", description="The amount of the default bid associated with the ad group. Used if no bid is specified.")
    state: Optional[AdGroupResponseExState] = Field(None, description="The delivery state of the ad group.")
    tactic: Optional["Tactic"] = None
    creative_type: Optional["CreativeTypeInCreativeResponse"] = Field(None, alias="creativeType")
    serving_status: Optional[AdGroupResponseExServingstatus] = Field(None, alias="servingStatus", description="The status of the ad group.")
    bid_optimization: Optional[AdGroupResponseExBidoptimization] = Field(None, alias="bidOptimization", description="Bid optimization type for the Adgroup. Default behavior is to optimize for clicks. Note, reach, clicks are only accepted")
    creation_date: Optional[int] = Field(None, alias="creationDate", description="Epoch time the ad group was created.")
    last_updated_date: Optional[int] = Field(None, alias="lastUpdatedDate", description="Epoch time any property in the ad group was last updated.")

    model_config = {'populate_by_name': True}


class BaseProductAdState(StrEnum):
    ENABLED = "enabled"
    PAUSED = "paused"
    ARCHIVED = "archived"


class BaseProductAd(BaseModel):
    state: Optional[BaseProductAdState] = Field(None, description="The state of the campaign associated with the product ad.")

    model_config = {'populate_by_name': True}


class LandingPageURL(BaseModel):
    """The URL where customers will land after clicking on its link. Must be provided if a LandingPageType is set. Please note that if a single product ad sets the landing page url, only one product ad can b"""
    pass


class LandingPageType(StrEnum):
    STORE = "STORE"
    MOMENT = "MOMENT"
    OFF_AMAZON_LINK = "OFF_AMAZON_LINK"


class AdId(BaseModel):
    """The identifier of the product ad."""
    pass


class AdName(BaseModel):
    """The name of the ad. Note that this field is not supported when using ASIN or SKU fields."""
    pass


class ProductAd(BaseModel):
    pass


class CreateProductAd(BaseModel):
    pass


class UpdateProductAd(BaseModel):
    pass


class ProductAdResponse(BaseModel):
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    description: Optional[str] = Field(None, description="A human-readable description of the response.")
    ad_id: Optional[float] = Field(None, alias="adId", description="The identifier of the ad.")

    model_config = {'populate_by_name': True}


class ProductAdResponseExState(StrEnum):
    ENABLED = "enabled"
    PAUSED = "paused"
    ARCHIVED = "archived"


class ProductAdResponseExServingstatus(StrEnum):
    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ACCOUNT_OUT_OF_BUDGET = "ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    PENDING_START_DATE = "PENDING_START_DATE"
    ENDED = "ENDED"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    AD_STATUS_LIVE = "AD_STATUS_LIVE"
    AD_STATUS_PAUSED = "AD_STATUS_PAUSED"
    AD_STATUS_ARCHIVED = "AD_STATUS_ARCHIVED"
    MISSING_IMAGE = "MISSING_IMAGE"
    MISSING_DECORATION = "MISSING_DECORATION"
    NOT_BUYABLE = "NOT_BUYABLE"
    NOT_IN_BUYBOX = "NOT_IN_BUYBOX"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    NOT_IN_POLICY = "NOT_IN_POLICY"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    INELIGIBLE = "INELIGIBLE"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET"


class ProductAdResponseEx(BaseModel):
    ad_id: Optional[float] = Field(None, alias="adId", description="The identifier of the ad.")
    ad_group_id: Optional[float] = Field(None, alias="adGroupId", description="The identifier of the ad group associated with the ad.")
    campaign_id: Optional[float] = Field(None, alias="campaignId", description="The identifier of the campaign associated with the ad.")
    landing_page_url: Optional["LandingPageURL"] = Field(None, alias="landingPageURL")
    landing_page_type: Optional["LandingPageType"] = Field(None, alias="landingPageType")
    ad_name: Optional["AdName"] = Field(None, alias="adName")
    asin: Optional[str] = Field(None, description="The ASIN of the product being advertised. This parameter is included in the response for sellers and vendors.")
    sku: Optional[str] = Field(None, description="The SKU of the product being advertised. This parameter is included in the response for sellers.")
    state: Optional[ProductAdResponseExState] = Field(None, description="The state of the product ad.")
    serving_status: Optional[ProductAdResponseExServingstatus] = Field(None, alias="servingStatus", description="The status of the product ad.")
    creation_date: Optional[int] = Field(None, alias="creationDate", description="Epoch date the product ad was created.")
    last_updated_date: Optional[int] = Field(None, alias="lastUpdatedDate", description="Epoch date of the last update to any property associated with the product ad.")

    model_config = {'populate_by_name': True}


class TargetingPredicateType(StrEnum):
    ASINSAMEAS = "asinSameAs"
    ASINCATEGORYSAMEAS = "asinCategorySameAs"
    ASINBRANDSAMEAS = "asinBrandSameAs"
    ASINPRICEBETWEEN = "asinPriceBetween"
    ASINPRICEGREATERTHAN = "asinPriceGreaterThan"
    ASINPRICELESSTHAN = "asinPriceLessThan"
    ASINREVIEWRATINGLESSTHAN = "asinReviewRatingLessThan"
    ASINREVIEWRATINGGREATERTHAN = "asinReviewRatingGreaterThan"
    ASINREVIEWRATINGBETWEEN = "asinReviewRatingBetween"
    ASINISPRIMESHIPPINGELIGIBLE = "asinIsPrimeShippingEligible"
    ASINAGERANGESAMEAS = "asinAgeRangeSameAs"
    ASINGENRESAMEAS = "asinGenreSameAs"
    SIMILARPRODUCT = "similarProduct"


class TargetingPredicate(BaseModel):
    """A predicate to match against in the targeting expression (only applicable to contextual targeting - T00020).  * All IDs passed for category and brand-targeting predicates must be valid IDs in the Amaz"""
    type_: Optional[TargetingPredicateType] = Field(None, alias="type")
    value: Optional[str] = Field(None, description="The value to be targeted.")

    model_config = {'populate_by_name': True}


class ContentTargetingPredicateType(StrEnum):
    CONTENTCATEGORYSAMEAS = "contentCategorySameAs"


class ContentTargetingPredicate(BaseModel):
    """A predicate to match against in the content targeting expression."""
    type_: Optional[ContentTargetingPredicateType] = Field(None, alias="type")
    value: Optional[str] = Field(None, description="The value to be targeted.  The following table shows all possible values of the `contentCategorySameAs` predicate. | Cat")

    model_config = {'populate_by_name': True}


class TargetingPredicateLegacyType(StrEnum):
    ASINSAMEAS = "asinSameAs"
    ASINCATEGORYSAMEAS = "asinCategorySameAs"
    ASINBRANDSAMEAS = "asinBrandSameAs"
    ASINPRICEBETWEEN = "asinPriceBetween"
    ASINPRICEGREATERTHAN = "asinPriceGreaterThan"
    ASINPRICELESSTHAN = "asinPriceLessThan"
    ASINREVIEWRATINGLESSTHAN = "asinReviewRatingLessThan"
    ASINREVIEWRATINGGREATERTHAN = "asinReviewRatingGreaterThan"
    ASINREVIEWRATINGBETWEEN = "asinReviewRatingBetween"
    SIMILARPRODUCT = "similarProduct"
    EXACTPRODUCT = "exactProduct"
    ASINISPRIMESHIPPINGELIGIBLE = "asinIsPrimeShippingEligible"
    ASINAGERANGESAMEAS = "asinAgeRangeSameAs"
    ASINGENRESAMEAS = "asinGenreSameAs"


class TargetingPredicateLegacyEventtype(StrEnum):
    VIEWS = "views"


class TargetingPredicateLegacy(BaseModel):
    type_: Optional[TargetingPredicateLegacyType] = Field(None, alias="type")
    value: Optional[str] = Field(None, description="The value to be targeted.")
    event_type: Optional[TargetingPredicateLegacyEventtype] = Field(None, alias="eventType", description="The type of event that the value applies to. Only available for similarProduct and exactProduct currently. * views event")

    model_config = {'populate_by_name': True}


class TargetingPredicateBaseType(StrEnum):
    ASINCATEGORYSAMEAS = "asinCategorySameAs"
    ASINBRANDSAMEAS = "asinBrandSameAs"
    ASINPRICEBETWEEN = "asinPriceBetween"
    ASINPRICEGREATERTHAN = "asinPriceGreaterThan"
    ASINPRICELESSTHAN = "asinPriceLessThan"
    ASINREVIEWRATINGLESSTHAN = "asinReviewRatingLessThan"
    ASINREVIEWRATINGGREATERTHAN = "asinReviewRatingGreaterThan"
    ASINREVIEWRATINGBETWEEN = "asinReviewRatingBetween"
    SIMILARPRODUCT = "similarProduct"
    EXACTPRODUCT = "exactProduct"
    ASINISPRIMESHIPPINGELIGIBLE = "asinIsPrimeShippingEligible"
    ASINAGERANGESAMEAS = "asinAgeRangeSameAs"
    ASINGENRESAMEAS = "asinGenreSameAs"
    AUDIENCESAMEAS = "audienceSameAs"
    LOOKBACK = "lookback"
    NEGATIVE = "negative"
    RELATEDPRODUCT = "relatedProduct"


class TargetingPredicateBase(BaseModel):
    """A predicate to match against inside the TargetingPredicateNested component (only applicable to audience targeting - T00030).  * All IDs passed for category and brand-targeting predicates must be valid"""
    type_: Optional[TargetingPredicateBaseType] = Field(None, alias="type")
    value: Optional[str] = Field(None, description="The value to be targeted.")

    model_config = {'populate_by_name': True}


class TargetingPredicateNestedType(StrEnum):
    VIEWS = "views"
    AUDIENCE = "audience"
    PURCHASES = "purchases"


class TargetingPredicateNested(BaseModel):
    """A behavioral event and list of targeting predicates that represents an audience to target (only applicable to audience targeting - T00030).  * For manual ASIN-grain targeting, the value array must con"""
    type_: Optional[TargetingPredicateNestedType] = Field(None, alias="type")
    value: Optional[list["TargetingPredicateBase"]] = None

    model_config = {'populate_by_name': True}


class TargetingExpression(BaseModel):
    """The targeting expression to match against.  ------- Applicable to contextual or content targeting (T00020) ------- * A 'TargetingExpression' in a contextual targeting campaign can contain 'TargetingPr"""
    pass


class CreateTargetingExpression(BaseModel):
    """The targeting expression to match against.  ------- Applicable to contextual targeting (T00020) ------- * A 'TargetingExpression' in a contextual targeting campaign can only contain 'TargetingPredicat"""
    pass


class BaseTargetingClauseState(StrEnum):
    ENABLED = "enabled"
    PAUSED = "paused"
    ARCHIVED = "archived"


class BaseTargetingClause(BaseModel):
    state: Optional[BaseTargetingClauseState] = None
    bid: Optional[float] = Field(None, description="The bid will override the adGroup bid if specified. This field is not used for negative targeting clauses. The bid must ")

    model_config = {'populate_by_name': True}


class TargetId(BaseModel):
    pass


class SDForecastRequestTargetingClause(BaseModel):
    pass


class TargetingClause(BaseModel):
    pass


class UpdateTargetingClause(BaseModel):
    pass


class CreateTargetingClause(BaseModel):
    pass


class TargetResponse(BaseModel):
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    description: Optional[str] = Field(None, description="A human-readable description of the response.")
    target_id: Optional["TargetId"] = Field(None, alias="targetId")

    model_config = {'populate_by_name': True}


class TargetingClauseExState(StrEnum):
    ENABLED = "enabled"
    PAUSED = "paused"
    ARCHIVED = "archived"


class TargetingClauseExExpressiontype(StrEnum):
    AUTO = "auto"
    MANUAL = "manual"


class TargetingClauseExServingstatus(StrEnum):
    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ACCOUNT_OUT_OF_BUDGET = "ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    PENDING_START_DATE = "PENDING_START_DATE"
    ENDED = "ENDED"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    TARGET_STATUS_LIVE = "TARGET_STATUS_LIVE"
    TARGET_STATUS_PAUSED = "TARGET_STATUS_PAUSED"
    TARGET_STATUS_ARCHIVED = "TARGET_STATUS_ARCHIVED"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    INELIGIBLE = "INELIGIBLE"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET"


class TargetingClauseEx(BaseModel):
    target_id: Optional[float] = Field(None, alias="targetId")
    ad_group_id: Optional[float] = Field(None, alias="adGroupId")
    campaign_id: Optional[float] = Field(None, alias="campaignId")
    state: Optional[TargetingClauseExState] = None
    expression_type: Optional[TargetingClauseExExpressiontype] = Field(None, alias="expressionType")
    bid: Optional[float] = Field(None, description="If a value for `bid` is specified, it overrides the current adGroup bid. When using vcpm costType. $1 is the minimum bid")
    expression: Optional["TargetingExpression"] = None
    resolved_expression: Optional["TargetingExpression"] = Field(None, alias="resolvedExpression")
    serving_status: Optional[TargetingClauseExServingstatus] = Field(None, alias="servingStatus", description="The status of the target.")
    creation_date: Optional[int] = Field(None, alias="creationDate", description="Epoch date the target was created.")
    last_updated_date: Optional[int] = Field(None, alias="lastUpdatedDate", description="Epoch date of the last update to any property associated with the target.")

    model_config = {'populate_by_name': True}


class BaseNegativeTargetingClauseState(StrEnum):
    ENABLED = "enabled"
    PAUSED = "paused"
    ARCHIVED = "archived"


class BaseNegativeTargetingClause(BaseModel):
    state: Optional[BaseNegativeTargetingClauseState] = None

    model_config = {'populate_by_name': True}


class NegativeTargetingExpressionType(StrEnum):
    ASINSAMEAS = "asinSameAs"
    ASINBRANDSAMEAS = "asinBrandSameAs"


class NegativeTargetingExpression(BaseModel):
    type_: Optional[NegativeTargetingExpressionType] = Field(None, alias="type", description="The intent type. See the [targeting topic](https://advertising.amazon.com/help#GQCBASRVERXSARL3) in the Amazon Ads suppo")
    value: Optional[str] = Field(None, description="The value to be negatively targeted. Used only in manual expressions.")

    model_config = {'populate_by_name': True}


class NegativeTargetingClause(BaseModel):
    pass


class CreateNegativeTargetingClause(BaseModel):
    pass


class UpdateNegativeTargetingClause(BaseModel):
    pass


class NegativeTargetingClauseExState(StrEnum):
    ENABLED = "enabled"
    PAUSED = "paused"
    ARCHIVED = "archived"


class NegativeTargetingClauseExExpressiontype(StrEnum):
    MANUAL = "manual"
    AUTO = "auto"


class NegativeTargetingClauseExExpressionType(StrEnum):
    ASINSAMEAS = "asinSameAs"
    ASINBRANDSAMEAS = "asinBrandSameAs"


class NegativeTargetingClauseExExpression(BaseModel):
    type_: Optional[NegativeTargetingClauseExExpressionType] = Field(None, alias="type", description="The intent type. See the [targeting topic](https://advertising.amazon.com/help#GQCBASRVERXSARL3) in the Amazon Ads suppo")
    value: Optional[str] = Field(None, description="The value to be negatively targeted. Used only in manual expressions.")

    model_config = {'populate_by_name': True}


class NegativeTargetingClauseExServingstatus(StrEnum):
    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ACCOUNT_OUT_OF_BUDGET = "ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    PENDING_START_DATE = "PENDING_START_DATE"
    ENDED = "ENDED"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    TARGET_STATUS_LIVE = "TARGET_STATUS_LIVE"
    TARGET_STATUS_PAUSED = "TARGET_STATUS_PAUSED"
    TARGET_STATUS_ARCHIVED = "TARGET_STATUS_ARCHIVED"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    INELIGIBLE = "INELIGIBLE"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET"


class NegativeTargetingClauseEx(BaseModel):
    target_id: Optional[float] = Field(None, alias="targetId")
    ad_group_id: Optional[float] = Field(None, alias="adGroupId")
    state: Optional[NegativeTargetingClauseExState] = None
    expression_type: Optional[NegativeTargetingClauseExExpressiontype] = Field(None, alias="expressionType")
    expression: Optional[list["NegativeTargetingClauseExExpression"]] = Field(None, description="The expression to negatively match against. * Only one brand may be specified per targeting expression. * Only one asin ")
    serving_status: Optional[NegativeTargetingClauseExServingstatus] = Field(None, alias="servingStatus", description="The status of the target.")
    creation_date: Optional[int] = Field(None, alias="creationDate", description="Epoch date the target was created.")
    last_updated_date: Optional[int] = Field(None, alias="lastUpdatedDate", description="Epoch date of the last update to any property associated with the target.")

    model_config = {'populate_by_name': True}


class ASIN(BaseModel):
    """Amazon Standard Identification Number"""
    pass


class GoalProduct(BaseModel):
    """A product an advertisers wants to advertise. Recommendations will be made for specified goal products."""
    asin: "ASIN"

    model_config = {'populate_by_name': True}


class ProductRecommendation(BaseModel):
    """A recommended product to target ads on"""
    asin: Optional["ASIN"] = None
    rank: Optional[int] = Field(None, description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation")

    model_config = {'populate_by_name': True}


class TargetingRecommendations(BaseModel):
    """A collection of targeting recommendations. Results will be sorted with strongest recommendations in the beginning."""
    products: Optional[list["ProductRecommendation"]] = Field(None, description="List of recommended product targets")

    model_config = {'populate_by_name': True}


class TargetingRecommendationsResponse(BaseModel):
    """Response to a request for targeting recommendations."""
    recommendations: Optional["TargetingRecommendations"] = None

    model_config = {'populate_by_name': True}


class RecommendationType(StrEnum):
    PRODUCT = "PRODUCT"


class TargetingRecommendationsRequest(BaseModel):
    """Request for targeting recommendations"""
    tactic: "Tactic"
    products: list["GoalProduct"] = Field(..., description="A list of products for which to get targeting recommendations")
    type_filter: list["RecommendationType"] = Field(..., alias="typeFilter", description="A filter to indicate which types of recommendations to request. T00030 only allow 'CATEGORY'.")

    model_config = {'populate_by_name': True}


class ReportRequest(BaseModel):
    report_date: Optional[str] = Field(None, alias="reportDate", description="Date in YYYYMMDD format. The report contains only metrics generated on the specified date. Note that the time zone used ")
    tactic: Optional["TacticReport"] = None
    segment: Optional["Segment"] = None
    metrics: Optional[str] = Field(None, description="A comma-separated list of the metrics to be included in the report.  Each report type supports different metrics. **To u")

    model_config = {'populate_by_name': True}


class ReportResponseRecordtype(StrEnum):
    CAMPAIGN = "CAMPAIGN"
    AD_GROUP = "AD_GROUP"
    PRODUCT_AD = "PRODUCT_AD"


class ReportResponseStatus(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class ReportResponse(BaseModel):
    report_id: Optional[str] = Field(None, alias="reportId", description="The identifier of the report.")
    record_type: Optional[ReportResponseRecordtype] = Field(None, alias="recordType", description="The type of report requested.")
    status: Optional[ReportResponseStatus] = Field(None, description="The build status of the report.")
    status_details: Optional[str] = Field(None, alias="statusDetails", description="A human-readable description of the current status.")
    location: Optional[str] = Field(None, description="The URI location of the report.")
    file_size: Optional[int] = Field(None, alias="fileSize", description="The size of the report file, in bytes.")
    expiration: Optional[int] = Field(None, description="Epoch date of the expiration of the URI in the `location` property.")

    model_config = {'populate_by_name': True}


class PatchDocumentOp(StrEnum):
    ADD = "add"
    REMOVE = "remove"
    REPLACE = "replace"


class PatchDocument(BaseModel):
    """JSONPatch request document."""
    op: PatchDocumentOp = Field(..., description="The JSONPatch operation type.")
    path: str = Field(..., description="A path constructed from the JSON object to be updated.")
    value: Optional[Union[str, float, int, bool, list[Any], dict[str, Any]]] = Field(None, description="The value used by the operation specified in the `op` field.")

    model_config = {'populate_by_name': True}


class PatchRequest(BaseModel):
    """JSONPatch request request object."""
    id_: str = Field(..., alias="id")
    request: list["PatchDocument"]

    model_config = {'populate_by_name': True}


class Background(BaseModel):
    """This field denotes background which are displayed on the ad. This field is optional and mutable."""
    color: Optional[str] = Field(None, description="The standard HTML hex color codes of the background (e.g. '#3cb371').")

    model_config = {'populate_by_name': True}


class BackgroundCreativeProperties(BaseModel):
    """User-customizable properties of a creative with background. Only supported for productAds with landingPageType of OFF_AMAZON_LINK."""
    backgrounds: Optional[list["Background"]] = Field(None, description="An optional collection of backgrounds which are displayed on the ad.")

    model_config = {'populate_by_name': True}


class ImageCroppingcoordinates(BaseModel):
    """Optional cropping coordinates to apply to the image."""
    top: int = Field(..., description="Pixel distance from the top edge of the cropping zone to the top edge of the original image.")
    left: int = Field(..., description="Pixel distance from the left edge of the cropping zone to the left edge of the original image.")
    width: int = Field(..., description="Pixel width of the cropping zone.")
    height: int = Field(..., description="Pixel height of the cropping zone.")

    model_config = {'populate_by_name': True}


class Image(BaseModel):
    """This field denotes image which is displayed on the ad. This can either be a brand logo or a custom image. This field is optional and mutable. For custom image, both rectCustomImage and squareCustomIma"""
    asset_id: str = Field(..., alias="assetId", description="The unique identifier of the image asset. This assetId comes from the Creative Asset Library.")
    asset_version: str = Field(..., alias="assetVersion", description="The identifier of the particular image assetversion.")
    cropping_coordinates: Optional["ImageCroppingcoordinates"] = Field(None, alias="croppingCoordinates", description="Optional cropping coordinates to apply to the image.")

    model_config = {'populate_by_name': True}


class LogoCreativeProperties(BaseModel):
    """User-customizable properties of a creative with a logo."""
    brand_logo: Optional["Image"] = Field(None, alias="brandLogo")

    model_config = {'populate_by_name': True}


class HeadlineCreativeProperties(BaseModel):
    """User-customizable properties of a creative with headline."""
    headline: Optional[str] = Field(None, description="A marketing phrase to display on the ad. This field is optional and mutable. Maximum number of characters allowed is 50.")
    has_terms_and_conditions: Optional[bool] = Field(None, alias="hasTermsAndConditions", description="Indicates that the ad promotes a free product or service (e.g., 'buy one get one free' or 'free one-month trial') and ha")
    original_headline: Optional[str] = Field(None, alias="originalHeadline", description="The original headline submitted by the advertiser. If 'consentToTranslate' is set to true and translation is SUCCESSFUL ")

    model_config = {'populate_by_name': True}


class Video(BaseModel):
    """This field denotes video which is displayed on the ad. This field is optional and mutable. A video asset must be provided for a VIDEO creative. Specific restrictions based on the video are listed in t"""
    asset_id: str = Field(..., alias="assetId", description="The unique identifier of the video asset. This assetId comes from the Creative Asset Library.")
    asset_version: str = Field(..., alias="assetVersion", description="The identifier of the particular video assetversion.")
    original_asset_id: Optional[str] = Field(None, alias="originalAssetId", description="The assetId of the original video submitted by the advertiser. If 'consentToTranslate' is set to true and translation is")
    original_asset_version: Optional[str] = Field(None, alias="originalAssetVersion", description="The asset version of the original video submitted by the advertiser. If 'consentToTranslate' is set to true and translat")

    model_config = {'populate_by_name': True}


class VideoCreativeProperties(BaseModel):
    """User-customizable properties of a video creative. Use either the 'video' property for a single video, OR one or more of the aspect-ratio-specific collections (squareVideos, horizontalVideos, verticalV"""
    video: Optional["Video"] = None
    square_videos: Optional[list["Video"]] = Field(None, alias="squareVideos", description="An optional collection of 1:1 square videos which are displayed on the ad. Currently, only one asset is supported in the")
    horizontal_videos: Optional[list["Video"]] = Field(None, alias="horizontalVideos", description="An optional collection of 16:9 horizontal videos which are displayed on the ad. Currently, only one asset is supported i")
    vertical_videos: Optional[list["Video"]] = Field(None, alias="verticalVideos", description="An optional collection of 9:16 vertical videos which are displayed on the ad. Currently, only one asset is supported in ")

    model_config = {'populate_by_name': True}


class CustomImageCreativeProperties(BaseModel):
    """User-customizable properties of a custom image creative."""
    rect_custom_image: Optional["Image"] = Field(None, alias="rectCustomImage")
    square_custom_image: Optional["Image"] = Field(None, alias="squareCustomImage")
    square_images: Optional[list["Image"]] = Field(None, alias="squareImages", description="An optional collection of 1:1 square images which are displayed on the ad.")
    horizontal_images: Optional[list["Image"]] = Field(None, alias="horizontalImages", description="An optional collection of 1.91:1 horizontal images which are displayed on the ad.")
    vertical_images: Optional[list["Image"]] = Field(None, alias="verticalImages", description="An optional collection of 9:16 vertical images which are displayed on the ad.")

    model_config = {'populate_by_name': True}


class CreativeProperties(BaseModel):
    """Select customizations on your creative from any combination of headline, logo, custom image and backgrounds."""
    pass


class CreativeModerationModerationstatus(StrEnum):
    APPROVED = "APPROVED"
    PENDING_REVIEW = "PENDING_REVIEW"
    REJECTED = "REJECTED"


class CreativeModerationPolicyviolationsViolatingheadlinecontentsTextevidenceViolatingtextposition(BaseModel):
    start: Optional[int] = Field(None, description="Zero-based index into the text in reviewedText where the text specified in violatingText starts")
    end: Optional[int] = Field(None, description="Zero-based index into the text in reviewedText where the text specified in violatingText ends")

    model_config = {'populate_by_name': True}


class CreativeModerationPolicyviolationsViolatingheadlinecontentsTextevidence(BaseModel):
    violating_text: Optional[str] = Field(None, alias="violatingText", description="The specific text determined to violate the specified policy in reviewedText")
    violating_text_position: Optional["CreativeModerationPolicyviolationsViolatingheadlinecontentsTextevidenceViolatingtextposition"] = Field(None, alias="violatingTextPosition")

    model_config = {'populate_by_name': True}


class CreativeModerationPolicyviolationsViolatingheadlinecontents(BaseModel):
    reviewed_text: Optional[str] = Field(None, alias="reviewedText", description="The specific text reviewed during moderation.")
    text_evidence: Optional[list["CreativeModerationPolicyviolationsViolatingheadlinecontentsTextevidence"]] = Field(None, alias="textEvidence")

    model_config = {'populate_by_name': True}


class CreativeModerationPolicyviolationsViolatingbrandlogocontentsImageevidencesViolatingimagecrop(BaseModel):
    top_left_x: Optional[int] = Field(None, alias="topLeftX", description="The top left X-coordinate of the content that violates the specfied policy within the image.")
    top_left_y: Optional[int] = Field(None, alias="topLeftY", description="The top left Y-coordinate of the content that violates the specfied policy within the image.")
    height: Optional[int] = Field(None, description="The height of the content that violates the specfied policy within the image.")
    width: Optional[int] = Field(None, description="The width of the content that violates the specfied policy within the image.")

    model_config = {'populate_by_name': True}


class CreativeModerationPolicyviolationsViolatingbrandlogocontentsImageevidences(BaseModel):
    violating_image_crop: Optional["CreativeModerationPolicyviolationsViolatingbrandlogocontentsImageevidencesViolatingimagecrop"] = Field(None, alias="violatingImageCrop")

    model_config = {'populate_by_name': True}


class CreativeModerationPolicyviolationsViolatingbrandlogocontents(BaseModel):
    reviewed_image_url: Optional[str] = Field(None, alias="reviewedImageUrl", description="Address of the image reviewed during moderation.")
    image_evidences: Optional[list["CreativeModerationPolicyviolationsViolatingbrandlogocontentsImageevidences"]] = Field(None, alias="imageEvidences")

    model_config = {'populate_by_name': True}


class CreativeModerationPolicyviolationsViolatingcustomimagecontentsImageevidencesViolatingimagecrop(BaseModel):
    top_left_x: Optional[int] = Field(None, alias="topLeftX", description="The top left X-coordinate of the content that violates the specfied policy within the image.")
    top_left_y: Optional[int] = Field(None, alias="topLeftY", description="The top left Y-coordinate of the content that violates the specfied policy within the image.")
    height: Optional[int] = Field(None, description="The height of the content that violates the specfied policy within the image.")
    width: Optional[int] = Field(None, description="The width of the content that violates the specfied policy within the image.")

    model_config = {'populate_by_name': True}


class CreativeModerationPolicyviolationsViolatingcustomimagecontentsImageevidences(BaseModel):
    violating_image_crop: Optional["CreativeModerationPolicyviolationsViolatingcustomimagecontentsImageevidencesViolatingimagecrop"] = Field(None, alias="violatingImageCrop")

    model_config = {'populate_by_name': True}


class CreativeModerationPolicyviolationsViolatingcustomimagecontents(BaseModel):
    reviewed_image_url: Optional[str] = Field(None, alias="reviewedImageUrl", description="Address of the image reviewed during moderation.")
    image_evidences: Optional[list["CreativeModerationPolicyviolationsViolatingcustomimagecontentsImageevidences"]] = Field(None, alias="imageEvidences")

    model_config = {'populate_by_name': True}


class CreativeModerationPolicyviolationsViolatingvideocontentsVideoevidencesViolatingvideoposition(BaseModel):
    start: Optional[int] = Field(None, description="Time at which policy violation within video asset starts.")
    end: Optional[int] = Field(None, description="Time at which policy violation within the video asset ends.")

    model_config = {'populate_by_name': True}


class CreativeModerationPolicyviolationsViolatingvideocontentsVideoevidences(BaseModel):
    violating_video_position: Optional["CreativeModerationPolicyviolationsViolatingvideocontentsVideoevidencesViolatingvideoposition"] = Field(None, alias="violatingVideoPosition")

    model_config = {'populate_by_name': True}


class CreativeModerationPolicyviolationsViolatingvideocontents(BaseModel):
    reviewed_video_url: Optional[str] = Field(None, alias="reviewedVideoUrl", description="Address of the video reviewed during moderation.")
    video_evidences: Optional[list["CreativeModerationPolicyviolationsViolatingvideocontentsVideoevidences"]] = Field(None, alias="videoEvidences")

    model_config = {'populate_by_name': True}


class CreativeModerationPolicyviolations(BaseModel):
    policy_description: Optional[str] = Field(None, alias="policyDescription", description="A human-readable description of the policy.")
    policy_link_url: Optional[str] = Field(None, alias="policyLinkUrl", description="Address of the policy documentation. Follow the link to learn more about the specified policy.")
    violating_headline_contents: Optional[list["CreativeModerationPolicyviolationsViolatingheadlinecontents"]] = Field(None, alias="violatingHeadlineContents", description="Information about the headline text that violates the specified policy.")
    violating_brand_logo_contents: Optional[list["CreativeModerationPolicyviolationsViolatingbrandlogocontents"]] = Field(None, alias="violatingBrandLogoContents", description="Information about the brand logo that violates the specified policy.")
    violating_custom_image_contents: Optional[list["CreativeModerationPolicyviolationsViolatingcustomimagecontents"]] = Field(None, alias="violatingCustomImageContents", description="Information about the custom image that violates the specified policy.")
    violating_video_contents: Optional[list["CreativeModerationPolicyviolationsViolatingvideocontents"]] = Field(None, alias="violatingVideoContents", description="Information about the video that violates the specified policy.")

    model_config = {'populate_by_name': True}


class CreativeModeration(BaseModel):
    """System generated Creative moderation."""
    creative_id: float = Field(..., alias="creativeId", description="Unique identifier of the creative.")
    creative_type: "CreativeTypeInCreativeResponse" = Field(..., alias="creativeType")
    moderation_status: CreativeModerationModerationstatus = Field(..., alias="moderationStatus", description="The moderation status of the creative. |Status|Description| |------|-----------| |APPROVED|Moderation for the creative i")
    eta_for_moderation: str = Field(..., alias="etaForModeration", description="Expected date and time by which moderation will be complete.")
    policy_violations: list["CreativeModerationPolicyviolations"] = Field(..., alias="policyViolations", description="A list of policy violations for a creative that has failed moderation.")

    model_config = {'populate_by_name': True}


class CreativeTypeInCreativeRequest(StrEnum):
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class CreativeModerationstatus(StrEnum):
    APPROVED = "APPROVED"
    PENDING_REVIEW = "PENDING_REVIEW"
    REJECTED = "REJECTED"


class Creative(BaseModel):
    """Creative model."""
    creative_id: float = Field(..., alias="creativeId", description="Unique identifier of the creative.")
    ad_group_id: "AdGroupId" = Field(..., alias="adGroupId")
    creative_type: "CreativeTypeInCreativeResponse" = Field(..., alias="creativeType")
    properties: "CreativeProperties"
    moderation_status: CreativeModerationstatus = Field(..., alias="moderationStatus", description="The moderation status of the creative")

    model_config = {'populate_by_name': True}


class PreviewCreativeModel(BaseModel):
    """Creative model for preview."""
    creative_type: Optional["CreativeTypeInCreativeRequest"] = Field(None, alias="creativeType")
    properties: Optional["CreativeProperties"] = None

    model_config = {'populate_by_name': True}


class CreativeUpdate(BaseModel):
    """Creative update model."""
    creative_id: float = Field(..., alias="creativeId", description="Unique identifier of the creative.")
    creative_type: Optional["CreativeTypeInCreativeRequest"] = Field(None, alias="creativeType")
    properties: "CreativeProperties"

    model_config = {'populate_by_name': True}


class CreateCreative(BaseModel):
    """Creative create model."""
    ad_group_id: float = Field(..., alias="adGroupId", description="Unqiue identifier for the ad group associated with the creative.")
    creative_type: Optional["CreativeTypeInCreativeRequest"] = Field(None, alias="creativeType")
    properties: "CreativeProperties"
    consent_to_translate: Optional[bool] = Field(None, alias="consentToTranslate", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")

    model_config = {'populate_by_name': True}


class CreativeResponse(BaseModel):
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    description: Optional[str] = Field(None, description="A human-readable description of the response.")
    creative_id: Optional[float] = Field(None, alias="creativeId", description="The identifier of the creative.")

    model_config = {'populate_by_name': True}


class CreativePreviewConfigurationSize(BaseModel):
    """The slot dimension to render the creative. Sponsored Display creatives are responsive to a limited list of width and height pairs, including 300x250, 650x130, 245x250, 414x125, 600x160, 600x300, 728x9"""
    width: Optional[int] = None
    height: Optional[int] = None

    model_config = {'populate_by_name': True}


class CreativePreviewConfigurationProducts(BaseModel):
    asin: Optional[str] = Field(None, description="The ASIN of the product.")

    model_config = {'populate_by_name': True}


class CreativePreviewConfiguration(BaseModel):
    """Optional configuration for creative preview."""
    size: Optional["CreativePreviewConfigurationSize"] = Field(None, description="The slot dimension to render the creative. Sponsored Display creatives are responsive to a limited list of width and hei")
    products: Optional[list["CreativePreviewConfigurationProducts"]] = Field(None, description="The products to preview. Currently only the first product is previewable.")
    landing_page_url: Optional["LandingPageURL"] = Field(None, alias="landingPageURL")
    landing_page_type: Optional["LandingPageType"] = Field(None, alias="landingPageType")
    ad_name: Optional["AdName"] = Field(None, alias="adName")
    is_mobile: Optional[bool] = Field(None, alias="isMobile", description="Preview the creative as if it is on a mobile environment.")
    is_on_amazon: Optional[bool] = Field(None, alias="isOnAmazon", description="Preview the creative as if it is on an amazon site or third party site. The main difference is whether the preview will ")

    model_config = {'populate_by_name': True}


class CreativePreviewConfigurations(BaseModel):
    pass


class CreativePreviewRequest(BaseModel):
    creative: "PreviewCreativeModel"
    preview_configuration: "CreativePreviewConfiguration" = Field(..., alias="previewConfiguration")
    preview_configurations: Optional["CreativePreviewConfigurations"] = Field(None, alias="previewConfigurations")

    model_config = {'populate_by_name': True}


class CreativePreviewResponse(BaseModel):
    preview_html: str = Field(..., alias="previewHtml")
    preview_htmls: Optional[list[str]] = Field(None, alias="previewHtmls")

    model_config = {'populate_by_name': True}


class Locale(StrEnum):
    EN_US = "en-US"
    ES_MX = "es-MX"
    ZH_CN = "zh-CN"
    ES_ES = "es-ES"
    IT_IT = "it-IT"
    FR_FR = "fr-FR"
    FR_CA = "fr-CA"
    DE_DE = "de-DE"
    JA_JP = "ja-JP"
    KO_KR = "ko-KR"
    EN_GB = "en-GB"
    EN_CA = "en-CA"
    HI_IN = "hi-IN"
    EN_IN = "en-IN"
    EN_DE = "en-DE"
    EN_ES = "en-ES"
    EN_FR = "en-FR"
    EN_IT = "en-IT"
    EN_JP = "en-JP"
    EN_AE = "en-AE"
    AR_AE = "ar-AE"


class Error(BaseModel):
    """The error response object."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class TacticFilter(StrEnum):
    T00020 = "T00020"
    T00030 = "T00030"
    T00020_T00030 = "T00020,T00030"


class SnapshotRequestStatefilter(StrEnum):
    ENABLED = "enabled"
    PAUSED = "paused"
    ARCHIVED = "archived"


class SnapshotRequest(BaseModel):
    state_filter: Optional[SnapshotRequestStatefilter] = Field(None, alias="stateFilter", description="Optional. Restricts results to entities with state within the specified comma-separated list. Default behavior is to inc")
    tactic_filter: Optional["TacticFilter"] = Field(None, alias="tacticFilter")

    model_config = {'populate_by_name': True}


class SnapshotResponseRecordtype(StrEnum):
    CAMPAIGNS = "campaigns"
    ADGROUPS = "adgroups"
    PRODUCTADS = "productAds"
    TARGETS = "targets"


class SnapshotResponseStatus(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class SnapshotResponse(BaseModel):
    snapshot_id: Optional[str] = Field(None, alias="snapshotId", description="The identifier of the snapshot that was requested.")
    record_type: Optional[SnapshotResponseRecordtype] = Field(None, alias="recordType", description="The record type of the snapshot file.")
    status: Optional[SnapshotResponseStatus] = Field(None, description="The status of the generation of the snapshot.")
    status_details: Optional[str] = Field(None, alias="statusDetails", description="Optional description of the status.")
    location: Optional[str] = Field(None, description="The URI for the snapshot. It's only available if status is SUCCESS.")
    file_size: Optional[float] = Field(None, alias="fileSize", description="The size of the snapshot file in bytes. It's only available if status is SUCCESS.")
    expiration: Optional[float] = Field(None, description="The epoch time for expiration of the snapshot file and each snapshot file will be expired in 30 mins after generated. It")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsLocale(StrEnum):
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


class SDTactic(StrEnum):
    T00020 = "T00020"


class SDASIN(BaseModel):
    """Amazon Standard Identification Number"""
    pass


class SDGoalProduct(BaseModel):
    """A product an advertisers wants to advertise. Recommendations will be made for specified goal products."""
    asin: "SDASIN"

    model_config = {'populate_by_name': True}


class SDRecommendationType(StrEnum):
    PRODUCT = "PRODUCT"


class SDTargetingRecommendationsRequest(BaseModel):
    """Request for targeting recommendations"""
    tactic: "SDTactic"
    products: list["SDGoalProduct"] = Field(..., description="A list of products for which to get targeting recommendations")
    type_filter: list["SDRecommendationType"] = Field(..., alias="typeFilter", description="A filter to indicate which types of recommendations to request.")

    model_config = {'populate_by_name': True}


class SDTacticV31(StrEnum):
    T00020 = "T00020"
    T00030 = "T00030"


class SDTargetingRecommendationsProducts(BaseModel):
    """A list of products for which to get targeting recommendations"""
    pass


class SDRecommendationTypeV31(StrEnum):
    PRODUCT = "PRODUCT"
    CATEGORY = "CATEGORY"


class SDTargetingRecommendationsTypeFilterV31(BaseModel):
    """A filter to indicate which types of recommendations to request."""
    pass


class SDTargetingRecommendationsRequestV31(BaseModel):
    """Request for targeting recommendations"""
    tactic: "SDTacticV31"
    products: "SDTargetingRecommendationsProducts"
    type_filter: "SDTargetingRecommendationsTypeFilterV31" = Field(..., alias="typeFilter")

    model_config = {'populate_by_name': True}


class SDProductTargetingThemeExpressionType(StrEnum):
    ASINPRICEGREATERTHAN = "asinPriceGreaterThan"
    ASINBRANDSAMEAS = "asinBrandSameAs"
    ASINREVIEWRATINGLESSTHAN = "asinReviewRatingLessThan"
    ASINGLANCEVIEWSGREATERTHAN = "asinGlanceViewsGreaterThan"


class SDProductTargetingThemeExpression(BaseModel):
    """The expression used to define the contextual targeting theme."""
    type_: SDProductTargetingThemeExpressionType = Field(..., alias="type", description="The contextual targeting grammar used to define the targeting theme. Note asinAsBestSeller is currently not supported.")

    model_config = {'populate_by_name': True}


class SDProductTargetingTheme(BaseModel):
    """Contextual targeting theme definitions."""
    name: str = Field(..., description="This is the meaningful theme name which will be used as a unique identifier across various themes in the same request. T")
    expression: list["SDProductTargetingThemeExpression"] = Field(..., description="A list of expressions defining the contextual targeting theme. The list will define an AND operator on different express")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsThemes(BaseModel):
    """The themes used to refine the recommendations. Currently only contextual targeting themes are supported."""
    product: Optional[list["SDProductTargetingTheme"]] = Field(None, description="A list of themes for product targeting recommendations. If this list is empty, the service will return all the current a")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsRequestV32(BaseModel):
    """Request for targeting recommendations for API version 3.2."""
    tactic: "SDTacticV31"
    products: "SDTargetingRecommendationsProducts"
    type_filter: "SDTargetingRecommendationsTypeFilterV31" = Field(..., alias="typeFilter")
    themes: Optional["SDTargetingRecommendationsThemes"] = None

    model_config = {'populate_by_name': True}


class SDRecommendationTypeV32(StrEnum):
    PRODUCT = "PRODUCT"
    CATEGORY = "CATEGORY"
    AUDIENCE = "AUDIENCE"


class SDTargetingRecommendationsTypeFilterV32(BaseModel):
    """A filter to indicate which types of recommendations to request."""
    pass


class SDTargetingRecommendationsRequestV33(BaseModel):
    """Request for targeting recommendations for API version 3.3."""
    tactic: "SDTacticV31"
    products: "SDTargetingRecommendationsProducts"
    type_filter: "SDTargetingRecommendationsTypeFilterV32" = Field(..., alias="typeFilter")
    themes: Optional["SDTargetingRecommendationsThemes"] = None

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsRequestV34(BaseModel):
    """Request for targeting recommendations for API version 3.4."""
    tactic: "SDTacticV31"
    products: "SDTargetingRecommendationsProducts"
    type_filter: "SDTargetingRecommendationsTypeFilterV32" = Field(..., alias="typeFilter")
    themes: Optional["SDTargetingRecommendationsThemes"] = None

    model_config = {'populate_by_name': True}


class SDLandingPageType(StrEnum):
    OFF_AMAZON_LINK = "OFF_AMAZON_LINK"


class SDLandingPageURL(BaseModel):
    """The URL where customers will land after clicking on its link. Must be provided if landingPageType field is set. This field is not supported when using asin field. ||Specifications| |------------------"""
    pass


class SDAdvertisedProduct(BaseModel):
    """Product that advertisers want to advertise. Recommendations will be made for specified products. SDAdvertisedProduct can only contain either asins or landing pages. If landingPageUrl is used, there ca"""
    asin: Optional["SDASIN"] = None
    landing_page_type: Optional["SDLandingPageType"] = Field(None, alias="landingPageType")
    landing_page_url: Optional["SDLandingPageURL"] = Field(None, alias="landingPageURL")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsProductsV31(BaseModel):
    """A list of products for which to get targeting recommendations. This array can only contain either asins or landing pages. If landingPageUrl is used, there can only be one item in the array for each re"""
    pass


class SDRecommendationTypeV33(StrEnum):
    PRODUCT = "PRODUCT"
    CATEGORY = "CATEGORY"
    AUDIENCE = "AUDIENCE"
    CONTENT_CATEGORY = "CONTENT_CATEGORY"


class SDTargetingRecommendationsTypeFilterV33(BaseModel):
    """A filter to indicate which types of recommendations to request."""
    pass


class LocationPredicate(StrEnum):
    LOCATION = "location"


class LocationExpression(BaseModel):
    type_: Optional["LocationPredicate"] = Field(None, alias="type")
    value: Optional[str] = Field(None, description="The location identifier. Currently, this can correspond to either a 'city', 'state', 'dma', 'postal code', or 'country'.")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsRequestV35Categorytype(StrEnum):
    VIEWS = "views"
    PURCHASES = "purchases"


class SDTargetingRecommendationsRequestV35(BaseModel):
    """Request for targeting recommendations for API version 3.5."""
    tactic: "SDTacticV31"
    products: "SDTargetingRecommendationsProductsV31"
    type_filter: "SDTargetingRecommendationsTypeFilterV33" = Field(..., alias="typeFilter")
    themes: Optional["SDTargetingRecommendationsThemes"] = None
    category_type: Optional[SDTargetingRecommendationsRequestV35Categorytype] = Field(None, alias="categoryType", description="This field is optional unless the field locationExpression is present in the request. It is used for category audience t")
    location_expression: Optional[list["LocationExpression"]] = Field(None, alias="locationExpression", description="This optional field is used to specify the locations used in SD location targeting for non-Amazon sellers only at the mo")

    model_config = {'populate_by_name': True}


class SDErrorResponse(BaseModel):
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SDProductRecommendation(BaseModel):
    """A recommended product to target ads on"""
    asin: Optional["SDASIN"] = None
    rank: Optional[int] = Field(None, description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendations(BaseModel):
    """A collection of targeting recommendations. Results will be sorted with strongest recommendations in the beginning."""
    products: Optional[list["SDProductRecommendation"]] = Field(None, description="List of recommended product targets")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsResponse(BaseModel):
    """Response to a request for targeting recommendations."""
    recommendations: Optional["SDTargetingRecommendations"] = None

    model_config = {'populate_by_name': True}


class SDCategory(BaseModel):
    """The category identifier"""
    pass


class SDCategoryRecommendationTargetableasincountrange(BaseModel):
    """The range of ASINs available within the category catalogue. If no targetable ASIN counts are available then the targetableAsinCountRange value will be null without any properties."""
    range_lower: Optional[int] = Field(None, alias="rangeLower")
    range_upper: Optional[int] = Field(None, alias="rangeUpper")

    model_config = {'populate_by_name': True}


class SDCategoryRecommendation(BaseModel):
    """A recommended category to target ads on"""
    category: Optional["SDCategory"] = None
    name: Optional[str] = Field(None, description="The category name")
    path: Optional[list[str]] = Field(None, description="The path of the category within the category catalogue.")
    targetable_asin_count_range: Optional["SDCategoryRecommendationTargetableasincountrange"] = Field(None, alias="targetableAsinCountRange", description="The range of ASINs available within the category catalogue. If no targetable ASIN counts are available then the targetab")
    rank: Optional[int] = Field(None, description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation")

    model_config = {'populate_by_name': True}


class SDCategoryRecommendations(BaseModel):
    categories: Optional[list["SDCategoryRecommendation"]] = Field(None, description="List of recommended category targets")

    model_config = {'populate_by_name': True}


class SDProductRecommendationsV31(BaseModel):
    products: Optional[list["SDProductRecommendation"]] = Field(None, description="List of recommended product targets")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsV31(BaseModel):
    pass


class SDTargetingRecommendationsResponseV31(BaseModel):
    """Response to a request for targeting recommendations."""
    recommendations: Optional["SDTargetingRecommendationsV31"] = None

    model_config = {'populate_by_name': True}


class SDProductRecommendationV32(BaseModel):
    """A recommended product to target ads on"""
    asin: Optional["SDASIN"] = None
    rank: Optional[int] = Field(None, description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation")
    advertised_asins: Optional[list["SDASIN"]] = Field(None, alias="advertisedAsins", description="The top advertised products this recommendation is made for.")

    model_config = {'populate_by_name': True}


class SDProductTargetingRecommendationsSuccess(BaseModel):
    """Recommendation results for contextual targeting."""
    code: Optional[str] = Field(None, description="HTTP status code 200 indicating a successful response for product recomendations.")
    name: Optional[str] = Field(None, description="The theme name specified in the request.")
    recommendations: Optional[list["SDProductRecommendationV32"]] = Field(None, description="A list of recommended products.")

    model_config = {'populate_by_name': True}


class SDThemeRecommendations(BaseModel):
    themes: Optional[Any] = None

    model_config = {'populate_by_name': True}


class SDProductRecommendationsV32(BaseModel):
    products: Optional[list["SDProductRecommendationV32"]] = Field(None, description="List of recommended product targets")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsV32(BaseModel):
    """For v3.2 the service will continue to return the recommendations returned for v3.1 in products field, and return recommendations for contextual targeting themes in themes field."""
    pass


class SDTargetingRecommendationsResponseV32(BaseModel):
    """Response to a request for targeting recommendations."""
    recommendations: Optional["SDTargetingRecommendationsV32"] = None

    model_config = {'populate_by_name': True}


class SDCategoryRecommendationV33Targetableasincountrange(BaseModel):
    """The range of ASINs available within the category catalogue."""
    range_lower: Optional[int] = Field(None, alias="rangeLower")
    range_upper: Optional[int] = Field(None, alias="rangeUpper")

    model_config = {'populate_by_name': True}


class SDCategoryRecommendationV33(BaseModel):
    """A recommended category to target ads on"""
    category: Optional["SDCategory"] = None
    name: Optional[str] = Field(None, description="The category name")
    translated_name: Optional[str] = Field(None, alias="translatedName", description="The translated category name by requested locale, field will not be provided if locale is not provided or campaign local")
    path: Optional[list[str]] = Field(None, description="The path of the category within the category catalogue.")
    translated_path: Optional[list[str]] = Field(None, alias="translatedPath", description="The translated path of the category within the category catalogue by requested locale, field will not be provided if loc")
    targetable_asin_count_range: Optional["SDCategoryRecommendationV33Targetableasincountrange"] = Field(None, alias="targetableAsinCountRange", description="The range of ASINs available within the category catalogue.")
    rank: Optional[int] = Field(None, description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation")

    model_config = {'populate_by_name': True}


class SDCategoryRecommendationsV33(BaseModel):
    categories: Optional[list["SDCategoryRecommendationV33"]] = Field(None, description="List of recommended category targets.")

    model_config = {'populate_by_name': True}


class SDAudienceCategory(StrEnum):
    IN_MARKET = "In-market"
    LIFESTYLE = "Lifestyle"
    INTEREST = "Interest"
    LIFE_EVENT = "Life event"


class SDAudience(BaseModel):
    """The audience identifier"""
    pass


class SDAudienceRecommendation(BaseModel):
    """A recommended standard Amazon audience to target ads on"""
    audience: Optional["SDAudience"] = None
    name: Optional[str] = Field(None, description="The Amazon audience name")
    rank: Optional[int] = Field(None, description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation")

    model_config = {'populate_by_name': True}


class SDAudienceCategoryRecommendations(BaseModel):
    """List of recommended standard Amazon audience targets of a specific audience category"""
    category: Optional["SDAudienceCategory"] = None
    audiences: Optional[list["SDAudienceRecommendation"]] = Field(None, description="List of recommended standard Amazon audience targets")

    model_config = {'populate_by_name': True}


class SDAudienceRecommendations(BaseModel):
    audiences: Optional[list["SDAudienceCategoryRecommendations"]] = Field(None, description="List of recommended audience targets, broken down by audience category")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsV33(BaseModel):
    """For v3.3 the service will continue to return the recommendations returned for v3.2, and return audience recommendations if requested."""
    pass


class SDTargetingRecommendationsResponseV33(BaseModel):
    """Response to a request for targeting recommendations."""
    recommendations: Optional["SDTargetingRecommendationsV33"] = None

    model_config = {'populate_by_name': True}


class SDProductTargetingRecommendationsSuccessV34(BaseModel):
    """Recommendation results for contextual targeting."""
    code: Optional[str] = Field(None, description="HTTP status code 200 indicating a successful response for product recommendations.")
    name: Optional[str] = Field(None, description="The theme name specified in the request.")
    expression: Optional[list["SDProductTargetingThemeExpression"]] = Field(None, description="A list of expressions defining the product targeting theme. The list will define an AND operator on different expression")
    recommendations: Optional[list["SDProductRecommendationV32"]] = Field(None, description="A list of recommended products.")

    model_config = {'populate_by_name': True}


class SDThemeRecommendationsV34(BaseModel):
    themes: Optional[Any] = None

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsV34(BaseModel):
    """For v3.4 the service will continue to return the recommendations returned for v3.2, return audience recommendations if requested, and return the theme expression used in product targeting if requested"""
    products: Optional[list["SDProductRecommendationsV32"]] = Field(None, description="List of recommended product targets")
    categories: Optional[list["SDCategoryRecommendationV33"]] = Field(None, description="List of recommended category targets")
    audiences: Optional[list["SDAudienceCategoryRecommendations"]] = Field(None, description="List of recommended audience targets, broken down by audience category")
    themes: Optional["SDThemeRecommendationsV34"] = None

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsResponseV34(BaseModel):
    """Response to a request for targeting recommendations."""
    recommendations: Optional["SDTargetingRecommendationsV34"] = None

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


class SDTargetingRecommendationsV35(BaseModel):
    """For v3.5 the service will continue to return the recommendations returned for v3.4, return Entertainment targeting recommendations if requested and return asin-less recommendations if a landing page U"""
    products: Optional[list["SDProductRecommendationsV32"]] = Field(None, description="List of recommended product targets")
    categories: Optional[list["SDCategoryRecommendationV33"]] = Field(None, description="List of recommended category targets")
    audiences: Optional[list["SDAudienceCategoryRecommendations"]] = Field(None, description="List of recommended audience targets, broken down by audience category")
    content_categories: Optional[list["SDContentCategoryRecommendations"]] = Field(None, alias="contentCategories", description="List of recommended entertainment targets")
    themes: Optional["SDThemeRecommendationsV34"] = None

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsResponseV35(BaseModel):
    """Response to a request for targeting recommendations."""
    recommendations: Optional["SDTargetingRecommendationsV35"] = None

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsFailure(BaseModel):
    """A targeting recommendation failure record."""
    code: Optional[str] = Field(None, description="HTTP status code indicating a failure response for targeting recomendations.")
    name: Optional[str] = Field(None, description="The theme name specified in the request. If the themes field is not provided in the request, the value of this field wil")
    error_message: Optional[str] = Field(None, alias="errorMessage", description="A human friendly error message indicating the failure reasons.")

    model_config = {'populate_by_name': True}


class SDTargetingRecommendationsFailureV34(BaseModel):
    """A targeting recommendation failure record."""
    code: Optional[str] = Field(None, description="HTTP status code indicating a failure response for targeting recomendations.")
    name: Optional[str] = Field(None, description="The theme name specified in the request. If the themes field is not provided in the request, the value of this field wil")
    expression: Optional[list["SDProductTargetingThemeExpression"]] = Field(None, description="A list of expressions that failed to be applied in the product targeting theme.")
    error_message: Optional[str] = Field(None, alias="errorMessage", description="A human friendly error message indicating the failure reasons.")

    model_config = {'populate_by_name': True}


class SDBudgetRecommendationsRequest(BaseModel):
    """Request for budget recommendations."""
    campaign_ids: list[str] = Field(..., alias="campaignIds", description="A list of campaign ids for which to get budget recommendations and missed opportunities.")

    model_config = {'populate_by_name': True}


class SDSevenDaysMissedOpportunities(BaseModel):
    start_date: Optional[str] = Field(None, alias="startDate", description="Start date of the missed opportunities date range (YYYY-MM-DD).")
    end_date: Optional[str] = Field(None, alias="endDate", description="End date of the missed opportunities date range (YYYY-MM-DD).")
    percent_time_in_budget: Optional[float] = Field(None, alias="percentTimeInBudget", description="Percentage of time the campaign is active with a budget.")
    estimated_missed_sales_lower: Optional[float] = Field(None, alias="estimatedMissedSalesLower", description="Lower bound of the estimated missed sales. This will be in local currency.")
    estimated_missed_sales_upper: Optional[float] = Field(None, alias="estimatedMissedSalesUpper", description="Upper bound of the estimated missed sales. This will be in local currency.")
    estimated_missed_clicks_lower: Optional[int] = Field(None, alias="estimatedMissedClicksLower", description="Lower bound of the estimated missed clicks.")
    estimated_missed_clicks_upper: Optional[int] = Field(None, alias="estimatedMissedClicksUpper", description="Upper bound of the estimated missed clicks.")
    estimated_missed_impressions_lower: Optional[int] = Field(None, alias="estimatedMissedImpressionsLower", description="Lower bound of the estimated missed impressions.")
    estimated_missed_impressions_upper: Optional[int] = Field(None, alias="estimatedMissedImpressionsUpper", description="Upper bound of the estimated missed impressions.")
    estimated_missed_viewable_impressions_lower: Optional[int] = Field(None, alias="estimatedMissedViewableImpressionsLower", description="Lower bound of the estimated missed viewable impressions for vCPM campaigns.")
    estimated_missed_viewable_impressions_upper: Optional[int] = Field(None, alias="estimatedMissedViewableImpressionsUpper", description="Upper bound of the estimated missed viewable impressions for vCPM campaigns.")

    model_config = {'populate_by_name': True}


class SDBudgetRecommendation(BaseModel):
    index: int = Field(..., description="Correlate the recommendation to the campaign index in the request. Zero-based.")
    campaign_id: str = Field(..., alias="campaignId", description="Campaign id.")
    suggested_budget: float = Field(..., alias="suggestedBudget", description="Recommended budget for the campaign. This will be in local currency.")
    seven_days_missed_opportunities: "SDSevenDaysMissedOpportunities" = Field(..., alias="sevenDaysMissedOpportunities")

    model_config = {'populate_by_name': True}


class SDBudgetRecommendationError(BaseModel):
    index: int = Field(..., description="Correlate the recommendation to the campaign index in the request. Zero-based.")
    campaign_id: str = Field(..., alias="campaignId", description="Campaign id.")
    code: str = Field(..., description="The HTTP status code of the response.")
    details: str = Field(..., description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class SDBudgetRecommendationsResponse(BaseModel):
    budget_recommendations_success_results: list["SDBudgetRecommendation"] = Field(..., alias="budgetRecommendationsSuccessResults", description="List of successful budget recommendation for campaigns.")
    budget_recommendations_error_results: list["SDBudgetRecommendationError"] = Field(..., alias="budgetRecommendationsErrorResults", description="List of errors that occurred when generating budget recommendation.")

    model_config = {'populate_by_name': True}


class BrandSafetyDenyListDomainType(StrEnum):
    WEBSITE = "WEBSITE"
    APP = "APP"


class BrandSafetyDenyListDomainState(StrEnum):
    ENABLED = "ENABLED"
    ARCHIVED = "ARCHIVED"


class BrandSafetyRequestStatusStatus(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILURE = "FAILURE"


class BrandSafetyRequestStatus(BaseModel):
    request_id: Optional[str] = Field(None, alias="requestId", description="Request ID")
    timestamp: Optional[str] = Field(None, description="Request timestamp")
    status: Optional[BrandSafetyRequestStatusStatus] = Field(None, description="The status of the request")
    status_details: Optional[str] = Field(None, alias="statusDetails", description="Details related to the request status")

    model_config = {'populate_by_name': True}


class BrandSafetyGetResponsePagination(BaseModel):
    """Response pagination info for Brand Safety Deny List GET requests"""
    total: Optional[int] = Field(None, description="The total number of deny list domains created by the advertiser")
    limit: Optional[int] = Field(None, description="The maximum number of deny list domains returned from GET request")
    offset: Optional[int] = Field(None, description="The number of deny list domains skipped")

    model_config = {'populate_by_name': True}


class BrandSafetyDenyListProcessedDomain(BaseModel):
    domain_id: Optional[int] = Field(None, alias="domainId", description="The identifier of the Brand Safety List domain.")
    name: Optional[str] = Field(None, description="The website or app identifier. This can be in the form of full domain (eg. 'example.com' or 'example.net'), or mobile ap")
    type_: Optional["BrandSafetyDenyListDomainType"] = Field(None, alias="type")
    state: Optional["BrandSafetyDenyListDomainState"] = None
    created_at: Optional[str] = Field(None, alias="createdAt", description="The date time the domain was created at. Format YYYY-MM-ddT:HH:mm:ssZ")
    last_modified: Optional[str] = Field(None, alias="lastModified", description="The date time the domain was last modified. Format YYYY-MM-ddT:HH:mm:ssZ")

    model_config = {'populate_by_name': True}


class BrandSafetyGetResponse(BaseModel):
    """Response for Brand Safety Deny List GET requests"""
    pagination: Optional["BrandSafetyGetResponsePagination"] = None
    domains: Optional[list["BrandSafetyDenyListProcessedDomain"]] = Field(None, description="List of Brand Safety Deny List Domains")

    model_config = {'populate_by_name': True}


class BrandSafetyDenyListDomain(BaseModel):
    name: str = Field(..., description="The website or app identifier. This can be in the form of full domain (eg. 'example.com' or 'example.net'), or mobile ap")
    type_: "BrandSafetyDenyListDomainType" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class BrandSafetyPostRequest(BaseModel):
    """POST Request for Brand Safety"""
    domains: list["BrandSafetyDenyListDomain"]

    model_config = {'populate_by_name': True}


class BrandSafetyUpdateResponse(BaseModel):
    """Response for Brand Safety POST and DELETE requests"""
    request_id: Optional[str] = Field(None, alias="requestId", description="The identifier of the request")

    model_config = {'populate_by_name': True}


class BrandSafetyDenyListDomainUpdateResultStatus(StrEnum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class BrandSafetyRequestStatusResponse(BaseModel):
    """The status of the request."""
    request_status: Optional["BrandSafetyRequestStatus"] = Field(None, alias="requestStatus")

    model_config = {'populate_by_name': True}


class BrandSafetyListRequestStatusResponse(BaseModel):
    """List of all requests' status."""
    request_status_list: Optional[list["BrandSafetyRequestStatus"]] = Field(None, alias="requestStatusList", description="List of all requests' status.")

    model_config = {'populate_by_name': True}


class BrandSafetyRequestResult(BaseModel):
    status: Optional["BrandSafetyDenyListDomainUpdateResultStatus"] = None
    details: Optional[str] = Field(None, description="A human-readable description of the response.")
    domain_id: Optional[int] = Field(None, alias="domainId", description="The identifier of the Brand Safety Deny List Domain.")
    name: Optional[str] = Field(None, description="The website or app identifier.")

    model_config = {'populate_by_name': True}


class BrandSafetyRequestResultsResponse(BaseModel):
    results: Optional[list["BrandSafetyRequestResult"]] = Field(None, description="A list of results for the given requestId")

    model_config = {'populate_by_name': True}


class SDTargetingPredicateV31Type(StrEnum):
    ASINSAMEAS = "asinSameAs"
    ASINCATEGORYSAMEAS = "asinCategorySameAs"
    ASINBRANDSAMEAS = "asinBrandSameAs"
    ASINPRICEBETWEEN = "asinPriceBetween"
    ASINPRICEGREATERTHAN = "asinPriceGreaterThan"
    ASINPRICELESSTHAN = "asinPriceLessThan"
    ASINREVIEWRATINGLESSTHAN = "asinReviewRatingLessThan"
    ASINREVIEWRATINGGREATERTHAN = "asinReviewRatingGreaterThan"
    ASINREVIEWRATINGBETWEEN = "asinReviewRatingBetween"
    ASINISPRIMESHIPPINGELIGIBLE = "asinIsPrimeShippingEligible"
    ASINAGERANGESAMEAS = "asinAgeRangeSameAs"
    ASINGENRESAMEAS = "asinGenreSameAs"


class SDTargetingPredicateV31(BaseModel):
    """A predicate to match against in the Targeting Expression (only applicable to contextual targeting - T00020).  * All IDs passed for category and brand-targeting predicates must be valid IDs in the Amaz"""
    type_: SDTargetingPredicateV31Type = Field(..., alias="type")
    value: Optional[str] = Field(None, description="The value to be targeted.")

    model_config = {'populate_by_name': True}


class SDTargetingPredicateBaseV31Type(StrEnum):
    ASINCATEGORYSAMEAS = "asinCategorySameAs"
    ASINBRANDSAMEAS = "asinBrandSameAs"
    ASINPRICEBETWEEN = "asinPriceBetween"
    ASINPRICEGREATERTHAN = "asinPriceGreaterThan"
    ASINPRICELESSTHAN = "asinPriceLessThan"
    ASINREVIEWRATINGLESSTHAN = "asinReviewRatingLessThan"
    ASINREVIEWRATINGGREATERTHAN = "asinReviewRatingGreaterThan"
    ASINREVIEWRATINGBETWEEN = "asinReviewRatingBetween"
    SIMILARPRODUCT = "similarProduct"
    RELATEDPRODUCT = "relatedProduct"
    EXACTPRODUCT = "exactProduct"
    ASINISPRIMESHIPPINGELIGIBLE = "asinIsPrimeShippingEligible"
    ASINAGERANGESAMEAS = "asinAgeRangeSameAs"
    ASINGENRESAMEAS = "asinGenreSameAs"
    AUDIENCESAMEAS = "audienceSameAs"
    LOOKBACK = "lookback"


class SDTargetingPredicateBaseV31(BaseModel):
    """A predicate to match against inside the TargetingPredicateNested component (only applicable to audience targeting - T00030).  * All IDs passed for category and brand-targeting predicates must be valid"""
    type_: SDTargetingPredicateBaseV31Type = Field(..., alias="type")
    value: Optional[str] = Field(None, description="The value to be targeted.")

    model_config = {'populate_by_name': True}


class SDTargetingPredicateNestedV31Type(StrEnum):
    VIEWS = "views"
    AUDIENCE = "audience"
    PURCHASES = "purchases"


class SDTargetingPredicateNestedV31(BaseModel):
    """A behavioral event and list of targeting predicates that represents an audience to target (only applicable to audience targeting - T00030).  * For manual ASIN-grain targeting, the value array must con"""
    type_: SDTargetingPredicateNestedV31Type = Field(..., alias="type")
    value: list["SDTargetingPredicateBaseV31"]

    model_config = {'populate_by_name': True}


class SDTargetExpressionV31(BaseModel):
    pass


class SDTargetingExpressionV31(BaseModel):
    """The targeting expression to match against.  ------- Applicable to contextual targeting (T00020) ------- * A 'TargetingExpression' in a contextual targeting campaign can only contain 'TargetingPredicat"""
    pass


class SDTargetingClauseV31Expressiontype(StrEnum):
    MANUAL = "manual"
    AUTO = "auto"


class SDTargetingClauseV31(BaseModel):
    """The targeting clause"""
    expression_type: SDTargetingClauseV31Expressiontype = Field(..., alias="expressionType", description="Tactic T00020 ad groups only allow manual targeting.")
    expression: "SDTargetingExpressionV31"

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsRequestV31Targetingclauses(BaseModel):
    targeting_clause: "SDTargetingClauseV31" = Field(..., alias="targetingClause")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsRequestV31(BaseModel):
    """Request for targeting bid recommendations."""
    products: Optional[list["SDGoalProduct"]] = Field(None, description="A list of products to tailor bid recommendations for category and audience based targeting clauses.")
    targeting_clauses: list["SDTargetingBidRecommendationsRequestV31Targetingclauses"] = Field(..., alias="targetingClauses", description="A list of targeting clauses to receive bid recommendations for.")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsResponseItemFailureV31(BaseModel):
    """Failed bid recommendation response."""
    code: str = Field(..., description="The HTTP status code of this item.")
    details: str = Field(..., description="A human-readable description of this item on error.")

    model_config = {'populate_by_name': True}


class SDBidRecommendationV31(BaseModel):
    """A recommended bid range to use for a target."""
    range_lower: float = Field(..., alias="rangeLower", description="The lowest recommended bid to use to win an ad placement for this target.")
    range_upper: float = Field(..., alias="rangeUpper", description="The highest recommended bid to use to win an ad placement for this target.")
    recommended: float = Field(..., description="The recommended bid to use to win an ad placement for this target.")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsResponseItemSuccessV31(BaseModel):
    """A recommended bid range to use for a target."""
    pass


class SDCostTypeV31(StrEnum):
    CPC = "cpc"
    VCPM = "vcpm"


class SDTargetingBidRecommendationsResponseV31(BaseModel):
    """Response to a request for targeting bid recommendations."""
    cost_type: "SDCostTypeV31" = Field(..., alias="costType")
    bid_recommendations: Any = Field(..., alias="bidRecommendations")

    model_config = {'populate_by_name': True}


class SDCreativeType(StrEnum):
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class SDContentTargetingPredicateV31Type(StrEnum):
    CONTENTCATEGORYSAMEAS = "contentCategorySameAs"


class SDContentTargetingPredicateV31(BaseModel):
    """A predicate to match against in the content targeting expression."""
    type_: SDContentTargetingPredicateV31Type = Field(..., alias="type")
    value: str = Field(..., description="The value to be targeted.")

    model_config = {'populate_by_name': True}


class SDTargetExpressionV32(BaseModel):
    pass


class SDTargetingExpressionV32(BaseModel):
    """The targeting expression to match against.  ------- Applicable to contextual targeting (T00020) ------- * A 'TargetingExpression' in a contextual targeting campaign can only contain 'TargetingPredicat"""
    pass


class SDTargetingClauseV32Expressiontype(StrEnum):
    MANUAL = "manual"
    AUTO = "auto"


class SDTargetingClauseV32(BaseModel):
    """The targeting clause"""
    expression_type: SDTargetingClauseV32Expressiontype = Field(..., alias="expressionType", description="Tactic T00020 ad groups only allow manual targeting.")
    expression: "SDTargetingExpressionV32"

    model_config = {'populate_by_name': True}


class SDBidOptimizationV32(StrEnum):
    REACH = "reach"
    CLICKS = "clicks"
    CONVERSIONS = "conversions"


class SDTargetingBidRecommendationsRequestV32Targetingclauses(BaseModel):
    targeting_clause: "SDTargetingClauseV31" = Field(..., alias="targetingClause")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsRequestV32(BaseModel):
    """Request for targeting bid recommendations."""
    products: Optional[list["SDGoalProduct"]] = Field(None, description="A list of products to tailor bid recommendations for category and audience based targeting clauses.")
    bid_optimization: "SDBidOptimizationV32" = Field(..., alias="bidOptimization")
    cost_type: "SDCostTypeV31" = Field(..., alias="costType")
    targeting_clauses: list["SDTargetingBidRecommendationsRequestV32Targetingclauses"] = Field(..., alias="targetingClauses", description="A list of targeting clauses to receive bid recommendations for.")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsRequestV33Targetingclauses(BaseModel):
    targeting_clause: "SDTargetingClauseV31" = Field(..., alias="targetingClause")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsRequestV33(BaseModel):
    """Request for targeting bid recommendations."""
    products: Optional[list["SDGoalProduct"]] = Field(None, description="A list of products to tailor bid recommendations for category and audience based targeting clauses.")
    bid_optimization: "SDBidOptimizationV32" = Field(..., alias="bidOptimization")
    cost_type: "SDCostTypeV31" = Field(..., alias="costType")
    creative_type: Optional["SDCreativeType"] = Field(None, alias="creativeType")
    targeting_clauses: list["SDTargetingBidRecommendationsRequestV33Targetingclauses"] = Field(..., alias="targetingClauses", description="A list of targeting clauses to receive bid recommendations for.")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsRequestV34Targetingclauses(BaseModel):
    targeting_clause: "SDTargetingClauseV32" = Field(..., alias="targetingClause")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsRequestV34(BaseModel):
    """Request for targeting bid recommendations."""
    products: Optional[list["SDGoalProduct"]] = Field(None, description="A list of products to tailor bid recommendations for category and audience based targeting clauses. This array must cont")
    bid_optimization: "SDBidOptimizationV32" = Field(..., alias="bidOptimization")
    cost_type: "SDCostTypeV31" = Field(..., alias="costType")
    creative_type: Optional["SDCreativeType"] = Field(None, alias="creativeType")
    targeting_clauses: list["SDTargetingBidRecommendationsRequestV34Targetingclauses"] = Field(..., alias="targetingClauses", description="A list of targeting clauses to receive bid recommendations for.")

    model_config = {'populate_by_name': True}


class SDTargetingBidRecommendationsResponseV32(BaseModel):
    """Response to a request for targeting bid recommendations."""
    bid_optimization: "SDBidOptimizationV32" = Field(..., alias="bidOptimization")
    cost_type: "SDCostTypeV31" = Field(..., alias="costType")
    bid_recommendations: Any = Field(..., alias="bidRecommendations")

    model_config = {'populate_by_name': True}


class RuleId(BaseModel):
    """The identifier of the optimization rule."""
    pass


class PlacementType(StrEnum):
    ALL = "ALL"


class RuleConditionMetricname(StrEnum):
    COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS = "COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS"
    COST_PER_CLICK = "COST_PER_CLICK"
    COST_PER_ORDER = "COST_PER_ORDER"


class RuleConditionComparisonoperator(StrEnum):
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"


class RuleCondition(BaseModel):
    """A rule condition that defines the advertiser's intent for the outcome of the rule. Certain actions are performed by the product to achieve and maintain the rule condition."""
    metric_name: RuleConditionMetricname = Field(..., alias="metricName", description="The name of the metric. Supported rule metrics and corresponding supported comparisonOperators: |      MetricName      |")
    comparison_operator: RuleConditionComparisonoperator = Field(..., alias="comparisonOperator", description="The comparison operator.")
    threshold: float = Field(..., description="The value of the threshold associated with the metric. The threshold values has defined minimums depending on the metric")

    model_config = {'populate_by_name': True}


class BaseOptimizationRuleState(StrEnum):
    ENABLED = "enabled"
    PAUSED__COMING_LATER_ = "paused [COMING LATER]"


class BaseOptimizationRule(BaseModel):
    state: Optional[BaseOptimizationRuleState] = Field(None, description="The state of the optimization rule.")
    rule_name: Optional[str] = Field(None, alias="ruleName", description="The name of the optimization rule.")
    rule_conditions: Optional[list["RuleCondition"]] = Field(None, alias="ruleConditions", description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to ")

    model_config = {'populate_by_name': True}


class OptimizationRule(BaseModel):
    pass


class GetOptimizationRuleResponse(BaseModel):
    optimization_rule: Optional["OptimizationRule"] = Field(None, alias="optimizationRule")
    ad_group_ids: Optional[list["AdGroupId"]] = Field(None, alias="adGroupIds", description="A list of adGroup identifiers that the optimization rule associates with.")

    model_config = {'populate_by_name': True}


class CreateOptimizationRule(BaseModel):
    pass


class UpdateOptimizationRule(BaseModel):
    pass


class OptimizationRuleResponse(BaseModel):
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    description: Optional[str] = Field(None, description="A human-readable description of the response.")
    rule_id: Optional["RuleId"] = Field(None, alias="ruleId")

    model_config = {'populate_by_name': True}


class SingleOptimizationRuleAssociationResponse(BaseModel):
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")
    optimization_rule_id: Optional["RuleId"] = Field(None, alias="optimizationRuleId")

    model_config = {'populate_by_name': True}


class OptimizationRuleAssociationResponse(BaseModel):
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    responses: Optional[list["SingleOptimizationRuleAssociationResponse"]] = Field(None, description="An array of response objects. Each response object has code, details and optimizationRuleId.")

    model_config = {'populate_by_name': True}


class CreateAssociatedOptimizationRulesRequest(BaseModel):
    optimization_rule_ids: Optional[list["RuleId"]] = Field(None, alias="optimizationRuleIds", description="A list of optimization rule identifiers.")

    model_config = {'populate_by_name': True}


class SDForecastRequest(BaseModel):
    """Request payload for SD forecasting. Below are required and optional fields. Fields not listed will not impact forecast results. |Field              |Object            |Required| |-------------------|-"""
    campaign: "Campaign"
    ad_group: "AdGroup" = Field(..., alias="adGroup")
    optimization_rules: Optional[list["OptimizationRule"]] = Field(None, alias="optimizationRules", description="A list of SD optimization rules. Forecast will be affected by the optimization strategy rules.  Currently, supported rul")
    product_ads: list["ProductAd"] = Field(..., alias="productAds")
    targeting_clauses: list["SDForecastRequestTargetingClause"] = Field(..., alias="targetingClauses", description="A list of SD targeting clauses.")
    negative_targeting_clauses: Optional[list["NegativeTargetingClause"]] = Field(None, alias="negativeTargetingClauses", description="A list of SD negative targeting clauses.")
    location_expressions: Optional[list["LocationExpression"]] = Field(None, alias="locationExpressions", description="A list of location expressions. Only applicable for advertisers using landingPageType of OFF_AMAZON_LINK.")

    model_config = {'populate_by_name': True}


class ForecastStatus(StrEnum):
    IMPRESSION_TARGETING_TOO_NARROW = "IMPRESSION_TARGETING_TOO_NARROW"
    IMPRESSION_TARGETING_TOO_BROAD = "IMPRESSION_TARGETING_TOO_BROAD"
    COMPLETE = "COMPLETE"


class ForecastRange(BaseModel):
    """Forecast range values."""
    min: Optional[int] = None
    max: Optional[int] = None

    model_config = {'populate_by_name': True}


class ForecastMetric(StrEnum):
    IMPRESSIONS = "IMPRESSIONS"
    REACH = "REACH"
    CLICKS = "CLICKS"
    CONVERSIONS = "CONVERSIONS"


class Forecast(BaseModel):
    """Forecast impressions, clicks, reach, or conversions."""
    metric: Optional[ForecastMetric] = Field(None, description="Describes which metric is forecasted. |Name|Description| |-----------|------------------------| |IMPRESSIONS| Available ")
    value: Optional["ForecastRange"] = None

    model_config = {'populate_by_name': True}


class ForecastRangeDouble(BaseModel):
    """A range of value."""
    min: Optional[Any] = Field(None, description="Lower bound.")
    mean: Optional[Any] = Field(None, description="Geometric mean of the upper and lower bounds.")
    max: Optional[Any] = Field(None, description="Upper bound.")

    model_config = {'populate_by_name': True}


class CurvePointRangedValueLabel(StrEnum):
    CLICKS = "CLICKS"
    REACH = "REACH"


class CurvePointRangedValue(BaseModel):
    """A ranged value."""
    label: Optional[CurvePointRangedValueLabel] = Field(None, description="KPI label.")
    value: Optional["ForecastRangeDouble"] = None

    model_config = {'populate_by_name': True}


class CurvePointFixedValue(BaseModel):
    value: Optional[Any] = None

    model_config = {'populate_by_name': True}


class CurvePoint(BaseModel):
    """A single point on a curve."""
    is_focus: Optional[bool] = Field(None, alias="isFocus", description="If this point is the point with the focus circle.")
    x: Optional[dict[str, Any]] = Field(None, description="x-axis value.")
    y: Optional[list["CurvePointRangedValue"]] = Field(None, description="y-axis value of multiple KPI types.")

    model_config = {'populate_by_name': True}


class CurveGraph(StrEnum):
    BUDGET = "BUDGET"


class Curve(BaseModel):
    """Forecast curve of a certain type. The type could be budget vs forecast outcome."""
    meet_threshold: Optional[bool] = Field(None, alias="meetThreshold", description="True if the budget utilization is good to show the curve.")
    graph: Optional[CurveGraph] = Field(None, description="Type of Graph.")
    points: Optional[list["CurvePoint"]] = None

    model_config = {'populate_by_name': True}


class SDForecastResponse(BaseModel):
    """Response to a request for SD forecasting."""
    bid_optimization: Optional[str] = Field(None, alias="bidOptimization")
    lifetime_forecasts: Optional[list["Forecast"]] = Field(None, alias="lifetimeForecasts", description="Forecasts for campaign start date and end date. Default end date is start date plus 7 days.")
    weekly_forecasts: Optional[list["Forecast"]] = Field(None, alias="weeklyForecasts", description="Weekly average forecasts.")
    daily_forecasts: Optional[list["Forecast"]] = Field(None, alias="dailyForecasts", description="Daily average forecasts.")
    curves: Optional[list["Curve"]] = Field(None, description="Forecasting curves.")
    forecast_status: Optional["ForecastStatus"] = Field(None, alias="forecastStatus")

    model_config = {'populate_by_name': True}


class SDForecastErrorResponse(BaseModel):
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

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


class PerformanceMetric(StrEnum):
    ACOS = "ACOS"
    CTR = "CTR"
    CVR = "CVR"
    ROAS = "ROAS"


class ComparisonOperator(StrEnum):
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"


class PerformanceMeasureCondition(BaseModel):
    metric_name: "PerformanceMetric" = Field(..., alias="metricName")
    comparison_operator: "ComparisonOperator" = Field(..., alias="comparisonOperator")
    threshold: float = Field(..., description="The performance threshold value.")

    model_config = {'populate_by_name': True}


class timeOfDay(BaseModel):
    start_time: Optional[str] = Field(None, alias="startTime", description="The start time of intra-day budget rule window in the format 'hh:mm:ss'")
    end_time: Optional[str] = Field(None, alias="endTime", description="The end time of intra-day budget rule window in the format 'hh:mm:ss'. Required to be greater than start-time.")

    model_config = {'populate_by_name': True}


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


class BudgetChangeType(StrEnum):
    PERCENT = "PERCENT"


class budgetIncreaseBy(BaseModel):
    type_: "BudgetChangeType" = Field(..., alias="type")
    value: float = Field(..., description="The budget value.")

    model_config = {'populate_by_name': True}


class SDRuleType(StrEnum):
    SCHEDULE = "SCHEDULE"
    PERFORMANCE = "PERFORMANCE"


class SDBudgetRuleDetails(BaseModel):
    """Object representing details of a budget rule for SD campaign"""
    duration: Optional["RuleDuration"] = None
    recurrence: Optional["Recurrence"] = None
    rule_type: Optional["SDRuleType"] = Field(None, alias="ruleType")
    budget_increase_by: Optional["budgetIncreaseBy"] = Field(None, alias="budgetIncreaseBy")
    name: Optional[str] = Field(None, description="The budget rule name. Required to be unique within a campaign.")
    performance_measure_condition: Optional["PerformanceMeasureCondition"] = Field(None, alias="performanceMeasureCondition")

    model_config = {'populate_by_name': True}


class CreateSDBudgetRulesRequest(BaseModel):
    budget_rules_details: Optional[list["SDBudgetRuleDetails"]] = Field(None, alias="budgetRulesDetails", description="A list of budget rule details.")

    model_config = {'populate_by_name': True}


class BudgetRuleResponse(BaseModel):
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the error, if unsuccessful")
    rule_id: Optional[str] = Field(None, alias="ruleId", description="The rule identifier.")
    associated_campaign_ids: Optional[list[str]] = Field(None, alias="associatedCampaignIds")

    model_config = {'populate_by_name': True}


class CreateBudgetRulesResponse(BaseModel):
    responses: Optional[list["BudgetRuleResponse"]] = None

    model_config = {'populate_by_name': True}


class BudgetRuleError(BaseModel):
    """The Error Response Object."""
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

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


class PerformanceMetricValue(BaseModel):
    """An object giving the name of the performance metric and its value when the rule was evaluated"""
    name: Optional[str] = Field(None, description="Name of the performance metric")
    value: Optional[float] = Field(None, description="Value of the performance metric")

    model_config = {'populate_by_name': True}


class SDRuleBasedBudget(BaseModel):
    execution_time: Optional[float] = Field(None, alias="executionTime", description="Epoch time of budget rule execution.")
    applied_rule: Optional["SDBudgetRule"] = Field(None, alias="appliedRule")
    rule_based_budget_value: Optional[float] = Field(None, alias="ruleBasedBudgetValue", description="The budget value.")
    daily_budget_value: Optional[float] = Field(None, alias="dailyBudgetValue", description="The daily budget value.")
    performance_metric: Optional["PerformanceMetricValue"] = Field(None, alias="performanceMetric")

    model_config = {'populate_by_name': True}


class SDBudgetHistory(BaseModel):
    history: Optional[list["SDRuleBasedBudget"]] = None

    model_config = {'populate_by_name': True}


class GetSDBudgetRuleResponse(BaseModel):
    budget_rule: Optional["SDBudgetRule"] = Field(None, alias="budgetRule")

    model_config = {'populate_by_name': True}


class GetSDBudgetRulesForAdvertiserResponse(BaseModel):
    budget_rules_for_advertiser_response: Optional[list["SDBudgetRule"]] = Field(None, alias="budgetRulesForAdvertiserResponse", description="A list of rules created by the advertiser.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` ")

    model_config = {'populate_by_name': True}


class UpdateSDBudgetRulesRequest(BaseModel):
    """Request object for updating budget rule for SD campaign"""
    budget_rules_details: Optional[list["SDBudgetRule"]] = Field(None, alias="budgetRulesDetails", description="A list of budget rule details.")

    model_config = {'populate_by_name': True}


class UpdateBudgetRulesResponse(BaseModel):
    responses: Optional[list["BudgetRuleResponse"]] = None

    model_config = {'populate_by_name': True}


class AssociatedCampaign(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="The campaign identifier.")
    rule_status: str = Field(..., alias="ruleStatus", description="The budget rule evaluation status for this campaign. Read-only.")
    campaign_name: str = Field(..., alias="campaignName", description="The campaign name.")

    model_config = {'populate_by_name': True}


class SDGetAssociatedCampaignsResponse(BaseModel):
    associated_campaigns: Optional[list["AssociatedCampaign"]] = Field(None, alias="associatedCampaigns", description="A list of campaigns that are associated to this budget rule.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` ")

    model_config = {'populate_by_name': True}


class AssociatedBudgetRuleResponse(BaseModel):
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the error, if unsuccessful")
    rule_id: Optional[str] = Field(None, alias="ruleId", description="The budget rule identifier.")

    model_config = {'populate_by_name': True}


class DisassociateAssociatedBudgetRuleResponse(BaseModel):
    pass


class CreateAssociatedBudgetRulesRequest(BaseModel):
    budget_rule_ids: Optional[list[str]] = Field(None, alias="budgetRuleIds", description="A list of budget rule identifiers.")

    model_config = {'populate_by_name': True}


class CreateAssociatedBudgetRulesResponse(BaseModel):
    responses: Optional[list["AssociatedBudgetRuleResponse"]] = None

    model_config = {'populate_by_name': True}


class SDListAssociatedBudgetRulesResponse(BaseModel):
    associated_rules: Optional[list["SDBudgetRule"]] = Field(None, alias="associatedRules", description="A list of associated budget rules.")

    model_config = {'populate_by_name': True}


class BudgetUsageCampaignRequest(BaseModel):
    campaign_ids: Optional[list[str]] = Field(None, alias="campaignIds", description="A list of campaign IDs")

    model_config = {'populate_by_name': True}


class BudgetUsageCampaignBatchError(BaseModel):
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="ID of requested resource")
    index: Optional[float] = Field(None, description="An index to maintain order of the campaignIds")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

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


class BudgetUsageError(BaseModel):
    """The Error Response Object."""
    code: Optional[str] = Field(None, description="An enumerated error code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class LocationExpressionId(BaseModel):
    """The identifier of the location."""
    pass


class BaseLocationState(StrEnum):
    ENABLED = "enabled"


class BaseLocation(BaseModel):
    state: Optional[BaseLocationState] = None

    model_config = {'populate_by_name': True}


class ResolvedLocationExpression(BaseModel):
    type_: Optional["LocationPredicate"] = Field(None, alias="type")
    value: Optional[str] = Field(None, description="The human-readable location name.")

    model_config = {'populate_by_name': True}


class Location(BaseModel):
    pass


class CreateLocation(BaseModel):
    pass


class Include(BaseModel):
    """Array of Location Expression Ids"""
    pass


class LocationExpressionIdFilter(BaseModel):
    """Filter entities by the list of objectIds"""
    include: "Include"

    model_config = {'populate_by_name': True}


class ArchiveLocationRequest(BaseModel):
    """Request body for the Archive Locations API"""
    location_expression_id_filter: Optional["LocationExpressionIdFilter"] = Field(None, alias="locationExpressionIdFilter")

    model_config = {'populate_by_name': True}


class ArchiveLocationResponse(BaseModel):
    code: Optional[str] = Field(None, description="Returns 'SUCCESS' for a successful response, otherwise a HTTP error code")
    description: Optional[str] = Field(None, description="A human-readable description of the response if there is an error")
    location_expression_id: Optional["LocationExpressionId"] = Field(None, alias="locationExpressionId")

    model_config = {'populate_by_name': True}


class SDHeadlineRecommendationRequestAdformat(StrEnum):
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"


class SDHeadlineRecommendationRequest(BaseModel):
    """Request structure of SD headline recommendation API."""
    asins: Optional[list[str]] = Field(None, description="An array of ASINs associated with the creative.")
    max_num_recommendations: Optional[float] = Field(None, alias="maxNumRecommendations", description="Maximum number of recommendations that API should return. Response will [0, maxNumRecommendations] recommendations (reco")
    ad_format: Optional[SDHeadlineRecommendationRequestAdformat] = Field(None, alias="adFormat")

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


class SDHeadlineRecommendationSchemaValidationExceptionCode(StrEnum):
    INVALID_ARGUMENT = "INVALID_ARGUMENT"


class SDHeadlineRecommendationSchemaValidationException(BaseModel):
    code: Optional[SDHeadlineRecommendationSchemaValidationExceptionCode] = Field(None, description="InvalidArgumentErrorCode.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

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


class SDHeadlineRecommendationMarsThrottlingExceptionCode(StrEnum):
    THROTTLED = "THROTTLED"


class SDHeadlineRecommendationMarsThrottlingException(BaseModel):
    code: Optional[SDHeadlineRecommendationMarsThrottlingExceptionCode] = Field(None, description="ThrottledErrorCode.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class SDHeadlineRecommendationInternalServerExceptionCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class SDHeadlineRecommendationInternalServerException(BaseModel):
    code: Optional[SDHeadlineRecommendationInternalServerExceptionCode] = Field(None, description="InternalErrorCode.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}

