"""
Sponsored Display - Reports & Snapshots API (异步版本)
SD报告和快照

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi
"""

from amazon_ads_api.base import BaseAdsClient, JSONData


class SDReportsAPI(BaseAdsClient):
    """SD Reports & Snapshots API (全异步)"""

    # ============ Reports (V2 Legacy) ============

    async def request_report(
        self,
        record_type: str,
        report_date: str | None = None,
        metrics: list[str] | None = None,
        segment: str | None = None,
        tactic: str | None = None,
    ) -> JSONData:
        """
        请求创建报告（V2 Legacy）
        
        Args:
            record_type: campaigns, adGroups, productAds, targets, asins
            report_date: 报告日期 (YYYYMMDD)
            metrics: 指标列表
            segment: 细分 (placement)
            tactic: 定向类型 (T00020, T00030, T00001)
        """
        body: JSONData = {"recordType": record_type}
        if report_date:
            body["reportDate"] = report_date
        if metrics:
            body["metrics"] = ",".join(metrics)
        if segment:
            body["segment"] = segment
        if tactic:
            body["tactic"] = tactic

        result = await self.post(f"/sd/{record_type}/report", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_report(self, report_id: str) -> JSONData:
        """获取报告状态（V2 Legacy）"""
        result = await self.get(f"/v2/reports/{report_id}")
        return result if isinstance(result, dict) else {}

    async def download_report(self, report_id: str) -> JSONData:
        """下载报告（V2 Legacy）"""
        result = await self.get(f"/v2/reports/{report_id}/download")
        return result if isinstance(result, dict) else {}

    # ============ Snapshots ============

    async def request_snapshot(
        self,
        record_type: str,
        state_filter: str | None = None,
        tactic: str | None = None,
    ) -> JSONData:
        """
        请求创建快照
        
        Args:
            record_type: campaigns, adGroups, productAds, targets, negativeTargets
            state_filter: enabled, paused, archived, pending
            tactic: 定向类型
        """
        body: JSONData = {"recordType": record_type}
        if state_filter:
            body["stateFilter"] = state_filter
        if tactic:
            body["tactic"] = tactic

        result = await self.post(f"/sd/{record_type}/snapshot", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_snapshot(self, snapshot_id: str) -> JSONData:
        """获取快照状态"""
        result = await self.get(f"/sd/snapshots/{snapshot_id}")
        return result if isinstance(result, dict) else {}

    async def download_snapshot(self, snapshot_id: str) -> bytes:
        """下载快照（返回gzip压缩的JSON）"""
        result = await self.get(f"/sd/snapshots/{snapshot_id}/download")
        return result if isinstance(result, bytes) else b""

    # ============ Creative Recommendations ============

    async def get_headline_recommendations(
        self,
        asins: list[str],
        max_results: int = 10,
    ) -> JSONData:
        """
        获取创意标题推荐
        
        Args:
            asins: ASIN列表
            max_results: 最大推荐数
        """
        result = await self.post(
            "/sd/recommendations/creative/headline",
            json_data={"asins": asins, "maxResults": max_results}
        )
        return result if isinstance(result, dict) else {"recommendations": []}

    # ============ 便捷方法 ============

    async def request_and_wait_report(
        self,
        record_type: str,
        report_date: str | None = None,
        max_wait_seconds: int = 300,
        poll_interval_seconds: int = 5,
    ) -> JSONData:
        """
        请求报告并等待完成
        
        Args:
            record_type: 记录类型
            report_date: 报告日期
            max_wait_seconds: 最大等待时间
            poll_interval_seconds: 轮询间隔
            
        Returns:
            报告下载结果
        """
        import asyncio
        
        # 请求报告
        response = await self.request_report(record_type, report_date)
        report_id = response.get("reportId")
        if not report_id:
            return {"error": "Failed to create report", "response": response}
        
        # 等待完成
        elapsed = 0
        while elapsed < max_wait_seconds:
            status = await self.get_report(report_id)
            state = status.get("status", "").upper()
            
            if state == "COMPLETED":
                return await self.download_report(report_id)
            elif state == "FAILED":
                return {"error": "Report failed", "status": status}
            
            await asyncio.sleep(poll_interval_seconds)
            elapsed += poll_interval_seconds
        
        return {"error": "Report timed out", "reportId": report_id}

