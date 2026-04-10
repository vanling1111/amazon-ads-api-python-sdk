"""Auto-generated Pydantic models. Do not edit manually.

Source: Changehistory_prod_3p.json
Title:  Change history
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class HistoryError(BaseModel):
    """The error response object."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class HistoryEventTypeFilters(StrEnum):
    BID_AMOUNT = "BID_AMOUNT"
    BUDGET_AMOUNT = "BUDGET_AMOUNT"
    END_DATE = "END_DATE"
    IN_BUDGET = "IN_BUDGET"
    NAME = "NAME"
    PLACEMENT_GROUP = "PLACEMENT_GROUP"
    SMART_BIDDING_STRATEGY = "SMART_BIDDING_STRATEGY"
    START_DATE = "START_DATE"
    STATUS = "STATUS"


class HistoryEventTypeParents(BaseModel):
    ad_group_id: Optional[str] = Field(None, alias="adGroupId")
    campaign_id: Optional[str] = Field(None, alias="campaignId")
    use_profile_id_advertiser: Optional[bool] = Field(None, alias="useProfileIdAdvertiser", description="If true, retrieves events which belong to the associated advertiser")

    model_config = {'populate_by_name': True}


class HistoryEventType(BaseModel):
    event_type_ids: Optional[list[str]] = Field(None, alias="eventTypeIds", description="max of 10 event types. IDs here belong to the EventType. For example, if requesting CAMPAGIN as the eventType, these are")
    filters: Optional[list[HistoryEventTypeFilters]] = Field(None, description="| Filter | Entity Types | ||-| | BUDGET_AMOUNT | CAMPAIGN | | IN_BUDGET | CAMPAIGN | | STATUS | CAMPAIGN, AD_GROUP, AD, ")
    parents: Optional[list["HistoryEventTypeParents"]] = Field(None, description="maximum of 10 parents")

    model_config = {'populate_by_name': True}


class HistoryEventTypes(BaseModel):
    """Event types that can be queried. **Note:** THEME event type requires API version 1.1 or higher (Accept: application/vnd.historyresponse.v1.1+json)"""
    ad: Optional["HistoryEventType"] = Field(None, alias="AD")
    ad_group: Optional["HistoryEventType"] = Field(None, alias="AD_GROUP")
    campaign: Optional["HistoryEventType"] = Field(None, alias="CAMPAIGN")
    keyword: Optional["HistoryEventType"] = Field(None, alias="KEYWORD")
    negative_keyword: Optional["HistoryEventType"] = Field(None, alias="NEGATIVE_KEYWORD")
    product_targeting: Optional["HistoryEventType"] = Field(None, alias="PRODUCT_TARGETING")
    theme: Optional["HistoryEventType"] = Field(None, alias="THEME")

    model_config = {'populate_by_name': True}


class HistoryResponseEvents(BaseModel):
    pass


class HistorySortParameterDirection(StrEnum):
    ASC = "ASC"
    DESC = "DESC"


class HistorySortParameterKey(StrEnum):
    DATE = "DATE"


class HistorySortParameter(BaseModel):
    direction: Optional[HistorySortParameterDirection] = None
    key: Optional[HistorySortParameterKey] = None

    model_config = {'populate_by_name': True}

