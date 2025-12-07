"""
Amazon DSP Conversions API

官方文档: https://advertising.amazon.com/API/docs/en-us/dsp
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/ConversionsAPI_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class DSPConversionsAPI(BaseAdsClient):
    """DSP Conversions API - 转化追踪
    
    管理DSP广告的转化追踪和上传离线转化数据。
    """
    
    # ==================== 转化追踪像素 ====================
    
    async def list_conversion_pixels(
        self,
        advertiser_id: str,
    ) -> List[Dict[str, Any]]:
        """获取转化追踪像素列表
        
        Args:
            advertiser_id: 广告商ID
            
        Returns:
            转化像素列表
        """
        params = {"advertiserId": advertiser_id}
        response = await self._make_request(
            "GET",
            "/dsp/conversions/pixels",
            params=params,
        )
        return response.get("pixels", [])
    
    async def create_conversion_pixel(
        self,
        advertiser_id: str,
        name: str,
        pixel_type: str,
        conversion_window_days: int = 30,
    ) -> Dict[str, Any]:
        """创建转化追踪像素
        
        Args:
            advertiser_id: 广告商ID
            name: 像素名称
            pixel_type: 像素类型 (PURCHASE, LEAD, SIGN_UP, etc.)
            conversion_window_days: 转化窗口天数
            
        Returns:
            创建的像素信息
        """
        data = {
            "advertiserId": advertiser_id,
            "name": name,
            "pixelType": pixel_type,
            "conversionWindowDays": conversion_window_days,
        }
        return await self._make_request(
            "POST",
            "/dsp/conversions/pixels",
            json=data,
        )
    
    async def get_conversion_pixel(
        self,
        pixel_id: str,
    ) -> Dict[str, Any]:
        """获取转化像素详情
        
        Args:
            pixel_id: 像素ID
            
        Returns:
            像素详情
        """
        return await self._make_request(
            "GET",
            f"/dsp/conversions/pixels/{pixel_id}",
        )
    
    async def get_pixel_code(
        self,
        pixel_id: str,
    ) -> Dict[str, Any]:
        """获取像素安装代码
        
        Args:
            pixel_id: 像素ID
            
        Returns:
            像素代码
        """
        return await self._make_request(
            "GET",
            f"/dsp/conversions/pixels/{pixel_id}/code",
        )
    
    # ==================== 离线转化上传 ====================
    
    async def upload_offline_conversions(
        self,
        advertiser_id: str,
        conversions: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """上传离线转化数据
        
        Args:
            advertiser_id: 广告商ID
            conversions: 转化数据列表，每个包含:
                - conversionTime: 转化时间
                - conversionType: 转化类型
                - conversionValue: 转化价值（可选）
                - hashedEmail or hashedPhone: 哈希后的用户标识
                
        Returns:
            上传结果
        """
        data = {
            "advertiserId": advertiser_id,
            "conversions": conversions,
        }
        return await self._make_request(
            "POST",
            "/dsp/conversions/offline",
            json=data,
        )
    
    async def get_offline_upload_status(
        self,
        upload_id: str,
    ) -> Dict[str, Any]:
        """获取离线转化上传状态
        
        Args:
            upload_id: 上传ID
            
        Returns:
            上传状态
        """
        return await self._make_request(
            "GET",
            f"/dsp/conversions/offline/{upload_id}/status",
        )
    
    # ==================== 转化事件 ====================
    
    async def list_conversion_events(
        self,
        advertiser_id: str,
        start_date: str,
        end_date: str,
        pixel_id: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """获取转化事件列表
        
        Args:
            advertiser_id: 广告商ID
            start_date: 开始日期
            end_date: 结束日期
            pixel_id: 像素ID（可选）
            
        Returns:
            转化事件列表
        """
        params = {
            "advertiserId": advertiser_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        if pixel_id:
            params["pixelId"] = pixel_id
            
        response = await self._make_request(
            "GET",
            "/dsp/conversions/events",
            params=params,
        )
        return response.get("events", [])
    
    # ==================== 转化归因 ====================
    
    async def get_conversion_attribution(
        self,
        advertiser_id: str,
        start_date: str,
        end_date: str,
        attribution_model: str = "LAST_TOUCH",
    ) -> Dict[str, Any]:
        """获取转化归因数据
        
        Args:
            advertiser_id: 广告商ID
            start_date: 开始日期
            end_date: 结束日期
            attribution_model: 归因模型 (LAST_TOUCH, FIRST_TOUCH, LINEAR, etc.)
            
        Returns:
            归因数据
        """
        params = {
            "advertiserId": advertiser_id,
            "startDate": start_date,
            "endDate": end_date,
            "attributionModel": attribution_model,
        }
        return await self._make_request(
            "GET",
            "/dsp/conversions/attribution",
            params=params,
        )

