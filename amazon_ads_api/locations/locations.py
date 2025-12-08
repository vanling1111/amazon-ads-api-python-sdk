"""
Amazon Ads Locations API (异步版本)
地理位置定向
"""

from typing import Any
from ..base import BaseAdsClient, JSONData, JSONList


class LocationsAPI(BaseAdsClient):
    """Locations API (全异步)"""

    # ==================== 位置搜索 ====================

    async def search_locations(
        self,
        query: str,
        location_type: str | None = None,
        country_code: str | None = None,
        max_results: int = 100,
    ) -> JSONList:
        """搜索位置"""
        params: dict[str, Any] = {
            "query": query,
            "maxResults": max_results,
        }
        if location_type:
            params["locationType"] = location_type
        if country_code:
            params["countryCode"] = country_code

        response = await self.get("/locations/search", params=params)
        if isinstance(response, dict):
            return response.get("locations", [])
        return []

    async def get_location(self, location_id: str) -> JSONData:
        """获取位置详情"""
        result = await self.get(f"/locations/{location_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 位置层级 ====================

    async def list_countries(self) -> JSONList:
        """获取国家列表"""
        response = await self.get("/locations/countries")
        if isinstance(response, dict):
            return response.get("countries", [])
        return []

    async def list_states(self, country_code: str) -> JSONList:
        """获取州/省列表"""
        params = {"countryCode": country_code}
        response = await self.get("/locations/states", params=params)
        if isinstance(response, dict):
            return response.get("states", [])
        return []

    async def list_cities(self, state_id: str) -> JSONList:
        """获取城市列表"""
        params = {"stateId": state_id}
        response = await self.get("/locations/cities", params=params)
        if isinstance(response, dict):
            return response.get("cities", [])
        return []

    async def list_dmas(self, country_code: str = "US") -> JSONList:
        """获取DMA列表"""
        params = {"countryCode": country_code}
        response = await self.get("/locations/dmas", params=params)
        if isinstance(response, dict):
            return response.get("dmas", [])
        return []

    async def list_postal_codes(
        self,
        city_id: str | None = None,
        state_id: str | None = None,
        prefix: str | None = None,
        max_results: int = 100,
    ) -> JSONList:
        """获取邮编列表"""
        params: dict[str, Any] = {"maxResults": max_results}
        if city_id:
            params["cityId"] = city_id
        if state_id:
            params["stateId"] = state_id
        if prefix:
            params["prefix"] = prefix

        response = await self.get("/locations/postalCodes", params=params)
        if isinstance(response, dict):
            return response.get("postalCodes", [])
        return []

    # ==================== 批量查询 ====================

    async def get_locations_by_ids(self, location_ids: list[str]) -> JSONList:
        """批量获取位置信息"""
        data = {"locationIds": location_ids}
        response = await self.post("/locations/batch", json_data=data)
        if isinstance(response, dict):
            return response.get("locations", [])
        return []
