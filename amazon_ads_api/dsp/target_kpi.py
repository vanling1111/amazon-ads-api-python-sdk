"""
Amazon DSP Target KPI Recommendations API

官方文档: https://advertising.amazon.com/API/docs/en-us/dsp
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/GoalSeekingBidderTargetKPIRecommendation_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class DSPTargetKPIAPI(BaseAdsClient):
    """DSP Target KPI Recommendations API - 目标KPI建议
    
    获取DSP广告活动的目标KPI优化建议。
    """
    
    # ==================== KPI建议 ====================
    
    async def get_target_kpi_recommendations(
        self,
        order_id: str,
        kpi_type: str,
    ) -> Dict[str, Any]:
        """获取目标KPI建议
        
        Args:
            order_id: Order ID
            kpi_type: KPI类型 (ROAS, CPA, CTR, VCR, etc.)
            
        Returns:
            KPI建议
        """
        params = {
            "orderId": order_id,
            "kpiType": kpi_type,
        }
        return await self._make_request(
            "GET",
            "/dsp/targetKpi/recommendations",
            params=params,
        )
    
    async def get_line_item_kpi_recommendations(
        self,
        line_item_id: str,
        kpi_type: str,
    ) -> Dict[str, Any]:
        """获取Line Item的KPI建议
        
        Args:
            line_item_id: Line Item ID
            kpi_type: KPI类型
            
        Returns:
            KPI建议
        """
        params = {
            "lineItemId": line_item_id,
            "kpiType": kpi_type,
        }
        return await self._make_request(
            "GET",
            "/dsp/targetKpi/lineItem/recommendations",
            params=params,
        )
    
    # ==================== KPI优化 ====================
    
    async def apply_kpi_recommendation(
        self,
        order_id: str,
        recommendation_id: str,
    ) -> Dict[str, Any]:
        """应用KPI建议
        
        Args:
            order_id: Order ID
            recommendation_id: 建议ID
            
        Returns:
            应用结果
        """
        data = {
            "orderId": order_id,
            "recommendationId": recommendation_id,
        }
        return await self._make_request(
            "POST",
            "/dsp/targetKpi/apply",
            json=data,
        )
    
    async def get_kpi_forecast(
        self,
        order_id: str,
        target_kpi: float,
        kpi_type: str,
    ) -> Dict[str, Any]:
        """获取KPI预测
        
        Args:
            order_id: Order ID
            target_kpi: 目标KPI值
            kpi_type: KPI类型
            
        Returns:
            KPI预测结果
        """
        params = {
            "orderId": order_id,
            "targetKpi": target_kpi,
            "kpiType": kpi_type,
        }
        return await self._make_request(
            "GET",
            "/dsp/targetKpi/forecast",
            params=params,
        )
    
    # ==================== 历史KPI分析 ====================
    
    async def get_kpi_history(
        self,
        order_id: str,
        kpi_type: str,
        start_date: str,
        end_date: str,
        granularity: str = "DAILY",
    ) -> Dict[str, Any]:
        """获取KPI历史数据
        
        Args:
            order_id: Order ID
            kpi_type: KPI类型
            start_date: 开始日期
            end_date: 结束日期
            granularity: 时间粒度 (HOURLY, DAILY, WEEKLY)
            
        Returns:
            KPI历史数据
        """
        params = {
            "orderId": order_id,
            "kpiType": kpi_type,
            "startDate": start_date,
            "endDate": end_date,
            "granularity": granularity,
        }
        return await self._make_request(
            "GET",
            "/dsp/targetKpi/history",
            params=params,
        )
    
    async def get_kpi_benchmark(
        self,
        industry: str,
        kpi_type: str,
    ) -> Dict[str, Any]:
        """获取行业KPI基准
        
        Args:
            industry: 行业类别
            kpi_type: KPI类型
            
        Returns:
            行业基准数据
        """
        params = {
            "industry": industry,
            "kpiType": kpi_type,
        }
        return await self._make_request(
            "GET",
            "/dsp/targetKpi/benchmark",
            params=params,
        )

