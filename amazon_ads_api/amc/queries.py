"""
Amazon Marketing Cloud Queries API

官方文档: https://advertising.amazon.com/API/docs/en-us/amc/amc-query-api
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AMC_Query_API_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class AMCQueriesAPI(BaseAdsClient):
    """AMC Queries API - 查询管理
    
    管理Amazon Marketing Cloud SQL查询。
    """
    
    # ==================== 查询管理 ====================
    
    async def list_queries(
        self,
        state: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取查询列表
        
        Args:
            state: 状态 (ACTIVE, PAUSED, DELETED)
            max_results: 最大结果数
            next_token: 分页token
            
        Returns:
            查询列表
        """
        params = {"maxResults": max_results}
        if state:
            params["state"] = state
        if next_token:
            params["nextToken"] = next_token
            
        return await self._make_request(
            "GET",
            "/amc/queries",
            params=params,
        )
    
    async def create_query(
        self,
        name: str,
        sql: str,
        description: Optional[str] = None,
        parameters: Optional[List[Dict[str, Any]]] = None,
    ) -> Dict[str, Any]:
        """创建查询
        
        Args:
            name: 查询名称
            sql: SQL语句
            description: 描述
            parameters: 查询参数定义
            
        Returns:
            创建的查询
        """
        data = {
            "name": name,
            "sql": sql,
        }
        if description:
            data["description"] = description
        if parameters:
            data["parameters"] = parameters
            
        return await self._make_request(
            "POST",
            "/amc/queries",
            json=data,
        )
    
    async def get_query(
        self,
        query_id: str,
    ) -> Dict[str, Any]:
        """获取查询详情
        
        Args:
            query_id: 查询ID
            
        Returns:
            查询详情
        """
        return await self._make_request(
            "GET",
            f"/amc/queries/{query_id}",
        )
    
    async def update_query(
        self,
        query_id: str,
        name: Optional[str] = None,
        sql: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """更新查询
        
        Args:
            query_id: 查询ID
            name: 查询名称
            sql: SQL语句
            description: 描述
            
        Returns:
            更新后的查询
        """
        data = {}
        if name:
            data["name"] = name
        if sql:
            data["sql"] = sql
        if description:
            data["description"] = description
            
        return await self._make_request(
            "PUT",
            f"/amc/queries/{query_id}",
            json=data,
        )
    
    async def delete_query(
        self,
        query_id: str,
    ) -> None:
        """删除查询
        
        Args:
            query_id: 查询ID
        """
        await self._make_request(
            "DELETE",
            f"/amc/queries/{query_id}",
        )
    
    # ==================== 查询执行 ====================
    
    async def execute_query(
        self,
        query_id: str,
        parameters: Optional[Dict[str, Any]] = None,
        time_window: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """执行查询
        
        Args:
            query_id: 查询ID
            parameters: 查询参数值
            time_window: 时间窗口 {"startDate": "YYYY-MM-DD", "endDate": "YYYY-MM-DD"}
            
        Returns:
            执行任务信息
        """
        data = {}
        if parameters:
            data["parameters"] = parameters
        if time_window:
            data["timeWindow"] = time_window
            
        return await self._make_request(
            "POST",
            f"/amc/queries/{query_id}/execute",
            json=data if data else None,
        )
    
    async def get_execution_status(
        self,
        execution_id: str,
    ) -> Dict[str, Any]:
        """获取执行状态
        
        Args:
            execution_id: 执行ID
            
        Returns:
            执行状态
        """
        return await self._make_request(
            "GET",
            f"/amc/executions/{execution_id}",
        )
    
    async def get_execution_results(
        self,
        execution_id: str,
        max_results: int = 1000,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取执行结果
        
        Args:
            execution_id: 执行ID
            max_results: 最大结果数
            next_token: 分页token
            
        Returns:
            查询结果
        """
        params = {"maxResults": max_results}
        if next_token:
            params["nextToken"] = next_token
            
        return await self._make_request(
            "GET",
            f"/amc/executions/{execution_id}/results",
            params=params,
        )
    
    async def cancel_execution(
        self,
        execution_id: str,
    ) -> Dict[str, Any]:
        """取消执行
        
        Args:
            execution_id: 执行ID
            
        Returns:
            取消结果
        """
        return await self._make_request(
            "POST",
            f"/amc/executions/{execution_id}/cancel",
        )
    
    # ==================== 查询模板 ====================
    
    async def list_query_templates(self) -> List[Dict[str, Any]]:
        """获取查询模板列表
        
        Returns:
            模板列表
        """
        response = await self._make_request(
            "GET",
            "/amc/templates",
        )
        return response.get("templates", [])
    
    async def get_query_template(
        self,
        template_id: str,
    ) -> Dict[str, Any]:
        """获取查询模板详情
        
        Args:
            template_id: 模板ID
            
        Returns:
            模板详情
        """
        return await self._make_request(
            "GET",
            f"/amc/templates/{template_id}",
        )

