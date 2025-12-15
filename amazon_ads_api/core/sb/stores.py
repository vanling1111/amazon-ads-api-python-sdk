"""
Sponsored Brands - Stores API (异步版本)
SB品牌旗舰店资产管理

官方文档: SponsoredBrands_v3.yaml
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SBStoresAPI(BaseAdsClient):
    """
    SB Stores API (全异步)
    
    API Tier: L1
    Source: OpenAPI
    OpenAPI_SPEC: SponsoredBrands_v3.yaml
    Stability: 高
    """

    async def list_assets(
        self,
        brand_entity_id: str,
        media_type: str | None = None,
    ) -> JSONData:
        """
        获取品牌旗舰店资产列表
        
        官方端点: GET /stores/assets
        官方文档: SponsoredBrands_v3.yaml
        
        Args:
            brand_entity_id: 品牌实体 ID
            media_type: 媒体类型过滤
        """
        params: JSONData = {"brandEntityId": brand_entity_id}
        if media_type:
            params["mediaType"] = media_type

        result = await self.get("/stores/assets", params=params)
        return result if isinstance(result, dict) else {"assets": []}

    async def create_asset(
        self,
        brand_entity_id: str,
        media_type: str,
        url: str,
        name: str | None = None,
    ) -> JSONData:
        """
        创建新的图片资产
        
        官方端点: POST /stores/assets
        官方文档: SponsoredBrands_v3.yaml
        
        Args:
            brand_entity_id: 品牌实体 ID
            media_type: 媒体类型
            url: 图片 URL
            name: 资产名称
        """
        body: JSONData = {
            "brandEntityId": brand_entity_id,
            "mediaType": media_type,
            "url": url,
        }
        if name:
            body["name"] = name

        result = await self.post("/stores/assets", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_page_asins(
        self,
        page_url: str,
    ) -> JSONData:
        """
        获取指定页面的 ASIN 信息
        
        官方端点: GET /pageAsins
        官方文档: SponsoredBrands_v3.yaml
        
        Args:
            page_url: 页面 URL
        """
        params = {"pageUrl": page_url}
        result = await self.get("/pageAsins", params=params)
        return result if isinstance(result, dict) else {"asins": []}

