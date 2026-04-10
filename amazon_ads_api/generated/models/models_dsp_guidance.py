"""Auto-generated Pydantic models. Do not edit manually.

Source: DSPGuidance_prod_3p.json
Title:  DSP Guidance
"""

from __future__ import annotations

from enum import StrEnum
from typing import Optional, Union

from pydantic import BaseModel, Field



class adGroupId(BaseModel):
    """An identifier for an ad group."""
    pass


class advertiserId(BaseModel):
    """An identifier for an advertiser."""
    pass


class budgetRecoverableVisualisationVisualisationtype(StrEnum):
    BUDGET_RECOVERABLE = "BUDGET_RECOVERABLE"


class budgetRecoverableVisualisation(BaseModel):
    """Visualisation showing the amount of at-risk budget that can be recovered through recommendations."""
    at_risk: float = Field(..., alias="atRisk", description="Amount of budget projected to be unspent by end of flight.")
    at_risk_label: Optional[str] = Field(None, alias="atRiskLabel", description="Translated label for the at-risk amount (e.g. 'At Risk').")
    currency: str = Field(..., description="Currency code of the budget values, e.g. USD.")
    recoverable: float = Field(..., description="Amount of at-risk budget that can be recovered with recommendations.")
    recoverable_label: Optional[str] = Field(None, alias="recoverableLabel", description="Translated label for the recoverable amount (e.g. 'Recoverable').")
    recoverable_percent_label: Optional[str] = Field(None, alias="recoverablePercentLabel", description="Translated label for the recovery percentage (e.g. '92% recoverable').")
    visualisation_type: budgetRecoverableVisualisationVisualisationtype = Field(..., alias="visualisationType")

    model_config = {'populate_by_name': True}


class campaignId(BaseModel):
    """An identifier for a campaign."""
    pass


class canonicalId(BaseModel):
    """An identifier for DSP advertising objects such as line item, order or advertiser Id."""
    pass


class category(StrEnum):
    BIDDING = "BIDDING"
    BUDGET = "BUDGET"
    DELIVERY = "DELIVERY"
    PERFORMANCE = "PERFORMANCE"
    REPAIR = "REPAIR"
    RETAIL = "RETAIL"
    TARGETING = "TARGETING"


class dateTime(BaseModel):
    """A string representation of this instant formatted as ISO-8601."""
    pass


class dateTimeInstant(BaseModel):
    """A string representation of this instant formatted as ISO-8601 cast to an Instant datatype."""
    pass


class dspObject(BaseModel):
    """The DSP object to which the recommendation is related."""
    id_: Optional["canonicalId"] = Field(None, alias="id")
    name: Optional[str] = Field(None, description="Name of the DSP object that is set by user during initialisation step.")

    model_config = {'populate_by_name': True}


class entityId(BaseModel):
    """An identifier for an entity."""
    pass


class executionExecutionstatus(StrEnum):
    COMPLETED = "COMPLETED"
    CREATED = "CREATED"
    EXPECTED_FAILURE = "EXPECTED_FAILURE"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"


class executionMessagetype(StrEnum):
    COMPLETED = "COMPLETED"
    FAILED_GENERIC_MESSAGE = "FAILED_GENERIC_MESSAGE"
    IN_PROGRESS = "IN_PROGRESS"
    MOVE_BUDGET_WORLD_STATE_CHANGED_EXCEPTION = "MOVE_BUDGET_WORLD_STATE_CHANGED_EXCEPTION"
    PREVIEW = "PREVIEW"
    WORLD_STATE_CHANGED_EXCEPTION = "WORLD_STATE_CHANGED_EXCEPTION"


class execution(BaseModel):
    """The execution done by QuickActions on the recommendation."""
    action_id: Optional["canonicalId"] = Field(None, alias="actionId")
    creation_date: Optional["dateTime"] = Field(None, alias="creationDate")
    execution_id: Optional["canonicalId"] = Field(None, alias="executionId")
    execution_status: Optional[executionExecutionstatus] = Field(None, alias="executionStatus", description="Status of the execution.")
    last_update_date: Optional["dateTime"] = Field(None, alias="lastUpdateDate")
    message: Optional[str] = Field(None, description="Generic message to be used for errors or omissions.")
    message_type: Optional[executionMessagetype] = Field(None, alias="messageType", description="Type of message to be used for errors or omissions, which will be mapped to localised strings at the client side.")

    model_config = {'populate_by_name': True}


