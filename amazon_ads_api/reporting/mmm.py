"""
Amazon Ads Marketing Mix Modeling (MMM) API

官方文档: https://advertising.amazon.com/API/docs/en-us/guides/reporting/marketing-mix-modeling/overview
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/MarketingMixModeling_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class MarketingMixModelingAPI(BaseAdsClient):
    """Marketing Mix Modeling API - 营销组合建模
    
    获取用于营销组合建模的数据馈送。
    """
    
    # ==================== 数据馈送 ====================
    
    async def list_data_feeds(self) -> List[Dict[str, Any]]:
        """获取可用的MMM数据馈送列表
        
        Returns:
            数据馈送列表
        """
        response = await self._make_request(
            "GET",
            "/mmm/feeds",
        )
        return response.get("feeds", [])
    
    async def create_data_feed(
        self,
        name: str,
        start_date: str,
        end_date: str,
        granularity: str = "DAILY",
        dimensions: Optional[List[str]] = None,
        metrics: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """创建MMM数据馈送请求
        
        Args:
            name: 馈送名称
            start_date: 开始日期 (YYYY-MM-DD)
            end_date: 结束日期 (YYYY-MM-DD)
            granularity: 时间粒度 (DAILY, WEEKLY)
            dimensions: 维度列表
            metrics: 指标列表
            
        Returns:
            创建的数据馈送
        """
        data = {
            "name": name,
            "startDate": start_date,
            "endDate": end_date,
            "granularity": granularity,
        }
        if dimensions:
            data["dimensions"] = dimensions
        if metrics:
            data["metrics"] = metrics
            
        return await self._make_request(
            "POST",
            "/mmm/feeds",
            json=data,
        )
    
    async def get_data_feed(
        self,
        feed_id: str,
    ) -> Dict[str, Any]:
        """获取数据馈送状态
        
        Args:
            feed_id: 馈送ID
            
        Returns:
            馈送详情
        """
        return await self._make_request(
            "GET",
            f"/mmm/feeds/{feed_id}",
        )
    
    async def download_data_feed(
        self,
        feed_id: str,
    ) -> bytes:
        """下载数据馈送文件
        
        Args:
            feed_id: 馈送ID
            
        Returns:
            文件内容
        """
        return await self._make_request(
            "GET",
            f"/mmm/feeds/{feed_id}/download",
        )
    
    # ==================== 数据规范 ====================
    
    async def get_available_dimensions(self) -> List[Dict[str, Any]]:
        """获取可用维度列表
        
        Returns:
            维度列表
        """
        response = await self._make_request(
            "GET",
            "/mmm/dimensions",
        )
        return response.get("dimensions", [])
    
    async def get_available_metrics(self) -> List[Dict[str, Any]]:
        """获取可用指标列表
        
        Returns:
            指标列表
        """
        response = await self._make_request(
            "GET",
            "/mmm/metrics",
        )
        return response.get("metrics", [])
    
    # ==================== 数据验证 ====================
    
    async def validate_feed_request(
        self,
        start_date: str,
        end_date: str,
        dimensions: List[str],
        metrics: List[str],
    ) -> Dict[str, Any]:
        """验证数据馈送请求
        
        Args:
            start_date: 开始日期
            end_date: 结束日期
            dimensions: 维度列表
            metrics: 指标列表
            
        Returns:
            验证结果
        """
        data = {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": dimensions,
            "metrics": metrics,
        }
        return await self._make_request(
            "POST",
            "/mmm/feeds/validate",
            json=data,
        )

