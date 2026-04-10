"""Auto-generated Pydantic models. Do not edit manually.

Source: Billing_prod_3p.json
Title:  Billing
"""

from __future__ import annotations

from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field



class date(BaseModel):
    """Date in YYYYMMDD format"""
    pass


class countryCode(BaseModel):
    """ISO 3611 country code"""
    pass


class currencyCode(StrEnum):
    USD = "USD"
    CAD = "CAD"
    MXN = "MXN"
    BRL = "BRL"
    GBP = "GBP"
    EUR = "EUR"
    AED = "AED"
    SAR = "SAR"
    INR = "INR"
    JPY = "JPY"
    AUD = "AUD"
    SGD = "SGD"
    TRY = "TRY"
    SEK = "SEK"
    EGP = "EGP"
    PLN = "PLN"


class currencyAmount(BaseModel):
    amount: Optional[float] = None
    currency_code: Optional["currencyCode"] = Field(None, alias="currencyCode")

    model_config = {'populate_by_name': True}


class feeFeeidentifiers(BaseModel):
    """Identifiers describing attributes for different fee types. * countryCode: ISO 3611 country code for country specific Regulatory Advertising Fees."""
    country_code: Optional["countryCode"] = Field(None, alias="countryCode")

    model_config = {'populate_by_name': True}


class feeFeetype(StrEnum):
    AUDIENCE_FEE = "AUDIENCE_FEE"
    V_3P_AUTO_NON_ABSORBED_FEE = "3P_AUTO_NON_ABSORBED_FEE"
    V_3P_NON_ABSORBED_FEE = "3P_NON_ABSORBED_FEE"
    PLATFORM_FEE = "PLATFORM_FEE"
    OMNICHANNEL_METRICS_FEE = "OMNICHANNEL_METRICS_FEE"
    REGULATORY_ADVERTISING_FEE = "REGULATORY_ADVERTISING_FEE"
    V_3P_PREBID_FEE = "3P_PREBID_FEE"


class fee(BaseModel):
    cost: "currencyAmount"
    fee_identifiers: Optional["feeFeeidentifiers"] = Field(None, alias="feeIdentifiers", description="Identifiers describing attributes for different fee types. * countryCode: ISO 3611 country code for country specific Reg")
    fee_type: feeFeetype = Field(..., alias="feeType", description="* `PLATFORM_FEE`: Billable fee set at the Rodeo Entity level by internal users which reflects the cost of using the Amaz")

    model_config = {'populate_by_name': True}


class fees(BaseModel):
    pass


class adjustment(BaseModel):
    amount: "currencyAmount"
    accounting_date: "date" = Field(..., alias="accountingDate")
    fees: Optional[list["fee"]] = Field(None, description="Charges can include different fees (see feeType below).")
    comments: Optional[str] = None
    portfolio_id: Optional[int] = Field(None, alias="portfolioId", description="Sponsored Ads only. This identifier maps to one of the portfolios listed in the portfolios section.")

    model_config = {'populate_by_name': True}


class adjustments(BaseModel):
    """List of adjustments (positive and negative) applied to this invoice."""
    pass


class email(BaseModel):
    email_address: str = Field(..., alias="emailAddress")
    display_name: str = Field(..., alias="displayName", description="Customer name used in email communication.")

    model_config = {'populate_by_name': True}


class address(BaseModel):
    state_or_region: str = Field(..., alias="stateOrRegion")
    attention_name: Optional[str] = Field(None, alias="attentionName")
    city: str
    country_code: "countryCode" = Field(..., alias="countryCode")
    company_name: str = Field(..., alias="companyName")
    postal_code: str = Field(..., alias="postalCode")
    address_line1: str = Field(..., alias="addressLine1")
    address_line2: str = Field(..., alias="addressLine2")
    address_line3: str = Field(..., alias="addressLine3")

    model_config = {'populate_by_name': True}


class contactInfo(BaseModel):
    address: "address"
    email: "email"

    model_config = {'populate_by_name': True}


