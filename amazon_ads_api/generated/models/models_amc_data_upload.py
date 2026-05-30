"""Auto-generated Pydantic models. Do not edit manually.

Source: AdvertiserDataUpload_prod_3p.json
Title:  Advertiser Data Upload
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class ExternalIdentityType(StrEnum):
    EXPERIAN = "EXPERIAN"
    IDFA = "IDFA"
    KANTAR = "KANTAR"
    LIVERAMP = "LIVERAMP"
    MAID = "MAID"
    MERKLE = "MERKLE"
    NEUSTAR = "NEUSTAR"
    REALID = "REALID"
    SAMBATV = "SAMBATV"


class HashedPiiType(StrEnum):
    ADDRESS = "ADDRESS"
    CITY = "CITY"
    COUNTRY_CODE = "COUNTRY_CODE"
    EMAIL = "EMAIL"
    FIRST_NAME = "FIRST_NAME"
    LAST_NAME = "LAST_NAME"
    PHONE = "PHONE"
    STATE = "STATE"
    ZIP = "ZIP"


class UserIdType(BaseModel):
    """Specifies the type of an identity. An identity column may represent either a single hashed PII attribute, or an external identity in one of the supported identity spaces."""
    pass


class ConsentType(StrEnum):
    AMZN_AD_STORAGE = "AMZN_AD_STORAGE"
    AMZN_USER_DATA = "AMZN_USER_DATA"
    GPP = "GPP"
    TCF = "TCF"


class DataType(StrEnum):
    DATE = "DATE"
    DECIMAL = "DECIMAL"
    INTEGER = "INTEGER"
    LONG = "LONG"
    STRING = "STRING"
    TIMESTAMP = "TIMESTAMP"


class ColumnType(StrEnum):
    DIMENSION = "DIMENSION"
    METRIC = "METRIC"


class Column(BaseModel):
    """The definition of a column in a data set."""
    column_type: "ColumnType" = Field(..., alias="columnType")
    consent_type: Optional["ConsentType"] = Field(None, alias="consentType")
    data_type: "DataType" = Field(..., alias="dataType")
    description: Optional[str] = Field(None, description="Optional. The human-readable description of the purpose of this column.")
    external_user_id_type: Optional["UserIdType"] = Field(None, alias="externalUserIdType")
    is_country_code: Optional[bool] = Field(None, alias="isCountryCode", description="Optional. If this column is countryCode or not. Default is false.")
    is_main_event_time: Optional[bool] = Field(None, alias="isMainEventTime", description="Optional. If this column is contains the main event time of the record. Default is false.")
    is_main_user_id: Optional[bool] = Field(None, alias="isMainUserId", description="Optional. If this column is the resolved user id. Default is false.")
    is_main_user_id_type: Optional[bool] = Field(None, alias="isMainUserIdType", description="Optional. If this column should contain the resolved user id type. Default is false.")
    name: str = Field(..., description="The name of this column.")
    nullable: Optional[bool] = Field(None, description="Optional. If data in this column can be null or not. Default is true.")
    requires_one_way_hashing: Optional[bool] = Field(None, alias="requiresOneWayHashing", description="Optional. If this column requires one way hashing or not. Default is false.")

    model_config = {'populate_by_name': True}


class AddColumnToDataSetRequestContent(BaseModel):
    """A request to add a column to a data set."""
    column: "Column"

    model_config = {'populate_by_name': True}


class TimePartitionGranularity(StrEnum):
    P1D = "P1D"
    P1M = "P1M"
    PT1H = "PT1H"


class DataSet(BaseModel):
    """The definition of a data set."""
    columns: list["Column"] = Field(..., description="A list of data set columns.")
    country_code: Optional[str] = Field(None, alias="countryCode", description="Optional. A field that specifies a country. Values corresponds to ISO-3166 codes for country definitions. Required to re")
    customer_encryption_key_arn: Optional[str] = Field(None, alias="customerEncryptionKeyArn", description="Optional. If the data being uploaded is encrypted with a customer-managed encryption key, the ARN of said encryption key")
    data_set_id: str = Field(..., alias="dataSetId", description="The unique identifier of the data set. Used to query the data set. Cannot contain spaces.")
    description: Optional[str] = Field(None, description="Optional. The human-readable description of the data set.")
    period: Optional["TimePartitionGranularity"] = None

    model_config = {'populate_by_name': True}


class AddColumnToDataSetResponseContent(BaseModel):
    """A response containing the updated data set containing the new column."""
    data_set: Optional["DataSet"] = Field(None, alias="dataSet")

    model_config = {'populate_by_name': True}


class BadRequestExceptionResponseContent(BaseModel):
    """Bad Request."""
    code: Optional[str] = Field(None, description="The error code associated with the exception.")
    details: Optional[str] = Field(None, description="The error code associated with the exception.")
    errors: Optional[list[str]] = Field(None, description="The error message(s) associated with the exception.")
    request_id: Optional[str] = Field(None, alias="requestId", description="The request ID associated with the exception.")

    model_config = {'populate_by_name': True}


class ComparatorOperator(StrEnum):
    EQ = "EQ"
    GT = "GT"
    GTE = "GTE"
    LT = "LT"
    LTE = "LTE"


class CompressionFormat(StrEnum):
    BZIP = "BZIP"
    GZIP = "GZIP"
    NONE = "NONE"
    SNAPPY = "SNAPPY"
    ZIP = "ZIP"


class CreateDataSetRequestContent(BaseModel):
    """A request to create a new data set."""
    data_set: "DataSet" = Field(..., alias="dataSet")

    model_config = {'populate_by_name': True}


class CreateDataSetResponseContent(BaseModel):
    """A response containing the identifiers of the created data set."""
    data_set_id: Optional[str] = Field(None, alias="dataSetId", description="The data set ID of the data set created.")
    instance_id: Optional[str] = Field(None, alias="instanceId", description="The instance ID of the instance.")

    model_config = {'populate_by_name': True}


class UpdateStrategy(StrEnum):
    ADDITIVE = "ADDITIVE"
    FULL_REPLACE = "FULL_REPLACE"
    OVERLAP_KEEP = "OVERLAP_KEEP"
    OVERLAP_REPLACE = "OVERLAP_REPLACE"


class CustomerDataSource(BaseModel):
    """Describes the source of the data. Exactly one of `sourceManifestS3Key`, `sourceFileS3Key`, or `sourceS3Prefix` must be provided."""
    source_file_s3_key: Optional[str] = Field(None, alias="sourceFileS3Key", description="S3 key of the single object to upload.")
    source_manifest_s3_key: Optional[str] = Field(None, alias="sourceManifestS3Key", description="S3 key of the manifest containing the object(s) to upload.")
    source_s3_bucket: str = Field(..., alias="sourceS3Bucket", description="S3 bucket that is the source of the upload.")
    source_s3_prefix: Optional[str] = Field(None, alias="sourceS3Prefix", description="S3 key prefix containing the object(s) to upload.")

    model_config = {'populate_by_name': True}


class ParquetDataFormat(StrEnum):
    PARQUET_DATA_FORMAT = "PARQUET_DATA_FORMAT"


class CsvDataFormat(BaseModel):
    """Represents a CSV data format, and the values needed to ingest the source CSV file."""
    comment_character: Optional[str] = Field(None, alias="commentCharacter", description="Optional. String representing the comment character for a CSV file. Default is none.")
    field_delimiter: Optional[str] = Field(None, alias="fieldDelimiter", description="Optional. String representing the field delimiter for a CSV file. Default is `,`.")
    quote_character: Optional[str] = Field(None, alias="quoteCharacter", description="Optional. String representing the quote character for a CSV file. Default is `'`.")
    quote_escape_character: Optional[str] = Field(None, alias="quoteEscapeCharacter", description="Optional. String representing the quote escape character for a CSV file. Default is `\\`.")
    record_delimiter: Optional[str] = Field(None, alias="recordDelimiter", description="Optional. String representing the record delimiter for a CSV file. Default is `\\n`.")

    model_config = {'populate_by_name': True}


class JsonDataFormat(StrEnum):
    DOCUMENT = "DOCUMENT"
    LINES = "LINES"


class FileFormat(BaseModel):
    """The format in which data to be uploaded is stored. Exactly one of `csvDataFormat`, `jsonDataFormat`, or `parquetDataFormat` must be provided."""
    pass


class CreateUploadRequestContent(BaseModel):
    """A request to create a new upload to a data set."""
    compression_format: "CompressionFormat" = Field(..., alias="compressionFormat")
    country_code: Optional[str] = Field(None, alias="countryCode", description="Optional. A field that specifies a country. Values corresponds to ISO-3166 codes for country definitions. Required to re")
    data_source: "CustomerDataSource" = Field(..., alias="dataSource")
    file_format: "FileFormat" = Field(..., alias="fileFormat")
    update_strategy: "UpdateStrategy" = Field(..., alias="updateStrategy")

    model_config = {'populate_by_name': True}


class Status(StrEnum):
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    SUBMITTED = "SUBMITTED"
    SUCCESS = "SUCCESS"


class CreateUploadResponseContent(BaseModel):
    """A response containing information about the upload."""
    status: Optional["Status"] = None
    upload_id: Optional[str] = Field(None, alias="uploadId", description="The ID of the upload request.")

    model_config = {'populate_by_name': True}


class ExternalIdentity(BaseModel):
    """Representation of an External Identity to be removed. Contains the type of the ID, and the String value of the ID."""
    type_: "ExternalIdentityType" = Field(..., alias="type")
    value: str

    model_config = {'populate_by_name': True}


class HashedIdentity(BaseModel):
    """One or more pairs of a Hashed PII type and corresponding hashed value, representing a single individual to be deleted."""
    __root__: dict[str, str] = {}


class Identity(BaseModel):
    """The user identity to be deleted. Either an ExternalId or a collection of Hashed PII values representing a single user."""
    pass


class CreateUserDeletionRequestRequestContent(BaseModel):
    """A request to delete some user identities from previously uploaded data."""
    target_identities: list["Identity"] = Field(..., alias="targetIdentities", description="Identities to be deleted. Max number of identities to delete is 1,000 per request.")

    model_config = {'populate_by_name': True}


class CreateUserDeletionRequestResponseContent(BaseModel):
    """A response containing information about the deletion request."""
    user_deletion_request_id: str = Field(..., alias="userDeletionRequestId", description="The request ID of the user deletion request.")

    model_config = {'populate_by_name': True}


class DeleteColumnFromDataSetResponseContent(BaseModel):
    """A response containing the updated data set without the deleted column."""
    data_set: Optional["DataSet"] = Field(None, alias="dataSet")

    model_config = {'populate_by_name': True}


class DeleteDataSetResponseContent(BaseModel):
    """A response containing identifiers of the deleted data set."""
    data_set_id: Optional[str] = Field(None, alias="dataSetId", description="The data set ID of the deleted data set.")
    instance_id: Optional[str] = Field(None, alias="instanceId", description="The instance ID of the instance.")

    model_config = {'populate_by_name': True}


class ForbiddenRequestExceptionResponseContent(BaseModel):
    """Forbidden. The request failed because the user does not have access to the specified resource."""
    code: Optional[str] = Field(None, description="The error code associated with the exception.")
    details: Optional[str] = Field(None, description="The error code associated with the exception.")
    errors: Optional[list[str]] = Field(None, description="The error message(s) associated with the exception.")
    request_id: Optional[str] = Field(None, alias="requestId", description="The request ID associated with the exception.")

    model_config = {'populate_by_name': True}


class GatewayTimeoutExceptionResponseContent(BaseModel):
    """Internal server timeout waiting on upstream service. Retry later. Contact support if this response persists."""
    code: Optional[str] = Field(None, description="The error code associated with the exception.")
    details: Optional[str] = Field(None, description="The error code associated with the exception.")
    errors: Optional[list[str]] = Field(None, description="The error message(s) associated with the exception.")
    request_id: Optional[str] = Field(None, alias="requestId", description="The request ID associated with the exception.")

    model_config = {'populate_by_name': True}


class GetDataSetResponseContent(BaseModel):
    """A response containing the definition of the data set."""
    data_set: Optional["DataSet"] = Field(None, alias="dataSet")

    model_config = {'populate_by_name': True}


class MetricsMap(BaseModel):
    """A map containing metrics about an upload, where the key is the name of the metric and the value is a double representing the numerical value of said metric."""
    __root__: dict[str, float] = {}


class Upload(BaseModel):
    """The available metadata about a previously submitted upload."""
    country_code: Optional[str] = Field(None, alias="countryCode", description="Optional. A field that specifies a country. Values corresponds to ISO-3166 codes for country definitions. Required to re")
    created_at: Optional[str] = Field(None, alias="createdAt", description="A timestamp representing the time the upload was created.")
    data_set_id: Optional[str] = Field(None, alias="dataSetId", description="The data set ID of the upload.")
    data_source: Optional["CustomerDataSource"] = Field(None, alias="dataSource")
    instance_id: Optional[str] = Field(None, alias="instanceId", description="The instance ID of the upload.")
    message: Optional[str] = Field(None, description="A message specifying details of the upload. This is usually an error message describing a failure.")
    metrics: Optional["MetricsMap"] = None
    status: Optional["Status"] = None
    updated_at: Optional[str] = Field(None, alias="updatedAt", description="A timestamp representing the last time the upload was updated.")
    upload_id: Optional[str] = Field(None, alias="uploadId", description="The unique identifier for an upload.")

    model_config = {'populate_by_name': True}


class GetUploadResponseContent(BaseModel):
    """A response containing information about the upload."""
    upload: Optional["Upload"] = None

    model_config = {'populate_by_name': True}


class UserDeletionStatus(StrEnum):
    PENDING = "PENDING"
    SUCCEEDED = "SUCCEEDED"


class UserDeletion(BaseModel):
    """The available metadata about a previously submitted user deletion request."""
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="A timestamp representing the time the user deletion request was created. This field is in UTC and is formatted as yyyy-M")
    identity_count: Optional[float] = Field(None, alias="identityCount", description="The number of identities requested for user deletion.")
    status: Optional["UserDeletionStatus"] = None
    user_deletion_request_id: Optional[str] = Field(None, alias="userDeletionRequestId", description="The request ID of the user deletion request.")

    model_config = {'populate_by_name': True}


class GetUserDeletionRequestResponseContent(BaseModel):
    """A response containing information about the user deletion request."""
    identity_deletion: Optional["UserDeletion"] = Field(None, alias="identityDeletion")

    model_config = {'populate_by_name': True}


class InternalServerExceptionResponseContent(BaseModel):
    """Internal server error. Retry later. Contact support if this response persists."""
    code: Optional[str] = Field(None, description="The error code associated with the exception.")
    details: Optional[str] = Field(None, description="The error code associated with the exception.")
    errors: Optional[list[str]] = Field(None, description="The error message(s) associated with the exception.")
    request_id: Optional[str] = Field(None, alias="requestId", description="The request ID associated with the exception.")

    model_config = {'populate_by_name': True}


class ListDataSetsResponseContent(BaseModel):
    """A response containing a list of data sets for the specified instance."""
    data_sets: Optional[list["DataSet"]] = Field(None, alias="dataSets", description="The list of data sets returned by the request.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional. Token to use in subsequent request to retrieve next page of results. Null if all results have been returned.")

    model_config = {'populate_by_name': True}


class ListUploadsResponseContent(BaseModel):
    """A response containing a list of uploads for the specified instance."""
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional. Token to use in subsequent request to retrieve next page of results. Null if all results have been returned.")
    uploads: Optional[list["Upload"]] = Field(None, description="The list of uploads for the specified instance.")

    model_config = {'populate_by_name': True}


class ListUserDeletionRequestsResponseContent(BaseModel):
    """A response containing a list of user deletion requests."""
    next_token: Optional[str] = Field(None, alias="nextToken", description="Optional. Token to use in subsequent request to retrieve next page of results. Null if all results have been returned.")
    user_deletions: Optional[list["UserDeletion"]] = Field(None, alias="userDeletions", description="List of identity deletions.")

    model_config = {'populate_by_name': True}


class ResourceNotFoundExceptionResponseContent(BaseModel):
    """The requested resource was not found."""
    code: Optional[str] = Field(None, description="The error code associated with the exception.")
    details: Optional[str] = Field(None, description="The error code associated with the exception.")
    errors: Optional[list[str]] = Field(None, description="The error message(s) associated with the exception.")
    request_id: Optional[str] = Field(None, alias="requestId", description="The request ID associated with the exception.")

    model_config = {'populate_by_name': True}


class TooManyRequestsExceptionResponseContent(BaseModel):
    """Too Many Requests. The request was rate-limited. Retry later."""
    code: Optional[str] = Field(None, description="The error code associated with the exception.")
    details: Optional[str] = Field(None, description="The error code associated with the exception.")
    errors: Optional[list[str]] = Field(None, description="The error message(s) associated with the exception.")
    request_id: Optional[str] = Field(None, alias="requestId", description="The request ID associated with the exception.")

    model_config = {'populate_by_name': True}


class UnauthorizedRequestExceptionResponseContent(BaseModel):
    """Unauthorized. The request failed because the user is not authenticated or is not allowed to invoke the operation."""
    code: Optional[str] = Field(None, description="The error code associated with the exception.")
    details: Optional[str] = Field(None, description="The error code associated with the exception.")
    errors: Optional[list[str]] = Field(None, description="The error message(s) associated with the exception.")
    request_id: Optional[str] = Field(None, alias="requestId", description="The request ID associated with the exception.")

    model_config = {'populate_by_name': True}


class UpdateColumnInDataSetRequestContent(BaseModel):
    """A request to update a column in a data set."""
    update_description: Optional[str] = Field(None, alias="updateDescription", description="Optional. An updated column description.")
    updated_column_name: Optional[str] = Field(None, alias="updatedColumnName", description="Optional. An updated column name.")

    model_config = {'populate_by_name': True}


class UpdateColumnInDataSetResponseContent(BaseModel):
    """A response containing the updated data set containing the updated column."""
    data_set: Optional["DataSet"] = Field(None, alias="dataSet")

    model_config = {'populate_by_name': True}


class UpdateDataSetRequestContent(BaseModel):
    """A request to update a data set definition."""
    country_code: Optional[str] = Field(None, alias="countryCode", description="Optional. A field that specifies a country. Values corresponds to ISO-3166 codes for country definitions. Required to re")
    description: Optional[str] = Field(None, description="Optional. An updated description of the data set defintion.")

    model_config = {'populate_by_name': True}


class UpdateDataSetResponseContent(BaseModel):
    """A response containing the updated data set definition."""
    data_set: Optional["DataSet"] = Field(None, alias="dataSet")

    model_config = {'populate_by_name': True}