class recommendationText(BaseModel):
    """Description text for the recommendation."""
    pass


class type(BaseModel):
    """Describes the purpose for the recommendation, for example DEPRECATED_AUDIENCE_REMOVAL"""
    pass


class marketplaceId(BaseModel):
    """The identifier of the marketplace to which the recommendation is associated with."""
    pass


class guidanceType(StrEnum):
    ALERT = "ALERT"
    OPPORTUNITY = "OPPORTUNITY"


class recommendationId(BaseModel):
    """A unique identifier for recommendation."""
    pass


class userStatus(StrEnum):
    DEFERRED = "DEFERRED"
    DISMISSED = "DISMISSED"


class tableColumn(BaseModel):
    """A single column to be rendered in the front-end."""
    header: str = Field(..., description="Column header")
    width: int = Field(..., description="Column width ratio expressed as whole integer - does not necessarily add up to 100. Ratio must be positive.  E.g. four c")

    model_config = {'populate_by_name': True}


class quickActionActiontype(StrEnum):
    AUDIENCEREMOVAL = "AudienceRemoval"
    AUDIENCEREPLACEMENT = "AudienceReplacement"
    BASEBIDUPDATE = "BaseBidUpdate"
    FREQUENCYCAPUPDATE = "FrequencyCapUpdate"
    HIBOUENROLLMENT = "HibouEnrollment"
    MAXBIDUPDATE = "MaxBidUpdate"
    MOVEBUDGET = "MoveBudget"
    MOVEBUDGETBETA = "MoveBudgetBeta"
    ORDERBASEBIDUPDATE = "OrderBaseBidUpdate"
    ORDERMAXBIDUPDATE = "OrderMaxBidUpdate"
    ORDERVIEWABILITYUPDATE = "OrderViewabilityUpdate"
    VIEWABILITYUPDATE = "ViewabilityUpdate"


class quickAction(BaseModel):
    """An object describing the action associated with this recommendation."""
    action_id: "canonicalId" = Field(..., alias="actionId")
    action_type: quickActionActiontype = Field(..., alias="actionType", description="String identifying the type of suggested action.")
    current_value: Optional[str] = Field(None, alias="currentValue", description="Current setting value that triggered the recommendation.")
    description: str = Field(..., description="Description for the recommendation action.")
    recommended_value: Optional[str] = Field(None, alias="recommendedValue", description="Recommended setting value to be applied by the Quick Action.")

    model_config = {'populate_by_name': True}


class quickactionsData(BaseModel):
    """The automated QuickAction object associated with the recommendation."""
    current_actions: Optional[list["quickAction"]] = Field(None, alias="currentActions", description="Current active recommended actions.")
    execution_history: Optional[list["execution"]] = Field(None, alias="executionHistory", description="The history of existing QuickAction executions on this recommendation.")

    model_config = {'populate_by_name': True}


