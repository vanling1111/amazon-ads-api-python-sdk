"""
Amazon Ads Locations API (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/locations
OpenAPI Spec: Locations_prod_3p.json

地理位置数据
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class LocationsAPI(BaseAdsClient):
    """
    Locations API (全异步)
    
    官方端点 (共1个):
    - POST /locations/list - 获取位置列表
    
    注意:
    - 目前仅支持美国市场 (US only)
    - 支持按 locationId、name、category 过滤
    """

    async def list_locations(
        self,
        filters: list[dict] | None = None,
        max_results: int = 10,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取位置列表
        
        POST /locations/list
        
        Args:
            filters: 过滤条件列表
                [
                    {"field": "locationId", "values": ["xxx"]},
                    {"field": "name", "values": ["New York"]},  # 模糊搜索
                    {"field": "category", "values": ["CITY"]}
                ]
                
                field 支持:
                - locationId: 位置 ID
                - name: 位置名称（模糊搜索）
                - category: 位置类别
                    - CITY: 城市
                    - STATE: 州/省
                    - DMA: 指定市场区域
                    - COUNTRY: 国家
                    - POSTAL_CODE: 邮编
            max_results: 每页结果数 (1-2000，默认 10)
            next_token: 分页 token
        
        Returns:
            {
                "locations": [
                    {
                        "locationId": "xxx",
                        "name": "New York",
                        "category": "CITY"
                    }
                ],
                "nextToken": "..."
            }
        """
        params: JSONData = {}
        
        if max_results != 10:
            params["maxResults"] = max_results
        if next_token:
            params["nextToken"] = next_token
        
        body: JSONData = {}
        if filters:
            body["filters"] = filters
        
        result = await self.post(
            "/locations/list",
            json_data=body if body else None,
            params=params if params else None
        )
        return result if isinstance(result, dict) else {"locations": []}

    # ============ 便捷方法 ============

    async def search_by_name(
        self,
        name: str,
        category: str | None = None,
        max_results: int = 100,
    ) -> JSONList:
        """
        按名称搜索位置（模糊搜索）
        
        Args:
            name: 位置名称
            category: 可选，限制类别
        """
        filters = [{"field": "name", "values": [name]}]
        
        if category:
            filters.append({"field": "category", "values": [category.upper()]})
        
        result = await self.list_locations(filters=filters, max_results=max_results)
        return result.get("locations", [])

    async def get_by_ids(self, location_ids: list[str]) -> JSONList:
        """批量按 ID 获取位置"""
        filters = [{"field": "locationId", "values": location_ids}]
        result = await self.list_locations(filters=filters, max_results=len(location_ids))
        return result.get("locations", [])

    async def get_by_id(self, location_id: str) -> JSONData | None:
        """按 ID 获取单个位置"""
        locations = await self.get_by_ids([location_id])
        return locations[0] if locations else None

    async def list_cities(self, name_query: str | None = None, max_results: int = 100) -> JSONList:
        """获取城市列表"""
        filters = [{"field": "category", "values": ["CITY"]}]
        if name_query:
            filters.append({"field": "name", "values": [name_query]})
        
        result = await self.list_locations(filters=filters, max_results=max_results)
        return result.get("locations", [])

    async def list_states(self, name_query: str | None = None, max_results: int = 100) -> JSONList:
        """获取州/省列表"""
        filters = [{"field": "category", "values": ["STATE"]}]
        if name_query:
            filters.append({"field": "name", "values": [name_query]})
        
        result = await self.list_locations(filters=filters, max_results=max_results)
        return result.get("locations", [])

    async def list_dmas(self, name_query: str | None = None, max_results: int = 100) -> JSONList:
        """获取 DMA（指定市场区域）列表"""
        filters = [{"field": "category", "values": ["DMA"]}]
        if name_query:
            filters.append({"field": "name", "values": [name_query]})
        
        result = await self.list_locations(filters=filters, max_results=max_results)
        return result.get("locations", [])

    async def list_postal_codes(self, name_query: str | None = None, max_results: int = 100) -> JSONList:
        """获取邮编列表"""
        filters = [{"field": "category", "values": ["POSTAL_CODE"]}]
        if name_query:
            filters.append({"field": "name", "values": [name_query]})
        
        result = await self.list_locations(filters=filters, max_results=max_results)
        return result.get("locations", [])

    async def list_all_locations(
        self,
        filters: list[dict] | None = None,
        max_pages: int = 50,
    ) -> JSONList:
        """
        获取所有位置（自动处理分页）
        
        Args:
            filters: 过滤条件
            max_pages: 最大页数限制
        """
        all_locations: JSONList = []
        next_token = None
        
        for _ in range(max_pages):
            result = await self.list_locations(
                filters=filters,
                max_results=2000,
                next_token=next_token
            )
            
            locations = result.get("locations", [])
            all_locations.extend(locations)
            
            next_token = result.get("nextToken")
            if not next_token:
                break
        
        return all_locations
