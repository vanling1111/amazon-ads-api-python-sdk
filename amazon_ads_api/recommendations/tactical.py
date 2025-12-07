"""
Tactical Recommendations API

官方文档: https://advertising.amazon.com/API/docs/en-us/guides/recommendations/tactical-recommendations/overview
OpenAPI: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Recommendations_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class TacticalRecommendationsAPI(BaseAdsClient):
    """Tactical Recommendations API - 战术建议
    
    获取广告优化的战术建议。
    """
    
    # ==================== 建议列表 ====================
    
    async def list_recommendations(
        self,
        recommendation_type: Optional[str] = None,
        entity_type: Optional[str] = None,
        state: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取建议列表
        
        Args:
            recommendation_type: 建议类型 (BID, BUDGET, KEYWORD, TARGET, etc.)
            entity_type: 实体类型 (CAMPAIGN, AD_GROUP, KEYWORD, etc.)
            state: 状态 (NEW, APPLIED, DISMISSED)
            max_results: 最大结果数
            next_token: 分页token
            
        Returns:
            建议列表
        """
        params = {"maxResults": max_results}
        if recommendation_type:
            params["recommendationType"] = recommendation_type
        if entity_type:
            params["entityType"] = entity_type
        if state:
            params["state"] = state
        if next_token:
            params["nextToken"] = next_token
            
        return await self._make_request(
            "GET",
            "/recommendations",
            params=params,
        )
    
    async def get_recommendation(
        self,
        recommendation_id: str,
    ) -> Dict[str, Any]:
        """获取建议详情
        
        Args:
            recommendation_id: 建议ID
            
        Returns:
            建议详情
        """
        return await self._make_request(
            "GET",
            f"/recommendations/{recommendation_id}",
        )
    
    # ==================== 建议操作 ====================
    
    async def apply_recommendation(
        self,
        recommendation_id: str,
    ) -> Dict[str, Any]:
        """应用建议
        
        Args:
            recommendation_id: 建议ID
            
        Returns:
            应用结果
        """
        return await self._make_request(
            "POST",
            f"/recommendations/{recommendation_id}/apply",
        )
    
    async def apply_recommendations_batch(
        self,
        recommendation_ids: List[str],
    ) -> Dict[str, Any]:
        """批量应用建议
        
        Args:
            recommendation_ids: 建议ID列表
            
        Returns:
            批量应用结果
        """
        data = {"recommendationIds": recommendation_ids}
        return await self._make_request(
            "POST",
            "/recommendations/apply",
            json=data,
        )
    
    async def dismiss_recommendation(
        self,
        recommendation_id: str,
        reason: Optional[str] = None,
    ) -> Dict[str, Any]:
        """拒绝建议
        
        Args:
            recommendation_id: 建议ID
            reason: 拒绝原因
            
        Returns:
            操作结果
        """
        data = {}
        if reason:
            data["reason"] = reason
            
        return await self._make_request(
            "POST",
            f"/recommendations/{recommendation_id}/dismiss",
            json=data if data else None,
        )
    
    # ==================== 建议分析 ====================
    
    async def get_recommendation_impact(
        self,
        recommendation_id: str,
    ) -> Dict[str, Any]:
        """获取建议预估影响
        
        Args:
            recommendation_id: 建议ID
            
        Returns:
            预估影响
        """
        return await self._make_request(
            "GET",
            f"/recommendations/{recommendation_id}/impact",
        )
    
    async def list_recommendation_types(self) -> List[Dict[str, Any]]:
        """获取可用建议类型
        
        Returns:
            建议类型列表
        """
        response = await self._make_request(
            "GET",
            "/recommendations/types",
        )
        return response.get("types", [])
    
    # ==================== 建议配置 ====================
    
    async def get_recommendation_settings(self) -> Dict[str, Any]:
        """获取建议配置
        
        Returns:
            当前配置
        """
        return await self._make_request(
            "GET",
            "/recommendations/settings",
        )
    
    async def update_recommendation_settings(
        self,
        enabled_types: Optional[List[str]] = None,
        auto_apply: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """更新建议配置
        
        Args:
            enabled_types: 启用的建议类型
            auto_apply: 是否自动应用
            
        Returns:
            更新后的配置
        """
        data = {}
        if enabled_types is not None:
            data["enabledTypes"] = enabled_types
        if auto_apply is not None:
            data["autoApply"] = auto_apply
            
        return await self._make_request(
            "PUT",
            "/recommendations/settings",
            json=data,
        )

