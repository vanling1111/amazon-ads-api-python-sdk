"""
Pre-Moderation API

官方文档: https://advertising.amazon.com/API/docs/en-us/moderation
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/PreModeration_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class PreModerationAPI(BaseAdsClient):
    """Pre-Moderation API - 预审核
    
    在提交广告前进行预审核检查。
    """
    
    # ==================== 预审核请求 ====================
    
    async def submit_pre_moderation(
        self,
        ad_type: str,
        content: Dict[str, Any],
    ) -> Dict[str, Any]:
        """提交预审核请求
        
        Args:
            ad_type: 广告类型 (SP, SB, SD, DSP)
            content: 广告内容，包含:
                - headline: 标题
                - customImage: 自定义图片URL
                - video: 视频URL
                - landingPage: 落地页URL
                
        Returns:
            预审核请求结果
        """
        data = {
            "adType": ad_type,
            "content": content,
        }
        return await self._make_request(
            "POST",
            "/preModeration/submit",
            json=data,
        )
    
    async def get_pre_moderation_result(
        self,
        request_id: str,
    ) -> Dict[str, Any]:
        """获取预审核结果
        
        Args:
            request_id: 预审核请求ID
            
        Returns:
            预审核结果
        """
        return await self._make_request(
            "GET",
            f"/preModeration/{request_id}",
        )
    
    # ==================== 批量预审核 ====================
    
    async def submit_batch_pre_moderation(
        self,
        requests: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """批量提交预审核请求
        
        Args:
            requests: 预审核请求列表，每个包含:
                - adType: 广告类型
                - content: 广告内容
                
        Returns:
            批量预审核结果
        """
        data = {"requests": requests}
        return await self._make_request(
            "POST",
            "/preModeration/batch",
            json=data,
        )
    
    # ==================== 内容验证 ====================
    
    async def validate_headline(
        self,
        headline: str,
        ad_type: str,
        marketplace: str,
    ) -> Dict[str, Any]:
        """验证标题
        
        Args:
            headline: 广告标题
            ad_type: 广告类型
            marketplace: 市场 (US, UK, DE, etc.)
            
        Returns:
            验证结果
        """
        data = {
            "headline": headline,
            "adType": ad_type,
            "marketplace": marketplace,
        }
        return await self._make_request(
            "POST",
            "/preModeration/validate/headline",
            json=data,
        )
    
    async def validate_image(
        self,
        image_url: str,
        ad_type: str,
        image_type: str,
    ) -> Dict[str, Any]:
        """验证图片
        
        Args:
            image_url: 图片URL
            ad_type: 广告类型
            image_type: 图片类型 (CUSTOM_IMAGE, LOGO, etc.)
            
        Returns:
            验证结果
        """
        data = {
            "imageUrl": image_url,
            "adType": ad_type,
            "imageType": image_type,
        }
        return await self._make_request(
            "POST",
            "/preModeration/validate/image",
            json=data,
        )
    
    async def validate_video(
        self,
        video_url: str,
        ad_type: str,
    ) -> Dict[str, Any]:
        """验证视频
        
        Args:
            video_url: 视频URL
            ad_type: 广告类型
            
        Returns:
            验证结果
        """
        data = {
            "videoUrl": video_url,
            "adType": ad_type,
        }
        return await self._make_request(
            "POST",
            "/preModeration/validate/video",
            json=data,
        )
    
    async def validate_landing_page(
        self,
        landing_page_url: str,
        ad_type: str,
    ) -> Dict[str, Any]:
        """验证落地页
        
        Args:
            landing_page_url: 落地页URL
            ad_type: 广告类型
            
        Returns:
            验证结果
        """
        data = {
            "landingPageUrl": landing_page_url,
            "adType": ad_type,
        }
        return await self._make_request(
            "POST",
            "/preModeration/validate/landingPage",
            json=data,
        )
    
    # ==================== 政策指南 ====================
    
    async def get_policy_guidelines(
        self,
        ad_type: str,
        marketplace: str,
    ) -> Dict[str, Any]:
        """获取广告政策指南
        
        Args:
            ad_type: 广告类型
            marketplace: 市场
            
        Returns:
            政策指南
        """
        params = {
            "adType": ad_type,
            "marketplace": marketplace,
        }
        return await self._make_request(
            "GET",
            "/preModeration/policies",
            params=params,
        )