class targetType(StrEnum):
    AMH_PARENT_VENDOR = "AMH_PARENT_VENDOR"
    AMH_SELLER_MCID = "AMH_SELLER_MCID"
    AMH_VENDOR_CLAIM_ID = "AMH_VENDOR_CLAIM_ID"
    AMH_VENDOR_CODE = "AMH_VENDOR_CODE"
    ASIN_ID = "ASIN_ID"
    AXIOM_ADGROUP_EXTERNAL_ID = "AXIOM_ADGROUP_EXTERNAL_ID"
    AXIOM_ADGROUP_INTERNAL_ID = "AXIOM_ADGROUP_INTERNAL_ID"
    AXIOM_CAMPAIGN_EXTERNAL_ID = "AXIOM_CAMPAIGN_EXTERNAL_ID"
    AXIOM_CAMPAIGN_INERNAL_ID = "AXIOM_CAMPAIGN_INERNAL_ID"
    AXIOM_CAMPAIGN_INTERNAL_ID = "AXIOM_CAMPAIGN_INTERNAL_ID"
    AXIOM_KEYWORD_EXTERNAL_ID = "AXIOM_KEYWORD_EXTERNAL_ID"
    AXIOM_KEYWORD_INTERNAL_ID = "AXIOM_KEYWORD_INTERNAL_ID"
    BRAND_ADVERTISER = "BRAND_ADVERTISER"
    BRAND_AID = "BRAND_AID"
    COUNTRY_CODE = "COUNTRY_CODE"
    CUSTOM_BRAND = "CUSTOM_BRAND"
    DSM_LINE_ITEM = "DSM_LINE_ITEM"
    ENTITY_ID = "ENTITY_ID"
    GROUP_ID = "GROUP_ID"
    MARKETPLACE_ID = "MARKETPLACE_ID"
    OMS_PROPOSAL = "OMS_PROPOSAL"
    OPPORTUNITY_ID = "OPPORTUNITY_ID"
    REALM_ID = "REALM_ID"
    RODEO_ADVERTISER = "RODEO_ADVERTISER"
    RODEO_CREATIVE = "RODEO_CREATIVE"
    RODEO_DEAL = "RODEO_DEAL"
    RODEO_ENTITY = "RODEO_ENTITY"
    RODEO_LINEITEM = "RODEO_LINEITEM"
    RODEO_LINEITEM_OBJECT = "RODEO_LINEITEM_OBJECT"
    RODEO_ORDER = "RODEO_ORDER"
    RODEO_ORDER_FLIGHT = "RODEO_ORDER_FLIGHT"
    RODEO_PROPOSAL = "RODEO_PROPOSAL"
    SALESFORCE_ACCOUNT_ID = "SALESFORCE_ACCOUNT_ID"
    SALESFORCE_OPPORTUNITY = "SALESFORCE_OPPORTUNITY"
    SELLER_CENTRAL_ID = "SELLER_CENTRAL_ID"
    SESSION_ID = "SESSION_ID"
    SPOT_ID = "SPOT_ID"
    VAM_BRAND = "VAM_BRAND"


class target(BaseModel):
    """An object targeted by a recommendation, e.g a Rodeo order."""
    display_name: Optional[str] = Field(None, alias="displayName", description="Optional target display name, e.g. the Rodeo order name.")
    id_: Optional[str] = Field(None, alias="id", description="Target identifier, e.g. Rodeo orderCfid.")
    type_: Optional[targetType] = Field(None, alias="type", description="Type of the target, e.g. RODEO_ORDER.")

    model_config = {'populate_by_name': True}


class recommendation(BaseModel):
    """An object describing the DSP recommendation generated to improve the campaign performance for display advertising."""
    advertiser: Optional["dspObject"] = None
    category: Optional["category"] = None
    deferred_until: Optional["dateTime"] = Field(None, alias="deferredUntil")
    description: Optional["recommendationText"] = None
    entity_id: Optional["entityId"] = Field(None, alias="entityId")
    expected_changes: Optional[str] = Field(None, alias="expectedChanges", description="Expected changes are represented as a json array of arrays and are interpreted to be in a Disjunctive normal form (DNF).")
    explanation: Optional["recommendationText"] = None
    guidance_type: Optional["guidanceType"] = Field(None, alias="guidanceType")
    last_update_date: Optional["dateTime"] = Field(None, alias="lastUpdateDate")
    line_item: Optional["dspObject"] = Field(None, alias="lineItem")
    marketplace_id: Optional["marketplaceId"] = Field(None, alias="marketplaceId")
    order: Optional["dspObject"] = None
    quickactions_data: Optional["quickactionsData"] = Field(None, alias="quickactionsData")
    recommendation_id: Optional["recommendationId"] = Field(None, alias="recommendationId")
    recommendation_type: Optional[str] = Field(None, alias="recommendationType")
    table: Optional[list["tableColumn"]] = Field(None, description="List of columns to display")
    targets: Optional[list[list["target"]]] = Field(None, description="Nested list of lists used to group related objects targeted by this recommendation.")
    title: Optional["recommendationText"] = None
    type_: Optional["type"] = Field(None, alias="type")
    user_status: Optional["userStatus"] = Field(None, alias="userStatus")

    model_config = {'populate_by_name': True}


