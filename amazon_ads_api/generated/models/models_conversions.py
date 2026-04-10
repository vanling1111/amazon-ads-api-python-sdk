"""Auto-generated Pydantic models. Do not edit manually.

Source: ConversionsAPI_prod_3p.json
Title:  Conversions API
"""

from __future__ import annotations

from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field



class AmazonAdTagEventAssociationStatusV1(StrEnum):
    AVAILABLE = "AVAILABLE"
    IN_USE = "IN_USE"


class AmazonAdTagEventV1(BaseModel):
    event_name: Optional[str] = Field(None, alias="eventName", description="The name of the event.")
    last_activity_date_time: Optional[str] = Field(None, alias="lastActivityDateTime", description="The last time this event was triggered within the dates supplied by the startDateTime and endDateTime fields.")
    status: Optional["AmazonAdTagEventAssociationStatusV1"] = None

    model_config = {'populate_by_name': True}


class AmazonAdTagV1(BaseModel):
    """An Amazon ad tag for a given advertiser."""
    create_date_time: Optional[str] = Field(None, alias="createDateTime", description="The reported timestamp of when the ad tag was created in ISO format (YYYY-MM-DDThh:mm:ssTZD).")
    tag_id: Optional[str] = Field(None, alias="tagId", description="A string depicting the ID of the ad tag.")

    model_config = {'populate_by_name': True}


class MobileMeasurementPartnerNameV1(StrEnum):
    ADJUST = "ADJUST"
    AIRBRIDGE = "AIRBRIDGE"
    APPSFLYER = "APPSFLYER"
    BRANCH = "BRANCH"
    KOCHAVA = "KOCHAVA"
    SINGULAR = "SINGULAR"
    TENJIN = "TENJIN"


class MobileMeasurementPartnerPlatformV1(StrEnum):
    ANDROID = "ANDROID"
    FIRE_TV = "FIRE_TV"


class MobileMeasurementPartnerAppRegistrationV1(BaseModel):
    app_name: str = Field(..., alias="appName", description="The name of the application.")
    bundle_id: str = Field(..., alias="bundleId", description="The ID of the application with the app store it is registered with. The bundleId + platform + mmpName must be unique wit")
    conversions_created: Optional[float] = Field(None, alias="conversionsCreated", description="The number of conversions associated with this mobile application.")
    last_event_received: Optional[str] = Field(None, alias="lastEventReceived", description="The latest timestamp of when a conversion event for the mobile application was imported in ISO format (YYYY-MM-DDThh:mm:")
    mmp_app_id: Optional[str] = Field(None, alias="mmpAppId", description="The id of the mobile measurement partner app registration.")
    mmp_name: "MobileMeasurementPartnerNameV1" = Field(..., alias="mmpName")
    platform: "MobileMeasurementPartnerPlatformV1"
    skan_conversions_created: Optional[int] = Field(None, alias="skanConversionsCreated", description="Number of SKAN conversions created for this mobile measurement partner app registration.")

    model_config = {'populate_by_name': True}


class AssociatedMobileMeasurementPartnerAppRegistrationV1(BaseModel):
    associated_mobile_app: Optional["MobileMeasurementPartnerAppRegistrationV1"] = Field(None, alias="associatedMobileApp")
    event_name: Optional[str] = Field(None, alias="eventName", description="Mobile measurement partner event associated with this conversion definition")

    model_config = {'populate_by_name': True}


class BatchAssociateConversionDefinitionsRequestV1(BaseModel):
    pass


class BatchAssociateConversionDefinitionsRequestV2(BaseModel):
    pass


class BatchAssociateConversionDefinitionsRequestV3(BaseModel):
    pass


class ConversionDefinitionSuccessResponseV1(BaseModel):
    conversion_definition_id: Optional[str] = Field(None, alias="conversionDefinitionId")
    index: Optional[int] = Field(None, description="The index of the object in the request, starting from 1.")

    model_config = {'populate_by_name': True}


