"""Auto-generated async API client. Do not edit manually.

Source: Advertiseraudiences_prod_3p.json
Title:  Advertiser audiences
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_amc_advertiser_audiences import *  # noqa: F403
except ImportError:
    pass


class AmcAdvertiserAudiencesClient(BaseAdsClient):
    """Auto-generated from Advertiseraudiences_prod_3p.json (10 operations)"""

    async def amcp_link_remove_connection_v2(self, connection_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """DELETE /amc/audiences/connections

        Delete a connection between the Partner and Advertiser's AMC Instances and/or DSP Advertisers.
        """
        endpoint = "/amc/audiences/connections"
        params: dict[str, Any] = {}
        if connection_id is not None:
            params["connectionId"] = connection_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.delete(endpoint, params=params)

    async def amcp_link_get_connections_v2(self, connection_id: str | None = None, is_default: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/audiences/connections

        Get a list of connections between the Partner and Advertiser's AMC Instances & DSP Advertisers.
        """
        endpoint = "/amc/audiences/connections"
        params: dict[str, Any] = {}
        if connection_id is not None:
            params["connectionId"] = connection_id
        if is_default is not None:
            params["isDefault"] = is_default
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

    async def amcp_link_add_connection_v2(self, body: AmcpLinkAddConnectionV2RequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/audiences/connections

        Create a new connection between the Partner and Advertiser's AMC Instances and/or DSP Advertisers.
        """
        endpoint = "/amc/audiences/connections"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcaudiencesconnections.v1+json")

    async def amcp_link_get_terms_v2(self, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/audiences/connections/terms

        Get the Customer's AMC Terms and Conditions acceptance.
        """
        endpoint = "/amc/audiences/connections/terms"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

    async def amcp_link_set_terms_acceptance_v2(self, body: AmcpLinkSetTermsAcceptanceV2RequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """PATCH /amc/audiences/connections/terms

        Set the Customer's AMC Terms and Conditions acceptance.
        """
        endpoint = "/amc/audiences/connections/terms"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self._request('PATCH', endpoint, json_data=json_data, params=params, content_type="application/vnd.amcaudiencesconnections.v1+json")

    async def create_audience_metadata_v2(self, body: CreateAudienceMetadataV2RequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/audiences/metadata

        Create a new Advertiser Audience Metadata.
        """
        endpoint = "/amc/audiences/metadata"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcaudiences.v1+json")

    async def get_audience_metadata_v2(self, audience_id: str, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/audiences/metadata/{audienceId}

        Get an Advertiser Audience Metadata using AudienceId.
        """
        endpoint = f"/amc/audiences/metadata/{audience_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

    async def update_audience_metadata_v2(self, audience_id: str, body: UpdateAudienceMetadataV2RequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """PUT /amc/audiences/metadata/{audienceId}

        Update an existing Advertiser Audience Metadata.
        """
        endpoint = f"/amc/audiences/metadata/{audience_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcaudiences.v1+json")

    async def manage_audience_v2(self, body: ManageAudienceV2RequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/audiences/records

        Manage Advertiser audiences by adding or removing members from an Audience.
        """
        endpoint = "/amc/audiences/records"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcaudiences.v1+json")

    async def manage_audience_status_v2(self, job_request_id: str, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/audiences/records/{jobRequestId}

        Get the status of a manage audience members request.
        """
        endpoint = f"/amc/audiences/records/{job_request_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

