"""
Exports API

官方文档: https://advertising.amazon.com/API/docs/en-us/guides/exports/overview
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIExports_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class ExportsAPI(BaseAdsClient):
    """Exports API - 数据导出
    
    导出广告活动管理数据。
    """
    
    # ==================== 导出任务 ====================
    
    async def create_export(
        self,
        export_type: str,
        ad_product: str,
        filters: Optional[Dict[str, Any]] = None,
        columns: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """创建导出任务
        
        Args:
            export_type: 导出类型 (CAMPAIGNS, AD_GROUPS, ADS, KEYWORDS, TARGETS, etc.)
            ad_product: 广告产品 (SP, SB, SD)
            filters: 过滤条件
            columns: 导出列
            
        Returns:
            导出任务信息
        """
        data = {
            "exportType": export_type,
            "adProduct": ad_product,
        }
        if filters:
            data["filters"] = filters
        if columns:
            data["columns"] = columns
            
        return await self._make_request(
            "POST",
            "/exports",
            json=data,
        )
    
    async def get_export(
        self,
        export_id: str,
    ) -> Dict[str, Any]:
        """获取导出任务状态
        
        Args:
            export_id: 导出任务ID
            
        Returns:
            导出任务状态
        """
        return await self._make_request(
            "GET",
            f"/exports/{export_id}",
        )
    
    async def download_export(
        self,
        export_id: str,
    ) -> bytes:
        """下载导出文件
        
        Args:
            export_id: 导出任务ID
            
        Returns:
            导出文件内容
        """
        return await self._make_request(
            "GET",
            f"/exports/{export_id}/download",
        )
    
    async def list_exports(
        self,
        status: Optional[str] = None,
        export_type: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取导出任务列表
        
        Args:
            status: 状态 (PENDING, PROCESSING, COMPLETED, FAILED)
            export_type: 导出类型
            max_results: 最大结果数
            next_token: 分页token
            
        Returns:
            导出任务列表
        """
        params = {"maxResults": max_results}
        if status:
            params["status"] = status
        if export_type:
            params["exportType"] = export_type
        if next_token:
            params["nextToken"] = next_token
            
        return await self._make_request(
            "GET",
            "/exports",
            params=params,
        )
    
    # ==================== 导出配置 ====================
    
    async def list_export_types(
        self,
        ad_product: str,
    ) -> List[Dict[str, Any]]:
        """获取可用导出类型
        
        Args:
            ad_product: 广告产品 (SP, SB, SD)
            
        Returns:
            导出类型列表
        """
        params = {"adProduct": ad_product}
        response = await self._make_request(
            "GET",
            "/exports/types",
            params=params,
        )
        return response.get("types", [])
    
    async def get_export_schema(
        self,
        export_type: str,
        ad_product: str,
    ) -> Dict[str, Any]:
        """获取导出数据模式
        
        Args:
            export_type: 导出类型
            ad_product: 广告产品
            
        Returns:
            数据模式
        """
        params = {
            "exportType": export_type,
            "adProduct": ad_product,
        }
        return await self._make_request(
            "GET",
            "/exports/schema",
            params=params,
        )
    
    # ==================== 定时导出 ====================
    
    async def create_scheduled_export(
        self,
        export_type: str,
        ad_product: str,
        schedule: str,
        destination: Dict[str, Any],
        filters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """创建定时导出
        
        Args:
            export_type: 导出类型
            ad_product: 广告产品
            schedule: 调度表达式（cron格式）
            destination: 目标配置 (S3 bucket等)
            filters: 过滤条件
            
        Returns:
            定时导出配置
        """
        data = {
            "exportType": export_type,
            "adProduct": ad_product,
            "schedule": schedule,
            "destination": destination,
        }
        if filters:
            data["filters"] = filters
            
        return await self._make_request(
            "POST",
            "/exports/scheduled",
            json=data,
        )
    
    async def list_scheduled_exports(self) -> List[Dict[str, Any]]:
        """获取定时导出列表
        
        Returns:
            定时导出列表
        """
        response = await self._make_request(
            "GET",
            "/exports/scheduled",
        )
        return response.get("scheduledExports", [])
    
    async def delete_scheduled_export(
        self,
        scheduled_export_id: str,
    ) -> None:
        """删除定时导出
        
        Args:
            scheduled_export_id: 定时导出ID
        """
        await self._make_request(
            "DELETE",
            f"/exports/scheduled/{scheduled_export_id}",
        )

