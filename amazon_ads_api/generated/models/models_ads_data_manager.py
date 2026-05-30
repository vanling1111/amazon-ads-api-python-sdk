"""Auto-generated Pydantic models. Do not edit manually.

Source: AdsDataManager_prod_3p.json
Title:  Ads Data Manager
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class Action(StrEnum):
    CREATE = "CREATE"
    DELETE = "DELETE"


class DetailedError(BaseModel):
    """Detailed individual error information."""
    error_code: Optional[float] = Field(None, alias="errorCode")
    error_message: Optional[str] = Field(None, alias="errorMessage")
    error_type: Optional[str] = Field(None, alias="errorType")

    model_config = {'populate_by_name': True}


class AdsCdxBadRequestExceptionResponseContent(BaseModel):
    """Bad Request."""
    code: Optional[str] = Field(None, description="HTTP status code of the error encountered.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")
    errors: Optional[list["DetailedError"]] = Field(None, description="List of detailed errors, if any.")
    message: Optional[str] = Field(None, description="Error message.")

    model_config = {'populate_by_name': True}


class AdsCdxForbiddenRequestExceptionResponseContent(BaseModel):
    """Forbidden. The request failed because the user does not have access to the specified resource."""
    code: Optional[str] = Field(None, description="HTTP status code of the error encountered.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")
    errors: Optional[list["DetailedError"]] = Field(None, description="List of detailed errors, if any.")
    message: Optional[str] = Field(None, description="Error message.")

    model_config = {'populate_by_name': True}


class AdsCdxResourceNotFoundExceptionResponseContent(BaseModel):
    """Not Found. The requested resource does not exist or is not visible for the user."""
    code: Optional[str] = Field(None, description="HTTP status code of the error encountered.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")
    errors: Optional[list["DetailedError"]] = Field(None, description="List of detailed errors, if any.")
    message: Optional[str] = Field(None, description="Error message.")

    model_config = {'populate_by_name': True}


class AdsCdxServerExceptionResponseContent(BaseModel):
    """Internal server error. Retry later. Contact support if this response persists."""
    code: Optional[str] = Field(None, description="HTTP status code of the error encountered.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")
    errors: Optional[list["DetailedError"]] = Field(None, description="List of detailed errors, if any.")
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class CountryCode(StrEnum):
    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AL = "AL"
    AM = "AM"
    AN = "AN"
    AO = "AO"
    AQ = "AQ"
    AR = "AR"
    AS = "AS"
    AT = "AT"
    AU = "AU"
    AW = "AW"
    AX = "AX"
    AZ = "AZ"
    BA = "BA"
    BB = "BB"
    BD = "BD"
    BE = "BE"
    BF = "BF"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BJ = "BJ"
    BL = "BL"
    BM = "BM"
    BN = "BN"
    BO = "BO"
    BQ = "BQ"
    BR = "BR"
    BS = "BS"
    BT = "BT"
    BV = "BV"
    BW = "BW"
    BY = "BY"
    BZ = "BZ"
    CA = "CA"
    CC = "CC"
    CD = "CD"
    CF = "CF"
    CG = "CG"
    CH = "CH"
    CI = "CI"
    CK = "CK"
    CL = "CL"
    CM = "CM"
    CN = "CN"
    CO = "CO"
    CR = "CR"
    CU = "CU"
    CV = "CV"
    CW = "CW"
    CX = "CX"
    CY = "CY"
    CZ = "CZ"
    DE = "DE"
    DJ = "DJ"
    DK = "DK"
    DM = "DM"
    DO = "DO"
    DZ = "DZ"
    EC = "EC"
    EE = "EE"
    EG = "EG"
    EH = "EH"
    ER = "ER"
    ES = "ES"
    ET = "ET"
    FI = "FI"
    FJ = "FJ"
    FK = "FK"
    FM = "FM"
    FO = "FO"
    FR = "FR"
    GA = "GA"
    GB = "GB"
    GD = "GD"
    GE = "GE"
    GF = "GF"
    GG = "GG"
    GH = "GH"
    GI = "GI"
    GL = "GL"
    GM = "GM"
    GN = "GN"
    GP = "GP"
    GQ = "GQ"
    GR = "GR"
    GS = "GS"
    GT = "GT"
    GU = "GU"
    GW = "GW"
    GY = "GY"
    HK = "HK"
    HM = "HM"
    HN = "HN"
    HR = "HR"
    HT = "HT"
    HU = "HU"
    ID = "ID"
    IE = "IE"
    IL = "IL"
    IM = "IM"
    IN = "IN"
    IO = "IO"
    IQ = "IQ"
    IR = "IR"
    IS = "IS"
    IT = "IT"
    JE = "JE"
    JM = "JM"
    JO = "JO"
    JP = "JP"
    KE = "KE"
    KG = "KG"
    KH = "KH"
    KI = "KI"
    KM = "KM"
    KN = "KN"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KY = "KY"
    KZ = "KZ"
    LA = "LA"
    LB = "LB"
    LC = "LC"
    LI = "LI"
    LK = "LK"
    LR = "LR"
    LS = "LS"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    LY = "LY"
    MA = "MA"
    MC = "MC"
    MD = "MD"
    ME = "ME"
    MF = "MF"
    MG = "MG"
    MH = "MH"
    MK = "MK"
    ML = "ML"
    MM = "MM"
    MN = "MN"
    MO = "MO"
    MP = "MP"
    MQ = "MQ"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MU = "MU"
    MV = "MV"
    MW = "MW"
    MX = "MX"
    MY = "MY"
    MZ = "MZ"
    NA = "NA"
    NC = "NC"
    NE = "NE"
    NF = "NF"
    NG = "NG"
    NI = "NI"
    NL = "NL"
    NO = "NO"
    NP = "NP"
    NR = "NR"
    NU = "NU"
    NZ = "NZ"
    OM = "OM"
    PA = "PA"
    PE = "PE"
    PF = "PF"
    PG = "PG"
    PH = "PH"
    PK = "PK"
    PL = "PL"
    PM = "PM"
    PN = "PN"
    PR = "PR"
    PS = "PS"
    PT = "PT"
    PW = "PW"
    PY = "PY"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RS = "RS"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SB = "SB"
    SC = "SC"
    SD = "SD"
    SE = "SE"
    SG = "SG"
    SH = "SH"
    SI = "SI"
    SJ = "SJ"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SR = "SR"
    SS = "SS"
    ST = "ST"
    SV = "SV"
    SX = "SX"
    SY = "SY"
    SZ = "SZ"
    TC = "TC"
    TD = "TD"
    TF = "TF"
    TG = "TG"
    TH = "TH"
    TJ = "TJ"
    TK = "TK"
    TL = "TL"
    TM = "TM"
    TN = "TN"
    TO = "TO"
    TR = "TR"
    TT = "TT"
    TV = "TV"
    TW = "TW"
    TZ = "TZ"
    UA = "UA"
    UG = "UG"
    UM = "UM"
    UNKNOWN = "UNKNOWN"
    US = "US"
    UY = "UY"
    UZ = "UZ"
    VA = "VA"
    VC = "VC"
    VE = "VE"
    VG = "VG"
    VI = "VI"
    VN = "VN"
    VU = "VU"
    WF = "WF"
    WS = "WS"
    XK = "XK"
    YE = "YE"
    YT = "YT"
    ZA = "ZA"
    ZM = "ZM"
    ZW = "ZW"
    ZZ = "ZZ"


class AdsCdxSolCreateAudienceRequestContent(BaseModel):
    """Create Audience DataSet Request."""
    country_code: "CountryCode" = Field(..., alias="countryCode")
    description: Optional[str] = Field(None, description="A description of the DataSet.")
    id_retention: Optional[bool] = Field(None, alias="idRetention", description="Determines retention of hashed data for 90 days and refresh of UID tokens.")
    name: str = Field(..., description="The name of the DataSet.")

    model_config = {'populate_by_name': True}


class PartitionedByEnum(StrEnum):
    DAY = "DAY"
    HOUR = "HOUR"
    MONTH = "MONTH"
    YEAR = "YEAR"


class DataTypeEnum(StrEnum):
    ACTION = "ACTION"
    AMZN_AD_STORAGE = "AMZN_AD_STORAGE"
    AMZN_USER_DATA = "AMZN_USER_DATA"
    ARRAY = "ARRAY"
    CONVERSION_TYPE = "CONVERSION_TYPE"
    COUNTING_METHOD = "COUNTING_METHOD"
    COUNTRY_CODE = "COUNTRY_CODE"
    CURRENCY_CODE = "CURRENCY_CODE"
    DATE = "DATE"
    DECIMAL = "DECIMAL"
    DEDUPE_ID = "DEDUPE_ID"
    EVENT_COUNT = "EVENT_COUNT"
    EVENT_NAME = "EVENT_NAME"
    EVENT_SOURCE = "EVENT_SOURCE"
    EVENT_VALUE = "EVENT_VALUE"
    EXPERIAN_ID = "EXPERIAN_ID"
    EXTERNAL_ID = "EXTERNAL_ID"
    GPP = "GPP"
    HASHED_ADDRESS = "HASHED_ADDRESS"
    HASHED_CITY = "HASHED_CITY"
    HASHED_COUNTRY_CODE = "HASHED_COUNTRY_CODE"
    HASHED_EMAIL_ADDRESS = "HASHED_EMAIL_ADDRESS"
    HASHED_FIRST_NAME = "HASHED_FIRST_NAME"
    HASHED_LAST_NAME = "HASHED_LAST_NAME"
    HASHED_PHONE_NUMBER = "HASHED_PHONE_NUMBER"
    HASHED_STATE = "HASHED_STATE"
    HASHED_ZIP_CODE = "HASHED_ZIP_CODE"
    INTEGER = "INTEGER"
    IP_ADDRESS = "IP_ADDRESS"
    KANTAR_ID = "KANTAR_ID"
    LAST_ACTIVITY = "LAST_ACTIVITY"
    LONG = "LONG"
    MAID = "MAID"
    MAIN_EVENT_TIME = "MAIN_EVENT_TIME"
    MERKLE_ID = "MERKLE_ID"
    NEUSTAR_ID = "NEUSTAR_ID"
    RAMP_ID = "RAMP_ID"
    REAL_ID = "REAL_ID"
    SAMBA_TV_ID = "SAMBA_TV_ID"
    STRING = "STRING"
    TCF = "TCF"
    TIMESTAMP = "TIMESTAMP"
    TRANSUNION_ID = "TRANSUNION_ID"
    UNITS_SOLD = "UNITS_SOLD"


class ColumnType(StrEnum):
    DIMENSION = "DIMENSION"
    METRIC = "METRIC"


class DataSetColumn(BaseModel):
    column_type: Optional["ColumnType"] = Field(None, alias="columnType")
    data_type: "DataTypeEnum" = Field(..., alias="dataType")
    description: Optional[str] = Field(None, description="The description of the column.")
    is_required: Optional[bool] = Field(None, alias="isRequired", description="Boolean to determine if the column is required or not.")
    name: str = Field(..., description="The name of the column.")
    requires_one_way_hashing: Optional[bool] = Field(None, alias="requiresOneWayHashing", description="Indicates whether the data in the column should be one-way hashed.")

    model_config = {'populate_by_name': True}


class MmpPlatform(StrEnum):
    ANDROID = "ANDROID"
    FIRE_TABLET = "FIRE_TABLET"
    FIRE_TV = "FIRE_TV"
    IOS = "IOS"


class MmpName(StrEnum):
    ADJUST = "ADJUST"
    AIRBRIDGE = "AIRBRIDGE"
    APPSFLYER = "APPSFLYER"
    BRANCH = "BRANCH"
    KOCHAVA = "KOCHAVA"
    SINGULAR = "SINGULAR"
    TENJIN = "TENJIN"


class MmpMetadata(BaseModel):
    """MMP (Mobile Measurement Partner) metadata for dataset tracking"""
    app_name: str = Field(..., alias="appName", description="User-defined application name for MMP Registration")
    bundle_id: str = Field(..., alias="bundleId", description="Bundle ID parsed from app store URL")
    mmp_app_id: Optional[str] = Field(None, alias="mmpAppId", description="Unique app registration ID generated by Amazon")
    mmp_name: "MmpName" = Field(..., alias="mmpName")
    platform: "MmpPlatform"
    sk_ad_network_reference: Optional[bool] = Field(None, alias="skAdNetworkReference", description="SKAdNetwork enablement reference")

    model_config = {'populate_by_name': True}


class Metadata(BaseModel):
    """Container for dataset metadata"""
    mmp_metadata: Optional["MmpMetadata"] = Field(None, alias="mmpMetadata")

    model_config = {'populate_by_name': True}


class SchemaType(StrEnum):
    AUDIENCE = "AUDIENCE"
    CUSTOM = "CUSTOM"
    EVENT = "EVENT"


class AdsCdxSolCreateAudienceResponseContent(BaseModel):
    """Create Audience DataSet Response."""
    client_name: str = Field(..., alias="clientName", description="Identification of the source that created the DataSet.")
    country_code: "CountryCode" = Field(..., alias="countryCode")
    created_by: str = Field(..., alias="createdBy", description="Identifier of the user who created the DataSet.")
    data_set_id: Optional[str] = Field(None, alias="dataSetId")
    data_set_type: "SchemaType" = Field(..., alias="dataSetType")
    date_created: str = Field(..., alias="dateCreated", description="The Date Time that the DataSet was created.")
    description: Optional[str] = Field(None, description="A description of the DataSet.")
    id_retention: Optional[bool] = Field(None, alias="idRetention", description="Determines retention of hashed data for 90 days and refresh of UID tokens.")
    last_modified: str = Field(..., alias="lastModified", description="The Date time the DataSet was last modified")
    last_modified_by: str = Field(..., alias="lastModifiedBy", description="Identifier of the user who most recently modified the DataSet.")
    metadata: Optional["Metadata"] = None
    name: str = Field(..., description="The name of the DataSet.")
    partitioned_by: Optional["PartitionedByEnum"] = Field(None, alias="partitionedBy")
    schema: list["DataSetColumn"] = Field(..., description="The list of columns that make up the DataSet Schema.")

    model_config = {'populate_by_name': True}


class AdsCdxSolDuplicateDatasetNameExceptionResponseContent(BaseModel):
    """Dataset with this name already exists."""
    code: Optional[str] = Field(None, description="HTTP status code of the error encountered.")
    dataset_id: Optional[str] = Field(None, alias="datasetId")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")
    errors: Optional[list["DetailedError"]] = Field(None, description="List of detailed errors, if any.")
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class AdsCdxSolGetAudienceResponseContent(BaseModel):
    """Get Audience DataSet Response."""
    client_name: str = Field(..., alias="clientName", description="Identification of the source that created the DataSet.")
    country_code: "CountryCode" = Field(..., alias="countryCode")
    created_by: str = Field(..., alias="createdBy", description="Identifier of the user who created the DataSet.")
    data_set_id: Optional[str] = Field(None, alias="dataSetId")
    data_set_type: "SchemaType" = Field(..., alias="dataSetType")
    date_created: str = Field(..., alias="dateCreated", description="The Date Time that the DataSet was created.")
    description: Optional[str] = Field(None, description="A description of the DataSet.")
    id_retention: Optional[bool] = Field(None, alias="idRetention", description="Determines retention of hashed data for 90 days and refresh of UID tokens.")
    last_modified: str = Field(..., alias="lastModified", description="The Date time the DataSet was last modified")
    last_modified_by: str = Field(..., alias="lastModifiedBy", description="Identifier of the user who most recently modified the DataSet.")
    metadata: Optional["Metadata"] = None
    name: str = Field(..., description="The name of the DataSet.")
    partitioned_by: Optional["PartitionedByEnum"] = Field(None, alias="partitionedBy")
    schema: list["DataSetColumn"] = Field(..., description="The list of columns that make up the DataSet Schema.")

    model_config = {'populate_by_name': True}


class AdsCdxSolGetTermsResponseContent(BaseModel):
    """Get Terms Response"""
    agreement_content: Optional[str] = Field(None, alias="agreementContent", description="The Terms and Conditions agreement content.")
    agreement_token: Optional[str] = Field(None, alias="agreementToken", description="The terms and conditions agreement token. Required to accept an agreement.")
    has_accepted: bool = Field(..., alias="hasAccepted", description="Flag indicating whether the customer has accepted the Ads Data Manager Terms and Conditions.")

    model_config = {'populate_by_name': True}


class CdxDataSetWithoutSchema(BaseModel):
    client_name: str = Field(..., alias="clientName", description="Identification of the source that created the DataSet.")
    country_code: "CountryCode" = Field(..., alias="countryCode")
    created_by: str = Field(..., alias="createdBy", description="Identifier of the user who created the DataSet.")
    data_set_id: str = Field(..., alias="dataSetId", description="Unique identifier that represent the DataSet.")
    data_set_type: "SchemaType" = Field(..., alias="dataSetType")
    date_created: str = Field(..., alias="dateCreated", description="The Date Time that the DataSet was created.")
    description: Optional[str] = Field(None, description="A description of the DataSet.")
    id_retention: Optional[bool] = Field(None, alias="idRetention", description="Determines retention of hashed data for 90 days and refresh of UID tokens.")
    last_modified: str = Field(..., alias="lastModified", description="The Date time the DataSet was last modified")
    last_modified_by: str = Field(..., alias="lastModifiedBy", description="Identifier of the user who most recently modified the DataSet.")
    name: str = Field(..., description="The name of the DataSet.")

    model_config = {'populate_by_name': True}


class AdsCdxSolListAudienceResponseContent(BaseModel):
    """List Audience DataSet Response."""
    data_sets: Optional[list["CdxDataSetWithoutSchema"]] = Field(None, alias="dataSets")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to receive next page of results.")

    model_config = {'populate_by_name': True}


class AdsCdxSolSetTermsAcceptanceRequestContent(BaseModel):
    """Set Terms request."""
    agreement_token: str = Field(..., alias="agreementToken", description="The terms and conditions agreement token.")
    has_accepted: bool = Field(..., alias="hasAccepted", description="Flag indicating whether the Customer has accepted the Ads Data Manager Terms and conditions.")

    model_config = {'populate_by_name': True}


class AdsCdxTooManyRequestsExceptionResponseContent(BaseModel):
    """Too Many Requests. The request was rate-limited. Retry later."""
    code: Optional[str] = Field(None, description="HTTP status code of the error encountered.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")
    errors: Optional[list["DetailedError"]] = Field(None, description="List of detailed errors, if any.")
    message: Optional[str] = Field(None, description="Error message.")

    model_config = {'populate_by_name': True}


class AdsCdxUnauthorizedRequestExceptionResponseContent(BaseModel):
    """Unauthorized. The request failed because the user is not authenticated or is not allowed to invoke the operation."""
    code: Optional[str] = Field(None, description="HTTP status code of the error encountered.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")
    errors: Optional[list["DetailedError"]] = Field(None, description="List of detailed errors, if any.")
    message: Optional[str] = Field(None, description="Error message.")

    model_config = {'populate_by_name': True}


class AmcMetadata(BaseModel):
    amc_instance_id: str = Field(..., alias="amcInstanceId")
    amc_instance_name: Optional[str] = Field(None, alias="amcInstanceName")

    model_config = {'populate_by_name': True}


class ConsentEnums(StrEnum):
    DENIED = "DENIED"
    GRANTED = "GRANTED"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    UNKNOWN = "UNKNOWN"


class AmznConsent(BaseModel):
    amzn_ad_storage: Optional["ConsentEnums"] = Field(None, alias="amznAdStorage")
    amzn_user_data: Optional["ConsentEnums"] = Field(None, alias="amznUserData")

    model_config = {'populate_by_name': True}


class ApplicationId(StrEnum):
    AMAZON_MARKETING_CLOUD = "AMAZON_MARKETING_CLOUD"
    DSP_AUDIENCES = "DSP_AUDIENCES"
    EVENTS_MANAGER = "EVENTS_MANAGER"
    GEO_LOCATIONS = "GEO_LOCATIONS"
    PUBTECH = "PUBTECH"


class Consent(BaseModel):
    amzn: Optional["AmznConsent"] = None
    gpp: Optional[str] = Field(None, description="A field to hold a 'Global Privacy Platform (GPP)' string. Optional.")
    tcf: Optional[str] = Field(None, description="A field to hold the 'Transparency and Consent Framework (TCF)' string. Optional.")

    model_config = {'populate_by_name': True}


class Geo(BaseModel):
    country_code: Optional["CountryCode"] = Field(None, alias="countryCode")
    ip_address: Optional[str] = Field(None, alias="ipAddress", description="A String value holding an ipAddress used to determine country for members in this audience. Optional.")

    model_config = {'populate_by_name': True}


class UserConsent(BaseModel):
    consent: Optional["Consent"] = None
    geo: Optional["Geo"] = None

    model_config = {'populate_by_name': True}


class HashedPii(BaseModel):
    """Structure representing hashed personally identifiable information (PII)."""
    ad: Optional[str] = Field(None, description="Normalized and SHA-256 hashed street address")
    cty: Optional[str] = Field(None, description="Normalized and SHA-256 hashed city name")
    em: Optional[str] = Field(None, description="Normalized and SHA-256 hashed email address")
    fn: Optional[str] = Field(None, description="Normalized and SHA-256 hashed first name")
    ln: Optional[str] = Field(None, description="Normalized and SHA-256 hashed last name")
    ph: Optional[str] = Field(None, description="Normalized and SHA-256 hashed phone number")
    st: Optional[str] = Field(None, description="Normalized and SHA-256 hashed state or region code")
    zip: Optional[str] = Field(None, description="Normalized and SHA-256 hashed postal or zip code")

    model_config = {'populate_by_name': True}


class ExternalIdentity(BaseModel):
    """Support for externalIdentity is planned for the future."""
    experian_id: Optional[str] = Field(None, alias="experianId", description="User identifier provided by Experian")
    kantar_id: Optional[str] = Field(None, alias="kantarId", description="User identifier provided by Kantar")
    live_ramp_id: Optional[str] = Field(None, alias="liveRampId", description="User identifier provided by LiveRamp")
    ma_id: Optional[str] = Field(None, alias="maId", description="Mobile advertising identifier (IDFA for iOS or GAID for Android)")
    merkle_id: Optional[str] = Field(None, alias="merkleId", description="User identifier provided by Merkle")
    neustar_id: Optional[str] = Field(None, alias="neustarId", description="User identifier provided by Neustar")
    real_id: Optional[str] = Field(None, alias="realId", description="User identifier provided by RealId")
    samba_tv_id: Optional[str] = Field(None, alias="sambaTvId", description="User identifier provided by Samba TV")
    transunion_id: Optional[str] = Field(None, alias="transunionId", description="User identifier provided by TransUnion")

    model_config = {'populate_by_name': True}


class Identity(BaseModel):
    """Either one hashedPII object or external identity object is required"""
    external_identities: Optional[list["ExternalIdentity"]] = Field(None, alias="externalIdentities")
    hashed_piis: Optional[list["HashedPii"]] = Field(None, alias="hashedPiis", description="List of hashed personally-identifiable information records to be matched with Amazon identities for future use. All inpu")

    model_config = {'populate_by_name': True}


class AudienceMember(BaseModel):
    action: "Action"
    external_user_id: str = Field(..., alias="externalUserId", description="This is an external user identifier defined by the data owner. Each unique user should have a unique external user ident")
    user_consent: Optional["UserConsent"] = Field(None, alias="userConsent")
    user_identity: "Identity" = Field(..., alias="userIdentity")

    model_config = {'populate_by_name': True}


class AudienceMetadata(BaseModel):
    """A structure to represent the metadata required to create a DSP Audience."""
    audience_name: str = Field(..., alias="audienceName")
    description: Optional[str] = None
    external_audience_id: Optional[str] = Field(None, alias="externalAudienceId")

    model_config = {'populate_by_name': True}


class AudienceResponseMetadata(BaseModel):
    """A structure that represents the audience-specific metadata provided to API consumers."""
    audience_id: str = Field(..., alias="audienceId")
    audience_id_v2: str = Field(..., alias="audienceIdV2")
    audience_name: str = Field(..., alias="audienceName")

    model_config = {'populate_by_name': True}


class AwsRegion(StrEnum):
    EU_WEST_1 = "eu-west-1"
    US_EAST_1 = "us-east-1"
    US_WEST_2 = "us-west-2"


class ConversionDefinitionCountingMethodV1(StrEnum):
    EVERY = "EVERY"
    FIRST = "FIRST"


class ConversionDefinitionSourceV1(StrEnum):
    AMAZON_AD_TAG = "AMAZON_AD_TAG"
    MMP = "MMP"
    SERVER_TO_SERVER = "SERVER_TO_SERVER"


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


class ConversionDefinitionSourceTypeV1(StrEnum):
    ANDROID = "ANDROID"
    FIRE_TABLET = "FIRE_TABLET"
    FIRE_TV = "FIRE_TV"
    IOS = "IOS"
    OFFLINE = "OFFLINE"
    WEBSITE = "WEBSITE"


class ConversionDefinitionMetadata(BaseModel):
    """Base metadata related to a Conversion Definition, typically used in CD creation requests."""
    conversion_type: "ConversionDefinitionTypeV1" = Field(..., alias="conversionType")
    counting_method: "ConversionDefinitionCountingMethodV1" = Field(..., alias="countingMethod")
    name: str
    partner: Optional[str] = None
    source: "ConversionDefinitionSourceV1"
    source_type: "ConversionDefinitionSourceTypeV1" = Field(..., alias="sourceType")
    value: float

    model_config = {'populate_by_name': True}


class ConversionDefinitionResponseMetadata(BaseModel):
    """Metadata for an Conversion Definition response i.e., including a CD id and fields."""
    conversion_definition_id: str = Field(..., alias="conversionDefinitionId")
    conversion_definition_name: str = Field(..., alias="conversionDefinitionName")
    conversion_type: "ConversionDefinitionTypeV1" = Field(..., alias="conversionType")
    counting_method: "ConversionDefinitionCountingMethodV1" = Field(..., alias="countingMethod")
    name: str
    partner: Optional[str] = None
    source: "ConversionDefinitionSourceV1"
    source_type: "ConversionDefinitionSourceTypeV1" = Field(..., alias="sourceType")
    value: float

    model_config = {'populate_by_name': True}


class CreateDataroomResponseContent(BaseModel):
    account_id: str = Field(..., alias="accountId", description="The owner of this Data room")
    assigned_to_account_id: Optional[str] = Field(None, alias="assignedToAccountId", description="The Ads AccountId to which this dataroom is assigned to")
    creation_date_time: str = Field(..., alias="creationDateTime", description="An ISO UTC Timestamp value representing the time the dataroom was created")
    region: Optional["AwsRegion"] = None

    model_config = {'populate_by_name': True}


class DataProviderMetadata(BaseModel):
    """Data provider identification metadata. Used for creating usage reports and, when fees are applied to the audience, billing."""
    data_provider_id: str = Field(..., alias="dataProviderId", description="The Amazon ID for the data provider. This can be distinct from an advertiser ID.")
    data_provider_name: str = Field(..., alias="dataProviderName", description="The name of the data provider.")
    data_provider_reporting_id: Optional[str] = Field(None, alias="dataProviderReportingId", description="An external ID supplied by the data provider for ease of understanding reports sent to the data provider.")

    model_config = {'populate_by_name': True}


class PubTechMetadata(BaseModel):
    """Metadata specific to PubTech, including data provider and audience information."""
    allowed_countries: list["CountryCode"] = Field(..., alias="allowedCountries")
    audience_name: str = Field(..., alias="audienceName")
    data_provider_metadata: Optional["DataProviderMetadata"] = Field(None, alias="dataProviderMetadata")
    description: Optional[str] = None
    existing_audience_targeting_value: Optional[str] = Field(None, alias="existingAudienceTargetingValue", description="The targeting value for an existing PubTech audience. This maps to the `customExecutionId` of a TaxonomyNode. This is th")
    shared_seat_ids: list[str] = Field(..., alias="sharedSeatIds")

    model_config = {'populate_by_name': True}


class MMPMetadata(BaseModel):
    """A structure to represent the metadata required for Mobile Measurement Partner (MMP) entities."""
    mmp_app_id: str = Field(..., alias="mmpAppId")
    name: Optional[str] = None

    model_config = {'populate_by_name': True}


class SharingRuleMetadata(BaseModel):
    """A union to capture application specific metadata. Going forward, this will include Events Manager metadata, AMC metadata etc.."""
    pass


class CreateSharingRuleRequestContent(BaseModel):
    """The input parameters to create a Sharing Rule."""
    account_entity_id: Optional[str] = Field(None, alias="accountEntityId", description="The account (e.g., DSP Advertiser Account) entityId. This is different from 'destinationEntityId'. This is also known as")
    application: "ApplicationId"
    data_set_id: str = Field(..., alias="dataSetId", description="Data set which is being shared via the sharing rule. The minimum length of the datasetId is 1 to ensure that it's not an")
    destination_account_id: str = Field(..., alias="destinationAccountId", description="Account to which data is shared.")
    marketplace_id: str = Field(..., alias="marketplaceId", description="Marketplace to which data is shared.")
    metadata: "SharingRuleMetadata"

    model_config = {'populate_by_name': True}


class Unit(BaseModel):
    pass


class SharingRuleResponseMetadata(BaseModel):
    """A union to capture application specific metadata that is exposed to API consumers. Eventually, this will involve other applications' metadata."""
    pass


