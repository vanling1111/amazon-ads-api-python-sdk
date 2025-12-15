"""
Reports API V3 (异步版本)
统一报告接口（支持SP、SB、SD）
"""

import asyncio
from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList
from loguru import logger


class ReportsV3API(BaseAdsClient):
    """Reports V3 API (全异步)"""

    # ============ Report Request ============

    # adProduct 映射表
    AD_PRODUCT_MAP = {
        "sp": "SPONSORED_PRODUCTS",
        "sb": "SPONSORED_BRANDS",
        "sd": "SPONSORED_DISPLAY",
    }
    
    # 默认 groupBy 字段（必须符合 Amazon Ads API V3 规范）
    # 每种报告类型只能使用其允许的 groupBy 值
    DEFAULT_GROUP_BY = {
        # SP (Sponsored Products) - 根据官方文档
        "spCampaigns": ["campaign"],  # campaign, adGroup, campaignPlacement
        "spAdGroups": ["adGroup"],  # adGroup
        "spKeywords": ["adGroup"],  # adGroup (NOT keyword!)
        "spTargeting": ["targeting"],  # targeting
        "spSearchTerm": ["searchTerm"],  # searchTerm
        # SB (Sponsored Brands)
        "sbCampaigns": ["campaign"],
        "sbAdGroups": ["adGroup"],
        "sbKeywords": ["adGroup"],
        "sbTargets": ["targeting"],
        # SD (Sponsored Display)
        "sdCampaigns": ["campaign"],
        "sdAdGroups": ["adGroup"],
        "sdTargets": ["targeting"],
    }

    async def create_report(
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
            group_by: ['campaign', 'adGroup', 'keyword', ...]
            filters: [{"field": "state", "values": ["enabled"]}]
        """
        # 确定 adProduct
        ad_product_key = report_type[:2].lower()
        ad_product = self.AD_PRODUCT_MAP.get(ad_product_key, "SPONSORED_PRODUCTS")
        
        # 确定 groupBy（必填字段）
        effective_group_by = group_by or self.DEFAULT_GROUP_BY.get(report_type, ["campaign"])
        
        body: JSONData = {
            "startDate": start_date,
            "endDate": end_date,
            "configuration": {
                "adProduct": ad_product,
                "reportTypeId": report_type,
                "timeUnit": time_unit,
                "columns": metrics,
                "groupBy": effective_group_by,
                "format": "GZIP_JSON",
            }
        }

        if filters:
            body["configuration"]["filters"] = filters

        result = await self.post("/reporting/reports", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_report_status(self, report_id: str) -> JSONData:
        """
        获取报告状态
        
        官方端点: GET /reporting/reports/{reportId}
        
        Returns:
            status: PENDING | IN_PROGRESS | COMPLETED | FAILED
        """
        result = await self.get(f"/reporting/reports/{report_id}")
        return result if isinstance(result, dict) else {}

    async def delete_report(self, report_id: str) -> JSONData:
        """
        删除报告
        
        官方端点: DELETE /reporting/reports/{reportId}
        官方文档: OfflineReport.json
        
        Args:
            report_id: 报告ID
            
        Returns:
            删除结果
        """
        return await self.delete(f"/reporting/reports/{report_id}")

    async def download_report_data(self, report_id: str) -> JSONList:
        """
        下载报告数据
        
        需先确认报告状态为COMPLETED
        """
        status = await self.get_report_status(report_id)
        if status.get("status") != "COMPLETED":
            return []

        url = status.get("url")
        if not url:
            return []

        return await super().download_report(url)

    # ============ 异步等待报告 ============

    async def create_and_wait_report(
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
        创建报告并等待完成（异步）
        
        Args:
            max_wait_seconds: 最大等待秒数
            poll_interval: 轮询间隔秒数
        """
        # 创建报告
        result = await self.create_report(
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

        # 异步等待完成
        elapsed = 0
        while elapsed < max_wait_seconds:
            status = await self.get_report_status(report_id)
            state = status.get("status")

            if state == "COMPLETED":
                logger.info(f"Report {report_id} completed")
                return await self.download_report_data(report_id)
            elif state == "FAILED":
                logger.error(f"Report {report_id} failed: {status}")
                return []

            logger.debug(f"Report {report_id} status: {state}")
            await asyncio.sleep(poll_interval)  # 异步睡眠
            elapsed += poll_interval

        logger.warning(f"Report {report_id} timed out after {max_wait_seconds}s")
        return []

    # ============ 常用报告快捷方法 ============

    async def get_campaign_performance_report(
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

        return await self.create_and_wait_report(
            report_type=report_type,
            time_unit=time_unit,
            start_date=start_date,
            end_date=end_date,
            metrics=metrics,
        )

    async def get_keyword_performance_report(
        self,
        start_date: str,
        end_date: str,
        time_unit: str = "DAILY",
    ) -> JSONList:
        """获取SP关键词效果报告（按 adGroup 分组）"""
        # 注意：spKeywords 报告只能按 adGroup 分组
        metrics = [
            "impressions", "clicks", "cost", 
            "purchases7d", "purchases14d",
            "sales7d", "sales14d",
            "unitsSoldClicks7d", "unitsSoldClicks14d",
        ]

        return await self.create_and_wait_report(
            report_type="spKeywords",
            time_unit=time_unit,
            start_date=start_date,
            end_date=end_date,
            metrics=metrics,
            group_by=["adGroup"],  # 必须使用 adGroup
        )

    async def get_search_term_report(
        self,
        start_date: str,
        end_date: str,
        time_unit: str = "SUMMARY",
    ) -> JSONList:
        """获取搜索词报告（按 searchTerm 分组）"""
        metrics = [
            "impressions", "clicks", "cost",
            "purchases7d", "purchases14d",
            "sales7d", "sales14d",
        ]

        return await self.create_and_wait_report(
            report_type="spSearchTerm",
            time_unit=time_unit,
            start_date=start_date,
            end_date=end_date,
            metrics=metrics,
            group_by=["searchTerm"],  # 必须使用 searchTerm
        )

    async def get_targeting_report(
        self,
        ad_product: str,
        start_date: str,
        end_date: str,
        time_unit: str = "DAILY",
    ) -> JSONList:
        """获取定向报告（按 targeting 分组）"""
        report_type = f"{ad_product.lower()}Targeting" if ad_product == "SP" else f"{ad_product.lower()}Targets"
        metrics = [
            "impressions", "clicks", "cost",
            "purchases7d", "purchases14d",
            "sales7d", "sales14d",
        ]

        return await self.create_and_wait_report(
            report_type=report_type,
            time_unit=time_unit,
            start_date=start_date,
            end_date=end_date,
            metrics=metrics,
            group_by=["targeting"],  # 必须使用 targeting
        )

    async def get_placement_report(
        self,
        start_date: str,
        end_date: str,
        time_unit: str = "DAILY",
    ) -> JSONList:
        """获取广告位报告（按 campaignPlacement 分组）"""
        metrics = [
            "impressions", "clicks", "cost",
            "purchases7d", "purchases14d",
            "sales7d", "sales14d",
        ]

        return await self.create_and_wait_report(
            report_type="spCampaigns",
            time_unit=time_unit,
            start_date=start_date,
            end_date=end_date,
            metrics=metrics,
            group_by=["campaignPlacement"],  # 使用 campaignPlacement
        )

    # ============ 报告类型常量（官方文档定义） ============
    # 注意: Reports v3 API 没有 /reporting/reportTypes 端点
    # 报告类型是在 POST /reporting/reports 请求中通过 reportTypeId 指定
    
    # 可用的报告类型 (来自官方文档)
    REPORT_TYPES = {
        # Sponsored Products
        "spCampaigns": "SponsoredProductsCampaignsDailyReport",
        "spAdGroups": "SponsoredProductsAdGroupsDailyReport", 
        "spKeywords": "SponsoredProductsKeywordsDailyReport",
        "spTargeting": "SponsoredProductsTargetingDailyReport",
        "spSearchTerm": "SponsoredProductsSearchTermDailyReport",
        # Sponsored Brands
        "sbCampaigns": "SponsoredBrandsCampaignsDailyReport",
        "sbAdGroups": "SponsoredBrandsAdGroupsDailyReport",
        "sbKeywords": "SponsoredBrandsKeywordsDailyReport",
        "sbTargets": "SponsoredBrandsTargetingExpressionDailyReport",
        # Sponsored Display
        "sdCampaigns": "SponsoredDisplayCampaignsDailyReport",
        "sdAdGroups": "SponsoredDisplayAdGroupsDailyReport",
        "sdTargets": "SponsoredDisplayTargetingDailyReport",
    }
    
    def get_available_report_types(self) -> list[str]:
        """
        获取所有可用的报告类型
        
        注意: Reports v3 API 没有 /reporting/reportTypes 端点，
        此方法返回 SDK 已知的报告类型列表。
        """
        return list(self.REPORT_TYPES.keys())
