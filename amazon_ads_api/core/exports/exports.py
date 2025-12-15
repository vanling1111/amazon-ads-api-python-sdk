"""
Amazon Ads Exports API (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/guides/exports/get-started
OpenAPI Spec: Exports_prod_3p.json

数据导出
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


# Content-Type 常量
AD_GROUPS_EXPORT_CONTENT_TYPE = "application/vnd.adgroupsexport.v1+json"
ADS_EXPORT_CONTENT_TYPE = "application/vnd.adsexport.v1+json"
CAMPAIGNS_EXPORT_CONTENT_TYPE = "application/vnd.campaignsexport.v1+json"
TARGETS_EXPORT_CONTENT_TYPE = "application/vnd.targetsexport.v1+json"


class ExportsAPI(BaseAdsClient):
    """
    Exports API (全异步)
    
    官方端点 (共5个):
    - POST /adGroups/export - 导出广告组
    - POST /ads/export - 导出广告
    - POST /campaigns/export - 导出活动
    - GET /exports/{exportId} - 获取导出状态
    - POST /targets/export - 导出定向
    """

    # ============ Export Creation ============

    async def export_campaigns(
        self,
        ad_product_filter: list[str] | None = None,
        state_filter: list[str] | None = None,
    ) -> JSONData:
        """
        创建 Campaigns 导出
        
        POST /campaigns/export
        
        Args:
            ad_product_filter: 广告产品过滤（默认全部）
                - SPONSORED_PRODUCTS
                - SPONSORED_BRANDS
                - SPONSORED_DISPLAY
            state_filter: 状态过滤（默认 ENABLED, PAUSED）
                - ENABLED
                - PAUSED
                - ARCHIVED
        
        Returns:
            {
                "exportId": "xxx",
                "status": "PROCESSING" | "COMPLETED" | "FAILED",
                "createdAt": "2024-01-01T00:00:00Z",
                "url": "https://..." (仅 COMPLETED 状态)
            }
        """
        body: JSONData = {}
        
        if ad_product_filter:
            body["adProductFilter"] = ad_product_filter
        if state_filter:
            body["stateFilter"] = state_filter
        
        result = await self.post(
            "/campaigns/export",
            json_data=body,
            content_type=CAMPAIGNS_EXPORT_CONTENT_TYPE,
            accept=CAMPAIGNS_EXPORT_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {}

    async def export_ad_groups(
        self,
        ad_product_filter: list[str] | None = None,
        state_filter: list[str] | None = None,
    ) -> JSONData:
        """
        创建 Ad Groups 导出
        
        POST /adGroups/export
        
        Args:
            ad_product_filter: 广告产品过滤
            state_filter: 状态过滤
        """
        body: JSONData = {}
        
        if ad_product_filter:
            body["adProductFilter"] = ad_product_filter
        if state_filter:
            body["stateFilter"] = state_filter
        
        result = await self.post(
            "/adGroups/export",
            json_data=body,
            content_type=AD_GROUPS_EXPORT_CONTENT_TYPE,
            accept=AD_GROUPS_EXPORT_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {}

    async def export_ads(
        self,
        ad_product_filter: list[str] | None = None,
        state_filter: list[str] | None = None,
    ) -> JSONData:
        """
        创建 Ads 导出
        
        POST /ads/export
        
        Args:
            ad_product_filter: 广告产品过滤
            state_filter: 状态过滤
        """
        body: JSONData = {}
        
        if ad_product_filter:
            body["adProductFilter"] = ad_product_filter
        if state_filter:
            body["stateFilter"] = state_filter
        
        result = await self.post(
            "/ads/export",
            json_data=body,
            content_type=ADS_EXPORT_CONTENT_TYPE,
            accept=ADS_EXPORT_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {}

    async def export_targets(
        self,
        ad_product_filter: list[str] | None = None,
        state_filter: list[str] | None = None,
        target_type_filter: list[str] | None = None,
        target_level_filter: list[str] | None = None,
        negative_filter: list[bool] | None = None,
    ) -> JSONData:
        """
        创建 Targets 导出
        
        POST /targets/export
        
        Args:
            ad_product_filter: 广告产品过滤
            state_filter: 状态过滤
            target_type_filter: 定向类型过滤
                - KEYWORD
                - PRODUCT
                - AUDIENCE
                - AUTO
                - THEME
                - PRODUCT_CATEGORY
                - PRODUCT_AUDIENCE
                - PRODUCT_CATEGORY_AUDIENCE
            target_level_filter: 定向级别过滤
                - AD_GROUP
                - CAMPAIGN
            negative_filter: 否定定向过滤
                - [True]: 仅否定定向
                - [False]: 仅正向定向
                - [True, False]: 两者都返回
        """
        body: JSONData = {}
        
        if ad_product_filter:
            body["adProductFilter"] = ad_product_filter
        if state_filter:
            body["stateFilter"] = state_filter
        if target_type_filter:
            body["targetTypeFilter"] = target_type_filter
        if target_level_filter:
            body["targetLevelFilter"] = target_level_filter
        if negative_filter:
            body["negativeFilter"] = negative_filter
        
        result = await self.post(
            "/targets/export",
            json_data=body,
            content_type=TARGETS_EXPORT_CONTENT_TYPE,
            accept=TARGETS_EXPORT_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {}

    # ============ Export Status ============

    async def get_export(
        self,
        export_id: str,
        export_type: str = "campaigns",
    ) -> JSONData:
        """
        获取导出状态
        
        GET /exports/{exportId}
        
        Args:
            export_id: 导出 ID
            export_type: 导出类型（用于确定 Accept header）
                - campaigns
                - adGroups
                - ads
                - targets
        
        Returns:
            {
                "exportId": "xxx",
                "status": "PROCESSING" | "COMPLETED" | "FAILED",
                "createdAt": "2024-01-01T00:00:00Z",
                "generatedAt": "2024-01-01T00:05:00Z",
                "url": "https://...",
                "urlExpiresAt": "2024-01-02T00:00:00Z",
                "fileSize": 12345,
                "error": {"errorCode": "...", "message": "..."} (仅 FAILED)
            }
        """
        content_type_map = {
            "campaigns": CAMPAIGNS_EXPORT_CONTENT_TYPE,
            "adGroups": AD_GROUPS_EXPORT_CONTENT_TYPE,
            "ads": ADS_EXPORT_CONTENT_TYPE,
            "targets": TARGETS_EXPORT_CONTENT_TYPE,
        }
        accept = content_type_map.get(export_type, CAMPAIGNS_EXPORT_CONTENT_TYPE)
        
        result = await self.get(f"/exports/{export_id}", accept=accept)
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def export_all_sp_campaigns(self) -> JSONData:
        """导出所有 SP Campaigns"""
        return await self.export_campaigns(
            ad_product_filter=["SPONSORED_PRODUCTS"]
        )

    async def export_all_sb_campaigns(self) -> JSONData:
        """导出所有 SB Campaigns"""
        return await self.export_campaigns(
            ad_product_filter=["SPONSORED_BRANDS"]
        )

    async def export_all_sd_campaigns(self) -> JSONData:
        """导出所有 SD Campaigns"""
        return await self.export_campaigns(
            ad_product_filter=["SPONSORED_DISPLAY"]
        )

    async def export_sp_keywords(self) -> JSONData:
        """导出 SP 关键词定向"""
        return await self.export_targets(
            ad_product_filter=["SPONSORED_PRODUCTS"],
            target_type_filter=["KEYWORD"]
        )

    async def export_negative_keywords(self) -> JSONData:
        """导出否定关键词"""
        return await self.export_targets(
            target_type_filter=["KEYWORD"],
            negative_filter=[True]
        )

    async def is_export_complete(self, export_id: str, export_type: str = "campaigns") -> bool:
        """检查导出是否完成"""
        result = await self.get_export(export_id, export_type)
        return result.get("status") == "COMPLETED"

    async def get_export_url(self, export_id: str, export_type: str = "campaigns") -> str | None:
        """获取导出下载 URL"""
        result = await self.get_export(export_id, export_type)
        if result.get("status") == "COMPLETED":
            return result.get("url")
        return None

    async def wait_for_export(
        self,
        export_id: str,
        export_type: str = "campaigns",
        max_wait_seconds: int = 300,
        poll_interval: int = 5,
    ) -> JSONData:
        """
        等待导出完成
        
        Args:
            export_id: 导出 ID
            export_type: 导出类型
            max_wait_seconds: 最大等待时间（秒）
            poll_interval: 轮询间隔（秒）
        
        Returns:
            导出结果（包含 url 或 error）
        """
        import asyncio
        
        elapsed = 0
        while elapsed < max_wait_seconds:
            result = await self.get_export(export_id, export_type)
            status = result.get("status")
            
            if status == "COMPLETED" or status == "FAILED":
                return result
            
            await asyncio.sleep(poll_interval)
            elapsed += poll_interval
        
        return {"status": "TIMEOUT", "exportId": export_id}
