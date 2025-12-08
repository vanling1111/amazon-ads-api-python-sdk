"""
Audiences Discovery API - 受众发现 (异步版本)

端点前缀: /audiences/, /dsp/audiences/
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient, JSONData


class AudiencesDiscoveryAPI(BaseAdsClient):
    """受众发现API (全异步)"""
    
    # ==================== Discovery ====================
    
    async def fetch_taxonomy(
        self,
        *,
        parent_id: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """
        浏览受众类别分类
        
        Args:
            parent_id: 父节点ID，为空则返回根节点
            max_results: 每页数量
            next_token: 分页令牌
        """
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if parent_id:
            request_body["parentId"] = parent_id
        if next_token:
            request_body["nextToken"] = next_token
            
        result = await self.post("/audiences/taxonomy/list", json_data=request_body)
        return result if isinstance(result, dict) else {"taxonomy": []}
    
    async def list_audiences(
        self,
        *,
        audience_type: Optional[str] = None,
        category_ids: Optional[List[str]] = None,
        audience_ids: Optional[List[str]] = None,
        name_filter: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """
        根据筛选条件获取受众片段
        
        Args:
            audience_type: 受众类型
            category_ids: 类别ID列表
            audience_ids: 受众ID列表
            name_filter: 名称筛选
            max_results: 每页数量
            next_token: 分页令牌
        """
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if audience_type:
            request_body["audienceType"] = audience_type
        if category_ids:
            request_body["categoryIds"] = category_ids
        if audience_ids:
            request_body["audienceIds"] = audience_ids
        if name_filter:
            request_body["nameFilter"] = name_filter
        if next_token:
            request_body["nextToken"] = next_token
            
        result = await self.post("/audiences/list", json_data=request_body)
        return result if isinstance(result, dict) else {"audiences": []}
    
    # ==================== DSP Audiences ====================
    
    async def edit_dsp_audience(
        self,
        audiences: List[Dict[str, Any]],
    ) -> JSONData:
        """编辑DSP受众"""
        result = await self.put("/dsp/audiences/edit", json_data={"audiences": audiences})
        return result if isinstance(result, dict) else {}
    
    async def delete_dsp_audience(
        self,
        audience_ids: List[str],
    ) -> JSONData:
        """删除DSP受众"""
        result = await self.post("/dsp/audiences/delete", json_data={"audienceIds": audience_ids})
        return result if isinstance(result, dict) else {}
