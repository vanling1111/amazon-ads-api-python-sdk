"""Auto-generated Pydantic models. Do not edit manually.

Source: PreModeration_prod_3p.json
Title:  PreModeration
"""

from __future__ import annotations

from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field



class AsinComponentComponenttype(StrEnum):
    LANDING_ASIN = "LANDING_ASIN"
    PRODUCT_ASIN = "PRODUCT_ASIN"


class AsinComponent(BaseModel):
    """Asin component which needs to be pre moderated."""
    asin: str = Field(..., description="Asin id to be pre moderated.")
    component_type: AsinComponentComponenttype = Field(..., alias="componentType", description="Type of the asin component.")
    id_: str = Field(..., alias="id", description="Id of the component. The same will be returned as part of the response as well. This can be used to uniquely identify th")

    model_config = {'populate_by_name': True}


class AsinPolicyViolationType(StrEnum):
    REJECTED = "REJECTED"
    WARNING = "WARNING"


class AsinPolicyViolation(BaseModel):
    name: Optional[str] = Field(None, description="A policy violation code.")
    policy_description: Optional[str] = Field(None, alias="policyDescription", description="A human-readable description of the policy.")
    policy_link_url: Optional[str] = Field(None, alias="policyLinkUrl", description="Address of the policy documentation. Follow the link to learn more about the specified policy.")
    type_: Optional[AsinPolicyViolationType] = Field(None, alias="type", description="Type of policy violation.")

    model_config = {'populate_by_name': True}


class AsinComponentResponseComponenttype(StrEnum):
    LANDING_ASIN = "LANDING_ASIN"
    PRODUCT_ASIN = "PRODUCT_ASIN"


class AsinComponentResponsePremoderationstatus(StrEnum):
    APPROVED = "APPROVED"
    FAILED = "FAILED"
    REJECTED = "REJECTED"
    RETRYABLE_FAILURE = "RETRYABLE_FAILURE"


class AsinComponentResponse(BaseModel):
    """Pre-moderation result for an Asin component"""
    asin: Optional[str] = Field(None, description="Pre-moderated Asin Id.")
    component_type: Optional[AsinComponentResponseComponenttype] = Field(None, alias="componentType", description="Type of Asin component.")
    id_: Optional[str] = Field(None, alias="id", description="Id of the component. This is the same id sent as part of the request. This can be used to uniquely identify the componen")
    policy_violations: Optional[list["AsinPolicyViolation"]] = Field(None, alias="policyViolations", description="A list of policy violations for the component that were detected during pre moderation. Note that this field is present ")
    pre_moderation_status: Optional[AsinComponentResponsePremoderationstatus] = Field(None, alias="preModerationStatus", description="The pre-moderation status of the component.")

    model_config = {'populate_by_name': True}


class ClickThroughType(StrEnum):
    AMAZON_DOMAIN = "AMAZON_DOMAIN"
    EXTERNAL_DOMAIN = "EXTERNAL_DOMAIN"


class CreativeSize(BaseModel):
    """Size of the creative"""
    height: Optional[int] = Field(None, description="Height of the creative in pixels")
    width: Optional[int] = Field(None, description="Width of the creative in pixels")

    model_config = {'populate_by_name': True}


class DateComponentComponenttype(StrEnum):
    CAMPAIGN_DATE = "CAMPAIGN_DATE"


class DateComponent(BaseModel):
    """Date component which needs to be pre moderated. Either startDate or endDate must be populated, or both can be populated."""
    component_type: DateComponentComponenttype = Field(..., alias="componentType", description="Type of the date component.")
    end_date: Optional[str] = Field(None, alias="endDate", description="End date of the component in yyyy-MM-dd HH:mm:ss format")
    id_: str = Field(..., alias="id", description="Id of the component. The same will be returned as part of the response as well. This can be used to uniquely identify th")
    start_date: Optional[str] = Field(None, alias="startDate", description="Start date of the component in yyyy-MM-dd HH:mm:ss format")

    model_config = {'populate_by_name': True}


class DatePolicyViolationType(StrEnum):
    REJECTED = "REJECTED"
    WARNING = "WARNING"


class DatePolicyViolation(BaseModel):
    name: Optional[str] = Field(None, description="A policy violation code.")
    policy_description: Optional[str] = Field(None, alias="policyDescription", description="A human-readable description of the policy.")
    policy_link_url: Optional[str] = Field(None, alias="policyLinkUrl", description="Address of the policy documentation. Follow the link to learn more about the specified policy.")
    type_: Optional[DatePolicyViolationType] = Field(None, alias="type", description="Type of policy violation.")

    model_config = {'populate_by_name': True}


class DateComponentResponseComponenttype(StrEnum):
    CAMPAIGN_DATES = "CAMPAIGN_DATES"


