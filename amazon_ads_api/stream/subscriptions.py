"""
Amazon Marketing Stream API (异步版本)
营销数据流订阅
"""

from typing import Any
from ..base import BaseAdsClient, JSONData, JSONList


class MarketingStreamAPI(BaseAdsClient):
    """Amazon Marketing Stream API (全异步)"""

    # ==================== 订阅管理 ====================

    async def list_subscriptions(self) -> JSONList:
        """获取订阅列表"""
        response = await self.get("/streams/subscriptions")
        if isinstance(response, dict):
            return response.get("subscriptions", [])
        return []

    async def create_subscription(
        self,
        data_set_id: str,
        destination_arn: str,
        client_request_token: str | None = None,
        notes: str | None = None,
    ) -> JSONData:
        """创建订阅"""
        data: dict[str, Any] = {
            "dataSetId": data_set_id,
            "destinationArn": destination_arn,
        }
        if client_request_token:
            data["clientRequestToken"] = client_request_token
        if notes:
            data["notes"] = notes

        result = await self.post("/streams/subscriptions", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_subscription(self, subscription_id: str) -> JSONData:
        """获取订阅详情"""
        result = await self.get(f"/streams/subscriptions/{subscription_id}")
        return result if isinstance(result, dict) else {}

    async def update_subscription(
        self,
        subscription_id: str,
        status: str | None = None,
        notes: str | None = None,
    ) -> JSONData:
        """更新订阅"""
        data: dict[str, Any] = {}
        if status:
            data["status"] = status
        if notes:
            data["notes"] = notes

        result = await self.put(
            f"/streams/subscriptions/{subscription_id}", json_data=data
        )
        return result if isinstance(result, dict) else {}

    async def delete_subscription(self, subscription_id: str) -> JSONData:
        """删除订阅"""
        result = await self.delete(f"/streams/subscriptions/{subscription_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 数据集 ====================

    async def list_data_sets(self) -> JSONList:
        """获取可用数据集列表"""
        response = await self.get("/streams/dataSets")
        if isinstance(response, dict):
            return response.get("dataSets", [])
        return []

    async def get_data_set_schema(self, data_set_id: str) -> JSONData:
        """获取数据集模式"""
        result = await self.get(f"/streams/dataSets/{data_set_id}/schema")
        return result if isinstance(result, dict) else {}

    # ==================== 目标配置 ====================

    async def validate_destination(self, destination_arn: str) -> JSONData:
        """验证目标配置"""
        data = {"destinationArn": destination_arn}
        result = await self.post("/streams/destinations/validate", json_data=data)
        return result if isinstance(result, dict) else {}

    # ==================== 消息处理 ====================

    async def get_sample_messages(
        self,
        data_set_id: str,
        count: int = 10,
    ) -> JSONList:
        """获取示例消息"""
        params = {
            "dataSetId": data_set_id,
            "count": count,
        }
        response = await self.get("/streams/samples", params=params)
        if isinstance(response, dict):
            return response.get("messages", [])
        return []