class DspSubErrorV1(BaseModel):
    """The sub error object."""
    error_type: str = Field(..., alias="errorType")
    field_name: Optional[str] = Field(None, alias="fieldName")
    message: str

    model_config = {'populate_by_name': True}


class ConversionDefinitionErrorResponseV1(BaseModel):
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    errors: Optional[list["DspSubErrorV1"]] = None
    index: Optional[int] = Field(None, description="The index of the object in the request, starting from 1.")
    message: Optional[str] = Field(None, description="A human-readable message of the code.")

    model_config = {'populate_by_name': True}


class BatchAssociateConversionDefinitionsResponseV1(BaseModel):
    error: Optional[list["ConversionDefinitionErrorResponseV1"]] = None
    success: Optional[list["ConversionDefinitionSuccessResponseV1"]] = None

    model_config = {'populate_by_name': True}


class ConversionDefinitionSourceV1(StrEnum):
    AMAZON_AD_TAG = "AMAZON_AD_TAG"
    SERVER_TO_SERVER = "SERVER_TO_SERVER"


class ConversionDefinitionCountingMethodV1(StrEnum):
    EVERY = "EVERY"
    FIRST = "FIRST"


class ConversionDefinitionSourceTypeV1(StrEnum):
    ANDROID = "ANDROID"
    FIRE_TABLET = "FIRE_TABLET"
    FIRE_TV = "FIRE_TV"
    IOS = "IOS"
    OFFLINE = "OFFLINE"
    WEBSITE = "WEBSITE"


class ConversionDefinitionTypeV1(StrEnum):
    ADD_TO_SHOPPING_CART = "ADD_TO_SHOPPING_CART"
    APPLICATION = "APPLICATION"
    CHECKOUT = "CHECKOUT"
    CONTACT = "CONTACT"
    LEAD = "LEAD"
    OFF_AMAZON_PURCHASES = "OFF_AMAZON_PURCHASES"
    OTHER = "OTHER"
    PAGE_VIEW = "PAGE_VIEW"
    SEARCH = "SEARCH"
    SIGN_UP = "SIGN_UP"
    SUBSCRIBE = "SUBSCRIBE"


class ConversionDefinitionInputV1(BaseModel):
    """The conversion definition object."""
    conversion_definition_id: Optional[str] = Field(None, alias="conversionDefinitionId", description="The id of the ConversionDefinition.")
    conversion_type: "ConversionDefinitionTypeV1" = Field(..., alias="conversionType")
    counting_method: "ConversionDefinitionCountingMethodV1" = Field(..., alias="countingMethod")
    create_time: Optional[str] = Field(None, alias="createTime", description="The timestamp of when the ConversionDefinition was created in ISO format (YYYY-MM-DDThh:mm:ssTZD).")
    last_activity_time: Optional[str] = Field(None, alias="lastActivityTime", description="The latest timestamp of when a conversion event for the ConversionDefinition was imported in ISO format (YYYY-MM-DDThh:m")
    last_updated_time: Optional[str] = Field(None, alias="lastUpdatedTime", description="Date and time last edit was made to conversion settings in ISO format (YYYY-MM-DDThh:mm:ssTZD).")
    name: str = Field(..., description="The name of the ConversionDefinition.")
    source: "ConversionDefinitionSourceV1"
    source_type: "ConversionDefinitionSourceTypeV1" = Field(..., alias="sourceType")
    value: float = Field(..., description="The value of the event.<br> When the conversionType of the associated Conversion Definition is OFF_AMAZON_PURCHASES, thi")

    model_config = {'populate_by_name': True}


class BatchCreateConversionDefinitionsRequestV1(BaseModel):
    pass


