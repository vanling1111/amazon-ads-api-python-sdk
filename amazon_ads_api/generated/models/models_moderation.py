"""Auto-generated Pydantic models. Do not edit manually.

Source: Moderation_prod_3p.json
Title:  Moderation
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class ViolatingAsinEvidence(BaseModel):
    asin: Optional[str] = Field(None, description="ASIN which has the ad policy violation.")

    model_config = {'populate_by_name': True}


class ViolatingAsinContent(BaseModel):
    moderated_component: Optional[str] = Field(None, alias="moderatedComponent", description="Moderation component which marked the policy violation.")
    violating_asin_evidences: Optional[list["ViolatingAsinEvidence"]] = Field(None, alias="violatingAsinEvidences")

    model_config = {'populate_by_name': True}


class ImageCrop(BaseModel):
    height: Optional[int] = Field(None, description="Policy violated region's height in pixel.")
    top_left_x: Optional[int] = Field(None, alias="topLeftX", description="Policy violated region's top left X-axis pixel value.")
    top_left_y: Optional[int] = Field(None, alias="topLeftY", description="Policy violated region's top left Y-axis pixel value.")
    width: Optional[int] = Field(None, description="Policy violated region's width in pixel.")

    model_config = {'populate_by_name': True}


class ViolatingImageEvidence(BaseModel):
    violating_image_crop: Optional["ImageCrop"] = Field(None, alias="violatingImageCrop")

    model_config = {'populate_by_name': True}


class ViolatingImageContent(BaseModel):
    moderated_component: Optional[str] = Field(None, alias="moderatedComponent", description="Moderation component which marked the policy violation.")
    reviewed_image_url: Optional[str] = Field(None, alias="reviewedImageUrl", description="URL of the image which has the ad policy violation.")
    violating_image_evidences: Optional[list["ViolatingImageEvidence"]] = Field(None, alias="violatingImageEvidences")

    model_config = {'populate_by_name': True}


class TextPosition(BaseModel):
    end: Optional[int] = Field(None, description="Zero-based index into the text in reviewedText where the text specified in violatingText ends.")
    start: Optional[int] = Field(None, description="Zero-based index into the text in reviewedText where the text specified in violatingText starts.")

    model_config = {'populate_by_name': True}


class ViolatingTextEvidence(BaseModel):
    violating_text: Optional[str] = Field(None, alias="violatingText", description="The specific text determined to violate the specified policy in reviewedText.")
    violating_text_position: Optional["TextPosition"] = Field(None, alias="violatingTextPosition")

    model_config = {'populate_by_name': True}


class ViolatingTextContent(BaseModel):
    """Information about the specific text that violates the specified policy in the campaign."""
    moderated_component: Optional[str] = Field(None, alias="moderatedComponent", description="Moderation component which marked the policy violation.")
    reviewed_text: Optional[str] = Field(None, alias="reviewedText", description="The actual text on which the moderation was done.")
    violating_text_evidences: Optional[list["ViolatingTextEvidence"]] = Field(None, alias="violatingTextEvidences")

    model_config = {'populate_by_name': True}


class VideoPosition(BaseModel):
    end: Optional[int] = Field(None, description="End time of the video having the policy violation.")
    start: Optional[int] = Field(None, description="Start time of the video having the policy violation.")

    model_config = {'populate_by_name': True}


class ViolatingVideoEvidence(BaseModel):
    violating_video_position: Optional["VideoPosition"] = Field(None, alias="violatingVideoPosition")

    model_config = {'populate_by_name': True}


class ViolatingVideoContent(BaseModel):
    moderated_component: Optional[str] = Field(None, alias="moderatedComponent", description="Moderation component which marked the policy violation.")
    reviewed_video_url: Optional[str] = Field(None, alias="reviewedVideoUrl", description="URL of the video which has the ad policy violation.")
    violating_video_evidences: Optional[list["ViolatingVideoEvidence"]] = Field(None, alias="violatingVideoEvidences")

    model_config = {'populate_by_name': True}


class PolicyViolation(BaseModel):
    policy_description: Optional[str] = Field(None, alias="policyDescription", description="A human-readable description of the policy.")
    policy_link_url: Optional[str] = Field(None, alias="policyLinkUrl", description="Address of the policy documentation. Follow the link to learn more about the specified policy.")
    violating_asin_contents: Optional[list["ViolatingAsinContent"]] = Field(None, alias="violatingAsinContents")
    violating_image_contents: Optional[list["ViolatingImageContent"]] = Field(None, alias="violatingImageContents")
    violating_text_contents: Optional[list["ViolatingTextContent"]] = Field(None, alias="violatingTextContents")
    violating_video_contents: Optional[list["ViolatingVideoContent"]] = Field(None, alias="violatingVideoContents")

    model_config = {'populate_by_name': True}


class ModerationStatus(StrEnum):
    APPROVED = "APPROVED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    REJECTED = "REJECTED"


class TextComponentModerationResult(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="The ID of the text component.")
    moderation_status: Optional["ModerationStatus"] = Field(None, alias="moderationStatus", description="The moderation status of the text component.")
    policy_violations: Optional[list["PolicyViolation"]] = Field(None, alias="policyViolations", description="A list of policy violations for a text component that has failed moderation. Note that this field is present in the resp")
    text: Optional[str] = Field(None, description="The text value of the text component.")

    model_config = {'populate_by_name': True}


class ImageComponentModerationResult(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="The ID of the image component.")
    image_url: Optional[str] = Field(None, alias="imageUrl", description="The URL of the image component.")
    moderation_status: Optional["ModerationStatus"] = Field(None, alias="moderationStatus", description="The moderation status of the image component.")
    policy_violations: Optional[list["PolicyViolation"]] = Field(None, alias="policyViolations", description="A list of policy violations for an image component that has failed moderation. Note that this field is present in the re")

    model_config = {'populate_by_name': True}


class VideoComponentModerationResult(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="The ID of the video component.")
    moderation_status: Optional["ModerationStatus"] = Field(None, alias="moderationStatus", description="The moderation status of the video component.")
    policy_violations: Optional[list["PolicyViolation"]] = Field(None, alias="policyViolations", description="A list of policy violations for a video component that has failed moderation. Note that this field is present in the res")
    video_url: Optional[str] = Field(None, alias="videoUrl", description="The URL of the video component.")

    model_config = {'populate_by_name': True}


class ComponentModerationResults(BaseModel):
    """The moderation results of the individual components in the ad. This is currently only available for the SPONSORED_PRODUCTS adProgramType."""
    image_components: Optional[list["ImageComponentModerationResult"]] = Field(None, alias="imageComponents")
    text_components: Optional[list["TextComponentModerationResult"]] = Field(None, alias="textComponents")
    video_components: Optional[list["VideoComponentModerationResult"]] = Field(None, alias="videoComponents")

    model_config = {'populate_by_name': True}


class Id(BaseModel):
    """The unique identifier of the ad which can be obtained after the ad is created using create APIs."""
    pass


class IdType(StrEnum):
    AD_ID = "AD_ID"


class VersionId(BaseModel):
    """The version identifier that helps to keep track of multiple versions of a submitted ad. In case of Sponsored Brands this is the creative version id."""
    pass


class ModerationResult(BaseModel):
    component_moderation_results: Optional["ComponentModerationResults"] = Field(None, alias="componentModerationResults")
    eta_for_moderation: Optional[str] = Field(None, alias="etaForModeration", description="Expected date and time by which moderation will be complete. The format is ISO 8601 in UTC time zone. Note that this fie")
    id_: Optional["Id"] = Field(None, alias="id")
    id_type: Optional["IdType"] = Field(None, alias="idType")
    moderation_status: Optional["ModerationStatus"] = Field(None, alias="moderationStatus")
    policy_violations: Optional[list["PolicyViolation"]] = Field(None, alias="policyViolations", description="A list of policy violations for a campaign that has failed moderation. Note that this field is present in the response o")
    version_id: Optional["VersionId"] = Field(None, alias="versionId")

    model_config = {'populate_by_name': True}


class ModerationResultsAccessDeniedErrorCode(StrEnum):
    ACCESS_DENIED = "ACCESS_DENIED"


class ModerationResultsAccessDeniedError(BaseModel):
    code: Optional[ModerationResultsAccessDeniedErrorCode] = Field(None, description="Access denied error code.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class ModerationResultsAdProgramType(StrEnum):
    SB_PRODUCT_COLLECTION = "SB_PRODUCT_COLLECTION"
    SB_STORE_SPOTLIGHT = "SB_STORE_SPOTLIGHT"
    SB_VIDEO = "SB_VIDEO"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"


class ModerationResultsBadRequestErrorCode(StrEnum):
    BAD_REQUEST = "BAD_REQUEST"


class ModerationResultsBadRequestError(BaseModel):
    code: Optional[ModerationResultsBadRequestErrorCode] = Field(None, description="Bad request error code.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class ModerationResultsInternalServerErrorCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"


class ModerationResultsInternalServerError(BaseModel):
    code: Optional[ModerationResultsInternalServerErrorCode] = Field(None, description="Internal error code.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class ModerationResultsNotFoundErrorCode(StrEnum):
    NOT_FOUND = "NOT_FOUND"


class ModerationResultsNotFoundError(BaseModel):
    code: Optional[ModerationResultsNotFoundErrorCode] = Field(None, description="Not found error code.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}


class NextToken(BaseModel):
    """Operations that return paginated results include a pagination token in this field. To retrieve the next page of results, call the same operation and specify this token in the request. If the `NextToke"""
    pass


class ModerationResultsRequest(BaseModel):
    ad_program_type: "ModerationResultsAdProgramType" = Field(..., alias="adProgramType")
    id_: "Id" = Field(..., alias="id")
    id_type: "IdType" = Field(..., alias="idType")
    max_results: int = Field(..., alias="maxResults", description="Sets a limit on the number of results returned by an operation.")
    moderation_status_filter: Optional[list["ModerationStatus"]] = Field(None, alias="moderationStatusFilter", description="Filter by specific moderation status.")
    next_token: Optional["NextToken"] = Field(None, alias="nextToken")
    version_id_filter: Optional[list["VersionId"]] = Field(None, alias="versionIdFilter", description="Filter by specific version id of the ad. The API will return the ad's all versions moderation status if this field is em")

    model_config = {'populate_by_name': True}


class ModerationResultsResponse(BaseModel):
    moderation_results: Optional[list["ModerationResult"]] = Field(None, alias="moderationResults")
    next_token: Optional["NextToken"] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class ModerationResultsThrottlingErrorCode(StrEnum):
    THROTTLED = "THROTTLED"


class ModerationResultsThrottlingError(BaseModel):
    code: Optional[ModerationResultsThrottlingErrorCode] = Field(None, description="Throttled error code.")
    details: Optional[str] = Field(None, description="A human-readable description of the error response.")

    model_config = {'populate_by_name': True}

