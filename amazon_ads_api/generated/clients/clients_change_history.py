"""Auto-generated async API client. Do not edit manually.

Source: Changehistory_prod_3p.json
Title:  Change history
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_change_history import *  # noqa: F403
except ImportError:
    pass


class ChangeHistoryClient(BaseAdsClient):
    """Auto-generated from Changehistory_prod_3p.json (1 operations)"""

    async def get_history(self, body: dict[str, Any] | None = None) -> JSONData | JSONList:
        """POST /history

        History of entity changes.
        """
        endpoint = "/history"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data)