class ConversionDefinitionTypeV2(StrEnum):
    ADD_TO_SHOPPING_CART = "ADD_TO_SHOPPING_CART"
    APPLICATION = "APPLICATION"
    CHECKOUT = "CHECKOUT"
    CONTACT = "CONTACT"
    LEAD = "LEAD"
    MOBILE_APP_FIRST_START = "MOBILE_APP_FIRST_START"
    OFF_AMAZON_PURCHASES = "OFF_AMAZON_PURCHASES"
    OTHER = "OTHER"
    PAGE_VIEW = "PAGE_VIEW"
    SEARCH = "SEARCH"
    SIGN_UP = "SIGN_UP"
    SUBSCRIBE = "SUBSCRIBE"


class ConversionDefinitionInputV2(BaseModel):
    """The conversion definition object."""
    conversion_definition_id: Optional[str] = Field(None, alias="conversionDefinitionId", description="The id of the ConversionDefinition.")
    conversion_type: "ConversionDefinitionTypeV2" = Field(..., alias="conversionType")
    counting_method: "ConversionDefinitionCountingMethodV1" = Field(..., alias="countingMethod")
    create_time: Optional[str] = Field(None, alias="createTime", description="The timestamp of when the ConversionDefinition was created in ISO format (YYYY-MM-DDThh:mm:ssTZD).")
    last_activity_time: Optional[str] = Field(None, alias="lastActivityTime", description="The latest timestamp of when a conversion event for the ConversionDefinition was imported in ISO format (YYYY-MM-DDThh:m")
    last_updated_time: Optional[str] = Field(None, alias="lastUpdatedTime", description="Date and time last edit was made to conversion settings in ISO format (YYYY-MM-DDThh:mm:ssTZD).")
    name: str = Field(..., description="The name of the ConversionDefinition.")
    partner: Optional[str] = Field(None, description="The name of the third-party service used to deliver the conversions (if applicable).")
    source: "ConversionDefinitionSourceV1"
    source_type: "ConversionDefinitionSourceTypeV1" = Field(..., alias="sourceType")
    value: float = Field(..., description="The value of the event.<br> When the conversionType of the associated Conversion Definition is OFF_AMAZON_PURCHASES, thi")

    model_config = {'populate_by_name': True}


class BatchCreateConversionDefinitionsRequestV2(BaseModel):
    pass


class BatchCreateMobileMeasurementPartnerAppRegistrationRequestV1(BaseModel):
    pass


class DeleteMobileMeasurementPartnerAppRegistrationV1(BaseModel):
    mmp_app_id: str = Field(..., alias="mmpAppId")

    model_config = {'populate_by_name': True}


class BatchDeleteMobileMeasurementPartnerAppRegistrationRequestV1(BaseModel):
    pass


class ConversionMatchKeyTypeV1(StrEnum):
    ADDRESS = "ADDRESS"
    CITY = "CITY"
    EMAIL = "EMAIL"
    FIRST_NAME = "FIRST_NAME"
    LAST_NAME = "LAST_NAME"
    MAID = "MAID"
    PHONE = "PHONE"
    POSTAL = "POSTAL"
    RAMP_ID = "RAMP_ID"
    STATE = "STATE"


class ConversionMatchKeyV1(BaseModel):
    """The identifier used to match people for attribution. Match key value must be normalized and hashed, except for MAID which should not be hashed. ADID, IDFA, or FIREADID can be passed into the MAID fiel"""
    type_: "ConversionMatchKeyTypeV1" = Field(..., alias="type")
    values: list[str] = Field(..., description="List of SHA-256 hashed identifier values of the customer who performed the event.")

    model_config = {'populate_by_name': True}


class EventDeletionRequestV1(BaseModel):
    """All ConversionMatchKey objects for a single user should be grouped into a single EventDeletionRequest list."""
    match_keys: Optional[list["ConversionMatchKeyV1"]] = Field(None, alias="matchKeys")

    model_config = {'populate_by_name': True}


