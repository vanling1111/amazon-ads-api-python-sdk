"""Auto-generated Pydantic models. Do not edit manually.

Source: AdvertisingBilling_prod_3p.json
Title:  Advertising Billing
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class AdPayInvoicesMode(StrEnum):
    EXECUTE = "EXECUTE"
    PREVIEW = "PREVIEW"


class AdPaymentsPaymentMethodType(StrEnum):
    CREDIT_CARD = "CREDIT_CARD"
    DEDUCT_FOR_PAYMENT = "DEDUCT_FOR_PAYMENT"
    DIRECT_DEBIT = "DIRECT_DEBIT"
    PAY_BY_INVOICE = "PAY_BY_INVOICE"
    SELLER_PAYABLE = "SELLER_PAYABLE"


class AdPaymentsBackupMethodsConfiguration(BaseModel):
    """Describes backup method configuration for a payment method type."""
    types: Optional[list["AdPaymentsPaymentMethodType"]] = Field(None, description="List of eligible backup payment method types.")

    model_config = {'populate_by_name': True}


class AdPaymentsBulkCreationResult(BaseModel):
    id_: str = Field(..., alias="id", description="The identifier of the resource that this result is referencing.")
    index: int = Field(..., description="The index of the item in the input list.")
    reason: Optional[str] = Field(None, description="A human readable reason giving more details regarding this result.")

    model_config = {'populate_by_name': True}


class AdPaymentsCountryCode(StrEnum):
    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    CL = "CL"
    CO = "CO"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NG = "NG"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    UK = "UK"
    US = "US"
    ZA = "ZA"


class AdPaymentsCountryCodeList(BaseModel):
    """A list of country codes."""
    pass


class AdPaymentsPaymentAgreementType(StrEnum):
    AUTO_PAY = "AUTO_PAY"
    PAY_NOW = "PAY_NOW"


class AdPaymentsEntityType(StrEnum):
    AGENCY = "AGENCY"
    DSP_ADVERTISING_ACCOUNT = "DSP_ADVERTISING_ACCOUNT"
    GLOBAL_ACCOUNT = "GLOBAL_ACCOUNT"
    MANAGER_ACCOUNT = "MANAGER_ACCOUNT"
    SELLER = "SELLER"
    VENDOR = "VENDOR"


class AdPaymentsTarget(BaseModel):
    agreement_type: "AdPaymentsPaymentAgreementType" = Field(..., alias="agreementType")
    country_code: "AdPaymentsCountryCode" = Field(..., alias="countryCode")
    entity_id: Optional[str] = Field(None, alias="entityId", description="The ID associated to the entity in this target.")
    entity_type: Optional["AdPaymentsEntityType"] = Field(None, alias="entityType")

    model_config = {'populate_by_name': True}


class AdPaymentsEntityMarketplace(BaseModel):
    """Represents an advertiser and marketplace combination."""
    country_code: Optional["AdPaymentsCountryCode"] = Field(None, alias="countryCode")
    entity_id: str = Field(..., alias="entityId", description="The identifier of the entity.")
    entity_type: "AdPaymentsEntityType" = Field(..., alias="entityType")

    model_config = {'populate_by_name': True}


class AdPaymentsEntityMarketplaceList(BaseModel):
    """A list of uniquely identifiable advertising entities."""
    pass


class CurrencyConversionConsentStatus(StrEnum):
    NOT_SELECTED = "NOT_SELECTED"
    OPTED_IN = "OPTED_IN"
    OPTED_OUT = "OPTED_OUT"


class AdPaymentsForeignExchange(BaseModel):
    """Foreign exchange information on credit card."""
    currency_conversion_consent_status: Optional["CurrencyConversionConsentStatus"] = Field(None, alias="currencyConversionConsentStatus")
    fee_percentage: Optional[float] = Field(None, alias="feePercentage", description="Percentage fee amazon is taking in transaction.")
    rate: Optional[float] = Field(None, description="Rate used for currency conversion.")
    target_currency_code: Optional[str] = Field(None, alias="targetCurrencyCode", description="Currency the customer is paying in (credit card currency).")

    model_config = {'populate_by_name': True}


class AdPaymentsExpiryDetails(BaseModel):
    """Indicates the month a payment method will expire."""
    month: int = Field(..., description="The month the payment method will expire.")
    year: int = Field(..., description="The year the payment method will expire.")

    model_config = {'populate_by_name': True}


class AdPaymentsCurrencyCode(StrEnum):
    AED = "AED"
    AUD = "AUD"
    BGN = "BGN"
    BRL = "BRL"
    CAD = "CAD"
    CHF = "CHF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    CZK = "CZK"
    DKK = "DKK"
    EGP = "EGP"
    EUR = "EUR"
    GBP = "GBP"
    HKD = "HKD"
    HUF = "HUF"
    ILS = "ILS"
    INR = "INR"
    JPY = "JPY"
    KRW = "KRW"
    MXN = "MXN"
    NGN = "NGN"
    NZD = "NZD"
    PLN = "PLN"
    RON = "RON"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    TRY = "TRY"
    TWD = "TWD"
    USD = "USD"
    VND = "VND"
    ZAR = "ZAR"


class AdPaymentsCurrencyAmount(BaseModel):
    amount: float = Field(..., description="A monetary amount.")
    currency_code: "AdPaymentsCurrencyCode" = Field(..., alias="currencyCode")

    model_config = {'populate_by_name': True}


class AdPaymentsPaymentMethod(BaseModel):
    """Represents a payment method."""
    brand: Optional[str] = Field(None, description="The processor used to execute payments on the card, such as Visa, MasterCard, etc. Only valued for credit card payment m")
    country_code: Optional["AdPaymentsCountryCode"] = Field(None, alias="countryCode")
    expiry_details: Optional["AdPaymentsExpiryDetails"] = Field(None, alias="expiryDetails")
    foreign_exchange: Optional["AdPaymentsForeignExchange"] = Field(None, alias="foreignExchange")
    instrument_id: Optional[str] = Field(None, alias="instrumentId", description="Identifies a credit card or direct debit payment method.")
    priority: int = Field(..., description="A numerical priority assigned to each payment method within a given profile, dictating the sequential order in which the")
    seller_account_id: Optional[str] = Field(None, alias="sellerAccountId", description="The seller account ID associated to this payment method, only valued for seller payable payment methods.")
    tail: Optional[str] = Field(None, description="The last four digits of a credit card or bank account number.")
    type_: "AdPaymentsPaymentMethodType" = Field(..., alias="type")
    vendor_code: Optional[str] = Field(None, alias="vendorCode", description="The vendor code associated to this payment method, only valued for deduct from payment payment methods.")
    vendor_code_balance: Optional["AdPaymentsCurrencyAmount"] = Field(None, alias="vendorCodeBalance")
    vendor_code_name: Optional[str] = Field(None, alias="vendorCodeName", description="The name of the vendor code this payment method represents.")

    model_config = {'populate_by_name': True}


class AdPaymentsPaymentMethodList(BaseModel):
    pass


class AdPaymentsPaymentProfile(BaseModel):
    """Represents a list of payment methods and the scope of advertisers able to access them."""
    default_for: Optional["AdPaymentsEntityMarketplaceList"] = Field(None, alias="defaultFor")
    eligible_entities: Optional["AdPaymentsEntityMarketplaceList"] = Field(None, alias="eligibleEntities")
    payment_methods: Optional["AdPaymentsPaymentMethodList"] = Field(None, alias="paymentMethods")
    payment_profile_id: Optional[str] = Field(None, alias="paymentProfileId", description="The ID associated to this payment profile.")

    model_config = {'populate_by_name': True}


class AdPaymentsPaymentAgreement(BaseModel):
    """Represents an agreement between two parties indicating what profile to use during payment execution."""
    payment_agreement_id: Optional[str] = Field(None, alias="paymentAgreementId", description="The ID associated to this payment agreement.")
    payment_profile: "AdPaymentsPaymentProfile" = Field(..., alias="paymentProfile")
    target: "AdPaymentsTarget"

    model_config = {'populate_by_name': True}


class AdPaymentsPaymentAgreementList(BaseModel):
    pass


class AdPaymentsCreatePaymentAgreementsInput(BaseModel):
    """Represents the input of the create payment agreement API."""
    payment_agreements: "AdPaymentsPaymentAgreementList" = Field(..., alias="paymentAgreements")

    model_config = {'populate_by_name': True}


class AdPaymentsCreatePaymentAgreementsOutput(BaseModel):
    """Represent the output of the create payment agreement API."""
    error: list["AdPaymentsBulkCreationResult"]
    success: list["AdPaymentsBulkCreationResult"]

    model_config = {'populate_by_name': True}


class AdPaymentsPaymentProfileList(BaseModel):
    pass


class AdPaymentsCreatePaymentProfileInput(BaseModel):
    """Represents the input of the create payment profiles API."""
    payment_profiles: "AdPaymentsPaymentProfileList" = Field(..., alias="paymentProfiles")

    model_config = {'populate_by_name': True}


class AdPaymentsCreatePaymentProfilesOutput(BaseModel):
    """Represent the output of the create payment profiles API."""
    error: list["AdPaymentsBulkCreationResult"]
    success: list["AdPaymentsBulkCreationResult"]

    model_config = {'populate_by_name': True}


class AdPaymentsCreditCardPaymentMethod(BaseModel):
    """Represents Credit Card payment method structure."""
    brand: str = Field(..., description="The processor used to execute payments on the card, such as Visa, MasterCard, etc. Only valued for credit card payment m")
    eligible_countries: "AdPaymentsCountryCodeList" = Field(..., alias="eligibleCountries")
    expiry_details: "AdPaymentsExpiryDetails" = Field(..., alias="expiryDetails")
    foreign_exchange: Optional["AdPaymentsForeignExchange"] = Field(None, alias="foreignExchange")
    instrument_id: str = Field(..., alias="instrumentId", description="Identifies a credit card payment method.")
    tail: str = Field(..., description="The last four digits of the credit card number.")
    type_: "AdPaymentsPaymentMethodType" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class AdPaymentsCreditCardPaymentMethodList(BaseModel):
    """A list of credit card payment methods."""
    pass


class AdPaymentsDeductFromPaymentPaymentMethod(BaseModel):
    """Represents DeductFromPayment payment method structure. DeductFromPayment is a type of payment method where spends are deducted from vendor balance of a particular vendor code."""
    country_code: Optional["AdPaymentsCountryCode"] = Field(None, alias="countryCode")
    eligible_countries: "AdPaymentsCountryCodeList" = Field(..., alias="eligibleCountries")
    type_: "AdPaymentsPaymentMethodType" = Field(..., alias="type")
    vendor_code: str = Field(..., alias="vendorCode", description="A vendor code identifies a product being sold by a vendor on the retail website. When Amazon purchases products from a v")
    vendor_code_balance: Optional["AdPaymentsCurrencyAmount"] = Field(None, alias="vendorCodeBalance")
    vendor_code_name: str = Field(..., alias="vendorCodeName", description="The name of the vendor code this payment method represents.")
    vendor_group_id: Optional[str] = Field(None, alias="vendorGroupId", description="The identifier of the vendor group that this vendor code belongs to.")

    model_config = {'populate_by_name': True}


class AdPaymentsDeductFromPaymentPaymentMethodList(BaseModel):
    """A list of deduct from payment payment methods."""
    pass


class AdPaymentsDirectDebitPaymentMethod(BaseModel):
    """Represents Direct Debit payment method structure."""
    eligible_countries: "AdPaymentsCountryCodeList" = Field(..., alias="eligibleCountries")
    instrument_id: str = Field(..., alias="instrumentId", description="Identifies a direct debit payment method.")
    tail: str = Field(..., description="The last four digits of the bank account number.")
    type_: "AdPaymentsPaymentMethodType" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class AdPaymentsDirectDebitPaymentMethodList(BaseModel):
    """A list of direct debit payment methods."""
    pass


class AdPaymentsError(BaseModel):
    code: str
    details: str

    model_config = {'populate_by_name': True}


class AdPaymentsPayByInvoicePaymentMethod(BaseModel):
    """Represents Pay By Invoice payment method structure. Pay By Invoice is a type of payment method where the customer receives a physical invoice which they can pay via bank transfer."""
    eligible_countries: "AdPaymentsCountryCodeList" = Field(..., alias="eligibleCountries")
    type_: "AdPaymentsPaymentMethodType" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class AdPaymentsPayByInvoicePaymentMethodList(BaseModel):
    """A list of pay by invoice payment methods."""
    pass


class AdPaymentsPaymentMethodConfiguration(BaseModel):
    """Configuration for a primary payment method and its backup options."""
    backup_methods: Optional["AdPaymentsBackupMethodsConfiguration"] = Field(None, alias="backupMethods")
    primary_method: "AdPaymentsPaymentMethodType" = Field(..., alias="primaryMethod")

    model_config = {'populate_by_name': True}


class AdPaymentsPaymentMethodConfigurationList(BaseModel):
    """A list of payment method configurations."""
    pass


class AdPaymentsSellerPayablePaymentMethod(BaseModel):
    """Represents Seller Payable payment method structure. Seller Payable is a type of payment method where spends are deducted from the seller balance of a particular seller account."""
    country_code: Optional["AdPaymentsCountryCode"] = Field(None, alias="countryCode")
    eligible_countries: "AdPaymentsCountryCodeList" = Field(..., alias="eligibleCountries")
    seller_account_id: Optional[str] = Field(None, alias="sellerAccountId", description="The seller account ID associated to this payment method")
    type_: "AdPaymentsPaymentMethodType" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class AdPaymentsSellerPayablePaymentMethodList(BaseModel):
    """A list of seller payable payment methods."""
    pass


class AdPaymentsNextToken(BaseModel):
    """To retrieve the next page of results, call the same operation and specify this token in the request. If the nextToken field is empty, there are no further results."""
    pass


class AdPaymentsGetCustomerPaymentMethodsOutput(BaseModel):
    """Represents the output of the get payment methods API."""
    credit_card_payment_methods: Optional["AdPaymentsCreditCardPaymentMethodList"] = Field(None, alias="creditCardPaymentMethods")
    deduct_from_payment_payment_methods: Optional["AdPaymentsDeductFromPaymentPaymentMethodList"] = Field(None, alias="deductFromPaymentPaymentMethods")
    direct_debit_payment_methods: Optional["AdPaymentsDirectDebitPaymentMethodList"] = Field(None, alias="directDebitPaymentMethods")
    next_token: Optional["AdPaymentsNextToken"] = Field(None, alias="nextToken")
    pay_by_invoice_payment_methods: Optional["AdPaymentsPayByInvoicePaymentMethodList"] = Field(None, alias="payByInvoicePaymentMethods")
    payment_method_configurations: Optional["AdPaymentsPaymentMethodConfigurationList"] = Field(None, alias="paymentMethodConfigurations")
    seller_payable_payment_methods: Optional["AdPaymentsSellerPayablePaymentMethodList"] = Field(None, alias="sellerPayablePaymentMethods")

    model_config = {'populate_by_name': True}


class AdPaymentsGetPaymentAgreementOutput(BaseModel):
    """Represent the output of the get payment agreements API."""
    next_token: Optional["AdPaymentsNextToken"] = Field(None, alias="nextToken")
    payment_agreements: "AdPaymentsPaymentAgreementList" = Field(..., alias="paymentAgreements")

    model_config = {'populate_by_name': True}


class AdPaymentsIdempotenceId(BaseModel):
    """Idempotency Id that will be used as a identifier to ensure idempotency while creating /updating the given resource. Requests with same idempotency Id will be considered identical and processed in an i"""
    pass


class AdPaymentsLocale(StrEnum):
    AR_AE = "ar_AE"
    DE_DE = "de_DE"
    EN_AU = "en_AU"
    EN_CA = "en_CA"
    EN_GB = "en_GB"
    EN_IN = "en_IN"
    EN_SG = "en_SG"
    EN_US = "en_US"
    ES_CO = "es_CO"
    ES_ES = "es_ES"
    ES_MX = "es_MX"
    ES_US = "es_US"
    FR_CA = "fr_CA"
    FR_FR = "fr_FR"
    HI_IN = "hi_IN"
    IT_IT = "it_IT"
    JA_JP = "ja_JP"
    KO_KR = "ko_KR"
    NL_NL = "nl_NL"
    PL_PL = "pl_PL"
    PT_BR = "pt_BR"
    SV_SE = "sv_SE"
    TA_IN = "ta_IN"
    TH_TH = "th_TH"
    TR_TR = "tr_TR"
    VI_VN = "vi_VN"
    ZH_CN = "zh_CN"
    ZH_TW = "zh_TW"


class AdPaymentsPaymentAgreementId(BaseModel):
    """ID of a payment agreement that must belong to the customer. A one-time payment will be collected using the payment agreement's associated payment profile. If not provided, the latest payment agreement"""
    pass


