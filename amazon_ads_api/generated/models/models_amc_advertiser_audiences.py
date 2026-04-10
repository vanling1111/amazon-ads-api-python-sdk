"""Auto-generated Pydantic models. Do not edit manually.

Source: Advertiseraudiences_prod_3p.json
Title:  Advertiser audiences
"""

from __future__ import annotations

from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field



class AmcpLinkAddConnectionV2RequestContent(BaseModel):
    """Add Connection request."""
    amc_account_id: Optional[str] = Field(None, alias="amcAccountId", description="AMC Account identifier to connect.")
    amc_account_marketplace_id: Optional[str] = Field(None, alias="amcAccountMarketplaceId", description="Connected AMC Account Marketplace identifier.")
    amc_instance_id: Optional[str] = Field(None, alias="amcInstanceId", description="AMC Instance identifier to connect.")
    connection_id: Optional[str] = Field(None, alias="connectionId", description="An unique identifier for the connection. This will be auto-generated if not provided in the request.")
    dsp_advertiser_id: Optional[str] = Field(None, alias="dspAdvertiserId", description="DSP Advertiser identifier to connect.")
    dsp_profile_id: Optional[str] = Field(None, alias="dspProfileId", description="DSP Profile identifier.")
    is_default: Optional[bool] = Field(None, alias="isDefault", description="Flag indicating if this is the Default Connection for this Customer who is creating the Connection. The system will ensu")

    model_config = {'populate_by_name': True}


class AmcpLinkAddConnectionV2ResponseContent(BaseModel):
    """Add Connection response."""
    connection_id: Optional[str] = Field(None, alias="connectionId", description="Identifier of the connection that was created.")

    model_config = {'populate_by_name': True}


class AmcpLinkBadRequestExceptionResponseContent(BaseModel):
    """Bad Request."""
    message: Optional[str] = Field(None, description="Error message.")
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class AmcpLinkConnection(BaseModel):
    """Partner Connection Detail."""
    amc_account_id: Optional[str] = Field(None, alias="amcAccountId", description="Connected AMC Account identifier.")
    amc_account_marketplace_id: Optional[str] = Field(None, alias="amcAccountMarketplaceId", description="Connected AMC Account Marketplace identifier.")
    amc_account_name: Optional[str] = Field(None, alias="amcAccountName", description="Connected AMC Account Name.")
    amc_instance_id: Optional[str] = Field(None, alias="amcInstanceId", description="Connected AMC Instance identifier.")
    amc_instance_name: Optional[str] = Field(None, alias="amcInstanceName", description="Connected AMC Instance Name.")
    client_id: Optional[str] = Field(None, alias="clientId", description="The identifier of a client associated with a 'Login with Amazon' account.")
    connection_id: Optional[str] = Field(None, alias="connectionId", description="Unique identifier of the connection.")
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="Timestamp for record creation.")
    customer_id: Optional[str] = Field(None, alias="customerId", description="Id of the Customer.")
    data_upload_aws_account_id: Optional[str] = Field(None, alias="dataUploadAwsAccountId", description="DataUploadAwsId Associated with the connectionId")
    dsp_advertiser_country_code: Optional[str] = Field(None, alias="dspAdvertiserCountryCode", description="Connected DSP Advertiser Country Code.")
    dsp_advertiser_id: Optional[str] = Field(None, alias="dspAdvertiserId", description="Connected DSP Advertiser identifier.")
    dsp_advertiser_marketplace_id: Optional[str] = Field(None, alias="dspAdvertiserMarketplaceId", description="Connected DSP Advertiser MarketplaceId.")
    dsp_advertiser_name: Optional[str] = Field(None, alias="dspAdvertiserName", description="Connected DSP Advertiser Name.")
    dsp_advertiser_region: Optional[str] = Field(None, alias="dspAdvertiserRegion", description="Connected DSP Advertiser Retail Region.")
    dsp_profile_id: Optional[str] = Field(None, alias="dspProfileId", description="DSP Advertiser identifier.")
    is_default: Optional[bool] = Field(None, alias="isDefault", description="Is Default Connection.")
    modified_date_time: Optional[str] = Field(None, alias="modifiedDateTime", description="Timestamp for record modification.")

    model_config = {'populate_by_name': True}


