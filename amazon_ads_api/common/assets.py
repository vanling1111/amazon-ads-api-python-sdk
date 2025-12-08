"""
Assets API (异步版本)
创意资产管理（图片、视频、Logo等）
"""

from ..base import BaseAdsClient, JSONData, JSONList


class AssetsAPI(BaseAdsClient):
    """Assets API (全异步)"""

    # ============ Assets ============

    async def list_assets(
        self,
        asset_type: str | None = None,
        state: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取资产列表"""
        params: JSONData = {"maxResults": max_results}
        if asset_type:
            params["assetType"] = asset_type
        if state:
            params["state"] = state
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/assets", params=params)
        return result if isinstance(result, dict) else {"assets": []}

    async def get_asset(self, asset_id: str) -> JSONData:
        """获取资产详情"""
        result = await self.get(f"/assets/{asset_id}")
        return result if isinstance(result, dict) else {}

    # ============ Upload Assets ============

    async def register_asset(
        self,
        asset_type: str,
        name: str,
        content_type: str,
    ) -> JSONData:
        """注册资产（获取上传URL）"""
        result = await self.post("/assets/register", json_data={
            "assetType": asset_type,
            "name": name,
            "contentType": content_type,
        })
        return result if isinstance(result, dict) else {}

    async def complete_asset_upload(self, asset_id: str) -> JSONData:
        """完成资产上传"""
        result = await self.post(f"/assets/{asset_id}/complete")
        return result if isinstance(result, dict) else {}

    # ============ Asset Versions ============

    async def list_asset_versions(self, asset_id: str) -> JSONList:
        """获取资产版本列表"""
        result = await self.get(f"/assets/{asset_id}/versions")
        return result if isinstance(result, list) else []

    async def get_asset_version(self, asset_id: str, version_id: str) -> JSONData:
        """获取特定版本详情"""
        result = await self.get(f"/assets/{asset_id}/versions/{version_id}")
        return result if isinstance(result, dict) else {}

    # ============ Asset Validation ============

    async def validate_image(
        self,
        asset_id: str,
        use_case: str,
    ) -> JSONData:
        """验证图片资产"""
        result = await self.post(f"/assets/{asset_id}/validate", json_data={
            "useCase": use_case,
        })
        return result if isinstance(result, dict) else {}

    async def validate_video(
        self,
        asset_id: str,
        use_case: str,
    ) -> JSONData:
        """验证视频资产"""
        result = await self.post(f"/assets/{asset_id}/validate", json_data={
            "useCase": use_case,
        })
        return result if isinstance(result, dict) else {}

    # ============ Video Processing ============

    async def get_video_processing_status(self, asset_id: str) -> JSONData:
        """获取视频处理状态"""
        result = await self.get(f"/assets/{asset_id}/processing")
        return result if isinstance(result, dict) else {}

    async def get_video_thumbnail(self, asset_id: str, timestamp_ms: int = 0) -> JSONData:
        """获取视频缩略图"""
        result = await self.get(f"/assets/{asset_id}/thumbnail", params={
            "timestampMs": timestamp_ms
        })
        return result if isinstance(result, dict) else {}

    # ============ Brand Logos ============

    async def list_brand_logos(self) -> JSONList:
        """获取品牌Logo列表"""
        result = await self.list_assets(asset_type="BRANDLOGO", state="AVAILABLE")
        return result.get("assets", [])

    # ============ 便捷方法 ============

    async def get_available_images(self) -> JSONList:
        """获取所有可用图片"""
        result = await self.list_assets(asset_type="IMAGE", state="AVAILABLE")
        return result.get("assets", [])

    async def get_available_videos(self) -> JSONList:
        """获取所有可用视频"""
        result = await self.list_assets(asset_type="VIDEO", state="AVAILABLE")
        return result.get("assets", [])

    async def delete_asset(self, asset_id: str) -> JSONData:
        """删除资产"""
        return await self.delete(f"/assets/{asset_id}")

    async def list_all_assets(
        self,
        asset_type: str | None = None,
    ) -> JSONList:
        """获取所有资产（自动分页）"""
        all_assets = []
        next_token = None

        while True:
            result = await self.list_assets(
                asset_type=asset_type,
                max_results=100,
                next_token=next_token,
            )
            assets = result.get("assets", [])
            all_assets.extend(assets)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_assets
