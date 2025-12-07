"""
Unified Moderation API

官方文档: https://advertising.amazon.com/API/docs/en-us/moderation
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Moderation_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class UnifiedModerationAPI(BaseAdsClient):
    """Unified Moderation API - 统一审核
    
    获取广告审核状态和结果。
    """
    
    # ==================== 审核状态 ====================
    
    async def get_moderation_status(
        self,
        entity_type: str,
        entity_id: str,
    ) -> Dict[str, Any]:
        """获取审核状态
        
        Args:
            entity_type: 实体类型 (AD, CREATIVE, CAMPAIGN)
            entity_id: 实体ID
            
        Returns:
            审核状态
        """
        params = {
            "entityType": entity_type,
            "entityId": entity_id,
        }
        return await self._make_request(
            "GET",
            "/moderation/status",
            params=params,
        )
    
    async def list_moderation_results(
        self,
        entity_type: Optional[str] = None,
        status: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取审核结果列表
        
        Args:
            entity_type: 实体类型
            status: 审核状态 (APPROVED, REJECTED, PENDING)
            start_date: 开始日期
            end_date: 结束日期
            max_results: 最大结果数
            next_token: 分页token
            
        Returns:
            审核结果列表
        """
        params = {"maxResults": max_results}
        if entity_type:
            params["entityType"] = entity_type
        if status:
            params["status"] = status
        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date
        if next_token:
            params["nextToken"] = next_token
            
        return await self._make_request(
            "GET",
            "/moderation/results",
            params=params,
        )
    
    # ==================== 审核详情 ====================
    
    async def get_rejection_reasons(
        self,
        entity_type: str,
        entity_id: str,
    ) -> List[Dict[str, Any]]:
        """获取拒绝原因
        
        Args:
            entity_type: 实体类型
            entity_id: 实体ID
            
        Returns:
            拒绝原因列表
        """
        params = {
            "entityType": entity_type,
            "entityId": entity_id,
        }
        response = await self._make_request(
            "GET",
            "/moderation/rejections",
            params=params,
        )
        return response.get("reasons", [])
    
    # ==================== 申诉 ====================
    
    async def submit_appeal(
        self,
        entity_type: str,
        entity_id: str,
        appeal_reason: str,
        supporting_documents: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """提交申诉
        
        Args:
            entity_type: 实体类型
            entity_id: 实体ID
            appeal_reason: 申诉原因
            supporting_documents: 支持文档URL列表
            
        Returns:
            申诉结果
        """
        data = {
            "entityType": entity_type,
            "entityId": entity_id,
            "appealReason": appeal_reason,
        }
        if supporting_documents:
            data["supportingDocuments"] = supporting_documents
            
        return await self._make_request(
            "POST",
            "/moderation/appeals",
            json=data,
        )
    
    async def get_appeal_status(
        self,
        appeal_id: str,
    ) -> Dict[str, Any]:
        """获取申诉状态
        
        Args:
            appeal_id: 申诉ID
            
        Returns:
            申诉状态
        """
        return await self._make_request(
            "GET",
            f"/moderation/appeals/{appeal_id}",
        )

