"""
Amazon Ads Stores Analytics API

官方文档: https://advertising.amazon.com/API/docs/en-us/reference/openapi-download
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Stores_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class StoresAnalyticsAPI(BaseAdsClient):
    """Stores Analytics API - 品牌旗舰店分析
    
    获取品牌旗舰店的流量和转化数据。
    """
    
    # ==================== 旗舰店列表 ====================
    
    async def list_stores(
        self,
        brand_entity_id: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """获取品牌旗舰店列表
        
        Args:
            brand_entity_id: 品牌实体ID (可选)
            
        Returns:
            旗舰店列表
        """
        params = {}
        if brand_entity_id:
            params["brandEntityId"] = brand_entity_id
            
        response = await self._make_request(
            "GET",
            "/stores",
            params=params if params else None,
        )
        return response.get("stores", [])
    
    async def get_store(
        self,
        store_id: str,
    ) -> Dict[str, Any]:
        """获取旗舰店详情
        
        Args:
            store_id: 旗舰店ID
            
        Returns:
            旗舰店详情
        """
        return await self._make_request(
            "GET",
            f"/stores/{store_id}",
        )
    
    # ==================== 旗舰店页面 ====================
    
    async def list_store_pages(
        self,
        store_id: str,
    ) -> List[Dict[str, Any]]:
        """获取旗舰店页面列表
        
        Args:
            store_id: 旗舰店ID
            
        Returns:
            页面列表
        """
        response = await self._make_request(
            "GET",
            f"/stores/{store_id}/pages",
        )
        return response.get("pages", [])
    
    async def get_store_page(
        self,
        store_id: str,
        page_id: str,
    ) -> Dict[str, Any]:
        """获取旗舰店页面详情
        
        Args:
            store_id: 旗舰店ID
            page_id: 页面ID
            
        Returns:
            页面详情
        """
        return await self._make_request(
            "GET",
            f"/stores/{store_id}/pages/{page_id}",
        )
    
    # ==================== 分析报告 ====================
    
    async def get_store_insights(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
        metrics: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """获取旗舰店洞察数据
        
        Args:
            store_id: 旗舰店ID
            start_date: 开始日期 (YYYY-MM-DD)
            end_date: 结束日期 (YYYY-MM-DD)
            metrics: 指标列表
            
        Returns:
            洞察数据
        """
        params = {
            "startDate": start_date,
            "endDate": end_date,
        }
        if metrics:
            params["metrics"] = ",".join(metrics)
            
        return await self._make_request(
            "GET",
            f"/stores/{store_id}/insights",
            params=params,
        )
    
    async def get_store_traffic(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
        granularity: str = "DAILY",
    ) -> Dict[str, Any]:
        """获取旗舰店流量数据
        
        Args:
            store_id: 旗舰店ID
            start_date: 开始日期
            end_date: 结束日期
            granularity: 时间粒度 (DAILY, WEEKLY, MONTHLY)
            
        Returns:
            流量数据
        """
        params = {
            "startDate": start_date,
            "endDate": end_date,
            "granularity": granularity,
        }
        return await self._make_request(
            "GET",
            f"/stores/{store_id}/traffic",
            params=params,
        )
    
    async def get_page_performance(
        self,
        store_id: str,
        page_id: str,
        start_date: str,
        end_date: str,
    ) -> Dict[str, Any]:
        """获取页面性能数据
        
        Args:
            store_id: 旗舰店ID
            page_id: 页面ID
            start_date: 开始日期
            end_date: 结束日期
            
        Returns:
            页面性能数据
        """
        params = {
            "startDate": start_date,
            "endDate": end_date,
        }
        return await self._make_request(
            "GET",
            f"/stores/{store_id}/pages/{page_id}/performance",
            params=params,
        )
    
    # ==================== 流量来源 ====================
    
    async def get_traffic_sources(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
    ) -> Dict[str, Any]:
        """获取流量来源分析
        
        Args:
            store_id: 旗舰店ID
            start_date: 开始日期
            end_date: 结束日期
            
        Returns:
            流量来源数据
        """
        params = {
            "startDate": start_date,
            "endDate": end_date,
        }
        return await self._make_request(
            "GET",
            f"/stores/{store_id}/traffic/sources",
            params=params,
        )
    
    async def get_search_terms(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
        max_results: int = 100,
    ) -> Dict[str, Any]:
        """获取搜索词分析
        
        Args:
            store_id: 旗舰店ID
            start_date: 开始日期
            end_date: 结束日期
            max_results: 最大结果数
            
        Returns:
            搜索词数据
        """
        params = {
            "startDate": start_date,
            "endDate": end_date,
            "maxResults": max_results,
        }
        return await self._make_request(
            "GET",
            f"/stores/{store_id}/searchTerms",
            params=params,
        )