class SharingRuleStatus(StrEnum):
    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    REVOKED_BY_DATASET = "REVOKED_BY_DATASET"
    REVOKED_BY_SHARING_GRANT = "REVOKED_BY_SHARING_GRANT"
    REVOKED_BY_USER = "REVOKED_BY_USER"
    SHADOW = "SHADOW"


class CreateSharingRuleResponseContent(BaseModel):
    """Output of a create sharing rule request, decoupled from sharing rule model."""
    account_entity_id: Optional[str] = Field(None, alias="accountEntityId", description="The account (e.g., DSP Advertiser Account) entityId. This is different from 'destinationEntityId'. This is also known as")
    activation_time: Optional[str] = Field(None, alias="activationTime", description="The timestamp when the sharing rule was activated.")
    application: "ApplicationId"
    creation_time: str = Field(..., alias="creationTime", description="Timestamp for time of creation in UTC.")
    data_set_id: str = Field(..., alias="dataSetId", description="Data set which is being shared via the sharing rule. The minimum length of the datasetId is 1 to ensure that it's not an")
    data_set_name: Optional[str] = Field(None, alias="dataSetName", description="The name of the DataSet part of this sharing rule.")
    destination_account_id: str = Field(..., alias="destinationAccountId", description="Account to which data is shared.")
    destination_entity_name: Optional[str] = Field(None, alias="destinationEntityName", description="The display name of the destination entity.")
    marketplace_id: str = Field(..., alias="marketplaceId", description="Marketplace to which data is shared.")
    metadata: Optional["SharingRuleResponseMetadata"] = None
    revoked_by: Optional[str] = Field(None, alias="revokedBy", description="The reason a rule was revoked, or NONE if rule is not revoked.")
    revoked_time: Optional[str] = Field(None, alias="revokedTime", description="The timestamp when the sharing rule was revoked.")
    sharing_rule_id: str = Field(..., alias="sharingRuleId", description="Unique ID for a sharing rule.")
    status: "SharingRuleStatus"

    model_config = {'populate_by_name': True}


