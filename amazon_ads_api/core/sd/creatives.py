"""
Sponsored Display - Creatives API (异步版本)
SD创意管理（自定义图片、视频等）
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SDCreativesAPI(BaseAdsClient):
    """SD Creatives API (全异步)"""

    # ============ Creatives ============

    async def get_creatives(
        self,
        start_index: int = 0,
        count: int = 100,
        campaign_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
        state_filter: str | None = None,
    ) -> JSONList:
        """
        获取SD Creative列表 (v3 GET API)
        
        官方端点: GET /sd/creatives
        官方文档: SponsoredDisplay_v3.yaml
        
        Args:
            start_index: 分页起始位置
            count: 最大返回数量
            campaign_id_filter: Campaign ID 过滤
            ad_group_id_filter: Ad Group ID 过滤
            creative_id_filter: Creative ID 过滤
            state_filter: 状态过滤 (enabled, paused, archived)
        """
        params: JSONData = {"startIndex": start_index, "count": count}
        if campaign_id_filter:
            params["campaignIdFilter"] = campaign_id_filter
        if ad_group_id_filter:
            params["adGroupIdFilter"] = ad_group_id_filter
        if creative_id_filter:
            params["creativeIdFilter"] = creative_id_filter
        if state_filter:
            params["stateFilter"] = state_filter

        result = await self.get("/sd/creatives", params=params)
        return result if isinstance(result, list) else []

    async def list_creatives(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        max_results: int = 100,
    ) -> JSONData:
        """获取SD Creative列表 (POST /sd/creatives/list)"""
        params: JSONData = {"maxResults": max_results}
        if ad_group_id:
            params["adGroupIdFilter"] = [ad_group_id]
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]

        result = await self.post("/sd/creatives/list", json_data=params)
        return result if isinstance(result, dict) else {"creatives": []}

    async def get_creative(self, creative_id: str) -> JSONData:
        """获取单个Creative详情"""
        result = await self.get(f"/sd/creatives/{creative_id}")
        return result if isinstance(result, dict) else {}

    async def create_creatives(self, creatives: JSONList) -> JSONData:
        """批量创建SD Creative"""
        result = await self.post("/sd/creatives", json_data=creatives)
        return result if isinstance(result, dict) else {"creatives": {"success": [], "error": []}}

    async def update_creatives(self, creatives: JSONList) -> JSONData:
        """批量更新SD Creative"""
        result = await self.put("/sd/creatives", json_data=creatives)
        return result if isinstance(result, dict) else {"creatives": {"success": [], "error": []}}

    async def delete_creative(self, creative_id: str) -> JSONData:
        """归档Creative"""
        return await self.delete(f"/sd/creatives/{creative_id}")

    # ============ Creative Templates ============

    async def list_creative_templates(self) -> JSONList:
        """获取可用的创意模板"""
        result = await self.get("/sd/creatives/templates")
        return result if isinstance(result, list) else []

    # ============ Creative Validation ============

    async def validate_creative(self, creative: JSONData) -> JSONData:
        """验证创意是否符合要求"""
        result = await self.post("/sd/creatives/validate", json_data=creative)
        return result if isinstance(result, dict) else {}

    async def preview_creative(self, creative: JSONData) -> JSONData:
        """
        预览创意效果
        
        Args:
            creative: 创意配置（与创建相同格式）
            
        Returns:
            预览数据（HTML或图片URL）
        """
        result = await self.post("/sd/creatives/preview", json_data=creative)
        return result if isinstance(result, dict) else {}

    # ============ Custom Images ============

    async def get_image_requirements(self) -> JSONData:
        """获取自定义图片要求"""
        result = await self.get("/sd/creatives/images/requirements")
        return result if isinstance(result, dict) else {}

    # ============ Video Creatives ============

    async def get_video_requirements(self) -> JSONData:
        """获取视频创意要求"""
        result = await self.get("/sd/creatives/videos/requirements")
        return result if isinstance(result, dict) else {}

    async def get_video_status(self, video_asset_id: str) -> JSONData:
        """获取视频处理状态"""
        result = await self.get(f"/sd/creatives/videos/{video_asset_id}/status")
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def create_image_creative(
        self,
        ad_group_id: str,
        headline: str,
        brand_logo_asset_id: str,
        custom_image_asset_id: str,
    ) -> JSONData:
        """快速创建图片创意"""
        creatives = [{
            "adGroupId": ad_group_id,
            "state": "enabled",
            "creativeType": "IMAGE",
            "properties": {
                "headline": headline,
                "brandLogoAssetID": brand_logo_asset_id,
                "customImageAssetID": custom_image_asset_id,
            }
        }]
        return await self.create_creatives(creatives)

    async def create_video_creative(
        self,
        ad_group_id: str,
        video_asset_id: str,
    ) -> JSONData:
        """快速创建视频创意"""
        creatives = [{
            "adGroupId": ad_group_id,
            "state": "enabled",
            "creativeType": "VIDEO",
            "properties": {
                "videoAssetID": video_asset_id,
            }
        }]
        return await self.create_creatives(creatives)

    async def update_headline(self, creative_id: str, headline: str) -> JSONData:
        """更新创意标题"""
        return await self.update_creatives([{
            "creativeId": creative_id,
            "properties": {"headline": headline}
        }])
