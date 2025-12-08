"""
Amazon Ads Reach Forecasting API (异步版本)
触达预测
"""

from typing import Any
from ..base import BaseAdsClient, JSONData


class ReachForecastingAPI(BaseAdsClient):
    """Reach Forecasting API (全异步)"""

    # ==================== 触达预测 ====================

    async def get_reach_forecast(
        self,
        budget: float,
        currency: str,
        ad_products: list[str],
        targeting: dict[str, Any],
        duration_days: int,
        frequency_cap: int | None = None,
    ) -> JSONData:
        """获取触达预测"""
        data: dict[str, Any] = {
            "budget": budget,
            "currency": currency,
            "adProducts": ad_products,
            "targeting": targeting,
            "durationDays": duration_days,
        }
        if frequency_cap:
            data["frequencyCap"] = frequency_cap

        result = await self.post("/mediaPlanning/reach/forecast", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_reach_curve(
        self,
        ad_products: list[str],
        targeting: dict[str, Any],
        duration_days: int,
        budget_range: dict[str, float],
    ) -> JSONData:
        """获取触达曲线"""
        data = {
            "adProducts": ad_products,
            "targeting": targeting,
            "durationDays": duration_days,
            "budgetRange": budget_range,
        }
        result = await self.post("/mediaPlanning/reach/curve", json_data=data)
        return result if isinstance(result, dict) else {}

    # ==================== 频次分析 ====================

    async def get_frequency_distribution(
        self,
        budget: float,
        currency: str,
        ad_products: list[str],
        targeting: dict[str, Any],
        duration_days: int,
    ) -> JSONData:
        """获取频次分布预测"""
        data = {
            "budget": budget,
            "currency": currency,
            "adProducts": ad_products,
            "targeting": targeting,
            "durationDays": duration_days,
        }
        result = await self.post("/mediaPlanning/frequency/distribution", json_data=data)
        return result if isinstance(result, dict) else {}

    # ==================== 预算建议 ====================

    async def get_budget_recommendation(
        self,
        target_reach: int,
        ad_products: list[str],
        targeting: dict[str, Any],
        duration_days: int,
    ) -> JSONData:
        """获取预算建议"""
        data = {
            "targetReach": target_reach,
            "adProducts": ad_products,
            "targeting": targeting,
            "durationDays": duration_days,
        }
        result = await self.post("/mediaPlanning/budget/recommendation", json_data=data)
        return result if isinstance(result, dict) else {}

    # ==================== 受众分析 ====================

    async def get_audience_size(self, targeting: dict[str, Any]) -> JSONData:
        """获取受众规模"""
        result = await self.post("/mediaPlanning/audience/size", json_data={"targeting": targeting})
        return result if isinstance(result, dict) else {}

    async def get_audience_overlap(
        self,
        targeting_sets: list[dict[str, Any]],
    ) -> JSONData:
        """获取受众重叠分析"""
        result = await self.post(
            "/mediaPlanning/audience/overlap", json_data={"targetingSets": targeting_sets}
        )
        return result if isinstance(result, dict) else {}

    # ==================== 竞价预测 ====================

    async def get_bid_forecast(
        self,
        ad_product: str,
        targeting: dict[str, Any],
        budget: float,
        currency: str,
    ) -> JSONData:
        """获取竞价预测"""
        data = {
            "adProduct": ad_product,
            "targeting": targeting,
            "budget": budget,
            "currency": currency,
        }
        result = await self.post("/mediaPlanning/bid/forecast", json_data=data)
        return result if isinstance(result, dict) else {}
