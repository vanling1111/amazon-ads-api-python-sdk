"""
Sponsored Display - Locations API (异步版本)
SD地理位置定向

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SDLocationsAPI(BaseAdsClient):
    """SD Locations API (全异步)"""

    async def list_locations(
        self,
        location_type: str | None = None,
        max_results: int = 100,
    ) -> JSONData:
        """
        获取可用的地理位置列表
        
        Args:
            location_type: 位置类型（COUNTRY, REGION, CITY等）
            max_results: 最大结果数
        """
        params: JSONData = {}
        if location_type:
            params["locationType"] = location_type
        if max_results:
            params["count"] = max_results

        result = await self.get("/sd/locations", params=params or None)
        return result if isinstance(result, dict) else {"locations": []}

    async def search_locations(
        self,
        query: str,
        location_type: str | None = None,
        max_results: int = 50,
    ) -> JSONData:
        """
        搜索地理位置
        
        Args:
            query: 搜索关键词
            location_type: 位置类型
            max_results: 最大结果数
        """
        body: JSONData = {"query": query, "maxResults": max_results}
        if location_type:
            body["locationType"] = location_type

        result = await self.post("/sd/locations", json_data=body)
        return result if isinstance(result, dict) else {"locations": []}

    async def delete_locations(self, location_ids: list[str]) -> JSONData:
        """
        删除位置定向 (归档)
        
        官方请求格式: {"locationExpressionIdFilter": {"include": [...]}}
        
        Args:
            location_ids: Location Expression ID列表
        """
        result = await self.post(
            "/sd/locations/delete",
            json_data={"locationExpressionIdFilter": {"include": location_ids}}
        )
        return result if isinstance(result, dict) else {"success": [], "error": []}

