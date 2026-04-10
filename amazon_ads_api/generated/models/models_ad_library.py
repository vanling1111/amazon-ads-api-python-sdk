"""Auto-generated Pydantic models. Do not edit manually.

Source: AdLibraryAPI_prod_3p.json
Title:  Ad Library API
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class AccessDeniedExceptionResponseContent(BaseModel):
    """Exception for AccessDeniedException 403 response."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class TotalRecipientsRange(BaseModel):
    max: float
    min: float

    model_config = {'populate_by_name': True}


class TargetMethodRecipientGroup(StrEnum):
    ADS_PREFERENCES = "ADS_PREFERENCES"
    LOCATION = "LOCATION"
    PAST_ACTIVITY = "PAST_ACTIVITY"
    SEARCH_TERMS = "SEARCH_TERMS"


class RecipientsBySite(BaseModel):
    amazon_be: Optional["TotalRecipientsRange"] = Field(None, alias="amazonBe")
    amazon_de: Optional["TotalRecipientsRange"] = Field(None, alias="amazonDe")
    amazon_es: Optional["TotalRecipientsRange"] = Field(None, alias="amazonEs")
    amazon_fr: Optional["TotalRecipientsRange"] = Field(None, alias="amazonFr")
    amazon_it: Optional["TotalRecipientsRange"] = Field(None, alias="amazonIt")
    amazon_nl: Optional["TotalRecipientsRange"] = Field(None, alias="amazonNl")
    amazon_pl: Optional["TotalRecipientsRange"] = Field(None, alias="amazonPl")
    amazon_se: Optional["TotalRecipientsRange"] = Field(None, alias="amazonSe")

    model_config = {'populate_by_name': True}


class Type(StrEnum):
    AD = "AD"
    AFFILIATE_MARKETING_CONTENT = "AFFILIATE_MARKETING_CONTENT"


class AdRepositoryResponseMap(BaseModel):
    advertisement_purpose: str = Field(..., alias="advertisementPurpose", description="Displays the intent of the advertisement.")
    advertiser_name: str = Field(..., alias="advertiserName", description="Name of the Advertiser.")
    content_urls: Optional[list[str]] = Field(None, alias="contentUrls", description="List of strings containing link to (1) the store product detail page of products shown in an ad, (2) the store brand pag")
    delivery_after_date_utc: str = Field(..., alias="deliveryAfterDateUtc", description="The specified start date of the delivered ads.The date string is specified in ISO format (YYYY-MM-DD) in UTC timezone. F")
    delivery_before_date_utc: str = Field(..., alias="deliveryBeforeDateUtc", description="The specified end date of the delivered ads.The date string is specified in ISO format (YYYY-MM-DD) in UTC timezone. For")
    id_: str = Field(..., alias="id", description="Globally unique identifier for the advertisement, to support lookups in the repository.  It represents the combination o")
    illegal_content_report: Optional[bool] = Field(None, alias="illegalContentReport", description="Describes whether the ad was removed as a result of an illegal content report.")
    is_restricted: bool = Field(..., alias="isRestricted", description="Whether the ad was paused, removed or suppressed based on alleged illegality or incompatibility with terms and condition")
    payer_name: Optional[str] = Field(None, alias="payerName", description="Name of the entity who paid for the Ad.")
    restriction_category: Optional[str] = Field(None, alias="restrictionCategory", description="Reason(s) why an ad was paused, removed, or suppressed.")
    restriction_detection_automated: Optional[bool] = Field(None, alias="restrictionDetectionAutomated", description="Describes whether automation was used to identify the restricted ad.")
    subject_matter_url: str = Field(..., alias="subjectMatterUrl", description="Subject matter of the advertisement (link to image or rendering).")
    targeting_methods: list["TargetMethodRecipientGroup"] = Field(..., alias="targetingMethods", description="This field lists the targeted advertising methods with the descriptions.     The targeted advertising methods includes: ")
    total_recipients_range: "TotalRecipientsRange" = Field(..., alias="totalRecipientsRange")
    total_recipients_range_by_site: "RecipientsBySite" = Field(..., alias="totalRecipientsRangeBySite")
    type_: "Type" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class GetAdsByIDResponseContent(BaseModel):
    ad: "AdRepositoryResponseMap"

    model_config = {'populate_by_name': True}


class InternalServerExceptionResponseContent(BaseModel):
    """Unexpected error during processing of request."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class InvalidInputExceptionResponseContent(BaseModel):
    """Exception for malformed input."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class NameMatchType(StrEnum):
    CONTAINS = "CONTAINS"
    EXACT_MATCH = "EXACT_MATCH"


class ListAdsRequestContent(BaseModel):
    advertisement_purpose: Optional[str] = Field(None, alias="advertisementPurpose", description="This parameter will limit results to those matching the requested advertisement purpose. This includes the name of the p")
    advertiser_name: Optional[str] = Field(None, alias="advertiserName", description="The person or entity on whose behalf the ad or affiliate marketing content is presented. This parameter will limit resul")
    delivery_after_date_utc: Optional[str] = Field(None, alias="deliveryAfterDateUtc", description="When specified, limits results to those with delivery date after the specified date string. The date string is specified")
    delivery_before_date_utc: Optional[str] = Field(None, alias="deliveryBeforeDateUtc", description="When specified, limits results to those with a delivery date prior to the specified date string. The date string is spec")
    is_restricted: Optional[bool] = Field(None, alias="isRestricted", description="Whether the advertisement was paused, removed or suppressed based on alleged illegality or incompatibility with terms an")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Defaults to 10, with supported values between 1 and 1000.     If the size of the result set is larger than the limit, ca")
    name_match_type: Optional["NameMatchType"] = Field(None, alias="nameMatchType")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Pagination token to retrieve the next set of results.     Callers must make use of the token provided in a previous resp")
    site_name: Optional[str] = Field(None, alias="siteName", description="When specified, limits results based on their delivery to a particular Amazon EU store (e.g., amazon.de, amazon.fr).")

    model_config = {'populate_by_name': True}


class ListAdsResponseContent(BaseModel):
    ads: list["AdRepositoryResponseMap"]
    next_token: Optional[str] = Field(None, alias="nextToken", description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results,")
    total_results: float = Field(..., alias="totalResults", description="Total number of return results for the query input.")

    model_config = {'populate_by_name': True}


class ResourceNotFoundExceptionResponseContent(BaseModel):
    """Request references a resource which does not exist."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class ThrottlingExceptionResponseContent(BaseModel):
    """Exception for ThrottlingException 429 response."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class UnauthorizedExceptionResponseContent(BaseModel):
    """Exception for UnauthorizedException 401 response."""
    message: Optional[str] = None

    model_config = {'populate_by_name': True}

