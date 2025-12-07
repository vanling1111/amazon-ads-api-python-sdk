"""
Amazon Marketing Cloud Workflows API

官方文档: https://advertising.amazon.com/API/docs/en-us/amc/amc-workflows
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AMC_Workflow_API_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class AMCWorkflowsAPI(BaseAdsClient):
    """AMC Workflows API - 工作流管理
    
    管理AMC自动化工作流。
    """
    
    # ==================== 工作流管理 ====================
    
    async def list_workflows(
        self,
        state: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取工作流列表
        
        Args:
            state: 状态 (ACTIVE, PAUSED, DELETED)
            max_results: 最大结果数
            next_token: 分页token
            
        Returns:
            工作流列表
        """
        params = {"maxResults": max_results}
        if state:
            params["state"] = state
        if next_token:
            params["nextToken"] = next_token
            
        return await self._make_request(
            "GET",
            "/amc/workflows",
            params=params,
        )
    
    async def create_workflow(
        self,
        name: str,
        query_id: str,
        schedule: str,
        description: Optional[str] = None,
        output_config: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """创建工作流
        
        Args:
            name: 工作流名称
            query_id: 关联的查询ID
            schedule: 调度表达式（cron格式）
            description: 描述
            output_config: 输出配置
            
        Returns:
            创建的工作流
        """
        data = {
            "name": name,
            "queryId": query_id,
            "schedule": schedule,
        }
        if description:
            data["description"] = description
        if output_config:
            data["outputConfig"] = output_config
            
        return await self._make_request(
            "POST",
            "/amc/workflows",
            json=data,
        )
    
    async def get_workflow(
        self,
        workflow_id: str,
    ) -> Dict[str, Any]:
        """获取工作流详情
        
        Args:
            workflow_id: 工作流ID
            
        Returns:
            工作流详情
        """
        return await self._make_request(
            "GET",
            f"/amc/workflows/{workflow_id}",
        )
    
    async def update_workflow(
        self,
        workflow_id: str,
        name: Optional[str] = None,
        schedule: Optional[str] = None,
        description: Optional[str] = None,
        state: Optional[str] = None,
    ) -> Dict[str, Any]:
        """更新工作流
        
        Args:
            workflow_id: 工作流ID
            name: 工作流名称
            schedule: 调度表达式
            description: 描述
            state: 状态 (ACTIVE, PAUSED)
            
        Returns:
            更新后的工作流
        """
        data = {}
        if name:
            data["name"] = name
        if schedule:
            data["schedule"] = schedule
        if description:
            data["description"] = description
        if state:
            data["state"] = state
            
        return await self._make_request(
            "PUT",
            f"/amc/workflows/{workflow_id}",
            json=data,
        )
    
    async def delete_workflow(
        self,
        workflow_id: str,
    ) -> None:
        """删除工作流
        
        Args:
            workflow_id: 工作流ID
        """
        await self._make_request(
            "DELETE",
            f"/amc/workflows/{workflow_id}",
        )
    
    # ==================== 工作流执行 ====================
    
    async def trigger_workflow(
        self,
        workflow_id: str,
        parameters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """手动触发工作流
        
        Args:
            workflow_id: 工作流ID
            parameters: 执行参数
            
        Returns:
            执行任务信息
        """
        return await self._make_request(
            "POST",
            f"/amc/workflows/{workflow_id}/trigger",
            json=parameters if parameters else None,
        )
    
    async def list_workflow_executions(
        self,
        workflow_id: str,
        status: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取工作流执行历史
        
        Args:
            workflow_id: 工作流ID
            status: 执行状态 (RUNNING, COMPLETED, FAILED)
            max_results: 最大结果数
            next_token: 分页token
            
        Returns:
            执行历史列表
        """
        params = {"maxResults": max_results}
        if status:
            params["status"] = status
        if next_token:
            params["nextToken"] = next_token
            
        return await self._make_request(
            "GET",
            f"/amc/workflows/{workflow_id}/executions",
            params=params,
        )
    
    async def get_workflow_execution(
        self,
        workflow_id: str,
        execution_id: str,
    ) -> Dict[str, Any]:
        """获取工作流执行详情
        
        Args:
            workflow_id: 工作流ID
            execution_id: 执行ID
            
        Returns:
            执行详情
        """
        return await self._make_request(
            "GET",
            f"/amc/workflows/{workflow_id}/executions/{execution_id}",
        )
    
    # ==================== 输出管理 ====================
    
    async def list_workflow_outputs(
        self,
        workflow_id: str,
        execution_id: str,
    ) -> List[Dict[str, Any]]:
        """获取工作流输出列表
        
        Args:
            workflow_id: 工作流ID
            execution_id: 执行ID
            
        Returns:
            输出列表
        """
        response = await self._make_request(
            "GET",
            f"/amc/workflows/{workflow_id}/executions/{execution_id}/outputs",
        )
        return response.get("outputs", [])
    
    async def download_workflow_output(
        self,
        workflow_id: str,
        execution_id: str,
        output_id: str,
    ) -> bytes:
        """下载工作流输出
        
        Args:
            workflow_id: 工作流ID
            execution_id: 执行ID
            output_id: 输出ID
            
        Returns:
            输出内容
        """
        return await self._make_request(
            "GET",
            f"/amc/workflows/{workflow_id}/executions/{execution_id}/outputs/{output_id}/download",
        )