class paymentMethod(StrEnum):
    CREDIT_CARD = "CREDIT_CARD"
    ELECTRONIC_FUNDS_TRANSFER = "ELECTRONIC_FUNDS_TRANSFER"
    DEDUCT_FROM_PAYMENT = "DEDUCT_FROM_PAYMENT"
    UNIFIED_BILLING = "UNIFIED_BILLING"
    DIRECT_DEBIT = "DIRECT_DEBIT"
    PREPAY = "PREPAY"


class invoiceStatus(StrEnum):
    ACCUMULATING = "ACCUMULATING"
    PROCESSING = "PROCESSING"
    ISSUED = "ISSUED"
    PAID_IN_PART = "PAID_IN_PART"
    PAID_IN_FULL = "PAID_IN_FULL"
    WRITTEN_OFF = "WRITTEN_OFF"


class documentType(StrEnum):
    INVOICE = "INVOICE"
    CREDIT_NOTE = "CREDIT_NOTE"


class invoiceSummaryPaymenttermstype(StrEnum):
    EOM = "EOM"
    NET = "NET"


class invoiceSummary(BaseModel):
    fees: Optional[list["fee"]] = Field(None, description="Regulatory Advertising Fees.")
    payment_terms_days: Optional[int] = Field(None, alias="paymentTermsDays")
    tax_amount_due: Optional["currencyAmount"] = Field(None, alias="taxAmountDue")
    remaining_tax_amount_due: Optional["currencyAmount"] = Field(None, alias="remainingTaxAmountDue")
    remaining_fees: Optional[list["fee"]] = Field(None, alias="remainingFees", description="Remaining Regulatory Advertising Fees.")
    to_date: "date" = Field(..., alias="toDate")
    due_date: Optional["date"] = Field(None, alias="dueDate")
    invoice_date: "date" = Field(..., alias="invoiceDate")
    remaining_amount_due: "currencyAmount" = Field(..., alias="remainingAmountDue")
    from_date: "date" = Field(..., alias="fromDate")
    amount_due: "currencyAmount" = Field(..., alias="amountDue")
    tax_rate: Optional[float] = Field(None, alias="taxRate")
    purchase_order_number: Optional[str] = Field(None, alias="purchaseOrderNumber")
    payment_terms_type: Optional[invoiceSummaryPaymenttermstype] = Field(None, alias="paymentTermsType")
    payment_method: Optional["paymentMethod"] = Field(None, alias="paymentMethod")
    id_: str = Field(..., alias="id")
    downloadable_documents: Optional[list["documentType"]] = Field(None, alias="downloadableDocuments", description="List of downloadable documents associated with this invoice and accessible from the advertising console.")
    status: "invoiceStatus"

    model_config = {'populate_by_name': True}


class paymentStatus(StrEnum):
    PROCESSING = "PROCESSING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    VERIFICATION_REQUIRED = "VERIFICATION_REQUIRED"
    REFUNDED = "REFUNDED"
    VOIDED = "VOIDED"


class payment(BaseModel):
    next_payment_attempt_date: Optional["date"] = Field(None, alias="nextPaymentAttemptDate")
    reason: Optional[str] = Field(None, description="Provides additional details and reason for the payment status")
    amount: "currencyAmount"
    payment_method: "paymentMethod" = Field(..., alias="paymentMethod")
    current_payment_attempt_date: Optional["date"] = Field(None, alias="currentPaymentAttemptDate")
    id_: int = Field(..., alias="id")
    last_payment_attempt_date: Optional["date"] = Field(None, alias="lastPaymentAttemptDate")
    refunded_amount: Optional["currencyAmount"] = Field(None, alias="refundedAmount")
    status: paymentStatus

    model_config = {'populate_by_name': True}


class payments(BaseModel):
    """List of payments made against the invoice."""
    pass


class adProgram(StrEnum):
    SPONSORED_PRODUCT = "SPONSORED PRODUCT"
    SPONSORED_BRANDS = "SPONSORED BRANDS"
    SPONSORED_DISPLAY = "SPONSORED DISPLAY"
    SPONSORED_DISPLAY_FOR_FIRE_TV = "SPONSORED DISPLAY FOR FIRE TV"
    CREATOR_CONNECTIONS = "CREATOR CONNECTIONS"
    AMAZON_LIVE = "AMAZON LIVE"


