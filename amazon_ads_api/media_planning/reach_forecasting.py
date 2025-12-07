"""
Reach Forecasting API

官方文档: https://advertising.amazon.com/API/docs/en-us/guides/media-planning/reach-forecasting/overview
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/ReachPlanningService_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class ReachForecastingAPI(BaseAdsClient):
    """Reach Forecasting API - 触达预测
    
    预测广告活动的触达范围和频次。
    """
    
    # ==================== 触达预测 ====================
    
    async def get_reach_forecast(
        self,
        budget: float,
        currency: str,
        ad_products: List[str],
        targeting: Dict[str, Any],
        duration_days: int,
        frequency_cap: Optional[int] = None,
    ) -> Dict[str, Any]:
        """获取触达预测
        
        Args:
            budget: 预算金额
            currency: 货币代码
            ad_products: 广告产品列表 (SP, SB, SD, DSP)
            targeting: 定向配置
            duration_days: 投放天数
            frequency_cap: 频次上限
            
        Returns:
            触达预测结果
        """
        data = {
            "budget": budget,
            "currency": currency,
            "adProducts": ad_products,
            "targeting": targeting,
            "durationDays": duration_days,
        }
        if frequency_cap:
            data["frequencyCap"] = frequency_cap
            
        return await self._make_request(
            "POST",
            "/mediaPlanning/reach/forecast",
            json=data,
        )
    
    async def get_reach_curve(
        self,
        ad_products: List[str],
        targeting: Dict[str, Any],
        duration_days: int,
        budget_range: Dict[str, float],
    ) -> Dict[str, Any]:
        """获取触达曲线
        
        Args:
            ad_products: 广告产品列表
            targeting: 定向配置
            duration_days: 投放天数
            budget_range: 预算范围 {"min": 1000, "max": 10000}
            
        Returns:
            触达曲线数据
        """
        data = {
            "adProducts": ad_products,
            "targeting": targeting,
            "durationDays": duration_days,
            "budgetRange": budget_range,
        }
        return await self._make_request(
            "POST",
            "/mediaPlanning/reach/curve",
            json=data,
        )
    
    # ==================== 频次分析 ====================
    
    async def get_frequency_distribution(
        self,
        budget: float,
        currency: str,
        ad_products: List[str],
        targeting: Dict[str, Any],
        duration_days: int,
    ) -> Dict[str, Any]:
        """获取频次分布预测
        
        Args:
            budget: 预算金额
            currency: 货币代码
            ad_products: 广告产品列表
            targeting: 定向配置
            duration_days: 投放天数
            
        Returns:
            频次分布预测
        """
        data = {
            "budget": budget,
            "currency": currency,
            "adProducts": ad_products,
            "targeting": targeting,
            "durationDays": duration_days,
        }
        return await self._make_request(
            "POST",
            "/mediaPlanning/frequency/distribution",
            json=data,
        )
    
    # ==================== 预算建议 ====================
    
    async def get_budget_recommendation(
        self,
        target_reach: int,
        ad_products: List[str],
        targeting: Dict[str, Any],
        duration_days: int,
    ) -> Dict[str, Any]:
        """获取预算建议
        
        Args:
            target_reach: 目标触达人数
            ad_products: 广告产品列表
            targeting: 定向配置
            duration_days: 投放天数
            
        Returns:
            预算建议
        """
        data = {
            "targetReach": target_reach,
            "adProducts": ad_products,
            "targeting": targeting,
            "durationDays": duration_days,
        }
        return await self._make_request(
            "POST",
            "/mediaPlanning/budget/recommendation",
            json=data,
        )
    
    # ==================== 受众分析 ====================
    
    async def get_audience_size(
        self,
        targeting: Dict[str, Any],
    ) -> Dict[str, Any]:
        """获取受众规模
        
        Args:
            targeting: 定向配置
            
        Returns:
            受众规模估算
        """
        return await self._make_request(
            "POST",
            "/mediaPlanning/audience/size",
            json={"targeting": targeting},
        )
    
    async def get_audience_overlap(
        self,
        targeting_sets: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """获取受众重叠分析
        
        Args:
            targeting_sets: 多组定向配置
            
        Returns:
            重叠分析结果
        """
        return await self._make_request(
            "POST",
            "/mediaPlanning/audience/overlap",
            json={"targetingSets": targeting_sets},
        )
    
    # ==================== 竞价预测 ====================
    
    async def get_bid_forecast(
        self,
        ad_product: str,
        targeting: Dict[str, Any],
        budget: float,
        currency: str,
    ) -> Dict[str, Any]:
        """获取竞价预测
        
        Args:
            ad_product: 广告产品
            targeting: 定向配置
            budget: 预算
            currency: 货币代码
            
        Returns:
            竞价预测结果
        """
        data = {
            "adProduct": ad_product,
            "targeting": targeting,
            "budget": budget,
            "currency": currency,
        }
        return await self._make_request(
            "POST",
            "/mediaPlanning/bid/forecast",
            json=data,
        )

