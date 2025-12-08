"""
Amazon DSP Target KPI Recommendations API (异步版本)
DSP目标KPI建议
"""

from ..base import BaseAdsClient, JSONData


class DSPTargetKPIAPI(BaseAdsClient):
    """DSP Target KPI Recommendations API (全异步)"""

    async def get_target_kpi_recommendations(
        self,
        order_id: str,
        kpi_type: str,
    ) -> JSONData:
        """获取目标KPI建议"""
        params = {
            "orderId": order_id,
            "kpiType": kpi_type,
        }
        result = await self.get("/dsp/targetKpi/recommendations", params=params)
        return result if isinstance(result, dict) else {}

    async def get_line_item_kpi_recommendations(
        self,
        line_item_id: str,
        kpi_type: str,
    ) -> JSONData:
        """获取Line Item的KPI建议"""
        params = {
            "lineItemId": line_item_id,
            "kpiType": kpi_type,
        }
        result = await self.get("/dsp/targetKpi/lineItem/recommendations", params=params)
        return result if isinstance(result, dict) else {}

    async def apply_kpi_recommendation(
        self,
        order_id: str,
        recommendation_id: str,
    ) -> JSONData:
        """应用KPI建议"""
        data = {
            "orderId": order_id,
            "recommendationId": recommendation_id,
        }
        result = await self.post("/dsp/targetKpi/apply", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_kpi_forecast(
        self,
        order_id: str,
        target_kpi: float,
        kpi_type: str,
    ) -> JSONData:
        """获取KPI预测"""
        params = {
            "orderId": order_id,
            "targetKpi": target_kpi,
            "kpiType": kpi_type,
        }
        result = await self.get("/dsp/targetKpi/forecast", params=params)
        return result if isinstance(result, dict) else {}

    async def get_kpi_history(
        self,
        order_id: str,
        kpi_type: str,
        start_date: str,
        end_date: str,
        granularity: str = "DAILY",
    ) -> JSONData:
        """获取KPI历史数据"""
        params = {
            "orderId": order_id,
            "kpiType": kpi_type,
            "startDate": start_date,
            "endDate": end_date,
            "granularity": granularity,
        }
        result = await self.get("/dsp/targetKpi/history", params=params)
        return result if isinstance(result, dict) else {}

    async def get_kpi_benchmark(
        self,
        industry: str,
        kpi_type: str,
    ) -> JSONData:
        """获取行业KPI基准"""
        params = {
            "industry": industry,
            "kpiType": kpi_type,
        }
        result = await self.get("/dsp/targetKpi/benchmark", params=params)
        return result if isinstance(result, dict) else {}
