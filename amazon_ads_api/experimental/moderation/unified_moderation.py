"""
Amazon Ads Unified Moderation API (异步版本)
统一审核结果查询

官方端点 (1个):
- POST /moderation/results - 获取广告审核结果

官方规范: Moderation.json
参考文档: https://advertising.amazon.com/API/docs/en-us/moderation

⚠️ 注意: 这是 L4 Experimental 层，API 可能变化

支持的广告类型:
- SPONSORED_PRODUCTS
- SPONSORED_DISPLAY
- SB_PRODUCT_COLLECTION
- SB_STORE_SPOTLIGHT
- SB_VIDEO
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class UnifiedModerationAPI(BaseAdsClient):
    """
    Unified Moderation API (全异步)
    
    用于获取 SP/SB/SD 广告的审核结果。
    
    官方端点 (共1个):
    - POST /moderation/results
    """

    async def get_moderation_results(
        self,
        ad_program_type: str,
        ad_id: str,
        id_type: str = "AD_ID",
        max_results: int = 10,
        moderation_status_filter: list[str] | None = None,
        version_id_filter: list[str] | None = None,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取广告审核结果
        
        官方端点: POST /moderation/results
        官方规范: Moderation.json
        
        Args:
            ad_program_type: 广告程序类型 (必填)
                - SB_PRODUCT_COLLECTION
                - SB_STORE_SPOTLIGHT
                - SB_VIDEO
                - SPONSORED_DISPLAY
                - SPONSORED_PRODUCTS
            ad_id: 广告 ID (必填)
            id_type: ID 类型 (默认 "AD_ID")
            max_results: 最大结果数 (1-10, 默认 10)
            moderation_status_filter: 状态过滤 (可选)
                - APPROVED
                - FAILED
                - IN_PROGRESS
                - REJECTED
            version_id_filter: 版本 ID 过滤 (可选)
            next_token: 分页 token
        
        Returns:
            {
                "moderationResults": [
                    {
                        "id": "...",
                        "idType": "AD_ID",
                        "versionId": "...",
                        "moderationStatus": "APPROVED" | "REJECTED" | "IN_PROGRESS" | "FAILED",
                        "policyViolations": [...],  // 仅当 REJECTED 时
                        "etaForModeration": "...",  // 仅当 IN_PROGRESS 时
                        "componentModerationResults": {...}  // 仅 SP 广告
                    }
                ],
                "nextToken": "..."
            }
        """
        body: JSONData = {
            "adProgramType": ad_program_type,
            "id": ad_id,
            "idType": id_type,
            "maxResults": min(max(1, max_results), 10),
        }
        
        if moderation_status_filter:
            body["moderationStatusFilter"] = moderation_status_filter
        if version_id_filter:
            body["versionIdFilter"] = version_id_filter
        if next_token:
            body["nextToken"] = next_token
        
        result = await self.post(
            "/moderation/results",
            json_data=body,
            content_type="application/vnd.moderationresultsrequest.v4.1+json",
            accept="application/vnd.moderationresultsresponse.v4.0+json",
        )
        return result if isinstance(result, dict) else {"moderationResults": []}

    # ============ 便捷方法 ============
    
    async def get_sp_moderation_results(
        self,
        ad_id: str,
        **kwargs,
    ) -> JSONData:
        """
        获取 Sponsored Products 广告审核结果
        
        Args:
            ad_id: SP 广告 ID
            **kwargs: 其他可选参数
        """
        return await self.get_moderation_results(
            ad_program_type="SPONSORED_PRODUCTS",
            ad_id=ad_id,
            **kwargs,
        )
    
    async def get_sd_moderation_results(
        self,
        ad_id: str,
        **kwargs,
    ) -> JSONData:
        """
        获取 Sponsored Display 广告审核结果
        
        Args:
            ad_id: SD 广告 ID
            **kwargs: 其他可选参数
        """
        return await self.get_moderation_results(
            ad_program_type="SPONSORED_DISPLAY",
            ad_id=ad_id,
            **kwargs,
        )
    
    async def get_sb_moderation_results(
        self,
        ad_id: str,
        ad_format: str = "SB_PRODUCT_COLLECTION",
        **kwargs,
    ) -> JSONData:
        """
        获取 Sponsored Brands 广告审核结果
        
        Args:
            ad_id: SB 广告 ID
            ad_format: SB 广告格式
                - SB_PRODUCT_COLLECTION
                - SB_STORE_SPOTLIGHT
                - SB_VIDEO
            **kwargs: 其他可选参数
        """
        return await self.get_moderation_results(
            ad_program_type=ad_format,
            ad_id=ad_id,
            **kwargs,
        )
    
    async def get_rejected_ads(
        self,
        ad_program_type: str,
        ad_id: str,
    ) -> JSONList:
        """
        获取被拒绝的广告及其违规原因
        
        Args:
            ad_program_type: 广告程序类型
            ad_id: 广告 ID
        
        Returns:
            被拒绝的审核结果列表（包含违规原因）
        """
        result = await self.get_moderation_results(
            ad_program_type=ad_program_type,
            ad_id=ad_id,
            moderation_status_filter=["REJECTED"],
        )
        return result.get("moderationResults", [])
    
    async def is_ad_approved(
        self,
        ad_program_type: str,
        ad_id: str,
    ) -> bool:
        """
        检查广告是否已通过审核
        
        Args:
            ad_program_type: 广告程序类型
            ad_id: 广告 ID
        
        Returns:
            True 如果已通过审核，否则 False
        """
        result = await self.get_moderation_results(
            ad_program_type=ad_program_type,
            ad_id=ad_id,
            moderation_status_filter=["APPROVED"],
            max_results=1,
        )
        results = result.get("moderationResults", [])
        return len(results) > 0 and results[0].get("moderationStatus") == "APPROVED"
