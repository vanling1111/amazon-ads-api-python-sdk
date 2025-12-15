"""
Amazon Ads Data Provider Audience Metadata API (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/data-provider/openapi
验证日期: 2024-12-15

端点:
- POST /v2/dp/audiencemetadata/ - 创建受众
- GET /v2/dp/audiencemetadata/{audienceId} - 获取受众
- PUT /v2/dp/audiencemetadata/{audienceId} - 更新受众
- PATCH /v2/dp/audience - 关联/取消关联记录
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData


class AudienceMetadataAPI(BaseAdsClient):
    """Data Provider Audience Metadata API (全异步)
    
    官方验证: 4个端点
    """

    # ==================== 受众创建 ====================

    async def create_audience(
        self,
        name: str,
        description: str,
        advertiser_id: int,
        metadata: dict[str, Any],
    ) -> JSONData:
        """创建新的数据提供商受众
        
        官方端点: POST /v2/dp/audiencemetadata/
        限流: 1 TPS
        
        Args:
            name: 受众名称 (10-128字符，字母数字)
            description: 受众描述 (0-1000字符)
            advertiser_id: 广告商ID
            metadata: 元数据对象，包含:
                - type: 受众类型 (如 "DATA_PROVIDER")
                - externalAudienceId: 外部受众ID
                - ttl: 生存时间 (秒)
                - audienceFees: 受众费用列表
                - dataSourceCountry: 数据源国家列表
        
        Returns:
            创建结果，包含 requestId 和 audience 对象
        """
        data = {
            "name": name,
            "description": description,
            "advertiserId": advertiser_id,
            "metadata": metadata,
        }
        result = await self.post("/v2/dp/audiencemetadata/", json_data=data)
        return result if isinstance(result, dict) else {}

    # ==================== 受众获取 ====================

    async def get_audience(self, audience_id: int) -> JSONData:
        """获取受众元数据
        
        官方端点: GET /v2/dp/audiencemetadata/{audienceId}
        限流: 1 TPS
        
        Args:
            audience_id: 受众ID (int64)
        
        Returns:
            受众详情，包含 id, name, description, advertiserId, metadata
        """
        result = await self.get(f"/v2/dp/audiencemetadata/{audience_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 受众更新 ====================

    async def update_audience(
        self,
        audience_id: int,
        description: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> JSONData:
        """更新受众元数据
        
        官方端点: PUT /v2/dp/audiencemetadata/{audienceId}
        限流: 1 TPS
        
        Args:
            audience_id: 受众ID (int64)
            description: 新的受众描述 (可选)
            metadata: 新的元数据对象 (可选)，可包含:
                - ttl: 生存时间 (秒)
                - audienceFees: 受众费用列表
                - dataSourceCountry: 数据源国家列表
        
        Returns:
            更新后的受众详情
        """
        data: dict[str, Any] = {}
        if description is not None:
            data["description"] = description
        if metadata is not None:
            data["metadata"] = metadata

        result = await self.put(f"/v2/dp/audiencemetadata/{audience_id}", json_data=data)
        return result if isinstance(result, dict) else {}

    # ==================== 记录关联 ====================

    async def associate_records(
        self,
        patches: list[dict[str, Any]],
    ) -> JSONData:
        """关联或取消关联记录与受众
        
        官方端点: PATCH /v2/dp/audience
        限流: 100 TPS
        最大负载: 6MB 或 2000 条记录
        
        Args:
            patches: 补丁操作列表，每个补丁包含:
                - op: 操作类型 ("add" 或 "remove")
                - path: 受众路径
                - value: 记录值
        
        Returns:
            请求结果，包含 jobId 和 requestId
            注意: 请求可能需要最多2小时处理
        """
        data = {"patches": patches}
        result = await self.patch("/v2/dp/audience", json_data=data)
        return result if isinstance(result, dict) else {}

    # ==================== 用户删除 ====================

    async def delete_users(
        self,
        patches: list[dict[str, Any]],
    ) -> JSONData:
        """删除用户数据（GDPR/隐私合规）
        
        官方端点: PATCH /v2/dp/users
        官方规范: DataProvider.yaml
        
        Args:
            patches: 补丁操作列表，每个补丁包含:
                - op: 操作类型 ("remove")
                - path: 用户路径
                - value: 用户标识符
        
        Returns:
            请求结果
        """
        data = {"patches": patches}
        result = await self.patch("/v2/dp/users", json_data=data)
        return result if isinstance(result, dict) else {}

