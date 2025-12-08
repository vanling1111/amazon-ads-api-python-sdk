"""
Amazon Ads Brand Metrics API (异步版本)
品牌健康指标
"""

from typing import Any
from ..base import BaseAdsClient, JSONData, JSONList


class BrandMetricsAPI(BaseAdsClient):
    """Brand Metrics API - 品牌指标 (全异步)"""

    # ==================== 品牌指标报告 ====================

    async def create_report(
        self,
        brand_entity_id: str,
        start_date: str,
        end_date: str,
        category_ids: list[str] | None = None,
        metrics: list[str] | None = None,
    ) -> JSONData:
        """创建品牌指标报告"""
        data: dict[str, Any] = {
            "brandEntityId": brand_entity_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        if category_ids:
            data["categoryIds"] = category_ids
        if metrics:
            data["metrics"] = metrics

        result = await self.post("/brandMetrics/reports", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_report(self, report_id: str) -> JSONData:
        """获取品牌指标报告状态"""
        result = await self.get(f"/brandMetrics/reports/{report_id}")
        return result if isinstance(result, dict) else {}

    async def download_report(self, report_id: str) -> JSONData:
        """下载品牌指标报告"""
        result = await self.get(f"/brandMetrics/reports/{report_id}/download")
        return result if isinstance(result, dict) else {}

    # ==================== 品牌健康指标 ====================

    async def get_brand_awareness(
        self,
        brand_entity_id: str,
        start_date: str,
        end_date: str,
        category_id: str | None = None,
    ) -> JSONData:
        """获取品牌知名度指标"""
        params: JSONData = {
            "brandEntityId": brand_entity_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        if category_id:
            params["categoryId"] = category_id

        result = await self.get("/brandMetrics/awareness", params=params)
        return result if isinstance(result, dict) else {}

    async def get_brand_consideration(
        self,
        brand_entity_id: str,
        start_date: str,
        end_date: str,
        category_id: str | None = None,
    ) -> JSONData:
        """获取品牌考虑度指标"""
        params: JSONData = {
            "brandEntityId": brand_entity_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        if category_id:
            params["categoryId"] = category_id

        result = await self.get("/brandMetrics/consideration", params=params)
        return result if isinstance(result, dict) else {}

    async def get_brand_purchase_intent(
        self,
        brand_entity_id: str,
        start_date: str,
        end_date: str,
        category_id: str | None = None,
    ) -> JSONData:
        """获取品牌购买意向指标"""
        params: JSONData = {
            "brandEntityId": brand_entity_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        if category_id:
            params["categoryId"] = category_id

        result = await self.get("/brandMetrics/purchaseIntent", params=params)
        return result if isinstance(result, dict) else {}

    # ==================== 品牌份额 ====================

    async def get_share_of_voice(
        self,
        brand_entity_id: str,
        category_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取品牌声量份额"""
        params = {
            "brandEntityId": brand_entity_id,
            "categoryId": category_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        result = await self.get("/brandMetrics/shareOfVoice", params=params)
        return result if isinstance(result, dict) else {}

    async def get_category_benchmark(
        self,
        category_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取类目基准数据"""
        params = {
            "categoryId": category_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        result = await self.get("/brandMetrics/categoryBenchmark", params=params)
        return result if isinstance(result, dict) else {}

    # ==================== 可用类目 ====================

    async def list_available_categories(self, brand_entity_id: str) -> JSONList:
        """获取品牌可用类目列表"""
        params = {"brandEntityId": brand_entity_id}
        response = await self.get("/brandMetrics/categories", params=params)
        if isinstance(response, dict):
            return response.get("categories", [])
        return []