class guidanceName(StrEnum):
    AGGREGATED_PRE_FLIGHT_DEALS_GUIDANCE = "AGGREGATED_PRE_FLIGHT_DEALS_GUIDANCE"
    AGGREGATED_PRE_FLIGHT_OPTIMIZATIONS_GUIDANCE = "AGGREGATED_PRE_FLIGHT_OPTIMIZATIONS_GUIDANCE"
    AGGREGATED_UNDERPACING_ORDER_GUIDANCE = "AGGREGATED_UNDERPACING_ORDER_GUIDANCE"
    AMAZON_RECOMMENDED_DEALS_GUIDANCE = "AMAZON_RECOMMENDED_DEALS_GUIDANCE"
    AMAZON_RECOMMENDED_TACTICS_GUIDANCE = "AMAZON_RECOMMENDED_TACTICS_GUIDANCE"
    AQUABOT_CREATIVE_INACTIVE_GUIDANCE = "AQUABOT_CREATIVE_INACTIVE_GUIDANCE"
    AQUABOT_DOMAIN_EXCLUSION_GUIDANCE = "AQUABOT_DOMAIN_EXCLUSION_GUIDANCE"
    AQUABOT_NO_CREATIVES_GUIDANCE = "AQUABOT_NO_CREATIVES_GUIDANCE"
    BID_ADJUSTMENTS_NOT_RUNNING_GUIDANCE = "BID_ADJUSTMENTS_NOT_RUNNING_GUIDANCE"
    CARD_ISSUES_GUIDANCE = "CARD_ISSUES_GUIDANCE"
    CARD_PRE_FLIGHT_GUIDANCE = "CARD_PRE_FLIGHT_GUIDANCE"
    CARD_UNDERPACING_GUIDANCE = "CARD_UNDERPACING_GUIDANCE"
    CREATIVE_REJECTED_ORDER_GUIDANCE = "CREATIVE_REJECTED_ORDER_GUIDANCE"
    INTERNAL_DEFECT_GUIDANCE = "INTERNAL_DEFECT_GUIDANCE"
    LINE_ITEM_DEFAULT_GUIDANCE = "LINE_ITEM_DEFAULT_GUIDANCE"
    NO_SPEND_ORDER_GUIDANCE = "NO_SPEND_ORDER_GUIDANCE"
    NO_TRAFFIC_DEAL_GUIDANCE = "NO_TRAFFIC_DEAL_GUIDANCE"
    OUT_OF_STOCK_GUIDANCE = "OUT_OF_STOCK_GUIDANCE"
    OVERDELIVERING_ORDER_GUIDANCE = "OVERDELIVERING_ORDER_GUIDANCE"
    PERFORMANCE_AT_RISK_GUIDANCE = "PERFORMANCE_AT_RISK_GUIDANCE"
    PG_DEALS_ALL_CREATIVES_INACTIVE_GUIDANCE = "PG_DEALS_ALL_CREATIVES_INACTIVE_GUIDANCE"
    PG_DEALS_ALL_DEALS_INACTIVE_GUIDANCE = "PG_DEALS_ALL_DEALS_INACTIVE_GUIDANCE"
    PG_DEALS_DEAL_TARGETED_BY_MULTIPLE_LINE_ITEMS = "PG_DEALS_DEAL_TARGETED_BY_MULTIPLE_LINE_ITEMS"
    PG_DEALS_INACTIVE_ORDER_GUIDANCE = "PG_DEALS_INACTIVE_ORDER_GUIDANCE"
    PG_DEALS_LINE_ITEM_BUDGET_LESS_THAN_DEAL_BUDGET = "PG_DEALS_LINE_ITEM_BUDGET_LESS_THAN_DEAL_BUDGET"
    PG_DEALS_LINE_ITEM_ENDS_BEFORE_DEAL = "PG_DEALS_LINE_ITEM_ENDS_BEFORE_DEAL"
    PG_DEALS_LINE_ITEM_STARTS_AFTER_DEAL = "PG_DEALS_LINE_ITEM_STARTS_AFTER_DEAL"
    PRE_FLIGHT_LINE_ITEM_GUIDANCE_V2 = "PRE_FLIGHT_LINE_ITEM_GUIDANCE_V2"
    PRE_FLIGHT_OPTIMIZATIONS_LINE_ITEM_GUIDANCE = "PRE_FLIGHT_OPTIMIZATIONS_LINE_ITEM_GUIDANCE"
    PRE_FLIGHT_OPTIMIZATIONS_ORDER_GUIDANCE = "PRE_FLIGHT_OPTIMIZATIONS_ORDER_GUIDANCE"
    PRE_FLIGHT_ORDER_GUIDANCE_V2 = "PRE_FLIGHT_ORDER_GUIDANCE_V2"
    UNDERPACING_LINE_ITEM_GUIDANCE = "UNDERPACING_LINE_ITEM_GUIDANCE"
    UNDERPACING_ORDER_GUIDANCE = "UNDERPACING_ORDER_GUIDANCE"
    ZERO_KPI_GUIDANCE = "ZERO_KPI_GUIDANCE"