class DataSetType(StrEnum):
    AUDIENCE = "AUDIENCE"
    CUSTOM = "CUSTOM"
    EVENT = "EVENT"
    GEO_LOCATIONS = "GEO_LOCATIONS"


class ExternalReferenceType(StrEnum):
    AMAZON_AD_TAG = "AMAZON_AD_TAG"
    CUSTOMER_PROVIDED = "CUSTOMER_PROVIDED"
    MMP = "MMP"


class DatasetUploadSourceType(StrEnum):
    API = "API"
    S3 = "S3"
    UI = "UI"


class DatasetMetadata(BaseModel):
    actions: list[str] = Field(..., description="The list of actions available for the dataset")
    active_destinations: float = Field(..., alias="activeDestinations", description="The active destinations for the dataset")
    country_code: str = Field(..., alias="countryCode", description="Default Country Code to fall back to for the records in this Dataset. Country Code should be represented in ISO 3166-1 a")
    created_at: str = Field(..., alias="createdAt", description="The timestamp when the dataset was created")
    dataset_id: str = Field(..., alias="datasetId", description="Id of a DataSet.")
    description: Optional[str] = Field(None, description="Description of the dataset")
    external_reference_id: Optional[str] = Field(None, alias="externalReferenceId", description="An internal Id generated from external source")
    external_reference_type: Optional["ExternalReferenceType"] = Field(None, alias="externalReferenceType")
    id_retention: Optional[bool] = Field(None, alias="idRetention", description="Determines retention of hashed data for 90 days and refresh of UID tokens.")
    last_modified: str = Field(..., alias="lastModified", description="The Date time the DataSet was last modified")
    last_modified_by: str = Field(..., alias="lastModifiedBy", description="Identifier of the user who most recently modified the DataSet.")
    metadata: Optional["Metadata"] = None
    name: str = Field(..., description="The name of the dataset")
    records: float = Field(..., description="The number of records in the dataset")
    schema: str = Field(..., description="The schema of the dataset")
    source: "DatasetUploadSourceType"
    ttl: Optional[float] = Field(None, description="Time-to-live in seconds. The amount of time the record is associated with the DataSet. Max is 12.5 months.")
    updated_at: str = Field(..., alias="updatedAt", description="The timestamp when the dataset was last updated")

    model_config = {'populate_by_name': True}


