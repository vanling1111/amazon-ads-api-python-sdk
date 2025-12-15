"""
Amazon DSP - Target KPI Recommendations API (异步版本)

官方端点 (1个):
- POST /dsp/campaigns/targetKpi/recommendations - 获取目标 KPI 推荐

官方规范: DSP_TargetKPI.json
参考文档: https://advertising.amazon.com/API/docs/en-us/dsp-campaign-api
"""

from amazon_ads_api.base import BaseAdsClient, JSONData


class DSPTargetKPIAPI(BaseAdsClient):
    """
    DSP Target KPI Recommendations API (全异步)
    
    为创建新 DSP 广告活动的广告商提供目标 KPI 推荐值。
    
    官方端点 (共1个):
    - POST /dsp/campaigns/targetKpi/recommendations
    """

    async def get_target_kpi_recommendations(
        self,
        advertiser_id: str,
        currency_code: str,
        entity_id: str,
        flight_start_date: str,
        flight_end_date: str,
        goal_kpi: str,
        advertiser_country: str | None = None,
        advertiser_industry: str | None = None,
        budget_amount: float | None = None,
    ) -> JSONData:
        """
        获取目标 KPI 推荐
        
        官方端点: POST /dsp/campaigns/targetKpi/recommendations
        官方规范: DSP_TargetKPI.json
        
        Args:
            advertiser_id: 广告商标识符 (必填)
                Example: "2622920504"
            currency_code: 用于预算的货币代码 (必填)
                Example: "JPY", "USD", "EUR"
            entity_id: 实体标识符 (必填)
                Example: "ENTITY2W3MXDBG96VM7"
            flight_start_date: 广告活动开始日期 (必填, 格式: YYYY-MM-DD)
            flight_end_date: 广告活动结束日期 (必填, 格式: YYYY-MM-DD)
            goal_kpi: 广告活动的关键绩效指标 (必填)
                Example: "CPC", "ROAS", "CPA"
            advertiser_country: 与广告商关联的国家名称 (可选)
                Example: "JP", "US"
            advertiser_industry: 广告商的行业或领域 (可选)
                Example: "Entertainment", "Electronics"
            budget_amount: 用户设置的预算金额 (可选, Pre-Budget 场景时为 null)
                Example: 100000
            
        Returns:
            {
                "currencyCode": "JPY",
                "goalKpi": "CPC",
                "modelBasedRecommendation": true,
                "recommendedKpi": {
                    "lowerBound": 2.25,
                    "upperBound": 3.75
                }
            }
        """
        body: JSONData = {
            "advertiserId": advertiser_id,
            "currencyCode": currency_code,
            "entityId": entity_id,
            "flightStartDate": flight_start_date,
            "flightEndDate": flight_end_date,
            "goalKpi": goal_kpi,
        }
        
        if advertiser_country:
            body["advertiserCountry"] = advertiser_country
        if advertiser_industry:
            body["advertiserIndustry"] = advertiser_industry
        if budget_amount is not None:
            body["budgetAmount"] = budget_amount
        
        result = await self.post(
            "/dsp/campaigns/targetKpi/recommendations",
            json_data=body,
            content_type="application/vnd.gsbtargetkpirecommendation.v1+json",
        )
        return result if isinstance(result, dict) else {}
