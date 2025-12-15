"""
Sponsored Brands - Reports v2 API (异步版本)
SB HSA 报告（旧版 v2 API）

官方文档: SponsoredBrands_v3.yaml
"""

from amazon_ads_api.base import BaseAdsClient, JSONData


class SBReportsV2API(BaseAdsClient):
    """
    SB Reports v2 API (全异步)
    
    API Tier: L1
    Source: OpenAPI
    OpenAPI_SPEC: SponsoredBrands_v3.yaml
    Stability: 高
    """

    async def request_report(
        self,
        record_type: str,
        report_date: str | None = None,
        metrics: list[str] | None = None,
        segment: str | None = None,
    ) -> JSONData:
        """
        请求创建 HSA 报告
        
        官方端点: POST /v2/hsa/{recordType}/report
        官方文档: SponsoredBrands_v3.yaml
        
        Args:
            record_type: 报告类型 (campaigns, adGroups, keywords, targets)
            report_date: 报告日期 (YYYYMMDD)
            metrics: 指标列表
            segment: 分段类型
        """
        body: JSONData = {}
        if report_date:
            body["reportDate"] = report_date
        if metrics:
            body["metrics"] = metrics
        if segment:
            body["segment"] = segment

        result = await self.post(f"/v2/hsa/{record_type}/report", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_report(self, report_id: str) -> JSONData:
        """
        获取报告状态
        
        官方端点: GET /v2/reports/{reportId}
        官方文档: SponsoredBrands_v3.yaml
        
        Args:
            report_id: 报告 ID
        """
        result = await self.get(f"/v2/reports/{report_id}")
        return result if isinstance(result, dict) else {}

    async def download_report(self, report_id: str) -> JSONData:
        """
        下载报告
        
        官方端点: GET /v2/reports/{reportId}/download
        官方文档: SponsoredBrands_v3.yaml
        
        Args:
            report_id: 报告 ID
        """
        result = await self.get(f"/v2/reports/{report_id}/download")
        return result if isinstance(result, dict) else {}

