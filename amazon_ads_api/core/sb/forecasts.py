"""
Sponsored Brands - Forecasts API (异步版本)
SB预算和效果预测

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi
"""

from amazon_ads_api.base import BaseAdsClient, JSONData


class SBForecastsAPI(BaseAdsClient):
    """SB Forecasts API (全异步)"""

    async def get_forecasts(
        self,
        campaign_id: str,
        budget_scenarios: list[float],
        forecast_days: int = 30,
    ) -> JSONData:
        """
        获取Campaign预算效果预测
        
        Args:
            campaign_id: Campaign ID
            budget_scenarios: 预算场景列表（如 [50, 100, 200]）
            forecast_days: 预测天数
            
        Returns:
            预测结果，包含不同预算下的预期效果
        """
        result = await self.post(
            "/sb/forecasts",
            json_data={
                "campaignId": campaign_id,
                "budgetScenarios": budget_scenarios,
                "forecastDays": forecast_days
            }
        )
        return result if isinstance(result, dict) else {"forecasts": []}

    async def get_batch_forecasts(
        self,
        requests: list[dict],
    ) -> JSONData:
        """
        批量获取预测
        
        Args:
            requests: [
                {
                    "campaignId": "xxx",
                    "budgetScenarios": [50, 100, 200],
                    "forecastDays": 30
                },
                ...
            ]
        """
        result = await self.post(
            "/sb/forecasts",
            json_data={"forecastRequests": requests}
        )
        return result if isinstance(result, dict) else {"forecasts": []}

