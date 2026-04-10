"""Auto-generated Pydantic models. Do not edit manually.

Source: Diagnostics_prod_3p.json
Title:  Diagnostics
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field



class CampaignDiagnosticsAuthorizationException(BaseModel):
    """401 Unauthorized Exception."""
    error_message: str = Field(..., alias="errorMessage")
    request_id: str = Field(..., alias="requestId")

    model_config = {'populate_by_name': True}


class CampaignDiagnosticsInternalException(BaseModel):
    """500 Internal Exception."""
    error_message: str = Field(..., alias="errorMessage")
    request_id: str = Field(..., alias="requestId")

    model_config = {'populate_by_name': True}


class IssueType(BaseModel):
    """Describes the type of the issue, for example FEATURED OFFER, PRODUCT_ELIGIBILITY, MODERATION."""
    pass


class Severity(BaseModel):
    """Describes the severity of the issue whether it is CRITICAL or WARNING."""
    pass


class CampaignDiagnosticsRequest(BaseModel):
    """A request to run diagnostics to retrieve issues impacting campaigns."""
    campaign_ids_list: list[str] = Field(..., alias="campaignIdsList", description="A list of campaign identifiers to be diagnosed.")
    include_only_active: Optional[bool] = Field(None, alias="includeOnlyActive", description="Includes diagnostics information for only enabled entities. By default the response includes diagnostics information for")
    issue_type_filter: Optional[list["IssueType"]] = Field(None, alias="issueTypeFilter", description="Specifies the issue types to be included. By default the response will include all issue types.")
    locale: Optional[str] = Field(None, description="Specifies the language in which diagnostics information is returned. By default value is set to en_US. Value must be one")
    max_issues_per_campaign: Optional[int] = Field(None, alias="maxIssuesPerCampaign", description="Sets a limit on the number of issues returned for a campaign. Default value is set to 100 and maximum value supported is")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results,")
    severity_filter: Optional[list["Severity"]] = Field(None, alias="severityFilter", description="Specifies the issue severities to be included. By default the response will include all issue severities.")

    model_config = {'populate_by_name': True}


class Error(BaseModel):
    error_code: str = Field(..., alias="errorCode", description="Enum indicating the category of error. Example `NOT_FOUND`.")
    error_message: str = Field(..., alias="errorMessage", description="Error message provided.")
    item_request_id: str = Field(..., alias="itemRequestId", description="Campaign identifier.")

    model_config = {'populate_by_name': True}


class IssueImpactSupplementalinfo(BaseModel):
    """Provides the corresponding ASIN information in case of seller product issue, reflected as 'SKU' in entityType."""
    asin: Optional[str] = Field(None, description="Amazon product identifier.")

    model_config = {'populate_by_name': True}


class IssueImpact(BaseModel):
    """Captures the impact of the issue across the campaign."""
    entity_identifier: str = Field(..., alias="entityIdentifier", description="An Amazon product identifier or seller product identifier.")
    entity_type: str = Field(..., alias="entityType", description="Field to mention the impacted entityType for the issue. Possible entityType values are 'ASIN' or 'SKU' and the value is ")
    num_ads_impacted: int = Field(..., alias="numAdsImpacted", description="A count of ads impacted by the entity.")
    supplemental_info: Optional["IssueImpactSupplementalinfo"] = Field(None, alias="supplementalInfo", description="Provides the corresponding ASIN information in case of seller product issue, reflected as 'SKU' in entityType.")

    model_config = {'populate_by_name': True}


class Issue(BaseModel):
    """Captures issue details."""
    impact: "IssueImpact" = Field(..., description="Captures the impact of the issue across the campaign.")
    information: str = Field(..., description="A human readable description of the issue including possible remediations, wherever applicable.")
    issue_code: str = Field(..., alias="issueCode", description="Describes the specific issue code under the broader issueType, for example MISSING_IMAGE.")
    issue_type: "IssueType" = Field(..., alias="issueType")
    severity: "Severity"

    model_config = {'populate_by_name': True}


class campaignDiagnosticsList(BaseModel):
    """A list of diagnosed campaigns with information on identified issues."""
    campaign_id: str = Field(..., alias="campaignId", description="Campaign identifier.")
    issues_list: list["Issue"] = Field(..., alias="issuesList", description="A list of issues impacting the campaign.")

    model_config = {'populate_by_name': True}


class CampaignDiagnosticsResponse(BaseModel):
    """A list of issues diagnosed for the campaigns specified by the requester."""
    campaign_diagnostics_list: list["campaignDiagnosticsList"] = Field(..., alias="campaignDiagnosticsList", description="A list of diagnosed campaigns with information on identified issues.")
    errors_list: list["Error"] = Field(..., alias="errorsList", description="Errors from api request.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results,")
    request_id: str = Field(..., alias="requestId")

    model_config = {'populate_by_name': True}


class CampaignDiagnosticsThrottlingException(BaseModel):
    """429 Throttling Exception."""
    error_message: str = Field(..., alias="errorMessage")
    request_id: str = Field(..., alias="requestId")

    model_config = {'populate_by_name': True}


class CampaignDiagnosticsValidationException(BaseModel):
    """400 Validation Exception."""
    error_message: str = Field(..., alias="errorMessage")
    request_id: str = Field(..., alias="requestId")

    model_config = {'populate_by_name': True}

