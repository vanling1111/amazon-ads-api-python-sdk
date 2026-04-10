"""Auto-generated Pydantic models. Do not edit manually.

Source: CampaignManagement_prod_3p.json
Title:  Campaign Management
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class copyCampaignsError(BaseModel):
    code: Optional[str] = Field(None, description="The status code of the response")
    details: Optional[str] = Field(None, description="A human-readable description of the response")

    model_config = {'populate_by_name': True}


class targetCampaignAttributeStatus(StrEnum):
    ENABLED = "enabled"
    PAUSED = "paused"


class targetCampaignAttribute(BaseModel):
    """Attribute of the campaign"""
    advertiser_id: Optional[str] = Field(None, alias="advertiserId", description="The advertiser id per the targeted marketplace. Advertiser id per marketplace can fetched through /v2/profiles API. Defa")
    budget: Optional[float] = Field(None, description="The budget for the campaign.")
    end_date: Optional[str] = Field(None, alias="endDate", description="The end date for the campaign in formats according to https://tools.ietf.org/html/rfc3339#section-5.6.")
    marketplace_id: Optional[str] = Field(None, alias="marketplaceId", description="The identifier of the target marketplace. Default identifier will be used from the header.")
    name_suffix: str = Field(..., alias="nameSuffix", description="The name to be appended to the campaign. If new name already exists, a number will be appended i.e. if 'Campaign Name Co")
    start_date: Optional[str] = Field(None, alias="startDate", description="The start date of the campaign in formats according to https://tools.ietf.org/html/rfc3339#section-5.6.")
    status: targetCampaignAttributeStatus = Field(..., description="The status of the new copied campaign.")

    model_config = {'populate_by_name': True}


class copyCampaignsItem(BaseModel):
    source_campaign_id: str = Field(..., alias="sourceCampaignId", description="The id of the source campaign.")
    target_campaign_attribute: "targetCampaignAttribute" = Field(..., alias="targetCampaignAttribute")

    model_config = {'populate_by_name': True}


class copyCampaignsRequest(BaseModel):
    copy_campaigns_items: list["copyCampaignsItem"] = Field(..., alias="copyCampaignsItems", description="List of campaign items in the source marketplace")

    model_config = {'populate_by_name': True}


class errorDetail(BaseModel):
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use")
    details: Optional[str] = Field(None, description="A human-readable description of the error, if unsuccessful")

    model_config = {'populate_by_name': True}


class copyCampaignsResponse(BaseModel):
    copy_campaigns_item: Optional["copyCampaignsItem"] = Field(None, alias="copyCampaignsItem")
    error_detail: Optional["errorDetail"] = Field(None, alias="errorDetail")
    request_id: Optional[str] = Field(None, alias="requestId", description="Id of the request to be passed in GET /copy/{requestId}.")

    model_config = {'populate_by_name': True}


class copyCampaignsResponseList(BaseModel):
    copy_campaigns_responses: Optional[list["copyCampaignsResponse"]] = Field(None, alias="copyCampaignsResponses", description="List of all copied campaigns")

    model_config = {'populate_by_name': True}


class copyErrorDetail(BaseModel):
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use")
    details: Optional[str] = Field(None, description="A human-readable description of the error, if unsuccessful")

    model_config = {'populate_by_name': True}


class copyTaskDetailsStatus(StrEnum):
    FAILED = "failed"
    INPROGRESS = "inProgress"
    SUCCEED = "succeed"
    WAITING = "waiting"


class copyTaskDetails(BaseModel):
    """details of the copying process."""
    error_details: Optional[list["copyErrorDetail"]] = Field(None, alias="errorDetails", description="Errors that could occur during async process (up to 10)")
    percentage_completed: Optional[int] = Field(None, alias="percentageCompleted", description="Percent of copy operation that is complete")
    source_advertiser_id: Optional[str] = Field(None, alias="sourceAdvertiserId", description="The identifier of the advertiser in source marketplace.")
    source_campaign_id: Optional[str] = Field(None, alias="sourceCampaignId", description="The identifier of the campaign in the source marketplace.")
    source_marketplace_id: Optional[str] = Field(None, alias="sourceMarketplaceId", description="The source marketplace in obfuscated format.")
    status: Optional[copyTaskDetailsStatus] = Field(None, description="The status of the copying process")
    target_advertiser_id: Optional[str] = Field(None, alias="targetAdvertiserId", description="The identifier of the advertiser in the target marketplace.")
    target_campaign_id: Optional[str] = Field(None, alias="targetCampaignId", description="The identifier of the campaign in the target marketplace.")
    target_marketplace_id: Optional[str] = Field(None, alias="targetMarketplaceId", description="The target marketplace in obfuscated format. The following marketplace pairs (bi-directional) are supported for product ")

    model_config = {'populate_by_name': True}


class getCopyStatusError(BaseModel):
    code: Optional[str] = Field(None, description="The status code of the response")
    details: Optional[str] = Field(None, description="A human-readable description of the response")

    model_config = {'populate_by_name': True}


class getCopyStatusResponse(BaseModel):
    async_task_detail: Optional["copyTaskDetails"] = Field(None, alias="asyncTaskDetail")

    model_config = {'populate_by_name': True}

