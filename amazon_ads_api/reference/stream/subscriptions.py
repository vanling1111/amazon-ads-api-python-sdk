"""
Amazon Marketing Stream API (异步版本)
基于官方文档: https://advertising.amazon.com/API/docs/en-us/amazon-marketing-stream/openapi

官方端点数: 8 (普通流 4 + DSP流 4)
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class MarketingStreamAPI(BaseAdsClient):
    """Amazon Marketing Stream API (全异步)
    
    管理营销数据流订阅，包括普通流和DSP流。
    """

    # ==================== 普通订阅 (SP/SB/SD) ====================

    async def list_subscriptions(self) -> JSONList:
        """获取订阅列表
        
        GET /streams/subscriptions
        """
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
        """创建订阅
        
        POST /streams/subscriptions
        """
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
        """获取订阅详情
        
        GET /streams/subscriptions/{subscriptionId}
        """
        result = await self.get(f"/streams/subscriptions/{subscription_id}")
        return result if isinstance(result, dict) else {}

    async def update_subscription(
        self,
        subscription_id: str,
        status: str | None = None,
        notes: str | None = None,
    ) -> JSONData:
        """更新订阅
        
        PUT /streams/subscriptions/{subscriptionId}
        """
        data: dict[str, Any] = {}
        if status:
            data["status"] = status
        if notes:
            data["notes"] = notes

        result = await self.put(
            f"/streams/subscriptions/{subscription_id}", json_data=data
        )
        return result if isinstance(result, dict) else {}

    # ==================== DSP订阅 ====================

    async def list_dsp_subscriptions(self) -> JSONList:
        """获取DSP订阅列表
        
        GET /dsp/streams/subscriptions
        """
        response = await self.get("/dsp/streams/subscriptions")
        if isinstance(response, dict):
            return response.get("subscriptions", [])
        return []

    async def create_dsp_subscription(
        self,
        data_set_id: str,
        destination_arn: str,
        client_request_token: str | None = None,
        notes: str | None = None,
    ) -> JSONData:
        """创建DSP订阅
        
        POST /dsp/streams/subscriptions
        """
        data: dict[str, Any] = {
            "dataSetId": data_set_id,
            "destinationArn": destination_arn,
        }
        if client_request_token:
            data["clientRequestToken"] = client_request_token
        if notes:
            data["notes"] = notes

        result = await self.post("/dsp/streams/subscriptions", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_dsp_subscription(self, subscription_id: str) -> JSONData:
        """获取DSP订阅详情
        
        GET /dsp/streams/subscriptions/{subscriptionId}
        """
        result = await self.get(f"/dsp/streams/subscriptions/{subscription_id}")
        return result if isinstance(result, dict) else {}

    async def update_dsp_subscription(
        self,
        subscription_id: str,
        status: str | None = None,
        notes: str | None = None,
    ) -> JSONData:
        """更新DSP订阅
        
        PUT /dsp/streams/subscriptions/{subscriptionId}
        """
        data: dict[str, Any] = {}
        if status:
            data["status"] = status
        if notes:
            data["notes"] = notes

        result = await self.put(
            f"/dsp/streams/subscriptions/{subscription_id}", json_data=data
        )
        return result if isinstance(result, dict) else {}
