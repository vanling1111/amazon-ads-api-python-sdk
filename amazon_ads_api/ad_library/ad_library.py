"""
Amazon Ads Ad Library API (异步版本)
广告库服务
"""

from typing import Any
from enum import Enum
from ..base import BaseAdsClient, JSONData


class AdType(str, Enum):
    """广告类型"""
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    DSP = "DSP"


class NameMatchType(str, Enum):
    """名称匹配类型"""
    EXACT = "EXACT"
    CONTAINS = "CONTAINS"
    STARTS_WITH = "STARTS_WITH"


class AdLibraryAPI(BaseAdsClient):
    """Ad Library API (全异步)"""

    # ==================== 广告搜索 ====================

    async def list_ads(
        self,
        *,
        advertiser_name: str | None = None,
        name_match_type: NameMatchType | None = None,
        ad_types: list[AdType] | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        marketplace_ids: list[str] | None = None,
        page_token: str | None = None,
        page_size: int = 100,
    ) -> JSONData:
        """搜索广告列表"""
        request_body: dict[str, Any] = {"pageSize": page_size}

        if advertiser_name:
            request_body["advertiserName"] = advertiser_name
        if name_match_type:
            request_body["nameMatchType"] = name_match_type.value
        if ad_types:
            request_body["adTypes"] = [t.value for t in ad_types]
        if start_date:
            request_body["startDate"] = start_date
        if end_date:
            request_body["endDate"] = end_date
        if marketplace_ids:
            request_body["marketplaceIds"] = marketplace_ids
        if page_token:
            request_body["pageToken"] = page_token

        result = await self.post("/adLibrary/ads/list", json_data=request_body)
        return result if isinstance(result, dict) else {"ads": []}

    async def get_ads_by_id(self, ad_ids: list[str]) -> JSONData:
        """根据ID获取广告详情"""
        result = await self.post("/adLibrary/ads", json_data={"adIds": ad_ids})
        return result if isinstance(result, dict) else {"ads": []}

    # ==================== 广告主搜索 ====================

    async def search_advertisers(
        self,
        *,
        query: str,
        marketplace_ids: list[str] | None = None,
        page_size: int = 100,
    ) -> JSONData:
        """搜索广告主"""
        request_body: dict[str, Any] = {
            "query": query,
            "pageSize": page_size,
        }

        if marketplace_ids:
            request_body["marketplaceIds"] = marketplace_ids

        result = await self.post("/adLibrary/advertisers/search", json_data=request_body)
        return result if isinstance(result, dict) else {"advertisers": []}

    # ==================== 统计信息 ====================

    async def get_ad_statistics(
        self,
        *,
        advertiser_id: str,
        start_date: str,
        end_date: str,
        granularity: str = "DAILY",
    ) -> JSONData:
        """获取广告统计信息"""
        result = await self.post(
            "/adLibrary/statistics",
            json_data={
                "advertiserId": advertiser_id,
                "startDate": start_date,
                "endDate": end_date,
                "granularity": granularity,
            },
        )
        return result if isinstance(result, dict) else {}

    # ==================== 类别和筛选 ====================

    async def get_categories(self, marketplace_id: str) -> JSONData:
        """获取可用的广告类别"""
        result = await self.get("/adLibrary/categories", params={"marketplaceId": marketplace_id})
        return result if isinstance(result, dict) else {"categories": []}

    async def get_filters(self, marketplace_id: str) -> JSONData:
        """获取可用的筛选选项"""
        result = await self.get("/adLibrary/filters", params={"marketplaceId": marketplace_id})
        return result if isinstance(result, dict) else {}
