"""Auto-generated Pydantic models. Do not edit manually.

Source: D16GFMApiFrequencyGroupAssociationV1_prod_3p.json
Title:  D16GFMApiFrequencyGroupAssociationV1
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class AdsOwnerType(StrEnum):
    ADVERTISER = "ADVERTISER"
    MANAGER_ACCOUNT = "MANAGER_ACCOUNT"


class CampaignType(StrEnum):
    CUSTOM = "CUSTOM"
    UNCAPPED = "UNCAPPED"


class TimeUnitV1(StrEnum):
    DAYS = "DAYS"
    HOURS = "HOURS"


class CampaignFrequency(BaseModel):
    max_impressions: Optional[float] = Field(None, alias="maxImpressions")
    time_unit: Optional["TimeUnitV1"] = Field(None, alias="timeUnit")
    time_unit_count: Optional[float] = Field(None, alias="timeUnitCount")
    type_: Optional["CampaignType"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class CauseForAssociationUnavailability(StrEnum):
    ALREADY_ASSOCIATED = "ALREADY_ASSOCIATED"
    DELIVERY_STATUS_NOT_ACTIVE = "DELIVERY_STATUS_NOT_ACTIVE"
    TARGET_FREQUENCY = "TARGET_FREQUENCY"


class DeliveryStatus(StrEnum):
    ACTIVE = "ACTIVE"
    ADS_NOT_RUNNING = "ADS_NOT_RUNNING"
    ADVERTISER_NOT_RUNNING = "ADVERTISER_NOT_RUNNING"
    BOOKING_REQUESTED = "BOOKING_REQUESTED"
    CAMPAIGN_NOT_RUNNING = "CAMPAIGN_NOT_RUNNING"
    CREATIVES_NOT_RUNNING = "CREATIVES_NOT_RUNNING"
    DELETED = "DELETED"
    ENDED = "ENDED"
    INACTIVE = "INACTIVE"
    NOT_APPROVED = "NOT_APPROVED"
    OK = "OK"
    OUT_OF_BUDGET = "OUT_OF_BUDGET"
    PAUSED_BY_SYSTEM = "PAUSED_BY_SYSTEM"
    PAUSED_BY_USER = "PAUSED_BY_USER"
    PENDING_ADSERVER_RECEIPT = "PENDING_ADSERVER_RECEIPT"
    PREBOOK = "PREBOOK"
    PREBOOKED = "PREBOOKED"
    PROPOSAL = "PROPOSAL"
    READY_TO_RUN = "READY_TO_RUN"
    RUNNING = "RUNNING"
    UNINITIALIZED_BUDGET = "UNINITIALIZED_BUDGET"


class DspSubError(BaseModel):
    error_code: str = Field(..., alias="errorCode")
    error_id: Optional[str] = Field(None, alias="errorId")
    error_message: str = Field(..., alias="errorMessage")

    model_config = {'populate_by_name': True}


class DspBadRequestExceptionResponseContent(BaseModel):
    errors: Optional[list["DspSubError"]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspForbiddenExceptionResponseContent(BaseModel):
    errors: Optional[list["DspSubError"]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspInternalServerExceptionResponseContent(BaseModel):
    errors: Optional[list["DspSubError"]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspNotFoundExceptionResponseContent(BaseModel):
    errors: Optional[list["DspSubError"]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspTooManyRequestsExceptionResponseContent(BaseModel):
    errors: Optional[list["DspSubError"]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspUnauthorizedExceptionResponseContent(BaseModel):
    errors: Optional[list["DspSubError"]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class DspUnsupportedMediaTypeExceptionResponseContent(BaseModel):
    errors: Optional[list["DspSubError"]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class FrequencyGroupInput(BaseModel):
    id_: str = Field(..., alias="id", description="The identifier of the frequency group.")

    model_config = {'populate_by_name': True}


class FrequencyGroupWithAssociationOutput(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="The frequency group identifier.")
    is_transitive_association: Optional[bool] = Field(None, alias="isTransitiveAssociation", description="Return true, if the campaign is not directly associated to the frequency group, but the advertiser that the campaign bel")
    name: Optional[str] = Field(None, description="The frequency group name.")
    owner_id: Optional[str] = Field(None, alias="ownerId", description="If the frequency group belongs to a DSP entity or manager account, ownerId is DSP entity id. If the frequency group belo")
    owner_type: Optional["AdsOwnerType"] = Field(None, alias="ownerType")

    model_config = {'populate_by_name': True}


class KPI(StrEnum):
    COMBINED_ROAS = "COMBINED_ROAS"
    COMPLETION_RATE = "COMPLETION_RATE"
    CPA = "CPA"
    CPC = "CPC"
    CPD = "CPD"
    CPDPV = "CPDPV"
    CPFAO = "CPFAO"
    CPI = "CPI"
    CPVC = "CPVC"
    CTR = "CTR"
    DPVR = "DPVR"
    INCREMENTAL_REACH = "INCREMENTAL_REACH"
    IOPS = "IOPS"
    NONE = "NONE"
    OTHER = "OTHER"
    REACH = "REACH"
    ROAS = "ROAS"
    TARGET_FREQUENCY = "TARGET_FREQUENCY"
    TOTAL_CPSU = "TOTAL_CPSU"
    TOTAL_ROAS = "TOTAL_ROAS"


class ListAdvertiserAssociationResponseBaseObject(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="The advertiser identifier.")
    name: Optional[str] = Field(None, description="The advertiser name.")

    model_config = {'populate_by_name': True}


class ListAdvertiserFrequencyGroupAssociationResponseBaseObject(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="The frequency group identifier.")
    name: Optional[str] = Field(None, description="The frequency group name.")
    owner_id: Optional[str] = Field(None, alias="ownerId", description="If the frequency group belongs to a DSP entity or manager account, ownerId is DSP entity id. If the frequency group belo")
    owner_type: Optional["AdsOwnerType"] = Field(None, alias="ownerType")

    model_config = {'populate_by_name': True}


class ListAdvertisersBaseObject(BaseModel):
    advertiser_id: Optional[str] = Field(None, alias="advertiserId")
    advertiser_name: Optional[str] = Field(None, alias="advertiserName")

    model_config = {'populate_by_name': True}


class ListAdvertisersFrequencyGroupBaseObject(BaseModel):
    frequency_group_ids: Optional[list[str]] = Field(None, alias="frequencyGroupIds")

    model_config = {'populate_by_name': True}


class ListAdvertisersFrequencyGroupAssociationsBaseObject(BaseModel):
    advertiser: Optional["ListAdvertisersBaseObject"] = None
    frequency_group: Optional["ListAdvertisersFrequencyGroupBaseObject"] = Field(None, alias="frequencyGroup")

    model_config = {'populate_by_name': True}


class ListAdvertisersFrequencyGroupAssociationsRequestContentV1(BaseModel):
    advertiser_name_filter: Optional[str] = Field(None, alias="advertiserNameFilter", description="Allows the user to specify a name filter to limit the results by advertiser name")
    frequency_group_id_filter: Optional[str] = Field(None, alias="frequencyGroupIdFilter", description="A frequency group identifier to extract the advertiserIdFilter from; and empty string indicates that we are querying for")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Sets the maximum number of objects in the returned array. Use in conjunction with the nextToken parameter to control pag")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token from a previous request. Use in conjunction with the maxResults N parameter to control pagination of the returned ")

    model_config = {'populate_by_name': True}


class ListCampaignAssociationResponseBaseObject(BaseModel):
    advertiser_id: Optional[str] = Field(None, alias="advertiserId", description="The identifier of the advertiser that the campaign belongs to.")
    id_: Optional[str] = Field(None, alias="id", description="The campaign identifier.")
    name: Optional[str] = Field(None, description="The campaign name.")

    model_config = {'populate_by_name': True}


class ListCampaignsCampaignBaseObject(BaseModel):
    advertiser_id: Optional[str] = Field(None, alias="advertiserId")
    available_for_fg_association: Optional[bool] = Field(None, alias="availableForFGAssociation")
    campaign_id: Optional[str] = Field(None, alias="campaignId")
    campaign_name: Optional[str] = Field(None, alias="campaignName")
    cause_for_association_unavailability: Optional[list["CauseForAssociationUnavailability"]] = Field(None, alias="causeForAssociationUnavailability")
    delivery_status: Optional["DeliveryStatus"] = Field(None, alias="deliveryStatus")
    frequency: Optional["CampaignFrequency"] = None
    kpi: Optional["KPI"] = None

    model_config = {'populate_by_name': True}


class ListCampaignsFrequencyGroupAssociationsRequestContentV1(BaseModel):
    advertiser_id_filter: Optional[str] = Field(None, alias="advertiserIdFilter", description="The advertiser identifier")
    campaign_name_filter: Optional[str] = Field(None, alias="campaignNameFilter", description="Allows the user to specify a name filter to limit the results by campaign name")
    frequency_group_id_filter: Optional[str] = Field(None, alias="frequencyGroupIdFilter", description="A frequency group identifier to extract the advertiserIdFilter from")
    include_transitive_associations: Optional[bool] = Field(None, alias="includeTransitiveAssociations", description="A campaign is transitively associated to a frequency group if the advertiser that this campaign belongs to is directly a")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Sets the maximum number of objects in the returned array. Use in conjunction with the nextToken parameter to control pag")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token from a previous request. Use in conjunction with the maxResults N parameter to control pagination of the returned ")

    model_config = {'populate_by_name': True}


class ListCampaignsFrequencyGroupBaseObject(BaseModel):
    frequency_group_id: Optional[str] = Field(None, alias="frequencyGroupId")

    model_config = {'populate_by_name': True}


class ListCampaignsFrequencyGroupCampaignAssociationsBaseObject(BaseModel):
    """Campaign and associated frequency groups. frequencyGroup contains a frequency group belongs to DSP advertiser. frequencyGroups contains frequency groups belong to DSP entities."""
    campaign: Optional["ListCampaignsCampaignBaseObject"] = None
    frequency_group: Optional["ListCampaignsFrequencyGroupBaseObject"] = Field(None, alias="frequencyGroup")
    frequency_groups: Optional[list["FrequencyGroupWithAssociationOutput"]] = Field(None, alias="frequencyGroups")

    model_config = {'populate_by_name': True}


class ListFrequencyGroupAdvertiserAssociationRequestContentV1(BaseModel):
    advertiser_ids: Optional[list[str]] = Field(None, alias="advertiserIds", description="A list of advertiser identifiers.")
    frequency_group_ids: Optional[list[str]] = Field(None, alias="frequencyGroupIds", description="A list of frequency group identifiers.")
    include_transitive_associations: Optional[bool] = Field(None, alias="includeTransitiveAssociations", description="An advertiser is transitively associated to a frequency group if one of its campaigns is directly associated to the freq")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Sets the maximum number of objects in the returned array. Use in conjunction with the nextToken parameter to control pag")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token from a previous request. Use in conjunction with the maxResults parameter to control the pagination of the returne")

    model_config = {'populate_by_name': True}


class ListFrequencyGroupAdvertiserAssociationResponseBaseObject(BaseModel):
    advertiser: Optional["ListAdvertiserAssociationResponseBaseObject"] = None
    entity_id: Optional[str] = Field(None, alias="entityId")
    entity_name: Optional[str] = Field(None, alias="entityName")
    frequency_group: Optional["ListAdvertiserFrequencyGroupAssociationResponseBaseObject"] = Field(None, alias="frequencyGroup")
    is_transitive_association: Optional[bool] = Field(None, alias="isTransitiveAssociation", description="Return true, if the campaign is not directly associated to the frequency group, but the advertiser that the campaign bel")

    model_config = {'populate_by_name': True}


class ListFrequencyGroupAssociationRequestContentV1(BaseModel):
    campaign_ids: Optional[list[str]] = Field(None, alias="campaignIds", description="A list of campaign identifiers.")
    frequency_group_ids: Optional[list[str]] = Field(None, alias="frequencyGroupIds", description="A list of frequency group identifiers.")
    include_transitive_associations: Optional[bool] = Field(None, alias="includeTransitiveAssociations", description="A campaign is transitively associated to a frequency group if the advertiser that this campaign belongs to is directly a")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Sets the maximum number of objects in the returned array. Use in conjunction with the nextToken parameter to control pag")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token from a previous request. Use in conjunction with the maxResults parameter to control the pagination of the returne")

    model_config = {'populate_by_name': True}


class ListFrequencyGroupAssociationResponseBaseObject(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="The frequency group identifier.")
    name: Optional[str] = Field(None, description="The frequency group name.")
    owner_id: Optional[str] = Field(None, alias="ownerId", description="If the frequency group belongs to a DSP entity or manager account, ownerId is DSP entity id. If the frequency group belo")
    owner_type: Optional["AdsOwnerType"] = Field(None, alias="ownerType")

    model_config = {'populate_by_name': True}


class ListFrequencyGroupCampaignAssociationResponseBaseObject(BaseModel):
    campaign: Optional["ListCampaignAssociationResponseBaseObject"] = None
    entity_id: Optional[str] = Field(None, alias="entityId")
    entity_name: Optional[str] = Field(None, alias="entityName")
    frequency_group: Optional["ListFrequencyGroupAssociationResponseBaseObject"] = Field(None, alias="frequencyGroup")
    is_transitive_association: Optional[bool] = Field(None, alias="isTransitiveAssociation", description="Return true, if the campaign is not directly associated to the frequency group, but the advertiser that the campaign bel")

    model_config = {'populate_by_name': True}


class UpdateFrequencyGroupAdvertiserAssociationsBaseObject(BaseModel):
    advertiser_id: str = Field(..., alias="advertiserId", description="The advertiser identifier.")
    frequency_group_ids: Optional[list[str]] = Field(None, alias="frequencyGroupIds", description="List of frequency groups identifiers to be associated. Represents the list of frequency groups associated to the adverti")

    model_config = {'populate_by_name': True}


class UpdateFrequencyGroupAdvertiserAssociationRequestContentV1(BaseModel):
    frequency_group_advertiser_associations: Optional[list["UpdateFrequencyGroupAdvertiserAssociationsBaseObject"]] = Field(None, alias="frequencyGroupAdvertiserAssociations")

    model_config = {'populate_by_name': True}


class UpdateFrequencyGroupAssociationsBaseObject(BaseModel):
    """Either frequencyGroupId or frequencyGroups should be provided, not both. Provide frequencyGroupId, if the frequency group belongs to a DSP advertiser. Provide frequencyGroups, if the frequency groups """
    campaign_id: str = Field(..., alias="campaignId", description="The campaign identifier of the campaign.")
    frequency_group_id: Optional[str] = Field(None, alias="frequencyGroupId", description="The frequency group identifier of the frequency group to which campaign needs to be updated. The frequency group should ")
    frequency_groups: Optional[list["FrequencyGroupInput"]] = Field(None, alias="frequencyGroups", description="The list of frequency groups to which campaign needs to be updated. The frequency groups should belong to DSP entities.")

    model_config = {'populate_by_name': True}


class UpdateFrequencyGroupAssociationsRequestContentV1(BaseModel):
    frequency_group_campaign_associations: Optional[list["UpdateFrequencyGroupAssociationsBaseObject"]] = Field(None, alias="frequencyGroupCampaignAssociations")

    model_config = {'populate_by_name': True}


class listAdvertisersFrequencyGroupAssociationsV1ResponseContent(BaseModel):
    advertisers: Optional[list["ListAdvertisersFrequencyGroupAssociationsBaseObject"]] = None
    entity_id: Optional[str] = Field(None, alias="entityId")
    max_results: Optional[float] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken")
    result_count: Optional[float] = Field(None, alias="resultCount")

    model_config = {'populate_by_name': True}


class listCampaignsFrequencyGroupAssociationsV1ResponseContent(BaseModel):
    advertiser_id: Optional[str] = Field(None, alias="advertiserId")
    associations: Optional[list["ListCampaignsFrequencyGroupCampaignAssociationsBaseObject"]] = None
    max_results: Optional[float] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken")
    result_count: Optional[float] = Field(None, alias="resultCount")

    model_config = {'populate_by_name': True}


class listFrequencyGroupAdvertiserAssociationsV1ResponseContent(BaseModel):
    associations: Optional[list["ListFrequencyGroupAdvertiserAssociationResponseBaseObject"]] = Field(None, description="A list of frequency group to advertiser associations returned by the operation.")
    next_token: Optional[str] = Field(None, alias="nextToken")
    total_results: Optional[float] = Field(None, alias="totalResults", description="The total number of results returned by the operation.")

    model_config = {'populate_by_name': True}


class listFrequencyGroupCampaignAssociationsV1ResponseContent(BaseModel):
    associations: Optional[list["ListFrequencyGroupCampaignAssociationResponseBaseObject"]] = Field(None, description="A list of frequency group to campaign associations returned by the operation.")
    next_token: Optional[str] = Field(None, alias="nextToken")
    total_results: Optional[float] = Field(None, alias="totalResults", description="The total number of results returned by the operation.")

    model_config = {'populate_by_name': True}