class DateComponentResponsePremoderationstatus(StrEnum):
    APPROVED = "APPROVED"
    FAILED = "FAILED"
    REJECTED = "REJECTED"
    RETRYABLE_FAILURE = "RETRYABLE_FAILURE"


class DateComponentResponse(BaseModel):
    """Pre-moderation result for a date component"""
    component_type: Optional[DateComponentResponseComponenttype] = Field(None, alias="componentType", description="Type of the date component.")
    end_date: Optional[str] = Field(None, alias="endDate", description="End date of the component.")
    id_: Optional[str] = Field(None, alias="id", description="Id of the component. This is the same id sent as part of the request. This can be used to uniquely identify the componen")
    policy_violations: Optional[list["DatePolicyViolation"]] = Field(None, alias="policyViolations", description="A list of policy violations for the component that were detected during pre moderation. Note that this field is present ")
    pre_moderation_status: Optional[DateComponentResponsePremoderationstatus] = Field(None, alias="preModerationStatus", description="The pre-moderation status of the component.")
    start_date: Optional[str] = Field(None, alias="startDate", description="Start date of the component.")

    model_config = {'populate_by_name': True}


class LandingPage(BaseModel):
    """Details of landing page. NOTE: Please use urlComponents to send landing page URLs. This field is preserved for future use and maintaining schema compatibility."""
    url: Optional[str] = Field(None, description="Landing Page Url of the component.")

    model_config = {'populate_by_name': True}


class ImageComponentComponenttype(StrEnum):
    BRAND_LOGO = "BRAND_LOGO"
    CUSTOM_IMAGE = "CUSTOM_IMAGE"
    CUSTOM_IMAGE_RESPONSIVE_SIZE = "CUSTOM_IMAGE_RESPONSIVE_SIZE"
    CUSTOM_IMAGE_SIZE_SPECIFIC = "CUSTOM_IMAGE_SIZE_SPECIFIC"
    OTHER_IMAGE = "OTHER_IMAGE"


class ImageComponent(BaseModel):
    """Image component which needs to be pre moderated. A publicly accessible imageUrl must be sent."""
    component_type: ImageComponentComponenttype = Field(..., alias="componentType", description="Type of the image component.")
    id_: str = Field(..., alias="id", description="Id of the component. The same will be returned as part of the response as well. This can be used to uniquely identify th")
    landing_page: Optional["LandingPage"] = Field(None, alias="landingPage")
    url: str = Field(..., description="Url of the image to be pre moderated. The url must be publicly accessible.")

    model_config = {'populate_by_name': True}


class ImageEvidence(BaseModel):
    """Structure of a image evidence"""
    height: Optional[int] = Field(None, description="The height of the content that violates the specified policy within the image.")
    top_left_x: Optional[int] = Field(None, alias="topLeftX", description="The top left X-coordinate of the content that violates the specified policy within the image.")
    top_left_y: Optional[int] = Field(None, alias="topLeftY", description="The top left Y-coordinate of the content that violates the specified policy within the image.")
    width: Optional[int] = Field(None, description="The width of the content that violates the specified policy within the image.")

    model_config = {'populate_by_name': True}


class TextEvidencePosition(BaseModel):
    """Position in the textComponent where the policy violation is detected."""
    end: Optional[int] = Field(None, description="Zero-based index into the text in textComponent where the text specified in violatingText ends.")
    start: Optional[int] = Field(None, description="Zero-based index into the text in textComponent where the text specified in violatingText starts.")

    model_config = {'populate_by_name': True}


class TextEvidence(BaseModel):
    """Structure of a text evidence"""
    position: Optional["TextEvidencePosition"] = Field(None, description="Position in the textComponent where the policy violation is detected.")
    violating_text: Optional[str] = Field(None, alias="violatingText", description="The specific text determined to violate the specified policy in reviewedText.")

    model_config = {'populate_by_name': True}


class ImagePolicyViolationType(StrEnum):
    REJECTED = "REJECTED"
    WARNING = "WARNING"


class ImagePolicyViolation(BaseModel):
    """Structure of policy violation for a image component"""
    image_evidences: Optional[list["ImageEvidence"]] = Field(None, alias="imageEvidences", description="List of evidences for the policy violations detected on the image component.")
    name: Optional[str] = Field(None, description="A policy violation code.")
    policy_description: Optional[str] = Field(None, alias="policyDescription", description="A human-readable description of the policy.")
    policy_link_url: Optional[str] = Field(None, alias="policyLinkUrl", description="Address of the policy documentation. Follow the link to learn more about the specified policy.")
    text_evidences: Optional[list["TextEvidence"]] = Field(None, alias="textEvidences", description="Policy violation on an image can be detected on the ocr detected text on the image as well. This list of text evidences ")
    type_: Optional[ImagePolicyViolationType] = Field(None, alias="type", description="Type of policy violation.")

    model_config = {'populate_by_name': True}