class AdPaymentsPayInvoicesInput(BaseModel):
    """Represents the input to the pay invoices API."""
    idempotence_id: "AdPaymentsIdempotenceId" = Field(..., alias="idempotenceId")
    mode: Optional["AdPayInvoicesMode"] = None
    payment_agreement_id: Optional["AdPaymentsPaymentAgreementId"] = Field(None, alias="paymentAgreementId")
    reason_locale: Optional["AdPaymentsLocale"] = Field(None, alias="reasonLocale")

    model_config = {'populate_by_name': True}


class AdPaymentsPaymentResult(BaseModel):
    """Represents the result of a payment execution."""
    foreign_exchange: Optional["AdPaymentsForeignExchange"] = Field(None, alias="foreignExchange")
    invoice_cfid: str = Field(..., alias="invoiceCFID", description="The customer facing ID of the invoice.")
    payment_amount: Optional["AdPaymentsCurrencyAmount"] = Field(None, alias="paymentAmount")
    reason: Optional[str] = Field(None, description="A human-readable reason explaining the payment result.")

    model_config = {'populate_by_name': True}


class AdPaymentsPaymentResultList(BaseModel):
    pass


class AdPaymentsPayInvoicesOutput(BaseModel):
    """Represents the output of the pay invoices API."""
    failure: "AdPaymentsPaymentResultList"
    success: "AdPaymentsPaymentResultList"

    model_config = {'populate_by_name': True}


class CountryCode(StrEnum):
    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    CL = "CL"
    CO = "CO"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    IE = "IE"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NG = "NG"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    UK = "UK"
    US = "US"
    ZA = "ZA"


class MarketplaceAdvertiser(BaseModel):
    """Represents one country inside a global account"""
    country_code: "CountryCode" = Field(..., alias="countryCode")

    model_config = {'populate_by_name': True}


class ApplyBillingProfileRequestBillingprofileusages(BaseModel):
    advertiser: "MarketplaceAdvertiser"
    billing_profile_ids: list[str] = Field(..., alias="billingProfileIds", description="List of billing profile identifiers which needs to be associated with an advertiser.")

    model_config = {'populate_by_name': True}


class ApplyBillingProfileRequest(BaseModel):
    """Request with a list of advertisers to which a list of billing profiles needs to be applied."""
    billing_profile_usages: list["ApplyBillingProfileRequestBillingprofileusages"] = Field(..., alias="billingProfileUsages", description="List of advertisers to which a list of billing profiles needs to be applied.")

    model_config = {'populate_by_name': True}


