"""
Stores API
品牌旗舰店管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class StoresAPI(BaseAdsClient):
    """Stores API"""

    # ============ Stores ============

    def list_stores(self, brand_entity_id: str | None = None) -> JSONList:
        """
        获取品牌旗舰店列表
        
        Args:
            brand_entity_id: 筛选特定品牌
        """
        params = {}
        if brand_entity_id:
            params["brandEntityId"] = brand_entity_id

        result = self.get("/stores", params=params or None)
        return result if isinstance(result, list) else []

    def get_store(self, store_id: str) -> JSONData:
        """获取旗舰店详情"""
        result = self.get(f"/stores/{store_id}")
        return result if isinstance(result, dict) else {}

    # ============ Store Pages ============

    def list_store_pages(self, store_id: str) -> JSONList:
        """获取旗舰店页面列表"""
        result = self.get(f"/stores/{store_id}/pages")
        return result if isinstance(result, list) else []

    def get_store_page(self, store_id: str, page_id: str) -> JSONData:
        """获取页面详情"""
        result = self.get(f"/stores/{store_id}/pages/{page_id}")
        return result if isinstance(result, dict) else {}

    def get_store_page_asins(self, store_id: str, page_id: str) -> JSONList:
        """获取页面上的ASIN列表"""
        result = self.get(f"/stores/{store_id}/pages/{page_id}/asins")
        return result if isinstance(result, list) else []

    # ============ Store Insights ============

    def get_store_insights(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """
        获取旗舰店洞察数据
        
        包括访问量、页面浏览、转化等
        """
        result = self.get(f"/stores/{store_id}/insights", params={
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, dict) else {}

    def get_page_insights(
        self,
        store_id: str,
        page_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取页面洞察数据"""
        result = self.get(f"/stores/{store_id}/pages/{page_id}/insights", params={
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, dict) else {}

    # ============ Store Traffic Sources ============

    def get_traffic_sources(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """
        获取旗舰店流量来源
        
        分析来自不同渠道的流量占比
        """
        result = self.get(f"/stores/{store_id}/trafficSources", params={
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, dict) else {}

    # ============ Store Visitors ============

    def get_visitor_demographics(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """
        获取访客人口统计
        
        年龄、性别、地域分布等
        """
        result = self.get(f"/stores/{store_id}/visitors/demographics", params={
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, dict) else {}

    def get_visitor_behavior(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """
        获取访客行为数据
        
        页面停留时间、跳出率等
        """
        result = self.get(f"/stores/{store_id}/visitors/behavior", params={
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    def get_store_by_brand(self, brand_entity_id: str) -> JSONData | None:
        """根据品牌获取旗舰店"""
        stores = self.list_stores(brand_entity_id)
        return stores[0] if stores else None

    def get_all_store_pages(self, store_id: str) -> JSONList:
        """获取旗舰店所有页面及其ASIN"""
        pages = self.list_store_pages(store_id)
        for page in pages:
            page["asins"] = self.get_store_page_asins(store_id, page["pageId"])
        return pages

    def get_store_performance_summary(
        self,
        store_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取旗舰店效果汇总"""
        insights = self.get_store_insights(store_id, start_date, end_date)
        traffic = self.get_traffic_sources(store_id, start_date, end_date)
        demographics = self.get_visitor_demographics(store_id, start_date, end_date)

        return {
            "insights": insights,
            "trafficSources": traffic,
            "demographics": demographics,
        }

