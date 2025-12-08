"""
Attribution API (异步版本)
广告归因分析
"""

from ..base import BaseAdsClient, JSONData, JSONList


class AttributionAPI(BaseAdsClient):
    """Attribution API (全异步)"""

    # ============ Publishers ============

    async def list_publishers(self) -> JSONList:
        """
        获取归因Publisher列表
        
        Publisher = 广告投放渠道
        """
        result = await self.get("/attribution/publishers")
        return result if isinstance(result, list) else []

    # ============ Advertisers ============

    async def list_advertisers(self) -> JSONList:
        """获取归因Advertiser列表"""
        result = await self.get("/attribution/advertisers")
        return result if isinstance(result, list) else []

    # ============ Attribution Tags ============

    async def list_tags(self, advertiser_id: str) -> JSONList:
        """
        获取归因标签列表
        
        Attribution Tag用于追踪站外广告效果
        """
        result = await self.get(f"/attribution/advertisers/{advertiser_id}/tags")
        return result if isinstance(result, list) else []

    async def create_tag(
        self,
        advertiser_id: str,
        name: str,
        publisher_id: str,
    ) -> JSONData:
        """创建归因标签"""
        result = await self.post(f"/attribution/advertisers/{advertiser_id}/tags", json_data={
            "name": name,
            "publisherId": publisher_id,
        })
        return result if isinstance(result, dict) else {}

    async def get_tag_macro(
        self,
        advertiser_id: str,
        tag_id: str,
        format_type: str = "CLICK",
    ) -> JSONData:
        """
        获取归因标签宏
        
        Args:
            format_type: CLICK | IMPRESSION
        """
        result = await self.get(f"/attribution/advertisers/{advertiser_id}/tags/{tag_id}/macro", params={
            "formatType": format_type
        })
        return result if isinstance(result, dict) else {}

    # ============ Attribution Reports ============

    async def create_attribution_report(
        self,
        advertiser_id: str,
        report_type: str,
        start_date: str,
        end_date: str,
        metrics: list[str],
        group_by: list[str] | None = None,
    ) -> JSONData:
        """
        创建归因报告
        
        Args:
            report_type: PERFORMANCE | PRODUCTS | GEOGRAPHIC
            metrics: [
                'Click-throughs', 'detailPageViews', 'purchases14d',
                'totalSales14d', 'totalUnits14d', 'addToCart', ...
            ]
            group_by: ['publisher', 'campaign', 'creative', ...]
        """
        body: JSONData = {
            "advertiserId": advertiser_id,
            "reportType": report_type,
            "startDate": start_date,
            "endDate": end_date,
            "metrics": metrics,
        }
        if group_by:
            body["groupBy"] = group_by

        result = await self.post("/attribution/report", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_attribution_report_status(self, report_id: str) -> JSONData:
        """获取归因报告状态"""
        result = await self.get(f"/attribution/report/{report_id}")
        return result if isinstance(result, dict) else {}

    # ============ Performance Data ============

    async def get_non_amazon_media_performance(
        self,
        advertiser_id: str,
        start_date: str,
        end_date: str,
        publisher_ids: list[str] | None = None,
    ) -> JSONData:
        """
        获取非Amazon媒体效果
        
        追踪Google、Facebook等站外广告的Amazon销售归因
        """
        body: JSONData = {
            "advertiserId": advertiser_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        if publisher_ids:
            body["publisherIds"] = publisher_ids

        result = await self.post("/attribution/performanceReport", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_product_performance(
        self,
        advertiser_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取产品归因效果"""
        result = await self.post("/attribution/productReport", json_data={
            "advertiserId": advertiser_id,
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, dict) else {}

    # ============ Conversion Path ============

    async def get_conversion_path(
        self,
        advertiser_id: str,
        start_date: str,
        end_date: str,
        path_length: int = 5,
    ) -> JSONData:
        """
        获取转化路径分析
        
        分析消费者从广告曝光到购买的完整路径
        """
        result = await self.post("/attribution/conversionPath", json_data={
            "advertiserId": advertiser_id,
            "startDate": start_date,
            "endDate": end_date,
            "pathLength": path_length,
        })
        return result if isinstance(result, dict) else {}

    # ============ Multi-Touch Attribution ============

    async def get_multi_touch_attribution(
        self,
        advertiser_id: str,
        start_date: str,
        end_date: str,
        attribution_model: str = "LINEAR",
    ) -> JSONData:
        """
        获取多触点归因分析
        
        Args:
            attribution_model: 
                - LINEAR: 线性归因（平均分配）
                - TIME_DECAY: 时间衰减
                - POSITION_BASED: 位置归因（首次+末次）
                - LAST_TOUCH: 末次触点
                - FIRST_TOUCH: 首次触点
        """
        result = await self.post("/attribution/multiTouch", json_data={
            "advertiserId": advertiser_id,
            "startDate": start_date,
            "endDate": end_date,
            "attributionModel": attribution_model,
        })
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def get_channel_performance_summary(
        self,
        advertiser_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """
        获取渠道效果汇总
        
        对比各渠道（Google、Facebook、TikTok等）的归因效果
        """
        report = await self.get_non_amazon_media_performance(
            advertiser_id=advertiser_id,
            start_date=start_date,
            end_date=end_date,
        )

        # 按Publisher汇总
        summary = {}
        for item in report.get("data", []):
            publisher = item.get("publisherName", "Unknown")
            if publisher not in summary:
                summary[publisher] = {
                    "clicks": 0,
                    "purchases": 0,
                    "sales": 0,
                }
            summary[publisher]["clicks"] += item.get("clicks", 0)
            summary[publisher]["purchases"] += item.get("purchases14d", 0)
            summary[publisher]["sales"] += item.get("totalSales14d", 0)

        return summary
