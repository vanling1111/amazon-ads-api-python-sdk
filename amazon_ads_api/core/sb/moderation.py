"""
Sponsored Brands - Moderation API (异步版本)
SB广告审核查询

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi#tag/Moderation
OpenAPI Spec: SponsoredBrands_v3.yaml

注意：SB v3 只有 1 个 moderation 端点
"""

from amazon_ads_api.base import BaseAdsClient, JSONData


class SBModerationAPI(BaseAdsClient):
    """
    SB Moderation API (全异步)
    
    官方端点 (共1个):
    - GET /sb/moderation/campaigns/{campaignId} - 获取Campaign审核状态
    
    注意：
    - 这是 SB v3 API 端点
    - 更全面的审核功能请使用通用 Moderation API
    """

    async def get_campaign_moderation(self, campaign_id: str) -> JSONData:
        """
        获取 Campaign 审核状态
        
        官方端点: GET /sb/moderation/campaigns/{campaignId}
        
        Args:
            campaign_id: Campaign ID
        
        Returns:
            {
                "campaignId": "xxx",
                "moderationStatus": "PENDING" | "APPROVED" | "REJECTED",
                "moderationReasons": ["reason1", "reason2"],
                "lastUpdated": "2024-01-01T00:00:00Z"
            }
        """
        result = await self.get(f"/sb/moderation/campaigns/{campaign_id}")
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def is_campaign_approved(self, campaign_id: str) -> bool:
        """检查 Campaign 是否已审核通过"""
        result = await self.get_campaign_moderation(campaign_id)
        return result.get("moderationStatus") == "APPROVED"

    async def is_campaign_pending(self, campaign_id: str) -> bool:
        """检查 Campaign 是否待审核"""
        result = await self.get_campaign_moderation(campaign_id)
        return result.get("moderationStatus") == "PENDING"

    async def is_campaign_rejected(self, campaign_id: str) -> bool:
        """检查 Campaign 是否被拒绝"""
        result = await self.get_campaign_moderation(campaign_id)
        return result.get("moderationStatus") == "REJECTED"

    async def get_rejection_reasons(self, campaign_id: str) -> list[str]:
        """获取 Campaign 被拒绝的原因"""
        result = await self.get_campaign_moderation(campaign_id)
        if result.get("moderationStatus") == "REJECTED":
            return result.get("moderationReasons", [])
        return []
