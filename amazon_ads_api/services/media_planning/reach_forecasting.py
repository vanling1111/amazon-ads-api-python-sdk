"""
Amazon Ads Reach Forecasting API (异步版本)

API Tier: L1
Source: OpenAPI
OpenAPI_SPEC: ReachForecasting.json
Stability: 高

官方端点 (5个):
- POST /mediaPlan/v1/reachForecasts
- POST /mediaPlan/v1/reachForecasts/list
- POST /mediaPlan/v1/reachForecasts/targets/list
- POST /mediaPlan/v1/deduplicatedReachForecasts
- POST /mediaPlan/v1/performanceForecasts
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData

# Content-Type
MEDIA_PLAN_CONTENT_TYPE = "application/vnd.mediaPlanForecastParams.v1+json"


class ReachForecastingAPI(BaseAdsClient):
    """
    Reach Forecasting API (全异步)
    
    触达预测和媒体规划服务
    
    API Tier: L1
    Source: OpenAPI
    OpenAPI_SPEC: ReachForecasting.json
    """

    async def create_reach_forecast(
        self,
        forecast_params: dict[str, Any],
    ) -> JSONData:
        """
        创建触达预测
        
        官方端点: POST /mediaPlan/v1/reachForecasts
        官方规范: ReachForecasting.json#/paths/~1mediaPlan~1v1~1reachForecasts/post
        
        Args:
            forecast_params: 预测参数，包含:
                - adProduct: 广告产品类型 (DSP, STV 等)
                - campaignInfo: 活动信息
                - targetingInfo: 定向信息
                - 等
                
        Returns:
            触达预测结果
        """
        result = await self.post(
            "/mediaPlan/v1/reachForecasts",
            json_data=forecast_params,
            content_type=MEDIA_PLAN_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    async def list_reach_forecasts(
        self,
        *,
        forecast_ids: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取触达预测列表
        
        官方端点: POST /mediaPlan/v1/reachForecasts/list
        官方规范: ReachForecasting.json#/paths/~1mediaPlan~1v1~1reachForecasts~1list/post
        
        Args:
            forecast_ids: 预测ID过滤列表
            max_results: 每页数量
            next_token: 分页令牌
            
        Returns:
            预测列表
        """
        request_body: dict[str, Any] = {"maxResults": max_results}
        
        if forecast_ids:
            request_body["forecastIdFilter"] = {"include": forecast_ids}
        if next_token:
            request_body["nextToken"] = next_token
            
        result = await self.post(
            "/mediaPlan/v1/reachForecasts/list",
            json_data=request_body,
            content_type=MEDIA_PLAN_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {"forecasts": []}

    async def list_forecast_targets(
        self,
        request_params: dict[str, Any],
    ) -> JSONData:
        """
        获取可用的预测定向选项
        
        官方端点: POST /mediaPlan/v1/reachForecasts/targets/list
        官方规范: ReachForecasting.json#/paths/~1mediaPlan~1v1~1reachForecasts~1targets~1list/post
        
        Args:
            request_params: 请求参数，包含定向类型等
            
        Returns:
            可用定向选项
        """
        result = await self.post(
            "/mediaPlan/v1/reachForecasts/targets/list",
            json_data=request_params,
            content_type=MEDIA_PLAN_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {"targets": []}

    async def create_deduplicated_reach_forecast(
        self,
        forecast_params: dict[str, Any],
    ) -> JSONData:
        """
        创建去重触达预测
        
        官方端点: POST /mediaPlan/v1/deduplicatedReachForecasts
        官方规范: ReachForecasting.json#/paths/~1mediaPlan~1v1~1deduplicatedReachForecasts/post
        
        用于跨多个广告活动或产品计算去重后的触达
        
        Args:
            forecast_params: 去重预测参数，包含多个活动的定向信息
            
        Returns:
            去重触达预测结果
        """
        result = await self.post(
            "/mediaPlan/v1/deduplicatedReachForecasts",
            json_data=forecast_params,
            content_type=MEDIA_PLAN_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    async def create_performance_forecast(
        self,
        forecast_params: dict[str, Any],
    ) -> JSONData:
        """
        创建效果预测
        
        官方端点: POST /mediaPlan/v1/performanceForecasts
        官方规范: ReachForecasting.json#/paths/~1mediaPlan~1v1~1performanceForecasts/post
        
        预测广告活动的效果指标（点击、转化等）
        
        Args:
            forecast_params: 效果预测参数
            
        Returns:
            效果预测结果
        """
        result = await self.post(
            "/mediaPlan/v1/performanceForecasts",
            json_data=forecast_params,
            content_type=MEDIA_PLAN_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}