class guidanceTarget(BaseModel):
    """An object targeted by guidance."""
    name: Optional[str] = Field(None, description="Optional display name of the guidance target.")

    model_config = {'populate_by_name': True}


class guidanceOrderFlightTarget(BaseModel):
    """An order flight targeted by guidance."""
    pass


class guidanceEntityTarget(BaseModel):
    """An entity targeted by guidance."""
    pass


class guidanceLineItemTarget(BaseModel):
    """A line item targeted by guidance."""
    pass


class guidanceMarketplaceTarget(BaseModel):
    """A marketplace targeted by guidance."""
    pass


class guidanceAdvertiserTarget(BaseModel):
    """An advertiser targeted by guidance."""
    pass


class guidanceCallToAction(BaseModel):
    label: Optional[str] = Field(None, description="Button or link label for call-to-action.")
    link: Optional[str] = Field(None, description="Optional link for call-to-action.")

    model_config = {'populate_by_name': True}


class guidanceOrderTarget(BaseModel):
    """An order targeted by guidance."""
    pass


class guidanceTag(BaseModel):
    """A structured type used to store additional metadata."""
    pass


class guidanceExplainabilitystatus(StrEnum):
    NOT_SUPPORTED = "NOT_SUPPORTED"
    SUPPORTED = "SUPPORTED"


class guidanceGrouprecommendationsby(StrEnum):
    MARKETPLACE_ID = "MARKETPLACE_ID"
    RECOMMENDATION_TYPE = "RECOMMENDATION_TYPE"
    RODEO_ADVERTISER = "RODEO_ADVERTISER"
    RODEO_CREATIVE = "RODEO_CREATIVE"
    RODEO_ENTITY = "RODEO_ENTITY"
    RODEO_LINEITEM = "RODEO_LINEITEM"
    RODEO_ORDER = "RODEO_ORDER"


class guidance(BaseModel):
    """An object describing dynamically created guidance derived by the rule-based aggregation of individual recommendations."""
    call_to_action: Optional["guidanceCallToAction"] = Field(None, alias="callToAction")
    card_title: Optional[str] = Field(None, alias="cardTitle", description="Title text for the guidance card.")
    description: str = Field(..., description="Description text of the guidance.")
    explainability_status: Optional[guidanceExplainabilitystatus] = Field(None, alias="explainabilityStatus", description="Indicates whether explainability can be requested for this guidance. - SUPPORTED: explainability can be generated by cal")
    explanation: Optional[str] = Field(None, description="Explanation text of the guidance.")
    generated_date: "dateTimeInstant" = Field(..., alias="generatedDate")
    group_recommendations_by: Optional[guidanceGrouprecommendationsby] = Field(None, alias="groupRecommendationsBy", description="Group recommendations according to this target in the UI")
    guidance_id: Optional[str] = Field(None, alias="guidanceId", description="A unique identifier for guidance object.")
    guidance_name: "guidanceName" = Field(..., alias="guidanceName")
    guidance_type: "guidanceType" = Field(..., alias="guidanceType")
    last_updated_date: "dateTimeInstant" = Field(..., alias="lastUpdatedDate")
    marketplace_id: "marketplaceId" = Field(..., alias="marketplaceId")
    parent_guidance_id: Optional[str] = Field(None, alias="parentGuidanceId", description="Identifier of a higher level guidance object.")
    prioritisation_score: float = Field(..., alias="prioritisationScore", description="Guidance prioritisation score based on aggregated recommendations to determine ranking of multiple guidance items among ")
    recommendations: Optional[list["recommendation"]] = Field(None, description="List of dynamically aggregated recommendations used to generate this guidance.")
    tags: Optional[list["guidanceTag"]] = Field(None, description="List of structured tags objects annotating the guidance.")
    targets: list[Union["guidanceMarketplaceTarget", "guidanceEntityTarget", "guidanceAdvertiserTarget", "guidanceOrderTarget", "guidanceOrderFlightTarget", "guidanceLineItemTarget"]] = Field(..., description="Objects targeted by this guidance depending on the aggregation level, including `ENTITY`, `ADVERTISER` and `ORDER`.")
    title: str = Field(..., description="Title text of the guidance.")
    total_recommendation_count: int = Field(..., alias="totalRecommendationCount", description="Total count of recommendations used to generate this guidance.")
    visualisation: Optional["budgetRecoverableVisualisation"] = Field(None, description="Optional visual data to render alongside the guidance card.")

    model_config = {'populate_by_name': True}


