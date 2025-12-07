"""
Amazon DSP - Creatives API
DSP创意管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class DSPCreativesAPI(BaseAdsClient):
    """DSP Creatives API"""

    # ============ Creatives ============

    def list_creatives(
        self,
        advertiser_id: str,
        creative_type: str | None = None,
        state_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取创意列表
        
        Args:
            creative_type: DISPLAY | VIDEO | AUDIO | NATIVE
            state_filter: APPROVED | PENDING | REJECTED
        """
        params: JSONData = {
            "advertiserId": advertiser_id,
            "maxResults": max_results,
        }
        if creative_type:
            params["creativeType"] = creative_type
        if state_filter:
            params["stateFilter"] = state_filter
        if next_token:
            params["nextToken"] = next_token

        result = self.get("/dsp/creatives", params=params)
        return result if isinstance(result, dict) else {"creatives": []}

    def get_creative(self, creative_id: str, advertiser_id: str) -> JSONData:
        """获取单个创意详情"""
        result = self.get(f"/dsp/creatives/{creative_id}", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, dict) else {}

    def create_creative(
        self,
        advertiser_id: str,
        name: str,
        creative_type: str,
        creative_format: str,
        landing_page_url: str,
        assets: JSONData,
    ) -> JSONData:
        """
        创建创意
        
        Args:
            creative_type: DISPLAY | VIDEO | AUDIO | NATIVE
            creative_format: 
                - DISPLAY: BANNER_300x250, BANNER_728x90, BANNER_160x600, etc.
                - VIDEO: VIDEO_15S, VIDEO_30S, etc.
            assets: {
                "imageUrl": "https://...",  # for DISPLAY
                "videoUrl": "https://...",  # for VIDEO
                "headline": "...",
                "description": "..."
            }
        """
        body: JSONData = {
            "advertiserId": advertiser_id,
            "name": name,
            "creativeType": creative_type,
            "creativeFormat": creative_format,
            "landingPageUrl": landing_page_url,
            "assets": assets,
        }

        result = self.post("/dsp/creatives", json_data=body)
        return result if isinstance(result, dict) else {}

    def update_creative(
        self,
        creative_id: str,
        advertiser_id: str,
        updates: JSONData,
    ) -> JSONData:
        """更新创意"""
        body = {"advertiserId": advertiser_id, **updates}
        result = self.put(f"/dsp/creatives/{creative_id}", json_data=body)
        return result if isinstance(result, dict) else {}

    def delete_creative(self, creative_id: str, advertiser_id: str) -> JSONData:
        """删除创意"""
        return self.delete(f"/dsp/creatives/{creative_id}?advertiserId={advertiser_id}")

    # ============ Creative Assets ============

    def upload_creative_asset(
        self,
        advertiser_id: str,
        asset_type: str,
        content_type: str,
        file_content: bytes,
    ) -> JSONData:
        """
        上传创意资产
        
        Args:
            asset_type: IMAGE | VIDEO | AUDIO
            content_type: image/jpeg, image/png, video/mp4, etc.
        """
        # 1. 获取上传URL
        registration = self.post("/dsp/creatives/assets/register", json_data={
            "advertiserId": advertiser_id,
            "assetType": asset_type,
            "contentType": content_type,
        })

        asset_id = registration.get("assetId")
        upload_url = registration.get("uploadUrl")

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

        # 3. 确认上传
        result = self.post(f"/dsp/creatives/assets/{asset_id}/complete", json_data={
            "advertiserId": advertiser_id,
        })
        return result if isinstance(result, dict) else {}

    def get_creative_asset(self, asset_id: str, advertiser_id: str) -> JSONData:
        """获取创意资产详情"""
        result = self.get(f"/dsp/creatives/assets/{asset_id}", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, dict) else {}

    # ============ Creative Moderation ============

    def get_moderation_status(self, creative_id: str, advertiser_id: str) -> JSONData:
        """获取创意审核状态"""
        result = self.get(f"/dsp/creatives/{creative_id}/moderation", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, dict) else {}

    def submit_for_moderation(self, creative_id: str, advertiser_id: str) -> JSONData:
        """提交创意审核"""
        result = self.post(f"/dsp/creatives/{creative_id}/moderation", json_data={
            "advertiserId": advertiser_id,
        })
        return result if isinstance(result, dict) else {}

    # ============ Creative Preview ============

    def get_creative_preview(
        self,
        creative_id: str,
        advertiser_id: str,
        device_type: str = "DESKTOP",
    ) -> JSONData:
        """
        获取创意预览
        
        Args:
            device_type: DESKTOP | MOBILE | TABLET
        """
        result = self.get(f"/dsp/creatives/{creative_id}/preview", params={
            "advertiserId": advertiser_id,
            "deviceType": device_type,
        })
        return result if isinstance(result, dict) else {}

    # ============ Creative Templates ============

    def list_creative_templates(
        self,
        advertiser_id: str,
        creative_type: str | None = None,
    ) -> JSONList:
        """获取可用的创意模板"""
        params: JSONData = {"advertiserId": advertiser_id}
        if creative_type:
            params["creativeType"] = creative_type

        result = self.get("/dsp/creatives/templates", params=params)
        return result if isinstance(result, list) else []

    def create_from_template(
        self,
        advertiser_id: str,
        template_id: str,
        name: str,
        parameters: JSONData,
    ) -> JSONData:
        """使用模板创建创意"""
        result = self.post("/dsp/creatives/fromTemplate", json_data={
            "advertiserId": advertiser_id,
            "templateId": template_id,
            "name": name,
            "parameters": parameters,
        })
        return result if isinstance(result, dict) else {}

    # ============ Creative Specifications ============

    def get_creative_specifications(self, creative_type: str) -> JSONData:
        """
        获取创意规格要求
        
        返回尺寸、文件大小、格式等要求
        """
        result = self.get(f"/dsp/creatives/specifications/{creative_type}")
        return result if isinstance(result, dict) else {}

    # ============ A/B Testing ============

    def create_creative_rotation(
        self,
        advertiser_id: str,
        name: str,
        creative_ids: list[str],
        rotation_type: str = "EVEN",
    ) -> JSONData:
        """
        创建创意轮换
        
        Args:
            rotation_type: EVEN | WEIGHTED | OPTIMIZED
        """
        result = self.post("/dsp/creatives/rotations", json_data={
            "advertiserId": advertiser_id,
            "name": name,
            "creativeIds": creative_ids,
            "rotationType": rotation_type,
        })
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    def list_all_creatives(
        self,
        advertiser_id: str,
        creative_type: str | None = None,
    ) -> JSONList:
        """获取所有创意（自动分页）"""
        all_creatives = []
        next_token = None

        while True:
            result = self.list_creatives(
                advertiser_id=advertiser_id,
                creative_type=creative_type,
                max_results=100,
                next_token=next_token,
            )
            creatives = result.get("creatives", [])
            all_creatives.extend(creatives)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_creatives

    def get_approved_creatives(self, advertiser_id: str) -> JSONList:
        """获取所有已审核通过的创意"""
        all_creatives = []
        next_token = None

        while True:
            result = self.list_creatives(
                advertiser_id=advertiser_id,
                state_filter="APPROVED",
                max_results=100,
                next_token=next_token,
            )
            creatives = result.get("creatives", [])
            all_creatives.extend(creatives)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_creatives

    def create_display_banner(
        self,
        advertiser_id: str,
        name: str,
        image_url: str,
        landing_page_url: str,
        size: str = "300x250",
    ) -> JSONData:
        """快速创建展示广告Banner"""
        return self.create_creative(
            advertiser_id=advertiser_id,
            name=name,
            creative_type="DISPLAY",
            creative_format=f"BANNER_{size}",
            landing_page_url=landing_page_url,
            assets={"imageUrl": image_url},
        )

