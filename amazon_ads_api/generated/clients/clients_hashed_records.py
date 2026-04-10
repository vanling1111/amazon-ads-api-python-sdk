"""Auto-generated async API client. Do not edit manually.

Source: HashedRecords_prod_3p.json
Title:  Hashed Records
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_hashed_records import *  # noqa: F403
except ImportError:
    pass


class HashedRecordsClient(BaseAdsClient):
    """Auto-generated from HashedRecords_prod_3p.json (1 operations)"""

    async def upload_hashed_records(self, body: dict[str, Any] | None = None, authorization: str | None = None, amazon_advertising_api_client_id: str | None = None, content_type: str | None = None) -> JSONData | JSONList:
        """POST /dp/records/hashed

        Upload a batch of hashed records for matching
        """
        endpoint = "/dp/records/hashed"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dpuploadhashedrecordsrequest.v3+json")

