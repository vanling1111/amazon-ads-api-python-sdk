"""
Stores API (异步版本)
品牌旗舰店管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class StoresAPI(BaseAdsClient):
    """Stores API (全异步)"""

    # ============ Stores ============

    async def list_stores(self, brand_entity_id: str | None = None) -> JSONList:
        """获取品牌旗舰店列表"""
        params = {}
        if brand_entity_id:
            params["brandEntityId"] = brand_entity_id

        result = await self.get("/stores", params=params or None)
        return result if isinstance(result, list) else []

    async def get_store(self, store_id: str) -> JSONData:
        """获取旗舰店详情"""
        result = await self.get(f"/stores/{store_id}")
        return result if isinstance(result, dict) else {}

    # ============ Store Pages ============

    async def list_store_pages(self, store_id: str) -> JSONList:
        """获取旗舰店页面列表"""
        result = await self.get(f"/stores/{store_id}/pages")
        return result if isinstance(result, list) else []

    async def get_store_page(self, store_id: str, page_id: str) -> JSONData:
        """获取页面详情"""
        result = await self.get(f"/stores/{store_id}/pages/{page_id}")
        return result if isinstance(result, dict) else {}

    async def get_store_page_asins(self, store_id: str, page_id: str) -> JSONList:
        """获取页面上的ASIN列表"""
        result = await self.get(f"/stores/{store_id}/pages/{page_id}/asins")
        return result if isinstance(result, list) else []

    # ============ Store Insights ============

    async def get_store_insights(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取旗舰店洞察数据"""
        result = await self.get(f"/stores/{store_id}/insights", params={
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, dict) else {}

    async def get_page_insights(
        self,
        store_id: str,
        page_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取页面洞察数据"""
        result = await self.get(f"/stores/{store_id}/pages/{page_id}/insights", params={
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, dict) else {}

    # ============ Store Traffic Sources ============

    async def get_traffic_sources(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取旗舰店流量来源"""
        result = await self.get(f"/stores/{store_id}/trafficSources", params={
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, dict) else {}

    # ============ Store Visitors ============

    async def get_visitor_demographics(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取访客人口统计"""
        result = await self.get(f"/stores/{store_id}/visitors/demographics", params={
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, dict) else {}

    async def get_visitor_behavior(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取访客行为数据"""
        result = await self.get(f"/stores/{store_id}/visitors/behavior", params={
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def get_store_by_brand(self, brand_entity_id: str) -> JSONData | None:
        """根据品牌获取旗舰店"""
        stores = await self.list_stores(brand_entity_id)
        return stores[0] if stores else None

    async def get_all_store_pages(self, store_id: str) -> JSONList:
        """获取旗舰店所有页面及其ASIN"""
        pages = await self.list_store_pages(store_id)
        for page in pages:
            page["asins"] = await self.get_store_page_asins(store_id, page["pageId"])
        return pages

    async def get_store_performance_summary(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取旗舰店效果汇总"""
        insights = await self.get_store_insights(store_id, start_date, end_date)
        traffic = await self.get_traffic_sources(store_id, start_date, end_date)
        demographics = await self.get_visitor_demographics(store_id, start_date, end_date)

        return {
            "insights": insights,
            "trafficSources": traffic,
            "demographics": demographics,
        }
