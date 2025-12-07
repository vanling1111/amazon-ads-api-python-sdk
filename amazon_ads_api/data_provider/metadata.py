"""
Data Provider Metadata API

官方文档: https://advertising.amazon.com/API/docs/en-us/data-provider
OpenAPI: https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/data-provider/openapi.yaml
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class DataProviderMetadataAPI(BaseAdsClient):
    """Data Provider Metadata API - 数据提供商元数据
    
    管理数据提供商的元数据配置。
    """
    
    # ==================== 数据源管理 ====================
    
    async def list_data_sources(self) -> List[Dict[str, Any]]:
        """获取数据源列表
        
        Returns:
            数据源列表
        """
        response = await self._make_request(
            "GET",
            "/dataProvider/sources",
        )
        return response.get("sources", [])
    
    async def create_data_source(
        self,
        name: str,
        data_type: str,
        description: Optional[str] = None,
        schema: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """创建数据源
        
        Args:
            name: 数据源名称
            data_type: 数据类型 (AUDIENCE, CONVERSION, etc.)
            description: 描述
            schema: 数据模式
            
        Returns:
            创建的数据源
        """
        data = {
            "name": name,
            "dataType": data_type,
        }
        if description:
            data["description"] = description
        if schema:
            data["schema"] = schema
            
        return await self._make_request(
            "POST",
            "/dataProvider/sources",
            json=data,
        )
    
    async def get_data_source(
        self,
        source_id: str,
    ) -> Dict[str, Any]:
        """获取数据源详情
        
        Args:
            source_id: 数据源ID
            
        Returns:
            数据源详情
        """
        return await self._make_request(
            "GET",
            f"/dataProvider/sources/{source_id}",
        )
    
    async def update_data_source(
        self,
        source_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        schema: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """更新数据源
        
        Args:
            source_id: 数据源ID
            name: 数据源名称
            description: 描述
            schema: 数据模式
            
        Returns:
            更新后的数据源
        """
        data = {}
        if name:
            data["name"] = name
        if description:
            data["description"] = description
        if schema:
            data["schema"] = schema
            
        return await self._make_request(
            "PUT",
            f"/dataProvider/sources/{source_id}",
            json=data,
        )
    
    async def delete_data_source(
        self,
        source_id: str,
    ) -> None:
        """删除数据源
        
        Args:
            source_id: 数据源ID
        """
        await self._make_request(
            "DELETE",
            f"/dataProvider/sources/{source_id}",
        )
    
    # ==================== 数据模式管理 ====================
    
    async def get_schema(
        self,
        source_id: str,
    ) -> Dict[str, Any]:
        """获取数据源模式
        
        Args:
            source_id: 数据源ID
            
        Returns:
            数据模式
        """
        return await self._make_request(
            "GET",
            f"/dataProvider/sources/{source_id}/schema",
        )
    
    async def validate_schema(
        self,
        schema: Dict[str, Any],
    ) -> Dict[str, Any]:
        """验证数据模式
        
        Args:
            schema: 待验证的数据模式
            
        Returns:
            验证结果
        """
        return await self._make_request(
            "POST",
            "/dataProvider/schema/validate",
            json={"schema": schema},
        )

