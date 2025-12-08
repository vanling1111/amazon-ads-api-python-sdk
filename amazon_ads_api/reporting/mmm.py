"""
Amazon Ads Marketing Mix Modeling (MMM) API (异步版本)
营销组合建模
"""

from typing import Any
from ..base import BaseAdsClient, JSONData, JSONList


class MarketingMixModelingAPI(BaseAdsClient):
    """Marketing Mix Modeling API (全异步)"""

    async def list_data_feeds(self) -> JSONList:
        """获取可用的MMM数据馈送列表"""
        response = await self.get("/mmm/feeds")
        if isinstance(response, dict):
            return response.get("feeds", [])
        return []

    async def create_data_feed(
        self,
        name: str,
        start_date: str,
        end_date: str,
        granularity: str = "DAILY",
        dimensions: list[str] | None = None,
        metrics: list[str] | None = None,
    ) -> JSONData:
        """创建MMM数据馈送请求"""
        data: dict[str, Any] = {
            "name": name,
            "startDate": start_date,
            "endDate": end_date,
            "granularity": granularity,
        }
        if dimensions:
            data["dimensions"] = dimensions
        if metrics:
            data["metrics"] = metrics

        result = await self.post("/mmm/feeds", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_data_feed(self, feed_id: str) -> JSONData:
        """获取数据馈送状态"""
        result = await self.get(f"/mmm/feeds/{feed_id}")
        return result if isinstance(result, dict) else {}

    async def download_data_feed(self, feed_id: str) -> JSONData:
        """下载数据馈送文件"""
        result = await self.get(f"/mmm/feeds/{feed_id}/download")
        return result if isinstance(result, dict) else {}

    async def get_available_dimensions(self) -> JSONList:
        """获取可用维度列表"""
        response = await self.get("/mmm/dimensions")
        if isinstance(response, dict):
            return response.get("dimensions", [])
        return []

    async def get_available_metrics(self) -> JSONList:
        """获取可用指标列表"""
        response = await self.get("/mmm/metrics")
        if isinstance(response, dict):
            return response.get("metrics", [])
        return []

    async def validate_feed_request(
        self,
        start_date: str,
        end_date: str,
        dimensions: list[str],
        metrics: list[str],
    ) -> JSONData:
        """验证数据馈送请求"""
        data = {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": dimensions,
            "metrics": metrics,
        }
        result = await self.post("/mmm/feeds/validate", json_data=data)
        return result if isinstance(result, dict) else {}