class BatchDeleteUserEventsRequestV1(BaseModel):
    deletion_requests: list["EventDeletionRequestV1"] = Field(..., alias="deletionRequests")

    model_config = {'populate_by_name': True}


class ConversionDeletionRequestSuccessResponseV1(BaseModel):
    index: Optional[int] = Field(None, description="The index of the object in the request, starting from 1.")

    model_config = {'populate_by_name': True}


class ConversionDeletionRequestErrorResponseV1(BaseModel):
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    errors: Optional[list["DspSubErrorV1"]] = None
    index: Optional[int] = Field(None, description="The index of the object in the request, starting from 1.")
    message: Optional[str] = Field(None, description="A human-readable message of the code.")

    model_config = {'populate_by_name': True}


class BatchDeleteUserEventsResponseV1(BaseModel):
    error: Optional[list["ConversionDeletionRequestErrorResponseV1"]] = None
    success: Optional[list["ConversionDeletionRequestSuccessResponseV1"]] = None

    model_config = {'populate_by_name': True}


class BatchGetConversionDefinitionsAssociatedForOrdersRequestV1(BaseModel):
    max_results: Optional[int] = Field(None, alias="maxResults", description="Sets the maximum number of conversions in the returned array. Use in conjunction with the `nextToken` parameter to contr")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token from a previous request. Use in conjunction with the `maxResults` parameter to control pagination of the returned ")
    order_ids: Optional[list[str]] = Field(None, alias="orderIds")

    model_config = {'populate_by_name': True}


class BatchOrdersAssociatedConversionDefinitionsV1(BaseModel):
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="Order identifier for this conversion definition.")
    conversion_definition_id: Optional[str] = Field(None, alias="conversionDefinitionId", description="Associated conversion definition identifier for the order.")

    model_config = {'populate_by_name': True}


class BatchGetConversionDefinitionsForOrdersResponseV1(BaseModel):
    conversion_definitions: Optional[list["BatchOrdersAssociatedConversionDefinitionsV1"]] = Field(None, alias="conversionDefinitions", description="List of associated ConversionDefinitions.")
    max_results: Optional[str] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class ConversionDefinitionCurrencyCodeV1(StrEnum):
    AED = "AED"
    AUD = "AUD"
    BRL = "BRL"
    CAD = "CAD"
    CNY = "CNY"
    DKK = "DKK"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"
    JPY = "JPY"
    MXN = "MXN"
    NOK = "NOK"
    NZD = "NZD"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    TRY = "TRY"
    USD = "USD"


class ConversionEventDataV1Dataprocessingoptions(StrEnum):
    LIMITED_DATA_USE = "LIMITED_DATA_USE"


class ConversionEventDataV1(BaseModel):
    client_dedupe_id: Optional[str] = Field(None, alias="clientDedupeId", description="An identifier chosen by the advertiser to represent a user event. This parameter is used for deduplication across all co")
    conversion_definition_id: str = Field(..., alias="conversionDefinitionId", description="The id of the associated ConversionDefinition.")
    country_code: str = Field(..., alias="countryCode", description="The country where the event originates from. e.g. US<br> This value is based on [ISO 3166-1 alpha-2](https://en.wikipedi")
    currency_code: Optional["ConversionDefinitionCurrencyCodeV1"] = Field(None, alias="currencyCode")
    data_processing_options: Optional[ConversionEventDataV1Dataprocessingoptions] = Field(None, alias="dataProcessingOptions", description="A flag for signaling how an event shall be processed. Events marked for limited data use will not be processed.")
    match_keys: list["ConversionMatchKeyV1"] = Field(..., alias="matchKeys", description="Array representing the user and device identifier types/values to be used for attribution to traffic events. Match key v")
    name: str = Field(..., description="The name of the imported event.")
    timestamp: str = Field(..., description="The timestamp when the event occurred in ISO format (YYYY-MM-DDThh:mm:ssTZD). The event's timestamp must be no more than")
    units_sold: Optional[int] = Field(None, alias="unitsSold", description="The number of items purchased. Only applicable for OFF_AMAZON_PURCHASES conversion type. If not provided on the conversi")
    value: Optional[float] = Field(None, description="The value of the event.<br> When the conversionType of the associated Conversion Definition is OFF_AMAZON_PURCHASES, thi")

    model_config = {'populate_by_name': True}


