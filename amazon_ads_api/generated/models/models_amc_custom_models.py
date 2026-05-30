"""Auto-generated Pydantic models. Do not edit manually.

Source: AMCCustomModels_prod_3p.json
Title:  AMC Custom Models
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class AMCModelBasedAudienceCMAAArn(BaseModel):
    """The ARN returned when the customer associates an algorithm with a membership."""
    pass


class AMCModelBasedAudienceConfiguredModelAlgorithmAssociations(BaseModel):
    """The ARN returned when the customer associates an algorithm with a membership."""
    pass


class AMCModelBasedAudienceCreateMlDataExportInput(BaseModel):
    """Create MlDataExport input"""
    data_type: Optional[str] = Field(None, alias="dataType", description="The data type that needs to be exported")
    inference_job_id: Optional[str] = Field(None, alias="inferenceJobId", description="InferenceJobId to export data from")
    trained_model_id: Optional[str] = Field(None, alias="trainedModelId", description="TrainedModelId to export data from")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceMlDataExportId(BaseModel):
    """MlDataExportId"""
    pass


class AMCModelBasedAudienceCreateMlDataExportOutput(BaseModel):
    """Response on a successful creation of a MlDAtaExport create."""
    ml_data_export_id: "AMCModelBasedAudienceMlDataExportId" = Field(..., alias="mlDataExportId")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceIdempotencyKey(BaseModel):
    """Idempotency key to prevent duplicate records."""
    pass


class ComplexDataType(BaseModel):
    pass


class SimpleDataType(BaseModel):
    pass


class DataTypes(BaseModel):
    pass


class QueryBasedAudienceInputParam(BaseModel):
    """'Optional. Defines the parameters that can be referenced by workflow. definition. If workflow references a parameter not defined here the compilation fails.'"""
    pass


class AMCModelBasedAudienceQueryParameters(BaseModel):
    """Defines the AMC query to run against AMC data whose output will be used for model training."""
    amc_query: str = Field(..., alias="amcQuery", description="Customer created query to run on AMC instance.")
    input_parameters: Optional["QueryBasedAudienceInputParam"] = Field(None, alias="inputParameters")
    parameter_values: Optional[dict[str, Any]] = Field(None, alias="parameterValues", description="Custom parameters specified in the query.")
    time_window_end: str = Field(..., alias="timeWindowEnd", description="Ending date of data to query. This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss'Z'.")
    time_window_start: str = Field(..., alias="timeWindowStart", description="Starting date of data to query. This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss'Z'.")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceCreateMlInputChannelInput(BaseModel):
    """Model based audience MlInputChannel create input"""
    configured_model_algorithm_associations: Optional["AMCModelBasedAudienceConfiguredModelAlgorithmAssociations"] = Field(None, alias="configuredModelAlgorithmAssociations")
    enforce_aggregation_thresholds: Optional[bool] = Field(None, alias="enforceAggregationThresholds", description="Optional. If the enforceAggregationThresholds option is enabled, the system will ensure SQL query and the resulting data")
    enforce_user_level_targeting: Optional[bool] = Field(None, alias="enforceUserLevelTargeting", description="If the enforceUserLevelTargeting option is enabled, the system will ensure that the it  only uses data sources relevant ")
    idempotency_key: Optional["AMCModelBasedAudienceIdempotencyKey"] = Field(None, alias="idempotencyKey")
    name: str = Field(..., description="The name of MlInputChannel.")
    query_parameters: "AMCModelBasedAudienceQueryParameters" = Field(..., alias="queryParameters")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceMlInputChannelId(BaseModel):
    """A unique ID that represents an AMCMlInputChannel object"""
    pass


class AMCModelBasedAudienceCreateMlInputChannelOut(BaseModel):
    """Model based audience MlInputChannel create output"""
    ml_input_channel_id: "AMCModelBasedAudienceMlInputChannelId" = Field(..., alias="mlInputChannelId")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceModeledDatasetTableColumn(BaseModel):
    """Object to store tableColumn"""
    column_name: str = Field(..., alias="columnName")
    data_type: str = Field(..., alias="dataType")
    description: Optional[str] = None
    user_id_column: bool = Field(..., alias="userIdColumn", description="True for only one column. The one that contains ad user id. If true, dataType must be STRING. Optional, defaults to fals")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceModeledDatasetSchema(BaseModel):
    """ModeledDataset schema"""
    table_columns: list["AMCModelBasedAudienceModeledDatasetTableColumn"] = Field(..., alias="tableColumns", description="a list of tableColumn")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceCreateModeledDatasetInput(BaseModel):
    """Create ModeledDataset input"""
    description: Optional[str] = Field(None, description="The description of the ModeledDataset")
    name: str = Field(..., description="The name of the ModeledDataset")
    schema: "AMCModelBasedAudienceModeledDatasetSchema"

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceModeledDatasetId(BaseModel):
    """Identifier that uniquely represents an AMC model based audience modeled dataset"""
    pass


class AMCModelBasedAudienceCreateModeledDatasetOutput(BaseModel):
    """Response on a successful creation of a ModeledDataset."""
    modeled_dataset_id: "AMCModelBasedAudienceModeledDatasetId" = Field(..., alias="modeledDatasetId")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceTrainedModelInferenceJobId(BaseModel):
    """A unique ID that represents a trained model inference job"""
    pass


class AMCModelBasedAudienceTrainedModelInferenceJobIds(BaseModel):
    """A list of trainedModelInferenceJobIds"""
    pass


class AMCModelBasedAudienceTrainedModelId(BaseModel):
    """Identifier that uniquely represents an AMC model based audience trained model."""
    pass


class AMCModelBasedAudienceTrainedModelIds(BaseModel):
    """A list of trainedModelIds"""
    pass


class AMCModelBasedAudienceModeledDatasetUploadJobUpdateStrategy(StrEnum):
    ADDITIVE = "ADDITIVE"
    FULL_REPLACE = "FULL_REPLACE"


class AMCModelBasedAudienceCreateModeledDatasetUploadJobInput(BaseModel):
    """CreateModeledDatasetUploadJobInput"""
    inference_job_ids: Optional["AMCModelBasedAudienceTrainedModelInferenceJobIds"] = Field(None, alias="inferenceJobIds")
    modeled_dataset_id: "AMCModelBasedAudienceModeledDatasetId" = Field(..., alias="modeledDatasetId")
    trained_model_ids: Optional["AMCModelBasedAudienceTrainedModelIds"] = Field(None, alias="trainedModelIds")
    update_strategy: Optional["AMCModelBasedAudienceModeledDatasetUploadJobUpdateStrategy"] = Field(None, alias="updateStrategy")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceModeledDatasetUploadJobId(BaseModel):
    """Identifier that uniquely represents an AMC model based audience modeled dataset upload job"""
    pass


class AMCModelBasedAudienceCreateModeledDatasetUploadJobOutput(BaseModel):
    """Response on a successful creation of a ModeledDataset."""
    modeled_dataset_upload_job_id: "AMCModelBasedAudienceModeledDatasetUploadJobId" = Field(..., alias="modeledDatasetUploadJobId")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceEnvironment(BaseModel):
    """The environment variables to set in the Docker container."""
    __root__: dict[str, str] = {}


class AMCModelBasedAudienceResourceConfig(BaseModel):
    """Configuration options for an training resource."""
    instance_count: Optional[int] = Field(None, alias="instanceCount", description="instanceCount of training resource.")
    instance_type: Optional[str] = Field(None, alias="instanceType")
    volume_size_in_gb: Optional[int] = Field(None, alias="volumeSizeInGb", description="The volume size in gigabytes (GB) of the training resource. Note that volume size limits depend on your instance type. C")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceMlInputChannel(BaseModel):
    """A named input source that the container will consume. This is the location of the output of the query."""
    channel_name: str = Field(..., alias="channelName")
    ml_input_channel_id: str = Field(..., alias="mlInputChannelId")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceMlInputChannels(BaseModel):
    """a list of mlInputChannels"""
    pass


class AMCModelBasedAudienceStoppingCondition(BaseModel):
    """Specifies a limit to how long a model training job can run."""
    max_runtime_in_seconds: Optional[int] = Field(None, alias="maxRuntimeInSeconds", description="The maximum length of time, in seconds, that a model can train before it is stopped. Minimum value of 1")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceHyperParameters(BaseModel):
    """Algorithm-specific parameters that influence the quality of the model."""
    __root__: dict[str, str] = {}


class AMCModelBasedAudienceIncrementalTrainingDataChannel(BaseModel):
    """A named input source that the container will consume. This is the location of a model which will be used for incremental training."""
    channel_name: str = Field(..., alias="channelName")
    trained_model_id: str = Field(..., alias="trainedModelId")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceIncrementalTrainingDataChannels(BaseModel):
    """A list of trained models to perform incremental training against."""
    pass


class AMCModelBasedAudienceCreateTrainedModelInput(BaseModel):
    """Model based audience trained model execution metadata information."""
    configured_model_algorithm_association_arn: "AMCModelBasedAudienceCMAAArn" = Field(..., alias="configuredModelAlgorithmAssociationArn")
    description: Optional[str] = Field(None, description="Customer provided description for a trained model.")
    enforce_anonymized_results: Optional[bool] = Field(None, alias="enforceAnonymizedResults", description="Optional. If the enforceAnonymizedResults option is enabled, the system will ensure that the training and inference proc")
    enforce_user_level_targeting: Optional[bool] = Field(None, alias="enforceUserLevelTargeting", description="If the enforceUserLevelTargeting option is enabled, the system will ensure that the training process only uses data sour")
    environment: Optional["AMCModelBasedAudienceEnvironment"] = None
    hyper_parameters: Optional["AMCModelBasedAudienceHyperParameters"] = Field(None, alias="hyperParameters")
    idempotency_key: Optional["AMCModelBasedAudienceIdempotencyKey"] = Field(None, alias="idempotencyKey")
    incremental_training_data_channels: Optional["AMCModelBasedAudienceIncrementalTrainingDataChannels"] = Field(None, alias="incrementalTrainingDataChannels")
    ml_input_channels: Optional["AMCModelBasedAudienceMlInputChannels"] = Field(None, alias="mlInputChannels")
    name: str = Field(..., description="Customer provided name for a trained model.")
    resource_config: Optional["AMCModelBasedAudienceResourceConfig"] = Field(None, alias="resourceConfig")
    stopping_condition: Optional["AMCModelBasedAudienceStoppingCondition"] = Field(None, alias="stoppingCondition")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceCreateTrainedModelOutput(BaseModel):
    """Response on a successful creation of a TrainedModel."""
    trained_model_id: "AMCModelBasedAudienceTrainedModelId" = Field(..., alias="trainedModelId")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceMlDataExportPresignedUrls(BaseModel):
    pass


class MlDataExportStatus(StrEnum):
    CREATE_FAILED = "CREATE_FAILED"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_SUCCEEDED = "CREATE_SUCCEEDED"


class AMCModelBasedAudienceGetMlDataExportOutput(BaseModel):
    """Model based audience MLDataExport metadata information."""
    create_time: str = Field(..., alias="createTime", description="Timestamp of when the mlDataExport request was submitted. This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss")
    ml_data_export_id: "AMCModelBasedAudienceMlDataExportId" = Field(..., alias="mlDataExportId")
    pre_signed_error_s3_uri: Optional[str] = Field(None, alias="preSignedErrorS3Uri", description="Presigned S3 url to download the error file.")
    pre_signed_s3_uris: Optional["AMCModelBasedAudienceMlDataExportPresignedUrls"] = Field(None, alias="preSignedS3Uris")
    status: "MlDataExportStatus"
    status_reason: Optional[str] = Field(None, alias="statusReason", description="Description of why the execution is in FAILED state.")
    valid_until: Optional[str] = Field(None, alias="validUntil", description="Timestamp of when the mlDataExport request will be valid until. This field is in UTC and is formatted as yyyy-MM-dd'T'HH")

    model_config = {'populate_by_name': True}


class ModeledDatasetStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CREATE_FAILED = "CREATE_FAILED"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    INACTIVE = "INACTIVE"


class AMCModelBasedAudienceGetModeledDatasetOutput(BaseModel):
    """Model based audience trained model inference job execution metadata information."""
    create_time: str = Field(..., alias="createTime", description="Timestamp of when the modeled dataset request was submitted.This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:")
    description: Optional[str] = Field(None, description="The description of the ModeledDataset")
    modeled_dataset_id: Optional["AMCModelBasedAudienceModeledDatasetId"] = Field(None, alias="modeledDatasetId")
    name: str = Field(..., description="The name of the ModeledDataset")
    schema: "AMCModelBasedAudienceModeledDatasetSchema"
    status: "ModeledDatasetStatus"
    status_reason: Optional[str] = Field(None, alias="statusReason", description="Description of why the execution is in FAILED state.")

    model_config = {'populate_by_name': True}


class ModeledDatasetUploadJobStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CREATE_FAILED = "CREATE_FAILED"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    INACTIVE = "INACTIVE"


class AMCModelBasedAudienceGetModeledDatasetUploadJobOutput(BaseModel):
    """Model based audience trained model inference job execution metadata information."""
    estimated_row_count: int = Field(..., alias="estimatedRowCount")
    inference_job_ids: Optional["AMCModelBasedAudienceTrainedModelInferenceJobIds"] = Field(None, alias="inferenceJobIds")
    modeled_dataset_id: Optional["AMCModelBasedAudienceModeledDatasetId"] = Field(None, alias="modeledDatasetId")
    modeled_dataset_upload_job_id: "AMCModelBasedAudienceModeledDatasetUploadJobId" = Field(..., alias="modeledDatasetUploadJobId")
    status: "ModeledDatasetUploadJobStatus"
    status_reason: Optional[str] = Field(None, alias="statusReason", description="Description of why the execution is in FAILED state.")
    trained_model_ids: Optional["AMCModelBasedAudienceTrainedModelIds"] = Field(None, alias="trainedModelIds")
    update_strategy: Optional["AMCModelBasedAudienceModeledDatasetUploadJobUpdateStrategy"] = Field(None, alias="updateStrategy")

    model_config = {'populate_by_name': True}


class InferenceJobContainerExecutionParameters(BaseModel):
    """Container execution parameters for an inference job."""
    max_payload_in_mb: Optional[int] = Field(None, alias="maxPayloadInMb")

    model_config = {'populate_by_name': True}


class TrainedModelInferenceJobStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CANCEL_FAILED = "CANCEL_FAILED"
    CANCEL_IN_PROGRESS = "CANCEL_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    INACTIVE = "INACTIVE"
    QUEUED = "QUEUED"


class PublishStatus(StrEnum):
    PUBLISH_FAILED = "PUBLISH_FAILED"
    PUBLISH_SUCCEEDED = "PUBLISH_SUCCEEDED"


class InferenceJobResourceConfig(BaseModel):
    """Configuration options for an inference resource."""
    instance_count: Optional[int] = Field(None, alias="instanceCount")
    instance_type: Optional[str] = Field(None, alias="instanceType")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceGetTrainedModelInferenceJobOutput(BaseModel):
    """Model based audience trained model inference job execution metadata information."""
    configured_model_algorithm_association_arn: "AMCModelBasedAudienceCMAAArn" = Field(..., alias="configuredModelAlgorithmAssociationArn")
    container_execution_parameters: Optional["InferenceJobContainerExecutionParameters"] = Field(None, alias="containerExecutionParameters")
    create_time: Optional[str] = Field(None, alias="createTime", description="Timestamp of when the trained model request was submitted.This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss")
    description: Optional[str] = Field(None, description="Description of the trained model inference job")
    enforce_anonymized_results: Optional[bool] = Field(None, alias="enforceAnonymizedResults", description="Optional. If the enforceAnonymizedResults option is enabled, the system will ensure that the training and inference proc")
    enforce_user_level_targeting: Optional[bool] = Field(None, alias="enforceUserLevelTargeting", description="If the enforceUserLevelTargeting option is enabled, the system will ensure that the inference process only uses data sou")
    instance_id: str = Field(..., alias="instanceId", description="AMC instance identifier.")
    logs_status: Optional["PublishStatus"] = Field(None, alias="logsStatus")
    logs_status_details: Optional[str] = Field(None, alias="logsStatusDetails", description="Detailed information about logs publishing status, especially useful when logsStatus is PUBLISH_FAILED")
    metrics_status: Optional["PublishStatus"] = Field(None, alias="metricsStatus")
    metrics_status_details: Optional[str] = Field(None, alias="metricsStatusDetails", description="Detailed information about metrics publishing status, especially useful when metricsStatus is PUBLISH_FAILED")
    ml_input_channel_id: "AMCModelBasedAudienceMlInputChannelId" = Field(..., alias="mlInputChannelId")
    name: Optional[str] = Field(None, description="Name of the trained model inference job")
    resource_config: Optional["InferenceJobResourceConfig"] = Field(None, alias="resourceConfig")
    status: "TrainedModelInferenceJobStatus"
    status_reason: Optional[str] = Field(None, alias="statusReason", description="The error message when the status is FAILED. Algorithm errors include an S3 URL to retrieve the error summary if you hav")
    trained_model_id: "AMCModelBasedAudienceTrainedModelId" = Field(..., alias="trainedModelId")
    trained_model_inference_job_id: "AMCModelBasedAudienceTrainedModelInferenceJobId" = Field(..., alias="trainedModelInferenceJobId")

    model_config = {'populate_by_name': True}


class TrainedModelStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CREATE_FAILED = "CREATE_FAILED"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    INACTIVE = "INACTIVE"
    QUEUED = "QUEUED"


class AMCModelBasedAudienceGetTrainedModelOutput(BaseModel):
    """Model based audience trained model execution metadata information."""
    audience_eligible: Optional[bool] = Field(None, alias="audienceEligible", description="Indicates if the TrainedModel can be used for audience generation.")
    configured_model_algorithm_association_arn: "AMCModelBasedAudienceCMAAArn" = Field(..., alias="configuredModelAlgorithmAssociationArn")
    create_time: str = Field(..., alias="createTime", description="Timestamp of when the trained model request was submitted.This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss")
    data_export_eligible: Optional[bool] = Field(None, alias="dataExportEligible", description="Indicates if the TrainedModel can be used for modeled output data exports generation.  You must create the TrainedModel ")
    description: Optional[str] = Field(None, description="Customer provided description for a trained model.")
    environment: Optional["AMCModelBasedAudienceEnvironment"] = None
    hyper_parameters: Optional["AMCModelBasedAudienceHyperParameters"] = Field(None, alias="hyperParameters")
    incremental_training_data_channels: Optional["AMCModelBasedAudienceIncrementalTrainingDataChannels"] = Field(None, alias="incrementalTrainingDataChannels")
    instance_id: Optional[str] = Field(None, alias="instanceId", description="AMC instance identifier.")
    logs_status: Optional["PublishStatus"] = Field(None, alias="logsStatus")
    logs_status_details: Optional[str] = Field(None, alias="logsStatusDetails", description="Detailed information about logs publishing status, especially useful when logsStatus is PUBLISH_FAILED")
    metrics_status: Optional["PublishStatus"] = Field(None, alias="metricsStatus")
    metrics_status_details: Optional[str] = Field(None, alias="metricsStatusDetails", description="Detailed information about metrics publishing status, especially useful when metricsStatus is PUBLISH_FAILED")
    ml_input_channels: Optional["AMCModelBasedAudienceMlInputChannels"] = Field(None, alias="mlInputChannels")
    name: str = Field(..., description="Customer provided name for a trained model.")
    resource_config: Optional["AMCModelBasedAudienceResourceConfig"] = Field(None, alias="resourceConfig")
    status: "TrainedModelStatus"
    status_reason: Optional[str] = Field(None, alias="statusReason", description="The error message when the status is FAILED. Algorithm errors include an S3 URL to retrieve the error summary if you hav")
    stopping_condition: Optional["AMCModelBasedAudienceStoppingCondition"] = Field(None, alias="stoppingCondition")
    trained_model_id: "AMCModelBasedAudienceTrainedModelId" = Field(..., alias="trainedModelId")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceListMlDataExportOutput(BaseModel):
    ml_data_export_list: Optional[list["AMCModelBasedAudienceGetMlDataExportOutput"]] = Field(None, alias="mlDataExportList", description="A list of mlDataExport metadata")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to use in subsequent request to retrieve next page of results. Field will be null if all results have been returne")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceListModeledDatasetOutput(BaseModel):
    modeled_dataset_list: Optional[list["AMCModelBasedAudienceGetModeledDatasetOutput"]] = Field(None, alias="modeledDatasetList", description="A list of ModeledDataset metadata")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to use in subsequent request to retrieve next page of results. Field will be null if all results have been returne")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceListModeledDatasetUploadJobsOutput(BaseModel):
    modeled_dataset_upload_job_list: Optional[list["AMCModelBasedAudienceGetModeledDatasetUploadJobOutput"]] = Field(None, alias="modeledDatasetUploadJobList", description="Paginated list of ModeledDatasetUploadJobs")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to use in subsequent request to retrieve next page of results. Field will be null if all results have been returne")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceListTrainedModelInferenceJobOutput(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to use in subsequent request to retrieve next page of results. Field will be null if all results have been returne")
    trained_model_inference_job_list: Optional[list["AMCModelBasedAudienceGetTrainedModelInferenceJobOutput"]] = Field(None, alias="trainedModelInferenceJobList", description="List of the AMC model based audience trained model inference job for a given instanceId.")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceListTrainedModelsOutput(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to use in subsequent request to retrieve next page of results. Field will be null if all results have been returne")
    trained_model_metadata_list: Optional[list["AMCModelBasedAudienceGetTrainedModelOutput"]] = Field(None, alias="trainedModelMetadataList", description="List of the AMC model based audience trained models for a given instanceId.")

    model_config = {'populate_by_name': True}


class MlInputChannelStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CREATE_FAILED = "CREATE_FAILED"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    INACTIVE = "INACTIVE"
    QUEUED = "QUEUED"


class AMCModelBasedAudienceMlInputChannelExecutionMetadata(BaseModel):
    """MlInputChannelExecutionMetadata"""
    approximate_record_count: Optional[str] = Field(None, alias="approximateRecordCount", description="The approximate record count.")
    approximate_size_on_disk: Optional[str] = Field(None, alias="approximateSizeOnDisk", description="The approximate size of the data result on disk.")
    configured_model_algorithm_associations: "AMCModelBasedAudienceConfiguredModelAlgorithmAssociations" = Field(..., alias="configuredModelAlgorithmAssociations")
    create_time: str = Field(..., alias="createTime", description="Timestamp of when the trained model request was submitted.This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss")
    enforce_aggregation_thresholds: Optional[bool] = Field(None, alias="enforceAggregationThresholds", description="Optional. If the enforceAggregationThresholds option is enabled, the system will ensure SQL query and the resulting data")
    enforce_user_level_targeting: Optional[bool] = Field(None, alias="enforceUserLevelTargeting", description="If the enforceUserLevelTargeting option is enabled, the system will ensure that the training process only uses data sour")
    expiration_time_in_utc: Optional[str] = Field(None, alias="expirationTimeInUtc", description="The expiration time of MlInputChannel")
    instance_id: str = Field(..., alias="instanceId", description="AMC instance identifier.")
    is_audience_eligible: Optional[bool] = Field(None, alias="isAudienceEligible", description="Indicates if the data source can be used for audience generation.")
    ml_input_channel_id: "AMCModelBasedAudienceMlInputChannelId" = Field(..., alias="mlInputChannelId")
    name: str = Field(..., description="The name for the ml input data.")
    number_of_files: Optional[int] = Field(None, alias="numberOfFiles", description="The number of files in the MlInputChannel.")
    query_parameters: "AMCModelBasedAudienceQueryParameters" = Field(..., alias="queryParameters")
    status: "MlInputChannelStatus"
    status_reason: Optional[str] = Field(None, alias="statusReason", description="Description of why the execution is in FAILED state.")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceMlInputChannelMetadataList(BaseModel):
    ml_input_channel_metadata_list: Optional[list["AMCModelBasedAudienceMlInputChannelExecutionMetadata"]] = Field(None, alias="mlInputChannelMetadataList", description="A list of MlInputChannelMetadata")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to use in subsequent request to retrieve next page of results. Field will be null if all results have been returne")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceTrainedModelInferenceJobRequest(BaseModel):
    """Model based audience TrainedModelInferenceJob execution metadata information."""
    configured_model_algorithm_association_arn: Optional["AMCModelBasedAudienceCMAAArn"] = Field(None, alias="configuredModelAlgorithmAssociationArn")
    container_execution_parameters: Optional["InferenceJobContainerExecutionParameters"] = Field(None, alias="containerExecutionParameters")
    description: Optional[str] = Field(None, description="Description of the trained model inference job")
    enforce_anonymized_results: Optional[bool] = Field(None, alias="enforceAnonymizedResults", description="Optional. If the enforceAnonymizedResults option is enabled, the system will ensure that the training and inference proc")
    enforce_user_level_targeting: bool = Field(..., alias="enforceUserLevelTargeting", description="If the enforceUserLevelTargeting option is enabled, the system will ensure that the inference process only uses data sou")
    environment: Optional["AMCModelBasedAudienceEnvironment"] = None
    idempotency_key: Optional["AMCModelBasedAudienceIdempotencyKey"] = Field(None, alias="idempotencyKey")
    ml_input_channel_id: "AMCModelBasedAudienceMlInputChannelId" = Field(..., alias="mlInputChannelId")
    name: str = Field(..., description="Name of the trained model inference job")
    resource_config: "InferenceJobResourceConfig" = Field(..., alias="resourceConfig")
    trained_model_id: "AMCModelBasedAudienceTrainedModelId" = Field(..., alias="trainedModelId")

    model_config = {'populate_by_name': True}


class AMCModelBasedAudienceTrainedModelInferenceJobResponse(BaseModel):
    """Model based audience trained model inference job execution metadata information."""
    trained_model_inference_job_id: "AMCModelBasedAudienceTrainedModelInferenceJobId" = Field(..., alias="trainedModelInferenceJobId")

    model_config = {'populate_by_name': True}


class ErrorCode(BaseModel):
    """Error code"""
    pass


class ErrorMessage(BaseModel):
    """Human readable response message"""
    pass


class HttpResponse(BaseModel):
    code: Optional["ErrorCode"] = None
    message: Optional["ErrorMessage"] = None

    model_config = {'populate_by_name': True}

