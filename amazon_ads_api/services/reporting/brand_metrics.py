"""
Brand Metrics API (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/brand-metrics
官方端点: 2个
- POST /insights/brandMetrics/report (创建报告)
- GET /insights/brandMetrics/report/{reportId} (获取报告)
"""

from typing import Literal
from amazon_ads_api.base import BaseAdsClient, JSONData


# 报告类型
ReportType = Literal[
    "BRAND_AWARENESS",
    "BRANDED_SEARCH",
    "MARKET_BASKET",
    "NEW_TO_BRAND",
    "REPEAT_PURCHASE",
]

# 时间粒度
Granularity = Literal["DAY", "WEEK", "MONTH"]


class BrandMetricsAPI(BaseAdsClient):
    """
    Brand Metrics API (全异步)
    
    官方只有 2 个端点:
    - POST /insights/brandMetrics/report (创建报告)
    - GET /insights/brandMetrics/report/{reportId} (获取报告状态/下载)
    """

    async def create_report(
        self,
        *,
        advertiser_id: str,
        brand_entity_id: str,
        report_type: ReportType,
        start_date: str,
        end_date: str,
        category_node_ids: list[str] | None = None,
        granularity: Granularity = "WEEK",
        marketplace_ids: list[str] | None = None,
    ) -> JSONData:
        """
        创建品牌指标报告
        
        官方端点: POST /insights/brandMetrics/report
        
        Args:
            advertiser_id: 广告主ID
            brand_entity_id: 品牌实体ID
            report_type: 报告类型
                - BRAND_AWARENESS: 品牌知名度
                - BRANDED_SEARCH: 品牌搜索
                - MARKET_BASKET: 购物篮分析
                - NEW_TO_BRAND: 新客户
                - REPEAT_PURCHASE: 复购
            start_date: 开始日期 (YYYY-MM-DD)
            end_date: 结束日期 (YYYY-MM-DD)
            category_node_ids: 类目节点ID列表
            granularity: 时间粒度 (DAY, WEEK, MONTH)
            marketplace_ids: 市场ID列表
            
        Returns:
            {
                "reportId": "...",
                "status": "PENDING"
            }
        """
        body: JSONData = {
            "advertiserId": advertiser_id,
            "brandEntityId": brand_entity_id,
            "reportType": report_type,
            "startDate": start_date,
            "endDate": end_date,
            "granularity": granularity,
        }
        
        if category_node_ids:
            body["categoryNodeIds"] = category_node_ids
        if marketplace_ids:
            body["marketplaceIds"] = marketplace_ids

        result = await self.post("/insights/brandMetrics/report", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_report(self, report_id: str) -> JSONData:
        """
        获取品牌指标报告状态/下载
        
        官方端点: GET /insights/brandMetrics/report/{reportId}
        
        Args:
            report_id: 报告ID
            
        Returns:
            报告状态为 PENDING/PROCESSING 时:
            {
                "reportId": "...",
                "status": "PROCESSING"
            }
            
            报告状态为 COMPLETED 时:
            {
                "reportId": "...",
                "status": "COMPLETED",
                "url": "https://...",  # 下载URL
                "expiration": "..."
            }
        """
        result = await self.get(f"/insights/brandMetrics/report/{report_id}")
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def create_and_wait_report(
        self,
        *,
        advertiser_id: str,
        brand_entity_id: str,
        report_type: ReportType,
        start_date: str,
        end_date: str,
        timeout_seconds: int = 300,
        poll_interval: int = 10,
        **kwargs,
    ) -> JSONData:
        """
        创建报告并等待完成
        
        Args:
            timeout_seconds: 超时时间（秒）
            poll_interval: 轮询间隔（秒）
            **kwargs: 其他 create_report 参数
            
        Returns:
            完成的报告（包含下载URL）
        """
        import asyncio
        
        # 创建报告
        result = await self.create_report(
            advertiser_id=advertiser_id,
            brand_entity_id=brand_entity_id,
            report_type=report_type,
            start_date=start_date,
            end_date=end_date,
            **kwargs,
        )
        
        report_id = result.get("reportId")
        if not report_id:
            return result
        
        # 轮询等待
        elapsed = 0
        while elapsed < timeout_seconds:
            await asyncio.sleep(poll_interval)
            elapsed += poll_interval
            
            status = await self.get_report(report_id)
            if status.get("status") == "COMPLETED":
                return status
            if status.get("status") == "FAILED":
                return status
        
        return {"reportId": report_id, "status": "TIMEOUT"}
