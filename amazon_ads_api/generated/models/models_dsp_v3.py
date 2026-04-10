"""Auto-generated Pydantic models. Do not edit manually.

Source: DSP_v3.1_openapi.yaml
Title:  Amazon Ads API - Amazon DSP
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional

from pydantic import BaseModel, Field



class FrequencyCapType(StrEnum):
    UNCAPPED = "UNCAPPED"
    CUSTOM = "CUSTOM"


class FrequencyCapTimeunit(StrEnum):
    DAYS = "DAYS"
    HOURS = "HOURS"


class FrequencyCap(BaseModel):
    type_: FrequencyCapType = Field(..., alias="type", description="The type of advertising frequency cap. If `UNCAPPED`, no other fields are used.")
    max_impressions: Optional[int] = Field(None, alias="maxImpressions", description="The maximum number of times an ad is displayed.")
    time_unit_count: Optional[int] = Field(None, alias="timeUnitCount", description="The count of time units.")
    time_unit: Optional[FrequencyCapTimeunit] = Field(None, alias="timeUnit", description="The time unit.")

    model_config = {'populate_by_name': True}


class CurrencyCode(StrEnum):
    USD = "USD"
    CAD = "CAD"
    MXN = "MXN"


class OrderDeliveryStatus(StrEnum):
    DELIVERING = "DELIVERING"
    ENDED = "ENDED"
    OUT_OF_BUDGET = "OUT_OF_BUDGET"
    LINEITEMS_NOT_RUNNING = "LINEITEMS_NOT_RUNNING"
    INACTIVE = "INACTIVE"
    READY_TO_DELIVER = "READY_TO_DELIVER"


class AgencyFee(BaseModel):
    """The service fee associated with an agency."""
    fee_percentage: Optional[float] = Field(None, alias="feePercentage", description="Fee expressed as a percentage of the total budget.")

    model_config = {'populate_by_name': True}


class DeliveryActivationStatus(StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class BudgetCapRecurrencetimeperiod(StrEnum):
    UNCAPPED = "UNCAPPED"
    DAILY = "DAILY"
    MONTHLY = "MONTHLY"


class BudgetCap(BaseModel):
    """Adding a budget cap can result in under-delivery."""
    recurrence_time_period: BudgetCapRecurrencetimeperiod = Field(..., alias="recurrenceTimePeriod", description="The type of recurrence for the spending limit.")
    amount: float = Field(..., description="The spending limit amount.")

    model_config = {'populate_by_name': True}


class OrderBudgetBasic(BaseModel):
    total_budget_amount: Optional[float] = Field(None, alias="totalBudgetAmount", description="The total budget amount. For create/update operations, budget has to be modeled as part of flights object.")
    budget_caps: Optional[list["BudgetCap"]] = Field(None, alias="budgetCaps")

    model_config = {'populate_by_name': True}


class ProductLocation(StrEnum):
    SOLD_ON_AMAZON = "SOLD_ON_AMAZON"
    NOT_SOLD_ON_AMAZON = "NOT_SOLD_ON_AMAZON"


class BiddingStrategy(StrEnum):
    SPEND_BUDGET_IN_FULL = "SPEND_BUDGET_IN_FULL"
    MAXIMIZE_PERFORMANCE = "MAXIMIZE_PERFORMANCE"


class OptimizationGoal(StrEnum):
    AWARENESS = "AWARENESS"
    ENGAGEMENT_WITH_MY_AD = "ENGAGEMENT_WITH_MY_AD"
    CONSIDERATIONS_ON_AMAZON = "CONSIDERATIONS_ON_AMAZON"
    CONVERSIONS_OFF_AMAZON = "CONVERSIONS_OFF_AMAZON"
    PURCHASES_ON_AMAZON = "PURCHASES_ON_AMAZON"
    MOBILE_APP_INSTALLS = "MOBILE_APP_INSTALLS"


class AutoOptimizations(BaseModel):
    """The list of optimizations supported. When goal=`AWARENESS`, `CONVERSIONS`, or `CONSIDERATION`, `BID` auto optimization is not supported."""
    pass


class OptimizationGoalKpi(StrEnum):
    VIDEO_COMPLETION_RATE = "VIDEO_COMPLETION_RATE"
    CLICK_THROUGH_RATE = "CLICK_THROUGH_RATE"
    COST_PER_CLICK = "COST_PER_CLICK"
    COST_PER_ACQUISITION = "COST_PER_ACQUISITION"
    COST_PER_DOWNLOAD = "COST_PER_DOWNLOAD"
    DETAIL_PAGE_VIEW_RATE = "DETAIL_PAGE_VIEW_RATE"
    COST_PER_DETAIL_PAGE_VIEW = "COST_PER_DETAIL_PAGE_VIEW"
    RETURN_ON_AD_SPEND = "RETURN_ON_AD_SPEND"
    TOTAL_RETURN_ON_AD_SPEND = "TOTAL_RETURN_ON_AD_SPEND"
    COST_PER_VIDEO_COMPLETION = "COST_PER_VIDEO_COMPLETION"
    NONE = "NONE"
    OTHER = "OTHER"
    REACH = "REACH"


class OrderOptimization(BaseModel):
    product_location: "ProductLocation" = Field(..., alias="productLocation")
    goal: "OptimizationGoal"
    goal_kpi: "OptimizationGoalKpi" = Field(..., alias="goalKpi")
    auto_optimizations: Optional["AutoOptimizations"] = Field(None, alias="autoOptimizations")
    bidding_strategy: Optional["BiddingStrategy"] = Field(None, alias="biddingStrategy")

    model_config = {'populate_by_name': True}


class OrderBasic(BaseModel):
    """This model is designed to support batch get operation for better performance."""
    order_id: Optional[str] = Field(None, alias="orderId", description="The order identifier.")
    advertiser_id: Optional[str] = Field(None, alias="advertiserId", description="The advertiser identifier.")
    name: Optional[str] = Field(None, description="The order name.")
    external_id: Optional[str] = Field(None, alias="externalId", description="The order external identifier, also known as purchase order number (PO number). This field is required if 'Mandatory PO ")
    comments: Optional[str] = Field(None, description="The order comments.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The order start date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:00 UTC")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The order end date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:00 UTC")
    budget: Optional["OrderBudgetBasic"] = None
    agency_fee: Optional["AgencyFee"] = Field(None, alias="agencyFee")
    currency_code: Optional["CurrencyCode"] = Field(None, alias="currencyCode")
    delivery_activation_status: Optional["DeliveryActivationStatus"] = Field(None, alias="deliveryActivationStatus")
    delivery_status: Optional["OrderDeliveryStatus"] = Field(None, alias="deliveryStatus")
    frequency_cap: Optional["FrequencyCap"] = Field(None, alias="frequencyCap")
    optimization: Optional["OrderOptimization"] = None

    model_config = {'populate_by_name': True}


class Orders(BaseModel):
    total_results: Optional[int] = Field(None, alias="totalResults", description="Total number of results which satisfy the filtering criteria. This will help to support pagination.")
    response: Optional[list["OrderBasic"]] = None

    model_config = {'populate_by_name': True}


class OrderBasicV21(BaseModel):
    creation_date: Optional[str] = Field(None, alias="creationDate", description="The order creation date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:00.")
    last_updated_date: Optional[str] = Field(None, alias="lastUpdatedDate", description="The order last update date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:")

    model_config = {'populate_by_name': True}


class OrdersV21(BaseModel):
    total_results: Optional[int] = Field(None, alias="totalResults", description="Total number of results which satisfy the filtering criteria. This will help to support pagination.")
    response: Optional[list["OrderBasicV21"]] = None

    model_config = {'populate_by_name': True}


class CurrencyCodeV3(StrEnum):
    BRL = "BRL"


class OrderBasicV22(BaseModel):
    currency_code: Optional["CurrencyCodeV3"] = Field(None, alias="currencyCode")

    model_config = {'populate_by_name': True}


class OrdersV22(BaseModel):
    total_results: Optional[int] = Field(None, alias="totalResults", description="Total number of results which satisfy the filtering criteria. This will help to support pagination.")
    response: Optional[list["OrderBasicV22"]] = None

    model_config = {'populate_by_name': True}


class OptimizationGoalKpiV23(StrEnum):
    COMBINED_RETURN_ON_AD_SPEND = "COMBINED_RETURN_ON_AD_SPEND"


class OptimizationGoalV23(StrEnum):
    PURCHASES_ON_OFF_AMAZON = "PURCHASES_ON_OFF_AMAZON"


class OrderOptimizationV23(BaseModel):
    product_location: "ProductLocation" = Field(..., alias="productLocation")
    goal: "OptimizationGoalV23"
    goal_kpi: "OptimizationGoalKpiV23" = Field(..., alias="goalKpi")
    auto_optimizations: Optional["AutoOptimizations"] = Field(None, alias="autoOptimizations")
    bidding_strategy: Optional["BiddingStrategy"] = Field(None, alias="biddingStrategy")

    model_config = {'populate_by_name': True}


class OrderBasicV23(BaseModel):
    """This model is designed to support batch get operation for better performance."""
    order_id: Optional[str] = Field(None, alias="orderId", description="The order identifier.")
    advertiser_id: Optional[str] = Field(None, alias="advertiserId", description="The advertiser identifier.")
    name: Optional[str] = Field(None, description="The order name.")
    external_id: Optional[str] = Field(None, alias="externalId", description="The order external identifier, also known as purchase order number (PO number). This field is required if 'Mandatory PO ")
    comments: Optional[str] = Field(None, description="The order comments.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The order start date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:00 UTC")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The order end date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:00 UTC")
    budget: Optional["OrderBudgetBasic"] = None
    agency_fee: Optional["AgencyFee"] = Field(None, alias="agencyFee")
    currency_code: Optional["CurrencyCodeV3"] = Field(None, alias="currencyCode")
    delivery_activation_status: Optional["DeliveryActivationStatus"] = Field(None, alias="deliveryActivationStatus")
    delivery_status: Optional["OrderDeliveryStatus"] = Field(None, alias="deliveryStatus")
    frequency_cap: Optional["FrequencyCap"] = Field(None, alias="frequencyCap")
    optimization: Optional["OrderOptimizationV23"] = None
    creation_date: Optional[str] = Field(None, alias="creationDate", description="The order creation date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:00.")
    last_updated_date: Optional[str] = Field(None, alias="lastUpdatedDate", description="The order last update date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:")

    model_config = {'populate_by_name': True}


class OrdersV23(BaseModel):
    total_results: Optional[int] = Field(None, alias="totalResults", description="Total number of results which satisfy the filtering criteria. This will help to support pagination.")
    response: Optional[list["OrderBasicV23"]] = None

    model_config = {'populate_by_name': True}


class OptimizationGoalKpiV24(StrEnum):
    CLICK_THROUGH_RATE = "CLICK_THROUGH_RATE"
    COMBINED_RETURN_ON_AD_SPEND = "COMBINED_RETURN_ON_AD_SPEND"
    COST_PER_ACTION = "COST_PER_ACTION"
    COST_PER_CLICK = "COST_PER_CLICK"
    COST_PER_DETAIL_PAGE_VIEW = "COST_PER_DETAIL_PAGE_VIEW"
    COST_PER_FIRST_APP_OPEN = "COST_PER_FIRST_APP_OPEN"
    COST_PER_INSTALL = "COST_PER_INSTALL"
    COST_PER_VIDEO_COMPLETION = "COST_PER_VIDEO_COMPLETION"
    DETAIL_PAGE_VIEW_RATE = "DETAIL_PAGE_VIEW_RATE"
    NONE = "NONE"
    OTHER = "OTHER"
    REACH = "REACH"
    RETURN_ON_AD_SPEND = "RETURN_ON_AD_SPEND"
    TOTAL_COST_PER_SUBSCRIPTION = "TOTAL_COST_PER_SUBSCRIPTION"
    TOTAL_RETURN_ON_AD_SPEND = "TOTAL_RETURN_ON_AD_SPEND"
    VIDEO_COMPLETION_RATE = "VIDEO_COMPLETION_RATE"


class OrderOptimizationV24(BaseModel):
    product_location: "ProductLocation" = Field(..., alias="productLocation")
    goal: "OptimizationGoalV23"
    goal_kpi: "OptimizationGoalKpiV24" = Field(..., alias="goalKpi")
    auto_optimizations: Optional["AutoOptimizations"] = Field(None, alias="autoOptimizations")
    bidding_strategy: Optional["BiddingStrategy"] = Field(None, alias="biddingStrategy")

    model_config = {'populate_by_name': True}


class OrderBasicV24(BaseModel):
    """This model is designed to support batch get operation for better performance."""
    order_id: Optional[str] = Field(None, alias="orderId", description="The order identifier.")
    advertiser_id: Optional[str] = Field(None, alias="advertiserId", description="The advertiser identifier.")
    name: Optional[str] = Field(None, description="The order name.")
    external_id: Optional[str] = Field(None, alias="externalId", description="The order external identifier, also known as purchase order number (PO number). This field is required if 'Mandatory PO ")
    comments: Optional[str] = Field(None, description="The order comments.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The order start date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:00 UTC")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The order end date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:00 UTC")
    budget: Optional["OrderBudgetBasic"] = None
    agency_fee: Optional["AgencyFee"] = Field(None, alias="agencyFee")
    currency_code: Optional["CurrencyCodeV3"] = Field(None, alias="currencyCode")
    delivery_activation_status: Optional["DeliveryActivationStatus"] = Field(None, alias="deliveryActivationStatus")
    delivery_status: Optional["OrderDeliveryStatus"] = Field(None, alias="deliveryStatus")
    frequency_cap: Optional["FrequencyCap"] = Field(None, alias="frequencyCap")
    optimization: Optional["OrderOptimizationV24"] = None
    creation_date: Optional[str] = Field(None, alias="creationDate", description="The order creation date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:00.")
    last_updated_date: Optional[str] = Field(None, alias="lastUpdatedDate", description="The order last update date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:")

    model_config = {'populate_by_name': True}


class OrdersV24(BaseModel):
    total_results: Optional[int] = Field(None, alias="totalResults", description="Total number of results which satisfy the filtering criteria. This will help to support pagination.")
    response: Optional[list["OrderBasicV24"]] = None

    model_config = {'populate_by_name': True}


class OptimizationGoalV25(StrEnum):
    AWARENESS = "AWARENESS"
    ENGAGEMENT_WITH_MY_AD = "ENGAGEMENT_WITH_MY_AD"
    CONSIDERATIONS_ON_AMAZON = "CONSIDERATIONS_ON_AMAZON"
    CONVERSIONS_OFF_AMAZON = "CONVERSIONS_OFF_AMAZON"
    PURCHASES_ON_AMAZON = "PURCHASES_ON_AMAZON"
    MOBILE_APP_INSTALLS = "MOBILE_APP_INSTALLS"
    PURCHASES_ON_OFF_AMAZON = "PURCHASES_ON_OFF_AMAZON"
    CONSIDERATION = "CONSIDERATION"
    CONVERSIONS = "CONVERSIONS"


class OrderOptimizationV25(BaseModel):
    goal: "OptimizationGoalV25"
    target_kpi: Optional[float] = Field(None, alias="targetKpi", description="The key performance metric that will be used to measure success of your order. Depending on the `goalKpi` selected, this")

    model_config = {'populate_by_name': True}


class OrderBasicV25(BaseModel):
    optimization: Optional["OrderOptimizationV25"] = None

    model_config = {'populate_by_name': True}


class OrdersV25(BaseModel):
    total_results: Optional[int] = Field(None, alias="totalResults", description="Total number of results which satisfy the filtering criteria. This will help to support pagination.")
    response: Optional[list["OrderBasicV25"]] = None

    model_config = {'populate_by_name': True}


class OptimizationGoalKpiV26(StrEnum):
    CLICK_THROUGH_RATE = "CLICK_THROUGH_RATE"
    COMBINED_RETURN_ON_AD_SPEND = "COMBINED_RETURN_ON_AD_SPEND"
    COST_PER_ACTION = "COST_PER_ACTION"
    COST_PER_CLICK = "COST_PER_CLICK"
    COST_PER_DETAIL_PAGE_VIEW = "COST_PER_DETAIL_PAGE_VIEW"
    COST_PER_FIRST_APP_OPEN = "COST_PER_FIRST_APP_OPEN"
    COST_PER_INSTALL = "COST_PER_INSTALL"
    COST_PER_VIDEO_COMPLETION = "COST_PER_VIDEO_COMPLETION"
    DETAIL_PAGE_VIEW_RATE = "DETAIL_PAGE_VIEW_RATE"
    NONE = "NONE"
    OTHER = "OTHER"
    REACH = "REACH"
    RETURN_ON_AD_SPEND = "RETURN_ON_AD_SPEND"
    TOTAL_COST_PER_SUBSCRIPTION = "TOTAL_COST_PER_SUBSCRIPTION"
    TOTAL_RETURN_ON_AD_SPEND = "TOTAL_RETURN_ON_AD_SPEND"
    VIDEO_COMPLETION_RATE = "VIDEO_COMPLETION_RATE"
    FREQUENCY = "FREQUENCY"


class OrderOptimizationV26(BaseModel):
    goal: "OptimizationGoalV25"
    goal_kpi: "OptimizationGoalKpiV26" = Field(..., alias="goalKpi")
    target_kpi: Optional[float] = Field(None, alias="targetKpi", description="The key performance metric that will be used to measure success of your order. Depending on the `goalKpi` selected, this")

    model_config = {'populate_by_name': True}


class OrderBasicV26(BaseModel):
    optimization: Optional["OrderOptimizationV26"] = None

    model_config = {'populate_by_name': True}


class OrdersV26(BaseModel):
    total_results: Optional[int] = Field(None, alias="totalResults", description="Total number of results which satisfy the filtering criteria. This will help to support pagination.")
    response: Optional[list["OrderBasicV26"]] = None

    model_config = {'populate_by_name': True}


class OrderFlight(BaseModel):
    flight_id: Optional[str] = Field(None, alias="flightId", description="The flight identifier. Immutable field.")
    start_date_time: str = Field(..., alias="startDateTime", description="The flight start date in ISO format (YYYY-MM-DD hh:mm:ss z). Timezone is UTC. For example, 2020-10-21 03:59:00 UTC.")
    end_date_time: str = Field(..., alias="endDateTime", description="The flight start date in ISO format (YYYY-MM-DD hh:mm:ss z). Timezone is UTC. For example, 2020-10-21 03:59:00 UTC.")
    amount: float = Field(..., description="The total flight budget amount.")
    spent_amount: Optional[float] = Field(None, alias="spentAmount", description="The spent flight budget amount.")
    remaining_amount: Optional[float] = Field(None, alias="remainingAmount", description="The remaining flight budget amount.")

    model_config = {'populate_by_name': True}


class OrderBudget(BaseModel):
    pass


class Order(BaseModel):
    """Complete order model which willl be used for create/update and get."""
    order_id: Optional[str] = Field(None, alias="orderId", description="The order identifier. It will be used to perform update operation. Immutable field.")
    advertiser_id: str = Field(..., alias="advertiserId", description="The advertiser identifier. Immutable field.")
    name: str = Field(..., description="The order name.")
    external_id: Optional[str] = Field(None, alias="externalId", description="The order external identifier, also known as purchase order number (PO number). This field is required if 'Mandatory PO ")
    comments: Optional[str] = Field(None, description="The order comments.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The order start date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:00 UTC")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The order end date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:00 UTC. ")
    budget: "OrderBudget"
    currency_code: Optional["CurrencyCode"] = Field(None, alias="currencyCode")
    agency_fee: Optional["AgencyFee"] = Field(None, alias="agencyFee", description="It is immutable if the order has one or more lineItems.")
    frequency_cap: "FrequencyCap" = Field(..., alias="frequencyCap")
    optimization: "OrderOptimization"
    delivery_activation_status: Optional["DeliveryActivationStatus"] = Field(None, alias="deliveryActivationStatus")
    delivery_status: Optional["OrderDeliveryStatus"] = Field(None, alias="deliveryStatus")
    creation_date: Optional[str] = Field(None, alias="creationDate", description="The order creation date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:00.")
    last_updated_date: Optional[str] = Field(None, alias="lastUpdatedDate", description="The order last update date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:")

    model_config = {'populate_by_name': True}


class OrderV22(BaseModel):
    currency_code: Optional["CurrencyCodeV3"] = Field(None, alias="currencyCode")

    model_config = {'populate_by_name': True}


class OrderV23(BaseModel):
    """Complete order model which willl be used for create/update and get."""
    order_id: Optional[str] = Field(None, alias="orderId", description="The order identifier. It will be used to perform update operation. Immutable field.")
    advertiser_id: str = Field(..., alias="advertiserId", description="The advertiser identifier. Immutable field.")
    name: str = Field(..., description="The order name.")
    external_id: Optional[str] = Field(None, alias="externalId", description="The order external identifier, also known as purchase order number (PO number). This field is required if 'Mandatory PO ")
    comments: Optional[str] = Field(None, description="The order comments.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The order start date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:00 UTC")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The order end date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:00 UTC. ")
    budget: "OrderBudget"
    currency_code: Optional["CurrencyCodeV3"] = Field(None, alias="currencyCode")
    agency_fee: Optional["AgencyFee"] = Field(None, alias="agencyFee", description="It is immutable if the order has one or more lineItems.")
    frequency_cap: "FrequencyCap" = Field(..., alias="frequencyCap")
    optimization: "OrderOptimizationV23"
    delivery_activation_status: Optional["DeliveryActivationStatus"] = Field(None, alias="deliveryActivationStatus")
    delivery_status: Optional["OrderDeliveryStatus"] = Field(None, alias="deliveryStatus")
    creation_date: Optional[str] = Field(None, alias="creationDate", description="The order creation date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:00.")
    last_updated_date: Optional[str] = Field(None, alias="lastUpdatedDate", description="The order last update date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-12-16T19:20:30+01:")

    model_config = {'populate_by_name': True}


class OrderV24(BaseModel):
    optimization: Optional["OrderOptimizationV24"] = None

    model_config = {'populate_by_name': True}


class OrderV25(BaseModel):
    optimization: Optional["OrderOptimizationV25"] = None

    model_config = {'populate_by_name': True}


class OrderV26(BaseModel):
    optimization: Optional["OrderOptimizationV26"] = None

    model_config = {'populate_by_name': True}


class SubError(BaseModel):
    """The sub error object."""
    error_type: str = Field(..., alias="errorType")
    message: str
    field_name: Optional[str] = Field(None, alias="fieldName")

    model_config = {'populate_by_name': True}


class Error(BaseModel):
    """The error response object."""
    request_id: Optional[str] = Field(None, alias="requestId", description="Request Id that uniquely identifies your request.")
    message: Optional[str] = Field(None, description="A human-readable description of the response.")
    errors: Optional[list["SubError"]] = None

    model_config = {'populate_by_name': True}


class OrderResponse(BaseModel):
    """Response for the order create/update operations. If operation is successful, it contains only orderId. If it is a failure, it contains only errorDetails. success and failure will be corresponding to t"""
    order_id: Optional[str] = Field(None, alias="orderId", description="The order Identifier.")
    error_details: Optional["Error"] = Field(None, alias="errorDetails")

    model_config = {'populate_by_name': True}


class Bidding(BaseModel):
    """The bid values associated with a line item."""
    base_supply_bid: float = Field(..., alias="baseSupplyBid", description="The base bid per thousand impressions for ad inventory. Expressed in dollars.")
    max_supply_bid: Optional[float] = Field(None, alias="maxSupplyBid", description="The maximum cost-per-thousand impressions bid for media supply. Expressed in dollars.")

    model_config = {'populate_by_name': True}


class LineItemDeliveryStatus(StrEnum):
    DELIVERING = "DELIVERING"
    ENDED = "ENDED"
    OUT_OF_BUDGET = "OUT_OF_BUDGET"
    INACTIVE = "INACTIVE"
    READY_TO_DELIVER = "READY_TO_DELIVER"
    CREATIVES_NOT_RUNNING = "CREATIVES_NOT_RUNNING"


class LineItemType(StrEnum):
    STANDARD_DISPLAY = "STANDARD_DISPLAY"
    AMAZON_MOBILE_DISPLAY = "AMAZON_MOBILE_DISPLAY"
    AAP_MOBILE_APP = "AAP_MOBILE_APP"


class PacingDeliveryprofile(StrEnum):
    FRONT_LOADED = "FRONT_LOADED"
    EVENLY = "EVENLY"


class Pacing(BaseModel):
    delivery_profile: PacingDeliveryprofile = Field(..., alias="deliveryProfile", description="The type of line item delivery profile. FRONT_LOADED: Front loaded can deliver up to 25% more than the daily Even pace t")

    model_config = {'populate_by_name': True}


class LineItemBudget(BaseModel):
    total_budget_amount: Optional[float] = Field(None, alias="totalBudgetAmount", description="The total budget amount.")
    budget_caps: Optional[list["BudgetCap"]] = Field(None, alias="budgetCaps")
    pacing: Optional["Pacing"] = None

    model_config = {'populate_by_name': True}


class LineItemOptimization(BaseModel):
    budget_optimization: bool = Field(..., alias="budgetOptimization", description="Set to `true` to enable budget optimization for the line item.")

    model_config = {'populate_by_name': True}


class LineItemBasic(BaseModel):
    line_item_id: Optional[str] = Field(None, alias="lineItemId", description="The line item identifier.")
    line_item_type: Optional["LineItemType"] = Field(None, alias="lineItemType")
    name: Optional[str] = Field(None, description="The line item name.")
    external_id: Optional[str] = Field(None, alias="externalId", description="The line item external identifier.")
    comments: Optional[str] = Field(None, description="The line item comments.")
    order_id: Optional[str] = Field(None, alias="orderId", description="The order to which the line item is associated.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The line item start date in ISO date format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-07-16T19:20:30+")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The line item end date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example,2020-07-16T19:20:30+01:00")
    delivery_activation_status: Optional["DeliveryActivationStatus"] = Field(None, alias="deliveryActivationStatus")
    delivery_status: Optional["LineItemDeliveryStatus"] = Field(None, alias="deliveryStatus")
    currency_code: Optional["CurrencyCode"] = Field(None, alias="currencyCode")
    bidding: Optional["Bidding"] = None
    budget: Optional["LineItemBudget"] = None
    frequency_cap: Optional["FrequencyCap"] = Field(None, alias="frequencyCap")
    optimization: Optional["LineItemOptimization"] = None

    model_config = {'populate_by_name': True}


class LineItems(BaseModel):
    total_results: Optional[int] = Field(None, alias="totalResults", description="Total number of results which satisfy the filtering criteria. This will help to support pagination.")
    response: Optional[list["LineItemBasic"]] = None

    model_config = {'populate_by_name': True}


class LineItemTypeBasicV21(StrEnum):
    VIDEO = "VIDEO"
    OTT_GUARANTEED = "OTT_GUARANTEED"


class LineItemBasicV21(BaseModel):
    line_item_type: Optional["LineItemTypeBasicV21"] = Field(None, alias="lineItemType")

    model_config = {'populate_by_name': True}


class LineItemsV21(BaseModel):
    total_results: Optional[int] = Field(None, alias="totalResults", description="Total number of results which satisfy the filtering criteria. This will help to support pagination.")
    response: Optional[list["LineItemBasicV21"]] = None

    model_config = {'populate_by_name': True}


class LineItemBasicV22(BaseModel):
    line_item_type: Optional["LineItemTypeBasicV21"] = Field(None, alias="lineItemType")
    creation_date: Optional[str] = Field(None, alias="creationDate", description="The line item creation date. This field is available since version `application/vnd.dsplineitems.v2.2+json`.")
    last_updated_date: Optional[str] = Field(None, alias="lastUpdatedDate", description="The line item last updated date. This field is available since version `application/vnd.dsplineitems.v2.2+json`.")

    model_config = {'populate_by_name': True}


class LineItemsV22(BaseModel):
    total_results: Optional[int] = Field(None, alias="totalResults", description="Total number of results which satisfy the filtering criteria. This will help to support pagination.")
    response: Optional[list["LineItemBasicV22"]] = None

    model_config = {'populate_by_name': True}


class CreativeOptionsCreativerotationtype(StrEnum):
    WEIGHTED = "WEIGHTED"
    RANDOM = "RANDOM"


class CreativeOptions(BaseModel):
    creative_rotation_type: Optional[CreativeOptionsCreativerotationtype] = Field(None, alias="creativeRotationType", description="The creative rotation type.")

    model_config = {'populate_by_name': True}


class Identifier(BaseModel):
    """The unique identifier of the DSP resource/object."""
    pass


class LineItemClassification(BaseModel):
    product_categories: list["Identifier"] = Field(..., alias="productCategories", description="The array of identifiers of product categories associated with the line item. For `VIDEO` line item type only one parent")

    model_config = {'populate_by_name': True}


class ThirdPartyFeeProvidername(StrEnum):
    INTEGRAL_AD_SCIENCE = "INTEGRAL_AD_SCIENCE"
    DOUBLE_VERIFY = "DOUBLE_VERIFY"
    DOUBLE_CLICK_CAMPAIGN_MANAGER = "DOUBLE_CLICK_CAMPAIGN_MANAGER"
    COM_SCORE = "COM_SCORE"
    CPM_1 = "CPM_1"
    CPM_2 = "CPM_2"
    CPM_3 = "CPM_3"


class ThirdPartyFeeFeeallocation(StrEnum):
    ABSORB_WITH_AGENCY_FEE = "ABSORB_WITH_AGENCY_FEE"
    PASS_TO_ADVERTISER = "PASS_TO_ADVERTISER"


class ThirdPartyFee(BaseModel):
    """Third-party fees enable the platform to apply an additional fee. For example, a third-party vendor fee for ad verification, an agency markup fee, and the like."""
    provider_name: ThirdPartyFeeProvidername = Field(..., alias="providerName", description="The provider name.")
    fee_amount: float = Field(..., alias="feeAmount", description="The fee amount associated a third-party provider.")
    fee_allocation: ThirdPartyFeeFeeallocation = Field(..., alias="feeAllocation", description="The type of fee allocation.")

    model_config = {'populate_by_name': True}


class AmazonConsoleFee(BaseModel):
    """A service fee for using the Amazon Ad Platform. Fees are applied as a percentage of supply costs."""
    fee_percentage: float = Field(..., alias="feePercentage", description="The service fee expressed as a percentage.")

    model_config = {'populate_by_name': True}


class AudienceFeeFeename(StrEnum):
    IN_MARKET_LIFESTYLE = "IN_MARKET_LIFESTYLE"
    AUTOMOTIVE = "AUTOMOTIVE"


class AudienceFee(BaseModel):
    """The audience fee applied to Amazon (in-market and lifestyle) third-party (automotive)."""
    fee_name: AudienceFeeFeename = Field(..., alias="feeName", description="The category of the audience fee.")
    amount: float = Field(..., description="The amount of the audience fee.")

    model_config = {'populate_by_name': True}


class AppliedFees(BaseModel):
    third_party_fees: Optional[list["ThirdPartyFee"]] = Field(None, alias="thirdPartyFees", description="The list of third party fees associated with the line item.")
    audience_fees: Optional[list["AudienceFee"]] = Field(None, alias="audienceFees", description="The list of audience fees associated with the line item.")
    amazon_dsp_console_fee: Optional["AmazonConsoleFee"] = Field(None, alias="amazonDspConsoleFee")

    model_config = {'populate_by_name': True}


class ViewabilityTier(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    VIEWABILITY_TIER_GT_70 = "VIEWABILITY_TIER_GT_70"
    VIEWABILITY_TIER_GT_60 = "VIEWABILITY_TIER_GT_60"
    VIEWABILITY_TIER_GT_50 = "VIEWABILITY_TIER_GT_50"
    VIEWABILITY_TIER_GT_40 = "VIEWABILITY_TIER_GT_40"
    VIEWABILITY_TIER_LT_40 = "VIEWABILITY_TIER_LT_40"


class AmazonViewabilityTargeting(BaseModel):
    """Selects a viewability tier to target. The predicted view rate percentages are based on historical data and are not guaranteed. Actual view rates may vary by measurement provider and order."""
    viewability_tier: "ViewabilityTier" = Field(..., alias="viewabilityTier")
    include_unmeasurable_impressions: bool = Field(..., alias="includeUnmeasurableImpressions", description="Set to `true` to include impressions where impressions can't be measured.")

    model_config = {'populate_by_name': True}


class SegmentClause(BaseModel):
    """The segment clause."""
    segment_id: "Identifier" = Field(..., alias="segmentId")
    is_not: Optional[bool] = Field(None, alias="isNot", description="Set to `true` to set to negative targeting. Set to `false` to set to  positive targeting. Default is false.")

    model_config = {'populate_by_name': True}


class SegmentGroupIntraoperator(StrEnum):
    AND = "AND"
    OR = "OR"


class SegmentGroup(BaseModel):
    """This segment group."""
    segments: list["SegmentClause"] = Field(..., description="The list of segment clauses.")
    intra_operator: SegmentGroupIntraoperator = Field(..., alias="intraOperator", description="The intra operator used between two segment groups.")
    inter_operator: Any = Field(..., alias="interOperator", description="The inter operator used among segments within the same segment group.")

    model_config = {'populate_by_name': True}


class SegmentTargeting(BaseModel):
    segment_groups: Optional[list["SegmentGroup"]] = Field(None, alias="segmentGroups", description="The list of segment groups.")

    model_config = {'populate_by_name': True}


class MergedDomainListDomainlistmergedtargetingtype(StrEnum):
    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"


class MergedDomainList(BaseModel):
    domain_list_merged_targeting_type: Optional[MergedDomainListDomainlistmergedtargetingtype] = Field(None, alias="domainListMergedTargetingType", description="The list type of the domain. Either include or exclude")
    domain_list_merged_file: Optional[str] = Field(None, alias="domainListMergedFile", description="The URL address of the domain list file after merging all domains into single file'")

    model_config = {'populate_by_name': True}


class DomainList(BaseModel):
    merged_domain_list: Optional["MergedDomainList"] = Field(None, alias="mergedDomainList")
    inherit_from_advertiser: Optional[bool] = Field(None, alias="inheritFromAdvertiser", description="Inherit domains from advertiser settings.")

    model_config = {'populate_by_name': True}


class DoubleVerifyBrandSafetyHighseveritycontent(StrEnum):
    ADULT_CONTENT = "ADULT_CONTENT"
    DRUGS_SUBSTANCES = "DRUGS_SUBSTANCES"
    EXTREME_GRAPHICS_VIOLENCE_WEAPONS = "EXTREME_GRAPHICS_VIOLENCE_WEAPONS"
    HATE_SPEECH_PROFANITY = "HATE_SPEECH_PROFANITY"
    ILLEGAL_ACTIVITIES = "ILLEGAL_ACTIVITIES"
    INCENTIVIZED_MALWARE_CLUTTER = "INCENTIVIZED_MALWARE_CLUTTER"
    PIRACY_COPYRIGHT_INFRINGEMENT = "PIRACY_COPYRIGHT_INFRINGEMENT"


class DoubleVerifyBrandSafetyMediumseveritycontent(StrEnum):
    AD_SERVER = "AD_SERVER"
    ADULT_CONTENT = "ADULT_CONTENT"
    CULTS_SURVIVALISM = "CULTS_SURVIVALISM"
    CELEBRITY_GOSSIP = "CELEBRITY_GOSSIP"
    GAMBLING = "GAMBLING"
    DISASTER_AVIATION = "DISASTER_AVIATION"
    DISASTER_MAN_MADE = "DISASTER_MAN_MADE"
    DISASTER_NATURAL = "DISASTER_NATURAL"
    DISASTER_TERRORISTS_EVENTS = "DISASTER_TERRORISTS_EVENTS"
    DISASTER_VEHICLE = "DISASTER_VEHICLE"
    DRUGS_ALCOHOL = "DRUGS_ALCOHOL"
    DRUGS_SMOKING = "DRUGS_SMOKING"
    INFLAMMATORY_POLITICS_NEWS = "INFLAMMATORY_POLITICS_NEWS"
    NEGATIVE_NEWS_FINANCIAL = "NEGATIVE_NEWS_FINANCIAL"
    NEGATIVE_NEWS_PHARMACEUTICAL = "NEGATIVE_NEWS_PHARMACEUTICAL"
    NON_STANDARD_CONTENT_NON_ENGLISH = "NON_STANDARD_CONTENT_NON_ENGLISH"
    NON_STANDARD_CONTENT_PARKING_PAGE = "NON_STANDARD_CONTENT_PARKING_PAGE"
    OCCULT = "OCCULT"
    SEX_EDUCATION = "SEX_EDUCATION"
    UNMODERATED_UGC_FORUMS_IMAGES_VIDEO = "UNMODERATED_UGC_FORUMS_IMAGES_VIDEO"


class DoubleVerifyBrandSafetyAppagerating(StrEnum):
    EVERYONE = "EVERYONE"
    TWEENS = "TWEENS"
    TEEN = "TEEN"
    MATURE = "MATURE"
    ADULTS_ONLY = "ADULTS_ONLY"
    UNKNOWN = "UNKNOWN"


class DoubleVerifyBrandSafetyAppstarrating(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    APP_STAR_RATING_LT_15 = "APP_STAR_RATING_LT_15"
    APP_STAR_RATING_LT_20 = "APP_STAR_RATING_LT_20"
    APP_STAR_RATING_LT_25 = "APP_STAR_RATING_LT_25"
    APP_STAR_RATING_LT_30 = "APP_STAR_RATING_LT_30"
    APP_STAR_RATING_LT_35 = "APP_STAR_RATING_LT_35"
    APP_STAR_RATING_LT_40 = "APP_STAR_RATING_LT_40"
    APP_STAR_RATING_LT_45 = "APP_STAR_RATING_LT_45"


class DoubleVerifyBrandSafety(BaseModel):
    """In an update from Double Verify (DV), support for `HATE_SPEECH_PROFANITY`, medium severity `ADULT_CONTENT`, and `SEX_EDUCATION` has been dropped. Additionally, DV has moved away from high severity con"""
    high_severity_content: Optional[list[DoubleVerifyBrandSafetyHighseveritycontent]] = Field(None, alias="highSeverityContent", description="A list of high severity content and corresponding status.")
    medium_severity_content: Optional[list[DoubleVerifyBrandSafetyMediumseveritycontent]] = Field(None, alias="mediumSeverityContent", description="A list of medium severity content and corresponding status.")
    unknown_content: Optional[bool] = Field(None, alias="unknownContent", description="Set to `true` to exclude unknown content.")
    app_age_rating: Optional[list[DoubleVerifyBrandSafetyAppagerating]] = Field(None, alias="appAgeRating", description="A list of app age rating to be used for excluding apps.")
    app_star_rating: Optional[DoubleVerifyBrandSafetyAppstarrating] = Field(None, alias="appStarRating", description="Exclude by app star rating (app inventory only)")
    exclude_apps_with_insufficient_rating: Optional[bool] = Field(None, alias="excludeAppsWithInsufficientRating", description="Set to `true` to exclude unofficial apps or apps with insufficient user ratings (<100 lifetime).")

    model_config = {'populate_by_name': True}


class DoubleVerifyFraudInvalidTrafficExcludeappsandsites(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    FRAUD_TRAFFIC_LEVEL_GTE_100 = "FRAUD_TRAFFIC_LEVEL_GTE_100"
    FRAUD_TRAFFIC_LEVEL_GTE_50 = "FRAUD_TRAFFIC_LEVEL_GTE_50"
    FRAUD_TRAFFIC_LEVEL_GTE_25 = "FRAUD_TRAFFIC_LEVEL_GTE_25"
    FRAUD_TRAFFIC_LEVEL_GTE_10 = "FRAUD_TRAFFIC_LEVEL_GTE_10"
    FRAUD_TRAFFIC_LEVEL_GTE_08 = "FRAUD_TRAFFIC_LEVEL_GTE_08"
    FRAUD_TRAFFIC_LEVEL_GTE_06 = "FRAUD_TRAFFIC_LEVEL_GTE_06"
    FRAUD_TRAFFIC_LEVEL_GTE_04 = "FRAUD_TRAFFIC_LEVEL_GTE_04"
    FRAUD_TRAFFIC_LEVEL_GTE_02 = "FRAUD_TRAFFIC_LEVEL_GTE_02"


class DoubleVerifyFraudInvalidTraffic(BaseModel):
    exclude_impressions: Optional[bool] = Field(None, alias="excludeImpressions", description="Set to `true` to exclude impressions delivered to devices identified to be fraudulent or invalid.")
    exclude_apps_and_sites: Optional[DoubleVerifyFraudInvalidTrafficExcludeappsandsites] = Field(None, alias="excludeAppsAndSites")
    block_app_and_sites: Optional[bool] = Field(None, alias="blockAppAndSites", description="Set to `true` to block applications and sites with insufficient historical fraud and invalid traffic statistics. This wi")

    model_config = {'populate_by_name': True}


class DoubleVerifyViewabilityMrcviewabilitytargeting(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    MRC_VIEWABILITY_GTE_80 = "MRC_VIEWABILITY_GTE_80"
    MRC_VIEWABILITY_GTE_75 = "MRC_VIEWABILITY_GTE_75"
    MRC_VIEWABILITY_GTE_70 = "MRC_VIEWABILITY_GTE_70"
    MRC_VIEWABILITY_GTE_65 = "MRC_VIEWABILITY_GTE_65"
    MRC_VIEWABILITY_GTE_60 = "MRC_VIEWABILITY_GTE_60"
    MRC_VIEWABILITY_GTE_55 = "MRC_VIEWABILITY_GTE_55"
    MRC_VIEWABILITY_GTE_50 = "MRC_VIEWABILITY_GTE_50"
    MRC_VIEWABILITY_GTE_40 = "MRC_VIEWABILITY_GTE_40"
    MRC_VIEWABILITY_GTE_30 = "MRC_VIEWABILITY_GTE_30"


class DoubleVerifyViewabilityBrandexposureviewabilitytargeting(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    BRAND_EXPOSURE_VIEWABILITY_GTE_15_SEC_AVG_DURATION = "BRAND_EXPOSURE_VIEWABILITY_GTE_15_SEC_AVG_DURATION"
    BRAND_EXPOSURE_VIEWABILITY_GTE_10_SEC_AVG_DURATION = "BRAND_EXPOSURE_VIEWABILITY_GTE_10_SEC_AVG_DURATION"
    BRAND_EXPOSURE_VIEWABILITY_GTE_5_SEC_AVG_DURATION = "BRAND_EXPOSURE_VIEWABILITY_GTE_5_SEC_AVG_DURATION"


class DoubleVerifyViewability(BaseModel):
    mrc_viewability_targeting: Optional[DoubleVerifyViewabilityMrcviewabilitytargeting] = Field(None, alias="mrcViewabilityTargeting", description="The type of MRC viewability targeting.")
    brand_exposure_viewability_targeting: Optional[DoubleVerifyViewabilityBrandexposureviewabilitytargeting] = Field(None, alias="brandExposureViewabilityTargeting", description="The type of brand exposure viewability targeting.")
    include_unmeasurable_impressions: Optional[bool] = Field(None, alias="includeUnmeasurableImpressions", description="Set to `true` to include impressions where impressions can't be measured.")

    model_config = {'populate_by_name': True}


class DoubleVerifyAuthenticBrandSafety(BaseModel):
    double_verify_segment_id: Optional[str] = Field(None, alias="doubleVerifySegmentId", description="The segment identifier.")

    model_config = {'populate_by_name': True}


class DoubleVerify(BaseModel):
    """Double Verify (DV) is a third party provider for digital ad verification. Double Verify offers technologies that drive high-quality advertising media."""
    brand_safety: Optional["DoubleVerifyBrandSafety"] = Field(None, alias="brandSafety")
    fraud_invalid_traffic: Optional["DoubleVerifyFraudInvalidTraffic"] = Field(None, alias="fraudInvalidTraffic")
    authentic_brand_safety: Optional["DoubleVerifyAuthenticBrandSafety"] = Field(None, alias="authenticBrandSafety")
    viewability: Optional["DoubleVerifyViewability"] = None
    custom_contextual_segment_id: Optional[str] = Field(None, alias="customContextualSegmentId", description="The custom segment identifier.")

    model_config = {'populate_by_name': True}


class IasViewabilityStandard(StrEnum):
    NONE = "NONE"
    MRC = "MRC"
    GROUPM = "GROUPM"
    PUBLICIS = "PUBLICIS"


class IasViewability(BaseModel):
    """The IAS viewability standard."""
    standard: IasViewabilityStandard = Field(..., description="The viewability standard")
    viewability_targeting: "ViewabilityTier" = Field(..., alias="viewabilityTargeting")

    model_config = {'populate_by_name': True}


class IasBrandSafetyLevel(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    BRAND_SAFETY_EXCLUE_HIGH_RISK = "BRAND_SAFETY_EXCLUE_HIGH_RISK"
    BRAND_SAFETY_EXCLUE_HIGH_AND_MODERATE_RISK = "BRAND_SAFETY_EXCLUE_HIGH_AND_MODERATE_RISK"


class IasBrandSafety(BaseModel):
    ias_brand_safety_adult: "IasBrandSafetyLevel" = Field(..., alias="iasBrandSafetyAdult")
    ias_brand_safety_alcohol: "IasBrandSafetyLevel" = Field(..., alias="iasBrandSafetyAlcohol")
    ias_brand_safety_gambling: "IasBrandSafetyLevel" = Field(..., alias="iasBrandSafetyGambling")
    ias_brand_safety_hate_speech: "IasBrandSafetyLevel" = Field(..., alias="iasBrandSafetyHateSpeech")
    ias_brand_safety_illegal_downloads: "IasBrandSafetyLevel" = Field(..., alias="iasBrandSafetyIllegalDownloads")
    ias_brand_safety_illegal_drugs: "IasBrandSafetyLevel" = Field(..., alias="iasBrandSafetyIllegalDrugs")
    ias_brand_safety_offensive_language: "IasBrandSafetyLevel" = Field(..., alias="iasBrandSafetyOffensiveLanguage")
    ias_brand_safety_violence: "IasBrandSafetyLevel" = Field(..., alias="iasBrandSafetyViolence")
    exclude_content: bool = Field(..., alias="excludeContent", description="Set to `true` to exclude content that Integral Ad Science is not able to rate.")

    model_config = {'populate_by_name': True}


class IntegralAdScienceFraudinvalidtraffic(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_RISK = "FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_RISK"
    FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_MODERATE_RISK = "FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_MODERATE_RISK"


class IntegralAdScience(BaseModel):
    """Integral Ad Science (IAS) is a third party provider in digital ad verification. IAS offers technologies to drive high-quality advertising media."""
    brand_safety: Optional["IasBrandSafety"] = Field(None, alias="brandSafety")
    fraud_invalid_traffic: Optional[IntegralAdScienceFraudinvalidtraffic] = Field(None, alias="fraudInvalidTraffic", description="The type of fraud invalid traffic.")
    viewability: Optional["IasViewability"] = None

    model_config = {'populate_by_name': True}


class OracleDataCloudBrandSafetyTargetingoption(StrEnum):
    NO_BRAND_SAFETY = "NO_BRAND_SAFETY"
    MAXIMUM_PROTECTION = "MAXIMUM_PROTECTION"
    ESSENTIAL_PROTECTION = "ESSENTIAL_PROTECTION"


class OracleDataCloudBrandSafetyEssentialprotection(StrEnum):
    ADULT = "ADULT"
    ARMS = "ARMS"
    CRIME = "CRIME"
    INJURY = "INJURY"
    PIRACY = "PIRACY"
    DRUGS = "DRUGS"
    HATE_SPEECH = "HATE_SPEECH"
    MILITARY = "MILITARY"
    OBSCENITY = "OBSCENITY"
    TERRORISM = "TERRORISM"
    TOBACCO = "TOBACCO"


class OracleDataCloudBrandSafety(BaseModel):
    """The oracle data cloud brand safety."""
    targeting_option: Optional[OracleDataCloudBrandSafetyTargetingoption] = Field(None, alias="targetingOption")
    essential_protection: Optional[OracleDataCloudBrandSafetyEssentialprotection] = Field(None, alias="essentialProtection")

    model_config = {'populate_by_name': True}


class OracleDataCloudFraudinvalidtraffic(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    FRAUD_INVALID_TRAFFIC_ESSENTIAL_PROTECTION = "FRAUD_INVALID_TRAFFIC_ESSENTIAL_PROTECTION"
    FRAUD_INVALID_TRAFFIC_MAXIMUM_PROTECTION = "FRAUD_INVALID_TRAFFIC_MAXIMUM_PROTECTION"


class OracleDataCloud(BaseModel):
    """Oracle Data Cloud is a third party provider in digital ad verification. Oracle Data Cloud offers technologies to drive high-quality advertising media."""
    brand_safety: Optional["OracleDataCloudBrandSafety"] = Field(None, alias="brandSafety")
    fraud_invalid_traffic: Optional[OracleDataCloudFraudinvalidtraffic] = Field(None, alias="fraudInvalidTraffic", description="The fraud invalid traffic type.")
    custom_segment_id: Optional[str] = Field(None, alias="customSegmentId", description="The custom segment identifier.")
    contextual_predicts_segment_id: Optional[str] = Field(None, alias="contextualPredictsSegmentId", description="The custom segment predict identifier.")

    model_config = {'populate_by_name': True}


class ThirdPartyPreBidTargeting(BaseModel):
    """Amazon DSP automatically filters fraudulent and invalid traffic as well as unsafe content using a combination of proprietary technology and solutions from comScore and Sizmek. This service is availabl"""
    double_verify: Optional["DoubleVerify"] = Field(None, alias="doubleVerify")
    oracle_data_cloud: Optional["OracleDataCloud"] = Field(None, alias="oracleDataCloud")
    integral_ad_science: Optional["IntegralAdScience"] = Field(None, alias="integralAdScience")

    model_config = {'populate_by_name': True}


class UserLocationTargeting(StrEnum):
    US = "US"
    EVERYWHERE = "EVERYWHERE"
    NON_US = "NON_US"


class MobileOsTargeting(StrEnum):
    ALL = "ALL"
    IOS = "IOS"
    ANDROID = "ANDROID"


class SupplySourceTargeting(BaseModel):
    supply_sources: Optional[list["Identifier"]] = Field(None, alias="supplySources", description="The list of supply sources to target. In case of OPEN_EXCHANGE, the ID is of consolidated supply source.")

    model_config = {'populate_by_name': True}


class SupplyDealTargeting(BaseModel):
    deals: Optional[list["Identifier"]] = Field(None, description="The list of deal supply sources to target.")

    model_config = {'populate_by_name': True}


class SupplyTargeting(BaseModel):
    supply_source_targeting: Optional["SupplySourceTargeting"] = Field(None, alias="supplySourceTargeting")
    supply_deal_targeting: Optional["SupplyDealTargeting"] = Field(None, alias="supplyDealTargeting")

    model_config = {'populate_by_name': True}


class GeoLocationTargetingLocationtargetingby(StrEnum):
    IPADDRESS = "IPADDRESS"
    IPADDRESS_POSTALCODE = "IPADDRESS_POSTALCODE"


class GeoLocationTargeting(BaseModel):
    """Targets based on city, state, country, DMA , or postal code."""
    location_targeting_by: Optional[GeoLocationTargetingLocationtargetingby] = Field(None, alias="locationTargetingBy", description="The geographic location targeting type. IPADDRESS: includes IP address only. IPADDRESS_POSTALCODE: includes both IP addr")
    inclusions: Optional[list["Identifier"]] = None
    exclusions: Optional[list["Identifier"]] = None

    model_config = {'populate_by_name': True}


class DayPartDayofweek(StrEnum):
    SUNDAY = "SUNDAY"
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"


class DayPart(BaseModel):
    """The parts of a day."""
    hour_slots: list[int] = Field(..., alias="hourSlots")
    day_of_week: DayPartDayofweek = Field(..., alias="dayOfWeek", description="The day of the week.")

    model_config = {'populate_by_name': True}


class DayPartTargetingTimezonepreference(StrEnum):
    USER_TIMEZONE = "USER_TIMEZONE"
    AD_SERVER_TIMEZONE = "AD_SERVER_TIMEZONE"


class DayPartTargeting(BaseModel):
    """Specifies time zone and parts of the day to target delivery of the line item."""
    time_zone_preference: DayPartTargetingTimezonepreference = Field(..., alias="timeZonePreference", description="The time zone associated with line item delivery.")
    day_parts: list["DayPart"] = Field(..., alias="dayParts", description="The list of parts of the day.")

    model_config = {'populate_by_name': True}


class SiteLanguageTargeting(StrEnum):
    EN = "EN"
    ES = "ES"


class StandardDisplayTargetingDevicetypetargeting(StrEnum):
    DESKTOP_AND_MOBILE = "DESKTOP_AND_MOBILE"
    MOBILE = "MOBILE"
    DESKTOP = "DESKTOP"


class StandardDisplayTargeting(BaseModel):
    user_location_targeting: Optional["UserLocationTargeting"] = Field(None, alias="userLocationTargeting")
    amazon_viewability_targeting: Optional["AmazonViewabilityTargeting"] = Field(None, alias="amazonViewabilityTargeting")
    third_party_pre_bid_targeting: Optional["ThirdPartyPreBidTargeting"] = Field(None, alias="thirdPartyPreBidTargeting")
    supply_targeting: Optional["SupplyTargeting"] = Field(None, alias="supplyTargeting")
    geo_location_targeting: Optional["GeoLocationTargeting"] = Field(None, alias="geoLocationTargeting")
    segment_targeting: Optional["SegmentTargeting"] = Field(None, alias="segmentTargeting")
    day_part_targeting: Optional["DayPartTargeting"] = Field(None, alias="dayPartTargeting")
    domain_list_targeting: Optional["DomainList"] = Field(None, alias="domainListTargeting")
    device_type_targeting: Optional[StandardDisplayTargetingDevicetypetargeting] = Field(None, alias="deviceTypeTargeting", description="The targeted device type for standard display line item type. It is required input for `STANDARD_DISPLAY` line item type")
    mobile_os_targeting: Optional["MobileOsTargeting"] = Field(None, alias="mobileOsTargeting")
    site_language_targeting: Optional["SiteLanguageTargeting"] = Field(None, alias="siteLanguageTargeting")
    content_targeting: Optional[list["Identifier"]] = Field(None, alias="contentTargeting", description="The IAB content category type. IAB content categories enable advertisers to target websites according to their subject m")
    contextual_targeting: Optional[bool] = Field(None, alias="contextualTargeting", description="Set to `true` to enable contextual targeting. Contextual targeting targets the detail page of products that are frequent")

    model_config = {'populate_by_name': True}


class MobileAppTargetingApptargetingoption(StrEnum):
    INCLUDE_APPS = "INCLUDE_APPS"
    EXCLUDE_APPS = "EXCLUDE_APPS"


class MobileAppTargeting(BaseModel):
    app_targeting_option: MobileAppTargetingApptargetingoption = Field(..., alias="appTargetingOption", description="The mobile application targeting inclusion type.")
    app_ids: list[str] = Field(..., alias="appIds", description="The list of application identifiers.")

    model_config = {'populate_by_name': True}


class AapMobileAppTargetingDevicetypetargeting(StrEnum):
    IPHONE = "IPHONE"
    IPAD = "IPAD"
    ANDROID = "ANDROID"
    KINDLE_FIRE = "KINDLE_FIRE"
    KINDLE_FIRE_HD = "KINDLE_FIRE_HD"


class AapMobileAppTargetingDeviceorientationtargeting(StrEnum):
    ANY = "ANY"
    PORTRAIT = "PORTRAIT"
    LANDSCAPE = "LANDSCAPE"


class AapMobileAppTargeting(BaseModel):
    user_location_targeting: Optional["UserLocationTargeting"] = Field(None, alias="userLocationTargeting")
    amazon_viewability_targeting: Optional["AmazonViewabilityTargeting"] = Field(None, alias="amazonViewabilityTargeting")
    third_party_pre_bid_targeting: Optional["ThirdPartyPreBidTargeting"] = Field(None, alias="thirdPartyPreBidTargeting")
    supply_targeting: Optional["SupplyTargeting"] = Field(None, alias="supplyTargeting")
    geo_location_targeting: Optional["GeoLocationTargeting"] = Field(None, alias="geoLocationTargeting")
    segment_targeting: Optional["SegmentTargeting"] = Field(None, alias="segmentTargeting")
    day_part_targeting: Optional["DayPartTargeting"] = Field(None, alias="dayPartTargeting")
    mobile_app_targeting: Optional["MobileAppTargeting"] = Field(None, alias="mobileAppTargeting")
    device_type_targeting: Optional[list[AapMobileAppTargetingDevicetypetargeting]] = Field(None, alias="deviceTypeTargeting", description="The targeted mobile application device type. Note that this is applicable only for the `AAP_MOBILE APP` type of line ite")
    device_orientation_targeting: Optional[AapMobileAppTargetingDeviceorientationtargeting] = Field(None, alias="deviceOrientationTargeting", description="The mobile device orientation targeting type.")

    model_config = {'populate_by_name': True}


class AmazonMobileDisplayTargeting(BaseModel):
    user_location_targeting: Optional["UserLocationTargeting"] = Field(None, alias="userLocationTargeting")
    amazon_viewability_targeting: Optional["AmazonViewabilityTargeting"] = Field(None, alias="amazonViewabilityTargeting")
    third_party_pre_bid_targeting: Optional["ThirdPartyPreBidTargeting"] = Field(None, alias="thirdPartyPreBidTargeting")
    supply_targeting: Optional["SupplyTargeting"] = Field(None, alias="supplyTargeting")
    geo_location_targeting: Optional["GeoLocationTargeting"] = Field(None, alias="geoLocationTargeting")
    segment_targeting: Optional["SegmentTargeting"] = Field(None, alias="segmentTargeting")
    day_part_targeting: Optional["DayPartTargeting"] = Field(None, alias="dayPartTargeting")
    mobile_os_targeting: Optional["MobileOsTargeting"] = Field(None, alias="mobileOsTargeting")
    contextual_targeting: Optional[bool] = Field(None, alias="contextualTargeting", description="Set to `true` to enable contextual targeting. Contextual targeting targets the detail page of products that are frequent")

    model_config = {'populate_by_name': True}


class LineItemTargeting(BaseModel):
    standard_display_targeting: Optional["StandardDisplayTargeting"] = Field(None, alias="standardDisplayTargeting")
    aap_mobile_app_targeting: Optional["AapMobileAppTargeting"] = Field(None, alias="aapMobileAppTargeting")
    amazon_mobile_display_targeting: Optional["AmazonMobileDisplayTargeting"] = Field(None, alias="amazonMobileDisplayTargeting")

    model_config = {'populate_by_name': True}


class LineItem(BaseModel):
    line_item_id: Optional[str] = Field(None, alias="lineItemId", description="The line item identifier. This is required when we perform update operations. Immutable field.")
    line_item_type: "LineItemType" = Field(..., alias="lineItemType")
    name: str = Field(..., description="The line item name.")
    order_id: str = Field(..., alias="orderId", description="The order to which the line item is associated. Immutable field.")
    external_id: Optional[str] = Field(None, alias="externalId", description="The external identifier of the line item.")
    start_date_time: str = Field(..., alias="startDateTime", description="The line item start date in ISO date format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-07-16T19:20:30+")
    end_date_time: str = Field(..., alias="endDateTime", description="The line item end date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-07-16T19:20:30+01:00")
    comments: Optional[str] = Field(None, description="The line item comments.")
    delivery_activation_status: Optional["DeliveryActivationStatus"] = Field(None, alias="deliveryActivationStatus")
    delivery_status: Optional["LineItemDeliveryStatus"] = Field(None, alias="deliveryStatus")
    line_item_classification: "LineItemClassification" = Field(..., alias="lineItemClassification")
    frequency_cap: "FrequencyCap" = Field(..., alias="frequencyCap")
    targeting: Optional["LineItemTargeting"] = None
    budget: Optional["LineItemBudget"] = None
    currency_code: Optional["CurrencyCode"] = Field(None, alias="currencyCode")
    applied_fees: Optional["AppliedFees"] = Field(None, alias="appliedFees")
    bidding: "Bidding"
    optimization: "LineItemOptimization"
    creative_options: Optional["CreativeOptions"] = Field(None, alias="creativeOptions")
    creation_date: Optional[str] = Field(None, alias="creationDate", description="The line item creation date.")
    last_update_date: Optional[str] = Field(None, alias="lastUpdateDate", description="The line item last update date.")

    model_config = {'populate_by_name': True}


class LineItemTypeV21(StrEnum):
    VIDEO = "VIDEO"


class OttContentGenres(StrEnum):
    ACTION = "ACTION"
    ADVENTURE = "ADVENTURE"
    ANIMATION = "ANIMATION"
    BIOGRAPHY = "BIOGRAPHY"
    COMEDY = "COMEDY"
    CRIME = "CRIME"
    DOCUMENTARY = "DOCUMENTARY"
    DRAMA = "DRAMA"
    FAMILY = "FAMILY"
    FANTASY = "FANTASY"
    FILM_NOIR = "FILM_NOIR"
    GAME_SHOW = "GAME_SHOW"
    HISTORY = "HISTORY"
    HORROR = "HORROR"
    MUSICAL = "MUSICAL"
    MYSTERY = "MYSTERY"
    NEWS = "NEWS"
    REALITY_TV = "REALITY_TV"
    ROMANCE = "ROMANCE"
    SCIENCE_FICTION = "SCIENCE_FICTION"
    SHORT = "SHORT"
    SPORT = "SPORT"
    SUPER_HERO = "SUPER_HERO"
    TALK_SHOW = "TALK_SHOW"
    THRILLER = "THRILLER"
    WAR = "WAR"
    WESTERN = "WESTERN"
    GENRE_NOT_AVAILABLE = "GENRE_NOT_AVAILABLE"


class OttTargeting(BaseModel):
    """This targeting only applies to Amazon O&O and Amazon Publisher Services (APS) inventory. It can only be provided when CONNECTED_TV is selected in deviceTypeTargeting. Currently API does not support ex"""
    ott_content_genres: Optional[list["OttContentGenres"]] = Field(None, alias="ottContentGenres", description="Select genres to exclude delivery to that audience.")
    ott_app_blocking: Optional[list[str]] = Field(None, alias="ottAppBlocking", description="Select the apps that should be excluded.")

    model_config = {'populate_by_name': True}


class DoubleVerifyViewabilityV21Averagecompletionandfullyviewableratetargeting(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_10 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_10"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_20 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_20"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_25 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_25"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_30 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_30"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_35 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_35"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_40 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_40"


class DoubleVerifyViewabilityV21(BaseModel):
    average_completion_and_fully_viewable_rate_targeting: Optional[DoubleVerifyViewabilityV21Averagecompletionandfullyviewableratetargeting] = Field(None, alias="averageCompletionAndFullyViewableRateTargeting", description="The type of average completion and fully viewable rate targeting.")

    model_config = {'populate_by_name': True}


class DoubleVerifyV21(BaseModel):
    viewability: Optional["DoubleVerifyViewabilityV21"] = None

    model_config = {'populate_by_name': True}


class ThirdPartyPreBidTargetingV21(BaseModel):
    double_verify: Optional["DoubleVerifyV21"] = Field(None, alias="doubleVerify")

    model_config = {'populate_by_name': True}


class VideoTargetingDevicetypetargeting(StrEnum):
    MOBILE = "MOBILE"
    DESKTOP = "DESKTOP"
    CONNECTED_TV = "CONNECTED_TV"


class VideoTargetingMobileenvironmenttargeting(StrEnum):
    WEB = "WEB"
    APP = "APP"


class VideoTargetingVideoinitiationtypetargeting(StrEnum):
    ANY = "ANY"
    USER_INITIATED_ONLY = "USER_INITIATED_ONLY"
    AUTOPLAY_ONLY = "AUTOPLAY_ONLY"
    UNKNOWN = "UNKNOWN"


class VideoTargetingVideoadformattargeting(StrEnum):
    IN_STREAM = "IN_STREAM"
    OUT_STREAM = "OUT_STREAM"
    IN_STREAM_AND_OUT_STREAM = "IN_STREAM_AND_OUT_STREAM"


class VideoTargetingVideoplayersizetargeting(StrEnum):
    ANY = "ANY"
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    UNKNOWN = "UNKNOWN"


class VideoTargetingVideocompletiontargeting(StrEnum):
    NO_TARGETING = "NO_TARGETING"
    VIDEO_COMPLETION_GTE_10 = "VIDEO_COMPLETION_GTE_10"
    VIDEO_COMPLETION_GTE_20 = "VIDEO_COMPLETION_GTE_20"
    VIDEO_COMPLETION_GTE_30 = "VIDEO_COMPLETION_GTE_30"
    VIDEO_COMPLETION_GTE_40 = "VIDEO_COMPLETION_GTE_40"
    VIDEO_COMPLETION_GTE_50 = "VIDEO_COMPLETION_GTE_50"
    VIDEO_COMPLETION_GTE_60 = "VIDEO_COMPLETION_GTE_60"
    VIDEO_COMPLETION_GTE_70 = "VIDEO_COMPLETION_GTE_70"
    VIDEO_COMPLETION_GTE_80 = "VIDEO_COMPLETION_GTE_80"
    VIDEO_COMPLETION_GTE_90 = "VIDEO_COMPLETION_GTE_90"


class VideoTargeting(BaseModel):
    """This field is available since version `application/vnd.dsplineitems.v2.1+json`."""
    user_location_targeting: Optional["UserLocationTargeting"] = Field(None, alias="userLocationTargeting")
    amazon_viewability_targeting: Optional["AmazonViewabilityTargeting"] = Field(None, alias="amazonViewabilityTargeting")
    third_party_pre_bid_targeting: Optional["ThirdPartyPreBidTargetingV21"] = Field(None, alias="thirdPartyPreBidTargeting")
    supply_targeting: Optional["SupplyTargeting"] = Field(None, alias="supplyTargeting")
    geo_location_targeting: Optional["GeoLocationTargeting"] = Field(None, alias="geoLocationTargeting")
    segment_targeting: Optional["SegmentTargeting"] = Field(None, alias="segmentTargeting")
    day_part_targeting: Optional["DayPartTargeting"] = Field(None, alias="dayPartTargeting")
    domain_list_targeting: Optional["DomainList"] = Field(None, alias="domainListTargeting")
    device_type_targeting: Optional[list[VideoTargetingDevicetypetargeting]] = Field(None, alias="deviceTypeTargeting", description="The targeted device type for video line item type. A list of device types can be provided.")
    mobile_environment_targeting: Optional[list[VideoTargetingMobileenvironmenttargeting]] = Field(None, alias="mobileEnvironmentTargeting", description="The targeted mobile environment for video line item type. It is required only when `MOBILE` device type is selected.")
    site_language_targeting: Optional["SiteLanguageTargeting"] = Field(None, alias="siteLanguageTargeting")
    content_targeting: Optional[list["Identifier"]] = Field(None, alias="contentTargeting", description="The IAB content category type. IAB content categories enable advertisers to target websites according to their subject m")
    video_initiation_type_targeting: Optional[list[VideoTargetingVideoinitiationtypetargeting]] = Field(None, alias="videoInitiationTypeTargeting", description="Target video inventory by how the video will be started. A list can be provided. If ANY is selected, no other type can b")
    video_ad_format_targeting: Optional[list[VideoTargetingVideoadformattargeting]] = Field(None, alias="videoAdFormatTargeting", description="Target a specific type of ad slot used to serve the video. A list can be provided.")
    limit_to_fep_targeting: Optional[bool] = Field(None, alias="limitToFepTargeting", description="Limit IN STREAM ad slot to full episode players (FEP).")
    video_player_size_targeting: Optional[list[VideoTargetingVideoplayersizetargeting]] = Field(None, alias="videoPlayerSizeTargeting", description="Target video inventory by publisher’s player size. A list can be provided.")
    video_completion_targeting: Optional[VideoTargetingVideocompletiontargeting] = Field(None, alias="videoCompletionTargeting", description="These are predictions based on machine learning and aren’t guaranteed. Selecting a higher percentage limits overall reac")
    ott_targeting: Optional["OttTargeting"] = Field(None, alias="ottTargeting")

    model_config = {'populate_by_name': True}


class LineItemTargetingV21(BaseModel):
    video_targeting: Optional["VideoTargeting"] = Field(None, alias="videoTargeting")

    model_config = {'populate_by_name': True}


class LineItemV21(BaseModel):
    line_item_type: Optional["LineItemTypeV21"] = Field(None, alias="lineItemType")
    targeting: Optional["LineItemTargetingV21"] = None

    model_config = {'populate_by_name': True}


class UserLocationTargetingV3(StrEnum):
    CA = "CA"
    MX = "MX"
    BR = "BR"


class MobileDisplayDoubleVerify(BaseModel):
    """Double Verify (DV) is a third party provider for digital ad verification. Double Verify offers technologies that drive high-quality advertising media."""
    fraud_invalid_traffic: Optional["DoubleVerifyFraudInvalidTraffic"] = Field(None, alias="fraudInvalidTraffic")

    model_config = {'populate_by_name': True}


class IasFraudInvalidTraffic(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_RISK = "FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_RISK"
    FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_MODERATE_RISK = "FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_MODERATE_RISK"


class MobileDisplayIntegralAdScience(BaseModel):
    """Integral Ad Science (IAS) is a third party provider in digital ad verification. IAS offers technologies to drive high-quality advertising media."""
    fraud_invalid_traffic: Optional["IasFraudInvalidTraffic"] = Field(None, alias="fraudInvalidTraffic")

    model_config = {'populate_by_name': True}


class MobileDisplayThirdPartyPreBidTargeting(BaseModel):
    """Amazon DSP automatically filters fraudulent and invalid traffic as well as unsafe content using a combination of proprietary technology and solutions from comScore and Sizmek. This service is availabl"""
    double_verify: Optional["MobileDisplayDoubleVerify"] = Field(None, alias="doubleVerify")
    integral_ad_science: Optional["MobileDisplayIntegralAdScience"] = Field(None, alias="integralAdScience")

    model_config = {'populate_by_name': True}


class AmazonMobileDisplayTargetingV3(BaseModel):
    user_location_targeting: Optional["UserLocationTargetingV3"] = Field(None, alias="userLocationTargeting")
    amazon_viewability_targeting: Optional["AmazonViewabilityTargeting"] = Field(None, alias="amazonViewabilityTargeting")
    third_party_pre_bid_targeting: Optional["MobileDisplayThirdPartyPreBidTargeting"] = Field(None, alias="thirdPartyPreBidTargeting")
    supply_targeting: Optional["SupplyTargeting"] = Field(None, alias="supplyTargeting")
    geo_location_targeting: Optional["GeoLocationTargeting"] = Field(None, alias="geoLocationTargeting")
    segment_targeting: Optional["SegmentTargeting"] = Field(None, alias="segmentTargeting")
    day_part_targeting: Optional["DayPartTargeting"] = Field(None, alias="dayPartTargeting")
    mobile_os_targeting: Optional["MobileOsTargeting"] = Field(None, alias="mobileOsTargeting")
    contextual_targeting: Optional[bool] = Field(None, alias="contextualTargeting", description="Set to `true` to enable contextual targeting. Contextual targeting targets the detail page of products that are frequent")

    model_config = {'populate_by_name': True}


class SiteLanguageTargetingV3(StrEnum):
    FR = "FR"
    PT = "PT"


class DvCustomContextualSegmentId(BaseModel):
    """The custom segment identifier."""
    pass


class DvBrandSafetyExcludeApps(BaseModel):
    """Set to `true` to exclude unofficial apps or apps with insufficient user ratings (<100 lifetime)."""
    pass


class DvBrandSafetyAppStarRating(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    APP_STAR_RATING_LT_1_POINT_5_STARS = "APP_STAR_RATING_LT_1_POINT_5_STARS"
    APP_STAR_RATING_LT_2_STARS = "APP_STAR_RATING_LT_2_STARS"
    APP_STAR_RATING_LT_2_POINT_5_STARS = "APP_STAR_RATING_LT_2_POINT_5_STARS"
    APP_STAR_RATING_LT_3_STARS = "APP_STAR_RATING_LT_3_STARS"
    APP_STAR_RATING_LT_3_POINT_5_STARS = "APP_STAR_RATING_LT_3_POINT_5_STARS"
    APP_STAR_RATING_LT_4_STARS = "APP_STAR_RATING_LT_4_STARS"
    APP_STAR_RATING_LT_4_POINT_5_STARS = "APP_STAR_RATING_LT_4_POINT_5_STARS"


class DvBrandSafetyContentCategories(BaseModel):
    """A list of content categories to exclude from targeting."""
    pass


class DvBrandSafetyUnknownContent(BaseModel):
    """Set to `true` to exclude unknown content."""
    pass


class DvBrandSafetyAppAgeRating(BaseModel):
    """A list of app age ratings to be used for excluding apps. For example, `TEENS_12_PLUS` will only exclude apps with content rated for everyone ages 12 and over. `UNKNOWN` will exclude apps with content """
    pass


class BrandSuitabilityRiskLevel(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    HIGH = "HIGH"
    HIGH_MEDIUM = "HIGH_MEDIUM"
    HIGH_MEDIUM_LOW = "HIGH_MEDIUM_LOW"


class DvBrandSafetyContentCategoriesWithRisk(BaseModel):
    """A map from content categories to risk level to exclude from targeting. Available keys are: [`ADULT_CONTENT`, `ALCOHOL`, `CRIME`, `DISASTER_AVIATION`, `DISASTER_MAN_MADE`, `DISASTER_NATURAL`, `DISASTER"""
    __root__: dict[str, "BrandSuitabilityRiskLevel"] = {}


class VideoDoubleVerifyBrandSafety(BaseModel):
    content_categories: Optional["DvBrandSafetyContentCategories"] = Field(None, alias="contentCategories")
    content_categories_with_risk: Optional["DvBrandSafetyContentCategoriesWithRisk"] = Field(None, alias="contentCategoriesWithRisk")
    unknown_content: Optional["DvBrandSafetyUnknownContent"] = Field(None, alias="unknownContent")
    app_age_rating: Optional["DvBrandSafetyAppAgeRating"] = Field(None, alias="appAgeRating")
    app_star_rating: Optional["DvBrandSafetyAppStarRating"] = Field(None, alias="appStarRating")
    exclude_apps_with_insufficient_rating: Optional["DvBrandSafetyExcludeApps"] = Field(None, alias="excludeAppsWithInsufficientRating")

    model_config = {'populate_by_name': True}


class VideoDoubleVerify(BaseModel):
    """Double Verify (DV) is a third party provider for digital ad verification. Double Verify offers technologies that drive high-quality advertising media."""
    brand_safety: Optional["VideoDoubleVerifyBrandSafety"] = Field(None, alias="brandSafety")
    fraud_invalid_traffic: Optional["DoubleVerifyFraudInvalidTraffic"] = Field(None, alias="fraudInvalidTraffic")
    authentic_brand_safety: Optional["DoubleVerifyAuthenticBrandSafety"] = Field(None, alias="authenticBrandSafety")
    viewability: Optional["DoubleVerifyViewabilityV21"] = None
    custom_contextual_segment_id: Optional["DvCustomContextualSegmentId"] = Field(None, alias="customContextualSegmentId")

    model_config = {'populate_by_name': True}


class IasBrandSafetyLevelV3(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    BRAND_SAFETY_EXCLUDE_HIGH_RISK = "BRAND_SAFETY_EXCLUDE_HIGH_RISK"
    BRAND_SAFETY_EXCLUDE_HIGH_AND_MODERATE_RISK = "BRAND_SAFETY_EXCLUDE_HIGH_AND_MODERATE_RISK"


class IasBrandSafetyV3(BaseModel):
    ias_brand_safety_adult: Optional["IasBrandSafetyLevelV3"] = Field(None, alias="iasBrandSafetyAdult")
    ias_brand_safety_alcohol: Optional["IasBrandSafetyLevelV3"] = Field(None, alias="iasBrandSafetyAlcohol")
    ias_brand_safety_gambling: Optional["IasBrandSafetyLevelV3"] = Field(None, alias="iasBrandSafetyGambling")
    ias_brand_safety_hate_speech: Optional["IasBrandSafetyLevelV3"] = Field(None, alias="iasBrandSafetyHateSpeech")
    ias_brand_safety_illegal_downloads: Optional["IasBrandSafetyLevelV3"] = Field(None, alias="iasBrandSafetyIllegalDownloads")
    ias_brand_safety_illegal_drugs: Optional["IasBrandSafetyLevelV3"] = Field(None, alias="iasBrandSafetyIllegalDrugs")
    ias_brand_safety_offensive_language: Optional["IasBrandSafetyLevelV3"] = Field(None, alias="iasBrandSafetyOffensiveLanguage")
    ias_brand_safety_violence: Optional["IasBrandSafetyLevelV3"] = Field(None, alias="iasBrandSafetyViolence")

    model_config = {'populate_by_name': True}


class VideoIntegralAdScience(BaseModel):
    """Integral Ad Science (IAS) is a third party provider in digital ad verification. IAS offers technologies to drive high-quality advertising media."""
    fraud_invalid_traffic: Optional["IasFraudInvalidTraffic"] = Field(None, alias="fraudInvalidTraffic")
    brand_safety: Optional["IasBrandSafetyV3"] = Field(None, alias="brandSafety")
    viewability: Optional["IasViewability"] = None

    model_config = {'populate_by_name': True}


class ODCViewabilityStandard(StrEnum):
    NONE = "NONE"
    MRC = "MRC"


class ODCViewabilityViewabilitytargeting(StrEnum):
    VIEWABILITY_TIER_GT_80 = "VIEWABILITY_TIER_GT_80"
    VIEWABILITY_TIER_GT_70 = "VIEWABILITY_TIER_GT_70"
    VIEWABILITY_TIER_GT_60 = "VIEWABILITY_TIER_GT_60"
    VIEWABILITY_TIER_GT_50 = "VIEWABILITY_TIER_GT_50"
    VIEWABILITY_TIER_GT_40 = "VIEWABILITY_TIER_GT_40"
    VIEWABILITY_TIER_GT_30 = "VIEWABILITY_TIER_GT_30"
    VIEWABILITY_TIER_GT_20 = "VIEWABILITY_TIER_GT_20"


class ODCViewability(BaseModel):
    """The ODC viewability standard."""
    standard: ODCViewabilityStandard = Field(..., description="The viewability standard.")
    viewability_targeting: ODCViewabilityViewabilitytargeting = Field(..., alias="viewabilityTargeting", description="The type of ODC MRC viewability tier.")

    model_config = {'populate_by_name': True}


class OracleDataCloudV3(BaseModel):
    viewability: Optional["ODCViewability"] = None

    model_config = {'populate_by_name': True}


class VideoThirdPartyPreBidTargeting(BaseModel):
    """Amazon DSP automatically filters fraudulent and invalid traffic as well as unsafe content using a combination of proprietary technology and solutions from comScore and Sizmek. This service is availabl"""
    double_verify: Optional["VideoDoubleVerify"] = Field(None, alias="doubleVerify")
    oracle_data_cloud: Optional["OracleDataCloudV3"] = Field(None, alias="oracleDataCloud")
    integral_ad_science: Optional["VideoIntegralAdScience"] = Field(None, alias="integralAdScience")

    model_config = {'populate_by_name': True}


class VideoTargetingV3Devicetypetargeting(StrEnum):
    MOBILE = "MOBILE"
    DESKTOP = "DESKTOP"
    CONNECTED_TV = "CONNECTED_TV"


class VideoTargetingV3Mobileenvironmenttargeting(StrEnum):
    WEB = "WEB"
    APP = "APP"


class VideoTargetingV3Videoinitiationtypetargeting(StrEnum):
    ANY = "ANY"
    USER_INITIATED_ONLY = "USER_INITIATED_ONLY"
    AUTOPLAY_ONLY = "AUTOPLAY_ONLY"
    UNKNOWN = "UNKNOWN"


class VideoTargetingV3Videoadformattargeting(StrEnum):
    IN_STREAM = "IN_STREAM"
    OUT_STREAM = "OUT_STREAM"
    IN_STREAM_AND_OUT_STREAM = "IN_STREAM_AND_OUT_STREAM"


class VideoTargetingV3Videoplayersizetargeting(StrEnum):
    ANY = "ANY"
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    UNKNOWN = "UNKNOWN"


class VideoTargetingV3Videocompletiontargeting(StrEnum):
    NO_TARGETING = "NO_TARGETING"
    VIDEO_COMPLETION_GTE_10 = "VIDEO_COMPLETION_GTE_10"
    VIDEO_COMPLETION_GTE_20 = "VIDEO_COMPLETION_GTE_20"
    VIDEO_COMPLETION_GTE_30 = "VIDEO_COMPLETION_GTE_30"
    VIDEO_COMPLETION_GTE_40 = "VIDEO_COMPLETION_GTE_40"
    VIDEO_COMPLETION_GTE_50 = "VIDEO_COMPLETION_GTE_50"
    VIDEO_COMPLETION_GTE_60 = "VIDEO_COMPLETION_GTE_60"
    VIDEO_COMPLETION_GTE_70 = "VIDEO_COMPLETION_GTE_70"
    VIDEO_COMPLETION_GTE_80 = "VIDEO_COMPLETION_GTE_80"
    VIDEO_COMPLETION_GTE_90 = "VIDEO_COMPLETION_GTE_90"


class VideoTargetingV3(BaseModel):
    """This field is available since version `application/vnd.dsplineitems.v2.1+json`."""
    user_location_targeting: Optional["UserLocationTargetingV3"] = Field(None, alias="userLocationTargeting")
    amazon_viewability_targeting: Optional["AmazonViewabilityTargeting"] = Field(None, alias="amazonViewabilityTargeting")
    third_party_pre_bid_targeting: Optional["VideoThirdPartyPreBidTargeting"] = Field(None, alias="thirdPartyPreBidTargeting")
    supply_targeting: Optional["SupplyTargeting"] = Field(None, alias="supplyTargeting")
    geo_location_targeting: Optional["GeoLocationTargeting"] = Field(None, alias="geoLocationTargeting")
    segment_targeting: Optional["SegmentTargeting"] = Field(None, alias="segmentTargeting")
    day_part_targeting: Optional["DayPartTargeting"] = Field(None, alias="dayPartTargeting")
    domain_list_targeting: Optional["DomainList"] = Field(None, alias="domainListTargeting")
    device_type_targeting: Optional[list[VideoTargetingV3Devicetypetargeting]] = Field(None, alias="deviceTypeTargeting", description="The targeted device type for video line item type. A list of device types can be provided.")
    mobile_environment_targeting: Optional[list[VideoTargetingV3Mobileenvironmenttargeting]] = Field(None, alias="mobileEnvironmentTargeting", description="The targeted mobile environment for video line item type. It is required only when `MOBILE` device type is selected.")
    site_language_targeting: Optional["SiteLanguageTargetingV3"] = Field(None, alias="siteLanguageTargeting")
    content_targeting: Optional[list["Identifier"]] = Field(None, alias="contentTargeting", description="The IAB content category type. IAB content categories enable advertisers to target websites according to their subject m")
    video_initiation_type_targeting: Optional[list[VideoTargetingV3Videoinitiationtypetargeting]] = Field(None, alias="videoInitiationTypeTargeting", description="Target video inventory by how the video will be started. A list can be provided. If ANY is selected, no other type can b")
    video_ad_format_targeting: Optional[list[VideoTargetingV3Videoadformattargeting]] = Field(None, alias="videoAdFormatTargeting", description="Target a specific type of ad slot used to serve the video. A list can be provided.")
    limit_to_fep_targeting: Optional[bool] = Field(None, alias="limitToFepTargeting", description="Limit IN STREAM ad slot to full episode players (FEP).")
    video_player_size_targeting: Optional[list[VideoTargetingV3Videoplayersizetargeting]] = Field(None, alias="videoPlayerSizeTargeting", description="Target video inventory by publisher’s player size. A list can be provided.")
    video_completion_targeting: Optional[VideoTargetingV3Videocompletiontargeting] = Field(None, alias="videoCompletionTargeting", description="These are predictions based on machine learning and aren’t guaranteed. Selecting a higher percentage limits overall reac")
    ott_targeting: Optional["OttTargeting"] = Field(None, alias="ottTargeting")

    model_config = {'populate_by_name': True}


class StandardDisplayDoubleVerifyBrandSafety(BaseModel):
    content_categories: Optional["DvBrandSafetyContentCategories"] = Field(None, alias="contentCategories")
    content_categories_with_risk: Optional["DvBrandSafetyContentCategoriesWithRisk"] = Field(None, alias="contentCategoriesWithRisk")
    unknown_content: Optional["DvBrandSafetyUnknownContent"] = Field(None, alias="unknownContent")

    model_config = {'populate_by_name': True}


class StandardDisplayDoubleVerify(BaseModel):
    """Double Verify (DV) is a third party provider for digital ad verification. Double Verify offers technologies that drive high-quality advertising media."""
    brand_safety: Optional["StandardDisplayDoubleVerifyBrandSafety"] = Field(None, alias="brandSafety")
    fraud_invalid_traffic: Optional["DoubleVerifyFraudInvalidTraffic"] = Field(None, alias="fraudInvalidTraffic")
    authentic_brand_safety: Optional["DoubleVerifyAuthenticBrandSafety"] = Field(None, alias="authenticBrandSafety")
    viewability: Optional["DoubleVerifyViewabilityV21"] = None
    custom_contextual_segment_id: Optional["DvCustomContextualSegmentId"] = Field(None, alias="customContextualSegmentId")

    model_config = {'populate_by_name': True}


class StandardDisplayIntegralAdScience(BaseModel):
    """Integral Ad Science (IAS) is a third party provider in digital ad verification. IAS offers technologies to drive high-quality advertising media."""
    fraud_invalid_traffic: Optional["IasFraudInvalidTraffic"] = Field(None, alias="fraudInvalidTraffic")
    brand_safety: Optional["IasBrandSafetyV3"] = Field(None, alias="brandSafety")
    viewability: Optional["IasViewability"] = None

    model_config = {'populate_by_name': True}


class StandardDisplayThirdPartyPreBidTargeting(BaseModel):
    """Amazon DSP automatically filters fraudulent and invalid traffic as well as unsafe content using a combination of proprietary technology and solutions from comScore and Sizmek. This service is availabl"""
    double_verify: Optional["StandardDisplayDoubleVerify"] = Field(None, alias="doubleVerify")
    oracle_data_cloud: Optional["OracleDataCloudV3"] = Field(None, alias="oracleDataCloud")
    integral_ad_science: Optional["StandardDisplayIntegralAdScience"] = Field(None, alias="integralAdScience")

    model_config = {'populate_by_name': True}


class StandardDisplayTargetingV3Devicetypetargeting(StrEnum):
    DESKTOP_AND_MOBILE = "DESKTOP_AND_MOBILE"
    MOBILE = "MOBILE"
    DESKTOP = "DESKTOP"


class StandardDisplayTargetingV3(BaseModel):
    user_location_targeting: Optional["UserLocationTargetingV3"] = Field(None, alias="userLocationTargeting")
    amazon_viewability_targeting: Optional["AmazonViewabilityTargeting"] = Field(None, alias="amazonViewabilityTargeting")
    third_party_pre_bid_targeting: Optional["StandardDisplayThirdPartyPreBidTargeting"] = Field(None, alias="thirdPartyPreBidTargeting")
    supply_targeting: Optional["SupplyTargeting"] = Field(None, alias="supplyTargeting")
    geo_location_targeting: Optional["GeoLocationTargeting"] = Field(None, alias="geoLocationTargeting")
    segment_targeting: Optional["SegmentTargeting"] = Field(None, alias="segmentTargeting")
    day_part_targeting: Optional["DayPartTargeting"] = Field(None, alias="dayPartTargeting")
    domain_list_targeting: Optional["DomainList"] = Field(None, alias="domainListTargeting")
    device_type_targeting: Optional[StandardDisplayTargetingV3Devicetypetargeting] = Field(None, alias="deviceTypeTargeting", description="The targeted device type for standard display line item type. It is required input for `STANDARD_DISPLAY` line item type")
    mobile_os_targeting: Optional["MobileOsTargeting"] = Field(None, alias="mobileOsTargeting")
    site_language_targeting: Optional["SiteLanguageTargetingV3"] = Field(None, alias="siteLanguageTargeting")
    content_targeting: Optional[list["Identifier"]] = Field(None, alias="contentTargeting", description="The IAB content category type. IAB content categories enable advertisers to target websites according to their subject m")
    contextual_targeting: Optional[bool] = Field(None, alias="contextualTargeting", description="Set to `true` to enable contextual targeting. Contextual targeting targets the detail page of products that are frequent")

    model_config = {'populate_by_name': True}


class MobileAppIntegralAdScience(BaseModel):
    """Integral Ad Science (IAS) is a third party provider in digital ad verification. IAS offers technologies to drive high-quality advertising media."""
    fraud_invalid_traffic: Optional["IasFraudInvalidTraffic"] = Field(None, alias="fraudInvalidTraffic")
    brand_safety: Optional["IasBrandSafetyV3"] = Field(None, alias="brandSafety")

    model_config = {'populate_by_name': True}


class MobileAppDoubleVerifyBrandSafety(BaseModel):
    content_categories: Optional["DvBrandSafetyContentCategories"] = Field(None, alias="contentCategories")
    content_categories_with_risk: Optional["DvBrandSafetyContentCategoriesWithRisk"] = Field(None, alias="contentCategoriesWithRisk")
    unknown_content: Optional["DvBrandSafetyUnknownContent"] = Field(None, alias="unknownContent")
    app_age_rating: Optional["DvBrandSafetyAppAgeRating"] = Field(None, alias="appAgeRating")
    app_star_rating: Optional["DvBrandSafetyAppStarRating"] = Field(None, alias="appStarRating")
    exclude_apps_with_insufficient_rating: Optional["DvBrandSafetyExcludeApps"] = Field(None, alias="excludeAppsWithInsufficientRating")

    model_config = {'populate_by_name': True}


class MobileAppDoubleVerify(BaseModel):
    """Double Verify (DV) is a third party provider for digital ad verification. Double Verify offers technologies that drive high-quality advertising media."""
    brand_safety: Optional["MobileAppDoubleVerifyBrandSafety"] = Field(None, alias="brandSafety")
    fraud_invalid_traffic: Optional["DoubleVerifyFraudInvalidTraffic"] = Field(None, alias="fraudInvalidTraffic")
    authentic_brand_safety: Optional["DoubleVerifyAuthenticBrandSafety"] = Field(None, alias="authenticBrandSafety")
    viewability: Optional["DoubleVerifyViewabilityV21"] = None
    custom_contextual_segment_id: Optional["DvCustomContextualSegmentId"] = Field(None, alias="customContextualSegmentId")

    model_config = {'populate_by_name': True}


class MobileAppThirdPartyPreBidTargeting(BaseModel):
    """Amazon DSP automatically filters fraudulent and invalid traffic as well as unsafe content using a combination of proprietary technology and solutions from comScore and Sizmek. This service is availabl"""
    double_verify: Optional["MobileAppDoubleVerify"] = Field(None, alias="doubleVerify")
    oracle_data_cloud: Optional["OracleDataCloudV3"] = Field(None, alias="oracleDataCloud")
    integral_ad_science: Optional["MobileAppIntegralAdScience"] = Field(None, alias="integralAdScience")

    model_config = {'populate_by_name': True}


class AapMobileAppTargetingV3Devicetypetargeting(StrEnum):
    IPHONE = "IPHONE"
    IPAD = "IPAD"
    ANDROID = "ANDROID"
    KINDLE_FIRE = "KINDLE_FIRE"
    KINDLE_FIRE_HD = "KINDLE_FIRE_HD"


class AapMobileAppTargetingV3Deviceorientationtargeting(StrEnum):
    ANY = "ANY"
    PORTRAIT = "PORTRAIT"
    LANDSCAPE = "LANDSCAPE"


class AapMobileAppTargetingV3(BaseModel):
    user_location_targeting: Optional["UserLocationTargetingV3"] = Field(None, alias="userLocationTargeting")
    amazon_viewability_targeting: Optional["AmazonViewabilityTargeting"] = Field(None, alias="amazonViewabilityTargeting")
    third_party_pre_bid_targeting: Optional["MobileAppThirdPartyPreBidTargeting"] = Field(None, alias="thirdPartyPreBidTargeting")
    supply_targeting: Optional["SupplyTargeting"] = Field(None, alias="supplyTargeting")
    geo_location_targeting: Optional["GeoLocationTargeting"] = Field(None, alias="geoLocationTargeting")
    segment_targeting: Optional["SegmentTargeting"] = Field(None, alias="segmentTargeting")
    day_part_targeting: Optional["DayPartTargeting"] = Field(None, alias="dayPartTargeting")
    mobile_app_targeting: Optional["MobileAppTargeting"] = Field(None, alias="mobileAppTargeting")
    device_type_targeting: Optional[list[AapMobileAppTargetingV3Devicetypetargeting]] = Field(None, alias="deviceTypeTargeting", description="The targeted mobile application device type. Note that this is applicable only for the `AAP_MOBILE APP` type of line ite")
    device_orientation_targeting: Optional[AapMobileAppTargetingV3Deviceorientationtargeting] = Field(None, alias="deviceOrientationTargeting", description="The mobile device orientation targeting type.")

    model_config = {'populate_by_name': True}


class LineItemTargetingV3(BaseModel):
    standard_display_targeting: Optional["StandardDisplayTargetingV3"] = Field(None, alias="standardDisplayTargeting")
    aap_mobile_app_targeting: Optional["AapMobileAppTargetingV3"] = Field(None, alias="aapMobileAppTargeting")
    amazon_mobile_display_targeting: Optional["AmazonMobileDisplayTargetingV3"] = Field(None, alias="amazonMobileDisplayTargeting")
    video_targeting: Optional["VideoTargetingV3"] = Field(None, alias="videoTargeting")

    model_config = {'populate_by_name': True}


class LineItemV3(BaseModel):
    line_item_id: Optional[str] = Field(None, alias="lineItemId", description="The line item identifier. This is required when we perform update operations. Immutable field.")
    line_item_type: "LineItemTypeV21" = Field(..., alias="lineItemType")
    name: str = Field(..., description="The line item name.")
    order_id: str = Field(..., alias="orderId", description="The order to which the line item is associated. Immutable field.")
    external_id: Optional[str] = Field(None, alias="externalId", description="The external identifier of the line item.")
    start_date_time: str = Field(..., alias="startDateTime", description="The line item start date in ISO date format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-07-16T19:20:30+")
    end_date_time: str = Field(..., alias="endDateTime", description="The line item end date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. For example, 2020-07-16T19:20:30+01:00")
    comments: Optional[str] = Field(None, description="The line item comments.")
    delivery_activation_status: Optional["DeliveryActivationStatus"] = Field(None, alias="deliveryActivationStatus")
    delivery_status: Optional["LineItemDeliveryStatus"] = Field(None, alias="deliveryStatus")
    line_item_classification: "LineItemClassification" = Field(..., alias="lineItemClassification")
    frequency_cap: "FrequencyCap" = Field(..., alias="frequencyCap")
    targeting: Optional["LineItemTargetingV3"] = None
    budget: Optional["LineItemBudget"] = None
    currency_code: Optional["CurrencyCodeV3"] = Field(None, alias="currencyCode")
    applied_fees: Optional["AppliedFees"] = Field(None, alias="appliedFees")
    bidding: "Bidding"
    optimization: "LineItemOptimization"
    creative_options: Optional["CreativeOptions"] = Field(None, alias="creativeOptions")
    creation_date: Optional[str] = Field(None, alias="creationDate", description="The line item creation date.")
    last_updated_date: Optional[str] = Field(None, alias="lastUpdatedDate", description="The line item last updated date.")

    model_config = {'populate_by_name': True}


class OracleDataCloudV31(BaseModel):
    standard_predicts_segment_ids: Optional[list[str]] = Field(None, alias="standardPredictsSegmentIds", description="The standard predict segment identifiers.")

    model_config = {'populate_by_name': True}


class PixalateFraudInvalidTraffic(BaseModel):
    exclude_ip_address_and_user_agents: Optional[bool] = Field(None, alias="excludeIpAddressAndUserAgents", description="Set to `true` to exclude traffic from IPV4 and IPV6 addresses and usger agents identified to to be fraudulent or invalid")
    exclude_ott_and_mobile_devices: Optional[bool] = Field(None, alias="excludeOttAndMobileDevices", description="Set to `true` to exclude traffic from OTT and Mobile devices identified to be fraudulent or invalid.")
    exclude_apps_and_domains: Optional[bool] = Field(None, alias="excludeAppsAndDomains", description="Set to `true` to exclude traffic from Apps and Domains identified to be fraudulent or invalid.")
    exclude_removed_apps_from_app_stores: Optional[bool] = Field(None, alias="excludeRemovedAppsFromAppStores", description="Set to `true` to exlude traffic from Apps that have been removed from the google play and apple app stores in the last 6")

    model_config = {'populate_by_name': True}


class Pixalate(BaseModel):
    """Pixalate is a third party provider for digital ad verification. Pixalate offers technologies that drive high-quality advertising media."""
    fraud_invalid_traffic: Optional["PixalateFraudInvalidTraffic"] = Field(None, alias="fraudInvalidTraffic")

    model_config = {'populate_by_name': True}


class StandardDisplayThirdPartyPreBidTargetingV31(BaseModel):
    oracle_data_cloud: Optional["OracleDataCloudV31"] = Field(None, alias="oracleDataCloud")
    pixalate: Optional["Pixalate"] = None

    model_config = {'populate_by_name': True}


class StandardDisplayTargetingV31(BaseModel):
    third_party_pre_bid_targeting: Optional["StandardDisplayThirdPartyPreBidTargetingV31"] = Field(None, alias="thirdPartyPreBidTargeting")

    model_config = {'populate_by_name': True}


class VideoThirdPartyPreBidTargetingV31(BaseModel):
    oracle_data_cloud: Optional["OracleDataCloudV31"] = Field(None, alias="oracleDataCloud")
    pixalate: Optional["Pixalate"] = None

    model_config = {'populate_by_name': True}


class VideoTargetingV31(BaseModel):
    third_party_pre_bid_targeting: Optional["VideoThirdPartyPreBidTargetingV31"] = Field(None, alias="thirdPartyPreBidTargeting")

    model_config = {'populate_by_name': True}


class MobileDisplayThirdPartyPreBidTargetingV31(BaseModel):
    pixalate: Optional["Pixalate"] = None

    model_config = {'populate_by_name': True}


class AmazonMobileDisplayTargetingV31(BaseModel):
    third_party_pre_bid_targeting: Optional["MobileDisplayThirdPartyPreBidTargetingV31"] = Field(None, alias="thirdPartyPreBidTargeting")

    model_config = {'populate_by_name': True}


class MobileAppThirdPartyPreBidTargetingV31(BaseModel):
    oracle_data_cloud: Optional["OracleDataCloudV31"] = Field(None, alias="oracleDataCloud")
    pixalate: Optional["Pixalate"] = None

    model_config = {'populate_by_name': True}


class AapMobileAppTargetingV31(BaseModel):
    third_party_pre_bid_targeting: Optional["MobileAppThirdPartyPreBidTargetingV31"] = Field(None, alias="thirdPartyPreBidTargeting")

    model_config = {'populate_by_name': True}


class LineItemTargetingV31(BaseModel):
    standard_display_targeting: Optional["StandardDisplayTargetingV31"] = Field(None, alias="standardDisplayTargeting")
    aap_mobile_app_targeting: Optional["AapMobileAppTargetingV31"] = Field(None, alias="aapMobileAppTargeting")
    amazon_mobile_display_targeting: Optional["AmazonMobileDisplayTargetingV31"] = Field(None, alias="amazonMobileDisplayTargeting")
    video_targeting: Optional["VideoTargetingV31"] = Field(None, alias="videoTargeting")

    model_config = {'populate_by_name': True}


class LineItemV31(BaseModel):
    targeting: Optional["LineItemTargetingV31"] = None

    model_config = {'populate_by_name': True}


class DvBrandSafetyContentCategoriesWithRiskV32(BaseModel):
    """A map from content categories to risk level to exclude from targeting. Available keys are: [`ADULT_CONTENT`, `ALCOHOL`, `CRIME`, `DEATH_INJURIES`, `DISASTER_AVIATION`, `DISASTER_MAN_MADE`, `DISASTER_N"""
    __root__: dict[str, "BrandSuitabilityRiskLevel"] = {}


class DvBrandSafetyContentCategoriesV32(BaseModel):
    """A list of content categories to exclude from targeting. EXTREME_GRAPHIC is available since version `application/vnd.dsplineitems.v3.2+json`."""
    pass


class VideoDoubleVerifyBrandSafetyV32(BaseModel):
    content_categories: Optional["DvBrandSafetyContentCategoriesV32"] = Field(None, alias="contentCategories")
    content_categories_with_risk: Optional["DvBrandSafetyContentCategoriesWithRiskV32"] = Field(None, alias="contentCategoriesWithRisk")

    model_config = {'populate_by_name': True}


class VideoDoubleVerifyV32(BaseModel):
    brand_safety: Optional["VideoDoubleVerifyBrandSafetyV32"] = Field(None, alias="brandSafety")

    model_config = {'populate_by_name': True}


class VideoThirdPartyPreBidTargetingV32(BaseModel):
    double_verify: Optional["VideoDoubleVerifyV32"] = Field(None, alias="doubleVerify")

    model_config = {'populate_by_name': True}


class VideoTargetingV32(BaseModel):
    third_party_pre_bid_targeting: Optional["VideoThirdPartyPreBidTargetingV32"] = Field(None, alias="thirdPartyPreBidTargeting")

    model_config = {'populate_by_name': True}


class StandardDisplayDoubleVerifyBrandSafetyV32(BaseModel):
    content_categories: Optional["DvBrandSafetyContentCategoriesV32"] = Field(None, alias="contentCategories")
    content_categories_with_risk: Optional["DvBrandSafetyContentCategoriesWithRiskV32"] = Field(None, alias="contentCategoriesWithRisk")

    model_config = {'populate_by_name': True}


class StandardDisplayDoubleVerifyV32(BaseModel):
    brand_safety: Optional["StandardDisplayDoubleVerifyBrandSafetyV32"] = Field(None, alias="brandSafety")

    model_config = {'populate_by_name': True}


class StandardDisplayThirdPartyPreBidTargetingV32(BaseModel):
    double_verify: Optional["StandardDisplayDoubleVerifyV32"] = Field(None, alias="doubleVerify")

    model_config = {'populate_by_name': True}


class StandardDisplayTargetingV32(BaseModel):
    third_party_pre_bid_targeting: Optional["StandardDisplayThirdPartyPreBidTargetingV32"] = Field(None, alias="thirdPartyPreBidTargeting")

    model_config = {'populate_by_name': True}


class MobileAppDoubleVerifyBrandSafetyV32(BaseModel):
    content_categories: Optional["DvBrandSafetyContentCategoriesV32"] = Field(None, alias="contentCategories")
    content_categories_with_risk: Optional["DvBrandSafetyContentCategoriesWithRiskV32"] = Field(None, alias="contentCategoriesWithRisk")

    model_config = {'populate_by_name': True}


class MobileAppDoubleVerifyV32(BaseModel):
    brand_safety: Optional["MobileAppDoubleVerifyBrandSafetyV32"] = Field(None, alias="brandSafety")

    model_config = {'populate_by_name': True}


class MobileAppThirdPartyPreBidTargetingV32(BaseModel):
    double_verify: Optional["MobileAppDoubleVerifyV32"] = Field(None, alias="doubleVerify")

    model_config = {'populate_by_name': True}


class AapMobileAppTargetingV32(BaseModel):
    third_party_pre_bid_targeting: Optional["MobileAppThirdPartyPreBidTargetingV32"] = Field(None, alias="thirdPartyPreBidTargeting")

    model_config = {'populate_by_name': True}


class LineItemTargetingV32(BaseModel):
    standard_display_targeting: Optional["StandardDisplayTargetingV32"] = Field(None, alias="standardDisplayTargeting")
    aap_mobile_app_targeting: Optional["AapMobileAppTargetingV32"] = Field(None, alias="aapMobileAppTargeting")
    amazon_mobile_display_targeting: Optional["AmazonMobileDisplayTargetingV31"] = Field(None, alias="amazonMobileDisplayTargeting")
    video_targeting: Optional["VideoTargetingV32"] = Field(None, alias="videoTargeting")

    model_config = {'populate_by_name': True}


class LineItemV32(BaseModel):
    targeting: Optional["LineItemTargetingV32"] = None

    model_config = {'populate_by_name': True}


class DspIasContextualControlTargetingV33(BaseModel):
    vertical_segments: Optional[list[str]] = Field(None, alias="verticalSegments")
    topical_segments: Optional[list[str]] = Field(None, alias="topicalSegments")

    model_config = {'populate_by_name': True}


class DspIasContextualControlAvoidanceV33(BaseModel):
    avoidance_segments: Optional[list[str]] = Field(None, alias="avoidanceSegments")

    model_config = {'populate_by_name': True}


class StandardDisplayIntegralAdScienceV33(BaseModel):
    contextual_targeting: Optional["DspIasContextualControlAvoidanceV33"] = Field(None, alias="contextualTargeting")
    contextual_avoidance: Optional["DspIasContextualControlTargetingV33"] = Field(None, alias="contextualAvoidance")

    model_config = {'populate_by_name': True}


class StandardDisplayThirdPartyPreBidTargetingV33(BaseModel):
    integral_ad_science: Optional["StandardDisplayIntegralAdScienceV33"] = Field(None, alias="integralAdScience")

    model_config = {'populate_by_name': True}


class StandardDisplayTargetingV33(BaseModel):
    third_party_pre_bid_targeting: Optional["StandardDisplayThirdPartyPreBidTargetingV33"] = Field(None, alias="thirdPartyPreBidTargeting")

    model_config = {'populate_by_name': True}


class MobileAppIntegralAdScienceV33(BaseModel):
    contextual_targeting: Optional["DspIasContextualControlAvoidanceV33"] = Field(None, alias="contextualTargeting")
    contextual_avoidance: Optional["DspIasContextualControlTargetingV33"] = Field(None, alias="contextualAvoidance")

    model_config = {'populate_by_name': True}


class MobileAppThirdPartyPreBidTargetingV33(BaseModel):
    integral_ad_science: Optional["MobileAppIntegralAdScienceV33"] = Field(None, alias="integralAdScience")

    model_config = {'populate_by_name': True}


class AapMobileAppTargetingV33(BaseModel):
    third_party_pre_bid_targeting: Optional["MobileAppThirdPartyPreBidTargetingV33"] = Field(None, alias="thirdPartyPreBidTargeting")

    model_config = {'populate_by_name': True}


class VideoIntegralAdScienceV33(BaseModel):
    contextual_targeting: Optional["DspIasContextualControlAvoidanceV33"] = Field(None, alias="contextualTargeting")
    contextual_avoidance: Optional["DspIasContextualControlTargetingV33"] = Field(None, alias="contextualAvoidance")

    model_config = {'populate_by_name': True}


class VideoThirdPartyPreBidTargetingV33(BaseModel):
    integral_ad_science: Optional["VideoIntegralAdScienceV33"] = Field(None, alias="integralAdScience")

    model_config = {'populate_by_name': True}


class VideoTargetingV33(BaseModel):
    third_party_pre_bid_targeting: Optional["VideoThirdPartyPreBidTargetingV33"] = Field(None, alias="thirdPartyPreBidTargeting")

    model_config = {'populate_by_name': True}


class LineItemTargetingV33(BaseModel):
    standard_display_targeting: Optional["StandardDisplayTargetingV33"] = Field(None, alias="standardDisplayTargeting")
    aap_mobile_app_targeting: Optional["AapMobileAppTargetingV33"] = Field(None, alias="aapMobileAppTargeting")
    amazon_mobile_display_targeting: Optional["AmazonMobileDisplayTargetingV31"] = Field(None, alias="amazonMobileDisplayTargeting")
    video_targeting: Optional["VideoTargetingV33"] = Field(None, alias="videoTargeting")

    model_config = {'populate_by_name': True}


class LineItemV33(BaseModel):
    targeting: Optional["LineItemTargetingV33"] = None

    model_config = {'populate_by_name': True}


class LineItemResponse(BaseModel):
    """Response for the line item create/update operations. Success contains only lineItemId and failure contains only errorDetails corresponding to that requested index in that batch (array of items)."""
    line_item_id: Optional[str] = Field(None, alias="lineItemId", description="The Line item identifier.")
    error_details: Optional["Error"] = Field(None, alias="errorDetails")

    model_config = {'populate_by_name': True}


class SupportedLineItemTypes(StrEnum):
    STANDARD_DISPLAY = "STANDARD_DISPLAY"
    AMAZON_MOBILE_DISPLAY = "AMAZON_MOBILE_DISPLAY"
    AAP_MOBILE_APP = "AAP_MOBILE_APP"
    VIDEO = "VIDEO"


class Creative(BaseModel):
    advertiser_id: Optional[str] = Field(None, alias="advertiserId", description="The identifier of the advertiser.")
    creative_id: Optional[str] = Field(None, alias="creativeId", description="The identifier of the creative.")
    type_: Optional[str] = Field(None, alias="type", description="The creative type.")
    name: Optional[str] = Field(None, description="The creative name.")
    external_id: Optional[str] = Field(None, alias="externalId", description="The external identifier of the creative.")
    size: Optional[str] = Field(None, description="The creative size.")
    supported_line_item_types: Optional[list["SupportedLineItemTypes"]] = Field(None, alias="supportedLineItemTypes", description="Supported lineItemTypes where creatives can be associated. VIDEO line item type is supported since version `application/")

    model_config = {'populate_by_name': True}


class Creatives(BaseModel):
    total_results: Optional[int] = Field(None, alias="totalResults", description="Total number of results which satisfy the filtering criteria. This will help to support pagination.")
    response: Optional[list["Creative"]] = None

    model_config = {'populate_by_name': True}


class DealInfoDealtype(StrEnum):
    PREFERRED_DEAL = "PREFERRED_DEAL"
    PRIVATE_AUCTION = "PRIVATE_AUCTION"


class DealInfo(BaseModel):
    """Deal metadata present only for the DEAL type."""
    deal_type: Optional[DealInfoDealtype] = Field(None, alias="dealType")
    deal_group: Optional[str] = Field(None, alias="dealGroup")
    publisher_name: Optional[str] = Field(None, alias="publisherName")
    deal_price: Optional[int] = Field(None, alias="dealPrice", description="Price of the deal")
    start_date: Optional[str] = Field(None, alias="startDate")
    end_date: Optional[str] = Field(None, alias="endDate")
    exchange_name: Optional[str] = Field(None, alias="exchangeName", description="The name of the supply source item to which the deal belongs. If deal belongs to OPEN_EXCHANGE, it is the name of the co")

    model_config = {'populate_by_name': True}


class SupplySourceSupplysourcetype(StrEnum):
    AMAZON_EXCLUSIVE = "AMAZON_EXCLUSIVE"
    OPEN_EXCHANGE = "OPEN_EXCHANGE"
    DEAL = "DEAL"


class SupplySource(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="ID of the supply source item. For OPEN_EXCHANGE type, it is ID of the consolidated supply source item.")
    name: Optional[str] = Field(None, description="The name of the supply source item. For OPEN_EXCHANGE type, it is the name of the consolidated supply source item.")
    supply_source_type: Optional[SupplySourceSupplysourcetype] = Field(None, alias="supplySourceType", description="Type of this item")
    deal_info: Optional["DealInfo"] = Field(None, alias="dealInfo")

    model_config = {'populate_by_name': True}


class SupplySourceResponse(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken")
    supply_sources: Optional[list["SupplySource"]] = Field(None, alias="supplySources", description="Array of supply source items sorted by deal start time (if available) then ID, ascending.")

    model_config = {'populate_by_name': True}


class DealFeeFeecalculationtype(StrEnum):
    FIXED_CPM = "FIXED_CPM"
    FLOOR_RATE = "FLOOR_RATE"


class DealFee(BaseModel):
    """The fee associated with the deal. This will be the same value as deal price, but includes more information such as currency code."""
    amount: Optional[int] = Field(None, description="The price agreed upon with the publisher. Given in base currency units multiplied by scaling factor ('scale').")
    currency: Optional[str] = Field(None, description="Base currency, such as US Dollar, given in ISO 4217.")
    scale: Optional[int] = Field(None, description="Scale of the amount relative to the base currency unit. For instance, if the scale is 100000, the currency is USD, and t")
    fee_calculation_type: Optional[DealFeeFeecalculationtype] = Field(None, alias="feeCalculationType", description="How the fee is applied.")

    model_config = {'populate_by_name': True}


class DealInfoV11(BaseModel):
    deal_fee: Optional["DealFee"] = Field(None, alias="dealFee")

    model_config = {'populate_by_name': True}


class SupplySourceResponseV11(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken")
    supply_sources: Optional[list["SupplySource"]] = Field(None, alias="supplySources", description="Array of supply source items sorted by deal start time (if available) then ID, ascending.")

    model_config = {'populate_by_name': True}


class DealInfoV12(BaseModel):
    pass


class SupplySourceResponseV12(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken")
    supply_sources: Optional[list["SupplySource"]] = Field(None, alias="supplySources", description="Array of supply source items sorted by deal start time (if available) then ID, ascending.")

    model_config = {'populate_by_name': True}


class DspAssetV1(BaseModel):
    """Asset to be associated with creative."""
    asset_id: str = Field(..., alias="assetId", description="The uploaded asset Id. This Id is provided by Creative Assets API when user registers an asset with assetType after uplo")
    version: str = Field(..., description="The uploaded asset version. This version is provided by Creative Assets API when user registers an asset with assetType ")
    url: Optional[str] = Field(None, description="The asset's URL. This will be provided if asset linked with the creative being read is not registered in Creative Assets")

    model_config = {'populate_by_name': True}


class DspSizeV1(BaseModel):
    """Size of the creative."""
    width: int = Field(..., description="The creative width in pixels.")
    height: int = Field(..., description="The creative height in pixels.")

    model_config = {'populate_by_name': True}


class DspThirdPartyTrackerTypeV1(StrEnum):
    IMPRESSION = "IMPRESSION"


class DspThirdPartyTrackerV1(BaseModel):
    """Trackers used for tracking interactions with third party"""
    type_: "DspThirdPartyTrackerTypeV1" = Field(..., alias="type")
    tracker_url: str = Field(..., alias="trackerUrl", description="URL used for tracking interactions with third party")

    model_config = {'populate_by_name': True}


class DspClickThroughKindleAppDownloadActionV1(BaseModel):
    """Click through Action - Kindle App Download. This is applicable only to `MOBILE_AAP` supply."""
    product_asin: str = Field(..., alias="productAsin", description="Amazon product Asin, used to build the download URL.")
    download_url: Optional[str] = Field(None, alias="downloadUrl", description="URL to direct users to download app. By default, this will be built automatically using `productAsin` information provid")

    model_config = {'populate_by_name': True}


class DspCustomUrlActionV1(BaseModel):
    """Click through Action - Custom Url."""
    url: str = Field(..., description="Define where the creative links to on click.")

    model_config = {'populate_by_name': True}


class DspClickThroughSearchAsinActionV1(BaseModel):
    """Click through Action - Search Asins. This is applicable only to `MOBILE_AAP` and `MOBILE_OO` supply."""
    product_asins: list[str] = Field(..., alias="productAsins", description="Define the Asins to query for in the search results that will be displayed on click-through.")
    enable_deep_linking: Optional[bool] = Field(None, alias="enableDeepLinking", description="Allow to open URL in Amazon App, if available on device. This will be considered only for `MOBILE_AAP` supply. Default v")

    model_config = {'populate_by_name': True}


class DspClickThroughDetailPageActionV1(BaseModel):
    """Click through Action - Detail Page. This is applicable only to `MOBILE_OO` and `MOBILE_AAP` supply."""
    product_asin: str = Field(..., alias="productAsin", description="Define which product's detail page the customer should be taken to when tapping on the creative.")
    enable_deep_linking: Optional[bool] = Field(None, alias="enableDeepLinking", description="Allow to open URL in Amazon App, if available on device. By default it is false. This will be considered only for `MOBIL")

    model_config = {'populate_by_name': True}


class DspClickThroughAndroidAppDownloadActionV1Storepriority(StrEnum):
    PLAY_STORE_THEN_AMAZON_APP_STORE = "PLAY_STORE_THEN_AMAZON_APP_STORE"
    AMAZON_APP_STORE_THEN_PLAY_STORE = "AMAZON_APP_STORE_THEN_PLAY_STORE"


class DspClickThroughAndroidAppDownloadActionV1(BaseModel):
    """To target Android app download as click through action, at least `storeId`, `productAsin` or `downloadUrl` must be provided. If both `storeId` and `productAsin` is provided, `storePriority` must be pr"""
    is_rtb: Optional[bool] = Field(None, alias="isRtb", description="Indicates whether it's for real time bidding or not. Default value is `false`. This is applicable only to `MOBILE_AAP` s")
    store_id: Optional[str] = Field(None, alias="storeId", description="Android play store Id for app, used to build the download URL.")
    product_asin: Optional[str] = Field(None, alias="productAsin", description="Amazon product Asin, used to build the download URL. This is applicable only to `MOBILE_AAP` supply.")
    store_priority: Optional[DspClickThroughAndroidAppDownloadActionV1Storepriority] = Field(None, alias="storePriority", description="The higher priority store will be tried first, then if it does not exist on device the second store will be tried. Defau")
    download_url: Optional[str] = Field(None, alias="downloadUrl", description="URL to direct users to download app. By default, This will be built automatically using `playStoreId` and `productAsin` ")

    model_config = {'populate_by_name': True}


class DspClickThroughSearchKeywordActionV1(BaseModel):
    """Click through action - Search Keywords. This is applicable only to `MOBILE_AAP` and `MOBILE_OO` supply."""
    keywords: list[str] = Field(..., description="Define the keywords to query for in the search results that will be displayed on click-through.")
    enable_deep_linking: Optional[bool] = Field(None, alias="enableDeepLinking", description="Allow to open URL in Amazon App, if available on device. This will be considered only for `MOBILE_AAP` supply. By defaul")

    model_config = {'populate_by_name': True}


class DspClickThroughIosAppDownloadActionV1(BaseModel):
    """Click through action - IOS App Download. This is applicable only to `MOBILE_AAP` supply."""
    store_link: str = Field(..., alias="storeLink", description="Apple app store link for app, used to build the download URL.")
    download_url: Optional[str] = Field(None, alias="downloadUrl", description="URL to direct users to download app. By default, This will be built automatically using `storeLink` information provided")

    model_config = {'populate_by_name': True}


class DspImageClickThroughActionV1(BaseModel):
    """Image's click through action which can have any one of the following properties. One action and one action alone must be provided."""
    custom_url: Optional["DspCustomUrlActionV1"] = Field(None, alias="customUrl")
    detail_page: Optional["DspClickThroughDetailPageActionV1"] = Field(None, alias="detailPage")
    search_asin: Optional["DspClickThroughSearchAsinActionV1"] = Field(None, alias="searchAsin")
    search_keyword: Optional["DspClickThroughSearchKeywordActionV1"] = Field(None, alias="searchKeyword")
    android_app_download: Optional["DspClickThroughAndroidAppDownloadActionV1"] = Field(None, alias="androidAppDownload")
    ios_app_download: Optional["DspClickThroughIosAppDownloadActionV1"] = Field(None, alias="iosAppDownload")
    kindle_app_download: Optional["DspClickThroughKindleAppDownloadActionV1"] = Field(None, alias="kindleAppDownload")

    model_config = {'populate_by_name': True}


class DspAdChoicesPositionV1(StrEnum):
    TOP_RIGHT = "TOP_RIGHT"
    TOP_LEFT = "TOP_LEFT"
    BOTTOM_RIGHT = "BOTTOM_RIGHT"
    BOTTOM_LEFT = "BOTTOM_LEFT"


class DspReadWriteImageCreativeAttributesV1(BaseModel):
    """This holds common properties that can we written and updated for image creative."""
    external_id: Optional[str] = Field(None, alias="externalId", description="The creative external Id.")
    size: "DspSizeV1"
    asset: "DspAssetV1"
    click_through_action: "DspImageClickThroughActionV1" = Field(..., alias="clickThroughAction")
    third_party_click_trackers: Optional[list[str]] = Field(None, alias="thirdPartyClickTrackers", description="This URL is pinged when the creative is clicked. The URL can contain macros.")
    third_party_trackers: Optional[list["DspThirdPartyTrackerV1"]] = Field(None, alias="thirdPartyTrackers")
    additional_html: Optional[str] = Field(None, alias="additionalHtml", description="Add HTML to the creative for surveys or other arbitrary HTML.")
    ad_choices_position: Optional["DspAdChoicesPositionV1"] = Field(None, alias="adChoicesPosition")

    model_config = {'populate_by_name': True}


class DspCreativeMarketplaceV1(StrEnum):
    US = "US"


class DspBaseWriteCreativeV1(BaseModel):
    """This holds common mutable properties of all creative types update request."""
    name: str = Field(..., description="The creative name.")

    model_config = {'populate_by_name': True}


class DspBaseCreateCreativeRequestV1(BaseModel):
    pass


class DspCreativeSupplyV1(StrEnum):
    DESKTOP = "DESKTOP"
    MOBILE_OO = "MOBILE_OO"
    MOBILE_AAP = "MOBILE_AAP"


class DspImageCreativeSupplyV1(BaseModel):
    pass


class DspCreateImageCreativeRequestV1(BaseModel):
    pass


class DspCreateImageCreativesRequestV1(BaseModel):
    """Create image creatives request."""
    pass


class DspBaseUpdateCreativeRequestV1(BaseModel):
    pass


class DspUpdateImageCreativeRequestV1(BaseModel):
    """Update image creative request"""
    pass


class DspUpdateImageCreativesRequestV1(BaseModel):
    """Update image creatives request."""
    pass


class DspCreativeApprovalStatusV1(StrEnum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    NOT_APPROVED = "NOT_APPROVED"
    WAITING_FOR_LINEITEM = "WAITING_FOR_LINEITEM"
    APPROVED_WITH_EXCEPTIONS = "APPROVED_WITH_EXCEPTIONS"


class DspBaseReadCreativeV1(BaseModel):
    """This holds common read-only properties of all creative types."""
    approval_status: Optional["DspCreativeApprovalStatusV1"] = Field(None, alias="approvalStatus")
    created_date: Optional[str] = Field(None, alias="createdDate", description="The creative created date.")
    last_updated_date: Optional[str] = Field(None, alias="lastUpdatedDate", description="The creative last updated date.")

    model_config = {'populate_by_name': True}


class DspImageCreativeV1(BaseModel):
    pass


class DspReadImageCreativesResponseV1(BaseModel):
    """Read image creatives response."""
    creatives: Optional[list["DspImageCreativeV1"]] = None

    model_config = {'populate_by_name': True}


class DspCreativeResponseV1(BaseModel):
    """Response for the creative create/update operations. If operation is successful, it contains only creativeId. If it is a failure, it contains only errorDetails."""
    creative_id: Optional[str] = Field(None, alias="creativeId", description="The creative Id.")
    error_details: Optional["Error"] = Field(None, alias="errorDetails")

    model_config = {'populate_by_name': True}


class DspImageCreativesResponseV1(BaseModel):
    """Create/Update operation's image creatives response."""
    pass


class DspImageCreativePreviewModelV1(BaseModel):
    """Image creative preview model. Populate this to preview a new creative."""
    marketplace: "DspCreativeMarketplaceV1"
    supply: "DspImageCreativeSupplyV1"
    size: "DspSizeV1"
    asset: "DspAssetV1"
    click_through_action: Optional["DspImageClickThroughActionV1"] = Field(None, alias="clickThroughAction")
    additional_html: Optional[str] = Field(None, alias="additionalHtml", description="Add HTML to the creative for surveys or other arbitrary HTML.")
    ad_choices_position: "DspAdChoicesPositionV1" = Field(..., alias="adChoicesPosition")
    third_party_click_trackers: Optional[list[str]] = Field(None, alias="thirdPartyClickTrackers", description="This URL is pinged when the creative is clicked. The URL can contain macros.")
    third_party_trackers: Optional[list["DspThirdPartyTrackerV1"]] = Field(None, alias="thirdPartyTrackers")

    model_config = {'populate_by_name': True}


class DspPreviewConfigurationV1(BaseModel):
    """Configuration settings for preview"""
    is_on_amazon: Optional[bool] = Field(None, alias="isOnAmazon", description="If it's true, shows preview in amazon websites, else shows in other websites")

    model_config = {'populate_by_name': True}


class DspImageCreativePreviewRequestV1(BaseModel):
    """Image creative preview request. Either `creativeId` or `creativeModel` must be provided, but not both."""
    creative_id: Optional[str] = Field(None, alias="creativeId", description="The creative Id.")
    creative_model: Optional["DspImageCreativePreviewModelV1"] = Field(None, alias="creativeModel")
    preview_configuration: Optional["DspPreviewConfigurationV1"] = Field(None, alias="previewConfiguration")

    model_config = {'populate_by_name': True}


class DspVideoClickThroughActionV1(BaseModel):
    """Click through action for video creatives"""
    custom_url: Optional["DspCustomUrlActionV1"] = Field(None, alias="customUrl")

    model_config = {'populate_by_name': True}


class DspReadWriteVideoCreativeAttributesV1(BaseModel):
    """This holds common properties that can we written and updated for video creative"""
    external_id: Optional[str] = Field(None, alias="externalId", description="The creative external identifier.")
    asset: "DspAssetV1"
    click_through_action: "DspVideoClickThroughActionV1" = Field(..., alias="clickThroughAction")
    third_party_trackers: Optional[list["DspThirdPartyTrackerV1"]] = Field(None, alias="thirdPartyTrackers")

    model_config = {'populate_by_name': True}


class DspCreateVideoCreativeRequestV1(BaseModel):
    """Create video creative request"""
    pass


class DspCreateVideoCreativesRequestV1(BaseModel):
    """Create video creatives request."""
    pass


class DspUpdateVideoCreativeRequestV1(BaseModel):
    """Update video creative request"""
    pass


class DspUpdateVideoCreativesRequestV1(BaseModel):
    """Update video creatives request"""
    pass


class DspVideoCreativeV1(BaseModel):
    pass


class DspReadVideoCreativesResponseV1(BaseModel):
    """Read video creatives response."""
    creatives: Optional[list["DspVideoCreativeV1"]] = None

    model_config = {'populate_by_name': True}


class DspVideoCreativesResponseV1(BaseModel):
    """Create/Update operation's video creatives response."""
    pass


class DspVideoCreativePreviewModelV1(BaseModel):
    """Video creative preview model. Populate this to preview a new creative."""
    marketplace: "DspCreativeMarketplaceV1"
    asset: "DspAssetV1"
    click_through_action: Optional["DspVideoClickThroughActionV1"] = Field(None, alias="clickThroughAction")
    third_party_trackers: Optional[list["DspThirdPartyTrackerV1"]] = Field(None, alias="thirdPartyTrackers")

    model_config = {'populate_by_name': True}


class DspVideoCreativePreviewRequestV1(BaseModel):
    """Video creative preview request. Either `creativeId` or `creativeModel` must be provided, but not both."""
    creative_id: Optional[str] = Field(None, alias="creativeId", description="The creative Id.")
    creative_model: Optional["DspVideoCreativePreviewModelV1"] = Field(None, alias="creativeModel")

    model_config = {'populate_by_name': True}


class DspRecFormatV1(StrEnum):
    SHOP_NOW = "SHOP_NOW"
    ADD_TO_CART = "ADD_TO_CART"
    COUPON = "COUPON"


class DspRecProductV1(BaseModel):
    """The object representation of a product."""
    asin: str = Field(..., description="Amazon standard identification number.")
    product_title: Optional[str] = Field(None, alias="productTitle", description="Retail product title.")

    model_config = {'populate_by_name': True}


class DspRecContentV1Logoheadline(BaseModel):
    """Creative customization field for displaying brandlogo and headline."""
    brand_logo: "DspAssetV1" = Field(..., alias="brandLogo")
    headline: Optional[str] = Field(None, description="Creative customization field for displaying headline.")

    model_config = {'populate_by_name': True}


class DspRecContentV1(BaseModel):
    """Responsive eCommerce creative field for displaying customized content. Provide either Background or LogoHeadline but not both."""
    background: Optional[list["DspAssetV1"]] = Field(None, description="Creative customization field for displaying custom images.")
    logo_headline: Optional["DspRecContentV1Logoheadline"] = Field(None, alias="logoHeadline", description="Creative customization field for displaying brandlogo and headline.")

    model_config = {'populate_by_name': True}


class DspRecOptimizationGoalV1(StrEnum):
    PURCHASE_RATE = "PURCHASE_RATE"
    CLICK_THROUGH_RATE = "CLICK_THROUGH_RATE"
    DETAIL_PAGE_VIEW_RATE = "DETAIL_PAGE_VIEW_RATE"


class DspReadWriteRecCreativeAttributesV1(BaseModel):
    """This holds common properties that can we written and updated for REC creative."""
    additional_html: Optional[str] = Field(None, alias="additionalHtml", description="Add HTML to the creative for surveys or other arbitrary HTML.")
    allow_third_party_sellers: Optional[bool] = Field(None, alias="allowThirdPartySellers", description="If it's true, orders can be fulfilled by third party sellers.")
    content: Optional["DspRecContentV1"] = None
    allowed_formats: Optional[list["DspRecFormatV1"]] = Field(None, alias="allowedFormats", description="A list of formats configured to display for the creative.")
    optimization_goal: Optional["DspRecOptimizationGoalV1"] = Field(None, alias="optimizationGoal")
    allowed_sizes: Optional[list["DspSizeV1"]] = Field(None, alias="allowedSizes", description="A list of sizes configured to display for the creative. This overrides the default REC supported sizes.")
    associated_products: list["DspRecProductV1"] = Field(..., alias="associatedProducts", description="Product objects associated with the creative.")
    third_party_click_trackers: Optional[list[str]] = Field(None, alias="thirdPartyClickTrackers", description="This URL is pinged when the creative is clicked. The URL can contain macros.")
    third_party_trackers: Optional[list["DspThirdPartyTrackerV1"]] = Field(None, alias="thirdPartyTrackers", description="URL used for tracking interactions with third party")

    model_config = {'populate_by_name': True}


class DspCreateRecCreativeRequestV1(BaseModel):
    """Create Responsive eCommerce creative (REC) request."""
    pass


class DspCreateRecCreativesRequestV1(BaseModel):
    """Create Responsive eCommerce creatives (REC) request."""
    pass


class DspUpdateRecCreativeRequestV1(BaseModel):
    """Update Responsive eCommerce creative (REC) request."""
    pass


class DspUpdateRecCreativesRequestV1(BaseModel):
    """Update Responsive eCommerce creatives (REC) request."""
    pass


class DspRecCreativeV1(BaseModel):
    pass


class DspReadRecCreativesResponseV1(BaseModel):
    """Read Responsive eCommerce creative (REC) creatives response."""
    creatives: Optional[list["DspRecCreativeV1"]] = None

    model_config = {'populate_by_name': True}


class DspRecCreativesResponseV1(BaseModel):
    """Create/Update operation's rec creatives response."""
    pass


class DspRecPreviewConfigurationV1(BaseModel):
    pass


class DspRecCreativePreviewModelV1(BaseModel):
    """Responsive eCommerce Creative preview model. Populate this to preview a new creative."""
    content: Optional["DspRecContentV1"] = None
    marketplace: "DspCreativeMarketplaceV1"
    third_party_click_trackers: Optional[list[str]] = Field(None, alias="thirdPartyClickTrackers", description="This URL is pinged when the creative is clicked. The URL can contain macros.")
    third_party_trackers: Optional[list["DspThirdPartyTrackerV1"]] = Field(None, alias="thirdPartyTrackers")

    model_config = {'populate_by_name': True}


class DspRecCreativePreviewRequestV1(BaseModel):
    """Responsive eCommerce creative preview request. Either `creativeId` or `creativeModel` must be provided, but not both."""
    creative_id: Optional[str] = Field(None, alias="creativeId", description="The identifier of the creative.")
    creative_model: Optional["DspRecCreativePreviewModelV1"] = Field(None, alias="creativeModel")
    preview_configuration: "DspRecPreviewConfigurationV1" = Field(..., alias="previewConfiguration")

    model_config = {'populate_by_name': True}


class DspCreativeModerationV1(BaseModel):
    """The creative moderation summary."""
    creative_id: Optional[str] = Field(None, alias="creativeId")
    status: Optional["DspCreativeApprovalStatusV1"] = None
    reasons: Optional[list[str]] = Field(None, description="The reasons why creative is not approved.")
    additional_notes: Optional[list[str]] = Field(None, alias="additionalNotes", description="The additional notes.")

    model_config = {'populate_by_name': True}


class DspClickThroughDestinationV1(StrEnum):
    AMAZON = "AMAZON"
    OTHER = "OTHER"


class DspReadWriteThirdPartyCreativeAttributesV1(BaseModel):
    """This holds common properties that can we written and updated for Third Party creative."""
    external_id: Optional[str] = Field(None, alias="externalId", description="The creative external Id.")
    size: "DspSizeV1"
    tag_source: str = Field(..., alias="tagSource", description="The third party tag associated with creative.")
    destination: Optional["DspClickThroughDestinationV1"] = Field(None, description="Choose `AMAZON` if the `tag` links to an Amazon site like Amazon.com or IMDb. Otherwise choose `OTHER`.")
    third_party_trackers: Optional[list["DspThirdPartyTrackerV1"]] = Field(None, alias="thirdPartyTrackers")
    additional_html: Optional[str] = Field(None, alias="additionalHtml", description="Add HTML to the creative for surveys or other arbitrary HTML.")
    ad_choices_position: Optional["DspAdChoicesPositionV1"] = Field(None, alias="adChoicesPosition")

    model_config = {'populate_by_name': True}


class DspCreateThirdPartyCreativeRequestV1(BaseModel):
    pass


class DspCreateThirdPartyCreativesRequestV1(BaseModel):
    """Create Third Party creatives request."""
    pass


class DspUpdateThirdPartyCreativeRequestV1(BaseModel):
    """Update Third Party creative request."""
    pass


class DspUpdateThirdPartyCreativesRequestV1(BaseModel):
    """Update Third Party creatives request."""
    pass


class DspThirdPartyCreativeV1(BaseModel):
    pass


class DspReadThirdPartyCreativesResponseV1(BaseModel):
    """Read Third Party creative creatives response."""
    creatives: Optional[list["DspThirdPartyCreativeV1"]] = None

    model_config = {'populate_by_name': True}


class DspThirdPartyCreativesResponseV1(BaseModel):
    """Create/Update third party creatives response."""
    pass


class DspThirdPartyCreativePreviewModelV1(BaseModel):
    """Third Party Creative preview model. Populate this to preview a new creative."""
    marketplace: "DspCreativeMarketplaceV1"
    supply: "DspCreativeSupplyV1"
    size: "DspSizeV1"
    tag_source: str = Field(..., alias="tagSource", description="The third party tag associated with creative.")
    additional_html: Optional[str] = Field(None, alias="additionalHtml", description="Add HTML to the creative for surveys or other arbitrary HTML.")
    ad_choices_position: "DspAdChoicesPositionV1" = Field(..., alias="adChoicesPosition")
    third_party_trackers: Optional[list["DspThirdPartyTrackerV1"]] = Field(None, alias="thirdPartyTrackers")

    model_config = {'populate_by_name': True}


class DspThirdPartyCreativePreviewRequestV1(BaseModel):
    """Third Party creative preview request. Either `creativeId` or `creativeModel` must be provided, but not both."""
    creative_id: Optional[str] = Field(None, alias="creativeId", description="The identifier of the creative.")
    creative_model: Optional["DspThirdPartyCreativePreviewModelV1"] = Field(None, alias="creativeModel")
    preview_configuration: "DspPreviewConfigurationV1" = Field(..., alias="previewConfiguration")

    model_config = {'populate_by_name': True}


class DspCreativePreviewResponseV1(BaseModel):
    """Creative preview response."""
    preview_content: Optional[str] = Field(None, alias="previewContent", description="The HTML content")

    model_config = {'populate_by_name': True}


class ProductTrackingDomain(StrEnum):
    AMAZON_US = "AMAZON_US"
    AMAZON_CA = "AMAZON_CA"
    AMAZON_MX = "AMAZON_MX"
    PRIME_NOW_US = "PRIME_NOW_US"
    PRIME_NOW_CA = "PRIME_NOW_CA"
    WHOLE_FOODS_MARKET_US = "WHOLE_FOODS_MARKET_US"


class ProductTrackingDomainV21(StrEnum):
    FRESH_STORES_US = "FRESH_STORES_US"


class ProductTrackingItemProductassociation(StrEnum):
    FEATURED = "FEATURED"
    NOT_FEATURED = "NOT_FEATURED"


class ProductTrackingItem(BaseModel):
    product_id: str = Field(..., alias="productId", description="The product identifier.")
    product_association: ProductTrackingItemProductassociation = Field(..., alias="productAssociation", description="The product feature type.")
    domain: "ProductTrackingDomain"

    model_config = {'populate_by_name': True}


class ProductTrackingItemV21(BaseModel):
    domain: "ProductTrackingDomainV21"

    model_config = {'populate_by_name': True}


class ProductTracking(BaseModel):
    product_list: Optional[list["ProductTrackingItem"]] = Field(None, alias="productList", description="The tracking product list.")
    product_file: Optional[str] = Field(None, alias="productFile", description="The URL of the product tracking file.")

    model_config = {'populate_by_name': True}


class ProductTrackingV21(BaseModel):
    product_list: Optional[Any] = Field(None, alias="productList")

    model_config = {'populate_by_name': True}


class PixelTracking(BaseModel):
    """A list of pixels associated with the campaign."""
    pass


class ProductTrackingList(BaseModel):
    """The tracking product list."""
    pass


class ProductTrackingFile(BaseModel):
    """The URL of the product tracking file."""
    pass


class ConversionTracking(BaseModel):
    products: Optional["ProductTracking"] = None
    pixels: Optional["PixelTracking"] = None

    model_config = {'populate_by_name': True}


class ConversionTrackingV21(BaseModel):
    products: Optional["ProductTrackingV21"] = None
    pixels: Optional["PixelTracking"] = None

    model_config = {'populate_by_name': True}


class FileUploadPolicy(BaseModel):
    url: Optional[str] = Field(None, description="The AWS S3 url for file upload. It will be used as POST request URL.")
    fields: Optional[dict[str, str]] = Field(None, description="Fields used in Post request. See more details at https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/modules/_aws_sdk")

    model_config = {'populate_by_name': True}


class SupportedPolicyType(StrEnum):
    PRODUCT = "PRODUCT"
    DOMAIN = "DOMAIN"


class LineItemCreativeAssociation(BaseModel):
    line_item_id: str = Field(..., alias="lineItemId", description="The lineitem to operate on.")
    creative_id: str = Field(..., alias="creativeId", description="The creative to operate on.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The creative start date in ISO format (YYYY-MM-DD hh:mm:ss z). Timezone is UTC. For example, 2020-10-21 03:59:00 UTC.")
    end_date: Optional[str] = Field(None, alias="endDate", description="The creative end date in in ISO format (YYYY-MM-DD hh:mm:ss z). Timezone is UTC. For example, 2020-10-21 03:59:00 UTC.")
    weight: Optional[int] = Field(None, description="The weight of the creative. This field will be available only if the creative rotation type is `WEIGHTED`.")

    model_config = {'populate_by_name': True}


class LineItemCreativeAssociationsResponse(BaseModel):
    """Response for the update operation. This object will have either success or failure property for the corresponding requests on the index."""
    success: Optional["LineItemCreativeAssociation"] = None
    error_details: Optional["Error"] = Field(None, alias="errorDetails")

    model_config = {'populate_by_name': True}


class LineItemCreativeAssociationOperation(StrEnum):
    CREATE = "CREATE"
    DELETE = "DELETE"


class LineItemCreativeAssociationsRequest(BaseModel):
    advertiser_id: str = Field(..., alias="advertiserId", description="The advertiser identifier.")
    operation: "LineItemCreativeAssociationOperation"
    associations: list["LineItemCreativeAssociation"] = Field(..., description="A list of the associations to operate on. This object requires only lineItemId and creativeId and other fields are not r")

    model_config = {'populate_by_name': True}


class LineItemCreativeAssociations(BaseModel):
    total_results: Optional[int] = Field(None, alias="totalResults", description="Total number of results which satisfy the filtering criteria. This will help to support pagination.")
    response: Optional[list["LineItemCreativeAssociation"]] = None

    model_config = {'populate_by_name': True}


class LineItemCreativeAssociationV22(BaseModel):
    pass


class LineItemCreativeAssociationsV22(BaseModel):
    total_results: Optional[int] = Field(None, alias="totalResults", description="Total number of results which satisfy the filtering criteria. This will help to support pagination.")
    response: Optional[list["LineItemCreativeAssociationV22"]] = None

    model_config = {'populate_by_name': True}


class PixelPurpose(StrEnum):
    ENGAGEMENT = "ENGAGEMENT"
    REMARKETING = "REMARKETING"
    CONVERSION = "CONVERSION"


class PixelEvent(StrEnum):
    MARKETING_LANDING_PAGE = "MARKETING_LANDING_PAGE"


class Pixel(BaseModel):
    id_: Optional[str] = Field(None, alias="id")
    name: Optional[str] = None
    purpose: Optional[list[PixelPurpose]] = None
    event: Optional[PixelEvent] = None
    domain: Optional[str] = None
    description: Optional[str] = None
    advertiser_id: Optional[str] = Field(None, alias="advertiserId")
    created: Optional[str] = None

    model_config = {'populate_by_name': True}


class ProductCategory(BaseModel):
    id_: str = Field(..., alias="id", description="The category identifier.")
    name: str = Field(..., description="The category name.")
    parent_id: Optional[str] = Field(None, alias="parentId", description="The identifier of the parent category. This is blank if the category is a parent category.")

    model_config = {'populate_by_name': True}


class DomainListMetadata(BaseModel):
    id_: Optional[str] = Field(None, alias="id")
    name: Optional[str] = None
    size: Optional[int] = Field(None, description="Number of URLs specified in this list")
    created: Optional[str] = None
    updated: Optional[str] = None

    model_config = {'populate_by_name': True}


class GeoLocationCategory(StrEnum):
    COUNTRY = "COUNTRY"
    STATE = "STATE"
    CITY = "CITY"
    POSTAL_CODE = "POSTAL_CODE"
    DMA = "DMA"


class GeoLocation(BaseModel):
    """Single geo location information."""
    id_: Optional[str] = Field(None, alias="id")
    name: Optional[str] = Field(None, description="Name of geo location.")
    category: Optional[GeoLocationCategory] = Field(None, description="Category of the geo location.")

    model_config = {'populate_by_name': True}


class IABContentCategory(BaseModel):
    id_: str = Field(..., alias="id", description="The category identifier.")
    name: str = Field(..., description="The category name.")
    parent_id: Optional[str] = Field(None, alias="parentId", description="The identifier of the parent category. This is blank if the category is a parent category.")

    model_config = {'populate_by_name': True}


class DiscoveryLineItemTypes(StrEnum):
    STANDARD_DISPLAY = "STANDARD_DISPLAY"
    AMAZON_MOBILE_DISPLAY = "AMAZON_MOBILE_DISPLAY"
    AAP_MOBILE_APP = "AAP_MOBILE_APP"
    VIDEO = "VIDEO"


class OdcPredict(BaseModel):
    id_: str = Field(..., alias="id", description="The segment identifier.")
    name: str = Field(..., description="The segment name.")

    model_config = {'populate_by_name': True}


class OdcCustomPredicts(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken")
    custom_predicts: Optional[list["OdcPredict"]] = Field(None, alias="customPredicts")

    model_config = {'populate_by_name': True}


class OdcStandardPredicts(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken")
    standard_predicts: Optional[list["OdcPredict"]] = Field(None, alias="standardPredicts")

    model_config = {'populate_by_name': True}


class DvCustomContextualSegment(BaseModel):
    id_: str = Field(..., alias="id", description="The segment identifier.")
    name: str = Field(..., description="The segment name.")

    model_config = {'populate_by_name': True}


class DvCustomContextualSegments(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken")
    custom_contextual_segments: Optional[list["DvCustomContextualSegment"]] = Field(None, alias="customContextualSegments")

    model_config = {'populate_by_name': True}


class Goal(StrEnum):
    AWARENESS = "AWARENESS"
    ENGAGEMENT_WITH_MY_AD = "ENGAGEMENT_WITH_MY_AD"
    CONSIDERATIONS_ON_AMAZON = "CONSIDERATIONS_ON_AMAZON"
    CONVERSIONS_OFF_AMAZON = "CONVERSIONS_OFF_AMAZON"
    PURCHASES_ON_AMAZON = "PURCHASES_ON_AMAZON"
    MOBILE_APP_INSTALLS = "MOBILE_APP_INSTALLS"


class GoalV1(StrEnum):
    PURCHASES_ON_OFF_AMAZON = "PURCHASES_ON_OFF_AMAZON"


class GoalKpi(StrEnum):
    CLICK_THROUGH_RATE = "CLICK_THROUGH_RATE"
    COST_PER_ACQUISITION = "COST_PER_ACQUISITION"
    COST_PER_CLICK = "COST_PER_CLICK"
    COST_PER_DETAIL_PAGE_VIEW = "COST_PER_DETAIL_PAGE_VIEW"
    COST_PER_VIDEO_COMPLETION = "COST_PER_VIDEO_COMPLETION"
    DETAIL_PAGE_VIEW_RATE = "DETAIL_PAGE_VIEW_RATE"
    NONE = "NONE"
    OTHER = "OTHER"
    REACH = "REACH"
    RETURN_ON_AD_SPEND = "RETURN_ON_AD_SPEND"
    TOTAL_RETURN_ON_AD_SPEND = "TOTAL_RETURN_ON_AD_SPEND"
    VIDEO_COMPLETION_RATE = "VIDEO_COMPLETION_RATE"


class GoalKpiV1(StrEnum):
    COMBINED_RETURN_ON_AD_SPEND = "COMBINED_RETURN_ON_AD_SPEND"
    COST_PER_FIRST_APP_OPEN = "COST_PER_FIRST_APP_OPEN"
    COST_PER_INSTALL = "COST_PER_INSTALL"
    TOTAL_COST_PER_SUBSCRIPTION = "TOTAL_COST_PER_SUBSCRIPTION"


class GoalKpiV11(StrEnum):
    CLICK_THROUGH_RATE = "CLICK_THROUGH_RATE"
    COMBINED_RETURN_ON_AD_SPEND = "COMBINED_RETURN_ON_AD_SPEND"
    COST_PER_ACTION = "COST_PER_ACTION"
    COST_PER_CLICK = "COST_PER_CLICK"
    COST_PER_DETAIL_PAGE_VIEW = "COST_PER_DETAIL_PAGE_VIEW"
    COST_PER_FIRST_APP_OPEN = "COST_PER_FIRST_APP_OPEN"
    COST_PER_INSTALL = "COST_PER_INSTALL"
    COST_PER_VIDEO_COMPLETION = "COST_PER_VIDEO_COMPLETION"
    DETAIL_PAGE_VIEW_RATE = "DETAIL_PAGE_VIEW_RATE"
    NONE = "NONE"
    OTHER = "OTHER"
    REACH = "REACH"
    RETURN_ON_AD_SPEND = "RETURN_ON_AD_SPEND"
    TOTAL_COST_PER_SUBSCRIPTION = "TOTAL_COST_PER_SUBSCRIPTION"
    TOTAL_RETURN_ON_AD_SPEND = "TOTAL_RETURN_ON_AD_SPEND"
    VIDEO_COMPLETION_RATE = "VIDEO_COMPLETION_RATE"


class AutoOptimization(StrEnum):
    BUDGET = "BUDGET"
    BID = "BID"


class GoalConfigurationAvailablekpis(BaseModel):
    kpi_name: Optional["GoalKpi"] = Field(None, alias="kpiName")
    auto_optimizations: Optional[list["AutoOptimization"]] = Field(None, alias="autoOptimizations", description="Which optimizations can be applied for this KPI")

    model_config = {'populate_by_name': True}


class GoalConfiguration(BaseModel):
    goal_name: Optional["Goal"] = Field(None, alias="goalName")
    available_kpis: Optional[list["GoalConfigurationAvailablekpis"]] = Field(None, alias="availableKpis")

    model_config = {'populate_by_name': True}


class GoalConfigurationV1Availablekpis(BaseModel):
    kpi_name: Optional["GoalKpiV1"] = Field(None, alias="kpiName")
    auto_optimizations: Optional[list["AutoOptimization"]] = Field(None, alias="autoOptimizations", description="Which optimizations can be applied for this KPI")

    model_config = {'populate_by_name': True}


class GoalConfigurationV1(BaseModel):
    goal_name: Optional["GoalV1"] = Field(None, alias="goalName")
    available_kpis: Optional[list["GoalConfigurationV1Availablekpis"]] = Field(None, alias="availableKpis")

    model_config = {'populate_by_name': True}


class GoalConfigurationV11Availablekpis(BaseModel):
    kpi_name: Optional["GoalKpiV11"] = Field(None, alias="kpiName")
    auto_optimizations: Optional[list["AutoOptimization"]] = Field(None, alias="autoOptimizations", description="Which optimizations can be applied for this KPI")

    model_config = {'populate_by_name': True}


class GoalConfigurationV11(BaseModel):
    goal_name: Optional["GoalV1"] = Field(None, alias="goalName")
    available_kpis: Optional[list["GoalConfigurationV11Availablekpis"]] = Field(None, alias="availableKpis")

    model_config = {'populate_by_name': True}


class App(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="The app identifier.")
    name: Optional[str] = Field(None, description="The app name.")

    model_config = {'populate_by_name': True}


class Apps(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken")
    apps: Optional[list["App"]] = None

    model_config = {'populate_by_name': True}


class SupportedProductAssociationV1(StrEnum):
    FEATURED = "FEATURED"
    NOT_FEATURED = "NOT_FEATURED"
    FEATURED_WITH_VARIATION = "FEATURED_WITH_VARIATION"


class SupportedProductTrackingDomainV1(StrEnum):
    AMAZON_US = "AMAZON_US"
    AMAZON_CA = "AMAZON_CA"
    AMAZON_MX = "AMAZON_MX"
    PRIME_NOW_US = "PRIME_NOW_US"
    PRIME_NOW_CA = "PRIME_NOW_CA"
    WHOLE_FOODS_MARKET_US = "WHOLE_FOODS_MARKET_US"
    FRESH_STORES_US = "FRESH_STORES_US"
    PRIME_VIDEO_ROW_NA = "PRIME_VIDEO_ROW_NA"


class ProductTrackingItemV1(BaseModel):
    product_id: str = Field(..., alias="productId", description="The product identifier.")
    product_association: "SupportedProductAssociationV1" = Field(..., alias="productAssociation")
    domain: "SupportedProductTrackingDomainV1"

    model_config = {'populate_by_name': True}


class ProductTrackingListV1(BaseModel):
    """The tracking product list."""
    pass


class ProductTrackingV1(BaseModel):
    product_list: Optional["ProductTrackingListV1"] = Field(None, alias="productList")
    product_file: Optional[str] = Field(None, alias="productFile", description="The URL of the product tracking file.")

    model_config = {'populate_by_name': True}


class TargetingType(StrEnum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class ReadDomainTargetingResponse(BaseModel):
    """The read operation response."""
    line_item_id: Optional[str] = Field(None, alias="lineItemId", description="The line item identifier.")
    inherit_from_advertiser: Optional[bool] = Field(None, alias="inheritFromAdvertiser", description="Set to `true` to enable domain inheritance from advertiser.")
    targeting_type: Optional["TargetingType"] = Field(None, alias="targetingType")
    domain_list_merged_file: Optional[str] = Field(None, alias="domainListMergedFile", description="The URL address of the domain file after merging all domains into single file, including inheritance from advertiser, do")

    model_config = {'populate_by_name': True}


class ReadDomainTargetingResponses(BaseModel):
    response: Optional[list["ReadDomainTargetingResponse"]] = None

    model_config = {'populate_by_name': True}


class DomainFileMetaData(BaseModel):
    file_key: str = Field(..., alias="fileKey", description="The S3 key of domain list file.")
    file_name: str = Field(..., alias="fileName", description="The domain list file name.")

    model_config = {'populate_by_name': True}


class UpdateDomainTargetingRequest(BaseModel):
    """The update operation request."""
    line_item_id: str = Field(..., alias="lineItemId", description="The line item identifier.")
    inherit_from_advertiser: bool = Field(..., alias="inheritFromAdvertiser", description="Set to `true` to enable domain inheritance from advertiser.")
    targeting_type: "TargetingType" = Field(..., alias="targetingType")
    domain_files: Optional[list["DomainFileMetaData"]] = Field(None, alias="domainFiles", description="The list of URL addresses of the domain list files.")
    domain_lists: Optional[list[str]] = Field(None, alias="domainLists", description="The list of domain lists Ids get from discovery API.")
    domain_names: Optional[list[str]] = Field(None, alias="domainNames", description="The list of raw domain names.")

    model_config = {'populate_by_name': True}


class DomainFileValidationResponse(BaseModel):
    file_name: Optional[str] = Field(None, alias="fileName", description="The uploaded file name.")
    added_domain_size: Optional[int] = Field(None, alias="addedDomainSize", description="Number of domains in the file that have been added to the line item.")
    invalid_domain_size: Optional[int] = Field(None, alias="invalidDomainSize", description="Number of invalid domains in the file. They are not added to the line item.")
    duplicate_domain_size: Optional[int] = Field(None, alias="duplicateDomainSize", description="Number of duplicate domains in the file. The unique ones of them are added to the line item.")
    invalid_domains_file_url: Optional[str] = Field(None, alias="invalidDomainsFileUrl", description="The URL of invalid domains file. It expires in 1 hour.")
    duplicate_domains_file_url: Optional[str] = Field(None, alias="duplicateDomainsFileUrl", description="The URL of duplicate domains file. It expires in 1 hour.")

    model_config = {'populate_by_name': True}


class UpdateDomainTargetingResponse(BaseModel):
    """The update operation response. If operation is successful, it contains lineItemId (and domainFilesUploaded). If it is a failure, it contains only errorDetails. Success and failure will be correspondin"""
    line_item_id: Optional[str] = Field(None, alias="lineItemId", description="The line item identifier.")
    domain_files_uploaded: Optional[list["DomainFileValidationResponse"]] = Field(None, alias="domainFilesUploaded", description="The list of domain file validation results.")
    error_details: Optional["Error"] = Field(None, alias="errorDetails")

    model_config = {'populate_by_name': True}

