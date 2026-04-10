"""Auto-generated async API client. Do not edit manually.

Source: BrandAidV2_prod_3p.json
Title:  BrandAidV2
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_brand_associations import *  # noqa: F403
except ImportError:
    pass


class BrandAssociationsClient(BaseAdsClient):
    """Auto-generated from BrandAidV2_prod_3p.json (2 operations)"""

    async def query_brand_advertiser_association(self, body: QueryBrandAdvertiserAssociationRequestContent | dict[str, Any] | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/query/brandAdvertiserAssociations

        <p>Query brands associated to an advertiser account.</p>  **Authorized resource type**: Global Ad Account ID  **Paramete
        """
        endpoint = "/adsApi/v1/query/brandAdvertiserAssociations"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data)

    async def retrieve_brand(self, body: RetrieveBrandRequestContent | dict[str, Any] | None = None) -> JSONData | JSONList:
        """POST /adsApi/v1/retrieve/brands

        <p>Get brand details for the specified brand identifiers.</p>  **Requires one of these permissions**: []
        """
        endpoint = "/adsApi/v1/retrieve/brands"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data)

