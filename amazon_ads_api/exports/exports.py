"""
Amazon Ads Exports API (异步版本)
数据导出
"""

from typing import Any
from ..base import BaseAdsClient, JSONData, JSONList


class ExportsAPI(BaseAdsClient):
    """Exports API (全异步)"""

    # ==================== 导出任务 ====================

    async def create_export(
        self,
        export_type: str,
        ad_product: str,
        filters: dict[str, Any] | None = None,
        columns: list[str] | None = None,
    ) -> JSONData:
        """创建导出任务"""
        data: dict[str, Any] = {
            "exportType": export_type,
            "adProduct": ad_product,
        }
        if filters:
            data["filters"] = filters
        if columns:
            data["columns"] = columns

        result = await self.post("/exports", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_export(self, export_id: str) -> JSONData:
        """获取导出任务状态"""
        result = await self.get(f"/exports/{export_id}")
        return result if isinstance(result, dict) else {}

    async def download_export(self, export_id: str) -> JSONData:
        """下载导出文件"""
        result = await self.get(f"/exports/{export_id}/download")
        return result if isinstance(result, dict) else {}

    async def list_exports(
        self,
        status: str | None = None,
        export_type: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取导出任务列表"""
        params: dict[str, Any] = {"maxResults": max_results}
        if status:
            params["status"] = status
        if export_type:
            params["exportType"] = export_type
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/exports", params=params)
        return result if isinstance(result, dict) else {"exports": []}

    # ==================== 导出配置 ====================

    async def list_export_types(self, ad_product: str) -> JSONList:
        """获取可用导出类型"""
        params = {"adProduct": ad_product}
        response = await self.get("/exports/types", params=params)
        if isinstance(response, dict):
            return response.get("types", [])
        return []

    async def get_export_schema(
        self,
        export_type: str,
        ad_product: str,
    ) -> JSONData:
        """获取导出数据模式"""
        params = {
            "exportType": export_type,
            "adProduct": ad_product,
        }
        result = await self.get("/exports/schema", params=params)
        return result if isinstance(result, dict) else {}

    # ==================== 定时导出 ====================

    async def create_scheduled_export(
        self,
        export_type: str,
        ad_product: str,
        schedule: str,
        destination: dict[str, Any],
        filters: dict[str, Any] | None = None,
    ) -> JSONData:
        """创建定时导出"""
        data: dict[str, Any] = {
            "exportType": export_type,
            "adProduct": ad_product,
            "schedule": schedule,
            "destination": destination,
        }
        if filters:
            data["filters"] = filters

        result = await self.post("/exports/scheduled", json_data=data)
        return result if isinstance(result, dict) else {}

    async def list_scheduled_exports(self) -> JSONList:
        """获取定时导出列表"""
        response = await self.get("/exports/scheduled")
        if isinstance(response, dict):
            return response.get("scheduledExports", [])
        return []

    async def delete_scheduled_export(self, scheduled_export_id: str) -> JSONData:
        """删除定时导出"""
        result = await self.delete(f"/exports/scheduled/{scheduled_export_id}")
        return result if isinstance(result, dict) else {}
