"""Auto-generated Pydantic models. Do not edit manually.

Source: WorkflowManagementService_prod_3p.json
Title:  Workflow Management Service
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class AdvertiserType(StrEnum):
    DISPLAY = "DISPLAY"
    SAS = "SAS"
    SPONSORED_ADS = "SPONSORED_ADS"


class AmcAdvertiserIdentifier(BaseModel):
    """Identifying properties of an advertiser."""
    id_: str = Field(..., alias="id", description="Depending on the value for advertiserType, this contains the CFID of a DSP, entity Id for a Sponsored Ads, or advertiser")
    marketplace_id: Optional[str] = Field(None, alias="marketplaceId", description="For Sponsored Ads and SAS advertisers, this contains the corresponding marketplaceId. This will be null for DSP advertis")
    type_: "AdvertiserType" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class ScheduleAggregationperiod(StrEnum):
    DAILY = "Daily"
    WEEKLY = "Weekly"


class ScheduleAggregationstartday(StrEnum):
    FRIDAY = "Friday"
    MONDAY = "Monday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
    THURSDAY = "Thursday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"


class Schedule(BaseModel):
    aggregation_hour_utc: Optional[int] = Field(None, alias="aggregationHourUtc", description="Specifies the number of hours of offset from UTC, which designates the delineating hour for workflow runs.")
    aggregation_period: Optional[ScheduleAggregationperiod] = Field(None, alias="aggregationPeriod", description="The cadence at which to run a workflow. The following table lists available periods: |Period Name|Description| |--------")
    aggregation_start_day: Optional[ScheduleAggregationstartday] = Field(None, alias="aggregationStartDay", description="Day of week to start aggregations. If not specified, this defaults to the day of week that the schedule is created.")
    disable_aggregation_controls: Optional[bool] = Field(None, alias="disableAggregationControls", description="If true aggregation controls were NOT applied to the workflow.  Query output could still be retrieved when aggregation c")
    require_synthetic_data: Optional[bool] = Field(None, alias="requireSyntheticData", description="If true the execution was allowed to use data sets that only contain synthetic data.")
    schedule_enabled: Optional[bool] = Field(None, alias="scheduleEnabled", description="Boolean flag to signify whether or not the schedule is enabled. Disabled schedules will not run workflows.")
    schedule_id: Optional[str] = Field(None, alias="scheduleId", description="User-supplied identifier of the schedule.")
    workflow_id: Optional[str] = Field(None, alias="workflowId", description="The identifier of the workflow associated with the schedule.")

    model_config = {'populate_by_name': True}


class CreateScheduleRequest(BaseModel):
    pass


class CreateScheduleResponse(BaseModel):
    """Empty response object denoting successful creation of a schedule."""
    pass


class WorkflowInputparametersColumntype(StrEnum):
    DIMENSION = "DIMENSION"
    METRIC = "METRIC"


class WorkflowInputparametersDatatype(StrEnum):
    BINARY = "BINARY"
    BOOLEAN = "BOOLEAN"
    BYTE = "BYTE"
    CALENDAR_INTERVAL = "CALENDAR_INTERVAL"
    DATE = "DATE"
    DECIMAL = "DECIMAL"
    DOUBLE = "DOUBLE"
    FLOAT = "FLOAT"
    INTEGER = "INTEGER"
    LONG = "LONG"
    SHORT = "SHORT"
    STRING = "STRING"
    TIMESTAMP = "TIMESTAMP"


class WorkflowInputparameters(BaseModel):
    column_type: Optional[WorkflowInputparametersColumntype] = Field(None, alias="columnType", description="The type of the column corresponding to the parameter. The following table lists available types: |Type Name|Description")
    data_type: Optional[WorkflowInputparametersDatatype] = Field(None, alias="dataType", description="The data type of the parameter corresponding to the data type of a column. The following table lists available types: |T")
    default_value: Optional[str] = Field(None, alias="defaultValue", description="The value to assign to the parameter if no value is provided.")
    description: Optional[str] = Field(None, description="The human-readable description of what the parameter is used for.")
    display_name: Optional[str] = Field(None, alias="displayName", description="The human-readable name of the parameter.")
    name: Optional[str] = Field(None, description="The name of the parameter used as a variable in SQL.")

    model_config = {'populate_by_name': True}


class WorkflowOutputcolumnsColumntype(StrEnum):
    DIMENSION = "DIMENSION"
    METRIC = "METRIC"


class WorkflowOutputcolumnsDatatype(StrEnum):
    BINARY = "BINARY"
    BOOLEAN = "BOOLEAN"
    BYTE = "BYTE"
    CALENDAR_INTERVAL = "CALENDAR_INTERVAL"
    DATE = "DATE"
    DECIMAL = "DECIMAL"
    DOUBLE = "DOUBLE"
    FLOAT = "FLOAT"
    INTEGER = "INTEGER"
    LONG = "LONG"
    SHORT = "SHORT"
    STRING = "STRING"
    TIMESTAMP = "TIMESTAMP"


class WorkflowOutputcolumns(BaseModel):
    column_type: Optional[WorkflowOutputcolumnsColumntype] = Field(None, alias="columnType", description="The type of the column. The following table lists available types: |Type Name|Description| |-----------|-----------| |ME")
    data_type: Optional[WorkflowOutputcolumnsDatatype] = Field(None, alias="dataType", description="The data type of the column. The following table lists available types: |Type Name|Description| |-----------|-----------")
    data_type_precision: Optional[int] = Field(None, alias="dataTypePrecision", description="Specifies additional information about the dataType for DataType.DECIMAL. Corresponds to the total number of digits.")
    data_type_scale: Optional[int] = Field(None, alias="dataTypeScale", description="Specifies additional information about the dataType DataType.DECIMAL. Corresponds to the number of digits to the right o")
    description: Optional[str] = Field(None, description="The human-readable description of what the parameter is used for.")
    name: Optional[str] = Field(None, description="The name of the column.")

    model_config = {'populate_by_name': True}


class WorkflowOutputformat(BaseModel):
    """Specifies the CSV output format for a workflow."""
    escape_character: Optional[str] = Field(None, alias="escapeCharacter", description="The character to use for escaping characters inside a quoted field.")
    quote_character: Optional[str] = Field(None, alias="quoteCharacter", description="The character to use for quoting fields that need it.")
    separator_character: Optional[str] = Field(None, alias="separatorCharacter", description="The character to use for separating fields.")

    model_config = {'populate_by_name': True}


class WorkflowPrivacyfilteringbehavior(StrEnum):
    REMOVE_ROWS = "REMOVE_ROWS"
    REMOVE_VALUES = "REMOVE_VALUES"


class Workflow(BaseModel):
    """Workflows are defined as a set of operations that take previously defined data sources as input and use them to generate reports.         Further information can be found in the AMC documentation host"""
    filtered_metrics_discriminator_column: Optional[str] = Field(None, alias="filteredMetricsDiscriminatorColumn", description="If this field is not provided, rows which do not meet the minimum distinct user count requirements will be completely fi")
    input_parameters: Optional[list["WorkflowInputparameters"]] = Field(None, alias="inputParameters", description="Optional. Defines the parameters that can be referenced by workflow definition. If workflow references a parameter not d")
    input_schema: Optional[str] = Field(None, alias="inputSchema", description="Optional. 'null' schema if not provided. Provides the schema to use when resolving unqualified data sources to avoid col")
    output_columns: Optional[list["WorkflowOutputcolumns"]] = Field(None, alias="outputColumns", description="Optional. The columns that the workflow must produce as output. If provided, the workflow will be validated during compi")
    output_format: Optional["WorkflowOutputformat"] = Field(None, alias="outputFormat", description="Specifies the CSV output format for a workflow.")
    privacy_filtering_behavior: Optional[WorkflowPrivacyfilteringbehavior] = Field(None, alias="privacyFilteringBehavior", description="Specifies how workflow output will be processed after sensitive values have been removed. The following table lists avai")
    query: Optional[list[str]] = Field(None, description="Defines a list of [operations] that produce a set of output data based on input data from one or more [DataSource]s. The")
    sql_query: Optional[str] = Field(None, alias="sqlQuery", description="The SQL query to run to produce output for the workflow. If a [sqlQuery] and a [query] are both provided, the [sqlQuery]")
    workflow_id: Optional[str] = Field(None, alias="workflowId", description="User-supplied identifier of the workflow.")

    model_config = {'populate_by_name': True}


class CreateWorkflowExecutionRequestTimewindowtype(StrEnum):
    ALL = "ALL"
    CURRENT_MONTH = "CURRENT_MONTH"
    EXPLICIT = "EXPLICIT"
    MOST_RECENT_DAY = "MOST_RECENT_DAY"
    MOST_RECENT_WEEK = "MOST_RECENT_WEEK"
    PREVIOUS_MONTH = "PREVIOUS_MONTH"


class CreateWorkflowExecutionRequest(BaseModel):
    additional_acr_results_receivers: Optional[list[str]] = Field(None, alias="additionalAcrResultsReceivers", description="AWS account IDs of additional customer-owned members which should receive the results of this execution through AWS Clea")
    advertisers: Optional[list["AmcAdvertiserIdentifier"]] = Field(None, description="Optional - if specified, the execution will only read data for the provided advertisers. If not specified, the execution")
    disable_aggregation_controls: Optional[bool] = Field(None, alias="disableAggregationControls", description="Optional - if true privacy controls will NOT be applied to the workflow.  Query output can still be retrieved when priva")
    dry_run: Optional[bool] = Field(None, alias="dryRun", description="Optional - if true, the execution will be processed but not submitted to compute, at which point the execution will be m")
    max_certified_time: Optional[str] = Field(None, alias="maxCertifiedTime", description="The maximum certified time that will be used for input data sets. This parameter can be used to execute a workflow again")
    max_dimension_time: Optional[str] = Field(None, alias="maxDimensionTime", description="The maximum time window end that that will be used for dimension data sets. This parameter can be used to execute a work")
    parameter_values: Optional[dict[str, str]] = Field(None, alias="parameterValues", description="Values to use for the parameters specified in the workflow.")
    require_synthetic_data: Optional[bool] = Field(None, alias="requireSyntheticData", description="Optional - if true the execution will only be allowed to use data sets that only contain synthetic data.")
    skip_publish: Optional[bool] = Field(None, alias="skipPublish", description="Optional - if true the workflow will be run without writing out results.")
    time_window_end: Optional[str] = Field(None, alias="timeWindowEnd", description="Optional. Only used with a timeWindowType of EXPLICIT. The end of the time window for input data for the workflow execut")
    time_window_start: Optional[str] = Field(None, alias="timeWindowStart", description="Optional. Only used with a timeWindowType of `EXPLICIT`. The start of the time window for input data for the workflow ex")
    time_window_time_zone: Optional[str] = Field(None, alias="timeWindowTimeZone", description="Optional. The time zone of the specified time window. This applies to both time window start and end if specified for ti")
    time_window_type: Optional[CreateWorkflowExecutionRequestTimewindowtype] = Field(None, alias="timeWindowType", description="Optional. The type of time window to use to for specifying input data for the workflow execution. If not provided, the t")
    workflow: Optional["Workflow"] = None
    workflow_execution_timeout_seconds: Optional[int] = Field(None, alias="workflowExecutionTimeoutSeconds", description="Optional. If specified, limits the workflow query execution time to the specified number of seconds. The value is requir")
    workflow_id: Optional[str] = Field(None, alias="workflowId", description="The ID of the workflow to execute, if executing an existing workflow. Required if a sqlQuery is not provided. Cannot be ")

    model_config = {'populate_by_name': True}


class OutputChannelType(StrEnum):
    ACR = "ACR"
    DOWNLOAD = "DOWNLOAD"
    PUBLISH = "PUBLISH"


class OutputChannel(BaseModel):
    """Contains information about a channel for retrieving workflow execution output in an instance."""
    acr_member_id: Optional[str] = Field(None, alias="acrMemberId", description="The account ID of the AWS Clean Rooms member to which results were delivered. Is only populated for the ACR channel type")
    acr_membership_id: Optional[str] = Field(None, alias="acrMembershipId", description="The membership ID of the AWS Clean Rooms member to which results were delivered. Is only populated for the ACR channel t")
    type_: "OutputChannelType" = Field(..., alias="type", description="The mechanism for retrieving output.")

    model_config = {'populate_by_name': True}


class WorkflowExecutionOutputChannelStatus(StrEnum):
    AVAILABLE = "AVAILABLE"
    FAILED = "FAILED"
    PENDING = "PENDING"
    UNAVAILABLE = "UNAVAILABLE"


class WorkflowExecutionOutputChannel(BaseModel):
    """Contains information about a channel for retrieving workflow execution output in an instance and information about whether or not the output of a specific workflow execution can be retrieved through t"""
    acr_detail_page_url: Optional[str] = Field(None, alias="acrDetailPageUrl", description="The URL of the AWS Clean Rooms protected query detail page URL which can be used to view information about this protecte")
    channel: "OutputChannel" = Field(..., description="The channel for receiving output.")
    status: "WorkflowExecutionOutputChannelStatus" = Field(..., description="A status indicating whether output can be retrieved through the channel now or in the future.")
    status_reason: Optional[str] = Field(None, alias="statusReason", description="If output cannot be retrieved through this channel, contains a description of why not. Otherwise, is null.")

    model_config = {'populate_by_name': True}


class WorkflowExecutionStatus(StrEnum):
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"


class WorkflowExecution(BaseModel):
    acr_collaboration_id: Optional[str] = Field(None, alias="acrCollaborationId", description="The ID of the ACR collaboration that the execution is being executed in. Will only be populated for executions where at ")
    acr_customer_membership_id: Optional[str] = Field(None, alias="acrCustomerMembershipId", description="The ID of the ACR membership for the primary customer-owned member. Will only be populated for executions where the prim")
    acr_detail_page_url: Optional[str] = Field(None, alias="acrDetailPageUrl", description="The URL for the detail page of the ACR protected query performing the compute for this execution. Will only be populated")
    acr_protected_query_id: Optional[str] = Field(None, alias="acrProtectedQueryId", description="The ID for the ACR protected query performing the compute for this execution. Will only be populated for executions wher")
    advertisers: Optional[list["AmcAdvertiserIdentifier"]] = Field(None, description="If the execution was configured to read data for only a specified list of advertisers queryable for the instance, contai")
    create_time: Optional[str] = Field(None, alias="createTime", description="The time the workflow execution was created. This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss'Z'.")
    disable_aggregation_controls: Optional[bool] = Field(None, alias="disableAggregationControls", description="If true aggregation controls were NOT applied to the workflow.  Query output could still be retrieved when aggregation c")
    expire_time: Optional[str] = Field(None, alias="expireTime", description="The time at which the workflow execution will alarm due to SLA breach (if it has not already started running). This fiel")
    invalidation_offset_secs: Optional[int] = Field(None, alias="invalidationOffsetSecs", description="How much wider of a time range should be used for fact invalidation data than for fact data, in seconds. For example, an")
    last_updated_time: Optional[str] = Field(None, alias="lastUpdatedTime", description="The last time the workflow execution was updated. This field is in UTC and is formatted as yyyy-MM-dd'T'HH:mm:ss'Z'.")
    output_channels: Optional[list["WorkflowExecutionOutputChannel"]] = Field(None, alias="outputChannels", description="The possible channels for retrieving workflow execution output in this instance with information about whether or not it")
    output_s3_uri: Optional[str] = Field(None, alias="outputS3URI", description="The fully qualified S3 path at which the output files for the workflow execution will be created inside the AMC instance")
    require_synthetic_data: Optional[bool] = Field(None, alias="requireSyntheticData", description="If true the execution was allowed to use data sets that only contain synthetic data.")
    sql_query: Optional[str] = Field(None, alias="sqlQuery", description="The SQL query that was executed. Will only be populated if includeWorkflow was true for the request to retrieve the exec")
    status: Optional[WorkflowExecutionStatus] = Field(None, description="The current status of the workflow execution. The following table lists available statuses: |Status Name|Description| |-")
    time_window_end: Optional[str] = Field(None, alias="timeWindowEnd", description="The end of the time window for data being used as input for the workflow execution. This is a nominal time window and no")
    time_window_end_original: Optional[str] = Field(None, alias="timeWindowEndOriginal", description="The originally provided end of the time window. This field is in the original timezone and is formatted as yyyy-MM-dd'T'")
    time_window_start: Optional[str] = Field(None, alias="timeWindowStart", description="The start of the time window for data being used as input for the workflow execution. This is a nominal time window and ")
    time_window_start_original: Optional[str] = Field(None, alias="timeWindowStartOriginal", description="The originally provided start of the time window. This field is in the original timezone and is formatted as yyyy-MM-dd'")
    time_window_time_zone_original: Optional[str] = Field(None, alias="timeWindowTimeZoneOriginal", description="The timezone provided when creating the workflow execution. This field allows using the timeWindowStartOriginal and time")
    wait_until: Optional[str] = Field(None, alias="waitUntil", description="The time at which the workflow execution will not start running before. This field is in UTC and is formatted as yyyy-MM")
    workflow_execution_id: Optional[str] = Field(None, alias="workflowExecutionId", description="The unique identifier of the workflow execution.")
    workflow_execution_timeout_seconds: Optional[int] = Field(None, alias="workflowExecutionTimeoutSeconds", description="The amount of time that the workflow is allowed to execute in the compute engine. If a workflow exceeds this value, the ")
    workflow_id: Optional[str] = Field(None, alias="workflowId", description="The ID of the workflow being executed. This ID is automatically generated when a new execution is created and can be use")

    model_config = {'populate_by_name': True}


class CreateWorkflowExecutionResponse(BaseModel):
    workflow_execution: Optional["WorkflowExecution"] = Field(None, alias="workflowExecution")

    model_config = {'populate_by_name': True}


class CreateWorkflowResponse(BaseModel):
    """Empty response object denoting successful creation of a workflow."""
    pass


class DataSourceOutputChannel(BaseModel):
    """Contains information about a channel for retrieving workflow execution output in an instance and information about whether or not the output of executions that read from this data source can be retrie"""
    channel: "OutputChannel" = Field(..., description="The channel for receiving output.")
    output_available: bool = Field(..., alias="outputAvailable", description="True if output would be available through this channel for a workflow execution that read from this data source, barring")
    output_unavailable_reason: Optional[str] = Field(None, alias="outputUnavailableReason", description="If output cannot be retrieved through this channel (i.e. `outputAvailable` is false), contains a description of why not.")

    model_config = {'populate_by_name': True}


class DataSourceColumnsColumntype(StrEnum):
    DIMENSION = "DIMENSION"
    METRIC = "METRIC"


class DataSourceColumns(BaseModel):
    """Defines a column in a data source."""
    column_type: Optional[DataSourceColumnsColumntype] = Field(None, alias="columnType", description="The type of a data source column. The following table lists available types: |Type Name|Description| |-----------|------")
    description: Optional[str] = Field(None, description="The human-readable description of what the column contains.")
    name: Optional[str] = Field(None, description="The name of the column.")

    model_config = {'populate_by_name': True}


class DataSourceOwner(StrEnum):
    AMAZON = "AMAZON"
    CUSTOMER = "CUSTOMER"


class DataSourceProvider(StrEnum):
    ADVERTISER_DATA_UPLOAD = "ADVERTISER_DATA_UPLOAD"
    AMAZON = "AMAZON"


class DataSourceTagsType(StrEnum):
    DEPRECATED = "DEPRECATED"
    NEW = "NEW"
    RENAMED = "RENAMED"


class DataSourceTags(BaseModel):
    """Defines a tag associated with a data source."""
    description: Optional[str] = Field(None, description="The human-readable description of the data source tag.")
    subtext: Optional[str] = Field(None, description="Field denoting the ad product relevant to the data source (e.g., 'Amazon DSP').")
    title: Optional[str] = Field(None, description="The title of the data source tag.")
    type_: Optional[DataSourceTagsType] = Field(None, alias="type", description="The type of a data source tag.")

    model_config = {'populate_by_name': True}


class DataSource(BaseModel):
    """Defines a type of data that may be used as a source for queries in workflows or data views. A data source has a flat schema defined by one or more columns. A data source may only be referenced directl"""
    columns: Optional[list["DataSourceColumns"]] = Field(None, description="List of data source columns.")
    data_source_id: Optional[str] = Field(None, alias="dataSourceId", description="The identifier of the data source.")
    description: Optional[str] = Field(None, description="The human-readable description of what the data source contains.")
    output_channels: Optional[list["DataSourceOutputChannel"]] = Field(None, alias="outputChannels", description="The possible channels for retrieving workflow execution output in this instance with information about whether or not it")
    owner: Optional[DataSourceOwner] = Field(None, description="The owner of a data source. The following table lists available owners: |Type Name|Description| |-----------|-----------")
    provider: Optional[DataSourceProvider] = Field(None, description="The provider of the data source.")
    tags: Optional[list["DataSourceTags"]] = Field(None, description="List of human-readable tags associated with a data source.")

    model_config = {'populate_by_name': True}


class DeleteScheduleResponse(BaseModel):
    """Empty response object denoting successful deletion of a schedule."""
    pass


class DeleteWorkflowResponse(BaseModel):
    """Empty response object denoting successful deletion of a workflow."""
    pass


class Error(BaseModel):
    """The error response object."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class GetDataSourceResponse(BaseModel):
    data_source: Optional["DataSource"] = Field(None, alias="dataSource")

    model_config = {'populate_by_name': True}


