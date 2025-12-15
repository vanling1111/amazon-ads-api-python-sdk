"""
Sponsored Brands - Media API (异步版本)
SB媒体上传管理

官方文档: SponsoredBrands_v3.yaml
"""

from amazon_ads_api.base import BaseAdsClient, JSONData


class SBMediaAPI(BaseAdsClient):
    """
    SB Media API (全异步)
    
    API Tier: L1
    Source: OpenAPI
    OpenAPI_SPEC: SponsoredBrands_v3.yaml
    Stability: 高
    """

    async def complete_upload(self, media_id: str, upload_location: str) -> JSONData:
        """
        通知媒体上传完成
        
        官方端点: PUT /media/complete
        官方文档: SponsoredBrands_v3.yaml
        
        Args:
            media_id: 媒体 ID
            upload_location: 上传位置
        """
        body: JSONData = {
            "mediaId": media_id,
            "uploadLocation": upload_location,
        }
        result = await self.put("/media/complete", json_data=body)
        return result if isinstance(result, dict) else {}

    async def describe_media(self, media_id: str) -> JSONData:
        """
        轮询媒体状态
        
        官方端点: GET /media/describe
        官方文档: SponsoredBrands_v3.yaml
        
        Args:
            media_id: 媒体 ID
        """
        params = {"mediaId": media_id}
        result = await self.get("/media/describe", params=params)
        return result if isinstance(result, dict) else {}