class AmcpLinkForbiddenRequestExceptionResponseContent(BaseModel):
    """Forbidden. The request failed because the user does not have access to the specified resource."""
    message: Optional[str] = Field(None, description="Error message.")
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class AmcpLinkGetConnectionsV2ResponseContent(BaseModel):
    """List of Partner Connections with an Advertiser's AMC Instances and DSP Advertisers."""
    connections: Optional[list["AmcpLinkConnection"]] = Field(None, description="List of Partner Connection.")

    model_config = {'populate_by_name': True}


class AmcpLinkGetTermsV2ResponseContent(BaseModel):
    """Get Terms response."""
    agreement_content: Optional[str] = Field(None, alias="agreementContent", description="The terms and conditions agreement content.")
    agreement_token: Optional[str] = Field(None, alias="agreementToken", description="The terms and conditions agreement token. Required to accept an agreement.")
    has_accepted: Optional[bool] = Field(None, alias="hasAccepted", description="Flag indicating whether the Customer has accepted the AMC Terms and Conditions.")

    model_config = {'populate_by_name': True}


class AmcpLinkResourceNotFoundExceptionResponseContent(BaseModel):
    """Not Found. The requested resource does not exist or is not visible for the user."""
    message: Optional[str] = Field(None, description="Error message.")
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class AmcpLinkServerExceptionResponseContent(BaseModel):
    """Internal server error. Retry later. Contact support if this response persists."""
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class AmcpLinkSetTermsAcceptanceV2RequestContent(BaseModel):
    """Set Terms Acceptance request."""
    agreement_token: str = Field(..., alias="agreementToken", description="The terms and conditions agreement token.")
    has_accepted: bool = Field(..., alias="hasAccepted", description="Flag indicating whether the Customer has accepted the AMC Terms and Conditions. Submitting true will set the customer as")

    model_config = {'populate_by_name': True}


class AmcpLinkTooManyRequestsExceptionResponseContent(BaseModel):
    """Too Many Requests. The request was rate-limited. Retry later."""
    message: Optional[str] = Field(None, description="Error message.")
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class AmcpLinkUnauthorizedRequestExceptionResponseContent(BaseModel):
    """Unauthorized. The request failed because the user is not authenticated or is not allowed to invoke the operation."""
    message: Optional[str] = Field(None, description="Error message.")
    request_id: Optional[str] = Field(None, alias="requestId")

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


class currency(StrEnum):
    AED = "AED"
    AUD = "AUD"
    CAD = "CAD"
    CNY = "CNY"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"
    JPY = "JPY"
    MXN = "MXN"
    SAR = "SAR"
    SEK = "SEK"
    TRY = "TRY"
    USD = "USD"


class AudienceFee(BaseModel):
    cpm_cents: float = Field(..., alias="cpmCents", description="Cost per thousand impressions (CPM) in cents. For example, $1.00 = 100 cents.")
    currency: "currency"

    model_config = {'populate_by_name': True}


class AudienceMetadata(BaseModel):
    audience_fees: Optional[list["AudienceFee"]] = Field(None, alias="audienceFees", description="A list of currency keys and costs per impressions (CPM)")
    external_audience_id: str = Field(..., alias="externalAudienceId", description="The user-defined audience identifier.")
    ttl: Optional[float] = Field(None, description="Time-to-live in seconds. The amount of time the record is associated with the audience.")

    model_config = {'populate_by_name': True}


class AudienceMetadataUpdate(BaseModel):
    audience_fees: Optional[list["AudienceFee"]] = Field(None, alias="audienceFees", description="A list of currency keys and costs per impressions (CPM)")
    ttl: Optional[float] = Field(None, description="Time-to-live in seconds. The amount of time the record is associated with the audience.")

    model_config = {'populate_by_name': True}


class AudienceSize(BaseModel):
    dsp_audience_size: Optional[float] = Field(None, alias="dspAudienceSize", description="The count of records in DSP audience.")
    id_resolution_count: Optional[float] = Field(None, alias="idResolutionCount", description="The number of matched records during id resolution.")
    received_record_size: Optional[float] = Field(None, alias="receivedRecordSize", description="The number of records received by ADSP.")

    model_config = {'populate_by_name': True}


