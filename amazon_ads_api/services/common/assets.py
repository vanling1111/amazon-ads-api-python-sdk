"""
Creative Asset Library API (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/creative-asset-library
官方端点: 6个
"""

from typing import Literal, BinaryIO
from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


# 资产类型
AssetType = Literal[
    "IMAGE",
    "VIDEO", 
    "BRANDLOGO",
]

# 资产子类型
AssetSubType = Literal[
    "LOGO",
    "BACKGROUND",
    "LIFESTYLE",
    "PRODUCT",
    "OTHER",
]


class AssetsAPI(BaseAdsClient):
    """
    Creative Asset Library API (全异步)
    
    官方端点:
    - GET /assets (列表)
    - POST /assets/register (注册单个)
    - POST /assets/batchRegister (批量注册)
    - GET /assets/batchRegister/{requestId} (批量注册状态)
    - POST /assets/upload (上传)
    - POST /assets/search (搜索)
    """

    # ============ 列表资产 ============

    async def list_assets(
        self,
        *,
        asset_type: AssetType | None = None,
        asset_sub_type_list: list[AssetSubType] | None = None,
        asset_id_list: list[str] | None = None,
        media_type: str | None = None,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取资产列表
        
        官方端点: GET /assets
        
        Args:
            asset_type: 资产类型 (IMAGE, VIDEO, BRANDLOGO)
            asset_sub_type_list: 子类型列表
            asset_id_list: 资产ID列表
            media_type: 媒体类型 (image/jpeg, video/mp4 等)
            next_token: 分页令牌
            
        Returns:
            {
                "assets": [...],
                "nextToken": "..."
            }
        """
        params: JSONData = {}
        if asset_type:
            params["assetType"] = asset_type
        if asset_sub_type_list:
            params["assetSubTypeList"] = ",".join(asset_sub_type_list)
        if asset_id_list:
            params["assetIdList"] = ",".join(asset_id_list)
        if media_type:
            params["mediaType"] = media_type
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/assets", params=params or None)
        return result if isinstance(result, dict) else {"assets": []}

    # ============ 注册资产 ============

    async def register_asset(
        self,
        *,
        url: str,
        asset_type: AssetType = "IMAGE",
        asset_sub_type: AssetSubType | None = None,
        name: str | None = None,
        associated_sub_entity_list: list[JSONData] | None = None,
    ) -> JSONData:
        """
        注册单个资产（从URL）
        
        官方端点: POST /assets/register
        
        Args:
            url: 资产URL (必须是可公开访问的URL)
            asset_type: 资产类型
            asset_sub_type: 子类型
            name: 资产名称
            associated_sub_entity_list: 关联实体列表
            
        Returns:
            {
                "assetId": "...",
                "status": "PROCESSING",
                ...
            }
        """
        body: JSONData = {
            "url": url,
            "assetType": asset_type,
        }
        if asset_sub_type:
            body["assetSubType"] = asset_sub_type
        if name:
            body["name"] = name
        if associated_sub_entity_list:
            body["associatedSubEntityList"] = associated_sub_entity_list

        result = await self.post("/assets/register", json_data=body)
        return result if isinstance(result, dict) else {}

    async def batch_register_assets(
        self,
        assets: list[JSONData],
    ) -> JSONData:
        """
        批量注册资产
        
        官方端点: POST /assets/batchRegister
        
        Args:
            assets: 资产列表，每个资产包含:
                - url: 资产URL
                - assetType: 类型
                - assetSubType: 子类型 (可选)
                - name: 名称 (可选)
                
        Returns:
            {
                "requestId": "...",
                "status": "PROCESSING"
            }
        """
        result = await self.post("/assets/batchRegister", json_data={"assets": assets})
        return result if isinstance(result, dict) else {}

    async def get_batch_register_status(self, request_id: str) -> JSONData:
        """
        获取批量注册状态
        
        官方端点: GET /assets/batchRegister/{requestId}
        
        Args:
            request_id: 批量注册请求ID
            
        Returns:
            {
                "requestId": "...",
                "status": "COMPLETED",
                "assets": [...]
            }
        """
        result = await self.get(f"/assets/batchRegister/{request_id}")
        return result if isinstance(result, dict) else {}

    # ============ 上传资产 ============

    async def upload_asset(
        self,
        *,
        file_content: bytes,
        file_name: str,
        content_type: str,
        asset_type: AssetType = "IMAGE",
        asset_sub_type: AssetSubType | None = None,
    ) -> JSONData:
        """
        直接上传资产文件
        
        官方端点: POST /assets/upload
        
        Args:
            file_content: 文件内容 (bytes)
            file_name: 文件名
            content_type: MIME类型 (image/jpeg, image/png, video/mp4)
            asset_type: 资产类型
            asset_sub_type: 子类型
            
        Returns:
            {
                "assetId": "...",
                "status": "...",
                ...
            }
            
        Note:
            此方法使用 multipart/form-data 上传。
            对于大文件，建议使用 register_asset 从URL注册。
        """
        # 构建 multipart 数据
        # 注意：实际实现可能需要使用 aiohttp 的 FormData
        body: JSONData = {
            "assetType": asset_type,
        }
        if asset_sub_type:
            body["assetSubType"] = asset_sub_type

        # 这里需要特殊处理 multipart 上传
        # 具体实现取决于 BaseAdsClient 的能力
        result = await self.post(
            "/assets/upload",
            json_data=body,
            # TODO: 需要支持 multipart/form-data 上传
        )
        return result if isinstance(result, dict) else {}

    # ============ 搜索资产 ============

    async def search_assets(
        self,
        *,
        asset_type: AssetType | None = None,
        asset_sub_type_list: list[AssetSubType] | None = None,
        name_filter: str | None = None,
        associated_sub_entity_list: list[JSONData] | None = None,
        next_token: str | None = None,
    ) -> JSONData:
        """
        搜索资产
        
        官方端点: POST /assets/search
        
        Args:
            asset_type: 资产类型
            asset_sub_type_list: 子类型列表
            name_filter: 名称过滤（模糊匹配）
            associated_sub_entity_list: 关联实体过滤
            next_token: 分页令牌
            
        Returns:
            {
                "assets": [...],
                "nextToken": "..."
            }
        """
        body: JSONData = {}
        if asset_type:
            body["assetType"] = asset_type
        if asset_sub_type_list:
            body["assetSubTypeList"] = asset_sub_type_list
        if name_filter:
            body["nameFilter"] = name_filter
        if associated_sub_entity_list:
            body["associatedSubEntityList"] = associated_sub_entity_list
        if next_token:
            body["nextToken"] = next_token

        result = await self.post("/assets/search", json_data=body or None)
        return result if isinstance(result, dict) else {"assets": []}

    # ============ 便捷方法 ============

    async def get_asset_by_id(self, asset_id: str) -> JSONData | None:
        """
        根据ID获取资产
        
        通过 list_assets 实现（官方无单独获取端点）
        """
        result = await self.list_assets(asset_id_list=[asset_id])
        assets = result.get("assets", [])
        return assets[0] if assets else None

    async def list_all_assets(
        self,
        asset_type: AssetType | None = None,
    ) -> JSONList:
        """
        获取所有资产（自动分页）
        """
        all_assets: JSONList = []
        next_token = None

        while True:
            result = await self.list_assets(
                asset_type=asset_type,
                next_token=next_token,
            )
            assets = result.get("assets", [])
            all_assets.extend(assets)

            next_token = result.get("nextToken")
            if not next_token or not assets:
                break

        return all_assets

    async def get_images(self) -> JSONList:
        """获取所有图片资产"""
        return await self.list_all_assets(asset_type="IMAGE")

    async def get_videos(self) -> JSONList:
        """获取所有视频资产"""
        return await self.list_all_assets(asset_type="VIDEO")

    async def get_brand_logos(self) -> JSONList:
        """获取所有品牌Logo"""
        return await self.list_all_assets(asset_type="BRANDLOGO")
