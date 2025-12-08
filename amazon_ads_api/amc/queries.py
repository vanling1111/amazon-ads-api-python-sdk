"""
Amazon Marketing Cloud Queries API (异步版本)
AMC查询管理
"""

from typing import Any
from ..base import BaseAdsClient, JSONData, JSONList


class AMCQueriesAPI(BaseAdsClient):
    """AMC Queries API (全异步)"""

    # ==================== 查询管理 ====================

    async def list_queries(
        self,
        state: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取查询列表"""
        params: dict[str, Any] = {"maxResults": max_results}
        if state:
            params["state"] = state
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/amc/queries", params=params)
        return result if isinstance(result, dict) else {"queries": []}

    async def create_query(
        self,
        name: str,
        sql: str,
        description: str | None = None,
        parameters: list[dict[str, Any]] | None = None,
    ) -> JSONData:
        """创建查询"""
        data: dict[str, Any] = {
            "name": name,
            "sql": sql,
        }
        if description:
            data["description"] = description
        if parameters:
            data["parameters"] = parameters

        result = await self.post("/amc/queries", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_query(self, query_id: str) -> JSONData:
        """获取查询详情"""
        result = await self.get(f"/amc/queries/{query_id}")
        return result if isinstance(result, dict) else {}

    async def update_query(
        self,
        query_id: str,
        name: str | None = None,
        sql: str | None = None,
        description: str | None = None,
    ) -> JSONData:
        """更新查询"""
        data: dict[str, Any] = {}
        if name:
            data["name"] = name
        if sql:
            data["sql"] = sql
        if description:
            data["description"] = description

        result = await self.put(f"/amc/queries/{query_id}", json_data=data)
        return result if isinstance(result, dict) else {}

    async def delete_query(self, query_id: str) -> JSONData:
        """删除查询"""
        result = await self.delete(f"/amc/queries/{query_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 查询执行 ====================

    async def execute_query(
        self,
        query_id: str,
        parameters: dict[str, Any] | None = None,
        time_window: dict[str, str] | None = None,
    ) -> JSONData:
        """执行查询"""
        data: dict[str, Any] = {}
        if parameters:
            data["parameters"] = parameters
        if time_window:
            data["timeWindow"] = time_window

        result = await self.post(
            f"/amc/queries/{query_id}/execute", json_data=data if data else None
        )
        return result if isinstance(result, dict) else {}

    async def get_execution_status(self, execution_id: str) -> JSONData:
        """获取执行状态"""
        result = await self.get(f"/amc/executions/{execution_id}")
        return result if isinstance(result, dict) else {}

    async def get_execution_results(
        self,
        execution_id: str,
        max_results: int = 1000,
        next_token: str | None = None,
    ) -> JSONData:
        """获取执行结果"""
        params: dict[str, Any] = {"maxResults": max_results}
        if next_token:
            params["nextToken"] = next_token

        result = await self.get(f"/amc/executions/{execution_id}/results", params=params)
        return result if isinstance(result, dict) else {"results": []}

    async def cancel_execution(self, execution_id: str) -> JSONData:
        """取消执行"""
        result = await self.post(f"/amc/executions/{execution_id}/cancel")
        return result if isinstance(result, dict) else {}

    # ==================== 查询模板 ====================

    async def list_query_templates(self) -> JSONList:
        """获取查询模板列表"""
        response = await self.get("/amc/templates")
        if isinstance(response, dict):
            return response.get("templates", [])
        return []

    async def get_query_template(self, template_id: str) -> JSONData:
        """获取查询模板详情"""
        result = await self.get(f"/amc/templates/{template_id}")
        return result if isinstance(result, dict) else {}
