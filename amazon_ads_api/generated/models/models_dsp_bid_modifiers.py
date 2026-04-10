"""Auto-generated Pydantic models. Do not edit manually.

Source: BidModifiers_prod_3p.json
Title:  Bid Modifiers
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class BidModifiersServiceAccessDeniedExceptionResponseContent(BaseModel):
    """Indicates the user does not have access to this API."""
    message: str = Field(..., description="Error message indicating why the request may have failed.")

    model_config = {'populate_by_name': True}


class BidModifiersServiceBidModifierRuleAssociations(BaseModel):
    ad_group_ids: Optional[list[str]] = Field(None, alias="adGroupIds")

    model_config = {'populate_by_name': True}


class BidModifiersServiceAllBidModifierRuleAssociations(BaseModel):
    """Returns active, inactive and audienceViolation associations for a bid adjustment rule: * activeAssociations: Ad groups currently associated with the rule * inactiveAssociations: Ad groups previously a"""
    active_associations: "BidModifiersServiceBidModifierRuleAssociations" = Field(..., alias="activeAssociations")
    audience_violations: Optional["BidModifiersServiceBidModifierRuleAssociations"] = Field(None, alias="audienceViolations")
    inactive_associations: Optional["BidModifiersServiceBidModifierRuleAssociations"] = Field(None, alias="inactiveAssociations")

    model_config = {'populate_by_name': True}


class BidModifiersServiceOnMultipleMatches(StrEnum):
    APPLY_PRODUCT = "APPLY_PRODUCT"


class BidModifiersServiceBidModifierTerm(BaseModel):
    """A bid adjustment term is composed of 1 or more of the below dimensions, and a bid adjustment.  A minimum of 1 dimension must be set, and there is no maximum on the number of dimensions. The same  dime"""
    ad_format: Optional[list[str]] = Field(None, alias="adFormat", description="Valid values: 'DISPLAY', 'AUDIO', 'VIDEO'. Values are case insensitive.")
    app_id: Optional[list[str]] = Field(None, alias="appId", description="Application identifiers unique to the app and independent of the exchange. On Android, this should be a bundle or packag")
    app_name: Optional[list[str]] = Field(None, alias="appName", description="The name of the application from the App Store. Examples include: 'Wordscapes', 'Pinterest', 'Yahoo Weather'.")
    behavioral_segment: Optional[list[str]] = Field(None, alias="behavioralSegment", description="Unique identifier for Amazon audiences. Selection of segments in Audience for the adgroup is required in order to use th")
    bid_adjustment: float = Field(..., alias="bidAdjustment", description="The value used to upscale/downscale the Amazon DSP computed bid amount. This will be multiplied with the bid amount  com")
    browser: Optional[list[str]] = Field(None, description="The browser family of the user viewing the page. Example: 'Chrome', 'Mozilla', 'Safari', 'Firefox'. Values are case inse")
    city: Optional[list[str]] = Field(None, description="Full name of the city. Values are case insensitive. Only listed values are allowed.")
    country: Optional[list[str]] = Field(None, description="The ISO 3166-1 alpha-2 country code, based on the IP address of the user. Example: 'JP'. Values are case insensitive.")
    device_make: Optional[list[str]] = Field(None, alias="deviceMake", description="The make of the device. Example: 'APPLE', 'GOOGLE', 'SAMSUNG', 'AMAZON'. Values are case insensitive.")
    device_type: Optional[list[str]] = Field(None, alias="deviceType", description="The device type of the user viewing the ad. Valid Values: 'Phone', 'Tablet', 'PC', 'TV', 'ConnectedDevice', 'SetTopBox'.")
    dma: Optional[list[str]] = Field(None, description="Designated market area. Example: 'DMA501' would be used for Nielsen DMA corresponding to New York, NY. Values are case i")
    domain: Optional[list[str]] = Field(None, description="Domain of a site. Example: 'msn.com' Values are case insensitive.")
    negative: Optional[bool] = Field(None, description="Determines when the bidAdjustment is applied. Defaults to false. If specified as true, then it defines a      matched te")
    operating_system: Optional[list[str]] = Field(None, alias="operatingSystem", description="The operating system of the user viewing the page. Example: 'MacOS', 'Windows', 'iOS', 'Android', 'Fire OS'. Values are ")
    postal_code: Optional[list[str]] = Field(None, alias="postalCode", description="The postal code with 2-letter country code prefix, based on the IP address of the user. Use '-' as a separator between c")
    region: Optional[list[str]] = Field(None, description="The geographical state, based on the IP address of the user. Values are case insensitive.")
    slot_position: Optional[list[str]] = Field(None, alias="slotPosition", description="Whether the slot is above, or below the fold. Valid Values: 'ABOVE', 'BELOW', 'UNKNOWN'. Values are case insensitive.")
    slot_size: Optional[list[str]] = Field(None, alias="slotSize", description="The slot's pixel size for the ad. This functions the same as the creative size with our slot-creative matching process. ")
    term_id: Optional[float] = Field(None, alias="termId", description="A system generated identifier for the term starting from 1.")

    model_config = {'populate_by_name': True}


class BidModifiersServiceBidModifierRuleExpression(BaseModel):
    on_multiple_matches: Optional["BidModifiersServiceOnMultipleMatches"] = Field(None, alias="onMultipleMatches")
    terms: list["BidModifiersServiceBidModifierTerm"]

    model_config = {'populate_by_name': True}


class BidModifiersServiceBidModifierRuleDetails(BaseModel):
    """Expected output for reading details of a bid adjustment rule."""
    active: bool = Field(..., description="Whether the current bid adjustment rule is considered active/inactive.")
    associations: "BidModifiersServiceAllBidModifierRuleAssociations"
    bid_modifier_rule_id: str = Field(..., alias="bidModifierRuleId", description="The unique identifier for the bid adjustment rule.")
    date_created: str = Field(..., alias="dateCreated", description="The ISO 8601 date time (in UTC) when the bid adjustment rule was created.")
    rule_description: str = Field(..., alias="ruleDescription", description="The name of the bid adjustment. No uniqueness requirements.")
    rule_expression: Optional["BidModifiersServiceBidModifierRuleExpression"] = Field(None, alias="ruleExpression")
    term_count: float = Field(..., alias="termCount", description="Number of terms present in the bid modifier rule.")

    model_config = {'populate_by_name': True}


class BidModifiersServiceConflictExceptionResponseContent(BaseModel):
    """Indicates that updating or deleting a resource can cause an inconsistent state."""
    message: str = Field(..., description="Error message indicating why the request may have failed.")

    model_config = {'populate_by_name': True}


class BidModifiersServiceCreateBidModifierRuleAssociationResponseContent(BaseModel):
    """Expected output for associating a bid adjustment rule with an adgroup."""
    details: str = Field(..., description="Description of the API result.")

    model_config = {'populate_by_name': True}


class BidModifiersServiceCreateBidModifierRuleRequestContent(BaseModel):
    """Expected input for the CreateBidModifierRuleInput operation. The maximum size  for the bid adjustment rule is 1mb. Please reach out to ADSP if you require an exception to the 1mb size  limit."""
    rule_description: str = Field(..., alias="ruleDescription", description="A meaningful description which captures the intent of the bid adjustment rule.")
    rule_expression: "BidModifiersServiceBidModifierRuleExpression" = Field(..., alias="ruleExpression")

    model_config = {'populate_by_name': True}


class BidModifiersServiceCreateBidModifierRuleResponseContent(BaseModel):
    """Expected output for the CreateBidModifierRuleOutput operation."""
    bid_modifier_rule_id: str = Field(..., alias="bidModifierRuleId", description="The newly created unique ID for the bid adjustment rule.")

    model_config = {'populate_by_name': True}


class BidModifiersServiceDeleteBidModifierRuleAssociationResponseContent(BaseModel):
    """Expected output for dissociating a bid adjustment rule from an adgroup."""
    details: str = Field(..., description="Description of the API result.")

    model_config = {'populate_by_name': True}


class BidModifiersServiceDeleteBidModifierRuleResponseContent(BaseModel):
    """Expected output for DeleteBidModifierRule operation."""
    details: str = Field(..., description="Description of the API result.")

    model_config = {'populate_by_name': True}


class BidModifiersServiceGetBidModifierRuleAssociationsRequestContent(BaseModel):
    """Expected input for reading details of a bid adjustment rule."""
    max_results: Optional[float] = Field(None, alias="maxResults", description="The maximum number of results the caller wishes to receive. Min 5 / Max 1000. Default to 100.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="A token that can be passed back to the same operation to get the next page of results.     If this field is missing, it ")
    show_inactive_associations: Optional[bool] = Field(None, alias="showInactiveAssociations", description="Set to true to see inactive associations. Default is false.")

    model_config = {'populate_by_name': True}


class BidModifiersServiceGetBidModifierRuleAssociationsResponseContent(BaseModel):
    """Expected output for reading details of a bid adjustment rule."""
    associations: "BidModifiersServiceAllBidModifierRuleAssociations"
    next_token: Optional[str] = Field(None, alias="nextToken", description="A token that can be passed back to the same operation to get the next page of results,     missing indicates no more res")

    model_config = {'populate_by_name': True}


class BidModifiersServiceGetBidModifierRuleResponseContent(BaseModel):
    """Expected output for reading details of a bid adjustment rule."""
    active: bool = Field(..., description="Whether the current bid adjustment rule is considered active/inactive.")
    bid_modifier_rule_id: str = Field(..., alias="bidModifierRuleId", description="The unique identifier for the bid adjustment rule.")
    date_created: str = Field(..., alias="dateCreated", description="The ISO 8601 date time (in UTC) when the bid adjustment rule was created.")
    rule_description: str = Field(..., alias="ruleDescription", description="The name of the bid adjustment. No uniqueness requirements.")
    rule_expression: "BidModifiersServiceBidModifierRuleExpression" = Field(..., alias="ruleExpression")

    model_config = {'populate_by_name': True}


class BidModifiersServiceInternalServerExceptionResponseContent(BaseModel):
    """Indicates that the server encountered an unexpected error."""
    message: str = Field(..., description="Error message indicating why the request may have failed.")

    model_config = {'populate_by_name': True}


class BidModifiersServiceInvalidBidModifierRuleExceptionResponseContent(BaseModel):
    """Indicates that the bid adjustment rule did not pass validations against the expected schema."""
    message: str = Field(..., description="Error message indicating why the request may have failed.")

    model_config = {'populate_by_name': True}


class BidModifiersServiceListBidModifierRulesRequestContent(BaseModel):
    """Expected input for reading details of a bid adjustment rule associated with one or more adgroups."""
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="List all bid adjustment rules associated with the single adGroupId passed. You can pass one of: single adGroupId or a li")
    ad_group_ids: Optional[list[str]] = Field(None, alias="adGroupIds", description="List all bid adjustment rules associated with the list of adGroupIds passed. You can pass one of: single adGroupId or a ")
    max_results: Optional[float] = Field(None, alias="maxResults", description="The maximum number of results the caller wishes to receive. Min 5 / Max 1000. Default to 100.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="A token that can be passed back to the same operation to get the next page of results.     If this field is missing, it ")

    model_config = {'populate_by_name': True}


class BidModifiersServiceListBidModifierRulesResponseContent(BaseModel):
    """Expected output for reading details of a bid adjustment rule associated with one or more adgroups."""
    bid_modifier_rules: Optional[list["BidModifiersServiceBidModifierRuleDetails"]] = Field(None, alias="bidModifierRules", description="List of bid adjustment rules")
    next_token: Optional[str] = Field(None, alias="nextToken", description="A token that can be passed back to the same operation to get the next page of results,     missing indicates no more res")

    model_config = {'populate_by_name': True}


class BidModifiersServiceResourceNotFoundExceptionResponseContent(BaseModel):
    """Indicates that the bid adjustment rule or associated metadata could not be found."""
    message: str = Field(..., description="Error message indicating why the request may have failed.")

    model_config = {'populate_by_name': True}


class BidModifiersServiceRetryRequestExceptionResponseContent(BaseModel):
    """Indicates that the request failed but may succeed if retried after the  specified time in seconds."""
    message: str = Field(..., description="Error message indicating why the request may have failed.")

    model_config = {'populate_by_name': True}


class BidModifiersServiceSurpassedQuotaExceptionResponseContent(BaseModel):
    """Indicates the user has surpassed their quota for creating bid modifiers"""
    message: str = Field(..., description="Error message indicating why the request may have failed.")

    model_config = {'populate_by_name': True}


class BidModifiersServiceThrottlingExceptionResponseContent(BaseModel):
    """Indicates that the request was denied due to too many requests from the same user. The  request may be retried after the specified time in seconds."""
    message: str = Field(..., description="Error message indicating why the request may have failed.")

    model_config = {'populate_by_name': True}


class BidModifiersServiceUnauthorizedExceptionResponseContent(BaseModel):
    """Indicates the user is unauthorized to invoke this API."""
    message: str = Field(..., description="Error message indicating why the request may have failed.")

    model_config = {'populate_by_name': True}


class BidModifiersServiceValidationExceptionResponseContent(BaseModel):
    """Indicates that the caller has provided invalid inputs for request fields, or was missing required fields."""
    message: str = Field(..., description="Error message indicating why the request may have failed.")

    model_config = {'populate_by_name': True}

