"""
Localization API - 本地化 (异步版本)

提供广告内容的本地化/翻译服务
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient, JSONData, JSONList


class LocalizationAPI(BaseAdsClient):
    """Localization API - 广告内容本地化 (全异步)"""
    
    async def get_supported_locales(self) -> JSONData:
        """获取支持的语言区域列表"""
        result = await self.get("/localization/locales")
        return result if isinstance(result, dict) else {"locales": []}
    
    async def translate_content(
        self,
        *,
        content: str,
        source_locale: str,
        target_locale: str,
        content_type: str = "AD_COPY",
    ) -> JSONData:
        """
        翻译广告内容
        
        Args:
            content: 要翻译的内容
            source_locale: 源语言区域 (如 "en_US")
            target_locale: 目标语言区域 (如 "de_DE")
            content_type: 内容类型 (AD_COPY, HEADLINE, DESCRIPTION等)
        """
        result = await self.post(
            "/localization/translate",
            json_data={
                "content": content,
                "sourceLocale": source_locale,
                "targetLocale": target_locale,
                "contentType": content_type,
            }
        )
        return result if isinstance(result, dict) else {}
    
    async def batch_translate(
        self,
        translations: List[Dict[str, Any]],
    ) -> JSONData:
        """
        批量翻译广告内容
        
        Args:
            translations: 翻译请求列表，每个包含:
                - content: 内容
                - sourceLocale: 源语言
                - targetLocale: 目标语言
                - contentType: 内容类型
        """
        result = await self.post(
            "/localization/translate/batch",
            json_data={"translations": translations}
        )
        return result if isinstance(result, dict) else {"translations": []}
    
    async def get_translation_status(
        self,
        translation_id: str,
    ) -> JSONData:
        """获取翻译状态"""
        result = await self.get(f"/localization/translations/{translation_id}")
        return result if isinstance(result, dict) else {}
