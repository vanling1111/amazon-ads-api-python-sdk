"""Auto-generated async API client. Do not edit manually.

Source: Posts_prod_3p.json
Title:  Posts
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_posts import *  # noqa: F403
except ImportError:
    pass


class PostsClient(BaseAdsClient):
    """Auto-generated from Posts_prod_3p.json (11 operations)"""

    async def create_post(self, body: CreatePostRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /bp/v2/posts

        API to create a Post.
        """
        endpoint = "/bp/v2/posts"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.bpPost.v2+json")

    async def list_posts(self, body: ListPostsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /bp/v2/posts/list

        API to get posts data along with performance metrics for each post.
        """
        endpoint = "/bp/v2/posts/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.bpPost.v2+json")

    async def get_post(self, post_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /bp/v2/posts/{postId}

        Get a post.
        """
        endpoint = f"/bp/v2/posts/{post_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def update_post(self, post_id: str, body: UpdatePostRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /bp/v2/posts/{postId}

        Update a Post's data.
        """
        endpoint = f"/bp/v2/posts/{post_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.bpPost.v2+json")

    async def submit_post_for_review(self, post_id: str, body: SubmitPostForReviewRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /bp/v2/posts/{postId}/submitForReview

        Submit a Post for review.
        """
        endpoint = f"/bp/v2/posts/{post_id}/submitForReview"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.bpPost.v2+json")

    async def withdraw_post(self, post_id: str, body: WithdrawPostRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /bp/v2/posts/{postId}/unpublish

        Unpublishes a Post from Amazon.
        """
        endpoint = f"/bp/v2/posts/{post_id}/unpublish"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.bpPost.v2+json")

    async def get_post_products(self, asins: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /bp/v2/products/list

        Get information for a list of products.
        """
        endpoint = "/bp/v2/products/list"
        params: dict[str, Any] = {}
        if asins is not None:
            params["asins"] = asins
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def list_profiles(self, next_token: str | None = None, max_results: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /bp/v2/profiles

        Get a list of Post Profiles that the advertiser has access to.
        """
        endpoint = "/bp/v2/profiles"
        params: dict[str, Any] = {}
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def get_profile(self, profile_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /bp/v2/profiles/{profileId}

        Get information for a Post Profile.
        """
        endpoint = f"/bp/v2/profiles/{profile_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def get_profile_metrics(self, profile_id: str, body: GetProfileMetricsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /bp/v2/profiles/{profileId}/metrics

        Get brand level performance metrics from Posts.
        """
        endpoint = f"/bp/v2/profiles/{profile_id}/metrics"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.bpProfile.v2+json")

    async def get_report_download_link(self, profile_id: str, metric_start_date: str | None = None, metric_end_date: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /bp/v2/profiles/{profileId}/metrics/download

        Get a URL to download a metrics report for the Post Profile.
        """
        endpoint = f"/bp/v2/profiles/{profile_id}/metrics/download"
        params: dict[str, Any] = {}
        if metric_start_date is not None:
            params["metricStartDate"] = metric_start_date
        if metric_end_date is not None:
            params["metricEndDate"] = metric_end_date
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