class DatasetMetric(StrEnum):
    CONSENTED = "CONSENTED"
    RECEIVED = "RECEIVED"
    RESOLVED = "RESOLVED"
    VALID = "VALID"


class DatasetMetricsValues(BaseModel):
    __root__: dict[str, float] = {}


class DatasetTimeSeries(BaseModel):
    """A time series of dataset metrics, keyed by timestamp"""
    __root__: dict[str, "DatasetMetricsValues"] = {}


class TargetIdentity(BaseModel):
    """The user identity to be deleted. Either an ExternalUserId or a collection of externalIdentities , maid or Hashed PII values representing a single user."""
    pass


class DeleteIdentityRequestContent(BaseModel):
    """The DeleteIdentityRequest represents a request to delete one or more user identities. It includes a list of target identities to be deleted, along with common headers."""
    target_identities: list["TargetIdentity"] = Field(..., alias="targetIdentities", description="A list of identities to be deleted from manager account id. Each identity is either a single supported ExternalUserId or")

    model_config = {'populate_by_name': True}


class GetDataSetMetricsResponseContent(BaseModel):
    accepted_count: float = Field(..., alias="acceptedCount", description="The number of accepted records in the dataset")
    client_name: Optional[str] = Field(None, alias="clientName", description="Identifier of the user who created the DataSet.")
    country_code: Optional["CountryCode"] = Field(None, alias="countryCode")
    created_by: Optional[str] = Field(None, alias="createdBy", description="Identifier of the user who created the DataSet.")
    data_set_id: str = Field(..., alias="dataSetId", description="The ID of the dataset")
    data_set_source: str = Field(..., alias="dataSetSource", description="The source of the dataset")
    data_set_type: "DataSetType" = Field(..., alias="dataSetType")
    date_created: str = Field(..., alias="dateCreated", description="The timestamp when the dataset was created")
    description: str = Field(..., description="The description of the dataset")
    external_reference_id: Optional[str] = Field(None, alias="externalReferenceId", description="An internal Id generated from external source")
    external_reference_type: Optional["ExternalReferenceType"] = Field(None, alias="externalReferenceType")
    id_retention: Optional[bool] = Field(None, alias="idRetention", description="Determines retention of hashed data for 90 days and refresh of UID tokens.")
    invalid_record_count: float = Field(..., alias="invalidRecordCount", description="The number of invalid records in the dataset")
    last_modified: str = Field(..., alias="lastModified", description="The timestamp when the dataset was last modified")
    last_modified_by: Optional[str] = Field(None, alias="lastModifiedBy", description="Identifier of the user who most recently modified the DataSet.")
    match_record_percentage: float = Field(..., alias="matchRecordPercentage", description="The percentage of records successfully matched in the dataset")
    metadata: Optional["Metadata"] = None
    name: str = Field(..., description="The name of the dataset")
    records_resolved: float = Field(..., alias="recordsResolved", description="The number of records successfully resolved in the dataset")
    records_with_identity: float = Field(..., alias="recordsWithIdentity", description="The number of records with identity information in the dataset")
    ttl: Optional[float] = Field(None, description="Time-to-live in seconds. The amount of time the record is associated with the DataSet. Max is 12.5 months.")
    upload_count: float = Field(..., alias="uploadCount", description="The total number of uploads for the dataset")

    model_config = {'populate_by_name': True}


