"""Auto-generated async API client. Do not edit manually.

Source: Rule-BasedAudiences_prod_3p.json
Title:  Rule-Based Audiences
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_amc_rule_based_audiences import *  # noqa: F403
except ImportError:
    pass


class AmcRuleBasedAudiencesClient(BaseAdsClient):
    """Auto-generated from Rule-BasedAudiences_prod_3p.json (6 operations)"""

    async def create_lookalike_audience(self, body: AMCLookalikeAudiencesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_entity_id: str | None = None, amazon_marketing_cloud_audience_instance_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/audiences/lookalike

        Creates lookalike audience execution metadata information.
        """
        endpoint = "/amc/audiences/lookalike"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_entity_id is not None:
            params["Amazon-Advertising-API-EntityId"] = amazon_advertising_api_entity_id
        if amazon_marketing_cloud_audience_instance_id is not None:
            params["Amazon-Marketing-Cloud-Audience-InstanceId"] = amazon_marketing_cloud_audience_instance_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcquerybasedaudience.v1+json")

    async def get_all_query_based_audiences_by_instance_id(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_entity_id: str | None = None, amazon_marketing_cloud_audience_instance_id: str | None = None, max_results: str | None = None, next_token: str | None = None) -> JSONData | JSONList:
        """GET /amc/audiences/query

        Get all query based audiences execution metadata.
        """
        endpoint = "/amc/audiences/query"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_entity_id is not None:
            params["Amazon-Advertising-API-EntityId"] = amazon_advertising_api_entity_id
        if amazon_marketing_cloud_audience_instance_id is not None:
            params["Amazon-Marketing-Cloud-Audience-InstanceId"] = amazon_marketing_cloud_audience_instance_id
        if max_results is not None:
            params["maxResults"] = max_results
        if next_token is not None:
            params["nextToken"] = next_token
        return await self.get(endpoint, params=params)

    async def create_query_based_audience(self, body: AMCQueryBasedAudiencesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_entity_id: str | None = None, amazon_marketing_cloud_audience_instance_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/audiences/query

        Creates query based audience execution metadata information.
        """
        endpoint = "/amc/audiences/query"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_entity_id is not None:
            params["Amazon-Advertising-API-EntityId"] = amazon_advertising_api_entity_id
        if amazon_marketing_cloud_audience_instance_id is not None:
            params["Amazon-Marketing-Cloud-Audience-InstanceId"] = amazon_marketing_cloud_audience_instance_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcquerybasedaudience.v1+json")

    async def delete_query_based_audience_by_audience_execution_id(self, audience_execution_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_entity_id: str | None = None, amazon_marketing_cloud_audience_instance_id: str | None = None) -> JSONData | JSONList:
        """DELETE /amc/audiences/query/{audienceExecutionId}

        Delete the AMC audience for a given audienceExecutionId.
        """
        endpoint = f"/amc/audiences/query/{audience_execution_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_entity_id is not None:
            params["Amazon-Advertising-API-EntityId"] = amazon_advertising_api_entity_id
        if amazon_marketing_cloud_audience_instance_id is not None:
            params["Amazon-Marketing-Cloud-Audience-InstanceId"] = amazon_marketing_cloud_audience_instance_id
        return await self.delete(endpoint, params=params)

    async def get_query_based_audience_by_audience_execution_id(self, audience_execution_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_entity_id: str | None = None, amazon_marketing_cloud_audience_instance_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/audiences/query/{audienceExecutionId}

        Get query based audience execution metadata for a given audienceExecutionId.
        """
        endpoint = f"/amc/audiences/query/{audience_execution_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_entity_id is not None:
            params["Amazon-Advertising-API-EntityId"] = amazon_advertising_api_entity_id
        if amazon_marketing_cloud_audience_instance_id is not None:
            params["Amazon-Marketing-Cloud-Audience-InstanceId"] = amazon_marketing_cloud_audience_instance_id
        return await self.get(endpoint, params=params)

    async def update_query_based_audience_by_audience_execution_id(self, audience_execution_id: str, body: AMCQueryBasedAudiencesUpdateRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_entity_id: str | None = None, amazon_marketing_cloud_audience_instance_id: str | None = None) -> JSONData | JSONList:
        """PUT /amc/audiences/query/{audienceExecutionId}

        Update query based audience execution metadata for a given audienceExecutionId.
        """
        endpoint = f"/amc/audiences/query/{audience_execution_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_entity_id is not None:
            params["Amazon-Advertising-API-EntityId"] = amazon_advertising_api_entity_id
        if amazon_marketing_cloud_audience_instance_id is not None:
            params["Amazon-Marketing-Cloud-Audience-InstanceId"] = amazon_marketing_cloud_audience_instance_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcquerybasedaudience.v1+json")

