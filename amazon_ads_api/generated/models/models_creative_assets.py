"""Auto-generated Pydantic models. Do not edit manually.

Source: CreativeAssetLibrary_openapi.yaml
Title:  Creative assets
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional

from pydantic import BaseModel, Field



class caProgram(StrEnum):
    A_PLUS = "A_PLUS"
    INTEGRATED_VIDEO_EXPERIENCE = "INTEGRATED_VIDEO_EXPERIENCE"
    SB = "SB"
    POSTS = "POSTS"
    STORES = "STORES"
    SPONSORED_BRANDS_VIDEO = "SPONSORED_BRANDS_VIDEO"
    SPONSORED_DISPLAY_VIDEO = "SPONSORED_DISPLAY_VIDEO"
    AMAZON_DSP = "AMAZON_DSP"
    FIRE_TV = "FIRE_TV"
    SPONSORED_TV = "SPONSORED_TV"
    PRODUCT_DESCRIPTION_PAGE = "PRODUCT_DESCRIPTION_PAGE"


class caMetadataMap(BaseModel):
    """Include key-value pairs related to the asset. For DSP use 'dspAdvertiserId' = 'ID'. Include program as AMAZON_DSP."""
    __root__: dict[str, str] = {}


class caAssociatedProgram(BaseModel):
    metadata: Optional["caMetadataMap"] = None
    program_name: Optional["caProgram"] = Field(None, alias="programName")

    model_config = {'populate_by_name': True}


class caFileName(BaseModel):
    """The fileName of the asset."""
    pass


class caAsins(BaseModel):
    """Tagging assets with ASIN, promotes asset discoverability downstream. If ASIN is provided at the time of upload/during asset registration, it is applied as a tag on that asset. This allows for that ass"""
    pass


class caAssetStatus(StrEnum):
    ACTIVE = "ACTIVE"
    PROCESSING = "PROCESSING"
    ARCHIVED = "ARCHIVED"


class caAssetSubType(StrEnum):
    LOGO = "LOGO"
    PRODUCT_IMAGE = "PRODUCT_IMAGE"
    AUTHOR_IMAGE = "AUTHOR_IMAGE"
    LIFESTYLE_IMAGE = "LIFESTYLE_IMAGE"
    OTHER_IMAGE = "OTHER_IMAGE"
    BACKGROUND_VIDEO = "BACKGROUND_VIDEO"


class caassetSubTypes(BaseModel):
    """1. For assetType `IMAGE` acceptable assetSubTypes are `LOGO`, `PRODUCT_IMAGE`, `AUTHOR_IMAGE`, `LIFESTYLE_IMAGE`, `OTHER_IMAGE`  2. For assetType `VIDEO` acceptable assetSubtype is `BACKGROUND_VIDEO`."""
    pass


class caVideoStreamMetadata(BaseModel):
    """Structure containing metadata of Video Stream.  profile: This is the profile of the stream.  width: This is the resolution width of stream.  height: This is the resolution height of stream.  duration:"""
    duration: Optional[float] = None
    frame_rate: Optional[float] = Field(None, alias="frameRate")
    bit_rate: Optional[int] = Field(None, alias="bitRate")
    profile: Optional[str] = None
    width: Optional[int] = None
    codec_name: Optional[str] = Field(None, alias="codecName")
    codec_type: Optional[str] = Field(None, alias="codecType")
    height: Optional[int] = None
    display_aspect_ratio: Optional[str] = Field(None, alias="displayAspectRatio")

    model_config = {'populate_by_name': True}


class caAudioStreamMetadata(BaseModel):
    """Structure containing metadata of Video Stream.  profile: This is the profile of the stream.  duration: This is the duration of the stream in secs.  codecName: This tells the codec of the media stream."""
    duration: Optional[float] = None
    channel_layout: Optional[str] = Field(None, alias="channelLayout")
    bit_rate: Optional[int] = Field(None, alias="bitRate")
    profile: Optional[str] = None
    codec_name: Optional[str] = Field(None, alias="codecName")
    codec_type: Optional[str] = Field(None, alias="codecType")
    sample_rate: Optional[int] = Field(None, alias="sampleRate")

    model_config = {'populate_by_name': True}


class caProcessedFileMetadata(BaseModel):
    """Structure containing metadata of processed file.  contentHash: This is the location of the original source.  contentType: This is the location of the original source.  videoStreams: This contains the """
    video_streams: Optional[list["caVideoStreamMetadata"]] = Field(None, alias="videoStreams")
    audio_streams: Optional[list["caAudioStreamMetadata"]] = Field(None, alias="audioStreams")
    content_type: Optional[str] = Field(None, alias="contentType")
    content_hash: Optional[str] = Field(None, alias="contentHash")

    model_config = {'populate_by_name': True}


class caProcessedUrlType(StrEnum):
    MODERATION = "MODERATION"
    IMAGE_THUMBNAIL_500 = "IMAGE_THUMBNAIL_500"
    VIDEO_DEFAULT_OPTIMIZED = "VIDEO_DEFAULT_OPTIMIZED"
    PRODUCT_VIDEO_OPTIMIZED = "PRODUCT_VIDEO_OPTIMIZED"
    BACKGROUND_VIDEO_TILE = "BACKGROUND_VIDEO_TILE"
    VIDEO_TILE = "VIDEO_TILE"
    INTRO_SPLASH = "INTRO_SPLASH"
    MP4_260KBS_25FPS_48KHZ_64KBS_180P_H264_BASELINE = "MP4_260KBS_25FPS_48KHZ_64KBS_180P_H264_BASELINE"
    MP4_300KBS_15FPS_48KHZ_96KBS_360P = "MP4_300KBS_15FPS_48KHZ_96KBS_360P"
    MP4_300KBS_30FPS_48KHZ_96KBS_360P_H264_BASELINE = "MP4_300KBS_30FPS_48KHZ_96KBS_360P_H264_BASELINE"
    MP4_320KBS_25FPS_48KHZ_96KBS_576P_H264_HIGH = "MP4_320KBS_25FPS_48KHZ_96KBS_576P_H264_HIGH"
    MP4_375KBS_30FPS_48KHZ_192KBS_360P_H264_HIGH = "MP4_375KBS_30FPS_48KHZ_192KBS_360P_H264_HIGH"
    MP4_450KBS_15FPS_48KHZ_96KBS_360P = "MP4_450KBS_15FPS_48KHZ_96KBS_360P"
    MP4_450KBS_30FPS_48KHZ_96KBS_360P_H264_BASELINE = "MP4_450KBS_30FPS_48KHZ_96KBS_360P_H264_BASELINE"
    MP4_600KBS_15FPS_48KHZ_96KBS_480P = "MP4_600KBS_15FPS_48KHZ_96KBS_480P"
    MP4_600KBS_30FPS_48KHZ_96KBS_480P_H264_BASELINE = "MP4_600KBS_30FPS_48KHZ_96KBS_480P_H264_BASELINE"
    MP4_600KBS_25FPS_48KHZ_128KBS_360P_H264_BASELINE = "MP4_600KBS_25FPS_48KHZ_128KBS_360P_H264_BASELINE"
    MP4_600KBS_30FPS_48KHZ_128KBS_360P_H264_BASELINE = "MP4_600KBS_30FPS_48KHZ_128KBS_360P_H264_BASELINE"
    MP4_700KBS_24FPS_48KHZ_96KBS_360P = "MP4_700KBS_24FPS_48KHZ_96KBS_360P"
    MP4_750KBS_30FPS_48KHZ_192KBS_432P_H264_HIGH = "MP4_750KBS_30FPS_48KHZ_192KBS_432P_H264_HIGH"
    MP4_750KBS_25FPS_48KHZ_96KBS_576P_H264_HIGH = "MP4_750KBS_25FPS_48KHZ_96KBS_576P_H264_HIGH"
    MP4_900KBS_15FPS_48KHZ_96KBS_480P = "MP4_900KBS_15FPS_48KHZ_96KBS_480P"
    MP4_900KBS_30FPS_48KHZ_96KBS_480P_H264_BASELINE = "MP4_900KBS_30FPS_48KHZ_96KBS_480P_H264_BASELINE"
    MP4_1350KBS_30FPS_48KHZ_96KBS_720P = "MP4_1350KBS_30FPS_48KHZ_96KBS_720P"
    MP4_1350KBS_30FPS_48KHZ_96KBS_720P_H264_HIGH = "MP4_1350KBS_30FPS_48KHZ_96KBS_720P_H264_HIGH"
    MP4_1350KBS_25FPS_48KHZ_128KBS_540P_H264_MAIN = "MP4_1350KBS_25FPS_48KHZ_128KBS_540P_H264_MAIN"
    MP4_1500KBS_24FPS_48KHZ_96KBS_576P = "MP4_1500KBS_24FPS_48KHZ_96KBS_576P"
    MP4_1500KBS_30FPS_48KHZ_192KBS_540P_H264_HIGH = "MP4_1500KBS_30FPS_48KHZ_192KBS_540P_H264_HIGH"
    MP4_1500KBS_25FPS_48KHZ_128KBS_576P_H264_HIGH = "MP4_1500KBS_25FPS_48KHZ_128KBS_576P_H264_HIGH"
    MP4_2000KBS_30FPS_48KHZ_96KBS_720P = "MP4_2000KBS_30FPS_48KHZ_96KBS_720P"
    MP4_2000KBS_30FPS_48KHZ_96KBS_720P_H264_HIGH = "MP4_2000KBS_30FPS_48KHZ_96KBS_720P_H264_HIGH"
    MP4_2000KBS_30FPS_48KHZ_192KBS_720P_H264_HIGH = "MP4_2000KBS_30FPS_48KHZ_192KBS_720P_H264_HIGH"
    MP4_2100KBS_30FPS_48KHZ_192KBS_576P_H264_HIGH = "MP4_2100KBS_30FPS_48KHZ_192KBS_576P_H264_HIGH"
    MP4_2100KBS_30FPS_48KHZ_192KBS_480P_H264_MAIN = "MP4_2100KBS_30FPS_48KHZ_192KBS_480P_H264_MAIN"
    MP4_3400KBS_30FPS_48KHZ_192KBS_1080P_H264_HIGH = "MP4_3400KBS_30FPS_48KHZ_192KBS_1080P_H264_HIGH"
    MP4_3500KBS_24FPS_48KHZ_96KBS_1080P = "MP4_3500KBS_24FPS_48KHZ_96KBS_1080P"
    MP4_3500KBS_30FPS_48KHZ_128KBS_720P_H264_HIGH = "MP4_3500KBS_30FPS_48KHZ_128KBS_720P_H264_HIGH"
    MP4_4000KBS_30FPS_48KHZ_192KBS_1080P = "MP4_4000KBS_30FPS_48KHZ_192KBS_1080P"
    MP4_4000KBS_30FPS_48KHZ_192KBS_1080P_H264_HIGH = "MP4_4000KBS_30FPS_48KHZ_192KBS_1080P_H264_HIGH"
    MP4_10000KBS_30FPS_48KHZ_320KBS_1080P = "MP4_10000KBS_30FPS_48KHZ_320KBS_1080P"
    MP4_10000KBS_30FPS_48KHZ_320KBS_1080P_H264_HIGH = "MP4_10000KBS_30FPS_48KHZ_320KBS_1080P_H264_HIGH"
    MP4_20000KBS_AUTOFPS_48KHZ_320KBS = "MP4_20000KBS_AUTOFPS_48KHZ_320KBS"
    MP4_20000KBS_AUTOFPS_48KHZ_320KBS_1080P_H264_HIGH = "MP4_20000KBS_AUTOFPS_48KHZ_320KBS_1080P_H264_HIGH"
    MP4_25000KBS_30FPS_48KHZ_192KBS_1080P_H264_HIGH = "MP4_25000KBS_30FPS_48KHZ_192KBS_1080P_H264_HIGH"
    MP4_25000KBS_30FPS_48KHZ_192KBS_1080P_H264_MAIN = "MP4_25000KBS_30FPS_48KHZ_192KBS_1080P_H264_MAIN"


class caProcessedFile(BaseModel):
    """Structure containing url, program, profile and metadata of processed output  program: This is the program for which this transcoding is done.  profile: This is the profile/outformat of the processed f"""
    file_metadata: Optional["caProcessedFileMetadata"] = Field(None, alias="fileMetadata")
    profile: Optional["caProcessedUrlType"] = None
    programs: Optional[list["caProgram"]] = None
    url: Optional[str] = None

    model_config = {'populate_by_name': True}


class caAssetFiles(BaseModel):
    """Structure containing processed transcode files for an asset  defaultUrl: This is the location of the original source.  processedFiles: List of processed files with metadata."""
    processed_files: Optional[list["caProcessedFile"]] = Field(None, alias="processedFiles")
    default_url: Optional[str] = Field(None, alias="defaultUrl")

    model_config = {'populate_by_name': True}


class caVersion(BaseModel):
    """The version of the asset."""
    pass


class caAssetId(BaseModel):
    """The asset identifier."""
    pass


class caAssetIdentifier(BaseModel):
    asset_id: Optional["caAssetId"] = Field(None, alias="assetId")
    version: Optional["caVersion"] = None

    model_config = {'populate_by_name': True}


class caSpecificationProgram(StrEnum):
    SPONSORED_BRANDS_VIDEO = "SPONSORED_BRANDS_VIDEO"
    SPONSORED_DISPLAY_VIDEO = "SPONSORED_DISPLAY_VIDEO"
    SPONSORED_DISPLAY_LANDSCAPE_VIDEO = "SPONSORED_DISPLAY_LANDSCAPE_VIDEO"
    SPONSORED_DISPLAY_PORTRAIT_VIDEO = "SPONSORED_DISPLAY_PORTRAIT_VIDEO"
    SPONSORED_DISPLAY_SQUARE_VIDEO = "SPONSORED_DISPLAY_SQUARE_VIDEO"
    STORES_VIDEO_TILE = "STORES_VIDEO_TILE"
    STORES_BACKGROUND_VIDEO_TILE = "STORES_BACKGROUND_VIDEO_TILE"
    STORES_INTRO_SPLASH = "STORES_INTRO_SPLASH"
    FIRE_TV_FEATURE_ROTATOR = "FIRE_TV_FEATURE_ROTATOR"
    SPONSORED_TV = "SPONSORED_TV"
    SPONSORED_BRANDS_VIDEO_PORTRAIT = "SPONSORED_BRANDS_VIDEO_PORTRAIT"
    DEMAND_SIDE_PLATFORM_OTT = "DEMAND_SIDE_PLATFORM_OTT"
    DEMAND_SIDE_PLATFORM_OLV = "DEMAND_SIDE_PLATFORM_OLV"
    DEMAND_SIDE_PLATFORM_H1_DESKTOP = "DEMAND_SIDE_PLATFORM_H1_DESKTOP"
    DEMAND_SIDE_PLATFORM_H1_MOBILE = "DEMAND_SIDE_PLATFORM_H1_MOBILE"
    LIVE_IMAGE_SPONSORED_DISPLAY = "LIVE_IMAGE_SPONSORED_DISPLAY"


class caSpecCheckApprovedPrograms(BaseModel):
    """List of spec programs for which asset spec check is approved"""
    pass


class caFileMetadataContenttype(StrEnum):
    JPEG = "jpeg"
    JPG = "jpg"
    PNG = "png"
    MP4 = "mp4"
    IMAGE_JPG = "image/jpg"
    IMAGE_JPEG = "image/jpeg"
    IMAGE_PNG = "image/png"


class caFileMetadata(BaseModel):
    duration: Optional[float] = None
    extension: Optional[str] = Field(None, description="The extension of the file name.")
    file_size: Optional[float] = Field(None, alias="fileSize", description="The asset size in bytes.")
    resolution_height: Optional[int] = Field(None, alias="resolutionHeight")
    width: Optional[float] = Field(None, description="The width of the asset in pixels.")
    aspect_ratio: Optional[str] = Field(None, alias="aspectRatio", description="The aspect ration of the asset.")
    resolution_width: Optional[int] = Field(None, alias="resolutionWidth")
    content_type: Optional[caFileMetadataContenttype] = Field(None, alias="contentType", description="The content type of the asset.")
    audio_sample_rate: Optional[float] = Field(None, alias="audioSampleRate")
    height: Optional[float] = Field(None, description="The height of the asset in pixels.")

    model_config = {'populate_by_name': True}


class caModerationStatus(StrEnum):
    REJECTED = "REJECTED"
    APPROVED = "APPROVED"
    PENDING = "PENDING"


class caAdPolicyModerationResult(BaseModel):
    marketplace_id: Optional[str] = Field(None, alias="marketplaceId")
    policy_name: Optional[str] = Field(None, alias="policyName")
    moderation_status: Optional["caModerationStatus"] = Field(None, alias="moderationStatus")
    locale: Optional[str] = None

    model_config = {'populate_by_name': True}


class caModerationContentStatus(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class caModerationContent(BaseModel):
    asset_sub_type: Optional["caAssetSubType"] = Field(None, alias="assetSubType")
    ad_policy_moderation_result_list: Optional[list["caAdPolicyModerationResult"]] = Field(None, alias="adPolicyModerationResultList")
    moderation_content_status: Optional["caModerationContentStatus"] = Field(None, alias="moderationContentStatus")

    model_config = {'populate_by_name': True}


class caProcessedUrlsMap(BaseModel):
    """Map containing processed urls of the asset. Key is the processed type and value is the url"""
    __root__: dict[str, dict[str, Any]] = {}


class caStorageLocationUrls(BaseModel):
    processed_urls: Optional["caProcessedUrlsMap"] = Field(None, alias="processedUrls")
    default_url: Optional[str] = Field(None, alias="defaultUrl")

    model_config = {'populate_by_name': True}


class caURL(BaseModel):
    """The URL of the asset."""
    pass


class caArgumentList(BaseModel):
    """List of arguments for translation string"""
    pass


class caSpecification(BaseModel):
    """Structure containing specification  stringId: This is the translated string Id, client will be retrieving the translation corresponding to this string.  failureReason: This specifies the failure reaso"""
    string_id: Optional[str] = Field(None, alias="stringId")
    is_passed: Optional[bool] = Field(None, alias="isPassed")
    failure_reason: Optional[str] = Field(None, alias="failureReason")
    actual_value: Optional[str] = Field(None, alias="actualValue")
    arguments: Optional["caArgumentList"] = None

    model_config = {'populate_by_name': True}


class caSpecificationList(BaseModel):
    """List of specifications"""
    pass


class caProgramSpecifications(BaseModel):
    """Specification Check for program, This contains program name and specifications"""
    spec_program_name: Optional["caSpecificationProgram"] = Field(None, alias="specProgramName")
    specifications: Optional["caSpecificationList"] = None

    model_config = {'populate_by_name': True}


class caProgramSpecificationsList(BaseModel):
    """Specification Checks for all programs"""
    pass


class caAssetVersion(BaseModel):
    last_updated_by: Optional[str] = Field(None, alias="lastUpdatedBy")
    creation_time: Optional[int] = Field(None, alias="creationTime")
    spec_check_approved_programs: Optional["caSpecCheckApprovedPrograms"] = Field(None, alias="specCheckApprovedPrograms")
    asset_identifier: Optional["caAssetIdentifier"] = Field(None, alias="assetIdentifier")
    asset_files: Optional["caAssetFiles"] = Field(None, alias="assetFiles")
    other_metadata: Optional["caMetadataMap"] = Field(None, alias="otherMetadata")
    url: Optional["caURL"] = None
    asset_sub_types: Optional["caassetSubTypes"] = Field(None, alias="assetSubTypes")
    file_metadata: Optional["caFileMetadata"] = Field(None, alias="fileMetadata")
    created_by: Optional[str] = Field(None, alias="createdBy")
    name: Optional["caFileName"] = None
    last_updated_time: Optional[int] = Field(None, alias="lastUpdatedTime")
    version_notes: Optional[str] = Field(None, alias="versionNotes", description="The URL of the asset")
    asset_status: Optional["caAssetStatus"] = Field(None, alias="assetStatus")
    failed_spec_checks: Optional["caProgramSpecificationsList"] = Field(None, alias="failedSpecChecks")
    storage_location_urls: Optional["caStorageLocationUrls"] = Field(None, alias="storageLocationUrls")
    moderation_content_list: Optional[list["caModerationContent"]] = Field(None, alias="moderationContentList")

    model_config = {'populate_by_name': True}


class caAssetVersionList(BaseModel):
    """The asset version list."""
    pass


class caPageIdentifier(BaseModel):
    page_number: Optional[int] = Field(None, alias="pageNumber")
    token: Optional[str] = None

    model_config = {'populate_by_name': True}


class caPageSize(BaseModel):
    pass


class caPageCriteria(BaseModel):
    """used for pagination  when searching for the first page, no need to put anything, otherwise, use the token returned from previous search call"""
    identifier: Optional["caPageIdentifier"] = None
    size: Optional["caPageSize"] = None

    model_config = {'populate_by_name': True}


class caModerationPolicyMap(BaseModel):
    """A hashmap of key-value pairs, this is the most accurate way of defining a map in swagger 2.0"""
    pass


class caUnauthorizedRequest(BaseModel):
    """401 unauthorized request"""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class caAccounts(BaseModel):
    """The list of advertiser accounts the asset can be shared with. All the accounts within this list will be able to search this asset. Additional validation of checking that the accounts are associated wi"""
    pass


class caMarketplaceIds(BaseModel):
    """The list of marketplace Ids."""
    pass


class caAssetType(StrEnum):
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class caAssetGlobal(BaseModel):
    asset_id: Optional["caAssetId"] = Field(None, alias="assetId")
    asset_type: Optional["caAssetType"] = Field(None, alias="assetType")
    account_ids: Optional["caAccounts"] = Field(None, alias="accountIds")
    marketplace_id: Optional["caMarketplaceIds"] = Field(None, alias="marketplaceId")

    model_config = {'populate_by_name': True}


class caValueFilterValuefield(StrEnum):
    TAG = "TAG"
    ASIN = "ASIN"
    CAMPAIGN_NAME = "CAMPAIGN_NAME"
    CAMPAIGN_ID = "CAMPAIGN_ID"
    PROGRAM = "PROGRAM"
    ASSET_TYPE = "ASSET_TYPE"
    ASSET_SUB_TYPE = "ASSET_SUB_TYPE"
    APPROVED_AD_POLICY = "APPROVED_AD_POLICY"
    ASSET_EXTENSION = "ASSET_EXTENSION"


class caValueFilter(BaseModel):
    """Filter for certain values of asset attributes"""
    values: Optional[list[str]] = None
    value_field: Optional[caValueFilterValuefield] = Field(None, alias="valueField")

    model_config = {'populate_by_name': True}


class caAssociatedContextTypeMapping(BaseModel):
    """A hashmap of key-value pairs, this is the most accurate way of defining a map in swagger 2.0"""
    pass


class caAsset(BaseModel):
    moderation_policy_map: Optional["caModerationPolicyMap"] = Field(None, alias="moderationPolicyMap")
    last_updated_by: Optional[str] = Field(None, alias="lastUpdatedBy")
    creation_time: Optional[int] = Field(None, alias="creationTime")
    spec_check_approved_programs: Optional["caSpecCheckApprovedPrograms"] = Field(None, alias="specCheckApprovedPrograms")
    associated_account_ids: Optional[list[str]] = Field(None, alias="associatedAccountIds")
    marketplaces: Optional[list[str]] = None
    version: Optional[str] = None
    tags: Optional[list[str]] = None
    asset_type: Optional["caAssetType"] = Field(None, alias="assetType")
    file_metadata: Optional["caFileMetadata"] = Field(None, alias="fileMetadata")
    collections: Optional[list[str]] = None
    created_by: Optional[str] = Field(None, alias="createdBy")
    asset_id: Optional[str] = Field(None, alias="assetId")
    storage_location_urls: Optional["caStorageLocationUrls"] = Field(None, alias="storageLocationUrls")
    name: Optional[str] = None
    last_updated_time: Optional[int] = Field(None, alias="lastUpdatedTime")
    associated_contexts: Optional["caAssociatedContextTypeMapping"] = Field(None, alias="associatedContexts")
    asset_sub_types: Optional[list["caAssetSubType"]] = Field(None, alias="assetSubTypes")
    status: Optional["caAssetStatus"] = None

    model_config = {'populate_by_name': True}


class caRange(BaseModel):
    start: Optional[str] = None
    end: Optional[str] = None

    model_config = {'populate_by_name': True}


class SIZE(BaseModel):
    """File size in bytes."""
    pass


class DATEUPLOADED(BaseModel):
    """The value for this should be timestamp in milliseconds. It is the same as creation date."""
    pass


class caValueRangeFilterOptions(BaseModel):
    pass


class caRangeFilter(BaseModel):
    """Filter assets which have certain ranges of asset attributes.  For example, filter assets which have file size in the range of [10,20] or [40,50]."""
    range_field: Optional["caValueRangeFilterOptions"] = Field(None, alias="rangeField")
    ranges: Optional[list["caRange"]] = None

    model_config = {'populate_by_name': True}


class caAssetSortCriteriaField(StrEnum):
    CREATED_TIME = "CREATED_TIME"
    SIZE = "SIZE"
    NAME = "NAME"
    IMAGE_HEIGHT = "IMAGE_HEIGHT"
    IMAGE_WIDTH = "IMAGE_WIDTH"
    EXTENSION = "EXTENSION"


class caAssetSortCriteriaOrder(StrEnum):
    ASC = "ASC"
    DESC = "DESC"


class caAssetSortCriteria(BaseModel):
    field: Optional[caAssetSortCriteriaField] = None
    order: Optional[caAssetSortCriteriaOrder] = None

    model_config = {'populate_by_name': True}


class caSearchAssetText(BaseModel):
    """The text used for searching assets, it matches asset name, asset name prefix, tags and ASINs associated with the assets"""
    pass


class caAssetUploadLocation(BaseModel):
    """The url to upload the asset. The url expires in 15 minutes."""
    pass


class caAssetName(BaseModel):
    """The name to be given to the asset being registered."""
    pass


class caResourceNotFound(BaseModel):
    """404 requested resource not found"""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class caInternalError(BaseModel):
    """500 internal server error"""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class caForbiddenRequest(BaseModel):
    """403 forbidden request"""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class caBadRequest(BaseModel):
    """400 bad request"""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class caFilterCriteria(BaseModel):
    """**Optional** this is used to filter results, we support two types of filters, valueFilter and rangeFilter"""
    value_filters: Optional[list["caValueFilter"]] = Field(None, alias="valueFilters")
    range_filters: Optional[list["caRangeFilter"]] = Field(None, alias="rangeFilters")

    model_config = {'populate_by_name': True}


class caVersionInfo(BaseModel):
    linked_asset_id: Optional[str] = Field(None, alias="linkedAssetId", description="The registering asset will be created as a new version of this linkedAssetId.")
    version_notes: Optional[str] = Field(None, alias="versionNotes", description="The version notes that client can associate to the asset.Versioning enables users to update an old asset, so that you ca")

    model_config = {'populate_by_name': True}


class caRegistrationContext(BaseModel):
    """This is used on registration of an asset, to associate DSP assets to a specific advertiser. This is **required** for assets being uploaded for use in DSP."""
    associated_programs: Optional[list["caAssociatedProgram"]] = Field(None, alias="associatedPrograms")

    model_config = {'populate_by_name': True}


class caAssociatedSubEntity(BaseModel):
    brand_entity_id: Optional[str] = Field(None, alias="brandEntityId", description="The entity id of brand, which can be retrieved using GET /brands.")

    model_config = {'populate_by_name': True}


class caAssociatedSubEntityList(BaseModel):
    """This field is required for sellers, but not required for vendors. The brandEntityId is required for sellers uploading assets for use in Sponsored Brands. As a best practice, ensure to include brandEnt"""
    pass


class caSearchRequestCommon(BaseModel):
    text: Optional["caSearchAssetText"] = None
    filter_criteria: Optional["caFilterCriteria"] = Field(None, alias="filterCriteria")
    sort_criteria: Optional["caAssetSortCriteria"] = Field(None, alias="sortCriteria")
    page_criteria: Optional["caPageCriteria"] = Field(None, alias="pageCriteria")

    model_config = {'populate_by_name': True}


class TAG(BaseModel):
    """A tag is assigned to a creative asset at time of registration. Values can include any tags that you have created."""
    pass


class PROGRAM(StrEnum):
    A_PLUS = "A_PLUS"


class APPROVEDADPOLICY(StrEnum):
    STORE4V_SPOTLIGHT = "STORE4V_SPOTLIGHT"
    STORES_MODERATION = "STORES_MODERATION"
    HSA4V_PRODUCTS = "HSA4V_PRODUCTS"
    AD_POST = "AD_POST"


class CAMPAIGNNAME(BaseModel):
    """The name of the campaign for which to filter."""
    pass


class ASIN(BaseModel):
    """The ASIN value on which to filter."""
    pass


class CAMPAIGNID(BaseModel):
    """The campaignID for which to filter."""
    pass


class ASSETEXTENSION(StrEnum):
    JPG = "JPG"
    JPEG = "JPEG"
    PNG = "PNG"


class ASSETSUBTYPE(StrEnum):
    AUTHOR_IMAGE = "AUTHOR_IMAGE"
    LIFESTYLE_IMAGE = "LIFESTYLE_IMAGE"
    PRODUCT_IMAGE = "PRODUCT_IMAGE"
    OTHER_IMAGE = "OTHER_IMAGE"
    LOGO = "LOGO"


class ASSETTYPE(StrEnum):
    IMAGE = "IMAGE"


class caValueFilterOptions(BaseModel):
    pass


class caAssetSubTypes(BaseModel):
    pass


class caTagName(BaseModel):
    """Tag Name."""
    pass


class caTagList(BaseModel):
    """List of tags."""
    pass


class caAssetSourceMetadataMap(BaseModel):
    """Map containing source information details. Total map size should not exceed 5, with each Key's length 50 and Value's length 500."""
    __root__: dict[str, str] = {}


class caAssetSourceId(StrEnum):
    AMAZON_CREATIVE_SERVICES = "AMAZON_CREATIVE_SERVICES"
    AMAZON_VIDEO_BUILDER = "AMAZON_VIDEO_BUILDER"
    ASSET_LIBRARY = "ASSET_LIBRARY"
    SELF_SERVICE_FIRE_TV = "SELF_SERVICE_FIRE_TV"
    INTEGRATED_VIDEO_EXPERIENCE = "INTEGRATED_VIDEO_EXPERIENCE"
    CANVA_PLUGIN = "CANVA_PLUGIN"
    AMAZON_DSP = "AMAZON_DSP"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    SPONSORED_BRANDS = "SPONSORED_BRANDS"


class caAssetSourceInfo(BaseModel):
    """Details on the source of this asset and any source specific metadata to be associated against it."""
    asset_source_id: Optional["caAssetSourceId"] = Field(None, alias="assetSourceId")
    asset_source_metadata: Optional["caAssetSourceMetadataMap"] = Field(None, alias="assetSourceMetadata")

    model_config = {'populate_by_name': True}


class caBatchRegistrationContext(BaseModel):
    """Contextual information for asset registration e.g. what is the source of this asset."""
    asset_source_info: Optional["caAssetSourceInfo"] = Field(None, alias="assetSourceInfo")

    model_config = {'populate_by_name': True}


class caThrottledRequest(BaseModel):
    """429 request throttled"""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class caRegistrationStatus(StrEnum):
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"


class caFailedRegistrationDetails(BaseModel):
    """Structure containing details of registration failure for each url in a batch registration request."""
    url: Optional[str] = Field(None, description="Url of the media file as provided in the input of batch registration request.")
    failure_reason: Optional[str] = Field(None, alias="failureReason", description="Failure reason for registration of media file identified by corresponding url in batch registration request.")

    model_config = {'populate_by_name': True}


class caFailedRegistrationDetailsList(BaseModel):
    """List containing failed registration details"""
    pass


class caInProgressRegistrationDetails(BaseModel):
    """Structure containing details of in progress registration for each url in a batch registration request."""
    url: Optional[str] = Field(None, description="Url of the media file as provided in the input of batch registration request.")

    model_config = {'populate_by_name': True}


class caInProgressRegistrationDetailsList(BaseModel):
    """List containing in progress registration details"""
    pass


class caSuccessfulRegistrationDetails(BaseModel):
    """Structure containing details of successful registration for each url in a batch registration request."""
    url: Optional[str] = Field(None, description="Url of the media file as provided in the input of batch registration request.")
    asset_identifier: Optional["caAssetIdentifier"] = Field(None, alias="assetIdentifier")

    model_config = {'populate_by_name': True}


class caSuccessfulRegistrationDetailsList(BaseModel):
    """List containing successful registration details"""
    pass

