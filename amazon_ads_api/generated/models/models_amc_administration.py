"""Auto-generated Pydantic models. Do not edit manually.

Source: AMCAdministration_prod_3p.json
Title:  AMC Administration
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class CollaborationMemberStatus(StrEnum):
    ACTIVE = "ACTIVE"
    INVITED = "INVITED"
    LEFT = "LEFT"
    REMOVED = "REMOVED"


class AcrMemberAbility(StrEnum):
    CAN_RECEIVE_RESULTS = "CAN_RECEIVE_RESULTS"


class AcrCustomerPartner(BaseModel):
    """Metadata about a customer partner in a collaboration"""
    abilities: Optional[list["AcrMemberAbility"]] = Field(None, description="The abilities the member has in the collaboration. Set the value to [] (empty array) to allow a member to only contribut")
    acr_customer_partner_id: Optional[str] = Field(None, alias="acrCustomerPartnerId", description="The ID of the customer partner (same value as awsAccountId). This is a read-only field only present in response objects.")
    aws_account_id: Optional[str] = Field(None, alias="awsAccountId", description="The member's AWS account ID.")
    display_name: Optional[str] = Field(None, alias="displayName", description="The member's display name.")
    status: Optional["CollaborationMemberStatus"] = Field(None, description="The current status of this customer partner in the collaboration. This is a read-only field only present in response obj")

    model_config = {'populate_by_name': True}


class AddCollaborationCustomerPartnersPayload(BaseModel):
    """The payload of the request."""
    acr_customer_partners: list["AcrCustomerPartner"] = Field(..., alias="acrCustomerPartners", description="The list of customer partners that will be added to the collaboration in an instance backed by AWS Clean Rooms (ACR).")

    model_config = {'populate_by_name': True}


class AddCollaborationCustomerPartnersResponse(BaseModel):
    acr_customer_partners: Optional[list["AcrCustomerPartner"]] = Field(None, alias="acrCustomerPartners", description="The list of customer partners added to the collaboration.")

    model_config = {'populate_by_name': True}


class AdvertiserType(StrEnum):
    DISPLAY = "DISPLAY"
    SAS = "SAS"
    SPONSORED_ADS = "SPONSORED_ADS"


class AdvertiserConfiguredadvertisertypes(StrEnum):
    DISPLAY = "DISPLAY"
    SAS = "SAS"
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"


class Advertiser(BaseModel):
    """Details about an advertiser"""
    configured_advertiser_types: Optional[list[AdvertiserConfiguredadvertisertypes]] = Field(None, alias="configuredAdvertiserTypes", description="The type of ad configured for this advertiser")
    id_: str = Field(..., alias="id", description="Depending on the value for advertiserType, this contains the CFID of a DSP, entity Id for a Sponsored Ads, or advertiser")
    marketplace_id: Optional[str] = Field(None, alias="marketplaceId", description="For Sponsored Ads and SAS advertisers, this contains the corresponding marketplaceId, for DSP advertisers this will be n")
    name: str = Field(..., description="Depending on the value for advertiserType, this contains either the DSP, Sponsored Ads, or SAS advertiser name.")
    type_: "AdvertiserType" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class AmcAdvertiserIdentifier(BaseModel):
    """Identifying properties of an advertiser."""
    id_: str = Field(..., alias="id", description="Depending on the value for advertiserType, this contains the CFID of a DSP, entity Id for a Sponsored Ads, or advertiser")
    marketplace_id: Optional[str] = Field(None, alias="marketplaceId", description="For Sponsored Ads and SAS advertisers, this contains the corresponding marketplaceId. This will be null for DSP advertis")
    type_: "AdvertiserType" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class AmcAdvertiserUpdateStatus(StrEnum):
    COMPLETED = "COMPLETED"
    PENDING = "PENDING"
    REJECTED = "REJECTED"
    UPDATING = "UPDATING"


class AmcAdvertiserUpdate(BaseModel):
    advertisers_to_add: Optional[list["AmcAdvertiserIdentifier"]] = Field(None, alias="advertisersToAdd", description="List of advertiser identifiers to be added to the instance.")
    advertisers_to_remove: Optional[list["AmcAdvertiserIdentifier"]] = Field(None, alias="advertisersToRemove", description="List of advertiser identifiers to be deleted from the instance")
    pending_verification_reason: Optional[str] = Field(None, alias="pendingVerificationReason", description="Explanation for why a request has UPDATING or REJECTED status, when applicable.")
    status: Optional["AmcAdvertiserUpdateStatus"] = None
    update_id: Optional[int] = Field(None, alias="updateId", description="Identifier of the advertiser update request. It's numeric and increasing from each request")

    model_config = {'populate_by_name': True}


class AmcAdvertiserUpdateLite(BaseModel):
    status: Optional["AmcAdvertiserUpdateStatus"] = None
    update_id: Optional[int] = Field(None, alias="updateId", description="Identifier of the advertiser update request. It's numeric and increasing from each request")

    model_config = {'populate_by_name': True}


class AmcCreateAdvertiserUpdateRequest(BaseModel):
    advertisers_to_add: Optional[list["AmcAdvertiserIdentifier"]] = Field(None, alias="advertisersToAdd", description="List of advertiser identifiers. This is the list of advertisers which should be added for the given instance.")
    advertisers_to_remove: Optional[list["AmcAdvertiserIdentifier"]] = Field(None, alias="advertisersToRemove", description="List of advertiser identifiers. This is the list of advertisers which should be deleted for the given instance.")

    model_config = {'populate_by_name': True}


class AmcCreateAdvertiserUpdateResponse(BaseModel):
    advertiser_update: "AmcAdvertiserUpdate" = Field(..., alias="advertiserUpdate")

    model_config = {'populate_by_name': True}


class AmcCreateInstanceRequest(BaseModel):
    acr_backed: Optional[bool] = Field(None, alias="acrBacked", description="Boolean flag to indicate whether the instance will be a collaboration instance (leveraging AWS Clean Rooms). Set to 'Tru")
    acr_customer_partners: Optional[list["AcrCustomerPartner"]] = Field(None, alias="acrCustomerPartners", description="The list of customer partners that will be added to the collaboration in an instance backed by AWS Clean Rooms (ACR).")
    advertiser_name: Optional[str] = Field(None, alias="advertiserName", description="The advertiser name associated with the AMC instance. Only numbers, english letters and spaces are allowed and size betw")
    aws_account_id: Optional[str] = Field(None, alias="awsAccountId", description="Customer-owned AWS account ID associated with the AMC instance from which the customer will upload data. It is optional ")
    idempotency_token: Optional[str] = Field(None, alias="idempotencyToken", description="Optional token used to signal that the create operation should be idempotent. If supplied, subsequent requests with the ")
    instance_name: str = Field(..., alias="instanceName", description="Human-readable AMC instance identifier. Only numbers, english letters and spaces are allowed and size between 3 and 50 c")
    s3_bucket_name: Optional[str] = Field(None, alias="s3BucketName", description="The name of the S3 bucket associated with the AMC instance. This bucket will contain reporting workflow output.")

    model_config = {'populate_by_name': True}


class InstanceAdvertisertypes(StrEnum):
    DISPLAY = "DISPLAY"
    SAS = "SAS"
    SPONSORED_ADS = "SPONSORED_ADS"


class InstanceCreationstatus(StrEnum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    REQUESTED = "REQUESTED"
    SUBMITTED = "SUBMITTED"
    SUCCEEDED = "SUCCEEDED"


class Instance(BaseModel):
    """Details about an AMC instance."""
    advertiser_types: Optional[list[InstanceAdvertisertypes]] = Field(None, alias="advertiserTypes", description="The set of advertiser types currently associated to this instance.")
    api_endpoint: str = Field(..., alias="apiEndpoint", description="The API URL for access the AMC reporting and Data Upload API. Each AMC instance has a unique API URL.")
    aws_account_id: str = Field(..., alias="awsAccountId", description="The 12-digit AWS account ID which owns the S3 bucket associated with the instance.")
    creation_datetime: str = Field(..., alias="creationDatetime", description="The date time string corresponding to the creation of the AMC instance in UTC. Format is yyyy-MM-dd'T'HH:mm:ss'Z'.")
    creation_status: InstanceCreationstatus = Field(..., alias="creationStatus", description="The creation status of an AMC instance. The following table lists available statuses:  |Status Name|Description| |------")
    customer_canonical_name: Optional[str] = Field(None, alias="customerCanonicalName", description="Name of advertiser associated with the AMC instance.")
    data_upload_aws_account_id: str = Field(..., alias="dataUploadAwsAccountId", description="This AWS account ID is generated by Amazon for each AMC instance. It allows AMC users to grant an AMC instance permissio")
    entities: list[str] = Field(..., description="The Amazon Advertising entities associated with this AMC instance.")
    instance_id: str = Field(..., alias="instanceId", description="AMC instance identifier.")
    instance_name: str = Field(..., alias="instanceName", description="Human-readable AMC instance identifier.")
    s3_bucket_name: str = Field(..., alias="s3BucketName", description="The name of the S3 bucket associated with the AMC instance. This bucket will contain reporting workflow output.")
    s3_bucket_region: str = Field(..., alias="s3BucketRegion", description="The AWS region of the S3 bucket associated with the AMC instance.")

    model_config = {'populate_by_name': True}


class AmcCreateInstanceResponse(BaseModel):
    instance: Optional["Instance"] = None

    model_config = {'populate_by_name': True}


class AmcDeleteInstanceResponse(BaseModel):
    """Empty response object denoting successful deletion of an instance."""
    pass


class AmcGetAdvertiserUpdateResponse(BaseModel):
    advertiser_update: "AmcAdvertiserUpdate" = Field(..., alias="advertiserUpdate")

    model_config = {'populate_by_name': True}


class AmcListAdvertiserUpdatesResponse(BaseModel):
    advertiser_updates: Optional[list["AmcAdvertiserUpdateLite"]] = Field(None, alias="advertiserUpdates", description="List of advertiser updates.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional. Token to use in subsequent request to retrieve next page of results. Null if all results have been returned.")

    model_config = {'populate_by_name': True}


class AmcUpdateInstanceRequest(BaseModel):
    advertiser_name: Optional[str] = Field(None, alias="advertiserName", description="The advertiser name associated with the AMC instance.")
    aws_account_id: Optional[str] = Field(None, alias="awsAccountId", description="The 12-digit AWS account ID which owns the S3 bucket associated with the instance.")
    instance_name: Optional[str] = Field(None, alias="instanceName", description="Human-readable AMC instance identifier.")
    s3_bucket_name: Optional[str] = Field(None, alias="s3BucketName", description="The name of the S3 bucket associated with the AMC instance. This bucket will contain reporting workflow output.")

    model_config = {'populate_by_name': True}


class AmcUpdateInstanceResponse(BaseModel):
    instance: Optional["Instance"] = None

    model_config = {'populate_by_name': True}


class AmcpLinkAmcAccount(BaseModel):
    """AMC Account details."""
    account_id: Optional[str] = Field(None, alias="accountId", description="AMC Account identifier.")
    account_name: Optional[str] = Field(None, alias="accountName", description="AMC Account name.")
    marketplace_id: Optional[str] = Field(None, alias="marketplaceId", description="Obfuscated Marketplace Id.")

    model_config = {'populate_by_name': True}


class AmcpLinkBadRequestExceptionResponseContent(BaseModel):
    """Bad Request."""
    message: Optional[str] = Field(None, description="Error message.")
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class AmcpLinkForbiddenRequestExceptionResponseContent(BaseModel):
    """Forbidden. The request failed because the user does not have access to the specified resource."""
    message: Optional[str] = Field(None, description="Error message.")
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class AmcpLinkListAmcAccountsResponseContent(BaseModel):
    """List of AMC Accounts."""
    amc_accounts: Optional[list["AmcpLinkAmcAccount"]] = Field(None, alias="amcAccounts", description="List of AMC Accounts.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional. Token to use in subsequent request to retrieve next page of results. Null if all results have been returned.")

    model_config = {'populate_by_name': True}


class AmcpLinkServerExceptionResponseContent(BaseModel):
    """Internal server error. Retry later. Contact support if this response persists."""
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class AmcpLinkTooManyRequestsExceptionResponseContent(BaseModel):
    """Too Many Requests. The request was rate-limited. Retry later."""
    message: Optional[str] = Field(None, description="Error message.")
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class AmcpLinkUnauthorizedRequestExceptionResponseContent(BaseModel):
    """Unauthorized. The request failed because the user is not authenticated or is not allowed to invoke the operation."""
    message: Optional[str] = Field(None, description="Error message.")
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class CollaborationIdMappingJobMetrics(BaseModel):
    """Job data record processing metrics."""
    input_records: Optional[int] = Field(None, alias="inputRecords", description="Number of input records.")
    records_not_processed: Optional[int] = Field(None, alias="recordsNotProcessed", description="Number of records not processed.")
    total_mapped_records: Optional[int] = Field(None, alias="totalMappedRecords", description="Total number of mapped records.")
    total_mapped_source_records: Optional[int] = Field(None, alias="totalMappedSourceRecords", description="Total number of mapped records from the SOURCE.")
    total_mapped_target_records: Optional[int] = Field(None, alias="totalMappedTargetRecords", description="Total number of mapped records from the TARGET.")
    total_records_processed: Optional[int] = Field(None, alias="totalRecordsProcessed", description="Total number of records processed.")
    unique_records_loaded: Optional[int] = Field(None, alias="uniqueRecordsLoaded", description="Total number of unique mapped records.")

    model_config = {'populate_by_name': True}


class CollaborationIdMappingJobStatus(StrEnum):
    FAILED = "FAILED"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    UNKNOWN = "UNKNOWN"


class CollaborationIdMappingJob(BaseModel):
    """Metadata about the ID mapping job associated to an ID mapping table in the collaboration."""
    end_time: Optional[str] = Field(None, alias="endTime", description="The time the job execution ended.")
    error_details: Optional[str] = Field(None, alias="errorDetails", description="If the job failed, contains information about the error.")
    job_id: Optional[str] = Field(None, alias="jobId", description="Job unique identifier.")
    metrics: Optional["CollaborationIdMappingJobMetrics"] = None
    start_time: Optional[str] = Field(None, alias="startTime", description="The time the job execution started.")
    status: Optional["CollaborationIdMappingJobStatus"] = None

    model_config = {'populate_by_name': True}


class CollaborationIdMappingJobSummary(BaseModel):
    """Summarized metadata of the ID mapping job associated to an ID mapping table in the collaboration."""
    end_time: Optional[str] = Field(None, alias="endTime", description="The time the job execution ended.")
    job_id: Optional[str] = Field(None, alias="jobId", description="Job unique identifier.")
    start_time: Optional[str] = Field(None, alias="startTime", description="The time the job execution started.")
    status: Optional["CollaborationIdMappingJobStatus"] = None

    model_config = {'populate_by_name': True}


class CollaborationIdMappingTable(BaseModel):
    """Metadata about a collaboration ID mapping table"""
    arn: Optional[str] = Field(None, description="The ARN of the table.")
    create_time: Optional[str] = Field(None, alias="createTime", description="Creation time of the table.")
    description: Optional[str] = Field(None, description="The description of the table.")
    id_: Optional[str] = Field(None, alias="id", description="Unique identifier of the table.")
    name: Optional[str] = Field(None, description="The name of the table.")
    queryable: Optional[bool] = Field(None, description="Indicates if the table is queryable.")
    source_aws_account: Optional[str] = Field(None, alias="sourceAwsAccount", description="The AWS account ID of the input SOURCE of the ID mapping table. The SOURCE is always the member who requested the creati")
    update_time: Optional[str] = Field(None, alias="updateTime", description="Last time the table was updated.")
    workflow_arn: Optional[str] = Field(None, alias="workflowArn", description="The ARN of the id mapping workflow processing the data backing the table.")

    model_config = {'populate_by_name': True}


class CollaborationIdNamespaceAssociationIdnamespacetype(StrEnum):
    SOURCE = "SOURCE"
    TARGET = "TARGET"
    UNKNOWN = "UNKNOWN"


class CollaborationIdNamespaceAssociation(BaseModel):
    """Metadata of the Id Namespace associated to the ACR collaboration"""
    create_time: Optional[str] = Field(None, alias="createTime", description="The time when the association was created.")
    creator_account_id: Optional[str] = Field(None, alias="creatorAccountId", description="The AWS account of the member that associated the ID namespace to the collaboration.")
    id_: Optional[str] = Field(None, alias="id", description="Uniquely identifies the association between ID namespace and collaboration.")
    id_namespace_arn: Optional[str] = Field(None, alias="idNamespaceArn", description="ID namespace unique resource identifier.")
    id_namespace_type: Optional[CollaborationIdNamespaceAssociationIdnamespacetype] = Field(None, alias="idNamespaceType", description="The type of ID namespace.")
    update_time: Optional[str] = Field(None, alias="updateTime", description="The last time the association was updated.")

    model_config = {'populate_by_name': True}


class CollaborationMember(BaseModel):
    """Metadata about a collaboration member"""
    account_id: Optional[str] = Field(None, alias="accountId", description="The member's AWS account ID.")
    display_name: Optional[str] = Field(None, alias="displayName", description="The member's display name.")
    membership_id: Optional[str] = Field(None, alias="membershipId", description="Unique identifier of the member's membership in the collaboration.")
    status: Optional["CollaborationMemberStatus"] = Field(None, description="The current status of the member in the collaboration.")

    model_config = {'populate_by_name': True}


class CollaborationStatus(StrEnum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    IN_PROGRESS = "IN_PROGRESS"
    NOT_STARTED = "NOT_STARTED"
    PENDING_ACCEPTANCE = "PENDING_ACCEPTANCE"
    REJECTED = "REJECTED"


class CollaborationSummary(BaseModel):
    """ACR collaboration metadata"""
    amc_data_providers: Optional[list["CollaborationMember"]] = Field(None, alias="amcDataProviders", description="The list of AMC managed members who contribute data in the collaboration.")
    creator: Optional["CollaborationMember"] = None
    customer: Optional["CollaborationMember"] = None
    customer_acceptance_link: Optional[str] = Field(None, alias="customerAcceptanceLink", description="Deep link to the collaboration acceptance page in the customer's AWS account.")
    customer_partners: Optional[list["CollaborationMember"]] = Field(None, alias="customerPartners", description="The list of customer partners who contribute data in the collaboration.")
    description: Optional[str] = Field(None, description="The collaboration's description.")
    id_: Optional[str] = Field(None, alias="id", description="The collaboration's unique identifier.")
    name: Optional[str] = Field(None, description="The collaboration's display name.")
    query_submitter: Optional["CollaborationMember"] = Field(None, alias="querySubmitter")
    results_receivers: Optional[list["CollaborationMember"]] = Field(None, alias="resultsReceivers", description="The list of members that are results receivers in the collaboration.")
    status: Optional["CollaborationStatus"] = Field(None, description="The current status of the collaboration.")

    model_config = {'populate_by_name': True}


class CreateCollaborationIdMappingTablePayload(BaseModel):
    """Input data to create an ID mapping table"""
    id_mapping_table_name: str = Field(..., alias="idMappingTableName", description="ID mapping table name.")
    source_id_namespace_arn: str = Field(..., alias="sourceIdNamespaceArn", description="Source ID namespace ARN.")

    model_config = {'populate_by_name': True}


class CreateCollaborationIdMappingTableResponse(BaseModel):
    collaboration_id: Optional[str] = Field(None, alias="collaborationId", description="Unique identifier of the collaboration the ID mapping table is part of.")
    id_mapping_table: Optional["CollaborationIdMappingTable"] = Field(None, alias="idMappingTable")
    id_mapping_workflow_job_id: Optional[str] = Field(None, alias="idMappingWorkflowJobId", description="Unique identifier of the job started to populate the id mapping table. If AMC was not able to start the job, this field ")
    tracking_id: Optional[str] = Field(None, alias="trackingId", description="Unique identifier of a job tracking token in AMC. When this attribute is not null, it indicates an idMappingWorkflowJobI")

    model_config = {'populate_by_name': True}


class CreateCollaborationRequest(BaseModel):
    aws_account_id: Optional[str] = Field(None, alias="awsAccountId", description="Optional. The AWS account ID which owns the AMC instance. If left empty, the current AWS account ID (red room account) a")

    model_config = {'populate_by_name': True}


class CreateCollaborationResponse(BaseModel):
    id_: Optional[str] = Field(None, alias="id", description="Unique identifier of the collaboration.")
    status: Optional["CollaborationStatus"] = Field(None, description="The current status of the collaboration.")

    model_config = {'populate_by_name': True}


class DeleteCollaborationCustomerPartnerResponse(BaseModel):
    """Empty response object denoting successful deletion of a customer partner."""
    pass


class DeleteCollaborationIdMappingTableResponse(BaseModel):
    pass


class Error(BaseModel):
    """The error response object."""
    code: Optional[str] = Field(None, description="The HTTP status code of the response.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class GetCollaborationIdMappingJobForTrackingIdResponse(BaseModel):
    id_mapping_job_id: Optional[str] = Field(None, alias="idMappingJobId", description="Unique identifier of the ID mapping workflow job linked to the tracking ID provided in the request.")

    model_config = {'populate_by_name': True}


class GetCollaborationIdMappingJobResponse(BaseModel):
    id_mapping_job: Optional["CollaborationIdMappingJob"] = Field(None, alias="idMappingJob")

    model_config = {'populate_by_name': True}


class GetInstanceAdvertisersResponse(BaseModel):
    advertisers: Optional[list["Advertiser"]] = Field(None, description="List of advertisers added to the AMC instance. Currently supported advertiser types include DSP advertisers and Sponsore")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token to use in subsequent request to retrieve next page of results. Null if all results have been returned.")
    total_count: Optional[int] = Field(None, alias="totalCount", description="Total number of advertisers with the specified advertiser type in this instance")

    model_config = {'populate_by_name': True}


class GetInstanceCollaborationResponse(BaseModel):
    collaboration: Optional["CollaborationSummary"] = None

    model_config = {'populate_by_name': True}


class GetInstanceResponse(BaseModel):
    instance: Optional["Instance"] = None

    model_config = {'populate_by_name': True}


class InstanceCustomerAwsAccountMetadataPayload(BaseModel):
    """AWS account metadata"""
    aws_account_id: str = Field(..., alias="awsAccountId", description="The identifier of the customer's AWS account.")
    bucket_name: str = Field(..., alias="bucketName", description="The name of the S3 bucket in the customer's AWS account.")

    model_config = {'populate_by_name': True}


class ListCollaborationIdMappingJobsPayload(BaseModel):
    """The payload of the request."""
    max_results: Optional[int] = Field(None, alias="maxResults", description="Optional. Maximum number of results to retrieve in a single API call.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional. The pagination token from the previous API call.")

    model_config = {'populate_by_name': True}


class ListCollaborationIdMappingJobsResponse(BaseModel):
    id_mapping_jobs: Optional[list["CollaborationIdMappingJobSummary"]] = Field(None, alias="idMappingJobs", description="List of id mapping jobs.")
    id_mapping_table_id: Optional[str] = Field(None, alias="idMappingTableId", description="Unique identifier of the id mapping table the jobs are associated to.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="The pagination token from the previous API call.")

    model_config = {'populate_by_name': True}


class ListCollaborationIdMappingTablesPayload(BaseModel):
    """The payload of the request."""
    max_results: Optional[int] = Field(None, alias="maxResults", description="Optional. Maximum number of results to retrieve in a single API call.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional. The pagination token from the previous API call.")

    model_config = {'populate_by_name': True}


class ListCollaborationIdMappingTablesResponse(BaseModel):
    collaboration_id: Optional[str] = Field(None, alias="collaborationId", description="Unique identifier of the collaboration the ID mapping tables are associated to.")
    id_mapping_tables: Optional[list["CollaborationIdMappingTable"]] = Field(None, alias="idMappingTables", description="The list of id mapping tables.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="The pagination token from the previous API call.")

    model_config = {'populate_by_name': True}


class ListCollaborationIdNamespacesPayload(BaseModel):
    """The payload of the request."""
    max_results: Optional[int] = Field(None, alias="maxResults", description="Optional (not used). Maximum number of results to retrieve in a single API call. This API will always use the default va")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional. The pagination token from the previous API call.")

    model_config = {'populate_by_name': True}


class ListCollaborationIdNamespacesResponse(BaseModel):
    collaboration_id: Optional[str] = Field(None, alias="collaborationId", description="Unique identifier of the collaboration the ID namespaces are associated to.")
    collaboration_id_namespace_associations: Optional[list["CollaborationIdNamespaceAssociation"]] = Field(None, alias="collaborationIdNamespaceAssociations", description="The list of ID namespaces associated to the collaboration.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="The pagination token from the previous API call.")

    model_config = {'populate_by_name': True}


class ListInstancesResponse(BaseModel):
    instances: Optional[list["Instance"]] = Field(None, description="List of AMC instances.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional. Token to use in subsequent request to retrieve next page of results. Null if all results have been returned.")

    model_config = {'populate_by_name': True}


class RefreshCollaborationIdMappingTableResponse(BaseModel):
    collaboration_id: Optional[str] = Field(None, alias="collaborationId", description="Unique identifier of the collaboration the id mapping table belongs to.")
    id_mapping_workflow_job_id: Optional[str] = Field(None, alias="idMappingWorkflowJobId", description="Unique identifier of the job started to refresh the id mapping table. If AMC was not able to start the job, this field w")
    tracking_id: Optional[str] = Field(None, alias="trackingId", description="Unique identifier of a job tracking token in AMC. When this attribute is not null, it indicates an idMappingWorkflowJobI")

    model_config = {'populate_by_name': True}


class UpdateCollaborationCustomerPartnersPayload(BaseModel):
    """The payload of the request."""
    acr_customer_partners: list["AcrCustomerPartner"] = Field(..., alias="acrCustomerPartners", description="The list of customer partners that will be updated in the collaboration in an instance backed by AWS Clean Rooms (ACR).")

    model_config = {'populate_by_name': True}


class UpdateCollaborationCustomerPartnersResponse(BaseModel):
    acr_customer_partners: Optional[list["AcrCustomerPartner"]] = Field(None, alias="acrCustomerPartners", description="The list of customer partners updated in the collaboration.")

    model_config = {'populate_by_name': True}


class UpdateCollaborationCustomerRequest(BaseModel):
    aws_account_id: Optional[str] = Field(None, alias="awsAccountId", description="The new AWS account ID of the customer.")

    model_config = {'populate_by_name': True}


class UpdateCollaborationCustomerResponse(BaseModel):
    aws_account_id: Optional[str] = Field(None, alias="awsAccountId", description="The updated AWS account ID of the customer.")
    status: Optional["CollaborationMemberStatus"] = Field(None, description="The current status of the customer member in the collaboration.")

    model_config = {'populate_by_name': True}


class UpdateInstanceCustomerAwsAccountMetadataResponse(BaseModel):
    cfn_bucket_url: Optional[str] = Field(None, alias="cfnBucketUrl", description="The CloudFormation link to create the S3 bucket in the customer's AWS account.")

    model_config = {'populate_by_name': True}

