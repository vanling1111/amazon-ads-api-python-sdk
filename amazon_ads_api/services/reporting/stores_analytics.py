"""
Amazon Ads Stores Analytics API (异步版本)
品牌旗舰店分析
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class StoresAnalyticsAPI(BaseAdsClient):
    """Stores Analytics API - 品牌旗舰店分析 (全异步)"""

    # ==================== 旗舰店列表 ====================

    async def list_stores(self, brand_entity_id: str | None = None) -> JSONList:
        """获取品牌旗舰店列表"""
        params = {}
        if brand_entity_id:
            params["brandEntityId"] = brand_entity_id

        response = await self.get("/stores", params=params if params else None)
        if isinstance(response, dict):
            return response.get("stores", [])
        return response if isinstance(response, list) else []

    async def get_store(self, store_id: str) -> JSONData:
        """获取旗舰店详情"""
        result = await self.get(f"/stores/{store_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 旗舰店页面 ====================

    async def list_store_pages(self, store_id: str) -> JSONList:
        """获取旗舰店页面列表"""
        response = await self.get(f"/stores/{store_id}/pages")
        if isinstance(response, dict):
            return response.get("pages", [])
        return []

    async def get_store_page(self, store_id: str, page_id: str) -> JSONData:
        """获取旗舰店页面详情"""
        result = await self.get(f"/stores/{store_id}/pages/{page_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 分析报告 ====================

    async def get_store_insights(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
        metrics: list[str] | None = None,
    ) -> JSONData:
        """获取旗舰店洞察数据"""
        params: dict[str, Any] = {
            "startDate": start_date,
            "endDate": end_date,
        }
        if metrics:
            params["metrics"] = ",".join(metrics)

        result = await self.get(f"/stores/{store_id}/insights", params=params)
        return result if isinstance(result, dict) else {}

    async def get_store_traffic(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
        granularity: str = "DAILY",
    ) -> JSONData:
        """获取旗舰店流量数据"""
        params = {
            "startDate": start_date,
            "endDate": end_date,
            "granularity": granularity,
        }
        result = await self.get(f"/stores/{store_id}/traffic", params=params)
        return result if isinstance(result, dict) else {}

    async def get_page_performance(
        self,
        store_id: str,
        page_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取页面性能数据"""
        params = {
            "startDate": start_date,
            "endDate": end_date,
        }
        result = await self.get(
            f"/stores/{store_id}/pages/{page_id}/performance", params=params
        )
        return result if isinstance(result, dict) else {}

    # ==================== 流量来源 ====================

    async def get_traffic_sources(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取流量来源分析"""
        params = {
            "startDate": start_date,
            "endDate": end_date,
        }
        result = await self.get(f"/stores/{store_id}/traffic/sources", params=params)
        return result if isinstance(result, dict) else {}

    async def get_search_terms(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
        max_results: int = 100,
    ) -> JSONData:
        """获取搜索词分析"""
        params = {
            "startDate": start_date,
            "endDate": end_date,
            "maxResults": max_results,
        }
        result = await self.get(f"/stores/{store_id}/searchTerms", params=params)
        return result if isinstance(result, dict) else {}
