"""
Amazon Marketing Cloud Reporting API (异步版本)

官方 Spec: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/WorkflowManagementService_prod_3p.json
验证日期: 2024-12-15

官方端点数: 17
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData


class AMCReportingAPI(BaseAdsClient):
    """AMC Reporting API (全异步)
    
    API Tier: L1
    Source: OpenAPI
    OpenAPI_SPEC: WorkflowManagementService_prod_3p.json (AMC Reporting)
    Stability: 高
    
    管理 AMC 报告工作流、调度和执行。
    官方验证: 17个端点
    """

    # ==================== Data Sources ====================

    async def list_data_sources(self, instance_id: str) -> JSONData:
        """获取数据源列表
        
        官方端点: GET /amc/reporting/{instanceId}/dataSources
        """
        result = await self.get(f"/amc/reporting/{instance_id}/dataSources")
        return result if isinstance(result, dict) else {"dataSources": []}

    async def get_data_source(
        self,
        instance_id: str,
        data_source_id: str,
    ) -> JSONData:
        """获取数据源详情
        
        官方端点: GET /amc/reporting/{instanceId}/dataSources/{dataSourceId}
        """
        result = await self.get(
            f"/amc/reporting/{instance_id}/dataSources/{data_source_id}"
        )
        return result if isinstance(result, dict) else {}

    # ==================== Schedules ====================

    async def list_schedules(self, instance_id: str) -> JSONData:
        """获取调度列表
        
        官方端点: GET /amc/reporting/{instanceId}/schedules
        """
        result = await self.get(f"/amc/reporting/{instance_id}/schedules")
        return result if isinstance(result, dict) else {"schedules": []}

    async def create_schedule(
        self,
        instance_id: str,
        schedule_data: dict[str, Any],
    ) -> JSONData:
        """创建调度
        
        官方端点: POST /amc/reporting/{instanceId}/schedules
        """
        result = await self.post(
            f"/amc/reporting/{instance_id}/schedules",
            json_data=schedule_data,
        )
        return result if isinstance(result, dict) else {}

    async def get_schedule(
        self,
        instance_id: str,
        schedule_id: str,
    ) -> JSONData:
        """获取调度详情
        
        官方端点: GET /amc/reporting/{instanceId}/schedules/{scheduleId}
        """
        result = await self.get(
            f"/amc/reporting/{instance_id}/schedules/{schedule_id}"
        )
        return result if isinstance(result, dict) else {}

    async def update_schedule(
        self,
        instance_id: str,
        schedule_id: str,
        schedule_data: dict[str, Any],
    ) -> JSONData:
        """更新调度
        
        官方端点: PUT /amc/reporting/{instanceId}/schedules/{scheduleId}
        """
        result = await self.put(
            f"/amc/reporting/{instance_id}/schedules/{schedule_id}",
            json_data=schedule_data,
        )
        return result if isinstance(result, dict) else {}

    async def delete_schedule(
        self,
        instance_id: str,
        schedule_id: str,
    ) -> JSONData:
        """删除调度
        
        官方端点: DELETE /amc/reporting/{instanceId}/schedules/{scheduleId}
        """
        result = await self.delete(
            f"/amc/reporting/{instance_id}/schedules/{schedule_id}"
        )
        return result if isinstance(result, dict) else {}

    # ==================== Workflows ====================

    async def list_workflows(self, instance_id: str) -> JSONData:
        """获取工作流列表
        
        官方端点: GET /amc/reporting/{instanceId}/workflows
        """
        result = await self.get(f"/amc/reporting/{instance_id}/workflows")
        return result if isinstance(result, dict) else {"workflows": []}

    async def create_workflow(
        self,
        instance_id: str,
        workflow_data: dict[str, Any],
    ) -> JSONData:
        """创建工作流
        
        官方端点: POST /amc/reporting/{instanceId}/workflows
        """
        result = await self.post(
            f"/amc/reporting/{instance_id}/workflows",
            json_data=workflow_data,
        )
        return result if isinstance(result, dict) else {}

    async def get_workflow(
        self,
        instance_id: str,
        workflow_id: str,
    ) -> JSONData:
        """获取工作流详情
        
        官方端点: GET /amc/reporting/{instanceId}/workflows/{workflowId}
        """
        result = await self.get(
            f"/amc/reporting/{instance_id}/workflows/{workflow_id}"
        )
        return result if isinstance(result, dict) else {}

    async def update_workflow(
        self,
        instance_id: str,
        workflow_id: str,
        workflow_data: dict[str, Any],
    ) -> JSONData:
        """更新工作流
        
        官方端点: PUT /amc/reporting/{instanceId}/workflows/{workflowId}
        """
        result = await self.put(
            f"/amc/reporting/{instance_id}/workflows/{workflow_id}",
            json_data=workflow_data,
        )
        return result if isinstance(result, dict) else {}

    async def delete_workflow(
        self,
        instance_id: str,
        workflow_id: str,
    ) -> JSONData:
        """删除工作流
        
        官方端点: DELETE /amc/reporting/{instanceId}/workflows/{workflowId}
        """
        result = await self.delete(
            f"/amc/reporting/{instance_id}/workflows/{workflow_id}"
        )
        return result if isinstance(result, dict) else {}

    # ==================== Workflow Executions ====================

    async def list_workflow_executions(self, instance_id: str) -> JSONData:
        """获取工作流执行列表
        
        官方端点: GET /amc/reporting/{instanceId}/workflowExecutions
        """
        result = await self.get(f"/amc/reporting/{instance_id}/workflowExecutions")
        return result if isinstance(result, dict) else {"workflowExecutions": []}

    async def create_workflow_execution(
        self,
        instance_id: str,
        execution_data: dict[str, Any],
    ) -> JSONData:
        """创建工作流执行
        
        官方端点: POST /amc/reporting/{instanceId}/workflowExecutions
        
        Args:
            instance_id: AMC实例ID
            execution_data: 执行配置，可包含:
                - workflowId: 工作流ID
                - disableAggregationControl: 是否禁用隐私控制
                - dryRun: 是否干运行（验证但不执行）
                - maxCertifiedTime: 最大认证时间
                - requireSyntheticData: 是否需要合成数据
        """
        result = await self.post(
            f"/amc/reporting/{instance_id}/workflowExecutions",
            json_data=execution_data,
        )
        return result if isinstance(result, dict) else {}

    async def get_workflow_execution(
        self,
        instance_id: str,
        workflow_execution_id: str,
    ) -> JSONData:
        """获取工作流执行详情
        
        官方端点: GET /amc/reporting/{instanceId}/workflowExecutions/{workflowExecutionId}
        """
        result = await self.get(
            f"/amc/reporting/{instance_id}/workflowExecutions/{workflow_execution_id}"
        )
        return result if isinstance(result, dict) else {}

    async def update_workflow_execution(
        self,
        instance_id: str,
        workflow_execution_id: str,
        execution_data: dict[str, Any],
    ) -> JSONData:
        """更新工作流执行
        
        官方端点: PUT /amc/reporting/{instanceId}/workflowExecutions/{workflowExecutionId}
        """
        result = await self.put(
            f"/amc/reporting/{instance_id}/workflowExecutions/{workflow_execution_id}",
            json_data=execution_data,
        )
        return result if isinstance(result, dict) else {}

    async def get_workflow_execution_download_urls(
        self,
        instance_id: str,
        workflow_execution_id: str,
    ) -> JSONData:
        """获取工作流执行结果的下载链接
        
        官方端点: GET /amc/reporting/{instanceId}/workflowExecutions/{workflowExecutionId}/downloadUrls
        """
        result = await self.get(
            f"/amc/reporting/{instance_id}/workflowExecutions/{workflow_execution_id}/downloadUrls"
        )
        return result if isinstance(result, dict) else {"downloadUrls": []}