class BatchImportConversionEventDataRequestV1(BaseModel):
    event_data: list["ConversionEventDataV1"] = Field(..., alias="eventData")
    source: "ConversionDefinitionSourceV1"

    model_config = {'populate_by_name': True}


class ConversionEventDataErrorResponseV1(BaseModel):
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    errors: Optional[list["DspSubErrorV1"]] = None
    index: Optional[int] = Field(None, description="The index of the object in the request, starting from 1.")
    message: Optional[str] = Field(None, description="A human-readable message of the code.")

    model_config = {'populate_by_name': True}


class ConversionEventDataSuccessResponseV1(BaseModel):
    index: Optional[int] = Field(None, description="The index of the object in the request, starting from 1.")
    message: Optional[str] = Field(None, description="A human-readable message containing further details.")

    model_config = {'populate_by_name': True}


class BatchImportConversionEventDataResponseV1(BaseModel):
    error: Optional[list["ConversionEventDataErrorResponseV1"]] = None
    success: Optional[list["ConversionEventDataSuccessResponseV1"]] = None

    model_config = {'populate_by_name': True}


class UpdateConversionDefinitionV1(BaseModel):
    conversion_definition_id: str = Field(..., alias="conversionDefinitionId", description="The identifier of the ConversionDefinition.")
    conversion_type: Optional["ConversionDefinitionTypeV1"] = Field(None, alias="conversionType")
    counting_method: Optional["ConversionDefinitionCountingMethodV1"] = Field(None, alias="countingMethod")
    name: Optional[str] = Field(None, description="The name of the ConversionDefinition.")
    source: Optional["ConversionDefinitionSourceV1"] = None
    source_type: Optional["ConversionDefinitionSourceTypeV1"] = Field(None, alias="sourceType")
    value: Optional[float] = Field(None, description="The default value of each conversion event. Monetary value for OFF_AMAZON_PURCHASES ConversionDefinition type and non-mo")

    model_config = {'populate_by_name': True}


class BatchUpdateConversionDefinitionsRequestV1(BaseModel):
    pass


class UpdateConversionDefinitionV2(BaseModel):
    conversion_definition_id: str = Field(..., alias="conversionDefinitionId", description="The identifier of the ConversionDefinition.")
    conversion_type: Optional["ConversionDefinitionTypeV2"] = Field(None, alias="conversionType")
    counting_method: Optional["ConversionDefinitionCountingMethodV1"] = Field(None, alias="countingMethod")
    name: Optional[str] = Field(None, description="The name of the ConversionDefinition.")
    partner: Optional[str] = Field(None, description="The name of the third-party service used to deliver the conversions (if applicable).")
    source: Optional["ConversionDefinitionSourceV1"] = None
    source_type: Optional["ConversionDefinitionSourceTypeV1"] = Field(None, alias="sourceType")
    value: Optional[float] = Field(None, description="The default value of each conversion event. Monetary value for OFF_AMAZON_PURCHASES ConversionDefinition type and non-mo")

    model_config = {'populate_by_name': True}


class BatchUpdateConversionDefinitionsRequestV2(BaseModel):
    pass


class UpdateMobileMeasurementPartnerAppRegistrationV1(BaseModel):
    app_name: Optional[str] = Field(None, alias="appName", description="The name of the application.")
    bundle_id: Optional[str] = Field(None, alias="bundleId", description="The ID of the application with the app store it is registered with.")
    mmp_app_id: str = Field(..., alias="mmpAppId", description="The identifier of the app registration.")

    model_config = {'populate_by_name': True}