class taxBreakupIssuertaxinformation(BaseModel):
    tax_id: str = Field(..., alias="taxId", description="Tax registration with government (Ex: VAT ID, GST ID)")

    model_config = {'populate_by_name': True}


class taxBreakupThirdpartytaxinformation(BaseModel):
    tax_id: str = Field(..., alias="taxId", description="Tax registration with government (Ex: VAT ID, GST ID)")

    model_config = {'populate_by_name': True}


class taxBreakupPayertaxinformation(BaseModel):
    tax_id: Optional[str] = Field(None, alias="taxId", description="Tax registration with government (Ex: VAT ID, GST ID)")

    model_config = {'populate_by_name': True}


class taxBreakup(BaseModel):
    payer_jurisdiction: Optional[str] = Field(None, alias="payerJurisdiction", description="Tax jurisdiction of payer (billed customer)")
    tax_rate: float = Field(..., alias="taxRate")
    issuer_tax_information: "taxBreakupIssuertaxinformation" = Field(..., alias="issuerTaxInformation")
    third_party_tax_information: Optional["taxBreakupThirdpartytaxinformation"] = Field(None, alias="thirdPartyTaxInformation")
    issuer_jurisdiction: str = Field(..., alias="issuerJurisdiction", description="Tax jurisdiction of issuer (Amazon billing entity)")
    payer_tax_information: "taxBreakupPayertaxinformation" = Field(..., alias="payerTaxInformation")
    tax_amount: "currencyAmount" = Field(..., alias="taxAmount")
    tax_name: str = Field(..., alias="taxName")
    taxed_jurisdiction_name: str = Field(..., alias="taxedJurisdictionName", description="Tax jurisdiction for which tax applies, this can be at the country, state or local level.")

    model_config = {'populate_by_name': True}


class taxDetail(BaseModel):
    permanent_account_number: Optional[str] = Field(None, alias="permanentAccountNumber", description="**IN only** field that represents the tax account number of the billed entity entered on AMS portal.")
    tax_calculation_date: "date" = Field(..., alias="taxCalculationDate")
    tax_breakups: list["taxBreakup"] = Field(..., alias="taxBreakups", description="List of taxes applied on the transaction for this invoice.")

    model_config = {'populate_by_name': True}


class paymentDetailStatus(StrEnum):
    PENDING = "PENDING"
    BOUNCED = "BOUNCED"
    VOIDED = "VOIDED"
    SUCCESSFUL = "SUCCESSFUL"


class paymentDetail(BaseModel):
    amount: "currencyAmount"
    payment_method: Optional["paymentMethod"] = Field(None, alias="paymentMethod")
    received_date: "date" = Field(..., alias="receivedDate")
    status: paymentDetailStatus

    model_config = {'populate_by_name': True}


class invoiceLineCosteventtype(StrEnum):
    CLICKS = "CLICKS"
    IMPRESSIONS = "IMPRESSIONS"


class invoiceLinePricetype(StrEnum):
    CPC = "CPC"
    CPM = "CPM"


