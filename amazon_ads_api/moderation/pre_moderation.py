"""
Amazon Ads Pre-Moderation API (异步版本)
广告预审核
"""

from typing import Any
from ..base import BaseAdsClient, JSONData


class PreModerationAPI(BaseAdsClient):
    """Pre-Moderation API (全异步)"""

    # ==================== 预审核请求 ====================

    async def submit_pre_moderation(
        self,
        ad_type: str,
        content: dict[str, Any],
    ) -> JSONData:
        """提交预审核请求"""
        data = {
            "adType": ad_type,
            "content": content,
        }
        result = await self.post("/preModeration/submit", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_pre_moderation_result(self, request_id: str) -> JSONData:
        """获取预审核结果"""
        result = await self.get(f"/preModeration/{request_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 批量预审核 ====================

    async def submit_batch_pre_moderation(
        self,
        requests: list[dict[str, Any]],
    ) -> JSONData:
        """批量提交预审核请求"""
        data = {"requests": requests}
        result = await self.post("/preModeration/batch", json_data=data)
        return result if isinstance(result, dict) else {}

    # ==================== 内容验证 ====================

    async def validate_headline(
        self,
        headline: str,
        ad_type: str,
        marketplace: str,
    ) -> JSONData:
        """验证标题"""
        data = {
            "headline": headline,
            "adType": ad_type,
            "marketplace": marketplace,
        }
        result = await self.post("/preModeration/validate/headline", json_data=data)
        return result if isinstance(result, dict) else {}

    async def validate_image(
        self,
        image_url: str,
        ad_type: str,
        image_type: str,
    ) -> JSONData:
        """验证图片"""
        data = {
            "imageUrl": image_url,
            "adType": ad_type,
            "imageType": image_type,
        }
        result = await self.post("/preModeration/validate/image", json_data=data)
        return result if isinstance(result, dict) else {}

    async def validate_video(
        self,
        video_url: str,
        ad_type: str,
    ) -> JSONData:
        """验证视频"""
        data = {
            "videoUrl": video_url,
            "adType": ad_type,
        }
        result = await self.post("/preModeration/validate/video", json_data=data)
        return result if isinstance(result, dict) else {}

    async def validate_landing_page(
        self,
        landing_page_url: str,
        ad_type: str,
    ) -> JSONData:
        """验证落地页"""
        data = {
            "landingPageUrl": landing_page_url,
            "adType": ad_type,
        }
        result = await self.post("/preModeration/validate/landingPage", json_data=data)
        return result if isinstance(result, dict) else {}

    # ==================== 政策指南 ====================

    async def get_policy_guidelines(
        self,
        ad_type: str,
        marketplace: str,
    ) -> JSONData:
        """获取广告政策指南"""
        params = {
            "adType": ad_type,
            "marketplace": marketplace,
        }
        result = await self.get("/preModeration/policies", params=params)
        return result if isinstance(result, dict) else {}
