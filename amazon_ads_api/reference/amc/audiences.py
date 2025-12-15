"""
Amazon Marketing Cloud Advertiser Audiences API (异步版本)

官方 Spec: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Advertiseraudiences_prod_3p.json
验证日期: 2024-12-15

官方端点数: 10
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData


class AMCAudiencesAPI(BaseAdsClient):
    """AMC Advertiser Audiences API (全异步)
    
    API Tier: L1
    Source: OpenAPI
    OpenAPI_SPEC: Advertiseraudiences_prod_3p.json
    Stability: 高
    
    管理 AMC 广告主受众连接、元数据和记录。
    官方验证: 10个端点
    """

    # ==================== Connections ====================

    async def list_connections(self) -> JSONData:
        """获取受众连接列表
        
        官方端点: GET /amc/audiences/connections
        """
        result = await self.get("/amc/audiences/connections")
        return result if isinstance(result, dict) else {"connections": []}

    async def create_connection(
        self,
        connection_data: dict[str, Any],
    ) -> JSONData:
        """创建受众连接
        
        官方端点: POST /amc/audiences/connections
        
        Args:
            connection_data: 连接配置
        """
        result = await self.post("/amc/audiences/connections", json_data=connection_data)
        return result if isinstance(result, dict) else {}

    async def delete_connections(
        self,
        connection_ids: list[str] | None = None,
    ) -> JSONData:
        """删除受众连接
        
        官方端点: DELETE /amc/audiences/connections
        
        Args:
            connection_ids: 要删除的连接 ID 列表 (通过 query params)
        """
        params = {}
        if connection_ids:
            params["connectionIds"] = ",".join(connection_ids)
        result = await self.delete("/amc/audiences/connections", params=params or None)
        return result if isinstance(result, dict) else {}

    # ==================== Connections Terms ====================

    async def get_connections_terms(self) -> JSONData:
        """获取受众连接条款
        
        官方端点: GET /amc/audiences/connections/terms
        """
        result = await self.get("/amc/audiences/connections/terms")
        return result if isinstance(result, dict) else {}

    async def update_connections_terms(
        self,
        terms_data: dict[str, Any],
    ) -> JSONData:
        """更新受众连接条款 (接受条款)
        
        官方端点: PATCH /amc/audiences/connections/terms
        
        Args:
            terms_data: 条款更新数据，包含:
                - accepted: 是否接受条款 (boolean)
        """
        result = await self.patch("/amc/audiences/connections/terms", json_data=terms_data)
        return result if isinstance(result, dict) else {}

    # ==================== Audience Metadata ====================

    async def create_audience_metadata(
        self,
        metadata: dict[str, Any],
    ) -> JSONData:
        """创建受众元数据
        
        官方端点: POST /amc/audiences/metadata
        
        Args:
            metadata: 受众元数据配置，包含:
                - name: 受众名称
                - description: 受众描述
                - audienceType: 受众类型
                - ttlInDays: 生存时间 (天)
                - externalAudienceId: 外部受众 ID
        """
        result = await self.post("/amc/audiences/metadata", json_data=metadata)
        return result if isinstance(result, dict) else {}

    async def get_audience_metadata(
        self,
        audience_id: str,
    ) -> JSONData:
        """获取受众元数据
        
        官方端点: GET /amc/audiences/metadata/{audienceId}
        
        Args:
            audience_id: 受众 ID
        """
        result = await self.get(f"/amc/audiences/metadata/{audience_id}")
        return result if isinstance(result, dict) else {}

    async def update_audience_metadata(
        self,
        audience_id: str,
        metadata: dict[str, Any],
    ) -> JSONData:
        """更新受众元数据
        
        官方端点: PUT /amc/audiences/metadata/{audienceId}
        
        Args:
            audience_id: 受众 ID
            metadata: 更新的元数据
        """
        result = await self.put(
            f"/amc/audiences/metadata/{audience_id}",
            json_data=metadata,
        )
        return result if isinstance(result, dict) else {}

    # ==================== Audience Records ====================

    async def create_audience_records(
        self,
        records_data: dict[str, Any],
    ) -> JSONData:
        """创建/上传受众记录
        
        官方端点: POST /amc/audiences/records
        
        Args:
            records_data: 记录数据，包含:
                - audienceId: 受众 ID
                - records: 记录列表
                - action: 操作类型 (ADD/REMOVE)
        """
        result = await self.post("/amc/audiences/records", json_data=records_data)
        return result if isinstance(result, dict) else {}

    async def get_audience_records_job(
        self,
        job_request_id: str,
    ) -> JSONData:
        """获取受众记录任务状态
        
        官方端点: GET /amc/audiences/records/{jobRequestId}
        
        Args:
            job_request_id: 任务请求 ID
        """
        result = await self.get(f"/amc/audiences/records/{job_request_id}")
        return result if isinstance(result, dict) else {}
