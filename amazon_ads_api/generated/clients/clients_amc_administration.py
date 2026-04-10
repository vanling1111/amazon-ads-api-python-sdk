"""Auto-generated async API client. Do not edit manually.

Source: AMCAdministration_prod_3p.json
Title:  AMC Administration
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_amc_administration import *  # noqa: F403
except ImportError:
    pass


class AmcAdministrationClient(BaseAdsClient):
    """Auto-generated from AMCAdministration_prod_3p.json (25 operations)"""

    async def amcp_link_list_amc_accounts(self, next_token: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/accounts

        Get a list of AMC Accounts that the user have access to.
        """
        endpoint = "/amc/accounts"
        params: dict[str, Any] = {}
        if next_token is not None:
            params["nextToken"] = next_token
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

    async def list_instances(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, next_token: str | None = None, limit: str | None = None) -> JSONData | JSONList:
        """GET /amc/instances

        Gets information about all AMC instances.
        """
        endpoint = "/amc/instances"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if next_token is not None:
            params["nextToken"] = next_token
        if limit is not None:
            params["limit"] = limit
        return await self.get(endpoint, params=params)

    async def create_instance(self, body: AmcCreateInstanceRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/instances

        Creates a new AMC instance.
        """
        endpoint = "/amc/instances"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcinstances.v1+json")

    async def delete_instance(self, instance_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """DELETE /amc/instances/{instanceId}

        Deletes the requested AMC instance.
        """
        endpoint = f"/amc/instances/{instance_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        return await self.delete(endpoint, params=params)

    async def get_instance(self, instance_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/instances/{instanceId}

        Gets information about the requested AMC instance.
        """
        endpoint = f"/amc/instances/{instance_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        return await self.get(endpoint, params=params)

    async def update_instance(self, instance_id: str, body: AmcUpdateInstanceRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """PUT /amc/instances/{instanceId}

        Updates the requested AMC instance.
        """
        endpoint = f"/amc/instances/{instance_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcinstances.v1+json")

    async def get_instance_advertisers(self, instance_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, type: str | None = None, next_token: str | None = None, limit: str | None = None) -> JSONData | JSONList:
        """GET /amc/instances/{instanceId}/advertisers

        Gets advertisers information about the requested AMC instance.
        """
        endpoint = f"/amc/instances/{instance_id}/advertisers"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if type is not None:
            params["type"] = type
        if next_token is not None:
            params["nextToken"] = next_token
        if limit is not None:
            params["limit"] = limit
        return await self.get(endpoint, params=params)

    async def list_advertiser_updates(self, instance_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, next_token: str | None = None, limit: str | None = None) -> JSONData | JSONList:
        """GET /amc/instances/{instanceId}/advertisers/updates

        Lists advertiser updates for the requested AMC instance.
        """
        endpoint = f"/amc/instances/{instance_id}/advertisers/updates"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if next_token is not None:
            params["nextToken"] = next_token
        if limit is not None:
            params["limit"] = limit
        return await self.get(endpoint, params=params)

    async def create_advertiser_update(self, instance_id: str, body: AmcCreateAdvertiserUpdateRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/instances/{instanceId}/advertisers/updates

        Creates a new advertiser update for the requested AMC instance.
        """
        endpoint = f"/amc/instances/{instance_id}/advertisers/updates"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcinstances.v1+json")

    async def get_advertiser_update(self, instance_id: str, update_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/instances/{instanceId}/advertisers/updates/{updateId}

        Gets the requested advertiser update for the requested AMC instance.
        """
        endpoint = f"/amc/instances/{instance_id}/advertisers/updates/{update_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        return await self.get(endpoint, params=params)

    async def get_instance_collaboration(self, instance_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/instances/{instanceId}/collaboration

        Gets the collaboration metadata for the requested AMC instance.
        """
        endpoint = f"/amc/instances/{instance_id}/collaboration"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        return await self.get(endpoint, params=params)

    async def create_collaboration_id_mapping_table(self, instance_id: str, body: CreateCollaborationIdMappingTablePayload | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/instances/{instanceId}/collaboration/idmappingtables

        Creates an ID Mapping Table in the requested AMC instance collaboration and starts the job to populate the table.
        """
        endpoint = f"/amc/instances/{instance_id}/collaboration/idmappingtables"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcinstances.v1+json")

    async def list_collaboration_id_mapping_tables(self, instance_id: str, body: ListCollaborationIdMappingTablesPayload | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/instances/{instanceId}/collaboration/idmappingtables/list

        Lists the ID mapping tables in the collaboration in the requested AMC instance.
        """
        endpoint = f"/amc/instances/{instance_id}/collaboration/idmappingtables/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcinstances.v1+json")

    async def delete_collaboration_id_mapping_table(self, instance_id: str, id_mapping_table_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """DELETE /amc/instances/{instanceId}/collaboration/idmappingtables/{idMappingTableId}

        Deletes the given ID Mapping Table in the collaboration for the requested AMC instance.
        """
        endpoint = f"/amc/instances/{instance_id}/collaboration/idmappingtables/{id_mapping_table_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        return await self.delete(endpoint, params=params)

    async def get_collaboration_id_mapping_job_for_tracking_id(self, instance_id: str, id_mapping_table_id: str, tracking_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/instances/{instanceId}/collaboration/idmappingtables/{idMappingTableId}/jobTracker/{trackingId}

        Retrieves the ID mapping workflow job associated to the tracking ID.
        """
        endpoint = f"/amc/instances/{instance_id}/collaboration/idmappingtables/{id_mapping_table_id}/jobTracker/{tracking_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        return await self.get(endpoint, params=params)

    async def list_collaboration_id_mapping_jobs(self, instance_id: str, id_mapping_table_id: str, body: ListCollaborationIdMappingJobsPayload | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/instances/{instanceId}/collaboration/idmappingtables/{idMappingTableId}/jobs/list

        Lists the ID mapping jobs associated to the ID mapping table.
        """
        endpoint = f"/amc/instances/{instance_id}/collaboration/idmappingtables/{id_mapping_table_id}/jobs/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcinstances.v1+json")

    async def get_collaboration_id_mapping_job(self, instance_id: str, id_mapping_table_id: str, job_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/instances/{instanceId}/collaboration/idmappingtables/{idMappingTableId}/jobs/{jobId}

        Gets the ID mapping job metadata for the requested AMC instance.
        """
        endpoint = f"/amc/instances/{instance_id}/collaboration/idmappingtables/{id_mapping_table_id}/jobs/{job_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        return await self.get(endpoint, params=params)

    async def refresh_collaboration_id_mapping_table(self, instance_id: str, id_mapping_table_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/instances/{instanceId}/collaboration/idmappingtables/{idMappingTableId}/refresh

        Refreshes the data in the given ID Mapping Table in the collaboration for the requested AMC instance.
        """
        endpoint = f"/amc/instances/{instance_id}/collaboration/idmappingtables/{id_mapping_table_id}/refresh"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        return await self.post(endpoint, params=params)

    async def list_collaboration_id_namespaces(self, instance_id: str, body: ListCollaborationIdNamespacesPayload | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/instances/{instanceId}/collaboration/idnamespaces/list

        Lists the ID namespaces associated to the collaboration in the requested AMC instance.
        """
        endpoint = f"/amc/instances/{instance_id}/collaboration/idnamespaces/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcinstances.v1+json")

    async def create_collaboration(self, instance_id: str, body: CreateCollaborationRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/instances/{instanceId}/collaborations

        Creates a collaboration in AWS Clean Rooms for this AMC instance.
        """
        endpoint = f"/amc/instances/{instance_id}/collaborations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcinstances.v1+json")

    async def update_collaboration_customer(self, instance_id: str, collaboration_id: str, body: UpdateCollaborationCustomerRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """PUT /amc/instances/{instanceId}/collaborations/{collaborationId}/acrCustomer

        Update customer member in the collaboration.
        """
        endpoint = f"/amc/instances/{instance_id}/collaborations/{collaboration_id}/acrCustomer"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcinstances.v1+json")

    async def add_collaboration_customer_partners(self, instance_id: str, collaboration_id: str, body: AddCollaborationCustomerPartnersPayload | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/instances/{instanceId}/collaborations/{collaborationId}/acrCustomerPartners

        Add one or more customer partners to the collaboration.
        """
        endpoint = f"/amc/instances/{instance_id}/collaborations/{collaboration_id}/acrCustomerPartners"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcinstances.v1+json")

    async def update_collaboration_customer_partners(self, instance_id: str, collaboration_id: str, body: UpdateCollaborationCustomerPartnersPayload | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """PUT /amc/instances/{instanceId}/collaborations/{collaborationId}/acrCustomerPartners

        Update one or more customer partners in the collaboration.
        """
        endpoint = f"/amc/instances/{instance_id}/collaborations/{collaboration_id}/acrCustomerPartners"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcinstances.v1+json")

    async def delete_collaboration_customer_partner(self, instance_id: str, collaboration_id: str, acr_customer_partner_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """DELETE /amc/instances/{instanceId}/collaborations/{collaborationId}/acrCustomerPartners/{acrCustomerPartnerId}

        Delete the requested customer partner in the collaboration.
        """
        endpoint = f"/amc/instances/{instance_id}/collaborations/{collaboration_id}/acrCustomerPartners/{acr_customer_partner_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        return await self.delete(endpoint, params=params)

    async def update_instance_customer_aws_account_metadata(self, instance_id: str, body: InstanceCustomerAwsAccountMetadataPayload | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/instances/{instanceId}/updateCustomerAwsAccount

        Updates customer's AWS account metadata in the requested AMC instance.
        """
        endpoint = f"/amc/instances/{instance_id}/updateCustomerAwsAccount"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcinstances.v1+json")