class BatchUpdateMobileMeasurementPartnerAppRegistrationRequestV1(BaseModel):
    pass


class CampaignAssociatedConversionDefinitionV2(BaseModel):
    conversion_weight: Optional[float] = Field(None, alias="conversionWeight", description="The weight assigned to this conversion definition for optimization purposes. Supports weights ranging from 0-10 with up ")
    id_: Optional[str] = Field(None, alias="id", description="Associated conversion definition identifier for the campaign.")

    model_config = {'populate_by_name': True}


class CampaignAssociatedConversionDefinitionsResponseV3(BaseModel):
    conversion_definitions: Optional[list["CampaignAssociatedConversionDefinitionV2"]] = Field(None, alias="conversionDefinitions", description="List of associated ConversionDefinitions for the campaign.")
    max_results: Optional[str] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class ConversionDefinitionAdTagEventAssociationRequestV1Operation(StrEnum):
    ADD = "ADD"
    REMOVE = "REMOVE"


class ConversionDefinitionAdTagEventAssociationRequestV1(BaseModel):
    """The combination of adTagId and adTagEventName identifies an unique adTag event."""
    ad_tag_event_name: str = Field(..., alias="adTagEventName")
    ad_tag_id: str = Field(..., alias="adTagId")
    operation: ConversionDefinitionAdTagEventAssociationRequestV1Operation

    model_config = {'populate_by_name': True}


class ConversionDefinitionAssociatedAdTagEventV1(BaseModel):
    ad_tag_event_name: Optional[str] = Field(None, alias="adTagEventName")
    ad_tag_id: Optional[str] = Field(None, alias="adTagId")

    model_config = {'populate_by_name': True}


class ConversionDefinitionCreatedByV1(BaseModel):
    account_id: Optional[str] = Field(None, alias="accountId", description="ID of the account which created the conversion definition. The value could be either DSP Advertiser ID or manager Accoun")
    name: Optional[str] = Field(None, description="Name of the account which created the conversion definition.")

    model_config = {'populate_by_name': True}


class ConversionDefinitionCreatedSourceV1(StrEnum):
    AMAZON_AD_TAG = "AMAZON_AD_TAG"
    MMP = "MMP"
    SERVER_TO_SERVER = "SERVER_TO_SERVER"


class ConversionDefinitionFilterV1Field(StrEnum):
    CONVERSION_DEFINITION_ID = "CONVERSION_DEFINITION_ID"


class ConversionDefinitionFilterV1(BaseModel):
    field: ConversionDefinitionFilterV1Field
    values: list[str]

    model_config = {'populate_by_name': True}


class ConversionDefinitionMeasurementTypeV1(StrEnum):
    SKAN = "SKAN"


class ConversionDefinitionV1(BaseModel):
    """The conversion definition object."""
    conversion_definition_id: Optional[str] = Field(None, alias="conversionDefinitionId", description="The id of the ConversionDefinition.")
    conversion_type: "ConversionDefinitionTypeV1" = Field(..., alias="conversionType")
    counting_method: "ConversionDefinitionCountingMethodV1" = Field(..., alias="countingMethod")
    create_time: Optional[str] = Field(None, alias="createTime", description="The timestamp of when the ConversionDefinition was created in ISO format (YYYY-MM-DDThh:mm:ssTZD).")
    created_by: Optional["ConversionDefinitionCreatedByV1"] = Field(None, alias="createdBy")
    last_activity_time: Optional[str] = Field(None, alias="lastActivityTime", description="The latest timestamp of when a conversion event for the ConversionDefinition was imported in ISO format (YYYY-MM-DDThh:m")
    last_updated_time: Optional[str] = Field(None, alias="lastUpdatedTime", description="Date and time last edit was made to conversion settings in ISO format (YYYY-MM-DDThh:mm:ssTZD).")
    measurement_type: Optional["ConversionDefinitionMeasurementTypeV1"] = Field(None, alias="measurementType")
    name: str = Field(..., description="The name of the ConversionDefinition.")
    source: "ConversionDefinitionSourceV1"
    source_type: "ConversionDefinitionSourceTypeV1" = Field(..., alias="sourceType")
    value: float = Field(..., description="The value of the event.<br> When the conversionType of the associated Conversion Definition is OFF_AMAZON_PURCHASES, thi")

    model_config = {'populate_by_name': True}


