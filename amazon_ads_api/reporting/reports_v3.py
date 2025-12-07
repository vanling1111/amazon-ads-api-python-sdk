"""
Reports API V3
统一报告接口（支持SP、SB、SD）
"""

import time
from ..base import BaseAdsClient, JSONData, JSONList
from loguru import logger


class ReportsV3API(BaseAdsClient):
    """Reports V3 API"""

    # ============ Report Request ============

    def create_report(
        self,
        report_type: str,
        time_unit: str,
        start_date: str,
        end_date: str,
        metrics: list[str],
        group_by: list[str] | None = None,
        filters: list[dict] | None = None,
    ) -> JSONData:
        """
        创建报告请求
        
        Args:
            report_type: 
                SP: spCampaigns, spAdGroups, spKeywords, spTargeting, spSearchTerm
                SB: sbCampaigns, sbAdGroups, sbKeywords, sbTargets
                SD: sdCampaigns, sdAdGroups, sdTargets
            time_unit: SUMMARY | DAILY
            start_date: YYYY-MM-DD
            end_date: YYYY-MM-DD
            metrics: ['impressions', 'clicks', 'cost', 'sales', ...]
            group_by: ['campaignId', 'adGroupId', ...]
            filters: [{"field": "state", "values": ["enabled"]}]
        """
        body: JSONData = {
            "startDate": start_date,
            "endDate": end_date,
            "configuration": {
                "adProduct": report_type[:2].upper(),  # SP, SB, SD
                "reportTypeId": report_type,
                "timeUnit": time_unit,
                "columns": metrics,
            }
        }

        if group_by:
            body["configuration"]["groupBy"] = group_by
        if filters:
            body["configuration"]["filters"] = filters

        result = self.post("/reporting/reports", json_data=body)
        return result if isinstance(result, dict) else {}

    def get_report_status(self, report_id: str) -> JSONData:
        """
        获取报告状态
        
        Returns:
            status: PENDING | IN_PROGRESS | COMPLETED | FAILED
        """
        result = self.get(f"/reporting/reports/{report_id}")
        return result if isinstance(result, dict) else {}

    def download_report(self, report_id: str) -> JSONList:
        """
        下载报告数据
        
        需先确认报告状态为COMPLETED
        """
        status = self.get_report_status(report_id)
        if status.get("status") != "COMPLETED":
            return []

        url = status.get("url")
        if not url:
            return []

        return super().download_report(url)

    # ============ 同步等待报告 ============

    def create_and_wait_report(
        self,
        report_type: str,
        time_unit: str,
        start_date: str,
        end_date: str,
        metrics: list[str],
        group_by: list[str] | None = None,
        filters: list[dict] | None = None,
        max_wait_seconds: int = 300,
        poll_interval: int = 10,
    ) -> JSONList:
        """
        创建报告并等待完成
        
        Args:
            max_wait_seconds: 最大等待秒数
            poll_interval: 轮询间隔秒数
        """
        # 创建报告
        result = self.create_report(
            report_type=report_type,
            time_unit=time_unit,
            start_date=start_date,
            end_date=end_date,
            metrics=metrics,
            group_by=group_by,
            filters=filters,
        )

        report_id = result.get("reportId")
        if not report_id:
            logger.error(f"Failed to create report: {result}")
            return []

        logger.info(f"Report created: {report_id}")

        # 等待完成
        elapsed = 0
        while elapsed < max_wait_seconds:
            status = self.get_report_status(report_id)
            state = status.get("status")

            if state == "COMPLETED":
                logger.info(f"Report {report_id} completed")
                return self.download_report(report_id)
            elif state == "FAILED":
                logger.error(f"Report {report_id} failed: {status}")
                return []

            logger.debug(f"Report {report_id} status: {state}")
            time.sleep(poll_interval)
            elapsed += poll_interval

        logger.warning(f"Report {report_id} timed out after {max_wait_seconds}s")
        return []

    # ============ 常用报告快捷方法 ============

    def get_campaign_performance_report(
        self,
        ad_product: str,
        start_date: str,
        end_date: str,
        time_unit: str = "DAILY",
    ) -> JSONList:
        """
        获取Campaign效果报告
        
        Args:
            ad_product: SP | SB | SD
        """
        report_type = f"{ad_product.lower()}Campaigns"
        metrics = [
            "impressions", "clicks", "cost", "purchases14d",
            "sales14d", "unitsSold14d", "dpv14d",
        ]

        return self.create_and_wait_report(
            report_type=report_type,
            time_unit=time_unit,
            start_date=start_date,
            end_date=end_date,
            metrics=metrics,
        )

    def get_keyword_performance_report(
        self,
        start_date: str,
        end_date: str,
        time_unit: str = "DAILY",
    ) -> JSONList:
        """获取SP关键词效果报告"""
        metrics = [
            "impressions", "clicks", "cost", "purchases14d",
            "sales14d", "keywordId", "keyword", "matchType",
        ]

        return self.create_and_wait_report(
            report_type="spKeywords",
            time_unit=time_unit,
            start_date=start_date,
            end_date=end_date,
            metrics=metrics,
        )

    def get_search_term_report(
        self,
        start_date: str,
        end_date: str,
        time_unit: str = "SUMMARY",
    ) -> JSONList:
        """获取搜索词报告"""
        metrics = [
            "impressions", "clicks", "cost", "purchases14d",
            "sales14d", "searchTerm", "keywordId", "keyword",
        ]

        return self.create_and_wait_report(
            report_type="spSearchTerm",
            time_unit=time_unit,
            start_date=start_date,
            end_date=end_date,
            metrics=metrics,
        )

    def get_targeting_report(
        self,
        ad_product: str,
        start_date: str,
        end_date: str,
        time_unit: str = "DAILY",
    ) -> JSONList:
        """获取定向报告"""
        report_type = f"{ad_product.lower()}Targeting" if ad_product == "SP" else f"{ad_product.lower()}Targets"
        metrics = [
            "impressions", "clicks", "cost", "purchases14d",
            "sales14d", "targetId", "targetingExpression",
        ]

        return self.create_and_wait_report(
            report_type=report_type,
            time_unit=time_unit,
            start_date=start_date,
            end_date=end_date,
            metrics=metrics,
        )

    def get_placement_report(
        self,
        start_date: str,
        end_date: str,
        time_unit: str = "DAILY",
    ) -> JSONList:
        """获取广告位报告"""
        metrics = [
            "impressions", "clicks", "cost", "purchases14d",
            "sales14d", "campaignId", "placement",
        ]

        return self.create_and_wait_report(
            report_type="spCampaigns",
            time_unit=time_unit,
            start_date=start_date,
            end_date=end_date,
            metrics=metrics,
            group_by=["placement"],
        )

    # ============ 报告可用字段 ============

    def get_report_type_configuration(self, report_type: str) -> JSONData:
        """
        获取报告类型配置
        
        返回该报告类型可用的metrics、groupBy、filters
        """
        result = self.get(f"/reporting/reportTypes/{report_type}")
        return result if isinstance(result, dict) else {}

    def list_report_types(self) -> JSONList:
        """获取所有可用的报告类型"""
        result = self.get("/reporting/reportTypes")
        return result if isinstance(result, list) else []

