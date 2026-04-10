"""Auto-generated async API client. Do not edit manually.

Source: PartnerOpportunities_prod_3p.json
Title:  Partner Opportunities
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_partner_opportunities import *  # noqa: F403
except ImportError:
    pass


class PartnerOpportunitiesClient(BaseAdsClient):
    """Auto-generated from PartnerOpportunities_prod_3p.json (5 operations)"""

    async def partner_opportunities_list_opportunities(self, max_results: str | None = None, next_token: str | None = None, locale: str | None = None, retrieve_translation_keys: str | None = None, advertiser_id: str | None = None, profile_id: str | None = None, audience: str | None = None, objective_type: str | None = None, product: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """GET /partnerOpportunities

        Gets a list of opportunities specific to the partner making the request.  **Authorized resource type**: Global Manager A
        """
        endpoint = "/partnerOpportunities"
        params: dict[str, Any] = {}
        if max_results is not None:
            params["maxResults"] = max_results
        if next_token is not None:
            params["nextToken"] = next_token
        if locale is not None:
            params["locale"] = locale
        if retrieve_translation_keys is not None:
            params["retrieveTranslationKeys"] = retrieve_translation_keys
        if advertiser_id is not None:
            params["advertiserId"] = advertiser_id
        if profile_id is not None:
            params["profileId"] = profile_id
        if audience is not None:
            params["audience"] = audience
        if objective_type is not None:
            params["objectiveType"] = objective_type
        if product is not None:
            params["product"] = product
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        return await self.get(endpoint, params=params)

    async def partner_opportunities_summarize_opportunities(self, audience: str | None = None, objective_type: str | None = None, product: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """GET /partnerOpportunities/summary

        Gets aggregated information about all opportunities specific to the partner making the request. Supported since V1.1.  *
        """
        endpoint = "/partnerOpportunities/summary"
        params: dict[str, Any] = {}
        if audience is not None:
            params["audience"] = audience
        if objective_type is not None:
            params["objectiveType"] = objective_type
        if product is not None:
            params["product"] = product
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        return await self.get(endpoint, params=params)

    async def partner_opportunities_application_status(self, partner_opportunity_id: str, body: PartnerOpportunitiesApplicationStatusRequestDtoV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """POST /partnerOpportunities/{partnerOpportunityId}/applicationStatus

        Retrieves the current status of applied recommendations.  **Authorized resource type**: Global Manager Account ID  **Par
        """
        endpoint = f"/partnerOpportunities/{partner_opportunity_id}/applicationStatus"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.partneropportunity.v1+json")

    async def partner_opportunities_apply(self, partner_opportunity_id: str, body: PartnerOpportunitiesApplyRequestDtoV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """POST /partnerOpportunities/{partnerOpportunityId}/apply

        Applies a given set of recommendations. Application may be asynchronous. Application status may be checked using the app
        """
        endpoint = f"/partnerOpportunities/{partner_opportunity_id}/apply"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.partneropportunity.v1+json")

    async def partner_opportunities_get_opportunity_file(self, partner_opportunity_id: str, file_format: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """GET /partnerOpportunities/{partnerOpportunityId}/file

        Gets a 307 - TEMPORARY_REDIRECT to an opportunity data file.  **Authorized resource type**: Global Manager Account ID  *
        """
        endpoint = f"/partnerOpportunities/{partner_opportunity_id}/file"
        params: dict[str, Any] = {}
        if file_format is not None:
            params["fileFormat"] = file_format
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        return await self.get(endpoint, params=params)

