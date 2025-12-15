"""
Amazon Attribution API (异步版本)

官方端点 (5个):
- GET /attribution/advertisers - 获取广告主列表
- GET /attribution/publishers - 获取发布商列表  
- POST /attribution/report - 创建归因报告
- GET /attribution/tags/macroTag - 获取宏标签
- GET /attribution/tags/nonMacroTemplateTag - 获取非宏模板标签

官方规范: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/AmazonAttribution_prod_3p.json
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class AttributionAPI(BaseAdsClient):
    """
    Amazon Attribution API (全异步)
    
    用于追踪非 Amazon 广告（如 Google、Facebook）对 Amazon 销售的归因效果。
    """

    async def list_advertisers(self) -> JSONList:
        """
        获取归因广告主列表
        
        官方端点: GET /attribution/advertisers
        
        Returns:
            广告主列表
        """
        result = await self.get("/attribution/advertisers")
        return result if isinstance(result, list) else []

    async def list_publishers(self) -> JSONList:
        """
        获取发布商列表
        
        官方端点: GET /attribution/publishers
        
        发布商代表广告投放渠道（如 Google、Facebook、TikTok 等）
        
        Returns:
            发布商列表
        """
        result = await self.get("/attribution/publishers")
        return result if isinstance(result, list) else []

    async def create_report(
        self,
        report_type: str,
        start_date: str,
        end_date: str,
        metrics: list[str] | None = None,
        group_by: list[str] | None = None,
        advertiser_ids: list[str] | None = None,
        **kwargs,
    ) -> JSONData:
        """
        创建归因报告
        
        官方端点: POST /attribution/report
        
        Args:
            report_type: 报告类型 (PERFORMANCE, PRODUCTS, GEOGRAPHIC)
            start_date: 开始日期 (YYYY-MM-DD)
            end_date: 结束日期 (YYYY-MM-DD)
            metrics: 指标列表 [
                'Click-throughs', 'detailPageViews', 'purchases14d',
                'totalSales14d', 'totalUnits14d', 'addToCart', ...
            ]
            group_by: 分组维度 ['publisher', 'campaign', 'creative', ...]
            advertiser_ids: 广告主 ID 列表
            **kwargs: 其他可选参数
            
        Returns:
            报告创建结果
        """
        body: JSONData = {
            "reportType": report_type,
            "startDate": start_date,
            "endDate": end_date,
        }
        
        if metrics:
            body["metrics"] = metrics
        if group_by:
            body["groupBy"] = group_by
        if advertiser_ids:
            body["advertiserIds"] = advertiser_ids
            
        body.update(kwargs)
        
        result = await self.post("/attribution/report", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_macro_tag(self) -> JSONData:
        """
        获取宏标签
        
        官方端点: GET /attribution/tags/macroTag
        
        宏标签用于支持动态参数的广告平台（如 Google Ads）
        
        Returns:
            宏标签详情
        """
        result = await self.get("/attribution/tags/macroTag")
        return result if isinstance(result, dict) else {}

    async def get_non_macro_template_tag(self) -> JSONData:
        """
        获取非宏模板标签
        
        官方端点: GET /attribution/tags/nonMacroTemplateTag
        
        非宏模板标签用于不支持动态参数的广告平台
        
        Returns:
            非宏模板标签详情
        """
        result = await self.get("/attribution/tags/nonMacroTemplateTag")
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def get_advertiser_by_name(self, name: str) -> JSONData | None:
        """
        根据名称获取广告主
        
        Args:
            name: 广告主名称
            
        Returns:
            匹配的广告主，未找到返回 None
        """
        advertisers = await self.list_advertisers()
        for adv in advertisers:
            if adv.get("name") == name:
                return adv
        return None

    async def get_publisher_by_name(self, name: str) -> JSONData | None:
        """
        根据名称获取发布商
        
        Args:
            name: 发布商名称
            
        Returns:
            匹配的发布商，未找到返回 None
        """
        publishers = await self.list_publishers()
        for pub in publishers:
            if pub.get("name") == name:
                return pub
        return None
