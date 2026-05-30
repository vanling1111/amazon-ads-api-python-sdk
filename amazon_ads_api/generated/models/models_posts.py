"""Auto-generated Pydantic models. Do not edit manually.

Source: Posts_prod_3p.json
Title:  Posts
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class AccessDeniedExceptionResponseContent(BaseModel):
    """Access Denied Exception - Caller was not authorized to make this call."""
    code: Optional[str] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class AggregateProfileMetrics(BaseModel):
    """Set of aggregated metric for a given date range."""
    clicks_to_detail_page: Optional[float] = Field(None, alias="clicksToDetailPage")
    engagements: Optional[float] = None
    impressions: Optional[float] = None
    reach: Optional[float] = None

    model_config = {'populate_by_name': True}


class AggregateType(StrEnum):
    DAY = "DAY"
    WEEK = "WEEK"


class ConflictExceptionResponseContent(BaseModel):
    """Conflict Exception - Updating or deleting this resource can cause an inconsistent state."""
    code: Optional[str] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class MediaMetadata(BaseModel):
    """When mediaType is image, keys: assetId. When mediaType is video, keys: assetId, thumbnailUrl, closedCaptionUrl"""
    __root__: dict[str, str] = {}


class Media(BaseModel):
    """A media for a post."""
    media_id: Optional[str] = Field(None, alias="mediaId")
    media_metadata: Optional["MediaMetadata"] = Field(None, alias="mediaMetadata")
    media_type: Optional[str] = Field(None, alias="mediaType", description="One of the following: video, image")
    media_url: Optional[str] = Field(None, alias="mediaUrl")

    model_config = {'populate_by_name': True}


class CreatePostRequestContent(BaseModel):
    """Contains the post fields to create the post with."""
    caption: Optional[str] = Field(None, description="Caption for a post.")
    medias: list["Media"] = Field(..., description="A list of medias for a post.")
    products: list[str] = Field(..., description="A list of product identifiers.")
    profile_id: str = Field(..., alias="profileId", description="Identifier for a profile.")
    scheduled_live_date: Optional[str] = Field(None, alias="scheduledLiveDate", description="A date and time for when to publish a post. The value is in ISO8601 date-time format (UTC). For example, 2020-08-16T18:2")
    scheduled_withdrawal_date: Optional[str] = Field(None, alias="scheduledWithdrawalDate", description="A date and time for when to unpublish a post. The value is in ISO8601 date-time format (UTC). For example, 2020-08-16T18")

    model_config = {'populate_by_name': True}


class MetricsForPost(BaseModel):
    """A map of metrics for a post. Represents metric data. The detail on metric data is available in the link below: https://advertising.amazon.com/help#G8FRSCXFWNDW962E.  **Note**: Metrics only available f"""
    __root__: dict[str, float] = {}


class PostStatus(StrEnum):
    DRAFT = "DRAFT"
    LIVE = "LIVE"
    REJECTED = "REJECTED"
    REVIEW = "REVIEW"
    SCHEDULED = "SCHEDULED"
    WITHDRAWN = "WITHDRAWN"


class PromotionMetadata(BaseModel):
    """Metadata related to promoting a post to ad."""
    is_eligible_for_promotion: Optional[bool] = Field(None, alias="isEligibleForPromotion", description="Whether the post is eligible for promotion.")

    model_config = {'populate_by_name': True}


class RejectionEvidenceType(StrEnum):
    ASIN = "ASIN"
    DUPLICATE_IMAGE = "DUPLICATE_IMAGE"


