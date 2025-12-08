"""
Amazon Ads Data Provider Metadata API (异步版本)
数据提供商元数据
"""

from typing import Any
from ..base import BaseAdsClient, JSONData, JSONList


class DataProviderMetadataAPI(BaseAdsClient):
    """Data Provider Metadata API (全异步)"""

    # ==================== 数据源管理 ====================

    async def list_data_sources(self) -> JSONList:
        """获取数据源列表"""
        response = await self.get("/dataProvider/sources")
        if isinstance(response, dict):
            return response.get("sources", [])
        return []

    async def create_data_source(
        self,
        name: str,
        data_type: str,
        description: str | None = None,
        schema: dict[str, Any] | None = None,
    ) -> JSONData:
        """创建数据源"""
        data: dict[str, Any] = {
            "name": name,
            "dataType": data_type,
        }
        if description:
            data["description"] = description
        if schema:
            data["schema"] = schema

        result = await self.post("/dataProvider/sources", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_data_source(self, source_id: str) -> JSONData:
        """获取数据源详情"""
        result = await self.get(f"/dataProvider/sources/{source_id}")
        return result if isinstance(result, dict) else {}

    async def update_data_source(
        self,
        source_id: str,
        name: str | None = None,
        description: str | None = None,
        schema: dict[str, Any] | None = None,
    ) -> JSONData:
        """更新数据源"""
        data: dict[str, Any] = {}
        if name:
            data["name"] = name
        if description:
            data["description"] = description
        if schema:
            data["schema"] = schema

        result = await self.put(f"/dataProvider/sources/{source_id}", json_data=data)
        return result if isinstance(result, dict) else {}

    async def delete_data_source(self, source_id: str) -> JSONData:
        """删除数据源"""
        result = await self.delete(f"/dataProvider/sources/{source_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 数据模式管理 ====================

    async def get_schema(self, source_id: str) -> JSONData:
        """获取数据源模式"""
        result = await self.get(f"/dataProvider/sources/{source_id}/schema")
        return result if isinstance(result, dict) else {}

    async def validate_schema(self, schema: dict[str, Any]) -> JSONData:
        """验证数据模式"""
        result = await self.post("/dataProvider/schema/validate", json_data={"schema": schema})
        return result if isinstance(result, dict) else {}
