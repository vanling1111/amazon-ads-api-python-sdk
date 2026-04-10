"""Auto-generated async API client. Do not edit manually.

Source: AMCCustomModels_prod_3p.json
Title:  AMC Custom Models
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_amc_custom_models import *  # noqa: F403
except ImportError:
    pass


class AmcCustomModelsClient(BaseAdsClient):
    """Auto-generated from AMCCustomModels_prod_3p.json (23 operations)"""

    async def create_ml_data_export_v2(self, body: AMCModelBasedAudienceCreateMlDataExportInput | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/models/v1/mlDataExports

        Creates workflow to export ML data for model-based audiences.
        """
        endpoint = "/amc/models/v1/mlDataExports"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcmodelbasedaudience.v1+json")

    async def list_ml_data_export_v2(self, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None, max_results: str | None = None, next_token: str | None = None) -> JSONData | JSONList:
        """POST /amc/models/v1/mlDataExports/list

        List MlDataExport metadata.
        """
        endpoint = "/amc/models/v1/mlDataExports/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        if max_results is not None:
            params["maxResults"] = max_results
        if next_token is not None:
            params["nextToken"] = next_token
        return await self.post(endpoint, params=params)

    async def get_ml_data_export_v2(self, ml_data_export_id: str, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/models/v1/mlDataExports/{mlDataExportId}

        Get MlDataExport metadata for a given mlDataExportId.
        """
        endpoint = f"/amc/models/v1/mlDataExports/{ml_data_export_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        return await self.get(endpoint, params=params)

    async def create_ml_input_channel_v2(self, body: AMCModelBasedAudienceCreateMlInputChannelInput | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/models/v1/mlInputChannels

        Creates workflow to create a MlInputChannel for model-based audiences.
        """
        endpoint = "/amc/models/v1/mlInputChannels"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcmodelbasedaudience.v1+json")

    async def list_ml_input_channel_by_instance_id_v2(self, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None, max_results: str | None = None, next_token: str | None = None) -> JSONData | JSONList:
        """POST /amc/models/v1/mlInputChannels/list

        List MlInputChannel metadata.
        """
        endpoint = "/amc/models/v1/mlInputChannels/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        if max_results is not None:
            params["maxResults"] = max_results
        if next_token is not None:
            params["nextToken"] = next_token
        return await self.post(endpoint, params=params)

    async def delete_ml_input_channel_v2(self, ml_input_channel_id: str, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None) -> JSONData | JSONList:
        """DELETE /amc/models/v1/mlInputChannels/{mlInputChannelId}

        Delete MlInputChannel metadata for a given mlInputChannelId.
        """
        endpoint = f"/amc/models/v1/mlInputChannels/{ml_input_channel_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        return await self.delete(endpoint, params=params)

    async def get_ml_input_channel_v2(self, ml_input_channel_id: str, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/models/v1/mlInputChannels/{mlInputChannelId}

        Get MlInputChannel metadata for a given mlInputChannelId.
        """
        endpoint = f"/amc/models/v1/mlInputChannels/{ml_input_channel_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        return await self.get(endpoint, params=params)

    async def create_modeled_dataset_upload_job_v2(self, body: AMCModelBasedAudienceCreateModeledDatasetUploadJobInput | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/models/v1/modeledDatasetUploadJobs

        Creates workflow to create a ModeledDatasetUploadJob for model-based audiences.
        """
        endpoint = "/amc/models/v1/modeledDatasetUploadJobs"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcmodelbasedaudience.v1+json")

    async def list_modeled_dataset_upload_job_v2(self, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None, max_results: str | None = None, next_token: str | None = None) -> JSONData | JSONList:
        """POST /amc/models/v1/modeledDatasetUploadJobs/list

        List ModeledDatasetUploadJob metadata.
        """
        endpoint = "/amc/models/v1/modeledDatasetUploadJobs/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        if max_results is not None:
            params["maxResults"] = max_results
        if next_token is not None:
            params["nextToken"] = next_token
        return await self.post(endpoint, params=params)

    async def get_modeled_dataset_upload_job_v2(self, modeled_dataset_upload_job_id: str, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/models/v1/modeledDatasetUploadJobs/{modeledDatasetUploadJobId}

        Get ModeledDatasetUploadJob metadata for a given modeledDatasetUploadJobId.
        """
        endpoint = f"/amc/models/v1/modeledDatasetUploadJobs/{modeled_dataset_upload_job_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        return await self.get(endpoint, params=params)

    async def create_modeled_dataset_v2(self, body: AMCModelBasedAudienceCreateModeledDatasetInput | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/models/v1/modeledDatasets

        Creates workflow to create a ModeledDataset for model-based audiences.
        """
        endpoint = "/amc/models/v1/modeledDatasets"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcmodelbasedaudience.v1+json")

    async def list_modeled_dataset_v2(self, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None, max_results: str | None = None, next_token: str | None = None) -> JSONData | JSONList:
        """POST /amc/models/v1/modeledDatasets/list

        List ModeledDataset metadata.
        """
        endpoint = "/amc/models/v1/modeledDatasets/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        if max_results is not None:
            params["maxResults"] = max_results
        if next_token is not None:
            params["nextToken"] = next_token
        return await self.post(endpoint, params=params)

    async def delete_modeled_dataset_v2(self, modeled_dataset_id: str, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None) -> JSONData | JSONList:
        """DELETE /amc/models/v1/modeledDatasets/{modeledDatasetId}

        Delete ModeledDataset metadata for a given modeledDatasetId.
        """
        endpoint = f"/amc/models/v1/modeledDatasets/{modeled_dataset_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        return await self.delete(endpoint, params=params)

    async def get_modeled_dataset_v2(self, modeled_dataset_id: str, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/models/v1/modeledDatasets/{modeledDatasetId}

        Get ModeledDataset metadata for a given modeledDatasetId.
        """
        endpoint = f"/amc/models/v1/modeledDatasets/{modeled_dataset_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        return await self.get(endpoint, params=params)

    async def create_trained_model_inference_job_v2(self, body: AMCModelBasedAudienceTrainedModelInferenceJobRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/models/v1/trainedModelInferenceJobs

        Creates workflow to create a TrainedModelInferenceJob for model-based audiences.
        """
        endpoint = "/amc/models/v1/trainedModelInferenceJobs"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcmodelbasedaudience.v1+json")

    async def list_trained_model_inference_job_by_instance_id_v2(self, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None, max_results: str | None = None, next_token: str | None = None) -> JSONData | JSONList:
        """POST /amc/models/v1/trainedModelInferenceJobs/list

        List TrainedModelInferenceJob metadata.
        """
        endpoint = "/amc/models/v1/trainedModelInferenceJobs/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        if max_results is not None:
            params["maxResults"] = max_results
        if next_token is not None:
            params["nextToken"] = next_token
        return await self.post(endpoint, params=params)

    async def get_trained_model_inference_job_v2(self, trained_model_inference_job_id: str, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/models/v1/trainedModelInferenceJobs/{trainedModelInferenceJobId}

        Get TrainedModelInferenceJob metadata for a given trainedModelInferenceJobId.
        """
        endpoint = f"/amc/models/v1/trainedModelInferenceJobs/{trained_model_inference_job_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        return await self.get(endpoint, params=params)

    async def cancel_trained_model_inference_job_v2(self, trained_model_inference_job_id: str, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/models/v1/trainedModelInferenceJobs/{trainedModelInferenceJobId}/cancel

        Cancel TrainedModelInferenceJob for a given trainedModelInferenceJobId.
        """
        endpoint = f"/amc/models/v1/trainedModelInferenceJobs/{trained_model_inference_job_id}/cancel"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        return await self.post(endpoint, params=params)

    async def create_trained_model_v2(self, body: AMCModelBasedAudienceCreateTrainedModelInput | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/models/v1/trainedModels

        Creates a workflow to create a TrainedModel for model-based audiences.
        """
        endpoint = "/amc/models/v1/trainedModels"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.amcmodelbasedaudience.v1+json")

    async def list_trained_models_by_instance_id_v2(self, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None, max_results: str | None = None, next_token: str | None = None) -> JSONData | JSONList:
        """POST /amc/models/v1/trainedModels/list

        List TrainedModel metadata.
        """
        endpoint = "/amc/models/v1/trainedModels/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        if max_results is not None:
            params["maxResults"] = max_results
        if next_token is not None:
            params["nextToken"] = next_token
        return await self.post(endpoint, params=params)

    async def delete_trained_model_v2(self, trained_model_id: str, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None) -> JSONData | JSONList:
        """DELETE /amc/models/v1/trainedModels/{trainedModelId}

        Delete TrainedModel metadata for a given trainedModelId.
        """
        endpoint = f"/amc/models/v1/trainedModels/{trained_model_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        return await self.delete(endpoint, params=params)

    async def get_trained_model_by_trained_model_id_v2(self, trained_model_id: str, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None) -> JSONData | JSONList:
        """GET /amc/models/v1/trainedModels/{trainedModelId}

        Get TrainedModel metadata for a given trainedModelId.
        """
        endpoint = f"/amc/models/v1/trainedModels/{trained_model_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        return await self.get(endpoint, params=params)

    async def cancel_trained_model_v2(self, trained_model_id: str, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_marketing_cloud_instance_id: str | None = None) -> JSONData | JSONList:
        """POST /amc/models/v1/trainedModels/{trainedModelId}/cancel

        Cancel TrainedModel for a given trainedModelId.
        """
        endpoint = f"/amc/models/v1/trainedModels/{trained_model_id}/cancel"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_marketing_cloud_instance_id is not None:
            params["Amazon-Marketing-Cloud-InstanceId"] = amazon_marketing_cloud_instance_id
        return await self.post(endpoint, params=params)

