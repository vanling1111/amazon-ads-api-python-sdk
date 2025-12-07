"""
Amazon DSP Measurement API

官方文档: https://advertising.amazon.com/API/docs/en-us/dsp
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Measurement_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class DSPMeasurementAPI(BaseAdsClient):
    """DSP Measurement API - 效果测量
    
    测量DSP广告的效果和ROI。
    """
    
    # ==================== 转化事件 ====================
    
    async def list_conversion_definitions(self) -> List[Dict[str, Any]]:
        """获取转化定义列表
        
        Returns:
            转化定义列表
        """
        response = await self._make_request(
            "GET",
            "/dsp/measurement/conversionDefinitions",
        )
        return response.get("conversionDefinitions", [])
    
    async def create_conversion_definition(
        self,
        name: str,
        conversion_type: str,
        attribution_window_days: int = 14,
        count_type: str = "ALL",
    ) -> Dict[str, Any]:
        """创建转化定义
        
        Args:
            name: 转化名称
            conversion_type: 转化类型 (PURCHASE, ADD_TO_CART, PAGE_VIEW, etc.)
            attribution_window_days: 归因窗口天数
            count_type: 计数类型 (ALL, UNIQUE)
            
        Returns:
            创建的转化定义
        """
        data = {
            "name": name,
            "conversionType": conversion_type,
            "attributionWindowDays": attribution_window_days,
            "countType": count_type,
        }
        return await self._make_request(
            "POST",
            "/dsp/measurement/conversionDefinitions",
            json=data,
        )
    
    async def get_conversion_definition(
        self,
        definition_id: str,
    ) -> Dict[str, Any]:
        """获取转化定义详情
        
        Args:
            definition_id: 转化定义ID
            
        Returns:
            转化定义详情
        """
        return await self._make_request(
            "GET",
            f"/dsp/measurement/conversionDefinitions/{definition_id}",
        )
    
    # ==================== 品牌提升研究 ====================
    
    async def create_brand_lift_study(
        self,
        name: str,
        order_ids: List[str],
        start_date: str,
        end_date: str,
        questions: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """创建品牌提升研究
        
        Args:
            name: 研究名称
            order_ids: 关联的Order ID列表
            start_date: 开始日期
            end_date: 结束日期
            questions: 调查问题列表
            
        Returns:
            创建的品牌提升研究
        """
        data = {
            "name": name,
            "orderIds": order_ids,
            "startDate": start_date,
            "endDate": end_date,
            "questions": questions,
        }
        return await self._make_request(
            "POST",
            "/dsp/measurement/brandLiftStudies",
            json=data,
        )
    
    async def get_brand_lift_study(
        self,
        study_id: str,
    ) -> Dict[str, Any]:
        """获取品牌提升研究详情
        
        Args:
            study_id: 研究ID
            
        Returns:
            研究详情
        """
        return await self._make_request(
            "GET",
            f"/dsp/measurement/brandLiftStudies/{study_id}",
        )
    
    async def get_brand_lift_results(
        self,
        study_id: str,
    ) -> Dict[str, Any]:
        """获取品牌提升研究结果
        
        Args:
            study_id: 研究ID
            
        Returns:
            研究结果
        """
        return await self._make_request(
            "GET",
            f"/dsp/measurement/brandLiftStudies/{study_id}/results",
        )
    
    # ==================== 归因报告 ====================
    
    async def get_attribution_report(
        self,
        order_id: str,
        start_date: str,
        end_date: str,
        granularity: str = "DAILY",
    ) -> Dict[str, Any]:
        """获取归因报告
        
        Args:
            order_id: Order ID
            start_date: 开始日期
            end_date: 结束日期
            granularity: 时间粒度 (DAILY, WEEKLY)
            
        Returns:
            归因报告数据
        """
        params = {
            "orderId": order_id,
            "startDate": start_date,
            "endDate": end_date,
            "granularity": granularity,
        }
        return await self._make_request(
            "GET",
            "/dsp/measurement/attribution",
            params=params,
        )
    
    # ==================== 跨渠道分析 ====================
    
    async def get_cross_channel_report(
        self,
        advertiser_id: str,
        start_date: str,
        end_date: str,
    ) -> Dict[str, Any]:
        """获取跨渠道分析报告
        
        Args:
            advertiser_id: 广告商ID
            start_date: 开始日期
            end_date: 结束日期
            
        Returns:
            跨渠道分析数据
        """
        params = {
            "advertiserId": advertiser_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        return await self._make_request(
            "GET",
            "/dsp/measurement/crossChannel",
            params=params,
        )