class GetDataroomMetadataResponseContent(BaseModel):
    active_destinations: float = Field(..., alias="activeDestinations", description="The number of active destinations for the datasets")
    data_sets_in_use: float = Field(..., alias="dataSetsInUse", description="The number of datasets currently in use")
    linked_accounts: float = Field(..., alias="linkedAccounts", description="The number of linked accounts associated with the datasets")
    total_data_sets: float = Field(..., alias="totalDataSets", description="The total number of datasets")

    model_config = {'populate_by_name': True}


class GetDataroomResponseContent(BaseModel):
    account_id: str = Field(..., alias="accountId", description="The owner of this Data room")
    assigned_to_account_id: Optional[str] = Field(None, alias="assignedToAccountId", description="The Ads AccountId to which this dataroom is assigned to")
    creation_date_time: str = Field(..., alias="creationDateTime", description="An ISO UTC Timestamp value representing the time the dataroom was created")
    region: Optional["AwsRegion"] = None

    model_config = {'populate_by_name': True}


class GetDatasetAggregatesRequestContent(BaseModel):
    """List of Common Headers that could be added to any api with optional customerId and AdvertiserId"""
    end_date: Optional[str] = Field(None, alias="endDate", description="The end date for the metrics aggregation window, in UTC")
    metrics: Optional[list["DatasetMetric"]] = Field(None, description="The list of metrics to retrieve for the dataset")
    start_date: Optional[str] = Field(None, alias="startDate", description="The start date for the metrics aggregation window, in UTC")

    model_config = {'populate_by_name': True}


