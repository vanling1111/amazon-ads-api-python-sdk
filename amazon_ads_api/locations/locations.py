"""
Locations API

官方文档: https://advertising.amazon.com/API/docs/en-us/guides/sponsored-display/non-amazon-sellers/locations
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Locations_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class LocationsAPI(BaseAdsClient):
    """Locations API - 地理位置定向
    
    管理Sponsored Display广告的地理位置定向。
    """
    
    # ==================== 位置搜索 ====================
    
    async def search_locations(
        self,
        query: str,
        location_type: Optional[str] = None,
        country_code: Optional[str] = None,
        max_results: int = 100,
    ) -> List[Dict[str, Any]]:
        """搜索位置
        
        Args:
            query: 搜索关键词
            location_type: 位置类型 (COUNTRY, STATE, CITY, ZIP, DMA)
            country_code: 国家代码
            max_results: 最大结果数
            
        Returns:
            位置列表
        """
        params = {
            "query": query,
            "maxResults": max_results,
        }
        if location_type:
            params["locationType"] = location_type
        if country_code:
            params["countryCode"] = country_code
            
        response = await self._make_request(
            "GET",
            "/locations/search",
            params=params,
        )
        return response.get("locations", [])
    
    async def get_location(
        self,
        location_id: str,
    ) -> Dict[str, Any]:
        """获取位置详情
        
        Args:
            location_id: 位置ID
            
        Returns:
            位置详情
        """
        return await self._make_request(
            "GET",
            f"/locations/{location_id}",
        )
    
    # ==================== 位置层级 ====================
    
    async def list_countries(self) -> List[Dict[str, Any]]:
        """获取国家列表
        
        Returns:
            国家列表
        """
        response = await self._make_request(
            "GET",
            "/locations/countries",
        )
        return response.get("countries", [])
    
    async def list_states(
        self,
        country_code: str,
    ) -> List[Dict[str, Any]]:
        """获取州/省列表
        
        Args:
            country_code: 国家代码
            
        Returns:
            州/省列表
        """
        params = {"countryCode": country_code}
        response = await self._make_request(
            "GET",
            "/locations/states",
            params=params,
        )
        return response.get("states", [])
    
    async def list_cities(
        self,
        state_id: str,
    ) -> List[Dict[str, Any]]:
        """获取城市列表
        
        Args:
            state_id: 州/省ID
            
        Returns:
            城市列表
        """
        params = {"stateId": state_id}
        response = await self._make_request(
            "GET",
            "/locations/cities",
            params=params,
        )
        return response.get("cities", [])
    
    async def list_dmas(
        self,
        country_code: str = "US",
    ) -> List[Dict[str, Any]]:
        """获取DMA（指定市场区域）列表
        
        Args:
            country_code: 国家代码（默认US）
            
        Returns:
            DMA列表
        """
        params = {"countryCode": country_code}
        response = await self._make_request(
            "GET",
            "/locations/dmas",
            params=params,
        )
        return response.get("dmas", [])
    
    async def list_postal_codes(
        self,
        city_id: Optional[str] = None,
        state_id: Optional[str] = None,
        prefix: Optional[str] = None,
        max_results: int = 100,
    ) -> List[Dict[str, Any]]:
        """获取邮编列表
        
        Args:
            city_id: 城市ID
            state_id: 州/省ID
            prefix: 邮编前缀
            max_results: 最大结果数
            
        Returns:
            邮编列表
        """
        params = {"maxResults": max_results}
        if city_id:
            params["cityId"] = city_id
        if state_id:
            params["stateId"] = state_id
        if prefix:
            params["prefix"] = prefix
            
        response = await self._make_request(
            "GET",
            "/locations/postalCodes",
            params=params,
        )
        return response.get("postalCodes", [])
    
    # ==================== 批量查询 ====================
    
    async def get_locations_by_ids(
        self,
        location_ids: List[str],
    ) -> List[Dict[str, Any]]:
        """批量获取位置信息
        
        Args:
            location_ids: 位置ID列表
            
        Returns:
            位置信息列表
        """
        data = {"locationIds": location_ids}
        response = await self._make_request(
            "POST",
            "/locations/batch",
            json=data,
        )
        return response.get("locations", [])

