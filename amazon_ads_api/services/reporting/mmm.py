"""
Amazon Ads Marketing Mix Modeling (MMM) API (异步版本)
营销组合建模

官方端点 (共10个):
- POST /mmm/v1/brandGroupOverrides - 创建品牌组覆盖
- POST /mmm/v1/brandGroupOverrides/delete - 删除品牌组覆盖
- POST /mmm/v1/brandGroupOverrides/list - 列出品牌组覆盖
- POST /mmm/v1/brandGroups/list - 列出品牌组
- GET /mmm/v1/brandGroups/{brandGroupId}/campaigns - 获取品牌组活动
- GET /mmm/v1/brandGroups/{brandGroupId}/products - 获取品牌组产品
- POST /mmm/v1/reports - 创建报告
- POST /mmm/v1/reports/list - 列出报告
- GET /mmm/v1/reports/{reportId} - 获取报告
- DELETE /mmm/v1/reports/{reportId} - 删除报告

官方规范: MMM.json
参考文档: https://advertising.amazon.com/API/docs/en-us/mmm
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class MarketingMixModelingAPI(BaseAdsClient):
    """
    Marketing Mix Modeling (MMM) API (全异步)
    
    用于请求包含聚合 Amazon 销售和媒体表现信号的报告，
    用于营销组合建模 (MMM)。
    
    官方端点 (共10个):
    - Brand Groups: 2个
    - Brand Group Overrides: 3个
    - Reports: 5个
    
    注意: 需要 Amazon-Advertising-API-Manager-Account header
    """

    # ==================== Brand Groups ====================

    async def list_brand_groups(
        self,
        brand_group_id_filter: list[str] | None = None,
        country_code_filter: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        列出品牌组
        
        POST /mmm/v1/brandGroups/list
        
        Args:
            brand_group_id_filter: 只列出这些ID的品牌组
            country_code_filter: 只列出这些国家代码的品牌组 (ISO 3166)
            max_results: 每页记录数 (1-100, 默认100)
            next_token: 分页令牌
            
        Returns:
            包含 brandGroups 数组和可选 nextToken 的字典
        """
        body: dict[str, Any] = {}
        
        if brand_group_id_filter:
            body["brandGroupIdFilter"] = {"include": brand_group_id_filter}
        if country_code_filter:
            body["countryCodeFilter"] = {"include": country_code_filter}
        if max_results != 100:
            body["maxResults"] = max_results
        if next_token:
            body["nextToken"] = next_token
            
        result = await self.post("/mmm/v1/brandGroups/list", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_brand_group_campaigns(
        self,
        brand_group_id: str,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取品牌组的活动列表
        
        GET /mmm/v1/brandGroups/{brandGroupId}/campaigns
        
        返回与品牌组产品关联的活动列表（最近3年内）。
        
        Args:
            brand_group_id: 品牌组ID
            max_results: 每页记录数 (1-100)
            next_token: 分页令牌
            
        Returns:
            包含 campaigns 数组和可选 nextToken 的字典
        """
        params: dict[str, Any] = {}
        if max_results != 100:
            params["maxResults"] = max_results
        if next_token:
            params["nextToken"] = next_token
            
        result = await self.get(
            f"/mmm/v1/brandGroups/{brand_group_id}/campaigns",
            params=params
        )
        return result if isinstance(result, dict) else {}

    async def get_brand_group_products(
        self,
        brand_group_id: str,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取品牌组的产品列表
        
        GET /mmm/v1/brandGroups/{brandGroupId}/products
        
        返回品牌组的产品列表（最近3年内销售的）。
        
        Args:
            brand_group_id: 品牌组ID
            max_results: 每页记录数 (1-100)
            next_token: 分页令牌
            
        Returns:
            包含 products 数组和可选 nextToken 的字典
        """
        params: dict[str, Any] = {}
        if max_results != 100:
            params["maxResults"] = max_results
        if next_token:
            params["nextToken"] = next_token
            
        result = await self.get(
            f"/mmm/v1/brandGroups/{brand_group_id}/products",
            params=params
        )
        return result if isinstance(result, dict) else {}

    # ==================== Brand Group Overrides ====================

    async def create_brand_group_overrides(
        self,
        overrides: list[dict],
    ) -> JSONData:
        """
        创建品牌组覆盖
        
        POST /mmm/v1/brandGroupOverrides
        
        覆盖强制品牌组包含或排除特定产品或活动。
        
        Args:
            overrides: 覆盖列表，每个包含:
                - brandGroupId: 品牌组ID
                - identifierType: "ASIN" 或 "CAMPAIGN_ID"
                - identifierValue: ASIN 或活动ID
                - overrideType: "INCLUDE" 或 "EXCLUDE"
                
        Returns:
            包含 success 和 error 数组的字典
            
        Example:
            await api.create_brand_group_overrides([
                {
                    "brandGroupId": "xxx",
                    "identifierType": "ASIN",
                    "identifierValue": "B0018OFKJS",
                    "overrideType": "INCLUDE"
                }
            ])
        """
        body = {"overrides": overrides}
        result = await self.post("/mmm/v1/brandGroupOverrides", json_data=body)
        return result if isinstance(result, dict) else {}

    async def list_brand_group_overrides(
        self,
        brand_group_id_filter: list[str] | None = None,
        override_id_filter: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        列出品牌组覆盖
        
        POST /mmm/v1/brandGroupOverrides/list
        
        Args:
            brand_group_id_filter: 只列出这些品牌组的覆盖
            override_id_filter: 只列出这些ID的覆盖
            max_results: 每页记录数 (1-100)
            next_token: 分页令牌
            
        Returns:
            包含 overrides 数组和可选 nextToken 的字典
        """
        body: dict[str, Any] = {}
        
        if brand_group_id_filter:
            body["brandGroupIdFilter"] = {"include": brand_group_id_filter}
        if override_id_filter:
            body["overrideIdFilter"] = {"include": override_id_filter}
        if max_results != 100:
            body["maxResults"] = max_results
        if next_token:
            body["nextToken"] = next_token
            
        result = await self.post("/mmm/v1/brandGroupOverrides/list", json_data=body)
        return result if isinstance(result, dict) else {}

    async def delete_brand_group_overrides(
        self,
        override_ids: list[str],
    ) -> JSONData:
        """
        删除品牌组覆盖
        
        POST /mmm/v1/brandGroupOverrides/delete
        
        Args:
            override_ids: 要删除的覆盖ID列表
            
        Returns:
            包含 success 和 error 数组的字典
        """
        body = {
            "overrideIdFilter": {"include": override_ids}
        }
        result = await self.post("/mmm/v1/brandGroupOverrides/delete", json_data=body)
        return result if isinstance(result, dict) else {}

    # ==================== Reports ====================

    async def create_report(
        self,
        brand_group_id: str,
        start_date: str,
        end_date: str,
        geo_dimension: str,
        metrics_type: str,
        time_unit: str,
        report_name: str | None = None,
        description: str | None = None,
        due_date: str | None = None,
    ) -> JSONData:
        """
        创建 MMM 报告
        
        POST /mmm/v1/reports
        
        Args:
            brand_group_id: 品牌组ID
            start_date: 报告开始日期 (YYYY-MM-DD)
                - 当 time_unit=WEEKLY 时必须是周日或周一
            end_date: 报告结束日期 (YYYY-MM-DD)
                - 当 time_unit=WEEKLY 时必须是周六或周日
            geo_dimension: 地理粒度
                - COUNTRY: 按国家聚合
                - POSTAL_CODE: 按邮政编码聚合（仅部分国家）
                - DMA: 按 DMA 区域聚合（仅美国）
            metrics_type: 指标类型
                - MEDIA_ONLY: 仅广告指标
                - MEDIA_AND_SALES: 广告和零售指标
            time_unit: 时间粒度
                - DAILY: 每日粒度
                - WEEKLY: 每周粒度
            report_name: 报告显示名称
            description: 报告描述
            due_date: 截止日期 (用于优先级)
            
        Returns:
            创建的报告详情，包含 reportId 和 status
        """
        body: dict[str, Any] = {
            "configuration": {
                "brandGroupId": brand_group_id,
                "geoDimension": geo_dimension,
                "metricsType": metrics_type,
                "timeUnit": time_unit,
            },
            "startDate": start_date,
            "endDate": end_date,
        }
        
        if report_name:
            body["reportName"] = report_name
        if description:
            body["description"] = description
        if due_date:
            body["dueDate"] = due_date
            
        result = await self.post("/mmm/v1/reports", json_data=body)
        return result if isinstance(result, dict) else {}

    async def list_reports(
        self,
        report_id_filter: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        列出报告
        
        POST /mmm/v1/reports/list
        
        Args:
            report_id_filter: 只列出这些ID的报告
            max_results: 每页记录数 (1-100)
            next_token: 分页令牌
            
        Returns:
            包含 reports 数组和可选 nextToken 的字典
        """
        body: dict[str, Any] = {}
        
        if report_id_filter:
            body["reportIdFilter"] = {"include": report_id_filter}
        if max_results != 100:
            body["maxResults"] = max_results
        if next_token:
            body["nextToken"] = next_token
            
        result = await self.post("/mmm/v1/reports/list", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_report(self, report_id: str) -> JSONData:
        """
        获取报告状态
        
        GET /mmm/v1/reports/{reportId}
        
        Args:
            report_id: 报告ID
            
        Returns:
            报告详情，包含:
            - status: PENDING, PROCESSING, SUCCEEDED, FAILED, CANCELED
            - urls: 下载URL（status=SUCCEEDED时）
            - failureCode/failureMessage: 失败原因（status=FAILED时）
        """
        result = await self.get(f"/mmm/v1/reports/{report_id}")
        return result if isinstance(result, dict) else {}

    async def delete_report(self, report_id: str) -> bool:
        """
        删除报告
        
        DELETE /mmm/v1/reports/{reportId}
        
        用于取消或清理报告。
        
        Args:
            report_id: 报告ID
            
        Returns:
            成功返回 True
        """
        await self.delete(f"/mmm/v1/reports/{report_id}")
        return True

    # ==================== 便捷方法 ====================

    async def wait_for_report(
        self,
        report_id: str,
        max_wait_seconds: int = 86400,
        poll_interval_seconds: int = 60,
    ) -> JSONData:
        """
        等待报告完成
        
        轮询报告状态直到完成或超时。
        
        Args:
            report_id: 报告ID
            max_wait_seconds: 最大等待时间（默认24小时）
            poll_interval_seconds: 轮询间隔（默认60秒）
            
        Returns:
            最终报告状态
            
        Raises:
            TimeoutError: 超时
            RuntimeError: 报告失败
        """
        import asyncio
        
        elapsed = 0
        while elapsed < max_wait_seconds:
            report = await self.get_report(report_id)
            status = report.get("status", "")
            
            if status == "SUCCEEDED":
                return report
            elif status == "FAILED":
                failure_code = report.get("failureCode", "UNKNOWN")
                failure_message = report.get("failureMessage", "Unknown error")
                raise RuntimeError(f"Report failed: {failure_code} - {failure_message}")
            elif status == "CANCELED":
                raise RuntimeError("Report was canceled")
            
            await asyncio.sleep(poll_interval_seconds)
            elapsed += poll_interval_seconds
            
        raise TimeoutError(f"Report did not complete within {max_wait_seconds} seconds")
