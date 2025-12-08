"""
Amazon DSP Conversions API (异步版本)
DSP转化追踪
"""

from typing import Any
from ..base import BaseAdsClient, JSONData, JSONList


class DSPConversionsAPI(BaseAdsClient):
    """DSP Conversions API - 转化追踪 (全异步)"""

    # ==================== 转化追踪像素 ====================

    async def list_conversion_pixels(self, advertiser_id: str) -> JSONList:
        """获取转化追踪像素列表"""
        params = {"advertiserId": advertiser_id}
        response = await self.get("/dsp/conversions/pixels", params=params)
        if isinstance(response, dict):
            return response.get("pixels", [])
        return []

    async def create_conversion_pixel(
        self,
        advertiser_id: str,
        name: str,
        pixel_type: str,
        conversion_window_days: int = 30,
    ) -> JSONData:
        """创建转化追踪像素"""
        data = {
            "advertiserId": advertiser_id,
            "name": name,
            "pixelType": pixel_type,
            "conversionWindowDays": conversion_window_days,
        }
        result = await self.post("/dsp/conversions/pixels", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_conversion_pixel(self, pixel_id: str) -> JSONData:
        """获取转化像素详情"""
        result = await self.get(f"/dsp/conversions/pixels/{pixel_id}")
        return result if isinstance(result, dict) else {}

    async def get_pixel_code(self, pixel_id: str) -> JSONData:
        """获取像素安装代码"""
        result = await self.get(f"/dsp/conversions/pixels/{pixel_id}/code")
        return result if isinstance(result, dict) else {}

    # ==================== 离线转化上传 ====================

    async def upload_offline_conversions(
        self,
        advertiser_id: str,
        conversions: list[dict[str, Any]],
    ) -> JSONData:
        """上传离线转化数据"""
        data = {
            "advertiserId": advertiser_id,
            "conversions": conversions,
        }
        result = await self.post("/dsp/conversions/offline", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_offline_upload_status(self, upload_id: str) -> JSONData:
        """获取离线转化上传状态"""
        result = await self.get(f"/dsp/conversions/offline/{upload_id}/status")
        return result if isinstance(result, dict) else {}

    # ==================== 转化事件 ====================

    async def list_conversion_events(
        self,
        advertiser_id: str,
        start_date: str,
        end_date: str,
        pixel_id: str | None = None,
    ) -> JSONList:
        """获取转化事件列表"""
        params: JSONData = {
            "advertiserId": advertiser_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        if pixel_id:
            params["pixelId"] = pixel_id

        response = await self.get("/dsp/conversions/events", params=params)
        if isinstance(response, dict):
            return response.get("events", [])
        return []

    # ==================== 转化归因 ====================

    async def get_conversion_attribution(
        self,
        advertiser_id: str,
        start_date: str,
        end_date: str,
        attribution_model: str = "LAST_TOUCH",
    ) -> JSONData:
        """获取转化归因数据"""
        params = {
            "advertiserId": advertiser_id,
            "startDate": start_date,
            "endDate": end_date,
            "attributionModel": attribution_model,
        }
        result = await self.get("/dsp/conversions/attribution", params=params)
        return result if isinstance(result, dict) else {}
