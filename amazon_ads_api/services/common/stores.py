"""
Amazon Stores API (异步版本)

官方端点 (2个):
- POST /stores/{brandEntityId}/asinMetrics - 获取 ASIN 指标
- POST /stores/{brandEntityId}/insights - 获取旗舰店洞察

官方规范: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Stores_prod_3p.json
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class StoresAPI(BaseAdsClient):
    """
    Amazon Stores API (全异步)
    
    用于获取品牌旗舰店的洞察和 ASIN 指标数据。
    """

    async def get_asin_metrics(
        self,
        brand_entity_id: str,
        start_date: str,
        end_date: str,
        asins: list[str] | None = None,
        **kwargs,
    ) -> JSONData:
        """
        获取 ASIN 指标
        
        官方端点: POST /stores/{brandEntityId}/asinMetrics
        
        Args:
            brand_entity_id: 品牌实体 ID
            start_date: 开始日期 (YYYY-MM-DD)
            end_date: 结束日期 (YYYY-MM-DD)
            asins: ASIN 列表（可选，不指定则返回所有）
            **kwargs: 其他可选参数
            
        Returns:
            ASIN 指标数据
        """
        body: JSONData = {
            "startDate": start_date,
            "endDate": end_date,
        }
        
        if asins:
            body["asins"] = asins
            
        body.update(kwargs)
        
        result = await self.post(
            f"/stores/{brand_entity_id}/asinMetrics",
            json_data=body
        )
        return result if isinstance(result, dict) else {}

    async def get_insights(
        self,
        brand_entity_id: str,
        start_date: str,
        end_date: str,
        **kwargs,
    ) -> JSONData:
        """
        获取旗舰店洞察
        
        官方端点: POST /stores/{brandEntityId}/insights
        
        Args:
            brand_entity_id: 品牌实体 ID
            start_date: 开始日期 (YYYY-MM-DD)
            end_date: 结束日期 (YYYY-MM-DD)
            **kwargs: 其他可选参数
            
        Returns:
            旗舰店洞察数据，包括访客、浏览量、销售等
        """
        body: JSONData = {
            "startDate": start_date,
            "endDate": end_date,
        }
        
        body.update(kwargs)
        
        result = await self.post(
            f"/stores/{brand_entity_id}/insights",
            json_data=body
        )
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def get_store_performance(
        self,
        brand_entity_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """
        获取旗舰店综合表现
        
        同时获取洞察和 ASIN 指标
        
        Args:
            brand_entity_id: 品牌实体 ID
            start_date: 开始日期
            end_date: 结束日期
            
        Returns:
            综合表现数据
        """
        insights = await self.get_insights(brand_entity_id, start_date, end_date)
        asin_metrics = await self.get_asin_metrics(brand_entity_id, start_date, end_date)
        
        return {
            "insights": insights,
            "asinMetrics": asin_metrics,
        }
