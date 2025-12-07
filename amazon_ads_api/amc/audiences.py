"""
Amazon Marketing Cloud Audiences API

官方文档: https://advertising.amazon.com/API/docs/en-us/amc/amc-audiences
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AMC_Audiences_API_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class AMCAudiencesAPI(BaseAdsClient):
    """AMC Audiences API - 受众管理
    
    管理通过AMC查询创建的自定义受众。
    """
    
    # ==================== 受众管理 ====================
    
    async def list_audiences(
        self,
        state: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取受众列表
        
        Args:
            state: 状态 (ACTIVE, PROCESSING, FAILED)
            max_results: 最大结果数
            next_token: 分页token
            
        Returns:
            受众列表
        """
        params = {"maxResults": max_results}
        if state:
            params["state"] = state
        if next_token:
            params["nextToken"] = next_token
            
        return await self._make_request(
            "GET",
            "/amc/audiences",
            params=params,
        )
    
    async def create_audience(
        self,
        name: str,
        query_id: str,
        description: Optional[str] = None,
        ttl_days: int = 365,
        destinations: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """创建受众
        
        Args:
            name: 受众名称
            query_id: 关联的查询ID
            description: 描述
            ttl_days: 数据保留天数
            destinations: 目标广告产品列表 (SP, SB, SD, DSP)
            
        Returns:
            创建的受众
        """
        data = {
            "name": name,
            "queryId": query_id,
            "ttlDays": ttl_days,
        }
        if description:
            data["description"] = description
        if destinations:
            data["destinations"] = destinations
            
        return await self._make_request(
            "POST",
            "/amc/audiences",
            json=data,
        )
    
    async def get_audience(
        self,
        audience_id: str,
    ) -> Dict[str, Any]:
        """获取受众详情
        
        Args:
            audience_id: 受众ID
            
        Returns:
            受众详情
        """
        return await self._make_request(
            "GET",
            f"/amc/audiences/{audience_id}",
        )
    
    async def update_audience(
        self,
        audience_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        ttl_days: Optional[int] = None,
    ) -> Dict[str, Any]:
        """更新受众
        
        Args:
            audience_id: 受众ID
            name: 受众名称
            description: 描述
            ttl_days: 数据保留天数
            
        Returns:
            更新后的受众
        """
        data = {}
        if name:
            data["name"] = name
        if description:
            data["description"] = description
        if ttl_days:
            data["ttlDays"] = ttl_days
            
        return await self._make_request(
            "PUT",
            f"/amc/audiences/{audience_id}",
            json=data,
        )
    
    async def delete_audience(
        self,
        audience_id: str,
    ) -> None:
        """删除受众
        
        Args:
            audience_id: 受众ID
        """
        await self._make_request(
            "DELETE",
            f"/amc/audiences/{audience_id}",
        )
    
    # ==================== 受众刷新 ====================
    
    async def refresh_audience(
        self,
        audience_id: str,
    ) -> Dict[str, Any]:
        """刷新受众数据
        
        Args:
            audience_id: 受众ID
            
        Returns:
            刷新任务信息
        """
        return await self._make_request(
            "POST",
            f"/amc/audiences/{audience_id}/refresh",
        )
    
    async def get_refresh_status(
        self,
        audience_id: str,
        refresh_id: str,
    ) -> Dict[str, Any]:
        """获取刷新状态
        
        Args:
            audience_id: 受众ID
            refresh_id: 刷新任务ID
            
        Returns:
            刷新状态
        """
        return await self._make_request(
            "GET",
            f"/amc/audiences/{audience_id}/refreshes/{refresh_id}",
        )
    
    # ==================== 受众分析 ====================
    
    async def get_audience_size(
        self,
        audience_id: str,
    ) -> Dict[str, Any]:
        """获取受众规模
        
        Args:
            audience_id: 受众ID
            
        Returns:
            受众规模信息
        """
        return await self._make_request(
            "GET",
            f"/amc/audiences/{audience_id}/size",
        )
    
    async def get_audience_overlap(
        self,
        audience_ids: List[str],
    ) -> Dict[str, Any]:
        """获取受众重叠分析
        
        Args:
            audience_ids: 受众ID列表
            
        Returns:
            重叠分析结果
        """
        params = {"audienceIds": ",".join(audience_ids)}
        return await self._make_request(
            "GET",
            "/amc/audiences/overlap",
            params=params,
        )
    
    # ==================== 目标配置 ====================
    
    async def add_destination(
        self,
        audience_id: str,
        destination: str,
    ) -> Dict[str, Any]:
        """添加投放目标
        
        Args:
            audience_id: 受众ID
            destination: 目标广告产品 (SP, SB, SD, DSP)
            
        Returns:
            操作结果
        """
        data = {"destination": destination}
        return await self._make_request(
            "POST",
            f"/amc/audiences/{audience_id}/destinations",
            json=data,
        )
    
    async def remove_destination(
        self,
        audience_id: str,
        destination: str,
    ) -> None:
        """移除投放目标
        
        Args:
            audience_id: 受众ID
            destination: 目标广告产品
        """
        await self._make_request(
            "DELETE",
            f"/amc/audiences/{audience_id}/destinations/{destination}",
        )

