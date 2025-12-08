"""
Amazon DSP Measurement API (异步版本)
DSP效果测量
"""

from typing import Any
from ..base import BaseAdsClient, JSONData, JSONList


class DSPMeasurementAPI(BaseAdsClient):
    """DSP Measurement API - 效果测量 (全异步)"""

    # ==================== 转化事件 ====================

    async def list_conversion_definitions(self) -> JSONList:
        """获取转化定义列表"""
        response = await self.get("/dsp/measurement/conversionDefinitions")
        if isinstance(response, dict):
            return response.get("conversionDefinitions", [])
        return []

    async def create_conversion_definition(
        self,
        name: str,
        conversion_type: str,
        attribution_window_days: int = 14,
        count_type: str = "ALL",
    ) -> JSONData:
        """创建转化定义"""
        data = {
            "name": name,
            "conversionType": conversion_type,
            "attributionWindowDays": attribution_window_days,
            "countType": count_type,
        }
        result = await self.post("/dsp/measurement/conversionDefinitions", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_conversion_definition(self, definition_id: str) -> JSONData:
        """获取转化定义详情"""
        result = await self.get(f"/dsp/measurement/conversionDefinitions/{definition_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 品牌提升研究 ====================

    async def create_brand_lift_study(
        self,
        name: str,
        order_ids: list[str],
        start_date: str,
        end_date: str,
        questions: list[dict[str, Any]],
    ) -> JSONData:
        """创建品牌提升研究"""
        data = {
            "name": name,
            "orderIds": order_ids,
            "startDate": start_date,
            "endDate": end_date,
            "questions": questions,
        }
        result = await self.post("/dsp/measurement/brandLiftStudies", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_brand_lift_study(self, study_id: str) -> JSONData:
        """获取品牌提升研究详情"""
        result = await self.get(f"/dsp/measurement/brandLiftStudies/{study_id}")
        return result if isinstance(result, dict) else {}

    async def get_brand_lift_results(self, study_id: str) -> JSONData:
        """获取品牌提升研究结果"""
        result = await self.get(f"/dsp/measurement/brandLiftStudies/{study_id}/results")
        return result if isinstance(result, dict) else {}

    # ==================== 归因报告 ====================

    async def get_attribution_report(
        self,
        order_id: str,
        start_date: str,
        end_date: str,
        granularity: str = "DAILY",
    ) -> JSONData:
        """获取归因报告"""
        params = {
            "orderId": order_id,
            "startDate": start_date,
            "endDate": end_date,
            "granularity": granularity,
        }
        result = await self.get("/dsp/measurement/attribution", params=params)
        return result if isinstance(result, dict) else {}

    # ==================== 跨渠道分析 ====================

    async def get_cross_channel_report(
        self,
        advertiser_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取跨渠道分析报告"""
        params = {
            "advertiserId": advertiser_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        result = await self.get("/dsp/measurement/crossChannel", params=params)
        return result if isinstance(result, dict) else {}
