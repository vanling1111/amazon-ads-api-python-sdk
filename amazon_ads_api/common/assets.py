"""
Assets API
创意资产管理（图片、视频、Logo等）
"""

from ..base import BaseAdsClient, JSONData, JSONList


class AssetsAPI(BaseAdsClient):
    """Assets API"""

    # ============ Assets ============

    def list_assets(
        self,
        asset_type: str | None = None,
        state: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取资产列表
        
        Args:
            asset_type: IMAGE | VIDEO | BRANDLOGO
            state: AVAILABLE | PENDING | FAILED
        """
        params: JSONData = {"maxResults": max_results}
        if asset_type:
            params["assetType"] = asset_type
        if state:
            params["state"] = state
        if next_token:
            params["nextToken"] = next_token

        result = self.get("/assets", params=params)
        return result if isinstance(result, dict) else {"assets": []}

    def get_asset(self, asset_id: str) -> JSONData:
        """获取资产详情"""
        result = self.get(f"/assets/{asset_id}")
        return result if isinstance(result, dict) else {}

    # ============ Upload Assets ============

    def register_asset(
        self,
        asset_type: str,
        name: str,
        content_type: str,
    ) -> JSONData:
        """
        注册资产（获取上传URL）
        
        Args:
            asset_type: IMAGE | VIDEO | BRANDLOGO
            name: 资产名称
            content_type: image/jpeg, image/png, video/mp4, etc.
            
        Returns:
            {
                "assetId": "xxx",
                "uploadLocation": "https://...",  # 用于上传的预签名URL
            }
        """
        result = self.post("/assets/register", json_data={
            "assetType": asset_type,
            "name": name,
            "contentType": content_type,
        })
        return result if isinstance(result, dict) else {}

    def complete_asset_upload(self, asset_id: str) -> JSONData:
        """
        完成资产上传
        
        上传文件到uploadLocation后调用此方法
        """
        result = self.post(f"/assets/{asset_id}/complete")
        return result if isinstance(result, dict) else {}

    def upload_asset(
        self,
        asset_type: str,
        name: str,
        content_type: str,
        file_content: bytes,
    ) -> JSONData:
        """
        上传资产（完整流程）
        
        注册 -> 上传 -> 完成
        """
        # 1. 注册
        registration = self.register_asset(asset_type, name, content_type)
        asset_id = registration.get("assetId")
        upload_url = registration.get("uploadLocation")

        if not asset_id or not upload_url:
            return {}

        # 2. 上传文件
        response = self.session.put(
            upload_url,
            data=file_content,
            headers={"Content-Type": content_type},
            timeout=120,
        )

        if not response.ok:
            return {"error": f"Upload failed: {response.status_code}"}

        # 3. 完成
        return self.complete_asset_upload(asset_id)

    # ============ Asset Versions ============

    def list_asset_versions(self, asset_id: str) -> JSONList:
        """获取资产版本列表"""
        result = self.get(f"/assets/{asset_id}/versions")
        return result if isinstance(result, list) else []

    def get_asset_version(self, asset_id: str, version_id: str) -> JSONData:
        """获取特定版本详情"""
        result = self.get(f"/assets/{asset_id}/versions/{version_id}")
        return result if isinstance(result, dict) else {}

    # ============ Asset Validation ============

    def validate_image(
        self,
        asset_id: str,
        use_case: str,
    ) -> JSONData:
        """
        验证图片资产
        
        Args:
            use_case: SB_LOGO | SB_CUSTOM_IMAGE | SD_CUSTOM_IMAGE
        """
        result = self.post(f"/assets/{asset_id}/validate", json_data={
            "useCase": use_case,
        })
        return result if isinstance(result, dict) else {}

    def validate_video(
        self,
        asset_id: str,
        use_case: str,
    ) -> JSONData:
        """
        验证视频资产
        
        Args:
            use_case: SB_VIDEO | SD_VIDEO
        """
        result = self.post(f"/assets/{asset_id}/validate", json_data={
            "useCase": use_case,
        })
        return result if isinstance(result, dict) else {}

    # ============ Video Processing ============

    def get_video_processing_status(self, asset_id: str) -> JSONData:
        """获取视频处理状态"""
        result = self.get(f"/assets/{asset_id}/processing")
        return result if isinstance(result, dict) else {}

    def get_video_thumbnail(self, asset_id: str, timestamp_ms: int = 0) -> JSONData:
        """
        获取视频缩略图
        
        Args:
            timestamp_ms: 获取视频某一帧作为缩略图
        """
        result = self.get(f"/assets/{asset_id}/thumbnail", params={
            "timestampMs": timestamp_ms
        })
        return result if isinstance(result, dict) else {}

    # ============ Brand Logos ============

    def list_brand_logos(self) -> JSONList:
        """获取品牌Logo列表"""
        result = self.list_assets(asset_type="BRANDLOGO", state="AVAILABLE")
        return result.get("assets", [])

    def upload_brand_logo(
        self,
        name: str,
        file_content: bytes,
        content_type: str = "image/png",
    ) -> JSONData:
        """
        上传品牌Logo
        
        要求：
        - 尺寸：400x400 或更大
        - 格式：PNG（透明背景最佳）
        - 大小：< 1MB
        """
        return self.upload_asset(
            asset_type="BRANDLOGO",
            name=name,
            content_type=content_type,
            file_content=file_content,
        )

    # ============ 便捷方法 ============

    def get_available_images(self) -> JSONList:
        """获取所有可用图片"""
        result = self.list_assets(asset_type="IMAGE", state="AVAILABLE")
        return result.get("assets", [])

    def get_available_videos(self) -> JSONList:
        """获取所有可用视频"""
        result = self.list_assets(asset_type="VIDEO", state="AVAILABLE")
        return result.get("assets", [])

    def delete_asset(self, asset_id: str) -> JSONData:
        """删除资产"""
        return self.delete(f"/assets/{asset_id}")

    def list_all_assets(
        self,
        asset_type: str | None = None,
    ) -> JSONList:
        """获取所有资产（自动分页）"""
        all_assets = []
        next_token = None

        while True:
            result = self.list_assets(
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