class GetDatasetAggregatesResponseContent(BaseModel):
    metrics: Optional["DatasetTimeSeries"] = None

    model_config = {'populate_by_name': True}


class IngestAudiencesRequestContent(BaseModel):
    """List of Common Headers that could be added to any api in Bifrost service"""
    members: list["AudienceMember"]

    model_config = {'populate_by_name': True}


class ValidationError(BaseModel):
    """Error Details for Each Member in the Ingest Request Payload."""
    code: Optional[str] = Field(None, description="HTTP status code of the error encountered.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")
    errors: Optional[list["DetailedError"]] = Field(None, description="List of detailed errors, if any.")
    index: Optional[float] = Field(None, description="Index of the Member in the Request Payload List.")

    model_config = {'populate_by_name': True}


class IngestAudiencesResponseContent(BaseModel):
    errors: Optional[list["ValidationError"]] = Field(None, description="List of Validation Errors in the AudienceMembers, which are rejected from the request.")
    ingress_id: Optional[str] = Field(None, alias="ingressId", description="Unique identifier for data ingestion flow generated at the server side when an events data are uploaded . When `POST` me")

    model_config = {'populate_by_name': True}


class ListDatasetDetailsRequestContent(BaseModel):
    """List of Common Headers that could be added to any api with optional customerId and AdvertiserId"""
    dataset_ids: Optional[list[str]] = Field(None, alias="datasetIds", description="A set of datasetIds to retrieve data for")

    model_config = {'populate_by_name': True}


