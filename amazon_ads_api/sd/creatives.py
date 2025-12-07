"""
Sponsored Display - Creatives API
SD创意管理（自定义图片、视频等）
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SDCreativesAPI(BaseAdsClient):
    """SD Creatives API"""

    # ============ Creatives ============

    def list_creatives(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        max_results: int = 100,
    ) -> JSONData:
        """获取SD Creative列表"""
        params: JSONData = {"maxResults": max_results}
        if ad_group_id:
            params["adGroupIdFilter"] = [ad_group_id]
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]

        result = self.post("/sd/creatives/list", json_data=params)
        return result if isinstance(result, dict) else {"creatives": []}

    def get_creative(self, creative_id: str) -> JSONData:
        """获取单个Creative详情"""
        result = self.get(f"/sd/creatives/{creative_id}")
        return result if isinstance(result, dict) else {}

    def create_creatives(self, creatives: JSONList) -> JSONData:
        """
        批量创建SD Creative
        
        Args:
            creatives: [
                {
                    "adGroupId": "xxx",
                    "state": "enabled",
                    "creativeType": "IMAGE",  # IMAGE | VIDEO
                    "properties": {
                        "headline": "Shop Now",
                        "brandLogoAssetID": "xxx",
                        "customImageAssetID": "xxx"
                    }
                }
            ]
        """
        result = self.post("/sd/creatives", json_data=creatives)
        return result if isinstance(result, dict) else {"creatives": {"success": [], "error": []}}

    def update_creatives(self, creatives: JSONList) -> JSONData:
        """批量更新SD Creative"""
        result = self.put("/sd/creatives", json_data=creatives)
        return result if isinstance(result, dict) else {"creatives": {"success": [], "error": []}}

    def delete_creative(self, creative_id: str) -> JSONData:
        """归档Creative"""
        return self.delete(f"/sd/creatives/{creative_id}")

    # ============ Creative Templates ============

    def list_creative_templates(self) -> JSONList:
        """获取可用的创意模板"""
        result = self.get("/sd/creatives/templates")
        return result if isinstance(result, list) else []

    # ============ Creative Validation ============

    def validate_creative(self, creative: JSONData) -> JSONData:
        """
        验证创意是否符合要求
        
        在创建前验证图片尺寸、格式等
        """
        result = self.post("/sd/creatives/validate", json_data=creative)
        return result if isinstance(result, dict) else {}

    # ============ Custom Images ============

    def get_image_requirements(self) -> JSONData:
        """
        获取自定义图片要求
        
        返回支持的尺寸、格式等
        """
        result = self.get("/sd/creatives/images/requirements")
        return result if isinstance(result, dict) else {}

    # ============ Video Creatives ============

    def get_video_requirements(self) -> JSONData:
        """
        获取视频创意要求
        
        返回支持的时长、分辨率等
        """
        result = self.get("/sd/creatives/videos/requirements")
        return result if isinstance(result, dict) else {}

    def get_video_status(self, video_asset_id: str) -> JSONData:
        """获取视频处理状态"""
        result = self.get(f"/sd/creatives/videos/{video_asset_id}/status")
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    def create_image_creative(
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
        return self.create_creatives(creatives)

    def create_video_creative(
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
        return self.create_creatives(creatives)

    def update_headline(self, creative_id: str, headline: str) -> JSONData:
        """更新创意标题"""
        return self.update_creatives([{
            "creativeId": creative_id,
            "properties": {"headline": headline}
        }])

