"""Auto-generated Pydantic models. Do not edit manually.

Source: AmazonMarketingStream_prod_3p.json
Title:  Amazon Marketing Stream
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class AccessForbiddenErrorResponseContent(BaseModel):
    code: Optional[str] = None
    message: str

    model_config = {'populate_by_name': True}


class SqsDestination(BaseModel):
    queue_arn: str = Field(..., alias="queueArn")

    model_config = {'populate_by_name': True}


class FirehoseDestination(BaseModel):
    delivery_stream_arn: str = Field(..., alias="deliveryStreamArn")
    subscriber_role_arn: str = Field(..., alias="subscriberRoleArn")
    subscription_role_arn: str = Field(..., alias="subscriptionRoleArn")

    model_config = {'populate_by_name': True}


class Destination(BaseModel):
    firehose_destination: Optional["FirehoseDestination"] = Field(None, alias="firehoseDestination")
    sqs_destination: Optional["SqsDestination"] = Field(None, alias="sqsDestination")

    model_config = {'populate_by_name': True}


class CreateDspStreamSubscriptionRequestContent(BaseModel):
    client_request_token: str = Field(..., alias="clientRequestToken", description="Unique value supplied by the caller used to track identical API requests. Should request be re-tried, the caller should ")
    data_set_id: str = Field(..., alias="dataSetId", description="Identifier of data set, callers can be subscribed to. Please refer to https://advertising.amazon.com/API/docs/en-us/amaz")
    destination: Optional["Destination"] = None
    destination_arn: Optional[str] = Field(None, alias="destinationArn", description="AWS ARN of the destination endpoint associated with the subscription. Supported destination types: - SQS")
    notes: Optional[str] = Field(None, description="Additional details associated with the subscription")

    model_config = {'populate_by_name': True}


class CreateDspStreamSubscriptionResponseContent(BaseModel):
    client_request_token: str = Field(..., alias="clientRequestToken", description="Unique value supplied by the caller used to track identical API requests. Should request be re-tried, the caller should ")
    subscription_id: str = Field(..., alias="subscriptionId", description="Unique subscription identifier")

    model_config = {'populate_by_name': True}


class CreateStreamSubscriptionRequestContent(BaseModel):
    client_request_token: str = Field(..., alias="clientRequestToken", description="Unique value supplied by the caller used to track identical API requests. Should request be re-tried, the caller should ")
    data_set_id: str = Field(..., alias="dataSetId", description="Identifier of data set, callers can be subscribed to. Please refer to https://advertising.amazon.com/API/docs/en-us/amaz")
    destination: Optional["Destination"] = None
    destination_arn: Optional[str] = Field(None, alias="destinationArn", description="AWS ARN of the destination endpoint associated with the subscription. Supported destination types: - SQS")
    notes: Optional[str] = Field(None, description="Additional details associated with the subscription")

    model_config = {'populate_by_name': True}


class CreateStreamSubscriptionResponseContent(BaseModel):
    client_request_token: str = Field(..., alias="clientRequestToken", description="Unique value supplied by the caller used to track identical API requests. Should request be re-tried, the caller should ")
    subscription_id: str = Field(..., alias="subscriptionId", description="Unique subscription identifier")

    model_config = {'populate_by_name': True}


class SubscriptionEntityStatus(StrEnum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    FAILED_CONFIRMATION = "FAILED_CONFIRMATION"
    FAILED_PROVISIONING = "FAILED_PROVISIONING"
    PENDING_CONFIRMATION = "PENDING_CONFIRMATION"
    PROVISIONING = "PROVISIONING"
    SUSPENDED = "SUSPENDED"


class StreamSubscription(BaseModel):
    created_date: str = Field(..., alias="createdDate", description="ISO8601 Timestamp")
    data_set_id: str = Field(..., alias="dataSetId", description="Identifier of data set, callers can be subscribed to. Please refer to https://advertising.amazon.com/API/docs/en-us/amaz")
    destination: Optional["Destination"] = None
    destination_arn: Optional[str] = Field(None, alias="destinationArn", description="AWS ARN of the destination endpoint associated with the subscription. Supported destination types: - SQS")
    notes: Optional[str] = Field(None, description="Additional details associated with the subscription")
    status: "SubscriptionEntityStatus"
    subscription_id: str = Field(..., alias="subscriptionId", description="Unique subscription identifier")
    updated_date: str = Field(..., alias="updatedDate", description="ISO8601 Timestamp")

    model_config = {'populate_by_name': True}


class GetDspStreamSubscriptionResponseContent(BaseModel):
    subscription: "StreamSubscription"

    model_config = {'populate_by_name': True}


class GetStreamSubscriptionResponseContent(BaseModel):
    subscription: "StreamSubscription"

    model_config = {'populate_by_name': True}


class InternalServerErrorResponseContent(BaseModel):
    code: Optional[str] = None
    message: str

    model_config = {'populate_by_name': True}


class InvalidRequestErrorResponseContent(BaseModel):
    code: Optional[str] = None
    message: str

    model_config = {'populate_by_name': True}


class ListDspStreamSubscriptionsResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token which can be used to get the next page of results, if more entries exist")
    subscriptions: list["StreamSubscription"]

    model_config = {'populate_by_name': True}


class ListStreamSubscriptionsResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="Token which can be used to get the next page of results, if more entries exist")
    subscriptions: list["StreamSubscription"]

    model_config = {'populate_by_name': True}


class OperationConflictErrorResponseContent(BaseModel):
    code: Optional[str] = None
    message: str

    model_config = {'populate_by_name': True}


class ResourceNotFoundErrorResponseContent(BaseModel):
    code: Optional[str] = None
    message: str

    model_config = {'populate_by_name': True}


class TooManyRequestsErrorResponseContent(BaseModel):
    code: Optional[str] = None
    message: str

    model_config = {'populate_by_name': True}


class UnauthorizedAccessErrorResponseContent(BaseModel):
    code: Optional[str] = None
    message: str

    model_config = {'populate_by_name': True}


class UpdateEntityStatus(StrEnum):
    ARCHIVED = "ARCHIVED"


class UpdateDspStreamSubscriptionRequestContent(BaseModel):
    notes: Optional[str] = Field(None, description="Additional details associated with the subscription")
    status: Optional["UpdateEntityStatus"] = None

    model_config = {'populate_by_name': True}


class UpdateStreamSubscriptionRequestContent(BaseModel):
    notes: Optional[str] = Field(None, description="Additional details associated with the subscription")
    status: Optional["UpdateEntityStatus"] = None

    model_config = {'populate_by_name': True}