class RejectionEvidence(BaseModel):
    """Additional information for a rejection of a post or profile."""
    component_id: Optional[str] = Field(None, alias="componentId")
    type_: Optional["RejectionEvidenceType"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class RejectionReason(BaseModel):
    """Reason for rejecting a post or profile."""
    code: Optional[str] = None
    detail: Optional[str] = None
    evidences: Optional[list["RejectionEvidence"]] = None

    model_config = {'populate_by_name': True}


class StatusMetadata(BaseModel):
    """Additional data about the status of a post/profile."""
    media_defects: Optional[list[str]] = Field(None, alias="mediaDefects", description="Quality defects that can affect the impressions/engagement of a post.")
    rejection_reasons: Optional[list["RejectionReason"]] = Field(None, alias="rejectionReasons", description="A list of rejection reasons.")

    model_config = {'populate_by_name': True}


class Post(BaseModel):
    """A post, along with metadata about the post.   **Note: Metrics are not available for a single GetPost request.**"""
    caption: Optional[str] = Field(None, description="Caption for a post.")
    created_date: Optional[str] = Field(None, alias="createdDate", description="Date and time for when the post was created. The value is in ISO8601 date-time format (UTC). For example, 2020-08-16T18:")
    id_: Optional[str] = Field(None, alias="id")
    is_flagged_for_quality: Optional[bool] = Field(None, alias="isFlaggedForQuality", description="Whether the post has quality defects or not.")
    last_modified: Optional[str] = Field(None, alias="lastModified", description="Date and time for when the post was last modified. The value is in ISO8601 date-time format (UTC). For example, 2020-08-")
    live_date: Optional[str] = Field(None, alias="liveDate", description="Date and time for when the post was published. The value is in ISO8601 date-time format (UTC). For example, 2020-08-16T1")
    media_url: Optional[str] = Field(None, alias="mediaUrl")
    medias: Optional[list["Media"]] = Field(None, description="A list of medias for a post.")
    metrics: Optional["MetricsForPost"] = None
    products: Optional[list[str]] = Field(None, description="A list of product identifiers.")
    profile_id: Optional[str] = Field(None, alias="profileId", description="Identifier for a profile.")
    promotion_metadata: Optional["PromotionMetadata"] = Field(None, alias="promotionMetadata")
    scheduled_live_date: Optional[str] = Field(None, alias="scheduledLiveDate", description="Date and time for when the post was unpublished. The value is in ISO8601 date-time format (UTC). For example, 2020-08-16")
    scheduled_withdrawal_date: Optional[str] = Field(None, alias="scheduledWithdrawalDate", description="A date and time for when to unpublish a post. The value is in ISO8601 date-time format (UTC). For example, 2020-08-16T18")
    status: Optional["PostStatus"] = None
    status_metadata: Optional["StatusMetadata"] = Field(None, alias="statusMetadata")
    version: Optional[float] = Field(None, description="Version of a post. Used to ensure that post writes are consistent. Calls can only update the latest version of a post.")
    withdrawn_date: Optional[str] = Field(None, alias="withdrawnDate", description="Date and time for when the post was unpublished. The value is in ISO8601 date-time format (UTC). For example, 2020-08-16")

    model_config = {'populate_by_name': True}


class CreatePostResponseContent(BaseModel):
    """Returns the post created."""
    post: Optional["Post"] = None

    model_config = {'populate_by_name': True}


class ProductPriceSummary(BaseModel):
    basis_price: Optional[str] = Field(None, alias="basisPrice")
    max_price: Optional[str] = Field(None, alias="maxPrice")
    min_price: Optional[str] = Field(None, alias="minPrice")
    winning_price: Optional[str] = Field(None, alias="winningPrice")

    model_config = {'populate_by_name': True}


class ProductReviewSummary(BaseModel):
    display_string: Optional[str] = Field(None, alias="displayString")
    half_star: Optional[bool] = Field(None, alias="halfStar")
    review_full_star: Optional[float] = Field(None, alias="reviewFullStar")
    total_customer_review_count: Optional[float] = Field(None, alias="totalCustomerReviewCount")
    value: Optional[float] = None

    model_config = {'populate_by_name': True}


class Product(BaseModel):
    availability: Optional[str] = None
    customer_review_summary: Optional["ProductReviewSummary"] = Field(None, alias="customerReviewSummary")
    detail_page_url: Optional[str] = Field(None, alias="detailPageUrl")
    id_: Optional[str] = Field(None, alias="id")
    image_url: Optional[str] = Field(None, alias="imageUrl")
    is_prime: Optional[bool] = Field(None, alias="isPrime")
    name: Optional[str] = None
    price_summary: Optional["ProductPriceSummary"] = Field(None, alias="priceSummary")

    model_config = {'populate_by_name': True}


class ProductIneligibilityCode(StrEnum):
    INVALID = "INVALID"
    PROHIBITED = "PROHIBITED"
    UNAUTHORIZED = "UNAUTHORIZED"


class IneligibleProduct(BaseModel):
    """A product that is not eligible to be added to a post, along with the reason code."""
    asin: Optional[str] = Field(None, description="Identifier for a product on Amazon.")
    ineligibility_code: Optional["ProductIneligibilityCode"] = Field(None, alias="ineligibilityCode")

    model_config = {'populate_by_name': True}


class GetPostProductsResponseContent(BaseModel):
    eligible_products: Optional[list["Product"]] = Field(None, alias="eligibleProducts")
    ineligible_products: Optional[list["IneligibleProduct"]] = Field(None, alias="ineligibleProducts", description="List of ineligible products that cannot be added to a post.")

    model_config = {'populate_by_name': True}


class GetPostResponseContent(BaseModel):
    """Returns the post."""
    post: Optional["Post"] = None

    model_config = {'populate_by_name': True}


class GetProfileMetricsRequestContent(BaseModel):
    """Contains the profile identifier to get metrics for, the metric start and end dates, and the type of aggregation period for metrics. AggregateType can be either DAY or WEEK. For example, to get total m"""
    aggregate_type: Optional["AggregateType"] = Field(None, alias="aggregateType")
    metric_end_date: Optional[str] = Field(None, alias="metricEndDate", description="The end date to get metrics for. The value is in ISO8601 full-date format (UTC). For example, 2020-08-16.")
    metric_start_date: Optional[str] = Field(None, alias="metricStartDate", description="The start date to get metrics for. The value is in ISO8601 full-date format (UTC). For example, 2020-08-16.")

    model_config = {'populate_by_name': True}


class ProfileMetric(BaseModel):
    """Set of metrics at a profile level for a particular date."""
    clicks_to_detail_page: Optional[float] = Field(None, alias="clicksToDetailPage")
    date: Optional[str] = None
    engagements: Optional[float] = None
    impressions: Optional[float] = None
    reach: Optional[float] = None

    model_config = {'populate_by_name': True}


class GetProfileMetricsResponseContent(BaseModel):
    """Brand level performance metrics for posts."""
    aggregate_metrics: Optional["AggregateProfileMetrics"] = Field(None, alias="aggregateMetrics")
    aggregate_type: Optional["AggregateType"] = Field(None, alias="aggregateType")
    metrics: Optional[list["ProfileMetric"]] = None

    model_config = {'populate_by_name': True}


class ProfilePendingReviewChanges(BaseModel):
    """Values for a profile that are pending review."""
    logo_url: Optional[str] = Field(None, alias="logoUrl")
    name: Optional[str] = None
    status: Optional[str] = None

    model_config = {'populate_by_name': True}


class Profile(BaseModel):
    """A Post Profile represents a brand that can create posts."""
    brand_id: Optional[str] = Field(None, alias="brandId", description="Identifier for a brand on Brand Registry.")
    brand_profile_id: Optional[str] = Field(None, alias="brandProfileId", description="Identifier for a Brand Profile.")
    browse_node_id: Optional[str] = Field(None, alias="browseNodeId", description="Large Browse Refinement Brand identifier.")
    feed_url: Optional[str] = Field(None, alias="feedUrl", description="URL for the profile's post feed on Amazon.com")
    is_authorized: Optional[bool] = Field(None, alias="isAuthorized")
    last_approval_date: Optional[str] = Field(None, alias="lastApprovalDate")
    logo_url: Optional[str] = Field(None, alias="logoUrl")
    name: Optional[str] = None
    pending_changes: Optional["ProfilePendingReviewChanges"] = Field(None, alias="pendingChanges")
    post_profile_id: Optional[str] = Field(None, alias="postProfileId", description="Identifier for a profile.")
    status: Optional[str] = None
    status_metadata: Optional["StatusMetadata"] = Field(None, alias="statusMetadata")

    model_config = {'populate_by_name': True}


class GetProfileResponseContent(BaseModel):
    """Returns the profile."""
    profile: Optional["Profile"] = None

    model_config = {'populate_by_name': True}


class GetReportDownloadLinkResponseContent(BaseModel):
    """Returns a URL that can be used to download the metrics report."""
    metric_end_date: Optional[str] = Field(None, alias="metricEndDate", description="The end date to get metrics for. The value is in ISO8601 full-date format (UTC). For example, 2020-08-16.")
    metric_start_date: Optional[str] = Field(None, alias="metricStartDate", description="The start date to get metrics for. The value is in ISO8601 full-date format (UTC). For example, 2020-08-16.")
    profile_id: Optional[str] = Field(None, alias="profileId", description="Identifier for a profile.")
    report_download_url: Optional[str] = Field(None, alias="reportDownloadUrl", description="Link to download a metrics report.")

    model_config = {'populate_by_name': True}


class InternalServerExceptionResponseContent(BaseModel):
    """Internal Server Exception - Something went wrong with the server. Please try again later. If the issue persists, report an error."""
    code: Optional[str] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class PostListFilterField(StrEnum):
    CAPTION = "caption"
    CREATEDDATE = "createdDate"
    FLAGGEDFORQUALITY = "flaggedForQuality"
    STATE = "state"


class PostListFilterType(StrEnum):
    RANGE = "RANGE"
    TEXT = "TEXT"
    VALUES = "VALUES"


class PostListFilter(BaseModel):
    """A post filter."""
    end_date: Optional[str] = Field(None, alias="endDate", description="End date for a date range filter.")
    field_name: Optional["PostListFilterField"] = Field(None, alias="fieldName")
    filter_type: Optional["PostListFilterType"] = Field(None, alias="filterType")
    start_date: Optional[str] = Field(None, alias="startDate", description="Start date for a date range filter.")
    values: Optional[list[str]] = Field(None, description="Specifies a list of values to filter by. Applies only for filters of type VALUES and TEXT.")

    model_config = {'populate_by_name': True}


class PostListSortField(StrEnum):
    CLICKTHROUGHRATE = "clickThroughRate"
    CLICKSTOBRANDSTORE = "clicksToBrandStore"
    CLICKSTODETAILPAGE = "clicksToDetailPage"
    CLICKSTOFOLLOW = "clicksToFollow"
    CREATEDDATE = "createdDate"
    ENGAGEMENT = "engagement"
    IMPRESSIONS = "impressions"
    LIVEDATE = "liveDate"
    REACH = "reach"
    STATE = "state"


class PostListSortOrder(StrEnum):
    ASC = "ASC"
    DESC = "DESC"


class PostListSortCriterion(BaseModel):
    """The criteria to determine how to sort a list of posts. Consists of the field to sort by, and the order."""
    sort_field: Optional["PostListSortField"] = Field(None, alias="sortField")
    sort_order: Optional["PostListSortOrder"] = Field(None, alias="sortOrder")

    model_config = {'populate_by_name': True}


class MetricName(StrEnum):
    CLICKTHROUGHRATE = "clickThroughRate"
    CLICKSTOBRANDSTORE = "clicksToBrandStore"
    CLICKSTODETAILPAGE = "clicksToDetailPage"
    CLICKSTOFOLLOW = "clicksToFollow"
    ENGAGEMENT = "engagement"
    IMPRESSIONS = "impressions"
    REACH = "reach"


class ListPostsRequestContent(BaseModel):
    """Contains the profile identifier, optional metric date range, filters, sort criteria, and list of metrics to return. Request also contains pagination token and max results for paginated requests."""
    filters: Optional[list["PostListFilter"]] = Field(None, description="A list of post filters.")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Number of items to be returned on this call.")
    metric_end_date: Optional[str] = Field(None, alias="metricEndDate", description="The end date to get metrics for. The value is in ISO8601 full-date format (UTC). For example, 2020-08-16.")
    metric_start_date: Optional[str] = Field(None, alias="metricStartDate", description="The start date to get metrics for. The value is in ISO8601 full-date format (UTC). For example, 2020-08-16.")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Pagination token to get next page of results from previous call.")
    profile_id: str = Field(..., alias="profileId", description="Identifier for a profile.")
    selected_metrics: Optional[list["MetricName"]] = Field(None, alias="selectedMetrics", description="A list of metrics to return for each post.")
    sort_criterion: Optional["PostListSortCriterion"] = Field(None, alias="sortCriterion")

    model_config = {'populate_by_name': True}


class ListPostsResponseContent(BaseModel):
    """Returns list of posts with metrics. Also returns pagination token to get the next page of posts."""
    is_num_posts_over_limit: Optional[bool] = Field(None, alias="isNumPostsOverLimit", description="No more than 10,000 posts can be sorted by a field other than CREATED_DATE. This value represents if that limit has been")
    next_token: Optional[str] = Field(None, alias="nextToken", description="Pagination token to get next page of results from previous call.")
    posts: Optional[list["Post"]] = Field(None, description="A list of posts.")
    total_posts: Optional[float] = Field(None, alias="totalPosts", description="Total number of posts that exist within the conditions of the request.")

    model_config = {'populate_by_name': True}


class ListProfilesResponseContent(BaseModel):
    """Returns a list of profiles that the user has access to."""
    next_token: Optional[str] = Field(None, alias="nextToken", description="Pagination token to get next page of results from previous call.")
    profiles: Optional[list["Profile"]] = None

    model_config = {'populate_by_name': True}


class ResourceNotFoundExceptionResponseContent(BaseModel):
    """Resource Not Found Exception - The request references a resource that does not exist."""
    code: Optional[str] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class ServiceLimitExceededExceptionResponseContent(BaseModel):
    """Service Limit Exceeded Exception - A service limit has been exceeded in this request."""
    code: Optional[str] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class SubmitPostForReviewRequestContent(BaseModel):
    """Contains post identifier and version of the post to submit for review."""
    version: float = Field(..., description="Version of a post. Used to ensure that post writes are consistent. Calls can only update the latest version of a post.")

    model_config = {'populate_by_name': True}


class SubmitPostForReviewResponseContent(BaseModel):
    """Returns the post submitted for review."""
    post: Optional["Post"] = None

    model_config = {'populate_by_name': True}


class ThrottlingExceptionResponseContent(BaseModel):
    """Throttling Exception - Request was throttled."""
    code: Optional[str] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class UpdatePostRequestContent(BaseModel):
    """Contains post identifier and post data for post to be saved.  Also contains the version of the post that is intended to be saved."""
    caption: Optional[str] = Field(None, description="Caption for a post.")
    medias: list["Media"] = Field(..., description="A list of medias for a post.")
    products: list[str] = Field(..., description="A list of product identifiers.")
    profile_id: str = Field(..., alias="profileId", description="Identifier for a profile.")
    scheduled_live_date: Optional[str] = Field(None, alias="scheduledLiveDate", description="A date and time for when to publish a post. The value is in ISO8601 date-time format (UTC). For example, 2020-08-16T18:2")
    scheduled_withdrawal_date: Optional[str] = Field(None, alias="scheduledWithdrawalDate", description="A date and time for when to unpublish a post. The value is in ISO8601 date-time format (UTC). For example, 2020-08-16T18")
    version: float = Field(..., description="Version of a post. Used to ensure that post writes are consistent. Calls can only update the latest version of a post.")

    model_config = {'populate_by_name': True}


class UpdatePostResponseContent(BaseModel):
    """Returns post that was saved."""
    post: Optional["Post"] = None

    model_config = {'populate_by_name': True}


class ValidationExceptionResponseContent(BaseModel):
    """Validation Exception - Request failed because invalid parameters were provided."""
    code: Optional[str] = None
    message: Optional[str] = None
    request_id: Optional[str] = Field(None, alias="requestId")

    model_config = {'populate_by_name': True}


class WithdrawPostRequestContent(BaseModel):
    """Contains post identifier and version of post to be unpublished."""
    version: float = Field(..., description="Version of a post. Used to ensure that post writes are consistent. Calls can only update the latest version of a post.")

    model_config = {'populate_by_name': True}


class WithdrawPostResponseContent(BaseModel):
    """Returns post that was unpublished."""
    post: Optional["Post"] = None

    model_config = {'populate_by_name': True}

