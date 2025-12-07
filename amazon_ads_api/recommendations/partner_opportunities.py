"""
Partner Opportunities API

官方文档: https://advertising.amazon.com/API/docs/en-us/guides/recommendations/partner-opportunities/overview
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/PartnerOpportunities_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class PartnerOpportunitiesAPI(BaseAdsClient):
    """Partner Opportunities API - 合作机会
    
    获取和管理广告合作机会建议。
    """
    
    # ==================== 机会发现 ====================
    
    async def list_opportunities(
        self,
        opportunity_type: Optional[str] = None,
        state: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取合作机会列表
        
        Args:
            opportunity_type: 机会类型 (CAMPAIGN_EXPANSION, NEW_PRODUCT, etc.)
            state: 状态 (NEW, VIEWED, ACCEPTED, DISMISSED)
            max_results: 最大结果数
            next_token: 分页token
            
        Returns:
            机会列表
        """
        params = {"maxResults": max_results}
        if opportunity_type:
            params["opportunityType"] = opportunity_type
        if state:
            params["state"] = state
        if next_token:
            params["nextToken"] = next_token
            
        return await self._make_request(
            "GET",
            "/opportunities",
            params=params,
        )
    
    async def get_opportunity(
        self,
        opportunity_id: str,
    ) -> Dict[str, Any]:
        """获取机会详情
        
        Args:
            opportunity_id: 机会ID
            
        Returns:
            机会详情
        """
        return await self._make_request(
            "GET",
            f"/opportunities/{opportunity_id}",
        )
    
    # ==================== 机会操作 ====================
    
    async def accept_opportunity(
        self,
        opportunity_id: str,
        config: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """接受合作机会
        
        Args:
            opportunity_id: 机会ID
            config: 执行配置（可选）
            
        Returns:
            操作结果
        """
        data = {}
        if config:
            data["config"] = config
            
        return await self._make_request(
            "POST",
            f"/opportunities/{opportunity_id}/accept",
            json=data if data else None,
        )
    
    async def dismiss_opportunity(
        self,
        opportunity_id: str,
        reason: Optional[str] = None,
    ) -> Dict[str, Any]:
        """拒绝合作机会
        
        Args:
            opportunity_id: 机会ID
            reason: 拒绝原因（可选）
            
        Returns:
            操作结果
        """
        data = {}
        if reason:
            data["reason"] = reason
            
        return await self._make_request(
            "POST",
            f"/opportunities/{opportunity_id}/dismiss",
            json=data if data else None,
        )
    
    async def mark_opportunity_viewed(
        self,
        opportunity_id: str,
    ) -> Dict[str, Any]:
        """标记机会为已查看
        
        Args:
            opportunity_id: 机会ID
            
        Returns:
            操作结果
        """
        return await self._make_request(
            "POST",
            f"/opportunities/{opportunity_id}/view",
        )
    
    # ==================== 机会分析 ====================
    
    async def get_opportunity_impact(
        self,
        opportunity_id: str,
    ) -> Dict[str, Any]:
        """获取机会预估影响
        
        Args:
            opportunity_id: 机会ID
            
        Returns:
            预估影响数据
        """
        return await self._make_request(
            "GET",
            f"/opportunities/{opportunity_id}/impact",
        )
    
    async def list_opportunity_types(self) -> List[Dict[str, Any]]:
        """获取可用机会类型列表
        
        Returns:
            机会类型列表
        """
        response = await self._make_request(
            "GET",
            "/opportunities/types",
        )
        return response.get("types", [])

