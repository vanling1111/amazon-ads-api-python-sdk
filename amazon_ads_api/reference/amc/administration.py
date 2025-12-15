"""
Amazon Marketing Cloud Administration API (异步版本)

官方 Spec: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AMCAdministration_prod_3p.json
验证日期: 2024-12-15

官方端点数: 22
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData


class AMCAdministrationAPI(BaseAdsClient):
    """AMC Administration API (全异步)
    
    API Tier: L1
    Source: OpenAPI
    OpenAPI_SPEC: AMCAdministration_prod_3p.json
    Stability: 高
    
    管理 AMC 实例、广告主、协作和身份映射表。
    官方验证: 22个端点
    """

    # ==================== Accounts ====================

    async def get_accounts(self) -> JSONData:
        """获取可用的 AMC 账户列表
        
        官方端点: GET /amc/accounts
        """
        result = await self.get("/amc/accounts")
        return result if isinstance(result, dict) else {"accounts": []}

    # ==================== Instances ====================

    async def list_instances(self) -> JSONData:
        """获取 AMC 实例列表
        
        官方端点: GET /amc/instances
        """
        result = await self.get("/amc/instances")
        return result if isinstance(result, dict) else {"instances": []}

    async def create_instance(
        self,
        instance_data: dict[str, Any],
    ) -> JSONData:
        """创建 AMC 实例
        
        官方端点: POST /amc/instances
        
        Args:
            instance_data: 实例配置，包含:
                - instanceName: 实例名称 (必需)
                - advertiserName: 广告主名称
                - s3BucketName: S3 存储桶名称
                - awsAccountId: AWS 账户 ID
                - acrBacked: 是否使用 AWS Clean Rooms
                - acrCustomerPartners: ACR 客户合作伙伴列表
                - idempotencyToken: 幂等性令牌
        """
        result = await self.post("/amc/instances", json_data=instance_data)
        return result if isinstance(result, dict) else {}

    async def get_instance(self, instance_id: str) -> JSONData:
        """获取 AMC 实例详情
        
        官方端点: GET /amc/instances/{instanceId}
        """
        result = await self.get(f"/amc/instances/{instance_id}")
        return result if isinstance(result, dict) else {}

    async def update_instance(
        self,
        instance_id: str,
        instance_data: dict[str, Any],
    ) -> JSONData:
        """更新 AMC 实例
        
        官方端点: PUT /amc/instances/{instanceId}
        
        Args:
            instance_id: 实例 ID
            instance_data: 更新数据，可包含:
                - instanceName: 实例名称
                - advertiserName: 广告主名称
                - s3BucketName: S3 存储桶名称
                - awsAccountId: AWS 账户 ID
        """
        result = await self.put(f"/amc/instances/{instance_id}", json_data=instance_data)
        return result if isinstance(result, dict) else {}

    async def delete_instance(self, instance_id: str) -> JSONData:
        """删除 AMC 实例
        
        官方端点: DELETE /amc/instances/{instanceId}
        """
        result = await self.delete(f"/amc/instances/{instance_id}")
        return result if isinstance(result, dict) else {}

    async def update_customer_aws_account(
        self,
        instance_id: str,
        aws_account_data: dict[str, Any],
    ) -> JSONData:
        """更新客户 AWS 账户元数据
        
        官方端点: POST /amc/instances/{instanceId}/updateCustomerAwsAccount
        """
        result = await self.post(
            f"/amc/instances/{instance_id}/updateCustomerAwsAccount",
            json_data=aws_account_data,
        )
        return result if isinstance(result, dict) else {}

    # ==================== Advertisers ====================

    async def list_advertisers(self, instance_id: str) -> JSONData:
        """获取实例下的广告主列表
        
        官方端点: GET /amc/instances/{instanceId}/advertisers
        """
        result = await self.get(f"/amc/instances/{instance_id}/advertisers")
        return result if isinstance(result, dict) else {"advertisers": []}

    async def list_advertiser_updates(self, instance_id: str) -> JSONData:
        """获取广告主更新列表
        
        官方端点: GET /amc/instances/{instanceId}/advertisers/updates
        """
        result = await self.get(f"/amc/instances/{instance_id}/advertisers/updates")
        return result if isinstance(result, dict) else {"advertiserUpdates": []}

    async def create_advertiser_update(
        self,
        instance_id: str,
        update_data: dict[str, Any],
    ) -> JSONData:
        """创建广告主更新请求
        
        官方端点: POST /amc/instances/{instanceId}/advertisers/updates
        
        Args:
            instance_id: 实例 ID
            update_data: 更新数据，包含:
                - advertisersToAdd: 要添加的广告主列表
                - advertisersToRemove: 要移除的广告主列表
        """
        result = await self.post(
            f"/amc/instances/{instance_id}/advertisers/updates",
            json_data=update_data,
        )
        return result if isinstance(result, dict) else {}

    async def get_advertiser_update(
        self,
        instance_id: str,
        update_id: str,
    ) -> JSONData:
        """获取广告主更新详情
        
        官方端点: GET /amc/instances/{instanceId}/advertisers/updates/{updateId}
        """
        result = await self.get(
            f"/amc/instances/{instance_id}/advertisers/updates/{update_id}"
        )
        return result if isinstance(result, dict) else {}

    # ==================== Collaboration ====================

    async def get_collaboration(self, instance_id: str) -> JSONData:
        """获取实例的协作信息
        
        官方端点: GET /amc/instances/{instanceId}/collaboration
        """
        result = await self.get(f"/amc/instances/{instance_id}/collaboration")
        return result if isinstance(result, dict) else {}

    async def list_id_namespaces(
        self,
        instance_id: str,
        list_request: dict[str, Any] | None = None,
    ) -> JSONData:
        """获取 ID 命名空间列表
        
        官方端点: POST /amc/instances/{instanceId}/collaboration/idnamespaces/list
        """
        result = await self.post(
            f"/amc/instances/{instance_id}/collaboration/idnamespaces/list",
            json_data=list_request or {},
        )
        return result if isinstance(result, dict) else {"idNamespaces": []}

    # ==================== ID Mapping Tables ====================

    async def create_id_mapping_table(
        self,
        instance_id: str,
        table_data: dict[str, Any],
    ) -> JSONData:
        """创建 ID 映射表
        
        官方端点: POST /amc/instances/{instanceId}/collaboration/idmappingtables
        """
        result = await self.post(
            f"/amc/instances/{instance_id}/collaboration/idmappingtables",
            json_data=table_data,
        )
        return result if isinstance(result, dict) else {}

    async def list_id_mapping_tables(
        self,
        instance_id: str,
        list_request: dict[str, Any] | None = None,
    ) -> JSONData:
        """获取 ID 映射表列表
        
        官方端点: POST /amc/instances/{instanceId}/collaboration/idmappingtables/list
        """
        result = await self.post(
            f"/amc/instances/{instance_id}/collaboration/idmappingtables/list",
            json_data=list_request or {},
        )
        return result if isinstance(result, dict) else {"idMappingTables": []}

    async def delete_id_mapping_table(
        self,
        instance_id: str,
        id_mapping_table_id: str,
    ) -> JSONData:
        """删除 ID 映射表
        
        官方端点: DELETE /amc/instances/{instanceId}/collaboration/idmappingtables/{idMappingTableId}
        """
        result = await self.delete(
            f"/amc/instances/{instance_id}/collaboration/idmappingtables/{id_mapping_table_id}"
        )
        return result if isinstance(result, dict) else {}

    async def refresh_id_mapping_table(
        self,
        instance_id: str,
        id_mapping_table_id: str,
    ) -> JSONData:
        """刷新 ID 映射表
        
        官方端点: POST /amc/instances/{instanceId}/collaboration/idmappingtables/{idMappingTableId}/refresh
        """
        result = await self.post(
            f"/amc/instances/{instance_id}/collaboration/idmappingtables/{id_mapping_table_id}/refresh"
        )
        return result if isinstance(result, dict) else {}

    async def list_id_mapping_table_jobs(
        self,
        instance_id: str,
        id_mapping_table_id: str,
        list_request: dict[str, Any] | None = None,
    ) -> JSONData:
        """获取 ID 映射表任务列表
        
        官方端点: POST /amc/instances/{instanceId}/collaboration/idmappingtables/{idMappingTableId}/jobs/list
        """
        result = await self.post(
            f"/amc/instances/{instance_id}/collaboration/idmappingtables/{id_mapping_table_id}/jobs/list",
            json_data=list_request or {},
        )
        return result if isinstance(result, dict) else {"jobs": []}

    async def get_id_mapping_table_job(
        self,
        instance_id: str,
        id_mapping_table_id: str,
        job_id: str,
    ) -> JSONData:
        """获取 ID 映射表任务详情
        
        官方端点: GET /amc/instances/{instanceId}/collaboration/idmappingtables/{idMappingTableId}/jobs/{jobId}
        """
        result = await self.get(
            f"/amc/instances/{instance_id}/collaboration/idmappingtables/{id_mapping_table_id}/jobs/{job_id}"
        )
        return result if isinstance(result, dict) else {}

    async def get_job_tracker(
        self,
        instance_id: str,
        id_mapping_table_id: str,
        tracking_id: str,
    ) -> JSONData:
        """获取任务追踪状态
        
        官方端点: GET /amc/instances/{instanceId}/collaboration/idmappingtables/{idMappingTableId}/jobTracker/{trackingId}
        """
        result = await self.get(
            f"/amc/instances/{instance_id}/collaboration/idmappingtables/{id_mapping_table_id}/jobTracker/{tracking_id}"
        )
        return result if isinstance(result, dict) else {}

    # ==================== ACR Customer Partners ====================

    async def add_acr_customer_partners(
        self,
        instance_id: str,
        collaboration_id: str,
        partner_data: dict[str, Any],
    ) -> JSONData:
        """添加 ACR 客户合作伙伴
        
        官方端点: POST /amc/instances/{instanceId}/collaborations/{collaborationId}/acrCustomerPartners
        """
        result = await self.post(
            f"/amc/instances/{instance_id}/collaborations/{collaboration_id}/acrCustomerPartners",
            json_data=partner_data,
        )
        return result if isinstance(result, dict) else {}

    async def delete_acr_customer_partner(
        self,
        instance_id: str,
        collaboration_id: str,
        acr_customer_partner_id: str,
    ) -> JSONData:
        """删除 ACR 客户合作伙伴
        
        官方端点: DELETE /amc/instances/{instanceId}/collaborations/{collaborationId}/acrCustomerPartners/{acrCustomerPartnerId}
        """
        result = await self.delete(
            f"/amc/instances/{instance_id}/collaborations/{collaboration_id}/acrCustomerPartners/{acr_customer_partner_id}"
        )
        return result if isinstance(result, dict) else {}
