"""
Amazon Marketing Cloud Workflows API (异步版本)
AMC工作流管理
"""

from typing import Any
from ..base import BaseAdsClient, JSONData, JSONList


class AMCWorkflowsAPI(BaseAdsClient):
    """AMC Workflows API (全异步)"""

    # ==================== 工作流管理 ====================

    async def list_workflows(
        self,
        state: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取工作流列表"""
        params: dict[str, Any] = {"maxResults": max_results}
        if state:
            params["state"] = state
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/amc/workflows", params=params)
        return result if isinstance(result, dict) else {"workflows": []}

    async def create_workflow(
        self,
        name: str,
        query_id: str,
        schedule: str,
        description: str | None = None,
        output_config: dict[str, Any] | None = None,
    ) -> JSONData:
        """创建工作流"""
        data: dict[str, Any] = {
            "name": name,
            "queryId": query_id,
            "schedule": schedule,
        }
        if description:
            data["description"] = description
        if output_config:
            data["outputConfig"] = output_config

        result = await self.post("/amc/workflows", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_workflow(self, workflow_id: str) -> JSONData:
        """获取工作流详情"""
        result = await self.get(f"/amc/workflows/{workflow_id}")
        return result if isinstance(result, dict) else {}

    async def update_workflow(
        self,
        workflow_id: str,
        name: str | None = None,
        schedule: str | None = None,
        description: str | None = None,
        state: str | None = None,
    ) -> JSONData:
        """更新工作流"""
        data: dict[str, Any] = {}
        if name:
            data["name"] = name
        if schedule:
            data["schedule"] = schedule
        if description:
            data["description"] = description
        if state:
            data["state"] = state

        result = await self.put(f"/amc/workflows/{workflow_id}", json_data=data)
        return result if isinstance(result, dict) else {}

    async def delete_workflow(self, workflow_id: str) -> JSONData:
        """删除工作流"""
        result = await self.delete(f"/amc/workflows/{workflow_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 工作流执行 ====================

    async def trigger_workflow(
        self,
        workflow_id: str,
        parameters: dict[str, Any] | None = None,
    ) -> JSONData:
        """手动触发工作流"""
        result = await self.post(
            f"/amc/workflows/{workflow_id}/trigger",
            json_data=parameters if parameters else None,
        )
        return result if isinstance(result, dict) else {}

    async def list_workflow_executions(
        self,
        workflow_id: str,
        status: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取工作流执行历史"""
        params: dict[str, Any] = {"maxResults": max_results}
        if status:
            params["status"] = status
        if next_token:
            params["nextToken"] = next_token

        result = await self.get(f"/amc/workflows/{workflow_id}/executions", params=params)
        return result if isinstance(result, dict) else {"executions": []}

    async def get_workflow_execution(
        self,
        workflow_id: str,
        execution_id: str,
    ) -> JSONData:
        """获取工作流执行详情"""
        result = await self.get(f"/amc/workflows/{workflow_id}/executions/{execution_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 输出管理 ====================

    async def list_workflow_outputs(
        self,
        workflow_id: str,
        execution_id: str,
    ) -> JSONList:
        """获取工作流输出列表"""
        response = await self.get(
            f"/amc/workflows/{workflow_id}/executions/{execution_id}/outputs"
        )
        if isinstance(response, dict):
            return response.get("outputs", [])
        return []

    async def download_workflow_output(
        self,
        workflow_id: str,
        execution_id: str,
        output_id: str,
    ) -> JSONData:
        """下载工作流输出"""
        result = await self.get(
            f"/amc/workflows/{workflow_id}/executions/{execution_id}/outputs/{output_id}/download"
        )
        return result if isinstance(result, dict) else {}