class ListDatasetDetailsResponseContent(BaseModel):
    datasets: list["DatasetMetadata"] = Field(..., description="The list of dataset metadata objects")
    next_token: Optional[str] = Field(None, alias="nextToken", description="A token to retrieve the next page of results, if applicable")

    model_config = {'populate_by_name': True}


class ListSharingRulesRequestContent(BaseModel):
    """Fields for external ListSharingRules call, including filter expressions and common headers."""
    activated_after: Optional[str] = Field(None, alias="activatedAfter", description="The UTC date-time on or after which the sharing rule was activated.")
    activated_before: Optional[str] = Field(None, alias="activatedBefore", description="The UTC date-time on or before which the sharing rule was activated.")
    application: Optional["ApplicationId"] = None
    dataset_ids: Optional[list[str]] = Field(None, alias="datasetIds", description="The list of dataset ids to filter sharing rules by.")
    destination_account_id: Optional[str] = Field(None, alias="destinationAccountId", description="The account id to filter receiver of the sharing rule.")
    max_results: Optional[float] = Field(None, alias="maxResults", description="The maximum number of sharing rule results to return within one response.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="nextToken is used for pagination.")
    statuses: Optional[list["SharingRuleStatus"]] = Field(None, description="The list of statuses to filter sharing rules by. Exclusive filter if included, if not provided, all rules with any statu")

    model_config = {'populate_by_name': True}


class SharingRuleListItem(BaseModel):
    """Intermediate structure to allow use of SharingRule in SharingRuleList"""
    account_entity_id: Optional[str] = Field(None, alias="accountEntityId", description="The account (e.g., DSP Advertiser Account) entityId. This is different from 'destinationEntityId'. This is also known as")
    activation_time: Optional[str] = Field(None, alias="activationTime", description="The timestamp when the sharing rule was activated.")
    application: "ApplicationId"
    creation_time: str = Field(..., alias="creationTime", description="Timestamp for time of creation in UTC.")
    data_set_id: str = Field(..., alias="dataSetId", description="Data set which is being shared via the sharing rule. The minimum length of the datasetId is 1 to ensure that it's not an")
    data_set_name: Optional[str] = Field(None, alias="dataSetName", description="The name of the DataSet part of this sharing rule.")
    destination_account_id: str = Field(..., alias="destinationAccountId", description="Account to which data is shared.")
    destination_entity_name: Optional[str] = Field(None, alias="destinationEntityName", description="The display name of the destination entity.")
    marketplace_id: str = Field(..., alias="marketplaceId", description="Marketplace to which data is shared.")
    metadata: Optional["SharingRuleResponseMetadata"] = None
    revoked_by: Optional[str] = Field(None, alias="revokedBy", description="The reason a rule was revoked, or NONE if rule is not revoked.")
    revoked_time: Optional[str] = Field(None, alias="revokedTime", description="The timestamp when the sharing rule was revoked.")
    sharing_rule_id: str = Field(..., alias="sharingRuleId", description="Unique ID for a sharing rule.")
    status: "SharingRuleStatus"

    model_config = {'populate_by_name': True}


class ListSharingRulesResponseContent(BaseModel):
    """The response consisting of a list of sharing rules."""
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to get next page in a paginated response.")
    sharing_rules: Optional[list["SharingRuleListItem"]] = Field(None, alias="sharingRules", description="The list of sharing rules matching the input request.")

    model_config = {'populate_by_name': True}

