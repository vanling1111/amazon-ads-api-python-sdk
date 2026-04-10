"""Auto-generated Pydantic models. Do not edit manually.

Source: Localization_prod_3p.json
Title:  Localization
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class LocalizationCurrency(BaseModel):
    """A currency to be localized."""
    amount: float

    model_config = {'populate_by_name': True}


class LocalizationCurrencyRequestCurrencycode(StrEnum):
    USD = "USD"


class LocalizationCurrencyRequest(BaseModel):
    """LocalizationCurrencyRequest Object."""
    currency: "LocalizationCurrency"
    currency_code: Optional[LocalizationCurrencyRequestCurrencycode] = Field(None, alias="currencyCode", description="A three-letter currency code with enum value corresponding to ISO-4217 code.")

    model_config = {'populate_by_name': True}


class LocalizationCurrencyResponseStatus(StrEnum):
    ERROR = "ERROR"
    SUCCESS = "SUCCESS"


class LocalizationCurrencyResponse(BaseModel):
    """LocalizationCurrencyResponse Object."""
    error_code: Optional[str] = Field(None, alias="errorCode", description="If status is ERROR, the error code.")
    localized_currencies: dict[str, "LocalizationCurrency"] = Field(..., alias="localizedCurrencies", description="A map from target marketplace ID (string) to localized monetary amount.")
    status: LocalizationCurrencyResponseStatus = Field(..., description="If SUCCESS, do not retry. If ERROR, may retry.")

    model_config = {'populate_by_name': True}


class LocalizationCurrencyResultStatus(StrEnum):
    ERROR = "ERROR"
    FAILURE = "FAILURE"
    SUCCESS = "SUCCESS"


class LocalizationCurrencyResult(BaseModel):
    """LocalizationCurrencyResult Object."""
    error_code: Optional[str] = Field(None, alias="errorCode", description="If status is ERROR, the error code. Not present if status is SUCCESS.")
    localized_currency: "LocalizationCurrency" = Field(..., alias="localizedCurrency")
    messages: Optional[list[str]] = Field(None, description="If present, contains one or more strings describing why products could not be localized. For manual diagnostic use.")
    status: LocalizationCurrencyResultStatus = Field(..., description="If SUCCESS, FAILURE, do not retry. If ERROR, may retry.")

    model_config = {'populate_by_name': True}


class LocalizationCurrencyResponseV2Status(StrEnum):
    ERROR = "ERROR"
    FAILURE = "FAILURE"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"
    SUCCESS = "SUCCESS"


class LocalizationCurrencyResponseV2(BaseModel):
    """LocalizationCurrencyResponse Object."""
    error_code: Optional[str] = Field(None, alias="errorCode", description="If status is ERROR, the error code. Not present if status is SUCCESS.")
    localized_currency_results: dict[str, "LocalizationCurrencyResult"] = Field(..., alias="localizedCurrencyResults", description="A map from target marketplace ID (country code) (string) to details regarding the localization status and messages.")
    source_currency: "LocalizationCurrency" = Field(..., alias="sourceCurrency")
    status: LocalizationCurrencyResponseV2Status = Field(..., description="If SUCCESS, PARTIAL_SUCCESS, or FAILURE, do not retry. If ERROR, may retry.")

    model_config = {'populate_by_name': True}


class LocalizationKeyword(BaseModel):
    """An object containing information about a keyword."""
    keyword: str = Field(..., description="The keyword string.")

    model_config = {'populate_by_name': True}


class LocalizationKeywordRequest(BaseModel):
    """A LocalizationKeywordRequest object. Contains information needed about the keyword to be localized."""
    localization_keyword: dict[str, "LocalizationKeyword"] = Field(..., alias="localizationKeyword", description="A keyword to be localized.")

    model_config = {'populate_by_name': True}


class LocalizationKeywordResponseStatus(StrEnum):
    ERROR = "ERROR"
    SUCCESS = "SUCCESS"


class LocalizationKeywordResponse(BaseModel):
    """A LocalizationKeywordResponse object. Contains localized keywords in the various target marketplaces/locales."""
    error_code: Optional[str] = Field(None, alias="errorCode", description="If status is ERROR, the error code. Not present if status is SUCCESS.")
    localized_keywords: Optional[dict[str, "LocalizationKeyword"]] = Field(None, alias="localizedKeywords", description="Key (string): target marketplace ID. Value (LocalizationKeyword): localized keyword. If the source keyword cannot be tra")
    status: LocalizationKeywordResponseStatus = Field(..., description="If SUCCESS, do not retry. If ERROR, may retry.")

    model_config = {'populate_by_name': True}


class LocalizationKeywordResultStatus(StrEnum):
    ERROR = "ERROR"
    FAILURE = "FAILURE"
    SUCCESS = "SUCCESS"


class LocalizationKeywordResult(BaseModel):
    """LocalizationKeywordResult Object."""
    error_code: Optional[str] = Field(None, alias="errorCode", description="If status is ERROR or FAILURE, the error code.")
    localized_keyword: "LocalizationKeyword" = Field(..., alias="localizedKeyword")
    messages: Optional[list[str]] = Field(None, description="If present, contains one or more strings describing why products could not be localized. For manual diagnostic use.")
    status: LocalizationKeywordResultStatus = Field(..., description="If SUCCESS, FAILURE, do not retry. If ERROR, may retry.")

    model_config = {'populate_by_name': True}


class LocalizationKeywordResponseV2Status(StrEnum):
    ERROR = "ERROR"
    FAILURE = "FAILURE"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"
    SUCCESS = "SUCCESS"


class LocalizationKeywordResponseV2(BaseModel):
    """A LocalizationKeywordResponse object. Contains localized keywords in the various target marketplaces/locales."""
    error_code: Optional[str] = Field(None, alias="errorCode", description="If status is ERROR, the error code. Not present if status is SUCCESS.")
    localized_keyword_results: dict[str, "LocalizationKeywordResult"] = Field(..., alias="localizedKeywordResults", description="A map from target marketplace ID / locale / countryCode to details regarding the localization status and messages.")
    source_keyword: Optional[Any] = Field(None, alias="sourceKeyword", description="Source keyword that was localized.")
    status: LocalizationKeywordResponseV2Status = Field(..., description="If SUCCESS, PARTIAL_SUCCESS or FAILURE, do not retry. If ERROR, may retry.")

    model_config = {'populate_by_name': True}


class LocalizationKeywordSourceDetails(BaseModel):
    """The source details for the LocalizationKeywordRequests. One of locale, marketplaceId, or countryCode has to be present. If locale is present, the content of marketplaceIds or countryCode is ignored."""
    country_code: Optional[str] = Field(None, alias="countryCode", description="A two-letter country code. When locale or marketplaceId is present, countryCode is ignored. Please refer to the table ab")
    locale: Optional[str] = Field(None, description="The source locale. For example, if the caller is localizing keywords from British English (en_GB) to Simplified Chinese ")
    marketplace_id: Optional[str] = Field(None, alias="marketplaceId", description="The ID of the source marketplace. For example, if the caller is an advertiser based in the UK (marketplace ID A1F83G8C2A")

    model_config = {'populate_by_name': True}


class LocalizationKeywordTargetDetails(BaseModel):
    """The target details for the LocalizationKeywordRequests. One of locales, countryCode, or marketplaceIds must be present. If locale is present, the content of marketplaceIds and countryCodes is ignored."""
    country_codes: Optional[list[str]] = Field(None, alias="countryCodes", description="A list of two-letter country codes. When another form of locale (marketplaceId or locale) is present, countryCode is ign")
    locales: Optional[list[str]] = Field(None, description="The target locales (locales to which the caller wishes to localize the specified keywords). For example, if the caller i")
    marketplace_ids: Optional[list[str]] = Field(None, alias="marketplaceIds", description="The IDs of target marketplaces (marketplaces in which the caller wishes to localize the specified keywords). For example")

    model_config = {'populate_by_name': True}


class LocalizationProduct(BaseModel):
    """A product to be localized."""
    asin: Optional[str] = Field(None, description="The product's Amazon Standard Identification Number. Required for entityType=KDP_AUTHOR and entityType=VENDOR. If caller")
    sku: Optional[str] = Field(None, description="The product's Stock Keeping Unit. Required for entityType=SELLER. If caller's entityType is KDP_AUTHOR or VENDOR, this f")

    model_config = {'populate_by_name': True}


class LocalizationProductRequest(BaseModel):
    product: "LocalizationProduct"

    model_config = {'populate_by_name': True}


class LocalizationProductResponseStatus(StrEnum):
    ERROR = "ERROR"
    SUCCESS = "SUCCESS"


class LocalizationProductResponse(BaseModel):
    error_code: Optional[str] = Field(None, alias="errorCode", description="If the status is ERROR, the error code. Not present if the status is SUCCESS.")
    localized_products: dict[str, "LocalizationProduct"] = Field(..., alias="localizedProducts", description="Key (string): target marketplace ID. Value (LocalizationProduct): localized product. If no localized product is availabl")
    status: LocalizationProductResponseStatus = Field(..., description="If SUCCESS, do not retry. If ERROR, may retry.")

    model_config = {'populate_by_name': True}


class ProductMetadataCatalogsourcecountrycode(StrEnum):
    AE = "AE"
    DE = "DE"
    JP = "JP"
    UK = "UK"
    US = "US"


class ProductMetadata(BaseModel):
    """This represents the metadata associated with the product."""
    catalog_source_country_code: Optional[ProductMetadataCatalogsourcecountrycode] = Field(None, alias="catalogSourceCountryCode", description="This field will be present for Global Store business where it represents the country code of source marketplace where se")

    model_config = {'populate_by_name': True}


class LocalizationProductResultMatchtype(StrEnum):
    GLOBAL_STORE = "GLOBAL_STORE"
    LOCAL = "LOCAL"


class LocalizationProductResultStatus(StrEnum):
    ERROR = "ERROR"
    FAILURE = "FAILURE"
    SUCCESS = "SUCCESS"


class LocalizationProductResult(BaseModel):
    """Information regarding how a product was localized, or how a product was not localized in this particular marketplace."""
    error_code: Optional[str] = Field(None, alias="errorCode", description="If the status is ERROR, the error code. Not present if the status is SUCCESS.")
    localized_product: "LocalizationProduct" = Field(..., alias="localizedProduct")
    match_type: Optional[LocalizationProductResultMatchtype] = Field(None, alias="matchType", description="This represents the type of match for a localized product. LOCAL: It represents the product selling by an advertiser loc")
    messages: Optional[list[str]] = Field(None, description="If present, contains one or more strings describing why products could not be localized. For manual diagnostic use.")
    product_metadata: Optional["ProductMetadata"] = Field(None, alias="productMetadata")
    status: LocalizationProductResultStatus = Field(..., description="The status of the localization operation.  SUCCESS: The product was localized successfully for this marketplace. FAILURE")

    model_config = {'populate_by_name': True}


class LocalizationProductResponseV2Status(StrEnum):
    ERROR = "ERROR"
    FAILURE = "FAILURE"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"
    SUCCESS = "SUCCESS"


class LocalizationProductResponseV2(BaseModel):
    error_code: Optional[str] = Field(None, alias="errorCode", description="If the status is ERROR, the error code. Not present if the status is SUCCESS.")
    localized_product_results: dict[str, "LocalizationProductResult"] = Field(..., alias="localizedProductResults", description="Key (string): target marketplace ID. Value (LocalizationProductResult): localized product results. Information regarding")
    source_product: "LocalizationProduct" = Field(..., alias="sourceProduct")
    status: LocalizationProductResponseV2Status = Field(..., description="If SUCCESS, PARTIAL_SUCCESS or FAILURE, do not retry. If ERROR, may retry.")

    model_config = {'populate_by_name': True}


class LocalizationProductTargetDetails(BaseModel):
    """The target details for the LocalizationProductRequests. There must be only one target details object per marketplace ID. The advertiser ID may be repeated across target details objects. The order of t"""
    advertiser_id: str = Field(..., alias="advertiserId", description="The advertiser ID of the caller in the associated target marketplace. The ID of the source advertiser account. This may ")
    country_code: Optional[str] = Field(None, alias="countryCode", description="A two-letter country code. When both marketplaceId and countryCode are present, countryCode is ignored. Please refer to ")
    marketplace_id: Optional[str] = Field(None, alias="marketplaceId", description="The ID of a target marketplace (a marketplace in which the caller wishes to localize the specified products). For exampl")

    model_config = {'populate_by_name': True}


class LocalizationTargetingExpressionPredicateType(BaseModel):
    """Targeting predicate type. The following predicate types are supported: | Type | Description | Data in `value` String | | --- | --- | --- | | `asinCategorySameAs` | Target the specified category. | Int"""
    pass


class LocalizationTargetingExpressionPredicate(BaseModel):
    """A targeting expression predicate."""
    type_: "LocalizationTargetingExpressionPredicateType" = Field(..., alias="type")
    value: str = Field(..., description="The value of the predicate. Targeting expression syntax, including examples of predicates and the values they support, i")

    model_config = {'populate_by_name': True}


class LocalizationTargetingExpression(BaseModel):
    """A targeting expression composed of one or more predicates."""
    expression: list["LocalizationTargetingExpressionPredicate"] = Field(..., description="The predicates forming the targeting expression.")
    is_for_negative_targeting: bool = Field(..., alias="isForNegativeTargeting", description="Specifies whether the expression is for positive targeting (false) or negative targeting (true).")

    model_config = {'populate_by_name': True}


class LocalizationTargetingExpressionRequest(BaseModel):
    """A request to localize a targeting expression from a source marketplace to one or more target marketplaces."""
    targeting_expression: "LocalizationTargetingExpression" = Field(..., alias="targetingExpression")

    model_config = {'populate_by_name': True}


class LocalizationTargetingExpressionResultStatus(StrEnum):
    ERROR = "ERROR"
    FAILURE = "FAILURE"
    SUCCESS = "SUCCESS"


class LocalizationTargetingExpressionResult(BaseModel):
    """Information regarding how and to what extent a targeting expression was localized."""
    error_code: Optional[str] = Field(None, alias="errorCode", description="If status is ERROR or FAILURE, the error code.")
    localized_targeting_expression: Optional["LocalizationTargetingExpression"] = Field(None, alias="localizedTargetingExpression")
    messages: Optional[list[str]] = Field(None, description="If present, contains one or more strings describing why predicates could not be localized. For manual diagnostic use.")
    status: LocalizationTargetingExpressionResultStatus = Field(..., description="The status of the localization operation. Note that if the source targeting expression contains an age range predicate t")

    model_config = {'populate_by_name': True}


class LocalizationTargetingExpressionResponse(BaseModel):
    """A response to a request to localize a targeting expression from a source marketplace to one or more target marketplaces."""
    localized_targeting_expression_results: Optional[dict[str, "LocalizationTargetingExpressionResult"]] = Field(None, alias="localizedTargetingExpressionResults", description="A map from target marketplace ID (string) to the localization result (`LocalizationTargetingExpressionResult`). All targ")
    localized_targeting_expressions: Optional[dict[str, "LocalizationTargetingExpression"]] = Field(None, alias="localizedTargetingExpressions", description="A map from target marketplace ID (string) to localized targeting expression (`LocalizationTargetingExpression`). If no e")

    model_config = {'populate_by_name': True}


class LocalizationTargetingExpressionResponseV2Status(StrEnum):
    ERROR = "ERROR"
    FAILURE = "FAILURE"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"
    SUCCESS = "SUCCESS"


class LocalizationTargetingExpressionResponseV2(BaseModel):
    """A response to a request to localize a targeting expression from a source marketplace to one or more target marketplaces."""
    error_code: Optional[str] = Field(None, alias="errorCode", description="If status is ERROR, the error code. Not present if status is SUCCESS.")
    localized_targeting_expression_results: dict[str, "LocalizationTargetingExpressionResult"] = Field(..., alias="localizedTargetingExpressionResults", description="A map from target marketplace ID (string) to the localization result (`LocalizationTargetingExpressionResult`). All targ")
    source_targeting_expressions: Optional[dict[str, "LocalizationTargetingExpression"]] = Field(None, alias="sourceTargetingExpressions", description="Source targeting expression for this result set.")
    status: LocalizationTargetingExpressionResponseV2Status = Field(..., description="If SUCCESS, PARTIAL_SUCCESS or FAILURE, do not retry. If ERROR, may retry.")

    model_config = {'populate_by_name': True}


class LocalizationTargetingExpressionResponseV3Status(StrEnum):
    ERROR = "ERROR"
    FAILURE = "FAILURE"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"
    SUCCESS = "SUCCESS"


class LocalizationTargetingExpressionResponseV3(BaseModel):
    """A response to a request to localize a targeting expression from a source marketplace to one or more target marketplaces."""
    error_code: Optional[str] = Field(None, alias="errorCode", description="If status is ERROR, the error code. Not present if status is SUCCESS.")
    localized_resolved_targeting_expression_results: Optional[dict[str, "LocalizationTargetingExpressionResult"]] = Field(None, alias="localizedResolvedTargetingExpressionResults", description="A map from resolved target locales to the resolved result (`LocalizationTargetingExpressionResult`). All resolved target")
    localized_targeting_expression_results: dict[str, "LocalizationTargetingExpressionResult"] = Field(..., alias="localizedTargetingExpressionResults", description="A map from target marketplace ID (string) to the localization result (`LocalizationTargetingExpressionResult`). All targ")
    source_resolved_targeting_expression_results: Optional[dict[str, "LocalizationTargetingExpressionResult"]] = Field(None, alias="sourceResolvedTargetingExpressionResults", description="A map from resolved source locales to the resolved result (`LocalizationTargetingExpressionResult`). All resolved source")
    source_targeting_expression: Any = Field(..., alias="sourceTargetingExpression", description="Source targeting expression for this result set.")
    status: LocalizationTargetingExpressionResponseV3Status = Field(..., description="If SUCCESS, PARTIAL_SUCCESS or FAILURE, do not retry. If ERROR, may retry.")

    model_config = {'populate_by_name': True}


class LocalizationTargetingSourceDetails(BaseModel):
    """A source marketplace. One of the marketplace ID or the two-letter country code must be present. The latter is ignored if the former is present."""
    country_code: Optional[str] = Field(None, alias="countryCode", description="A two-letter country code. Please refer to the table above for a list of supported country codes.")
    marketplace_id: Optional[str] = Field(None, alias="marketplaceId", description="The ID of the source marketplace. For example, when mapping data from the UK (marketplace ID A1F83G8C2ARO7P) to Germany ")

    model_config = {'populate_by_name': True}


class LocalizationTargetingTargetDetails(BaseModel):
    """A target marketplace. One of the marketplace ID or the two-letter country code must be present. The latter is ignored if the former is present."""
    country_code: Optional[str] = Field(None, alias="countryCode", description="A two-letter country code. Please refer to the table above for a list of supported country codes.")
    marketplace_id: Optional[str] = Field(None, alias="marketplaceId", description="The ID of the target marketplace. For example, when mapping data from the UK (marketplace ID A1F83G8C2ARO7P) to Germany ")

    model_config = {'populate_by_name': True}


class currencyLocalizationError(BaseModel):
    """A CurrencyLocalizationError Object."""
    code: int = Field(..., description="Programmatic status code.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class currencyLocalizationRequest(BaseModel):
    """Currency Localization Request Object."""
    localize_currency_requests: list["LocalizationCurrencyRequest"] = Field(..., alias="localizeCurrencyRequests", description="An array of LocalizationCurrencyRequest objects. The order will be maintained in the response.")
    source_country_code: Optional[str] = Field(None, alias="sourceCountryCode", description="A two-letter country code. When both marketplaceId and countryCode are present, countryCode is ignored. Please refer to ")
    source_marketplace_id: Optional[str] = Field(None, alias="sourceMarketplaceId", description="The source marketplace ID. Please see the table in the description of `targetMarketplaces` for supported values.")
    target_country_codes: Optional[list[str]] = Field(None, alias="targetCountryCodes", description="A list of two-letter country codes. When both marketplaceId and countryCode are present, countryCode is ignored. Please ")
    target_marketplaces: Optional[list[str]] = Field(None, alias="targetMarketplaces", description="A list of target marketplace IDs. Each element must be unique. The order is irrelevant. The following marketplaces are s")

    model_config = {'populate_by_name': True}


class currencyLocalizationResponse(BaseModel):
    """CurrencyLocalizationResponse Object."""
    localized_currency_responses: list["LocalizationCurrencyResponse"] = Field(..., alias="localizedCurrencyResponses", description="An array of LocalizationCurrencyResponse objects. The order matches that of the input LocalizationCurrencyRequest object")

    model_config = {'populate_by_name': True}


class currencyLocalizationResponseV2(BaseModel):
    """CurrencyLocalizationResponse Object."""
    localized_currency_responses: list["LocalizationCurrencyResponseV2"] = Field(..., alias="localizedCurrencyResponses", description="An array of LocalizationCurrencyResponseV2 objects. The order matches that of the input LocalizationCurrencyRequest obje")

    model_config = {'populate_by_name': True}


class keywordsLocalizationError(BaseModel):
    code: Optional[int] = Field(None, description="Programmatic status code.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class keywordsLocalizationRequest(BaseModel):
    localize_keyword_requests: list["LocalizationKeywordRequest"] = Field(..., alias="localizeKeywordRequests", description="List of LocalizationKeywordRequests. The order will be maintained in the response.")
    source_details: Optional["LocalizationKeywordSourceDetails"] = Field(None, alias="sourceDetails")
    target_details: "LocalizationKeywordTargetDetails" = Field(..., alias="targetDetails")

    model_config = {'populate_by_name': True}


class keywordsLocalizationResponse(BaseModel):
    localized_keyword_responses: list["LocalizationKeywordResponse"] = Field(..., alias="localizedKeywordResponses", description="List of LocalizationKeywordResponses. The order matches that of the LocalizationKeywordRequests list in the request.")

    model_config = {'populate_by_name': True}


class keywordsLocalizationResponseV2(BaseModel):
    localized_keyword_responses: list["LocalizationKeywordResponseV2"] = Field(..., alias="localizedKeywordResponses", description="List of LocalizationKeywordResponses. The order matches that of the LocalizationKeywordRequests list in the request.")

    model_config = {'populate_by_name': True}


class productLocalizationError(BaseModel):
    code: Optional[int] = Field(None, description="Programmatic status code.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class productLocalizationRequestAdtype(StrEnum):
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"


class productLocalizationRequestEntitytype(StrEnum):
    KDP_AUTHOR = "KDP_AUTHOR"
    SELLER = "SELLER"
    VENDOR = "VENDOR"


class productLocalizationRequest(BaseModel):
    ad_type: productLocalizationRequestAdtype = Field(..., alias="adType", description="Used to confirm that the caller is eligible to advertise localized products. Currently, only Sponsored Products advertis")
    entity_type: productLocalizationRequestEntitytype = Field(..., alias="entityType", description="The type of the advertiser accounts for which IDs are specified elsewhere in the request.")
    localize_product_requests: list["LocalizationProductRequest"] = Field(..., alias="localizeProductRequests", description="The products to be localized. Their order will be maintained in the response.")
    source_advertiser_id: str = Field(..., alias="sourceAdvertiserId", description="The ID of the source advertiser account. This may be either a marketplace-specific obfuscated ID (AD9EUOBWMS33M), an ent")
    source_country_code: Optional[str] = Field(None, alias="sourceCountryCode", description="A two-letter country code. When both marketplaceId and countryCode are present, countryCode is ignored. Please refer to ")
    source_marketplace_id: Optional[str] = Field(None, alias="sourceMarketplaceId", description="The ID of the source marketplace. Please see the table within the description of the target details object for supported")
    target_details: list["LocalizationProductTargetDetails"] = Field(..., alias="targetDetails", description="The target details for the LocalizationProductRequests. There must be only one target details object per marketplace ID.")

    model_config = {'populate_by_name': True}


class productLocalizationResponse(BaseModel):
    localized_product_responses: list["LocalizationProductResponse"] = Field(..., alias="localizedProductResponses", description="List of product localization map objects. The order matches that of the localizeProductRequests field in the request.")

    model_config = {'populate_by_name': True}


class productLocalizationResponseV2(BaseModel):
    localized_product_responses: list["LocalizationProductResponseV2"] = Field(..., alias="localizedProductResponses", description="List of product localization map objects. The order matches that of the localizeProductRequests field in the request.")

    model_config = {'populate_by_name': True}


class targetingExpressionLocalizationError(BaseModel):
    code: Optional[int] = Field(None, description="Programmatic status code.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class targetingExpressionLocalizationRequest(BaseModel):
    requests: list["LocalizationTargetingExpressionRequest"] = Field(..., description="A list of requests, each containing a targeting expression to localize. Its order will be maintained in `responses` in t")
    source_details: "LocalizationTargetingSourceDetails" = Field(..., alias="sourceDetails")
    source_resolved_targeting_expression_locales: Optional[list[str]] = Field(None, alias="sourceResolvedTargetingExpressionLocales", description="The locales to which the caller wishes to retrieve the human readable string (e.g. category name instead of category id)")
    target_details_list: list["LocalizationTargetingTargetDetails"] = Field(..., alias="targetDetailsList", description="The targets to which the source targeting expression should be localized.")
    target_resolved_targeting_expression_locale: Optional[str] = Field(None, alias="targetResolvedTargetingExpressionLocale", description="The locale to which the caller wishes to retrieve the human readable string (e.g. category name instead of category id) ")

    model_config = {'populate_by_name': True}


class targetingExpressionLocalizationResponse(BaseModel):
    responses: list["LocalizationTargetingExpressionResponse"] = Field(..., description="A list of responses containing localized targeting expressions. Its order matches that of `requests` in the correspondin")

    model_config = {'populate_by_name': True}


class targetingExpressionLocalizationResponseV2(BaseModel):
    responses: list["LocalizationTargetingExpressionResponseV2"] = Field(..., description="A list of responses containing localized targeting expressions. Its order matches that of `requests` in the correspondin")

    model_config = {'populate_by_name': True}


class targetingExpressionLocalizationResponseV3(BaseModel):
    responses: list["LocalizationTargetingExpressionResponseV3"] = Field(..., description="A list of responses containing localized targeting expressions. Its order matches that of `requests` in the correspondin")

    model_config = {'populate_by_name': True}