class ImageSpecComputed(BaseModel):
    """Structure of actual specification of an image component, computed by moderation system."""
    image_evidences: Optional[list["ImageEvidence"]] = Field(None, alias="imageEvidences", description="List of evidences for the computed specification value on the image component.")
    violation_description: Optional[str] = Field(None, alias="violationDescription", description="A human-readable description of the computed specification for an image component, which violates the requirement")

    model_config = {'populate_by_name': True}


class ImageSpecViolationName(StrEnum):
    AMAZON_LOGO_BLURRY = "AMAZON_LOGO_BLURRY"
    ANIMATION_MORE_THAN_15_SECONDS = "ANIMATION_MORE_THAN_15_SECONDS"
    ANIMATION_MORE_THAN_30_SECONDS = "ANIMATION_MORE_THAN_30_SECONDS"
    CTA_IN_ALL_CAPS = "CTA_IN_ALL_CAPS"
    CUSTOM_IMAGE_BLURRY = "CUSTOM_IMAGE_BLURRY"
    CUSTOM_IMAGE_CONTAINS_TEXT = "CUSTOM_IMAGE_CONTAINS_TEXT"
    IMAGE_FONT_ILLEGIBLE = "IMAGE_FONT_ILLEGIBLE"
    INVALID_BRAND_LOGO = "INVALID_BRAND_LOGO"
    INVALID_CUSTOM_IMAGE = "INVALID_CUSTOM_IMAGE"
    LANGUAGE_MISMATCH = "LANGUAGE_MISMATCH"
    LOOPS_MORE_THAN_3_TIMES = "LOOPS_MORE_THAN_3_TIMES"
    POOR_IMAGE_OR_VIDEO_QUALITY = "POOR_IMAGE_OR_VIDEO_QUALITY"


class ImageSpecViolationType(StrEnum):
    REJECTED = "REJECTED"
    WARNING = "WARNING"


class ImageSpecViolation(BaseModel):
    """Structure of spec violation for an image component."""
    computed_violations: Optional[list["ImageSpecComputed"]] = Field(None, alias="computedViolations", description="Structure of specifications for an image component, computed by moderation system, which violates the requirement in spe")
    name: Optional[ImageSpecViolationName] = Field(None, description="A spec violation code.")
    spec_description: Optional[str] = Field(None, alias="specDescription", description="A human-readable description of the spec requirement.")
    spec_link_url: Optional[str] = Field(None, alias="specLinkUrl", description="Address of the ad specification documentation. Follow the link to learn more about the required ad specification.")
    type_: Optional[ImageSpecViolationType] = Field(None, alias="type", description="Type of spec violation.")

    model_config = {'populate_by_name': True}


class ImageComponentResponseComponenttype(StrEnum):
    BRAND_LOGO = "BRAND_LOGO"
    CUSTOM_IMAGE = "CUSTOM_IMAGE"
    CUSTOM_IMAGE_RESPONSIVE_SIZE = "CUSTOM_IMAGE_RESPONSIVE_SIZE"
    CUSTOM_IMAGE_SIZE_SPECIFIC = "CUSTOM_IMAGE_SIZE_SPECIFIC"
    OTHER_IMAGE = "OTHER_IMAGE"


class ImageComponentResponsePremoderationstatus(StrEnum):
    APPROVED = "APPROVED"
    FAILED = "FAILED"
    REJECTED = "REJECTED"
    RETRYABLE_FAILURE = "RETRYABLE_FAILURE"


class ImageComponentResponse(BaseModel):
    """Pre moderation result for a image component"""
    component_type: Optional[ImageComponentResponseComponenttype] = Field(None, alias="componentType", description="Type of the image component.")
    id_: Optional[str] = Field(None, alias="id", description="Id of the component. This is the same id sent as part of the request. This can be used to uniquely identify the componen")
    landing_page: Optional["LandingPage"] = Field(None, alias="landingPage")
    policy_violations: Optional[list["ImagePolicyViolation"]] = Field(None, alias="policyViolations", description="A list of policy violations for the component that were detected during pre moderation. Note that this field is present ")
    pre_moderation_status: Optional[ImageComponentResponsePremoderationstatus] = Field(None, alias="preModerationStatus", description="The pre moderation status of the component.")
    spec_violations: Optional[list["ImageSpecViolation"]] = Field(None, alias="specViolations", description="A list of specification violations for the component that were detected during pre moderation. Note that this field is p")
    url: Optional[str] = Field(None, description="Publicly accessible url of the image that got pre moderated.")

    model_config = {'populate_by_name': True}