class GetScheduleResponse(BaseModel):
    schedule: Optional["Schedule"] = None

    model_config = {'populate_by_name': True}


class GetWorkflowExecutionDownloadUrlsResponse(BaseModel):
    download_urls: Optional[list[str]] = Field(None, alias="downloadUrls", description="A list of pre-signed S3 URLs for the workflow execution's results. Multiple URLs will be given for results that produce ")
    metadata_download_urls: Optional[list[str]] = Field(None, alias="metadataDownloadUrls", description="A list of pre-signed S3 URLs for the workflow execution's metadata used during execution.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="[Placeholder - To be used as a Future Scope] Token to use in subsequent request to retrieve next page of results. Null i")

    model_config = {'populate_by_name': True}


class GetWorkflowExecutionResponse(BaseModel):
    workflow_execution: Optional["WorkflowExecution"] = Field(None, alias="workflowExecution")

    model_config = {'populate_by_name': True}


class GetWorkflowResponse(BaseModel):
    workflow: Optional["Workflow"] = None

    model_config = {'populate_by_name': True}


class ListDataSourcesResponse(BaseModel):
    data_sources: Optional[list["DataSource"]] = Field(None, alias="dataSources", description="List of data sources.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional. Token to use in subsequent request to retrieve next page of results. Null if all results have been returned.")

    model_config = {'populate_by_name': True}


class ListSchedulesResponse(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional. Token to use in subsequent request to retrieve next page of results. Null if all results have been returned.")
    schedules: Optional[list["Schedule"]] = Field(None, description="List of schedules.")

    model_config = {'populate_by_name': True}


class ListWorkflowExecutionsResponse(BaseModel):
    executions: Optional[list["WorkflowExecution"]] = Field(None, description="List of workflow executions.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional. Token to use in subsequent request to retrieve next page of results. Null if all results have been returned.")

    model_config = {'populate_by_name': True}


class ListWorkflowsResponse(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional. Token to use in subsequent request to retrieve next page of results. Null if all results have been returned.")
    workflows: Optional[list["Workflow"]] = Field(None, description="List of workflows.")

    model_config = {'populate_by_name': True}


class UpdateScheduleResponse(BaseModel):
    """Empty response object denoting successful update of a schedule."""
    pass


class UpdateWorkflowExecutionResponse(BaseModel):
    """Empty response object denoting a successful update of a workflow execution."""
    pass


class UpdateWorkflowResponse(BaseModel):
    """Empty response object denoting a successful update of a workflow."""
    pass