class language(StrEnum):
    AR_AE = "ar-AE"
    DE_DE = "de-DE"
    EN_AE = "en-AE"
    EN_AU = "en-AU"
    EN_CA = "en-CA"
    EN_GB = "en-GB"
    EN_IN = "en-IN"
    EN_SG = "en-SG"
    EN_US = "en-US"
    ES_CO = "es-CO"
    ES_ES = "es-ES"
    ES_MX = "es-MX"
    FR_CA = "fr-CA"
    FR_FR = "fr-FR"
    HI_IN = "hi-IN"
    IT_IT = "it-IT"
    JA_JP = "ja-JP"
    KO_KR = "ko-KR"
    NL_NL = "nl-NL"
    PL_PL = "pl-PL"
    PT_BR = "pt-BR"
    SV_SE = "sv-SE"
    TA_IN = "ta-IN"
    TH_TH = "th-TH"
    TR_TR = "tr-TR"
    VI_VN = "vi-VN"
    ZH_CN = "zh-CN"
    ZH_TW = "zh-TW"


class listGuidanceRequestFilters(BaseModel):
    """Optional filters to apply to generated guidance."""
    guidance_names: Optional[list["guidanceName"]] = Field(None, alias="guidanceNames", description="Limit guidance to the specified guidance names. If unset, defaults to returning all guidance.")
    include_recommendations: Optional[bool] = Field(None, alias="includeRecommendations", description="Specify if individual recommendations should be included in the guidance response. Useful to reduce response payload siz")

    model_config = {'populate_by_name': True}


class nextToken(BaseModel):
    """Opaque pagination token returned in the query response to be provided in subsequent calls to retrieve paginated recommendations."""
    pass


class listGuidanceV1RequestBase(BaseModel):
    filters: Optional["listGuidanceRequestFilters"] = None
    next_token: Optional["nextToken"] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class listAdGroupGuidanceV1Request(BaseModel):
    """Request body for ListAdGroupGuidanceV1 call."""
    pass


class listAdvertiserGuidanceV1Request(BaseModel):
    """Request body for ListAdvertiserGuidanceV1 call."""
    pass


class listCampaignGuidanceV1Request(BaseModel):
    """Request body for ListCampaignGuidanceV1 call."""
    pass


class listGuidanceResponseSuccess(BaseModel):
    guidance: Optional[list["guidance"]] = Field(None, description="An array of objects describing dynamically created guidance derived by the rule-based aggregation of individual recommen")
    index: Optional[int] = Field(None, description="Array index referencing the target object in the request array.")
    total_guidance_count: Optional[int] = Field(None, alias="totalGuidanceCount", description="Total count of guidance available for this target.")

    model_config = {'populate_by_name': True}


class listGuidanceV1ResponseErrorCode(StrEnum):
    FAILED_GENERATION = "FAILED_GENERATION"
    INVALID_TARGET_TYPE = "INVALID_TARGET_TYPE"


class listGuidanceV1ResponseError(BaseModel):
    code: Optional[listGuidanceV1ResponseErrorCode] = Field(None, description="Enum representing error code.")
    description: Optional[str] = Field(None, description="Textual description of the error.")
    index: Optional[int] = Field(None, description="Array index referencing the target object in the request array.")

    model_config = {'populate_by_name': True}


class listGuidanceV1Response(BaseModel):
    error: Optional[list["listGuidanceV1ResponseError"]] = Field(None, description="Error response containing error code and description associated with the target object, referenced by array index.")
    next_token: Optional["nextToken"] = Field(None, alias="nextToken")
    success: Optional[list["listGuidanceResponseSuccess"]] = Field(None, description="Success response containing guidance associated with the target object, referenced by array index.")

    model_config = {'populate_by_name': True}


class recommendationsError(BaseModel):
    """Error returned from the server."""
    error_message: str = Field(..., alias="errorMessage", description="Detailed information about the error that occurred.")
    request_id: str = Field(..., alias="requestId", description="A unique value generated by the server to identify the request.")

    model_config = {'populate_by_name': True}