class ModerationError(BaseModel):
    """The Error Response Object."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class TextComponentComponenttype(StrEnum):
    BRAND_NAME = "BRAND_NAME"
    HEADLINE = "HEADLINE"
    OTHER_TEXT = "OTHER_TEXT"


class TextComponent(BaseModel):
    """Text component which needs to be pre moderated"""
    component_type: TextComponentComponenttype = Field(..., alias="componentType", description="Type of text component.")
    id_: str = Field(..., alias="id", description="Id of the component. The same will be returned as part of the response as well. This can be used to uniquely identify th")
    text: str = Field(..., description="Text which needs to be moderated.")

    model_config = {'populate_by_name': True}


class UrlComponentComponenttype(StrEnum):
    CLICK_THROUGH_URL = "CLICK_THROUGH_URL"


class UrlComponent(BaseModel):
    """URL component which needs to be pre moderated"""
    component_type: UrlComponentComponenttype = Field(..., alias="componentType", description="Type of the URL component")
    id_: str = Field(..., alias="id", description="Id of the component. The same will be returned as part of the response as well.")
    url: str = Field(..., description="URL that needs to be validated")

    model_config = {'populate_by_name': True}


class VideoComponentComponenttype(StrEnum):
    DSP_VIDEO = "DSP_VIDEO"
    OTHER_VIDEO = "OTHER_VIDEO"
    SPONSORED_BRANDS_VIDEO = "SPONSORED_BRANDS_VIDEO"
    SPONSORED_DISPLAY_VIDEO = "SPONSORED_DISPLAY_VIDEO"
    SPONSORED_TV_VIDEO = "SPONSORED_TV_VIDEO"


class VideoComponent(BaseModel):
    """Video component which needs to be pre moderated. A publicly accessible videoUrl must be sent."""
    component_type: VideoComponentComponenttype = Field(..., alias="componentType", description="Type of the video component.")
    id_: str = Field(..., alias="id", description="Id of the component. The same will be returned as part of the response as well. This can be used to uniquely identify th")
    landing_page: Optional["LandingPage"] = Field(None, alias="landingPage")
    url: str = Field(..., description="Url of the video to be pre moderated. The url must be publicly accessible.")

    model_config = {'populate_by_name': True}


class ThirdPartyComponentComponenttype(StrEnum):
    ADSP_3P_DISPLAY = "ADSP_3P_DISPLAY"
    ADSP_3P_VIDEO = "ADSP_3P_VIDEO"


class ThirdPartyComponent(BaseModel):
    """Third party component which needs to be pre-moderated"""
    click_through_type: Optional["ClickThroughType"] = Field(None, alias="clickThroughType")
    component_type: ThirdPartyComponentComponenttype = Field(..., alias="componentType", description="Type of the third party component")
    creative_size: Optional["CreativeSize"] = Field(None, alias="creativeSize")
    id_: str = Field(..., alias="id", description="Id of the component. The same will be returned as part of the response as well.")
    tag: str = Field(..., description="The tag content for validation")

    model_config = {'populate_by_name': True}


class PreModerationRequestAdprogram(StrEnum):
    DSP = "DSP"
    DSP_CONSOLIDATED_TEMPLATE = "DSP_CONSOLIDATED_TEMPLATE"
    DSP_IMAGE = "DSP_IMAGE"
    DSP_REC = "DSP_REC"
    DSP_THIRD_PARTY = "DSP_THIRD_PARTY"
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_BRANDS_SPOTLIGHT = "SPONSORED_BRANDS_SPOTLIGHT"
    SPONSORED_BRANDS_VIDEO = "SPONSORED_BRANDS_VIDEO"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    SPONSORED_DISPLAY_NOT_SOLD_ON_AMAZON = "SPONSORED_DISPLAY_NOT_SOLD_ON_AMAZON"
    SPONSORED_TV = "SPONSORED_TV"
    STORES = "STORES"


class PreModerationRequestLocale(StrEnum):
    AR_AE = "ar-AE"
    DE_DE = "de-DE"
    EN_AE = "en-AE"
    EN_AU = "en-AU"
    EN_CA = "en-CA"
    EN_GB = "en-GB"
    EN_IN = "en-IN"
    EN_JP = "en-JP"
    EN_NL = "en-NL"
    EN_SA = "en-SA"
    EN_US = "en-US"
    ES_ES = "es-ES"
    ES_MX = "es-MX"
    ES_US = "es-US"
    FR_CA = "fr-CA"
    FR_FR = "fr-FR"
    IT_IT = "it-IT"
    JA_JP = "ja-JP"
    KO_KR = "ko-KR"
    NL_NL = "nl-NL"
    PT_BR = "pt-BR"
    TR_TR = "tr-TR"
    ZH_CN = "zh-CN"


class PreModerationRequestTargetlanguage(StrEnum):
    AR = "ar"
    DE = "de"
    EN = "en"
    ES = "es"
    FR = "fr"
    HI = "hi"
    IT = "it"
    JA = "ja"
    NL = "nl"
    PL = "pl"
    PT = "pt"
    RU = "ru"
    SV = "sv"
    TR = "tr"
    ZH = "zh"


class PreModerationRequest(BaseModel):
    """Components details that needs to be sent for pre moderation."""
    ad_program: PreModerationRequestAdprogram = Field(..., alias="adProgram", description="Type of Ad program to which this pre moderation components belong to.")
    asin_components: Optional[list["AsinComponent"]] = Field(None, alias="asinComponents", description="Asin components which needs to be pre moderated.")
    date_components: Optional[list["DateComponent"]] = Field(None, alias="dateComponents", description="Date components which needs to be pre moderated.")
    image_components: Optional[list["ImageComponent"]] = Field(None, alias="imageComponents", description="Image components which needs to be pre moderated.")
    locale: PreModerationRequestLocale = Field(..., description="Specifying locale will translate the premoderation message into that locale's associated language.     | Locale | Langua")
    record_id: Optional[str] = Field(None, alias="recordId", description="Id of the brand/advertiser.")
    target_language: Optional[PreModerationRequestTargetlanguage] = Field(None, alias="targetLanguage", description="Language, in ISO_639-1 standard, that the creative components should be moderated against.")
    text_components: Optional[list["TextComponent"]] = Field(None, alias="textComponents", description="Text components which needs to be pre moderated.")
    third_party_components: Optional[list["ThirdPartyComponent"]] = Field(None, alias="thirdPartyComponents", description="Third party components which need to be pre-moderated")
    url_components: Optional[list["UrlComponent"]] = Field(None, alias="urlComponents", description="URL components which need to be pre-moderated")
    video_components: Optional[list["VideoComponent"]] = Field(None, alias="videoComponents", description="Video components which needs to be pre moderated.")

    model_config = {'populate_by_name': True}


class VideoEvidence(BaseModel):
    """Structure of a video evidence"""
    end: Optional[int] = Field(None, description="The end position (in seconds) of the content that violates the specified policy within the video.")
    start: Optional[int] = Field(None, description="The start position (in seconds) of the content that violates the specified policy within the video.")

    model_config = {'populate_by_name': True}


class VideoSpecComputed(BaseModel):
    """Structure of actual specification of a video component, computed by moderation system."""
    video_evidences: Optional[list["VideoEvidence"]] = Field(None, alias="videoEvidences", description="List of evidences for the the computed specification value on the video component.")
    violation_description: Optional[str] = Field(None, alias="violationDescription", description="A human-readable description of the computed specification for a video component, which violates the requirement.")

    model_config = {'populate_by_name': True}


class VideoSpecViolationName(StrEnum):
    AUDIO_CODEC = "AUDIO_CODEC"
    AUDIO_FORMAT = "AUDIO_FORMAT"
    AUDIO_SAMPLE_RATE = "AUDIO_SAMPLE_RATE"
    AUDIO_STREAM_COUNT = "AUDIO_STREAM_COUNT"
    CHROMA_SUBSAMPLING = "CHROMA_SUBSAMPLING"
    LETTERBOX_FORMAT = "LETTERBOX_FORMAT"
    MAX_FILE_SIZE = "MAX_FILE_SIZE"
    MAX_VIDEO_RESOLUTION_HEIGHT = "MAX_VIDEO_RESOLUTION_HEIGHT"
    MIN_AUDIO_BITRATE = "MIN_AUDIO_BITRATE"
    MIN_AUDIO_CHANNEL_COUNT = "MIN_AUDIO_CHANNEL_COUNT"
    MIN_AUDIO_SAMPLE_RATE = "MIN_AUDIO_SAMPLE_RATE"
    MIN_VIDEO_BITRATE = "MIN_VIDEO_BITRATE"
    MIN_VIDEO_FRAME_RATE = "MIN_VIDEO_FRAME_RATE"
    MIN_VIDEO_RESOLUTION = "MIN_VIDEO_RESOLUTION"
    VIDEO_ASPECT_RATIO = "VIDEO_ASPECT_RATIO"
    VIDEO_CODEC = "VIDEO_CODEC"
    VIDEO_CONTAINER_FORMAT = "VIDEO_CONTAINER_FORMAT"
    VIDEO_DURATION = "VIDEO_DURATION"
    VIDEO_DURATION_RANGE = "VIDEO_DURATION_RANGE"
    VIDEO_FRAME_RATE = "VIDEO_FRAME_RATE"
    VIDEO_RESOLUTION = "VIDEO_RESOLUTION"
    VIDEO_STREAM_COUNT = "VIDEO_STREAM_COUNT"


class VideoSpecViolationType(StrEnum):
    REJECTED = "REJECTED"
    WARNING = "WARNING"


class VideoSpecViolation(BaseModel):
    """Structure of specification violation for a video component."""
    computed_violations: Optional[list["VideoSpecComputed"]] = Field(None, alias="computedViolations", description="Structure of specifications for a video component, computed by moderation system, which violates the requirement in spec")
    name: Optional[VideoSpecViolationName] = Field(None, description="A spec violation code.")
    spec_description: Optional[str] = Field(None, alias="specDescription", description="A human-readable description of the spec requirement.")
    spec_link_url: Optional[str] = Field(None, alias="specLinkUrl", description="Address of the ad specification documentation. Follow the link to learn more about the required ad specification.")
    type_: Optional[VideoSpecViolationType] = Field(None, alias="type", description="Type of spec violation.")

    model_config = {'populate_by_name': True}


class VideoPolicyViolationType(StrEnum):
    REJECTED = "REJECTED"
    WARNING = "WARNING"


class VideoPolicyViolation(BaseModel):
    """Structure of policy violation for a video component"""
    name: Optional[str] = Field(None, description="A policy violation code.")
    policy_description: Optional[str] = Field(None, alias="policyDescription", description="A human-readable description of the policy.")
    policy_link_url: Optional[str] = Field(None, alias="policyLinkUrl", description="Address of the policy documentation. Follow the link to learn more about the specified policy.")
    type_: Optional[VideoPolicyViolationType] = Field(None, alias="type", description="Type of policy violation.")
    video_evidences: Optional[list["VideoEvidence"]] = Field(None, alias="videoEvidences", description="List of evidences for the policy violations detected on the video component.")

    model_config = {'populate_by_name': True}


class VideoComponentResponseComponenttype(StrEnum):
    DSP_VIDEO = "DSP_VIDEO"
    OTHER_VIDEO = "OTHER_VIDEO"
    SPONSORED_BRANDS_VIDEO = "SPONSORED_BRANDS_VIDEO"
    SPONSORED_DISPLAY_VIDEO = "SPONSORED_DISPLAY_VIDEO"
    SPONSORED_TV_VIDEO = "SPONSORED_TV_VIDEO"


class VideoComponentResponsePremoderationstatus(StrEnum):
    APPROVED = "APPROVED"
    FAILED = "FAILED"
    REJECTED = "REJECTED"
    RETRYABLE_FAILURE = "RETRYABLE_FAILURE"


class VideoComponentResponse(BaseModel):
    """Pre moderation result for a video component"""
    component_type: Optional[VideoComponentResponseComponenttype] = Field(None, alias="componentType", description="Type of the video component.")
    id_: Optional[str] = Field(None, alias="id", description="Id of the component. This is the same id sent as part of the request. This can be used to uniquely identify the componen")
    landing_page: Optional["LandingPage"] = Field(None, alias="landingPage")
    policy_violations: Optional[list["VideoPolicyViolation"]] = Field(None, alias="policyViolations", description="A list of policy violations for the component that were detected during pre moderation. Note that this field is present ")
    pre_moderation_status: Optional[VideoComponentResponsePremoderationstatus] = Field(None, alias="preModerationStatus", description="The pre moderation status of the component.")
    spec_violations: Optional[list["VideoSpecViolation"]] = Field(None, alias="specViolations", description="A list of specification violations for the component that were detected during pre moderation. Note that this field is p")
    url: Optional[str] = Field(None, description="Publicly accessible url of the video that got pre moderated.")

    model_config = {'populate_by_name': True}


class TextPolicyViolationType(StrEnum):
    REJECTED = "REJECTED"
    WARNING = "WARNING"


class TextPolicyViolation(BaseModel):
    """Structure of policy violation for a text component"""
    name: Optional[str] = Field(None, description="A policy violation code.")
    policy_description: Optional[str] = Field(None, alias="policyDescription", description="A human-readable description of the policy.")
    policy_link_url: Optional[str] = Field(None, alias="policyLinkUrl", description="Address of the policy documentation. Follow the link to learn more about the specified policy.")
    text_evidences: Optional[list["TextEvidence"]] = Field(None, alias="textEvidences", description="List of text evidences")
    type_: Optional[TextPolicyViolationType] = Field(None, alias="type", description="Type of policy violation.")

    model_config = {'populate_by_name': True}


class TextComponentResponseComponenttype(StrEnum):
    BRAND_NAME = "BRAND_NAME"
    HEADLINE = "HEADLINE"
    OTHER_TEXT = "OTHER_TEXT"


class TextComponentResponsePremoderationstatus(StrEnum):
    APPROVED = "APPROVED"
    FAILED = "FAILED"
    REJECTED = "REJECTED"
    RETRYABLE_FAILURE = "RETRYABLE_FAILURE"


class TextComponentResponse(BaseModel):
    """Pre moderation result for a text component"""
    component_type: Optional[TextComponentResponseComponenttype] = Field(None, alias="componentType", description="Type of the text component.")
    corrections: Optional[list[str]] = Field(None, description="A list of corrected text without any policy violation. You could consider replacing the component with one of the correc")
    id_: Optional[str] = Field(None, alias="id", description="Id of the component. This is the same id sent as part of the request. This can be used to uniquely identify the componen")
    policy_violations: Optional[list["TextPolicyViolation"]] = Field(None, alias="policyViolations", description="A list of policy violations for the component that were detected during pre moderation. Note that this field is present ")
    pre_moderation_status: Optional[TextComponentResponsePremoderationstatus] = Field(None, alias="preModerationStatus", description="The pre moderation status of the component.")
    text: Optional[str] = Field(None, description="Text which got pre moderated.")

    model_config = {'populate_by_name': True}


class UrlSpecViolationName(StrEnum):
    CLICK_THROUGH_URL_CONTAINS_BROWSE_NODES = "CLICK_THROUGH_URL_CONTAINS_BROWSE_NODES"


class UrlSpecViolationType(StrEnum):
    REJECTED = "REJECTED"
    WARNING = "WARNING"


class UrlSpecViolation(BaseModel):
    """Structure of spec violation for a URL component."""
    name: Optional[UrlSpecViolationName] = Field(None, description="A spec violation code.")
    spec_description: Optional[str] = Field(None, alias="specDescription", description="A human-readable description of the spec requirement.")
    spec_link_url: Optional[str] = Field(None, alias="specLinkUrl", description="Address of the ad specification documentation. Follow the link to learn more about the required ad specification.")
    type_: Optional[UrlSpecViolationType] = Field(None, alias="type", description="Type of spec violation.")

    model_config = {'populate_by_name': True}


class UrlComponentResponseComponenttype(StrEnum):
    CLICK_THROUGH_URL = "CLICK_THROUGH_URL"


class UrlComponentResponsePremoderationstatus(StrEnum):
    APPROVED = "APPROVED"
    FAILED = "FAILED"
    REJECTED = "REJECTED"
    RETRYABLE_FAILURE = "RETRYABLE_FAILURE"


class UrlComponentResponse(BaseModel):
    """Pre moderation result for a URL component"""
    component_type: Optional[UrlComponentResponseComponenttype] = Field(None, alias="componentType", description="Type of the URL component.")
    id_: Optional[str] = Field(None, alias="id", description="Id of the component. This is the same id sent as part of the request. This can be used to uniquely identify the componen")
    pre_moderation_status: Optional[UrlComponentResponsePremoderationstatus] = Field(None, alias="preModerationStatus", description="The pre moderation status of the component.")
    spec_violations: Optional[list["UrlSpecViolation"]] = Field(None, alias="specViolations", description="A list of specification violations for the component that were detected during pre moderation. Note that this field is p")
    url: Optional[str] = Field(None, description="URL that got pre moderated.")

    model_config = {'populate_by_name': True}


class ThirdPartySpecViolationName(StrEnum):
    CREATIVE_SIZE_IS_INCORRECTLY_SET = "CREATIVE_SIZE_IS_INCORRECTLY_SET"
    TAG_INCORRECTLY_UPLOADED = "TAG_INCORRECTLY_UPLOADED"


class ThirdPartySpecViolationType(StrEnum):
    REJECTED = "REJECTED"
    WARNING = "WARNING"


class ThirdPartySpecViolation(BaseModel):
    """Structure of spec violation for a third party component."""
    name: Optional[ThirdPartySpecViolationName] = Field(None, description="A spec violation code.")
    spec_description: Optional[str] = Field(None, alias="specDescription", description="A human-readable description of the spec requirement.")
    spec_link_url: Optional[str] = Field(None, alias="specLinkUrl", description="Address of the ad specification documentation. Follow the link to learn more about the required ad specification.")
    type_: Optional[ThirdPartySpecViolationType] = Field(None, alias="type", description="Type of spec violation.")

    model_config = {'populate_by_name': True}


class ThirdPartyComponentResponseComponenttype(StrEnum):
    ADSP_3P_DISPLAY = "ADSP_3P_DISPLAY"
    ADSP_3P_VIDEO = "ADSP_3P_VIDEO"


class ThirdPartyComponentResponsePremoderationstatus(StrEnum):
    APPROVED = "APPROVED"
    FAILED = "FAILED"
    REJECTED = "REJECTED"
    RETRYABLE_FAILURE = "RETRYABLE_FAILURE"


class ThirdPartyComponentResponse(BaseModel):
    """Pre moderation result for a third party component"""
    click_through_type: Optional["ClickThroughType"] = Field(None, alias="clickThroughType")
    component_type: Optional[ThirdPartyComponentResponseComponenttype] = Field(None, alias="componentType", description="Type of the tag component.")
    creative_size: Optional["CreativeSize"] = Field(None, alias="creativeSize")
    id_: Optional[str] = Field(None, alias="id", description="Id of the component. This is the same id sent as part of the request. This can be used to uniquely identify the componen")
    pre_moderation_status: Optional[ThirdPartyComponentResponsePremoderationstatus] = Field(None, alias="preModerationStatus", description="The pre moderation status of the component.")
    spec_violations: Optional[list["ThirdPartySpecViolation"]] = Field(None, alias="specViolations", description="A list of specification violations for the component that were detected during pre moderation. Note that this field is p")
    tag: Optional[str] = Field(None, description="Tag content that got pre moderated.")

    model_config = {'populate_by_name': True}


class PreModerationResponseAdprogram(StrEnum):
    DSP = "DSP"
    DSP_CONSOLIDATED_TEMPLATE = "DSP_CONSOLIDATED_TEMPLATE"
    DSP_IMAGE = "DSP_IMAGE"
    DSP_REC = "DSP_REC"
    DSP_THIRD_PARTY = "DSP_THIRD_PARTY"
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_BRANDS_SPOTLIGHT = "SPONSORED_BRANDS_SPOTLIGHT"
    SPONSORED_BRANDS_VIDEO = "SPONSORED_BRANDS_VIDEO"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    SPONSORED_DISPLAY_NOT_SOLD_ON_AMAZON = "SPONSORED_DISPLAY_NOT_SOLD_ON_AMAZON"
    SPONSORED_TV = "SPONSORED_TV"
    STORES = "STORES"


class PreModerationResponseLocale(StrEnum):
    AR_AE = "ar-AE"
    DE_DE = "de-DE"
    EN_AE = "en-AE"
    EN_AU = "en-AU"
    EN_CA = "en-CA"
    EN_GB = "en-GB"
    EN_IN = "en-IN"
    EN_JP = "en-JP"
    EN_NL = "en-NL"
    EN_SA = "en-SA"
    EN_US = "en-US"
    ES_ES = "es-ES"
    ES_MX = "es-MX"
    ES_US = "es-US"
    FR_CA = "fr-CA"
    FR_FR = "fr-FR"
    IT_IT = "it-IT"
    JA_JP = "ja-JP"
    KO_KR = "ko-KR"
    NL_NL = "nl-NL"
    PT_BR = "pt-BR"
    TR_TR = "tr-TR"
    ZH_CN = "zh-CN"


class PreModerationResponseTargetlanguage(StrEnum):
    AR = "ar"
    DE = "de"
    EN = "en"
    ES = "es"
    FR = "fr"
    HI = "hi"
    IT = "it"
    JA = "ja"
    NL = "nl"
    PL = "pl"
    PT = "pt"
    RU = "ru"
    SV = "sv"
    TR = "tr"
    ZH = "zh"


class PreModerationResponse(BaseModel):
    """Information regarding the policy violations if present for the components, sent for pre moderation."""
    ad_program: Optional[PreModerationResponseAdprogram] = Field(None, alias="adProgram", description="Type of Ad program to which the pre moderation components belong to.")
    asin_components: Optional[list["AsinComponentResponse"]] = Field(None, alias="asinComponents", description="Pre moderation result of the asin components. It will have information regarding the policy violations present if any.")
    date_components: Optional[list["DateComponentResponse"]] = Field(None, alias="dateComponents", description="Pre moderation result of the date components. It will have information regarding the policy violations present if any.")
    image_components: Optional[list["ImageComponentResponse"]] = Field(None, alias="imageComponents", description="Pre moderation result of the image components. It will have information regarding the policy violations present if any.")
    locale: Optional[PreModerationResponseLocale] = Field(None, description="Locale value that was passed in request.")
    pre_moderation_id: Optional[str] = Field(None, alias="preModerationId", description="Unique Id for the moderation Request.")
    record_id: Optional[str] = Field(None, alias="recordId", description="Id of the brand/advertiser.")
    target_language: Optional[PreModerationResponseTargetlanguage] = Field(None, alias="targetLanguage", description="Language, in ISO_639-1 standard, that the creative components should be moderated against.")
    text_components: Optional[list["TextComponentResponse"]] = Field(None, alias="textComponents", description="Pre moderation result of the text components. It will have information regarding the policy violations present if any.")
    third_party_components: Optional[list["ThirdPartyComponentResponse"]] = Field(None, alias="thirdPartyComponents", description="Third party components which need to be pre-moderated")
    url_components: Optional[list["UrlComponentResponse"]] = Field(None, alias="urlComponents", description="Pre moderation result of the URL components. It will have information regarding policy or spec violations present if any")
    video_components: Optional[list["VideoComponentResponse"]] = Field(None, alias="videoComponents", description="Pre moderation result of the video components. It will have information regarding the policy violations present if any.")

    model_config = {'populate_by_name': True}

