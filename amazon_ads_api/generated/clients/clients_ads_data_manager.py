"""Auto-generated async API client. Do not edit manually.

Source: AdsDataManager_prod_3p.json
Title:  Ads Data Manager
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_ads_data_manager import *  # noqa: F403
except ImportError:
    pass


class AdsDataManagerClient(BaseAdsClient):
    """Auto-generated from AdsDataManager_prod_3p.json (17 operations)"""

    async def list_audience_datasets(self, next_token: str | None = None, limit: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /adm/audiences

        Lists all Audience DataSets.  **Authorized resource type**: Global Manager Account ID  **Parameter name**: Amazon-Ads-Ma
        """
        endpoint = "/adm/audiences"
        params: dict[str, Any] = {}
        if next_token is not None:
            params["nextToken"] = next_token
        if limit is not None:
            params["limit"] = limit
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

    async def create_audience_dataset(self, body: AdsCdxSolCreateAudienceRequestContent | dict[str, Any] | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adm/audiences

        Creates an Audience DataSet.  **Authorized resource type**: Global Manager Account ID  **Parameter name**: Amazon-Ads-Ma
        """
        endpoint = "/adm/audiences"
        params: dict[str, Any] = {}
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def get_audience_dataset(self, data_set_id: str, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /adm/audiences/{dataSetId}

        Gets an Audience DataSet.  **Authorized resource type**: Global Manager Account ID  **Parameter name**: Amazon-Ads-Manag
        """
        endpoint = f"/adm/audiences/{data_set_id}"
        params: dict[str, Any] = {}
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

    async def ingest_audiences(self, data_set_id: str, body: IngestAudiencesRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adm/audiences/{dataSetId}/members

        Posts audience members to an audience dataset.  **Authorized resource type**: Global Manager Account ID  **Parameter nam
        """
        endpoint = f"/adm/audiences/{data_set_id}/members"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.admAudiences.v1+json")

    async def get_dataroom(self, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /adm/datarooms

        Get a data room  **Authorized resource type**: Global Manager Account ID  **Parameter name**: Amazon-Ads-Manager-Account
        """
        endpoint = "/adm/datarooms"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

    async def create_dataroom(self, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adm/datarooms

        Create a dataroom  **Authorized resource type**: Global Manager Account ID  **Parameter name**: Amazon-Ads-Manager-Accou
        """
        endpoint = "/adm/datarooms"
        params: dict[str, Any] = {}
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.post(endpoint, params=params)

    async def get_dataroom_metadata(self, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /adm/datarooms/metadata

        Gets dataset metadata including linked datasets, active dest., etc  **Authorized resource type**: Global Manager Account
        """
        endpoint = "/adm/datarooms/metadata"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

    async def list_dataset_details(self, body: ListDatasetDetailsRequestContent | dict[str, Any] | None = None, search: str | None = None, order: str | None = None, next_token: str | None = None, max_results: str | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adm/datasets/list

        Lists details of datasets in a given account.  **Authorized resource type**: Global Manager Account ID  **Parameter name
        """
        endpoint = "/adm/datasets/list"
        params: dict[str, Any] = {}
        if search is not None:
            params["search"] = search
        if order is not None:
            params["order"] = order
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.admmetrics.v1+json")

    async def delete_dataset(self, data_set_id: str, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """DELETE /adm/datasets/{dataSetId}

        Delete a Dataset.  **Authorized resource type**: DSP Rodeo Entity ID, DSP Advertiser Account ID  **Parameter name**: Ama
        """
        endpoint = f"/adm/datasets/{data_set_id}"
        params: dict[str, Any] = {}
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.delete(endpoint, params=params)

    async def get_data_set_metrics(self, data_set_id: str, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /adm/datasets/{dataSetId}/metrics

        Gets the metrics associated to dataset across all uploads  **Authorized resource type**: Global Manager Account ID  **Pa
        """
        endpoint = f"/adm/datasets/{data_set_id}/metrics"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

    async def get_dataset_aggregates(self, data_set_id: str, body: GetDatasetAggregatesRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adm/datasets/{dataSetId}/metrics/aggregates

        Gets aggregated metrics for a dataset within a specified time range  **Authorized resource type**: Global Manager Accoun
        """
        endpoint = f"/adm/datasets/{data_set_id}/metrics/aggregates"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.admmetrics.v1+json")

    async def delete_identity(self, body: DeleteIdentityRequestContent | dict[str, Any] | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adm/identities/delete

        Deletes matched list of users from your data room within 30 days.  **Authorized resource type**: Global Manager Account 
        """
        endpoint = "/adm/identities/delete"
        params: dict[str, Any] = {}
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.admDataDeletion.v1+json")

    async def create_sharing_rule(self, body: CreateSharingRuleRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adm/sharingRules

        Create a new Sharing Rule in ADM.  **Authorized resource type**: Global Manager Account ID  **Parameter name**: Amazon-A
        """
        endpoint = "/adm/sharingRules"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def list_sharing_rules(self, body: ListSharingRulesRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """POST /adm/sharingRules/list

        List a set of sharing rules belonging to an account.  **Authorized resource type**: Global Manager Account ID  **Paramet
        """
        endpoint = "/adm/sharingRules/list"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def revoke_sharing_rule(self, sharing_rule_id: str, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """PATCH /adm/sharingRules/{sharingRuleId}/revoke

        Revoke an existing Sharing Rule in ADM.  **Authorized resource type**: Global Manager Account ID  **Parameter name**: Am
        """
        endpoint = f"/adm/sharingRules/{sharing_rule_id}/revoke"
        params: dict[str, Any] = {}
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self._request('PATCH', endpoint, params=params)

    async def get_terms(self, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """GET /adm/terms

        Get the Customer's Ads Data Manager Terms and Conditions  **Authorized resource type**: Global Manager Account ID  **Par
        """
        endpoint = "/adm/terms"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        return await self.get(endpoint, params=params)

    async def set_terms_acceptance(self, body: AdsCdxSolSetTermsAcceptanceRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None) -> JSONData | JSONList:
        """PATCH /adm/terms

        Set the Customer's Ads Data Manager Terms and Conditions acceptance  **Authorized resource type**: Global Manager Accoun
        """
        endpoint = "/adm/terms"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self._request('PATCH', endpoint, json_data=json_data, params=params)