class AudienceMetadataWithAudienceSize(BaseModel):
    audience_fees: Optional[list["AudienceFee"]] = Field(None, alias="audienceFees", description="A list of currency keys and costs per impressions (CPM)")
    audience_size: Optional["AudienceSize"] = Field(None, alias="audienceSize")
    external_audience_id: str = Field(..., alias="externalAudienceId", description="The user-defined audience identifier.")
    ttl: Optional[float] = Field(None, description="Time-to-live in seconds. The amount of time the record is associated with the audience.")

    model_config = {'populate_by_name': True}


class Consent(BaseModel):
    amzn: Optional["AmznConsent"] = None
    gpp: Optional[str] = Field(None, description="A field to hold a 'Global Privacy Platform (GPP)' string. Optional.")
    tcf: Optional[str] = Field(None, description="A field to hold the 'Transparency and Consent Framework (TCF)' string. Optional.")

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


class TargetResourceMetadata(BaseModel):
    """The identifier of the target resource. It can either be a connectionId or advertiserId."""
    pass


class CreateAudienceMetadataV2RequestContent(BaseModel):
    country_code: Optional["CountryCode"] = Field(None, alias="countryCode")
    description: str = Field(..., description="The audience description. Must be an alphanumeric, non-null string between 0 to 1000 characters in length.")
    metadata: "AudienceMetadata"
    name: str = Field(..., description="The audience name. Must be an alphanumeric string between 10 to 128 characters in length.")
    target_resource: "TargetResourceMetadata" = Field(..., alias="targetResource")

    model_config = {'populate_by_name': True}


class CreateAudienceMetadataV2ResponseContent(BaseModel):
    audience_id: Optional[float] = Field(None, alias="audienceId", description="A number value representing the Amazon audience identifier. This is the identifier that is returned during audience crea")
    external_audience_id: Optional[str] = Field(None, alias="externalAudienceId", description="The user-defined audience identifier.")

    model_config = {'populate_by_name': True}


class DataCollaborationClientFaultExceptionResponseContent(BaseModel):
    """Bad Request."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class DataCollaborationClientThrottlingExceptionResponseContent(BaseModel):
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class DataCollaborationInternalServerFaultExceptionResponseContent(BaseModel):
    """Internal server error."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class DataCollaborationJobNotFoundExceptionResponseContent(BaseModel):
    """The requested job was not found."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class DataCollaborationNotImplementedServerExceptionResponseContent(BaseModel):
    """Not implemented server exception."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class Geo(BaseModel):
    country_code: Optional["CountryCode"] = Field(None, alias="countryCode")
    ip_address: Optional[str] = Field(None, alias="ipAddress", description="A String value holding an ipAddress used to determine country for members in this audience. Optional.")

    model_config = {'populate_by_name': True}


class GetAudienceMetadataV2ResponseContent(BaseModel):
    advertiser_id: Optional[float] = Field(None, alias="advertiserId", description="An identifier for a targeted resource.")
    audience_id: Optional[float] = Field(None, alias="audienceId", description="A number value representing the Amazon audience identifier. This is the identifier that is returned during audience crea")
    country_code: Optional[str] = Field(None, alias="countryCode", description="A String value representing ISO 3166-1 alpha-2 country code for the members in this audience. Optional.")
    description: Optional[str] = Field(None, description="The audience description. Must be an alphanumeric, non-null string between 0 to 1000 characters in length.")
    metadata: Optional["AudienceMetadataWithAudienceSize"] = None
    name: Optional[str] = Field(None, description="The audience name. Must be an alphanumeric string between 10 to 128 characters in length.")

    model_config = {'populate_by_name': True}


class HashedPIIObj(BaseModel):
    address: Optional[str] = None
    city: Optional[str] = None
    email: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    phone: Optional[str] = None
    postal: Optional[str] = None
    state: Optional[str] = None

    model_config = {'populate_by_name': True}


class ManageAudienceStatusResponseErrorItem(BaseModel):
    audience_id: Optional[str] = Field(None, alias="audienceId", description="An integer value representing the Amazon audience identifier. This is the identifier that is returned during audience cr")
    error: Optional[str] = Field(None, description="Error message describing what happened")
    external_id: Optional[str] = Field(None, alias="externalId", description="The user-defined audience identifier.")

    model_config = {'populate_by_name': True}