class ConversionDefinitionV2(BaseModel):
    """The conversion definition object."""
    conversion_definition_id: Optional[str] = Field(None, alias="conversionDefinitionId", description="The id of the ConversionDefinition.")
    conversion_type: "ConversionDefinitionTypeV2" = Field(..., alias="conversionType")
    counting_method: "ConversionDefinitionCountingMethodV1" = Field(..., alias="countingMethod")
    create_time: Optional[str] = Field(None, alias="createTime", description="The timestamp of when the ConversionDefinition was created in ISO format (YYYY-MM-DDThh:mm:ssTZD).")
    created_by: Optional["ConversionDefinitionCreatedByV1"] = Field(None, alias="createdBy")
    data_set_name: Optional[str] = Field(None, alias="dataSetName", description="The dataset name linked to this conversion definition.")
    last_activity_time: Optional[str] = Field(None, alias="lastActivityTime", description="The latest timestamp of when a conversion event for the ConversionDefinition was imported in ISO format (YYYY-MM-DDThh:m")
    last_updated_time: Optional[str] = Field(None, alias="lastUpdatedTime", description="Date and time last edit was made to conversion settings in ISO format (YYYY-MM-DDThh:mm:ssTZD).")
    measurement_type: Optional["ConversionDefinitionMeasurementTypeV1"] = Field(None, alias="measurementType")
    name: str = Field(..., description="The name of the ConversionDefinition.")
    partner: Optional[str] = Field(None, description="The name of the third-party service used to deliver the conversions (if applicable).")
    source: "ConversionDefinitionCreatedSourceV1"
    source_type: "ConversionDefinitionSourceTypeV1" = Field(..., alias="sourceType")
    value: float = Field(..., description="The value of the event.<br> When the conversionType of the associated Conversion Definition is OFF_AMAZON_PURCHASES, thi")

    model_config = {'populate_by_name': True}


class ConversionDefinitionsBatchResponseV1(BaseModel):
    error: Optional[list["ConversionDefinitionErrorResponseV1"]] = None
    success: Optional[list["ConversionDefinitionSuccessResponseV1"]] = None

    model_config = {'populate_by_name': True}


class DspErrorV1(BaseModel):
    """The error response object."""
    errors: Optional[list["DspSubErrorV1"]] = None
    message: Optional[str] = Field(None, description="A human-readable description of the response.")
    request_id: Optional[str] = Field(None, alias="requestId", description="A value created by Amazon API Gateway that uniquely identifies your request.")

    model_config = {'populate_by_name': True}


class GetAdTagResponseV1(BaseModel):
    ad_tag: Optional["AmazonAdTagV1"] = Field(None, alias="adTag")

    model_config = {'populate_by_name': True}


class ListAdTagEventsResponseV1(BaseModel):
    amazon_ad_tag_events: Optional[list["AmazonAdTagEventV1"]] = Field(None, alias="amazonAdTagEvents", description="Array of Amazon ad tag events given filters.")
    max_results: Optional[int] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token from a previous request. Use in conjunction with the `maxResults` parameter to control pagination of the returned ")

    model_config = {'populate_by_name': True}


