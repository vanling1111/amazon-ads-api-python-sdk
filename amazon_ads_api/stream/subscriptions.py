"""
Amazon Marketing Stream Subscriptions API

官方文档: https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/overview
OpenAPI: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/AmazonMarketingStream_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class MarketingStreamAPI(BaseAdsClient):
    """Amazon Marketing Stream API - 营销数据流
    
    管理实时营销数据流订阅。
    """
    
    # ==================== 订阅管理 ====================
    
    async def list_subscriptions(self) -> List[Dict[str, Any]]:
        """获取订阅列表
        
        Returns:
            订阅列表
        """
        response = await self._make_request(
            "GET",
            "/streams/subscriptions",
        )
        return response.get("subscriptions", [])
    
    async def create_subscription(
        self,
        data_set_id: str,
        destination_arn: str,
        client_request_token: Optional[str] = None,
        notes: Optional[str] = None,
    ) -> Dict[str, Any]:
        """创建订阅
        
        Args:
            data_set_id: 数据集ID (SP_TRAFFIC, SP_CONVERSION, etc.)
            destination_arn: 目标SQS队列或SNS主题ARN
            client_request_token: 客户端请求令牌（幂等性）
            notes: 备注
            
        Returns:
            创建的订阅
        """
        data = {
            "dataSetId": data_set_id,
            "destinationArn": destination_arn,
        }
        if client_request_token:
            data["clientRequestToken"] = client_request_token
        if notes:
            data["notes"] = notes
            
        return await self._make_request(
            "POST",
            "/streams/subscriptions",
            json=data,
        )
    
    async def get_subscription(
        self,
        subscription_id: str,
    ) -> Dict[str, Any]:
        """获取订阅详情
        
        Args:
            subscription_id: 订阅ID
            
        Returns:
            订阅详情
        """
        return await self._make_request(
            "GET",
            f"/streams/subscriptions/{subscription_id}",
        )
    
    async def update_subscription(
        self,
        subscription_id: str,
        status: Optional[str] = None,
        notes: Optional[str] = None,
    ) -> Dict[str, Any]:
        """更新订阅
        
        Args:
            subscription_id: 订阅ID
            status: 状态 (ACTIVE, PAUSED)
            notes: 备注
            
        Returns:
            更新后的订阅
        """
        data = {}
        if status:
            data["status"] = status
        if notes:
            data["notes"] = notes
            
        return await self._make_request(
            "PUT",
            f"/streams/subscriptions/{subscription_id}",
            json=data,
        )
    
    async def delete_subscription(
        self,
        subscription_id: str,
    ) -> None:
        """删除订阅
        
        Args:
            subscription_id: 订阅ID
        """
        await self._make_request(
            "DELETE",
            f"/streams/subscriptions/{subscription_id}",
        )
    
    # ==================== 数据集 ====================
    
    async def list_data_sets(self) -> List[Dict[str, Any]]:
        """获取可用数据集列表
        
        Returns:
            数据集列表
        """
        response = await self._make_request(
            "GET",
            "/streams/dataSets",
        )
        return response.get("dataSets", [])
    
    async def get_data_set_schema(
        self,
        data_set_id: str,
    ) -> Dict[str, Any]:
        """获取数据集模式
        
        Args:
            data_set_id: 数据集ID
            
        Returns:
            数据集模式
        """
        return await self._make_request(
            "GET",
            f"/streams/dataSets/{data_set_id}/schema",
        )
    
    # ==================== 目标配置 ====================
    
    async def validate_destination(
        self,
        destination_arn: str,
    ) -> Dict[str, Any]:
        """验证目标配置
        
        Args:
            destination_arn: 目标ARN
            
        Returns:
            验证结果
        """
        data = {"destinationArn": destination_arn}
        return await self._make_request(
            "POST",
            "/streams/destinations/validate",
            json=data,
        )
    
    # ==================== 消息处理 ====================
    
    async def get_sample_messages(
        self,
        data_set_id: str,
        count: int = 10,
    ) -> List[Dict[str, Any]]:
        """获取示例消息
        
        Args:
            data_set_id: 数据集ID
            count: 消息数量
            
        Returns:
            示例消息列表
        """
        params = {
            "dataSetId": data_set_id,
            "count": count,
        }
        response = await self._make_request(
            "GET",
            "/streams/samples",
            params=params,
        )
        return response.get("messages", [])

