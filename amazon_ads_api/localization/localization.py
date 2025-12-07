"""
Localization API - 本地化

提供广告内容的本地化/翻译服务
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class LocalizationAPI(BaseAdsClient):
    """Localization API - 广告内容本地化"""
    
    async def get_supported_locales(self) -> Dict[str, Any]:
        """获取支持的语言区域列表"""
        return await self._request("GET", "/localization/locales")
    
    async def translate_content(
        self,
        *,
        content: str,
        source_locale: str,
        target_locale: str,
        content_type: str = "AD_COPY",
    ) -> Dict[str, Any]:
        """
        翻译广告内容
        
        Args:
            content: 要翻译的内容
            source_locale: 源语言区域 (如 "en_US")
            target_locale: 目标语言区域 (如 "de_DE")
            content_type: 内容类型 (AD_COPY, HEADLINE, DESCRIPTION等)
        """
        return await self._request(
            "POST",
            "/localization/translate",
            json={
                "content": content,
                "sourceLocale": source_locale,
                "targetLocale": target_locale,
                "contentType": content_type,
            }
        )
    
    async def batch_translate(
        self,
        translations: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        批量翻译广告内容
        
        Args:
            translations: 翻译请求列表，每个包含:
                - content: 内容
                - sourceLocale: 源语言
                - targetLocale: 目标语言
                - contentType: 内容类型
        """
        return await self._request(
            "POST",
            "/localization/translate/batch",
            json={"translations": translations}
        )
    
    async def get_translation_status(
        self,
        translation_id: str,
    ) -> Dict[str, Any]:
        """获取翻译状态"""
        return await self._request(
            "GET",
            f"/localization/translations/{translation_id}"
        )