class ErrorResponse(BaseModel):
    """Contains the machine-readable error code and human-readable details."""
    error_code: Optional[str] = Field(None, alias="errorCode", description="The code describing the error reason.")
    error_message: Optional[str] = Field(None, alias="errorMessage", description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class ApplyBillingProfileResponseBillingprofileusagesError(BaseModel):
    advertiser: Optional["MarketplaceAdvertiser"] = None
    billing_profile_ids: Optional[list[str]] = Field(None, alias="billingProfileIds", description="List of billing profile identifiers corresponding to billing profiles in request payload.")
    errors: Optional[list["ErrorResponse"]] = Field(None, description="Indicates the error occurred for a billing profile apply operation.")
    index: Optional[int] = Field(None, description="Index corresponding to index of the apply operation in request")

    model_config = {'populate_by_name': True}


class ApplyBillingProfileResponseBillingprofileusagesSuccess(BaseModel):
    advertiser: Optional["MarketplaceAdvertiser"] = None
    billing_profile_ids: Optional[list[str]] = Field(None, alias="billingProfileIds", description="List of billing profile identifiers corresponding to billing profiles in request payload.")
    index: Optional[int] = Field(None, description="Index corresponding to index of the apply operation in request")

    model_config = {'populate_by_name': True}


class ApplyBillingProfileResponseBillingprofileusages(BaseModel):
    """Segregated list of success and error responses for each country and applied billing profile(s)."""
    error: Optional[list["ApplyBillingProfileResponseBillingprofileusagesError"]] = Field(None, description="Error responses for each country and applied billing profile.")
    success: Optional[list["ApplyBillingProfileResponseBillingprofileusagesSuccess"]] = Field(None, description="Success responses for each country and applied billing profile(s).")

    model_config = {'populate_by_name': True}


class ApplyBillingProfileResponse(BaseModel):
    """Contains a list of one or more responses corresponding to each advertiser and applied billing profile(s)."""
    billing_profile_usages: Optional["ApplyBillingProfileResponseBillingprofileusages"] = Field(None, alias="billingProfileUsages", description="Segregated list of success and error responses for each country and applied billing profile(s).")

    model_config = {'populate_by_name': True}


class DocType(StrEnum):
    CREDIT_MEMO = "CREDIT_MEMO"
    GIS_CREDIT_MEMO = "GIS_CREDIT_MEMO"
    GIS_INVOICE = "GIS_INVOICE"
    INVOICE = "INVOICE"
    PAYMENT_COMPLEMENT = "PAYMENT_COMPLEMENT"
    PREPAYMENT_RECEIPT = "PREPAYMENT_RECEIPT"


class AvailableDocumentResponse(BaseModel):
    content_type: Optional[str] = Field(None, alias="contentType")
    doc_type: Optional["DocType"] = Field(None, alias="docType")
    file_name: Optional[str] = Field(None, alias="fileName")
    storage_path: Optional[str] = Field(None, alias="storagePath")

    model_config = {'populate_by_name': True}


class Locale(BaseModel):
    """Preferred locale can be chosen among the list of valid language codes. Check the table below for supported language code. <br/><br/><table border=1><caption> **Supported Locales Table** </caption><tr>"""
    pass


class BaseBillingProfileAddress(BaseModel):
    """Address details to be used for a billing profile"""
    address_line1: str = Field(..., alias="addressLine1")
    address_line2: Optional[str] = Field(None, alias="addressLine2")
    address_line3: Optional[str] = Field(None, alias="addressLine3")
    billing_name: str = Field(..., alias="billingName", description="The name of the person or organization who is going to recieve the invoice")
    city: str
    contact_name: str = Field(..., alias="contactName", description="Contact name for the billing profile which will also be printed on the invoice.")
    country_code: str = Field(..., alias="countryCode")
    fax_number: Optional[str] = Field(None, alias="faxNumber")
    phone_number: Optional[str] = Field(None, alias="phoneNumber")
    postal_code: Optional[str] = Field(None, alias="postalCode")
    primary_email: str = Field(..., alias="primaryEmail")
    secondary_emails: Optional[list[str]] = Field(None, alias="secondaryEmails")
    state_or_region: Optional[str] = Field(None, alias="stateOrRegion")

    model_config = {'populate_by_name': True}


class BaseBillingProfileAgreements(BaseModel):
    consent: bool = Field(..., description="Consent on the provided agreement document.")
    document_name: str = Field(..., alias="documentName", description="Agreement document name against which consent needs to be provided. The content of the agreement can be checked by provi")
    locale: Optional["Locale"] = None

    model_config = {'populate_by_name': True}


class BaseBillingProfileDisplayinfoDisplaynamefield(StrEnum):
    BILLING_NAME = "BILLING_NAME"
    DISPLAY_NAME = "DISPLAY_NAME"


class BaseBillingProfileDisplayinfo(BaseModel):
    """Object determines publicly displayed information about the advertiser"""
    display_name: Optional[str] = Field(None, alias="displayName", description="Relevant for only authors. Required if author chooses displayNameField as DISPLAY_NAME.The value inside this field will ")
    display_name_field: Optional[BaseBillingProfileDisplayinfoDisplaynamefield] = Field(None, alias="displayNameField", description="Determines the name field that will be displayed publicly.For non-authors, the default and only allowed value for this i")

    model_config = {'populate_by_name': True}


class BaseBillingProfileTaxes(BaseModel):
    country_code: Optional[str] = Field(None, alias="countryCode", description="Code of the country to which the tax value belongs to which would override the countryCode provided in the address.")
    type_: str = Field(..., alias="type", description="Type of tax. Check following table for supported tax types: <br/><br/><table border=1><caption> **Supported Tax Types** ")
    value: str = Field(..., description="Value of the tax type. For example, VAT number for VAT tax type, etc.")

    model_config = {'populate_by_name': True}


class BaseBillingProfile(BaseModel):
    """Billing profile object which contains details regarding address, tax, etc."""
    address: "BaseBillingProfileAddress" = Field(..., description="Address details to be used for a billing profile")
    agreements: Optional[list["BaseBillingProfileAgreements"]] = Field(None, description="List of tax-type and corresponding details.")
    billing_profile_name: str = Field(..., alias="billingProfileName", description="Name of a billing profile. This name will only be used to identify the billing profile and will not be used for billing.")
    display_info: Optional["BaseBillingProfileDisplayinfo"] = Field(None, alias="displayInfo", description="Object determines publicly displayed information about the advertiser")
    holding_company: Optional[str] = Field(None, alias="holdingCompany", description="Type of holding company for agency billing profile. Agency Holding Companies are conglomerate entities that own multiple")
    is_default: Optional[bool] = Field(None, alias="isDefault", description="Attribute to indicate if a billing profile is default or not under that global account. Once marked as default, for new ")
    purchase_order_number: str = Field(..., alias="purchaseOrderNumber", description="Number to track spend against the budgeted amounts.")
    taxes: Optional[list["BaseBillingProfileTaxes"]] = Field(None, description="List of tax-type and values.")

    model_config = {'populate_by_name': True}


class BillingInvoiceSummariesRequestAggregation(BaseModel):
    """Object encapsulating the aggregation query information"""
    attribute: Optional[str] = Field(None, description="Aggregation attribute for the billing invoice summary(s)")
    group_by: Optional[str] = Field(None, alias="groupBy", description="Aggregation bucket for the billing invoice summary(s)")
    operation: Optional[str] = Field(None, description="Aggregate operation for the billing invoice summary(s)")

    model_config = {'populate_by_name': True}


class BillingInvoiceSummariesRequestCountryvaluefilter(BaseModel):
    """Object encapsulating the country filtering information"""
    include: Optional[list[str]] = Field(None, description="List of country value(s) to filter from the list of billing invoice summary(s).")
    query_term_match_type: Optional[str] = Field(None, alias="queryTermMatchType", description="Defines how would the string resource field be matched with the query term in filter.")

    model_config = {'populate_by_name': True}


class BillingInvoiceSummariesRequestInvoiceduedaterangefilter(BaseModel):
    """Object encapsulating due date range information"""
    end_date: Optional[str] = Field(None, alias="endDate", description="The ending due date (inclusive) of the date range for filtering invoices. Please provide the date in ISO-8601 format, re")
    start_date: Optional[str] = Field(None, alias="startDate", description="The starting due date (inclusive) of the date range for filtering invoices. Please provide the date in ISO-8601 format, ")

    model_config = {'populate_by_name': True}


class BillingInvoiceSummariesRequestInvoiceissueddaterangefilter(BaseModel):
    """Object encapsulating issued date range information"""
    end_date: Optional[str] = Field(None, alias="endDate", description="The ending issued date (inclusive) of the date range for filtering invoices. Please provide the date in ISO-8601 format,")
    start_date: Optional[str] = Field(None, alias="startDate", description="The starting issued date (inclusive) of the date range for filtering invoices. Please provide the date in ISO-8601 forma")

    model_config = {'populate_by_name': True}


class BillingInvoiceSummariesRequestInvoicenumberfilter(BaseModel):
    """Object encapsulating the invoice number search information"""
    include: Optional[list[str]] = Field(None, description="List of invoice number(s) to filter from the list of billing invoice summary(s).")

    model_config = {'populate_by_name': True}


class BillingInvoiceSummariesRequestPaymentmethodtypevaluefilter(BaseModel):
    """Object encapsulating the payment method type filtering information against which invoice is issued"""
    include: Optional[list[str]] = Field(None, description="List of payment method type value(s) to filter from the list of billing invoice summary(s).")
    query_term_match_type: Optional[str] = Field(None, alias="queryTermMatchType", description="Defines how would the string resource field be matched with the query term in filter.")

    model_config = {'populate_by_name': True}


class BillingInvoiceSummariesRequestReserveordernumberfilter(BaseModel):
    """Object encapsulating the reserve order number search information"""
    include: Optional[list[str]] = Field(None, description="List of reserve order number(s) to filter from the list of billing invoice summary(s).")

    model_config = {'populate_by_name': True}


class BillingInvoiceSummariesRequestSort(BaseModel):
    """Object encapsulating the sort operation information"""
    attribute: Optional[str] = Field(None, description="Sort key or attribute for the list of billing invoice summary(s)")
    direction: Optional[str] = Field(None, description="Sort order(ascending or descending) for list of billing invoice summary(s)")

    model_config = {'populate_by_name': True}


class BillingInvoiceSummariesRequestStatusvaluefilter(BaseModel):
    """Object encapsulating the invoice status filtering information"""
    include: Optional[list[str]] = Field(None, description="List of invoice status value(s) to filter from the list of billing invoice summary(s).")
    query_term_match_type: Optional[str] = Field(None, alias="queryTermMatchType", description="Defines how would the string resource field be matched with the query term in filter.")

    model_config = {'populate_by_name': True}


class BillingInvoiceSummariesRequest(BaseModel):
    """Payload with filter, sort and aggregate key(s) to fetch list of billing invoice summary(s)."""
    aggregation: Optional["BillingInvoiceSummariesRequestAggregation"] = Field(None, description="Object encapsulating the aggregation query information")
    country_value_filter: Optional["BillingInvoiceSummariesRequestCountryvaluefilter"] = Field(None, alias="countryValueFilter", description="Object encapsulating the country filtering information")
    invoice_due_date_range_filter: Optional["BillingInvoiceSummariesRequestInvoiceduedaterangefilter"] = Field(None, alias="invoiceDueDateRangeFilter", description="Object encapsulating due date range information")
    invoice_issued_date_range_filter: Optional["BillingInvoiceSummariesRequestInvoiceissueddaterangefilter"] = Field(None, alias="invoiceIssuedDateRangeFilter", description="Object encapsulating issued date range information")
    invoice_number_filter: Optional["BillingInvoiceSummariesRequestInvoicenumberfilter"] = Field(None, alias="invoiceNumberFilter", description="Object encapsulating the invoice number search information")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Max results / billing invoice summary(s) to be shown in a single page.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Offset to fetch next page with list of billing invoice summary(s).")
    payment_method_type_value_filter: Optional["BillingInvoiceSummariesRequestPaymentmethodtypevaluefilter"] = Field(None, alias="paymentMethodTypeValueFilter", description="Object encapsulating the payment method type filtering information against which invoice is issued")
    reserve_order_number_filter: Optional["BillingInvoiceSummariesRequestReserveordernumberfilter"] = Field(None, alias="reserveOrderNumberFilter", description="Object encapsulating the reserve order number search information")
    sort: Optional["BillingInvoiceSummariesRequestSort"] = Field(None, description="Object encapsulating the sort operation information")
    status_value_filter: Optional["BillingInvoiceSummariesRequestStatusvaluefilter"] = Field(None, alias="statusValueFilter", description="Object encapsulating the invoice status filtering information")

    model_config = {'populate_by_name': True}


class CurrencyAmount(BaseModel):
    """Identifies the amount along with currency code."""
    amount: float
    currency_code: str = Field(..., alias="currencyCode")

    model_config = {'populate_by_name': True}


class BillingInvoiceSummaryCountry(BaseModel):
    """Object encapsulating billing invoice country information"""
    code: Optional[str] = Field(None, description="Country code for the invoice")
    value: Optional[str] = Field(None, description="Country name for the invoice")

    model_config = {'populate_by_name': True}


class BillingInvoiceSummaryRefunddetails(BaseModel):
    """Object encapsulating the invoice refund information"""
    amount: Optional["CurrencyAmount"] = Field(None, description="Object identifies the refunded amount along with currency code for the invoice")
    reason: Optional[str] = Field(None, description="Refund reason of the invoice")
    status: Optional[str] = Field(None, description="Refund status of the invoice")

    model_config = {'populate_by_name': True}


class BillingInvoiceSummary(BaseModel):
    """Object encapsulating billing invoice summary information"""
    amount_due: Optional["CurrencyAmount"] = Field(None, alias="amountDue", description="Object identifies the amount due along with currency code for the invoice")
    country: Optional["BillingInvoiceSummaryCountry"] = Field(None, description="Object encapsulating billing invoice country information")
    due_date: Optional[str] = Field(None, alias="dueDate", description="Invoice due date in ISO-8601 format, representing a UTC date with only the date portion (no time)")
    e_payment_status: Optional[str] = Field(None, alias="ePaymentStatus", description="Object encapsulating e-payment status for the invoice")
    id_: Optional[str] = Field(None, alias="id", description="Billing Document Number")
    issued_date: Optional[str] = Field(None, alias="issuedDate", description="Invoice issued date in ISO-8601 format, representing a UTC date with only the date portion (no time)")
    payment_method_type: Optional[str] = Field(None, alias="paymentMethodType", description="Object encapsulating payment method type against which invoice is issued")
    refund_details: Optional["BillingInvoiceSummaryRefunddetails"] = Field(None, alias="refundDetails", description="Object encapsulating the invoice refund information")
    remaining_amount_due: Optional["CurrencyAmount"] = Field(None, alias="remainingAmountDue", description="Object identifies the remaining amount due along with currency code for the invoice")
    reserve_order_number: Optional[str] = Field(None, alias="reserveOrderNumber", description="Reserve Order Number")
    status: Optional[str] = Field(None, description="Object encapsulating billing invoice summary status information")
    status_decorator: Optional[str] = Field(None, alias="statusDecorator", description="Object encapsulating billing invoice summary status decorator information")

    model_config = {'populate_by_name': True}


class BillingInvoiceSummariesResponseAggregationResults(BaseModel):
    """Object encapsulating the aggregation result as per aggregation attribute, operation and bucket (or groupById) on the list of billing invoice summary(s)."""
    currency_code: Optional[str] = Field(None, alias="currencyCode", description="Currency of the aggregate value over the aggregation bucket for a certain key on the aggregation attribute for the speci")
    group_id: Optional[str] = Field(None, alias="groupId", description="Aggregation bucket key (or groupById) to which the specific aggregation result belongs.")
    value: Optional[float] = Field(None, description="Aggregate value over the aggregation bucket for a certain key on the aggregation attribute for the specified aggregation")

    model_config = {'populate_by_name': True}


class BillingInvoiceSummariesResponseAggregation(BaseModel):
    """Object encapsulating the aggregation query and result(s) information"""
    invoice_summaries: Optional[list["BillingInvoiceSummary"]] = Field(None, alias="invoiceSummaries", description="List of object(s) encapsulating information of billing invoice summary(s).")
    results: Optional[list["BillingInvoiceSummariesResponseAggregationResults"]] = Field(None, description="Object encapsulating the aggregation result as per aggregation attribute, operation and bucket (or groupById) on the lis")

    model_config = {'populate_by_name': True}


class BillingInvoiceSummariesResponse(BaseModel):
    """Contains an object encapsulating either the aggregation result(s) or sorted & filtered billing invoice summary(s)."""
    aggregation: Optional["BillingInvoiceSummariesResponseAggregation"] = Field(None, description="Object encapsulating the aggregation query and result(s) information")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Offset to fetch next page with list of billing invoice summary(s).")

    model_config = {'populate_by_name': True}


class BillingProfile(BaseModel):
    """Billing profile object which contains details regarding address, tax, etc."""
    pass


class BillingProfileAgreementContentResponse(BaseModel):
    content: Optional[str] = Field(None, description="An HTML document to be rendered and read. A consent needs to be provided against this content.")

    model_config = {'populate_by_name': True}


class BillingProfileErrorResponse(BaseModel):
    """Contains the machine-readable error code and human-readable details."""
    code: Optional[str] = Field(None, description="The code describing the error reason.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class BillingProfileStatus(BaseModel):
    """Current Status of the link between the billing Profile and the country. The following table defines the statuses and their descriptions. <table><thead> <tr> <th>Status</th> <th>Description</th> </tr><"""
    status_code: Optional[str] = Field(None, alias="statusCode")
    status_message: Optional[str] = Field(None, alias="statusMessage")

    model_config = {'populate_by_name': True}


class BillingProfileUsage(BaseModel):
    """This object contains billing profile(s) that is applied to a given country under a global account"""
    advertiser: Optional["MarketplaceAdvertiser"] = None
    billing_profile_usage_id: Optional[str] = Field(None, alias="billingProfileUsageId", description="Billing profile usage unique identifier.")
    billing_profiles: Optional[list["BillingProfile"]] = Field(None, alias="billingProfiles")
    fallback_billing_profiles: Optional[list["BillingProfile"]] = Field(None, alias="fallbackBillingProfiles")
    status: Optional["BillingProfileStatus"] = None

    model_config = {'populate_by_name': True}


class BillingStatementErrorResponse(BaseModel):
    billing_statement_request_id: Optional[str] = Field(None, alias="billingStatementRequestId", description="Billing statement request identifier.")
    code: Optional[str] = Field(None, description="The code describing the error reason.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class CreateBillingProfile(BaseModel):
    """Object encapsulating information for creating a billing profile"""
    pass


class CreateBillingProfilesRequest(BaseModel):
    """Contains a list of one or more billing profiles to be created."""
    billing_profiles: list["CreateBillingProfile"] = Field(..., alias="billingProfiles")

    model_config = {'populate_by_name': True}


class CreateBillingStatementRequestFormat(StrEnum):
    CSV = "CSV"


class CreateBillingStatementRequest(BaseModel):
    country_codes: Optional[list["CountryCode"]] = Field(None, alias="countryCodes", description="List of countries for which billing statements are to be fetched. If no country codes are passed in the request, the sta")
    end_date: str = Field(..., alias="endDate", description="End date of the invoice summary period for a report in the format YYYY-MM-DD.")
    format_: Optional[CreateBillingStatementRequestFormat] = Field(None, alias="format", description="Format of the file, such as, for billing statements, etc.")
    locale: str = Field(..., description="Preferred locale can be chosen among the list of valid language codes. Check the table below for supported language code")
    start_date: str = Field(..., alias="startDate", description="Start date of the invoice summary period for a report in the format YYYY-MM-DD.")

    model_config = {'populate_by_name': True}


class CreateBillingStatementResponse(BaseModel):
    billing_statement_request_id: Optional[str] = Field(None, alias="billingStatementRequestId", description="Billing statement request identifier.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class CreateOrUpdateBillingProfilesResponseBillingprofilesError(BaseModel):
    billing_profile_id: Optional[str] = Field(None, alias="billingProfileId", description="Billing profile identifier corresponding to a billing profile in request payload.")
    errors: Optional[list["ErrorResponse"]] = Field(None, description="List of errors for a particular billing profile in request payload.")
    index: Optional[int] = Field(None, description="Indicates the index of a billing profile in request payload.")

    model_config = {'populate_by_name': True}


class CreateOrUpdateBillingProfilesResponseBillingprofilesSuccess(BaseModel):
    billing_profile_id: Optional[str] = Field(None, alias="billingProfileId", description="Billing profile identifier corresponding to a billing profile in the list.")
    index: Optional[int] = Field(None, description="Indicates the index of billing profile in the list of request payload.")

    model_config = {'populate_by_name': True}


class CreateOrUpdateBillingProfilesResponseBillingprofiles(BaseModel):
    """Segregated list of success and error responses for each billing profile in request payload."""
    error: Optional[list["CreateOrUpdateBillingProfilesResponseBillingprofilesError"]] = Field(None, description="List of error responses for each billing profile in request payload.")
    success: Optional[list["CreateOrUpdateBillingProfilesResponseBillingprofilesSuccess"]] = Field(None, description="List of success responses for each billing profile in request payload.")

    model_config = {'populate_by_name': True}


class CreateOrUpdateBillingProfilesResponse(BaseModel):
    """Contains a list of one or more responses corresponding to each billing profile along with index."""
    billing_profiles: Optional["CreateOrUpdateBillingProfilesResponseBillingprofiles"] = Field(None, alias="billingProfiles", description="Segregated list of success and error responses for each billing profile in request payload.")

    model_config = {'populate_by_name': True}


class GetBillingProfileUsageRequestFilters(BaseModel):
    """Filter object to be used to fetch list of billing profile usage(s)."""
    advertiser_filter: Optional[list["MarketplaceAdvertiser"]] = Field(None, alias="advertiserFilter", description="Indicates list of advertiser identifiers(s) for which billing profile(s) needs to be fetched.")

    model_config = {'populate_by_name': True}


class GetBillingProfileUsageRequest(BaseModel):
    """The request body to fetch billing profiles linked to each country of global ads account."""
    expand_billing_profile: Optional[bool] = Field(None, alias="expandBillingProfile", description="By default only the billingProfileId linked to the country will be returned. Choose `true` if you would like to see the ")
    expand_fallback_billing_profile: Optional[bool] = Field(None, alias="expandFallbackBillingProfile", description="Choose `true` if you would like to see the information currently being used for billing for this marketplace. Useful whe")
    filters: Optional["GetBillingProfileUsageRequestFilters"] = Field(None, description="Filter object to be used to fetch list of billing profile usage(s).")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Max results / billing profile usage(s) to be shown in a single page.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Offset to fetch next page with list of billing profile usage(s).")

    model_config = {'populate_by_name': True}


class GetBillingProfileUsageResponse(BaseModel):
    """Contains billing profile usages: list of advertisers and applied billing profile."""
    billing_profile_usages: Optional[list["BillingProfileUsage"]] = Field(None, alias="billingProfileUsages")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Max results / billing profile usage(s) to be shown in a single page.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Indicates the pagination token to be used to access next page.")

    model_config = {'populate_by_name': True}


class GetBillingProfilesRequestFilters(BaseModel):
    """Filter object to be used to fetch list of billing profile(s)."""
    billing_profile_id_filter: Optional[list[str]] = Field(None, alias="billingProfileIdFilter", description="Indicates list of billing profile identifier(s) for which billing profile(s) needs to be fetched.")
    default_billing_profile_filter: Optional[bool] = Field(None, alias="defaultBillingProfileFilter", description="Indicates if default billing profile needs to be fetched.")

    model_config = {'populate_by_name': True}


class GetBillingProfilesRequest(BaseModel):
    """Payload to fetch list of billing profile(s)."""
    filters: Optional["GetBillingProfilesRequestFilters"] = Field(None, description="Filter object to be used to fetch list of billing profile(s).")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Max results / billing profile(s) to be shown in a single page.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Offset to fetch next page with list of billing profile(s).")

    model_config = {'populate_by_name': True}


class GetBillingProfilesResponse(BaseModel):
    """Paginated list of billing profile(s) response."""
    billing_profiles: Optional[list["BillingProfile"]] = Field(None, alias="billingProfiles", description="Indicates list of billing profile(s).")
    max_results: Optional[int] = Field(None, alias="maxResults", description="Max results / billing profile(s) to be shown in a single page.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Offset to fetch next page with list of billing profile(s).")

    model_config = {'populate_by_name': True}


class GetBillingStatementResponseReportstatus(StrEnum):
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"


class GetBillingStatementResponse(BaseModel):
    details: Optional[str] = Field(None, description="The human-readable description of the response.")
    report_status: Optional[GetBillingStatementResponseReportstatus] = Field(None, alias="reportStatus", description="The request status of the billing statement.")
    s3_download_link: Optional[str] = Field(None, alias="s3DownloadLink", description="Download link of the billing statement file. Only when reportStatus is SUCCESS.")

    model_config = {'populate_by_name': True}


class UnavailableDocumentResponse(BaseModel):
    content_type: Optional[str] = Field(None, alias="contentType")
    doc_type: Optional["DocType"] = Field(None, alias="docType")
    file_name: Optional[str] = Field(None, alias="fileName")
    reason: Optional[str] = None
    storage_path: Optional[str] = Field(None, alias="storagePath")

    model_config = {'populate_by_name': True}


class GetDocumentResponseContent(BaseModel):
    available_documents: Optional[list["AvailableDocumentResponse"]] = Field(None, alias="availableDocuments")
    unavailable_documents: Optional[list["UnavailableDocumentResponse"]] = Field(None, alias="unavailableDocuments")

    model_config = {'populate_by_name': True}


class InternalServerExceptionResponseContent(BaseModel):
    """Thrown when service encounters unexpected error during processing of request."""
    code: str = Field(..., description="Error Code.")
    message: str = Field(..., description="Human readable response message.")

    model_config = {'populate_by_name': True}


class ResourceNotFoundExceptionResponseContent(BaseModel):
    """Request references a resource which does not exist."""
    code: str = Field(..., description="Error Code.")
    message: str = Field(..., description="Human readable response message.")

    model_config = {'populate_by_name': True}


class UnauthorizedExceptionResponseContent(BaseModel):
    code: str = Field(..., description="Error Code.")
    message: str = Field(..., description="Human readable response message.")

    model_config = {'populate_by_name': True}


class UpdateBillingProfile(BaseModel):
    """Object encapsulating information for updating a billing profile"""
    pass


class UpdateBillingProfilesRequest(BaseModel):
    """Contains a list of one or more billing profiles to be updated."""
    billing_profiles: Optional[list["UpdateBillingProfile"]] = Field(None, alias="billingProfiles")

    model_config = {'populate_by_name': True}


class ValidationExceptionResponseContent(BaseModel):
    """The input fails to satisfy the constraints specified by an Advertising API service."""
    code: str = Field(..., description="Error Code.")
    message: str = Field(..., description="Human readable response message.")

    model_config = {'populate_by_name': True}


class adProgram(StrEnum):
    AMAZON_LIVE = "AMAZON LIVE"
    CREATOR_CONNECTIONS = "CREATOR CONNECTIONS"
    SPONSORED_BRANDS = "SPONSORED BRANDS"
    SPONSORED_DISPLAY = "SPONSORED DISPLAY"
    SPONSORED_DISPLAY_FOR_FIRE_TV = "SPONSORED DISPLAY FOR FIRE TV"
    SPONSORED_PRODUCT = "SPONSORED PRODUCT"


class countryCode(BaseModel):
    """ISO 3611 country code"""
    pass


class address(BaseModel):
    address_line1: str = Field(..., alias="addressLine1")
    address_line2: str = Field(..., alias="addressLine2")
    address_line3: str = Field(..., alias="addressLine3")
    attention_name: Optional[str] = Field(None, alias="attentionName")
    city: str
    company_name: str = Field(..., alias="companyName")
    country_code: "countryCode" = Field(..., alias="countryCode")
    postal_code: str = Field(..., alias="postalCode")
    state_or_region: str = Field(..., alias="stateOrRegion")

    model_config = {'populate_by_name': True}


class date(BaseModel):
    """Date in YYYYMMDD format"""
    pass


class currencyCode(StrEnum):
    AED = "AED"
    AUD = "AUD"
    BRL = "BRL"
    CAD = "CAD"
    EGP = "EGP"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"
    JPY = "JPY"
    MXN = "MXN"
    PLN = "PLN"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    TRY = "TRY"
    USD = "USD"


class currencyAmount(BaseModel):
    amount: Optional[float] = None
    currency_code: Optional["currencyCode"] = Field(None, alias="currencyCode")

    model_config = {'populate_by_name': True}


class feeFeeidentifiers(BaseModel):
    """Identifiers describing attributes for different fee types. * countryCode: ISO 3611 country code for country specific Regulatory Advertising Fees."""
    country_code: Optional["countryCode"] = Field(None, alias="countryCode")

    model_config = {'populate_by_name': True}


class feeFeetype(StrEnum):
    V_3P_AUTO_NON_ABSORBED_FEE = "3P_AUTO_NON_ABSORBED_FEE"
    V_3P_NON_ABSORBED_FEE = "3P_NON_ABSORBED_FEE"
    V_3P_PREBID_FEE = "3P_PREBID_FEE"
    AUDIENCE_FEE = "AUDIENCE_FEE"
    OMNICHANNEL_METRICS_FEE = "OMNICHANNEL_METRICS_FEE"
    PLATFORM_FEE = "PLATFORM_FEE"
    REGULATORY_ADVERTISING_FEE = "REGULATORY_ADVERTISING_FEE"
    REWARDED_ADS_COST = "REWARDED_ADS_COST"


class fee(BaseModel):
    cost: "currencyAmount"
    fee_identifiers: Optional["feeFeeidentifiers"] = Field(None, alias="feeIdentifiers", description="Identifiers describing attributes for different fee types. * countryCode: ISO 3611 country code for country specific Reg")
    fee_type: feeFeetype = Field(..., alias="feeType", description="* `PLATFORM_FEE`: Billable fee set at the Rodeo Entity level by internal users which reflects the cost of using the Amaz")

    model_config = {'populate_by_name': True}


class adjustment(BaseModel):
    accounting_date: "date" = Field(..., alias="accountingDate")
    amount: "currencyAmount"
    comments: Optional[str] = None
    fees: Optional[list["fee"]] = Field(None, description="Charges can include different fees (see feeType below).")
    portfolio_id: Optional[int] = Field(None, alias="portfolioId", description="Sponsored Ads only. This identifier maps to one of the portfolios listed in the portfolios section.")

    model_config = {'populate_by_name': True}


class adjustments(BaseModel):
    """List of adjustments (positive and negative) applied to this invoice."""
    pass


class advertiserTypes(StrEnum):
    AGENCY = "AGENCY"
    DSP_ADVERTISING_ACCOUNT = "DSP_ADVERTISING_ACCOUNT"
    SELLER = "SELLER"
    VENDOR = "VENDOR"


class advertiserMarketplace(BaseModel):
    advertiser_id: str = Field(..., alias="advertiserId")
    advertiser_type: Optional["advertiserTypes"] = Field(None, alias="advertiserType")
    marketplace_id: str = Field(..., alias="marketplaceId")

    model_config = {'populate_by_name': True}


class billingLevel(StrEnum):
    ACCOUNT = "ACCOUNT"
    CAMPAIGN = "CAMPAIGN"


class billingAggregation(BaseModel):
    billing_aggregation_id: Optional[str] = Field(None, alias="billingAggregationId", description="An identifier that helps associate this invoice with specific billing entities, such as campaigns or rodeo advertiser ac")
    billing_aggregation_resource_path: Optional[str] = Field(None, alias="billingAggregationResourcePath", description="The resource path to suffix to the base URL endpoints to retrieve the corresponding billing aggregation entity, such as ")
    billing_level: Optional["billingLevel"] = Field(None, alias="billingLevel")

    model_config = {'populate_by_name': True}


class billingNotificationImpact(StrEnum):
    CAMPAIGNS_SUSPENDED = "CAMPAIGNS_SUSPENDED"
    NO_IMPACT = "NO_IMPACT"


class billingNotificationNames(StrEnum):
    ACCOUNT_ERROR = "ACCOUNT_ERROR"
    ACCOUNT_ERROR_IN_SELLER = "ACCOUNT_ERROR_IN_SELLER"
    AUTHOR_REGISTRATION_NOT_FOUND = "AUTHOR_REGISTRATION_NOT_FOUND"
    BAD_DEBT_SUSPENSION = "BAD_DEBT_SUSPENSION"
    BILLING_ADDRESS_REGISTRATION_NOT_FOUND = "BILLING_ADDRESS_REGISTRATION_NOT_FOUND"
    BILLING_PROFILE_ERROR = "BILLING_PROFILE_ERROR"
    BILLING_PROFILE_INVALID_DSA_INFO = "BILLING_PROFILE_INVALID_DSA_INFO"
    BILLING_PROFILE_INVALID_PERMISSION = "BILLING_PROFILE_INVALID_PERMISSION"
    BILLING_PROFILE_INVALID_TAX = "BILLING_PROFILE_INVALID_TAX"
    CNPJ_VERIFICATION_IN_PROGRESS = "CNPJ_VERIFICATION_IN_PROGRESS"
    CREDIT_CARD_ALLOWED_AMOUNT_FAILURE = "CREDIT_CARD_ALLOWED_AMOUNT_FAILURE"
    CREDIT_CARD_AUTHENTICATION_FAILURE = "CREDIT_CARD_AUTHENTICATION_FAILURE"
    CREDIT_CARD_AUTHORIZATION_FAILURE = "CREDIT_CARD_AUTHORIZATION_FAILURE"
    CREDIT_CARD_AUTH_EXPIRED_FAILURE = "CREDIT_CARD_AUTH_EXPIRED_FAILURE"
    CREDIT_CARD_CHARGE_DISPUTE_CAUSED_SUSPENSION = "CREDIT_CARD_CHARGE_DISPUTE_CAUSED_SUSPENSION"
    CREDIT_CARD_CLOSED_FAILURE = "CREDIT_CARD_CLOSED_FAILURE"
    CREDIT_CARD_EXPIRED = "CREDIT_CARD_EXPIRED"
    CREDIT_CARD_EXPIRES_SOON = "CREDIT_CARD_EXPIRES_SOON"
    CREDIT_CARD_GENERIC_FAILURE = "CREDIT_CARD_GENERIC_FAILURE"
    CREDIT_CARD_INELIGIBLE_CARD = "CREDIT_CARD_INELIGIBLE_CARD"
    CREDIT_CARD_INELIGIBLE_SHARED_CARD = "CREDIT_CARD_INELIGIBLE_SHARED_CARD"
    CREDIT_CARD_INSUF_BAL = "CREDIT_CARD_INSUF_BAL"
    CREDIT_CARD_INTERNAL_FAILURE = "CREDIT_CARD_INTERNAL_FAILURE"
    CREDIT_CARD_INVALID_ACCOUNT_FAILURE = "CREDIT_CARD_INVALID_ACCOUNT_FAILURE"
    CREDIT_CARD_INVALID_ADDRESS_FAILURE = "CREDIT_CARD_INVALID_ADDRESS_FAILURE"
    CREDIT_CARD_INVALID_BANK_HOLDER_FAILURE = "CREDIT_CARD_INVALID_BANK_HOLDER_FAILURE"
    CREDIT_CARD_INVALID_CARD_FAILURE = "CREDIT_CARD_INVALID_CARD_FAILURE"
    CREDIT_CARD_INVALID_DETAILS = "CREDIT_CARD_INVALID_DETAILS"
    CREDIT_CARD_ISSUE_WITH_CARD = "CREDIT_CARD_ISSUE_WITH_CARD"
    CREDIT_CARD_LOCKED_CARD = "CREDIT_CARD_LOCKED_CARD"
    CREDIT_CARD_MFA_EXPIRED_FAILURE = "CREDIT_CARD_MFA_EXPIRED_FAILURE"
    CREDIT_CARD_PAYMENT_FAILURE_CAUSED_SUSPENSION = "CREDIT_CARD_PAYMENT_FAILURE_CAUSED_SUSPENSION"
    CREDIT_CARD_TRANSACTION_SIZE_FAILURE = "CREDIT_CARD_TRANSACTION_SIZE_FAILURE"
    CREDIT_CARD_VERIFICATION_FAILURE = "CREDIT_CARD_VERIFICATION_FAILURE"
    CREDIT_CARD_VERIFICATION_FAILURE_CAUSED_SUSPENSION = "CREDIT_CARD_VERIFICATION_FAILURE_CAUSED_SUSPENSION"
    CREDIT_CARD_VERIFICATION_PENDING = "CREDIT_CARD_VERIFICATION_PENDING"
    CREDIT_CARD_VOLUME_FAILURE = "CREDIT_CARD_VOLUME_FAILURE"
    CREDIT_CARD_WITH_VERIFICATION_PAYMENT_FAILURE = "CREDIT_CARD_WITH_VERIFICATION_PAYMENT_FAILURE"
    CREDIT_CARD_WITH_VERIFICATION_PAYMENT_FAILURE_CAUSED_SUSPENSION = "CREDIT_CARD_WITH_VERIFICATION_PAYMENT_FAILURE_CAUSED_SUSPENSION"
    CREDIT_CARD_WITH_VERIFICATION_PENDING_CAUSED_SUSPENSION = "CREDIT_CARD_WITH_VERIFICATION_PENDING_CAUSED_SUSPENSION"
    CREDIT_CARD_WITH_VERIFICATION_SUSPENSION_WITH_PAYMENT_IN_PROGRESS = "CREDIT_CARD_WITH_VERIFICATION_SUSPENSION_WITH_PAYMENT_IN_PROGRESS"
    DEDUCT_FROM_PROCEEDS_PAYMENT_FAILURE_CAUSED_SUSPENSION = "DEDUCT_FROM_PROCEEDS_PAYMENT_FAILURE_CAUSED_SUSPENSION"
    DEDUCT_FROM_PROCEEDS_WITH_CREDIT_CARD_FALLBACK_PAYMENT_FAILURE_CAUSED_SUSPENSION = "DEDUCT_FROM_PROCEEDS_WITH_CREDIT_CARD_FALLBACK_PAYMENT_FAILURE_CAUSED_SUSPENSION"
    DEDUCT_FROM_PROCEEDS_WITH_CREDIT_LIMIT_ELIGIBLE = "DEDUCT_FROM_PROCEEDS_WITH_CREDIT_LIMIT_ELIGIBLE"
    DEDUCT_FROM_PROCEEDS_WITH_MONTHLY_INVOICE_ELIGIBLE = "DEDUCT_FROM_PROCEEDS_WITH_MONTHLY_INVOICE_ELIGIBLE"
    DIRECT_DEBIT_PAYMENT_PENDING = "DIRECT_DEBIT_PAYMENT_PENDING"
    DPS_DENIED_PARTY = "DPS_DENIED_PARTY"
    DPS_VERIFICATION_PENDING = "DPS_VERIFICATION_PENDING"
    INACTIVE_SELLER_ACCOUNT_CAUSED_SUSPENSION = "INACTIVE_SELLER_ACCOUNT_CAUSED_SUSPENSION"
    INVALID_PAYMENT_REGISTRATION = "INVALID_PAYMENT_REGISTRATION"
    MERCH_ON_DEMAND_REGISTRATION_NOT_FOUND = "MERCH_ON_DEMAND_REGISTRATION_NOT_FOUND"
    PAY_BY_INVOICE_OVERDUE_PAYMENT = "PAY_BY_INVOICE_OVERDUE_PAYMENT"
    PAY_BY_INVOICE_OVERDUE_PAYMENT_CAUSED_SUSPENSION = "PAY_BY_INVOICE_OVERDUE_PAYMENT_CAUSED_SUSPENSION"
    PAY_BY_INVOICE_OVERDUE_PAYMENT_PENDING_SUSPENSION = "PAY_BY_INVOICE_OVERDUE_PAYMENT_PENDING_SUSPENSION"
    PAY_BY_INVOICE_UPCOMING_PAYMENT = "PAY_BY_INVOICE_UPCOMING_PAYMENT"
    PENDING_PAYMENT_REGISTRATION = "PENDING_PAYMENT_REGISTRATION"
    PENDING_VALID_CNPJ_REGISTRATION = "PENDING_VALID_CNPJ_REGISTRATION"
    POLICY_VIOLATIONS = "POLICY_VIOLATIONS"
    PREPAY_INSUFFICIENT_BALANCE = "PREPAY_INSUFFICIENT_BALANCE"
    PRE_AUTH_FAILURE_SUSPENSION = "PRE_AUTH_FAILURE_SUSPENSION"
    RO_INSUFFICIENT_BALANCE = "RO_INSUFFICIENT_BALANCE"
    SELLER_ACCOUNT_BALANCE_LOW = "SELLER_ACCOUNT_BALANCE_LOW"
    SELLER_ACCOUNT_BALANCE_RESERVED = "SELLER_ACCOUNT_BALANCE_RESERVED"
    SELLER_ACCOUNT_INSUFFICIENT_AVAILABLE_BALANCE_CAUSED_SUSPENSION = "SELLER_ACCOUNT_INSUFFICIENT_AVAILABLE_BALANCE_CAUSED_SUSPENSION"
    SELLER_ACCOUNT_INSUFFICIENT_GROSS_BALANCE_CAUSED_SUSPENSION = "SELLER_ACCOUNT_INSUFFICIENT_GROSS_BALANCE_CAUSED_SUSPENSION"
    SELLER_ACCOUNT_MISSING_BACKUP = "SELLER_ACCOUNT_MISSING_BACKUP"
    SELLER_ACCOUNT_PAYMENT_FAILURE_CAUSED_SUSPENSION = "SELLER_ACCOUNT_PAYMENT_FAILURE_CAUSED_SUSPENSION"
    SELLER_ACCOUNT_WITH_CREDIT_CARD_FALLBACK_PAYMENT_FAILURE_CAUSED_SUSPENSION = "SELLER_ACCOUNT_WITH_CREDIT_CARD_FALLBACK_PAYMENT_FAILURE_CAUSED_SUSPENSION"
    STORED_VALUE_AUTO_RELOAD_PAYMENT_FAILURE = "STORED_VALUE_AUTO_RELOAD_PAYMENT_FAILURE"
    SUSPICIOUS_ACTIVITY = "SUSPICIOUS_ACTIVITY"
    TAX_ID_VALIDATION_IN_PROGRESS = "TAX_ID_VALIDATION_IN_PROGRESS"
    TAX_ID_VALIDATION_REJECTED = "TAX_ID_VALIDATION_REJECTED"


class billingNotificationSeverity(StrEnum):
    ALERT = "ALERT"
    INFO = "INFO"
    WARNING = "WARNING"


class billingNotification(BaseModel):
    advertiser_marketplaces: Optional[list["advertiserMarketplace"]] = Field(None, alias="advertiserMarketplaces")
    description: str
    impact: "billingNotificationImpact"
    notification_name: "billingNotificationNames" = Field(..., alias="notificationName")
    payment_due_date: Optional[str] = Field(None, alias="paymentDueDate")
    priority: int
    severity: "billingNotificationSeverity"
    suspension_date: Optional[str] = Field(None, alias="suspensionDate")
    title: str

    model_config = {'populate_by_name': True}


class billingStatusCode(StrEnum):
    ACCOUNT_BILLING_ISSUE = "ACCOUNT_BILLING_ISSUE"
    INVALID_PAYMENT_REGISTRATION = "INVALID_PAYMENT_REGISTRATION"
    PAYMENT_METHOD_EXPIRED = "PAYMENT_METHOD_EXPIRED"
    PAYMENT_METHOD_VERIFICATION_FAILED = "PAYMENT_METHOD_VERIFICATION_FAILED"
    PENDING_BILLING_REGISTRATION = "PENDING_BILLING_REGISTRATION"
    PENDING_PAYMENT_REGISTRATION = "PENDING_PAYMENT_REGISTRATION"
    PENDING_TAX_REGISTRATION = "PENDING_TAX_REGISTRATION"
    RESERVE_ORDER_BALANCE_TOO_LOW = "RESERVE_ORDER_BALANCE_TOO_LOW"
    STORED_VALUE_BALANCE_TOO_LOW = "STORED_VALUE_BALANCE_TOO_LOW"
    VALID_BILLING_STATUS = "VALID_BILLING_STATUS"


class billingStatus(BaseModel):
    billing_status_code: "billingStatusCode" = Field(..., alias="billingStatusCode")
    message: str

    model_config = {'populate_by_name': True}


class bulkGetBillingNotificationsErrorCodes(StrEnum):
    BAD_REQUEST = "BAD_REQUEST"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    NOT_AUTHORIZED = "NOT_AUTHORIZED"
    NOT_FOUND = "NOT_FOUND"


class bulkGetBillingNotificationsError(BaseModel):
    advertiser_marketplace: Optional["advertiserMarketplace"] = Field(None, alias="advertiserMarketplace")
    advertiser_marketplaces: Optional[list["advertiserMarketplace"]] = Field(None, alias="advertiserMarketplaces")
    description: str
    error_code: "bulkGetBillingNotificationsErrorCodes" = Field(..., alias="errorCode")
    index: int

    model_config = {'populate_by_name': True}


class bulkGetBillingNotificationsErrorResponse(BaseModel):
    code: Optional[str] = None
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class locale(StrEnum):
    AR_AE = "ar_AE"
    BN_IN = "bn_IN"
    CS_CZ = "cs_CZ"
    DE_DE = "de_DE"
    EN_AE = "en_AE"
    EN_AU = "en_AU"
    EN_CA = "en_CA"
    EN_GB = "en_GB"
    EN_IN = "en_IN"
    EN_NG = "en_NG"
    EN_SG = "en_SG"
    EN_US = "en_US"
    EN_ZA = "en_ZA"
    ES_CL = "es_CL"
    ES_CO = "es_CO"
    ES_ES = "es_ES"
    ES_MX = "es_MX"
    ES_US = "es_US"
    FR_BE = "fr_BE"
    FR_CA = "fr_CA"
    FR_FR = "fr_FR"
    HE_IL = "he_IL"
    HI_IN = "hi_IN"
    IT_IT = "it_IT"
    JA_JP = "ja_JP"
    KO_KR = "ko_KR"
    ML_IN = "ml_IN"
    MR_IN = "mr_IN"
    NL_BE = "nl_BE"
    NL_NL = "nl_NL"
    PL_PL = "pl_PL"
    PT_BR = "pt_BR"
    PT_PT = "pt_PT"
    SV_SE = "sv_SE"
    TA_IN = "ta_IN"
    TE_IN = "te_IN"
    TR_TR = "tr_TR"
    ZH_CN = "zh_CN"
    ZH_TW = "zh_TW"


class bulkGetBillingNotificationsRequestBody(BaseModel):
    """The properties needed to get the billing notifications for a set of advertisers."""
    advertiser_marketplaces: Optional[list["advertiserMarketplace"]] = Field(None, alias="advertiserMarketplaces")
    locale: Optional["locale"] = None

    model_config = {'populate_by_name': True}


class bulkGetBillingNotificationsSuccess(BaseModel):
    advertiser_marketplace: Optional["advertiserMarketplace"] = Field(None, alias="advertiserMarketplace")
    billing_notifications: list["billingNotification"] = Field(..., alias="billingNotifications")
    index: int

    model_config = {'populate_by_name': True}


class bulkGetBillingNotificationsResponse(BaseModel):
    error: list["bulkGetBillingNotificationsError"]
    success: list["bulkGetBillingNotificationsSuccess"]

    model_config = {'populate_by_name': True}


class bulkGetBillingStatusErrorCodes(StrEnum):
    BAD_REQUEST = "BAD_REQUEST"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    NOT_AUTHORIZED = "NOT_AUTHORIZED"
    NOT_FOUND = "NOT_FOUND"


class bulkGetBillingStatusError(BaseModel):
    advertiser_marketplace: Optional["advertiserMarketplace"] = Field(None, alias="advertiserMarketplace")
    description: Optional[str] = None
    error_code: Optional["bulkGetBillingStatusErrorCodes"] = Field(None, alias="errorCode")
    index: int

    model_config = {'populate_by_name': True}


class bulkGetBillingStatusErrorResponse(BaseModel):
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class bulkGetBillingStatusSuccess(BaseModel):
    advertiser_marketplace: "advertiserMarketplace" = Field(..., alias="advertiserMarketplace")
    billing_status: "billingStatus" = Field(..., alias="billingStatus")
    index: int

    model_config = {'populate_by_name': True}


class bulkGetBillingStatusResponse(BaseModel):
    error: list["bulkGetBillingStatusError"]
    success: list["bulkGetBillingStatusSuccess"]

    model_config = {'populate_by_name': True}


class bulkGetBillingStatusesRequestBody(BaseModel):
    """The properties needed to get the billing statuses for a set of advertisers."""
    advertiser_marketplaces: list["advertiserMarketplace"] = Field(..., alias="advertiserMarketplaces")
    locale: Optional["locale"] = None

    model_config = {'populate_by_name': True}


class email(BaseModel):
    display_name: str = Field(..., alias="displayName", description="Customer name used in email communication.")
    email_address: str = Field(..., alias="emailAddress")

    model_config = {'populate_by_name': True}


class contactInfo(BaseModel):
    address: "address"
    email: "email"

    model_config = {'populate_by_name': True}


class documentType(StrEnum):
    CREDIT_NOTE = "CREDIT_NOTE"
    INVOICE = "INVOICE"


class governmentInvoiceInformationTransactiontype(StrEnum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"


class governmentInvoiceInformation(BaseModel):
    """Government invoice data is provided in marketplaces (such as Italy or India) that require a government-assigned invoice ID. This object contains this identifier, along with the type of transaction (wh"""
    country_code: Optional["countryCode"] = Field(None, alias="countryCode")
    government_document_s3_link: Optional[str] = Field(None, alias="governmentDocumentS3Link", description="PreSigned URL to grant time-limited download access for govt invoice pdf")
    government_invoice_id: Optional[str] = Field(None, alias="governmentInvoiceId", description="Government generated ID")
    government_xml_document_s3_link: Optional[str] = Field(None, alias="governmentXmlDocumentS3Link", description="PreSigned URL to grant time-limited download access for govt invoice XML")
    transaction_type: Optional[governmentInvoiceInformationTransactiontype] = Field(None, alias="transactionType")

    model_config = {'populate_by_name': True}


class invoiceLineCosteventtype(StrEnum):
    CLICKS = "CLICKS"
    IMPRESSIONS = "IMPRESSIONS"


class invoiceLinePricetype(StrEnum):
    CPC = "CPC"
    CPM = "CPM"
    FIXED_PRICE = "FIXED_PRICE"


class invoiceLine(BaseModel):
    campaign_id: Optional[int] = Field(None, alias="campaignId")
    campaign_name: Optional[str] = Field(None, alias="campaignName")
    campaign_tags: Optional[dict[str, str]] = Field(None, alias="campaignTags", description="Campaign tags in the form of string key-value pairs.")
    commission_amount: Optional["currencyAmount"] = Field(None, alias="commissionAmount")
    commission_rate: Optional[float] = Field(None, alias="commissionRate")
    cost: "currencyAmount"
    cost_event_count: int = Field(..., alias="costEventCount", description="Number of clicks/impressions charged")
    cost_event_type: invoiceLineCosteventtype = Field(..., alias="costEventType", description="Type of event charged (clicks or impressions)")
    cost_per_event_type: Optional[float] = Field(None, alias="costPerEventType", description="Ad spends cost (Cost exclusive of adjustments/promotions/fees/etc) per unit (thousand impressions/clicks).")
    cost_per_unit: float = Field(..., alias="costPerUnit")
    fees: Optional[list["fee"]] = Field(None, description="Charges can include different fees (see feeType below).")
    name: str
    portfolio_id: Optional[int] = Field(None, alias="portfolioId", description="Sponsored Ads only. This identifier maps to one of the portfolios listed in the portfolios section.")
    price_type: invoiceLinePricetype = Field(..., alias="priceType", description="Metric used for performance measurement.")
    program_name: Optional["adProgram"] = Field(None, alias="programName")
    promotion_amount: Optional["currencyAmount"] = Field(None, alias="promotionAmount")
    purchase_order_number: Optional[str] = Field(None, alias="purchaseOrderNumber")
    supply_cost: Optional["currencyAmount"] = Field(None, alias="supplyCost")

    model_config = {'populate_by_name': True}


class invoiceLines(BaseModel):
    """Line items for this invoice. For Sponsored Ads, this will be a per-campaign breakdown of charges. For DSP, this will be the line items for the campaign getting invoiced."""
    pass


class portfolio(BaseModel):
    fee_amount: Optional["currencyAmount"] = Field(None, alias="feeAmount")
    id_: int = Field(..., alias="id")
    name: str
    total_amount: "currencyAmount" = Field(..., alias="totalAmount")

    model_config = {'populate_by_name': True}


class portfolios(BaseModel):
    """Sponsored Ads only. This is a list of portfolios with their name, ID and the total cost of the campaign(s) they contain. This totalAmount corresponds to the sum of the invoice lines tagged with the ID"""
    pass


class taxBreakupIssuertaxinformation(BaseModel):
    tax_id: str = Field(..., alias="taxId", description="Tax registration with government (Ex: VAT ID, GST ID)")

    model_config = {'populate_by_name': True}


class taxBreakupPayertaxinformation(BaseModel):
    tax_id: Optional[str] = Field(None, alias="taxId", description="Tax registration with government (Ex: VAT ID, GST ID)")

    model_config = {'populate_by_name': True}


class taxBreakupThirdpartytaxinformation(BaseModel):
    tax_id: str = Field(..., alias="taxId", description="Tax registration with government (Ex: VAT ID, GST ID)")

    model_config = {'populate_by_name': True}


class taxBreakup(BaseModel):
    issuer_jurisdiction: str = Field(..., alias="issuerJurisdiction", description="Tax jurisdiction of issuer (Amazon billing entity)")
    issuer_tax_information: "taxBreakupIssuertaxinformation" = Field(..., alias="issuerTaxInformation")
    payer_jurisdiction: Optional[str] = Field(None, alias="payerJurisdiction", description="Tax jurisdiction of payer (billed customer)")
    payer_tax_information: "taxBreakupPayertaxinformation" = Field(..., alias="payerTaxInformation")
    tax_amount: "currencyAmount" = Field(..., alias="taxAmount")
    tax_name: str = Field(..., alias="taxName")
    tax_rate: float = Field(..., alias="taxRate")
    taxed_jurisdiction_name: str = Field(..., alias="taxedJurisdictionName", description="Tax jurisdiction for which tax applies, this can be at the country, state or local level.")
    third_party_tax_information: Optional["taxBreakupThirdpartytaxinformation"] = Field(None, alias="thirdPartyTaxInformation")

    model_config = {'populate_by_name': True}


class taxDetail(BaseModel):
    permanent_account_number: Optional[str] = Field(None, alias="permanentAccountNumber", description="**IN only** field that represents the tax account number of the billed entity entered on AMS portal.")
    tax_breakups: list["taxBreakup"] = Field(..., alias="taxBreakups", description="List of taxes applied on the transaction for this invoice.")
    tax_calculation_date: "date" = Field(..., alias="taxCalculationDate")

    model_config = {'populate_by_name': True}


class paymentMethod(StrEnum):
    CREDIT_CARD = "CREDIT_CARD"
    DEDUCT_FROM_PAYMENT = "DEDUCT_FROM_PAYMENT"
    DIRECT_DEBIT = "DIRECT_DEBIT"
    ELECTRONIC_FUNDS_TRANSFER = "ELECTRONIC_FUNDS_TRANSFER"
    PREPAY = "PREPAY"
    UNIFIED_BILLING = "UNIFIED_BILLING"


class paymentStatus(StrEnum):
    FAILED = "FAILED"
    PROCESSING = "PROCESSING"
    REFUNDED = "REFUNDED"
    SUCCEEDED = "SUCCEEDED"
    VERIFICATION_REQUIRED = "VERIFICATION_REQUIRED"
    VOIDED = "VOIDED"


class payment(BaseModel):
    amount: "currencyAmount"
    current_payment_attempt_date: Optional["date"] = Field(None, alias="currentPaymentAttemptDate")
    id_: int = Field(..., alias="id")
    last_payment_attempt_date: Optional["date"] = Field(None, alias="lastPaymentAttemptDate")
    next_payment_attempt_date: Optional["date"] = Field(None, alias="nextPaymentAttemptDate")
    payment_method: "paymentMethod" = Field(..., alias="paymentMethod")
    reason: Optional[str] = Field(None, description="Provides additional details and reason for the payment status")
    refunded_amount: Optional["currencyAmount"] = Field(None, alias="refundedAmount")
    status: paymentStatus

    model_config = {'populate_by_name': True}


class payments(BaseModel):
    """List of payments made against the invoice."""
    pass


class invoiceStatus(StrEnum):
    ACCUMULATING = "ACCUMULATING"
    ISSUED = "ISSUED"
    PAID_IN_FULL = "PAID_IN_FULL"
    PAID_IN_PART = "PAID_IN_PART"
    PROCESSING = "PROCESSING"
    WRITTEN_OFF = "WRITTEN_OFF"


class invoiceSummaryPaymenttermstype(StrEnum):
    EOM = "EOM"
    NET = "NET"


class invoiceSummary(BaseModel):
    amount_due: "currencyAmount" = Field(..., alias="amountDue")
    billing_aggregation: Optional["billingAggregation"] = Field(None, alias="billingAggregation")
    downloadable_documents: Optional[list["documentType"]] = Field(None, alias="downloadableDocuments", description="List of downloadable documents associated with this invoice and accessible from the advertising console.")
    due_date: Optional["date"] = Field(None, alias="dueDate")
    fees: Optional[list["fee"]] = Field(None, description="Regulatory Advertising Fees.")
    from_date: "date" = Field(..., alias="fromDate")
    id_: str = Field(..., alias="id")
    invoice_date: "date" = Field(..., alias="invoiceDate")
    payment_method: Optional["paymentMethod"] = Field(None, alias="paymentMethod")
    payment_terms_days: Optional[int] = Field(None, alias="paymentTermsDays")
    payment_terms_type: Optional[invoiceSummaryPaymenttermstype] = Field(None, alias="paymentTermsType")
    purchase_order_number: Optional[str] = Field(None, alias="purchaseOrderNumber")
    remaining_amount_due: "currencyAmount" = Field(..., alias="remainingAmountDue")
    remaining_fees: Optional[list["fee"]] = Field(None, alias="remainingFees", description="Remaining Regulatory Advertising Fees.")
    remaining_tax_amount_due: Optional["currencyAmount"] = Field(None, alias="remainingTaxAmountDue")
    status: "invoiceStatus"
    tax_amount_due: Optional["currencyAmount"] = Field(None, alias="taxAmountDue")
    tax_rate: Optional[float] = Field(None, alias="taxRate")
    to_date: "date" = Field(..., alias="toDate")

    model_config = {'populate_by_name': True}


class thirdPartyContactInformation(BaseModel):
    """Additional contacts. This field is used in cases such as Loi Sapin in France where both advertiser and agency addresses need to be provided."""
    pass


class promotion(BaseModel):
    amount: "currencyAmount"
    description: str
    last_consumed_date: "date" = Field(..., alias="lastConsumedDate")

    model_config = {'populate_by_name': True}


class promotions(BaseModel):
    """List of promotions applied to the charges in this invoice."""
    pass


class invoice(BaseModel):
    adjustments: "adjustments"
    government_invoice_information: Optional["governmentInvoiceInformation"] = Field(None, alias="governmentInvoiceInformation")
    invoice_lines: "invoiceLines" = Field(..., alias="invoiceLines")
    invoice_summary: "invoiceSummary" = Field(..., alias="invoiceSummary")
    issuer_contact_info: "contactInfo" = Field(..., alias="issuerContactInfo")
    payer_contact_info: "contactInfo" = Field(..., alias="payerContactInfo")
    payments: "payments"
    portfolios: "portfolios"
    promotions: "promotions"
    tax_detail: "taxDetail" = Field(..., alias="taxDetail")
    third_party_contact_info: "thirdPartyContactInformation" = Field(..., alias="thirdPartyContactInfo")

    model_config = {'populate_by_name': True}