class ListConversionDefinitionsRequestV1(BaseModel):
    filters: Optional[list["ConversionDefinitionFilterV1"]] = None
    max_results: Optional[int] = Field(None, alias="maxResults", description="Sets the maximum number of conversions in the returned array. Use in conjunction with the `nextToken` parameter to contr")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token from a previous request. Use in conjunction with the `maxResults` parameter to control pagination of the returned ")

    model_config = {'populate_by_name': True}


class ListConversionDefinitionsResponseV1(BaseModel):
    conversion_definitions: Optional[list["ConversionDefinitionV1"]] = Field(None, alias="conversionDefinitions", description="Array of conversion definitions given filters.")
    max_results: Optional[int] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class ListConversionDefinitionsResponseV2(BaseModel):
    conversion_definitions: Optional[list["ConversionDefinitionV2"]] = Field(None, alias="conversionDefinitions", description="Array of conversion definitions given filters.")
    max_results: Optional[int] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class MobileMeasurementPartnerAppRegistrationFilterV1Field(StrEnum):
    APP_NAME = "APP_NAME"
    APP_STORE_ID = "APP_STORE_ID"
    MMP_NAME = "MMP_NAME"
    PLATFORM = "PLATFORM"


class MobileMeasurementPartnerAppRegistrationFilterV1(BaseModel):
    field: MobileMeasurementPartnerAppRegistrationFilterV1Field
    values: list[str]

    model_config = {'populate_by_name': True}


class ListMobileMeasurementPartnerAppRegistrationsRequestV1(BaseModel):
    filters: Optional[list["MobileMeasurementPartnerAppRegistrationFilterV1"]] = None
    max_results: Optional[int] = Field(None, alias="maxResults", description="Sets the maximum number of conversions in the returned array. Use in conjunction with the `nextToken` parameter to contr")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token from a previous request. Use in conjunction with the `maxResults` parameter to control pagination of the returned ")

    model_config = {'populate_by_name': True}


class ListMobileMeasurementPartnerAppRegistrationsResponseV1(BaseModel):
    app_registrations: Optional[list["MobileMeasurementPartnerAppRegistrationV1"]] = Field(None, alias="appRegistrations", description="Array of Mobile Measurement Partner app registrations given filters.")
    max_results: Optional[int] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class MobileMeasurementPartnerErrorResponseV1(BaseModel):
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    errors: Optional[list["DspSubErrorV1"]] = None
    index: Optional[int] = Field(None, description="The index of the object in the request, starting from 1.")
    message: Optional[str] = Field(None, description="A human-readable message of the code.")

    model_config = {'populate_by_name': True}


class MobileMeasurementPartnerSuccessResponseV1(BaseModel):
    index: Optional[int] = Field(None, description="The index of the object in the request, starting from 1.")
    mmp_app_id: Optional[str] = Field(None, alias="mmpAppId", description="ID of the create mobile measurement partner application registration.")

    model_config = {'populate_by_name': True}


class MobileMeasurementPartnerAppBatchResponseV1(BaseModel):
    error: Optional[list["MobileMeasurementPartnerErrorResponseV1"]] = None
    success: Optional[list["MobileMeasurementPartnerSuccessResponseV1"]] = None

    model_config = {'populate_by_name': True}


class OrderAssociatedConversionDefinitionV1(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="Associated conversion definition identifier for the order.")
    is_optimized: Optional[bool] = Field(None, alias="isOptimized", description="Denotes whether this conversion definition is optimized for this order.")

    model_config = {'populate_by_name': True}


class OrderAssociatedConversionDefinitionsResponseV1(BaseModel):
    conversion_definition_ids: Optional[list[str]] = Field(None, alias="conversionDefinitionIds", description="List of associated ConversionDefinition identifiers for the order.")
    max_results: Optional[str] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class OrderAssociatedConversionDefinitionsResponseV2(BaseModel):
    conversion_definitions: Optional[list["OrderAssociatedConversionDefinitionV1"]] = Field(None, alias="conversionDefinitions", description="List of associated ConversionDefinitions for the order.")
    max_results: Optional[str] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}

