"""Auto-generated async API client. Do not edit manually.

Source: DataProvider_openapi.yaml
Title:  Amazon Ads API for Data Providers.
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_data_provider_v2 import *  # noqa: F403
except ImportError:
    pass


class DataProviderV2Client(BaseAdsClient):
    """Auto-generated from DataProvider_openapi.yaml (5 operations)"""

    async def post_v2_dp_audiencemetadata(self, body: dict[str, Any] | None = None, authorization: str | None = None, amazon_advertising_api_client_id: str | None = None, content_type: str | None = None) -> JSONData | JSONList:
        """POST /v2/dp/audiencemetadata/

        Creates a new data provider audience. Note that the API call rate is limited to 1 transaction per second (TPS). Calls ex
        """
        endpoint = "/v2/dp/audiencemetadata/"
        params: dict[str, Any] = {}
        if authorization is not None:
            params["Authorization"] = authorization
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if content_type is not None:
            params["Content-Type"] = content_type
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def put_v2_dp_audiencemetadata_by_id(self, audience_id: str, body: dict[str, Any] | None = None, authorization: str | None = None, amazon_advertising_api_client_id: str | None = None, content_type: str | None = None) -> JSONData | JSONList:
        """PUT /v2/dp/audiencemetadata/{audienceId}

        Updates metadata of an existing audience specified by identifier. Note that the API call rate is limited to 1 transactio
        """
        endpoint = f"/v2/dp/audiencemetadata/{audience_id}"
        params: dict[str, Any] = {}
        if authorization is not None:
            params["Authorization"] = authorization
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if content_type is not None:
            params["Content-Type"] = content_type
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params)

    async def get_v2_dp_audiencemetadata_by_id(self, audience_id: str, authorization: str | None = None, amazon_advertising_api_client_id: str | None = None, content_type: str | None = None) -> JSONData | JSONList:
        """GET /v2/dp/audiencemetadata/{audienceId}

        Gets metadata for an audience specified by identifier. Note that the API call rate is limited to 1 transaction per secon
        """
        endpoint = f"/v2/dp/audiencemetadata/{audience_id}"
        params: dict[str, Any] = {}
        if authorization is not None:
            params["Authorization"] = authorization
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if content_type is not None:
            params["Content-Type"] = content_type
        return await self.get(endpoint, params=params)

    async def patch_v2_dp_audience(self, body: dict[str, Any] | None = None, authorization: str | None = None, amazon_advertising_api_client_id: str | None = None, content_type: str | None = None) -> JSONData | JSONList:
        """PATCH /v2/dp/audience

        Associates or disassociates a record with an audience. Note that the API call rate is limited to 100 transactions per se
        """
        endpoint = "/v2/dp/audience"
        params: dict[str, Any] = {}
        if authorization is not None:
            params["Authorization"] = authorization
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if content_type is not None:
            params["Content-Type"] = content_type
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self._request('PATCH', endpoint, json_data=json_data, params=params)

    async def patch_v2_dp_users(self, body: dict[str, Any] | None = None, authorization: str | None = None, amazon_advertising_api_client_id: str | None = None, content_type: str | None = None) -> JSONData | JSONList:
        """PATCH /v2/dp/users

        Deletes user data originally sourced from the client. The API call rate is limited to 1 transactions per second (TPS). C
        """
        endpoint = "/v2/dp/users"
        params: dict[str, Any] = {}
        if authorization is not None:
            params["Authorization"] = authorization
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientID"] = amazon_advertising_api_client_id
        if content_type is not None:
            params["Content-Type"] = content_type
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self._request('PATCH', endpoint, json_data=json_data, params=params)