class ManageAudienceStatusResponseSuccessSet(BaseModel):
    records_processed_rate: Optional[float] = Field(None, alias="recordsProcessedRate", description="Percent of records submitted that were successfully processed without errors.")

    model_config = {'populate_by_name': True}


class jobState(StrEnum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PARTIALLYSUCCEEDED = "PARTIALLYSUCCEEDED"
    PENDING = "PENDING"
    SUCCEEDED = "SUCCEEDED"


class ManageAudienceStatusV2ResponseContent(BaseModel):
    audience_size: Optional["AudienceSize"] = Field(None, alias="audienceSize")
    invalid_records: Optional[list["ManageAudienceStatusResponseErrorItem"]] = Field(None, alias="invalidRecords")
    job_request_id: Optional[str] = Field(None, alias="jobRequestId")
    job_state: Optional["jobState"] = Field(None, alias="jobState")
    successful: Optional["ManageAudienceStatusResponseSuccessSet"] = None

    model_config = {'populate_by_name': True}


class action(StrEnum):
    CREATE = "CREATE"
    DELETE = "DELETE"


class UserConsent(BaseModel):
    consent: Optional["Consent"] = None
    geo: Optional["Geo"] = None

    model_config = {'populate_by_name': True}


class MeasurementObj(BaseModel):
    pass


class PayloadObj(BaseModel):
    action: "action"
    country_code: Optional[str] = Field(None, alias="countryCode", description="A String value representing ISO 3166-1 alpha-2 country code for the members in this audience. Optional.")
    external_user_id: str = Field(..., alias="externalUserId", description="This is an external user identifier defined by data providers.")
    hashed_pii: list["HashedPIIObj"] = Field(..., alias="hashedPII", description="List of hashed personally-identifiable information records to be matched with Amazon identities for future use. All inpu")
    measurements: Optional["MeasurementObj"] = None
    user_consent: Optional["UserConsent"] = Field(None, alias="userConsent")

    model_config = {'populate_by_name': True}


class targetType(StrEnum):
    DSP = "DSP"


class TargetResourceRecords(BaseModel):
    """Record upload information"""
    connection_id: str = Field(..., alias="connectionId", description="Connection between Partner and Advertiser. If blank or not provided then the default active connection is used.")
    target_types: Optional[list["targetType"]] = Field(None, alias="targetTypes", description="List of included upload paths.  AMC is always included in this by default")

    model_config = {'populate_by_name': True}


class ManageAudienceV2RequestContent(BaseModel):
    audience_id: float = Field(..., alias="audienceId", description="An number value representing the Amazon audience identifier. This is the identifier that is returned during audience cre")
    records: list["PayloadObj"]
    target_resource: Optional["TargetResourceRecords"] = Field(None, alias="targetResource")

    model_config = {'populate_by_name': True}


class ManageAudienceV2ResponseContent(BaseModel):
    job_request_id: Optional[str] = Field(None, alias="jobRequestId", description="Unique identifier for job request generated at the server side when an audience records are uploaded . When `POST` metho")

    model_config = {'populate_by_name': True}


class UpdateAudienceMetadataV2RequestContent(BaseModel):
    description: Optional[str] = Field(None, description="The audience description. Must be an alphanumeric, non-null string between 0 to 1000 characters in length.")
    metadata: Optional["AudienceMetadataUpdate"] = None

    model_config = {'populate_by_name': True}


class UpdateAudienceMetadataV2ResponseContent(BaseModel):
    advertiser_id: Optional[float] = Field(None, alias="advertiserId", description="An identifier for a targeted resource.")
    audience_id: Optional[float] = Field(None, alias="audienceId", description="A number value representing the Amazon audience identifier. This is the identifier that is returned during audience crea")
    description: Optional[str] = Field(None, description="The audience description. Must be an alphanumeric, non-null string between 0 to 1000 characters in length.")
    metadata: Optional["AudienceMetadata"] = None
    name: Optional[str] = Field(None, description="The audience name. Must be an alphanumeric string between 10 to 128 characters in length.")

    model_config = {'populate_by_name': True}

