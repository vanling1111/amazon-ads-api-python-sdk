"""
Tactical Recommendations API (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/guides/recommendations/tactical-recommendations/overview
OpenAPI: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Recommendations_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class TacticalRecommendationsAPI(BaseAdsClient):
    """Tactical Recommendations API - 战术建议 (全异步)
    
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
            recommendation_type: 建议类型 (BID, BUDGET, KEYWORD, TARGET, NEGATIVE_KEYWORD, etc.)
            entity_type: 实体类型 (CAMPAIGN, AD_GROUP, KEYWORD, etc.)
            state: 状态 (NEW, APPLIED, DISMISSED)
            max_results: 最大结果数
            next_token: 分页token
            
        Returns:
            建议列表
        """
        params: Dict[str, Any] = {"maxResults": max_results}
        if recommendation_type:
            params["recommendationType"] = recommendation_type
        if entity_type:
            params["entityType"] = entity_type
        if state:
            params["state"] = state
        if next_token:
            params["nextToken"] = next_token
            
        result = await self.get("/recommendations", params=params)
        return result if isinstance(result, dict) else {"recommendations": []}
    
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
        result = await self.get(f"/recommendations/{recommendation_id}")
        return result if isinstance(result, dict) else {}
    
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
        result = await self.post(f"/recommendations/{recommendation_id}/apply")
        return result if isinstance(result, dict) else {}
    
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
        result = await self.post("/recommendations/apply", json_data=data)
        return result if isinstance(result, dict) else {"success": [], "error": []}
    
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
        data: Dict[str, Any] = {}
        if reason:
            data["reason"] = reason
            
        result = await self.post(
            f"/recommendations/{recommendation_id}/dismiss",
            json_data=data if data else None,
        )
        return result if isinstance(result, dict) else {}
    
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
        result = await self.get(f"/recommendations/{recommendation_id}/impact")
        return result if isinstance(result, dict) else {}
    
    async def list_recommendation_types(self) -> List[Dict[str, Any]]:
        """获取可用建议类型
        
        Returns:
            建议类型列表
        """
        result = await self.get("/recommendations/types")
        if isinstance(result, dict):
            return result.get("types", [])
        return result if isinstance(result, list) else []
    
    # ==================== 建议配置 ====================
    
    async def get_recommendation_settings(self) -> Dict[str, Any]:
        """获取建议配置
        
        Returns:
            当前配置
        """
        result = await self.get("/recommendations/settings")
        return result if isinstance(result, dict) else {}
    
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
        data: Dict[str, Any] = {}
        if enabled_types is not None:
            data["enabledTypes"] = enabled_types
        if auto_apply is not None:
            data["autoApply"] = auto_apply
            
        result = await self.put("/recommendations/settings", json_data=data)
        return result if isinstance(result, dict) else {}
    
    # ==================== 批量获取 ====================
    
    async def list_all_recommendations(
        self,
        recommendation_type: Optional[str] = None,
        entity_type: Optional[str] = None,
        state: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """获取所有建议（自动分页）
        
        Args:
            recommendation_type: 建议类型
            entity_type: 实体类型
            state: 状态
            
        Returns:
            所有建议列表
        """
        all_recommendations = []
        next_token = None
        
        while True:
            result = await self.list_recommendations(
                recommendation_type=recommendation_type,
                entity_type=entity_type,
                state=state,
                max_results=100,
                next_token=next_token,
            )
            recommendations = result.get("recommendations", [])
            all_recommendations.extend(recommendations)
            
            next_token = result.get("nextToken")
            if not next_token:
                break
        
        return all_recommendations