class invoiceLine(BaseModel):
    campaign_tags: Optional[dict[str, str]] = Field(None, alias="campaignTags", description="Campaign tags in the form of string key-value pairs.")
    cost_event_type: invoiceLineCosteventtype = Field(..., alias="costEventType", description="Type of event charged (clicks or impressions)")
    commission_rate: Optional[float] = Field(None, alias="commissionRate")
    fees: Optional[list["fee"]] = Field(None, description="Charges can include different fees (see feeType below).")
    cost: "currencyAmount"
    campaign_id: Optional[int] = Field(None, alias="campaignId")
    price_type: invoiceLinePricetype = Field(..., alias="priceType", description="Metric used for performance measurement.")
    supply_cost: Optional["currencyAmount"] = Field(None, alias="supplyCost")
    portfolio_id: Optional[int] = Field(None, alias="portfolioId", description="Sponsored Ads only. This identifier maps to one of the portfolios listed in the portfolios section.")
    cost_per_event_type: Optional[float] = Field(None, alias="costPerEventType", description="Ad spends cost (Cost exclusive of adjustments/promotions/fees/etc) per unit (thousand impressions/clicks).")
    program_name: Optional["adProgram"] = Field(None, alias="programName")
    cost_event_count: int = Field(..., alias="costEventCount", description="Number of clicks/impressions charged")
    purchase_order_number: Optional[str] = Field(None, alias="purchaseOrderNumber")
    name: str
    campaign_name: Optional[str] = Field(None, alias="campaignName")
    promotion_amount: Optional["currencyAmount"] = Field(None, alias="promotionAmount")
    cost_per_unit: float = Field(..., alias="costPerUnit")
    commission_amount: Optional["currencyAmount"] = Field(None, alias="commissionAmount")

    model_config = {'populate_by_name': True}


class invoiceLines(BaseModel):
    """Line items for this invoice. For Sponsored Ads, this will be a per-campaign breakdown of charges. For DSP, this will be the line items for the campaign getting invoiced."""
    pass


class portfolio(BaseModel):
    total_amount: "currencyAmount" = Field(..., alias="totalAmount")
    fee_amount: Optional["currencyAmount"] = Field(None, alias="feeAmount")
    name: str
    id_: int = Field(..., alias="id")

    model_config = {'populate_by_name': True}


class governmentInvoiceInformationTransactiontype(StrEnum):
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"


class governmentInvoiceInformation(BaseModel):
    """Government invoice data is provided in marketplaces (such as Italy or India) that require a government-assigned invoice ID. This object contains this identifier, along with the type of transaction (wh"""
    transaction_type: Optional[governmentInvoiceInformationTransactiontype] = Field(None, alias="transactionType")
    country_code: Optional["countryCode"] = Field(None, alias="countryCode")
    government_document_s3_link: Optional[str] = Field(None, alias="governmentDocumentS3Link", description="PreSigned URL to grant time-limited download access for govt invoice pdf")
    government_xml_document_s3_link: Optional[str] = Field(None, alias="governmentXmlDocumentS3Link", description="PreSigned URL to grant time-limited download access for govt invoice XML")
    government_invoice_id: Optional[str] = Field(None, alias="governmentInvoiceId", description="Government generated ID")

    model_config = {'populate_by_name': True}


class portfolios(BaseModel):
    """Sponsored Ads only. This is a list of portfolios with their name, ID and the total cost of the campaign(s) they contain. This totalAmount corresponds to the sum of the invoice lines tagged with the ID"""
    pass


class promotion(BaseModel):
    last_consumed_date: "date" = Field(..., alias="lastConsumedDate")
    amount: "currencyAmount"
    description: str

    model_config = {'populate_by_name': True}


class promotions(BaseModel):
    """List of promotions applied to the charges in this invoice."""
    pass


class thirdPartyContactInformation(BaseModel):
    """Additional contacts. This field is used in cases such as Loi Sapin in France where both advertiser and agency addresses need to be provided."""
    pass


class invoice(BaseModel):
    promotions: "promotions"
    government_invoice_information: Optional["governmentInvoiceInformation"] = Field(None, alias="governmentInvoiceInformation")
    payer_contact_info: "contactInfo" = Field(..., alias="payerContactInfo")
    tax_detail: "taxDetail" = Field(..., alias="taxDetail")
    adjustments: "adjustments"
    invoice_lines: "invoiceLines" = Field(..., alias="invoiceLines")
    invoice_summary: "invoiceSummary" = Field(..., alias="invoiceSummary")
    issuer_contact_info: "contactInfo" = Field(..., alias="issuerContactInfo")
    third_party_contact_info: "thirdPartyContactInformation" = Field(..., alias="thirdPartyContactInfo")
    payments: "payments"
    portfolios: "portfolios"

    model_config = {'populate_by_name': True}

