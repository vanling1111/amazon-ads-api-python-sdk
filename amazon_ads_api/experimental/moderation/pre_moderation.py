"""
Amazon Ads Pre-Moderation API (异步版本)
广告预审核

官方端点 (1个):
- POST /preModeration - 预审核广告组件

官方规范: PreModeration.json
参考文档: https://advertising.amazon.com/API/docs/en-us/pre-moderation

⚠️ 注意: 这是 L4 Experimental 层，API 可能变化

支持的广告程序:
- DSP, DSP_CONSOLIDATED_TEMPLATE, DSP_IMAGE, DSP_REC, DSP_THIRD_PARTY
- SPONSORED_BRANDS, SPONSORED_BRANDS_SPOTLIGHT, SPONSORED_BRANDS_VIDEO
- SPONSORED_DISPLAY, SPONSORED_DISPLAY_NOT_SOLD_ON_AMAZON
- SPONSORED_TV, STORES
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class PreModerationAPI(BaseAdsClient):
    """
    Pre-Moderation API (全异步)
    
    用于在创建广告前预审核广告组件，提前发现政策违规。
    
    官方端点 (共1个):
    - POST /preModeration
    """

    async def pre_moderate(
        self,
        ad_program: str,
        locale: str,
        record_id: str | None = None,
        target_language: str | None = None,
        text_components: JSONList | None = None,
        image_components: JSONList | None = None,
        video_components: JSONList | None = None,
        asin_components: JSONList | None = None,
        url_components: JSONList | None = None,
        date_components: JSONList | None = None,
        third_party_components: JSONList | None = None,
    ) -> JSONData:
        """
        预审核广告组件
        
        官方端点: POST /preModeration
        官方规范: PreModeration.json
        
        推荐: 将同一实体的所有组件一起发送，以便更好地检测政策违规。
        
        Args:
            ad_program: 广告程序类型 (必填)
                - DSP, DSP_CONSOLIDATED_TEMPLATE, DSP_IMAGE, DSP_REC, DSP_THIRD_PARTY
                - SPONSORED_BRANDS, SPONSORED_BRANDS_SPOTLIGHT, SPONSORED_BRANDS_VIDEO
                - SPONSORED_DISPLAY, SPONSORED_DISPLAY_NOT_SOLD_ON_AMAZON
                - SPONSORED_TV, STORES
            locale: 区域设置 (必填)
                - ar-AE, de-DE, en-AE, en-AU, en-CA, en-GB, en-IN, en-JP, en-NL, en-SA, en-US
                - es-ES, es-MX, es-US, fr-CA, fr-FR, it-IT, ja-JP, ko-KR, nl-NL, pt-BR, tr-TR, zh-CN
            record_id: 品牌/广告商 ID (可选)
            target_language: 目标语言 ISO_639-1 (可选)
                - ar, de, en, es, fr, hi, it, ja, nl, pl, pt, ru, sv, tr, zh
            text_components: 文本组件列表 (最多10个)
                [{
                    "id": "unique-id",
                    "componentType": "BRAND_NAME" | "HEADLINE" | "OTHER_TEXT",
                    "text": "要审核的文本"
                }]
            image_components: 图片组件列表 (最多10个)
                [{
                    "id": "unique-id",
                    "componentType": "BRAND_LOGO" | "CUSTOM_IMAGE" | ...,
                    "url": "公开可访问的图片URL"
                }]
            video_components: 视频组件列表 (最多1个)
                [{
                    "id": "unique-id",
                    "componentType": "DSP_VIDEO" | "SPONSORED_BRANDS_VIDEO" | ...,
                    "url": "公开可访问的视频URL"
                }]
            asin_components: ASIN 组件列表 (最多10个)
                [{
                    "id": "unique-id",
                    "componentType": "LANDING_ASIN" | "PRODUCT_ASIN",
                    "asin": "B00XXXXXX"
                }]
            url_components: URL 组件列表 (最多10个)
                [{
                    "id": "unique-id",
                    "componentType": "CLICK_THROUGH_URL",
                    "url": "https://..."
                }]
            date_components: 日期组件列表 (最多10个)
                [{
                    "id": "unique-id",
                    "componentType": "CAMPAIGN_DATE",
                    "startDate": "yyyy-MM-dd HH:mm:ss",
                    "endDate": "yyyy-MM-dd HH:mm:ss"
                }]
            third_party_components: 第三方组件列表 (最多10个)
        
        Returns:
            {
                "preModerationId": "...",
                "adProgram": "...",
                "locale": "...",
                "textComponents": [{
                    "id": "...",
                    "preModerationStatus": "APPROVED" | "REJECTED" | "FAILED" | "RETRYABLE_FAILURE",
                    "policyViolations": [...]  // 仅当被拒绝时
                }],
                "imageComponents": [...],
                "videoComponents": [...],
                ...
            }
        """
        body: JSONData = {
            "adProgram": ad_program,
            "locale": locale,
        }
        
        if record_id:
            body["recordId"] = record_id
        if target_language:
            body["targetLanguage"] = target_language
        if text_components:
            body["textComponents"] = text_components
        if image_components:
            body["imageComponents"] = image_components
        if video_components:
            body["videoComponents"] = video_components
        if asin_components:
            body["asinComponents"] = asin_components
        if url_components:
            body["urlComponents"] = url_components
        if date_components:
            body["dateComponents"] = date_components
        if third_party_components:
            body["thirdPartyComponents"] = third_party_components
        
        result = await self.post("/preModeration", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============
    
    async def pre_moderate_headline(
        self,
        ad_program: str,
        locale: str,
        headline: str,
        component_id: str = "headline-1",
    ) -> JSONData:
        """
        预审核标题文本
        
        Args:
            ad_program: 广告程序类型
            locale: 区域设置
            headline: 标题文本
            component_id: 组件 ID
        
        Returns:
            预审核结果
        """
        return await self.pre_moderate(
            ad_program=ad_program,
            locale=locale,
            text_components=[{
                "id": component_id,
                "componentType": "HEADLINE",
                "text": headline,
            }],
        )
    
    async def pre_moderate_brand_name(
        self,
        ad_program: str,
        locale: str,
        brand_name: str,
        component_id: str = "brand-name-1",
    ) -> JSONData:
        """
        预审核品牌名称
        
        Args:
            ad_program: 广告程序类型
            locale: 区域设置
            brand_name: 品牌名称
            component_id: 组件 ID
        """
        return await self.pre_moderate(
            ad_program=ad_program,
            locale=locale,
            text_components=[{
                "id": component_id,
                "componentType": "BRAND_NAME",
                "text": brand_name,
            }],
        )
    
    async def pre_moderate_image(
        self,
        ad_program: str,
        locale: str,
        image_url: str,
        component_type: str = "CUSTOM_IMAGE",
        component_id: str = "image-1",
    ) -> JSONData:
        """
        预审核图片
        
        Args:
            ad_program: 广告程序类型
            locale: 区域设置
            image_url: 图片 URL（必须公开可访问）
            component_type: 组件类型
                - BRAND_LOGO
                - CUSTOM_IMAGE
                - CUSTOM_IMAGE_RESPONSIVE_SIZE
                - CUSTOM_IMAGE_SIZE_SPECIFIC
                - OTHER_IMAGE
            component_id: 组件 ID
        """
        return await self.pre_moderate(
            ad_program=ad_program,
            locale=locale,
            image_components=[{
                "id": component_id,
                "componentType": component_type,
                "url": image_url,
            }],
        )
    
    async def pre_moderate_video(
        self,
        ad_program: str,
        locale: str,
        video_url: str,
        component_type: str = "SPONSORED_BRANDS_VIDEO",
        component_id: str = "video-1",
    ) -> JSONData:
        """
        预审核视频
        
        Args:
            ad_program: 广告程序类型
            locale: 区域设置
            video_url: 视频 URL（必须公开可访问）
            component_type: 组件类型
                - DSP_VIDEO
                - SPONSORED_BRANDS_VIDEO
                - SPONSORED_DISPLAY_VIDEO
                - SPONSORED_TV_VIDEO
                - OTHER_VIDEO
            component_id: 组件 ID
        """
        return await self.pre_moderate(
            ad_program=ad_program,
            locale=locale,
            video_components=[{
                "id": component_id,
                "componentType": component_type,
                "url": video_url,
            }],
        )
    
    async def pre_moderate_asin(
        self,
        ad_program: str,
        locale: str,
        asin: str,
        component_type: str = "PRODUCT_ASIN",
        component_id: str = "asin-1",
    ) -> JSONData:
        """
        预审核 ASIN
        
        Args:
            ad_program: 广告程序类型
            locale: 区域设置
            asin: ASIN
            component_type: LANDING_ASIN 或 PRODUCT_ASIN
            component_id: 组件 ID
        """
        return await self.pre_moderate(
            ad_program=ad_program,
            locale=locale,
            asin_components=[{
                "id": component_id,
                "componentType": component_type,
                "asin": asin,
            }],
        )
    
    def is_approved(self, result: JSONData) -> bool:
        """
        检查预审核结果是否全部通过
        
        Args:
            result: pre_moderate 返回的结果
        
        Returns:
            True 如果所有组件都通过，否则 False
        """
        component_types = [
            "textComponents", "imageComponents", "videoComponents",
            "asinComponents", "urlComponents", "dateComponents",
            "thirdPartyComponents"
        ]
        
        for comp_type in component_types:
            components = result.get(comp_type, [])
            for comp in components:
                status = comp.get("preModerationStatus")
                if status != "APPROVED":
                    return False
        
        return True
    
    def get_policy_violations(self, result: JSONData) -> JSONList:
        """
        从预审核结果中提取所有政策违规
        
        Args:
            result: pre_moderate 返回的结果
        
        Returns:
            所有违规的列表
        """
        violations: JSONList = []
        component_types = [
            "textComponents", "imageComponents", "videoComponents",
            "asinComponents", "urlComponents", "dateComponents",
            "thirdPartyComponents"
        ]
        
        for comp_type in component_types:
            components = result.get(comp_type, [])
            for comp in components:
                comp_violations = comp.get("policyViolations", [])
                spec_violations = comp.get("specViolations", [])
                
                for v in comp_violations + spec_violations:
                    violations.append({
                        "componentId": comp.get("id"),
                        "componentType": comp.get("componentType"),
                        **v,
                    })
        
        return violations
