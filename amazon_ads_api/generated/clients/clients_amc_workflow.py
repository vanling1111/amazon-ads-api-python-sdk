"""Auto-generated async API client. Do not edit manually.

Source: WorkflowManagementService_prod_3p.json
Title:  Workflow Management Service
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_amc_workflow import *  # noqa: F403
except ImportError:
    pass


class AmcWorkflowClient(BaseAdsClient):
    """Auto-generated from WorkflowManagementService_prod_3p.json (17 operations)"""

    async def list_data_sources(self, instance_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, next_token: str | None = None, limit: str | None = None) -> JSONData | JSONList:
        """GET /amc/reporting/{instanceId}/dataSources

        Returns a list of available data sources.
        """
        endpoint = f"/amc/reporting/{instance_id}/dataSources"
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

    async def get_data_source(self, instance_id: str, data_source_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/reporting/{instanceId}/dataSources/{dataSourceId}

        Gets information about the requested data source.
        """
        endpoint = f"/amc/reporting/{instance_id}/dataSources/{data_source_id}"
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

    async def list_schedules(self, instance_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, next_token: str | None = None, limit: str | None = None, marketplace_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/reporting/{instanceId}/schedules

        Returns a list of schedules.
        """
        endpoint = f"/amc/reporting/{instance_id}/schedules"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if next_token is not None:
            params["nextToken"] = next_token
        if limit is not None:
            params["limit"] = limit
        if marketplace_id is not None:
            params["marketplaceId"] = marketplace_id
        return await self.get(endpoint, params=params)

    async def create_schedule(self, instance_id: str, body: CreateScheduleRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/reporting/{instanceId}/schedules

        Creates a new schedule.
        """
        endpoint = f"/amc/reporting/{instance_id}/schedules"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcschedules.v1+json")

    async def delete_schedule(self, instance_id: str, schedule_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_ads_account_id: str | None = None, marketplace_id: str | None = None) -> JSONData | JSONList:
        """DELETE /amc/reporting/{instanceId}/schedules/{scheduleId}

        Deletes the requested schedule.
        """
        endpoint = f"/amc/reporting/{instance_id}/schedules/{schedule_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if marketplace_id is not None:
            params["marketplaceId"] = marketplace_id
        return await self.delete(endpoint, params=params)

    async def get_schedule(self, instance_id: str, schedule_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, marketplace_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/reporting/{instanceId}/schedules/{scheduleId}

        Gets the requested schedule.
        """
        endpoint = f"/amc/reporting/{instance_id}/schedules/{schedule_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if marketplace_id is not None:
            params["marketplaceId"] = marketplace_id
        return await self.get(endpoint, params=params)

    async def update_schedule(self, instance_id: str, schedule_id: str, body: CreateScheduleRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """PUT /amc/reporting/{instanceId}/schedules/{scheduleId}

        Updates the requested schedule.
        """
        endpoint = f"/amc/reporting/{instance_id}/schedules/{schedule_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcschedules.v1+json")

    async def list_workflow_executions(self, instance_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, next_token: str | None = None, limit: str | None = None, sort_ascending: str | None = None, include_cancelled: str | None = None, min_creation_time: str | None = None, max_creation_time: str | None = None, time_zone: str | None = None, workflow_id: str | None = None, include_workflow: str | None = None) -> JSONData | JSONList:
        """GET /amc/reporting/{instanceId}/workflowExecutions

        Returns a list of workflow executions.
        """
        endpoint = f"/amc/reporting/{instance_id}/workflowExecutions"
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
        if sort_ascending is not None:
            params["sortAscending"] = sort_ascending
        if include_cancelled is not None:
            params["includeCancelled"] = include_cancelled
        if min_creation_time is not None:
            params["minCreationTime"] = min_creation_time
        if max_creation_time is not None:
            params["maxCreationTime"] = max_creation_time
        if time_zone is not None:
            params["timeZone"] = time_zone
        if workflow_id is not None:
            params["workflowId"] = workflow_id
        if include_workflow is not None:
            params["includeWorkflow"] = include_workflow
        return await self.get(endpoint, params=params)

    async def create_workflow_execution(self, instance_id: str, body: CreateWorkflowExecutionRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/reporting/{instanceId}/workflowExecutions

        Creates a new workflow execution.
        """
        endpoint = f"/amc/reporting/{instance_id}/workflowExecutions"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcworkflowexecutions.v1+json")

    async def get_workflow_execution(self, instance_id: str, workflow_execution_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, include_workflow: str | None = None) -> JSONData | JSONList:
        """GET /amc/reporting/{instanceId}/workflowExecutions/{workflowExecutionId}

        Gets status information about the requested workflow execution.
        """
        endpoint = f"/amc/reporting/{instance_id}/workflowExecutions/{workflow_execution_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if include_workflow is not None:
            params["includeWorkflow"] = include_workflow
        return await self.get(endpoint, params=params)

    async def update_workflow_execution(self, instance_id: str, workflow_execution_id: str, body: WorkflowExecution | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """PUT /amc/reporting/{instanceId}/workflowExecutions/{workflowExecutionId}

        Updates the requested workflow execution.
        """
        endpoint = f"/amc/reporting/{instance_id}/workflowExecutions/{workflow_execution_id}"
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcworkflowexecutions.v1+json")

    async def get_workflow_execution_download_urls(self, instance_id: str, workflow_execution_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/reporting/{instanceId}/workflowExecutions/{workflowExecutionId}/downloadUrls

        Retrieves pre-signed url for downloading workflow execution results from S3.
        """
        endpoint = f"/amc/reporting/{instance_id}/workflowExecutions/{workflow_execution_id}/downloadUrls"
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

    async def list_workflows(self, instance_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, next_token: str | None = None, limit: str | None = None) -> JSONData | JSONList:
        """GET /amc/reporting/{instanceId}/workflows

        Returns a list of workflows.
        """
        endpoint = f"/amc/reporting/{instance_id}/workflows"
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

    async def create_workflow(self, instance_id: str, body: Workflow | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/reporting/{instanceId}/workflows

        Creates a new workflow.
        """
        endpoint = f"/amc/reporting/{instance_id}/workflows"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcworkflows.v1+json")

    async def delete_workflow(self, instance_id: str, workflow_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """DELETE /amc/reporting/{instanceId}/workflows/{workflowId}

        Deletes the requested workflow.
        """
        endpoint = f"/amc/reporting/{instance_id}/workflows/{workflow_id}"
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

    async def get_workflow(self, instance_id: str, workflow_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/reporting/{instanceId}/workflows/{workflowId}

        Gets the requested workflow.
        """
        endpoint = f"/amc/reporting/{instance_id}/workflows/{workflow_id}"
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

    async def update_workflow(self, instance_id: str, workflow_id: str, body: Workflow | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None) -> JSONData | JSONList:
        """PUT /amc/reporting/{instanceId}/workflows/{workflowId}

        Updates the requested workflow.
        """
        endpoint = f"/amc/reporting/{instance_id}/workflows/{workflow_id}"
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcworkflows.v1+json")

