"""
Persona Builder API

官方文档: https://advertising.amazon.com/API/docs/en-us/guides/recommendations
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/PersonaBuilderAPI_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class PersonaBuilderAPI(BaseAdsClient):
    """Persona Builder API - 人群画像构建
    
    构建和管理目标受众人群画像。
    """
    
    # ==================== 人群画像管理 ====================
    
    async def list_personas(
        self,
        state: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取人群画像列表
        
        Args:
            state: 状态 (ACTIVE, DRAFT, ARCHIVED)
            max_results: 最大结果数
            next_token: 分页token
            
        Returns:
            画像列表
        """
        params = {"maxResults": max_results}
        if state:
            params["state"] = state
        if next_token:
            params["nextToken"] = next_token
            
        return await self._make_request(
            "GET",
            "/personas",
            params=params,
        )
    
    async def create_persona(
        self,
        name: str,
        description: Optional[str] = None,
        demographics: Optional[Dict[str, Any]] = None,
        interests: Optional[List[str]] = None,
        behaviors: Optional[List[str]] = None,
        purchase_history: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """创建人群画像
        
        Args:
            name: 画像名称
            description: 画像描述
            demographics: 人口统计特征
            interests: 兴趣标签
            behaviors: 行为标签
            purchase_history: 购买历史特征
            
        Returns:
            创建的画像
        """
        data = {"name": name}
        if description:
            data["description"] = description
        if demographics:
            data["demographics"] = demographics
        if interests:
            data["interests"] = interests
        if behaviors:
            data["behaviors"] = behaviors
        if purchase_history:
            data["purchaseHistory"] = purchase_history
            
        return await self._make_request(
            "POST",
            "/personas",
            json=data,
        )
    
    async def get_persona(
        self,
        persona_id: str,
    ) -> Dict[str, Any]:
        """获取画像详情
        
        Args:
            persona_id: 画像ID
            
        Returns:
            画像详情
        """
        return await self._make_request(
            "GET",
            f"/personas/{persona_id}",
        )
    
    async def update_persona(
        self,
        persona_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        demographics: Optional[Dict[str, Any]] = None,
        interests: Optional[List[str]] = None,
        behaviors: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """更新人群画像
        
        Args:
            persona_id: 画像ID
            name: 画像名称
            description: 画像描述
            demographics: 人口统计特征
            interests: 兴趣标签
            behaviors: 行为标签
            
        Returns:
            更新后的画像
        """
        data = {}
        if name:
            data["name"] = name
        if description:
            data["description"] = description
        if demographics:
            data["demographics"] = demographics
        if interests:
            data["interests"] = interests
        if behaviors:
            data["behaviors"] = behaviors
            
        return await self._make_request(
            "PUT",
            f"/personas/{persona_id}",
            json=data,
        )
    
    async def delete_persona(
        self,
        persona_id: str,
    ) -> None:
        """删除人群画像
        
        Args:
            persona_id: 画像ID
        """
        await self._make_request(
            "DELETE",
            f"/personas/{persona_id}",
        )
    
    # ==================== 画像分析 ====================
    
    async def get_persona_size(
        self,
        persona_id: str,
    ) -> Dict[str, Any]:
        """获取画像人群规模
        
        Args:
            persona_id: 画像ID
            
        Returns:
            人群规模估算
        """
        return await self._make_request(
            "GET",
            f"/personas/{persona_id}/size",
        )
    
    async def get_persona_insights(
        self,
        persona_id: str,
    ) -> Dict[str, Any]:
        """获取画像洞察
        
        Args:
            persona_id: 画像ID
            
        Returns:
            画像洞察数据
        """
        return await self._make_request(
            "GET",
            f"/personas/{persona_id}/insights",
        )
    
    async def compare_personas(
        self,
        persona_ids: List[str],
    ) -> Dict[str, Any]:
        """比较多个画像
        
        Args:
            persona_ids: 画像ID列表
            
        Returns:
            比较结果
        """
        params = {"personaIds": ",".join(persona_ids)}
        return await self._make_request(
            "GET",
            "/personas/compare",
            params=params,
        )
    
    # ==================== 画像属性 ====================
    
    async def list_available_demographics(self) -> List[Dict[str, Any]]:
        """获取可用人口统计属性
        
        Returns:
            人口统计属性列表
        """
        response = await self._make_request(
            "GET",
            "/personas/demographics",
        )
        return response.get("demographics", [])
    
    async def list_available_interests(self) -> List[Dict[str, Any]]:
        """获取可用兴趣标签
        
        Returns:
            兴趣标签列表
        """
        response = await self._make_request(
            "GET",
            "/personas/interests",
        )
        return response.get("interests", [])
    
    async def list_available_behaviors(self) -> List[Dict[str, Any]]:
        """获取可用行为标签
        
        Returns:
            行为标签列表
        """
        response = await self._make_request(
            "GET",
            "/personas/behaviors",
        )
        return response.get("behaviors", [])

