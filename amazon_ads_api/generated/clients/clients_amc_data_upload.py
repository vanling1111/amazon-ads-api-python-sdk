"""Auto-generated async API client. Do not edit manually.

Source: AdvertiserDataUpload_prod_3p.json
Title:  Advertiser Data Upload
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_amc_data_upload import *  # noqa: F403
except ImportError:
    pass


class AmcDataUploadClient(BaseAdsClient):
    """Auto-generated from AdvertiserDataUpload_prod_3p.json (14 operations)"""

    async def create_data_set(self, instance_id: str, body: CreateDataSetRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_advertising_api_scope: str | None = None, x_amzn_service_name: str | None = None, x_amzn_service_version: str | None = None) -> JSONData | JSONList:
        """POST /amc/advertiserData/{instanceId}/dataSets

        Creates a new data set. You must create a data set before you can upload data to it.  **Requires one of these permission
        """
        endpoint = f"/amc/advertiserData/{instance_id}/dataSets"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if x_amzn_service_name is not None:
            params["x-amzn-service-name"] = x_amzn_service_name
        if x_amzn_service_version is not None:
            params["x-amzn-service-version"] = x_amzn_service_version
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcadvertiserdataset.v1+json")

    async def list_data_sets(self, instance_id: str, next_token: str | None = None, max_results: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_advertising_api_scope: str | None = None, x_amzn_service_name: str | None = None, x_amzn_service_version: str | None = None) -> JSONData | JSONList:
        """POST /amc/advertiserData/{instanceId}/dataSets/list

        Gets a paginated list of data sets for a specified instance.  **Requires one of these permissions**: []
        """
        endpoint = f"/amc/advertiserData/{instance_id}/dataSets/list"
        params: dict[str, Any] = {}
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if x_amzn_service_name is not None:
            params["x-amzn-service-name"] = x_amzn_service_name
        if x_amzn_service_version is not None:
            params["x-amzn-service-version"] = x_amzn_service_version
        return await self.post(endpoint, params=params)

    async def delete_data_set(self, instance_id: str, data_set_id: str, amazon_ads_account_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_advertising_api_scope: str | None = None, x_amzn_service_name: str | None = None, x_amzn_service_version: str | None = None) -> JSONData | JSONList:
        """DELETE /amc/advertiserData/{instanceId}/dataSets/{dataSetId}

        Deletes the specified data set. WARNING: This is an irreversible action. All data associated with the data set will be d
        """
        endpoint = f"/amc/advertiserData/{instance_id}/dataSets/{data_set_id}"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if x_amzn_service_name is not None:
            params["x-amzn-service-name"] = x_amzn_service_name
        if x_amzn_service_version is not None:
            params["x-amzn-service-version"] = x_amzn_service_version
        return await self.delete(endpoint, params=params)

    async def get_data_set(self, instance_id: str, data_set_id: str, amazon_ads_account_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_advertising_api_scope: str | None = None, x_amzn_service_name: str | None = None, x_amzn_service_version: str | None = None) -> JSONData | JSONList:
        """GET /amc/advertiserData/{instanceId}/dataSets/{dataSetId}

        Gets the specified data set defintion.  **Requires one of these permissions**: []
        """
        endpoint = f"/amc/advertiserData/{instance_id}/dataSets/{data_set_id}"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if x_amzn_service_name is not None:
            params["x-amzn-service-name"] = x_amzn_service_name
        if x_amzn_service_version is not None:
            params["x-amzn-service-version"] = x_amzn_service_version
        return await self.get(endpoint, params=params)

    async def update_data_set(self, instance_id: str, data_set_id: str, body: UpdateDataSetRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_advertising_api_scope: str | None = None, x_amzn_service_name: str | None = None, x_amzn_service_version: str | None = None) -> JSONData | JSONList:
        """PUT /amc/advertiserData/{instanceId}/dataSets/{dataSetId}

        Updates the specified data set definition.  **Requires one of these permissions**: []
        """
        endpoint = f"/amc/advertiserData/{instance_id}/dataSets/{data_set_id}"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if x_amzn_service_name is not None:
            params["x-amzn-service-name"] = x_amzn_service_name
        if x_amzn_service_version is not None:
            params["x-amzn-service-version"] = x_amzn_service_version
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcadvertiserdataset.v1+json")

    async def add_column_to_data_set(self, instance_id: str, data_set_id: str, body: AddColumnToDataSetRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_advertising_api_scope: str | None = None, x_amzn_service_name: str | None = None, x_amzn_service_version: str | None = None) -> JSONData | JSONList:
        """POST /amc/advertiserData/{instanceId}/dataSets/{dataSetId}/columns

        Creates a new column and adds it to the specified data set.  **Requires one of these permissions**: []
        """
        endpoint = f"/amc/advertiserData/{instance_id}/dataSets/{data_set_id}/columns"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if x_amzn_service_name is not None:
            params["x-amzn-service-name"] = x_amzn_service_name
        if x_amzn_service_version is not None:
            params["x-amzn-service-version"] = x_amzn_service_version
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcadvertiserdatasetcolumn.v1+json")

    async def delete_column_from_data_set(self, instance_id: str, data_set_id: str, column_name: str, amazon_ads_account_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_advertising_api_scope: str | None = None, x_amzn_service_name: str | None = None, x_amzn_service_version: str | None = None) -> JSONData | JSONList:
        """DELETE /amc/advertiserData/{instanceId}/dataSets/{dataSetId}/columns/{columnName}

        Deletes a column from the specified data set.  **Requires one of these permissions**: []
        """
        endpoint = f"/amc/advertiserData/{instance_id}/dataSets/{data_set_id}/columns/{column_name}"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if x_amzn_service_name is not None:
            params["x-amzn-service-name"] = x_amzn_service_name
        if x_amzn_service_version is not None:
            params["x-amzn-service-version"] = x_amzn_service_version
        return await self.delete(endpoint, params=params)

    async def update_column_in_data_set(self, instance_id: str, data_set_id: str, column_name: str, body: UpdateColumnInDataSetRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_advertising_api_scope: str | None = None, x_amzn_service_name: str | None = None, x_amzn_service_version: str | None = None) -> JSONData | JSONList:
        """PUT /amc/advertiserData/{instanceId}/dataSets/{dataSetId}/columns/{columnName}

        Updates a column in the specified data set.  **Requires one of these permissions**: []
        """
        endpoint = f"/amc/advertiserData/{instance_id}/dataSets/{data_set_id}/columns/{column_name}"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if x_amzn_service_name is not None:
            params["x-amzn-service-name"] = x_amzn_service_name
        if x_amzn_service_version is not None:
            params["x-amzn-service-version"] = x_amzn_service_version
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcadvertiserdatasetcolumn.v1+json")

    async def list_uploads(self, instance_id: str, next_token: str | None = None, created_at: str | None = None, created_at_comparator: str | None = None, data_set_id: str | None = None, max_results: str | None = None, status: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_advertising_api_scope: str | None = None, x_amzn_service_name: str | None = None, x_amzn_service_version: str | None = None) -> JSONData | JSONList:
        """POST /amc/advertiserData/{instanceId}/uploads/list

        Gets a paginated list of previously submitted uploads for a specified instance.  **Requires one of these permissions**: 
        """
        endpoint = f"/amc/advertiserData/{instance_id}/uploads/list"
        params: dict[str, Any] = {}
        if next_token is not None:
            params["nextToken"] = next_token
        if created_at is not None:
            params["createdAt"] = created_at
        if created_at_comparator is not None:
            params["createdAtComparator"] = created_at_comparator
        if data_set_id is not None:
            params["dataSetId"] = data_set_id
        if max_results is not None:
            params["maxResults"] = max_results
        if status is not None:
            params["status"] = status
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if x_amzn_service_name is not None:
            params["x-amzn-service-name"] = x_amzn_service_name
        if x_amzn_service_version is not None:
            params["x-amzn-service-version"] = x_amzn_service_version
        return await self.post(endpoint, params=params)

    async def create_upload(self, instance_id: str, data_set_id: str, body: CreateUploadRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_advertising_api_scope: str | None = None, x_amzn_service_name: str | None = None, x_amzn_service_version: str | None = None) -> JSONData | JSONList:
        """POST /amc/advertiserData/{instanceId}/uploads/{dataSetId}

        Creates a asynchronous job to upload data to an Amazon Marketing Cloud instance. The request body is used as the definit
        """
        endpoint = f"/amc/advertiserData/{instance_id}/uploads/{data_set_id}"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if x_amzn_service_name is not None:
            params["x-amzn-service-name"] = x_amzn_service_name
        if x_amzn_service_version is not None:
            params["x-amzn-service-version"] = x_amzn_service_version
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcadvertiserdataupload.v1+json")

    async def get_upload(self, instance_id: str, data_set_id: str, upload_id: str, amazon_ads_account_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_advertising_api_scope: str | None = None, x_amzn_service_name: str | None = None, x_amzn_service_version: str | None = None) -> JSONData | JSONList:
        """GET /amc/advertiserData/{instanceId}/uploads/{dataSetId}/{uploadId}

        Gets the details of a previously submitted upload.  **Requires one of these permissions**: []
        """
        endpoint = f"/amc/advertiserData/{instance_id}/uploads/{data_set_id}/{upload_id}"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if x_amzn_service_name is not None:
            params["x-amzn-service-name"] = x_amzn_service_name
        if x_amzn_service_version is not None:
            params["x-amzn-service-version"] = x_amzn_service_version
        return await self.get(endpoint, params=params)

    async def create_user_deletion_request(self, instance_id: str, body: CreateUserDeletionRequestRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_advertising_api_scope: str | None = None, x_amzn_service_name: str | None = None, x_amzn_service_version: str | None = None) -> JSONData | JSONList:
        """POST /amc/advertiserData/{instanceId}/userDeletionRequest

        Creates a request for user deletion given an input set of user identities. Initiates a deletion of these identities from
        """
        endpoint = f"/amc/advertiserData/{instance_id}/userDeletionRequest"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if x_amzn_service_name is not None:
            params["x-amzn-service-name"] = x_amzn_service_name
        if x_amzn_service_version is not None:
            params["x-amzn-service-version"] = x_amzn_service_version
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcadvertiseruserdeletionrequest.v1+json")

    async def list_user_deletion_requests(self, instance_id: str, next_token: str | None = None, max_results: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_advertising_api_scope: str | None = None, x_amzn_service_name: str | None = None, x_amzn_service_version: str | None = None) -> JSONData | JSONList:
        """POST /amc/advertiserData/{instanceId}/userDeletionRequest/list

        Gets a paginated list of all user deletion requests for a specified instance.  **Requires one of these permissions**: []
        """
        endpoint = f"/amc/advertiserData/{instance_id}/userDeletionRequest/list"
        params: dict[str, Any] = {}
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if x_amzn_service_name is not None:
            params["x-amzn-service-name"] = x_amzn_service_name
        if x_amzn_service_version is not None:
            params["x-amzn-service-version"] = x_amzn_service_version
        return await self.post(endpoint, params=params)

    async def get_user_deletion_request(self, instance_id: str, user_deletion_request_id: str, amazon_ads_account_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_advertising_api_scope: str | None = None, x_amzn_service_name: str | None = None, x_amzn_service_version: str | None = None) -> JSONData | JSONList:
        """GET /amc/advertiserData/{instanceId}/userDeletionRequest/{userDeletionRequestId}

        Gets available metadata about a previously initiated user deletion.  **Requires one of these permissions**: []
        """
        endpoint = f"/amc/advertiserData/{instance_id}/userDeletionRequest/{user_deletion_request_id}"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if x_amzn_service_name is not None:
            params["x-amzn-service-name"] = x_amzn_service_name
        if x_amzn_service_version is not None:
            params["x-amzn-service-version"] = x_amzn_service_version
        return await self.get(endpoint, params=params)

