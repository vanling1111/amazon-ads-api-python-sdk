"""
Sponsored Display - Creative Moderation API (异步版本)
SD创意审核查询

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi
OpenAPI Spec: SponsoredDisplay_v3.yaml

注意：SD v3 只有 1 个 moderation 端点
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SDModerationAPI(BaseAdsClient):
    """
    SD Creative Moderation API (全异步)
    
    官方端点 (共1个):
    - GET /sd/moderation/creatives - 获取创意审核状态列表
    
    注意：
    - 这是 SD v3 API 端点
    - 更全面的审核功能请使用通用 Moderation API
    """

    async def list_creative_moderation(
        self,
        state_filter: str | None = None,
        start_index: int = 0,
        count: int = 100,
    ) -> JSONList:
        """
        获取创意审核状态列表
        
        官方端点: GET /sd/moderation/creatives
        
        Args:
            state_filter: 状态过滤
                - PENDING: 待审核
                - APPROVED: 已通过
                - REJECTED: 被拒绝
            start_index: 起始索引（分页）
            count: 返回数量（最大1000）
        
        Returns:
            [
                {
                    "creativeId": "xxx",
                    "state": "APPROVED" | "PENDING" | "REJECTED",
                    "creationType": "IMAGE" | "VIDEO",
                    "servingStatus": "...",
                    "moderationReasons": ["reason1", "reason2"]  // 仅当被拒绝时
                }
            ]
        """
        params: JSONData = {"startIndex": start_index, "count": count}
        if state_filter:
            params["stateFilter"] = state_filter

        result = await self.get("/sd/moderation/creatives", params=params)
        return result if isinstance(result, list) else []

    # ============ 便捷方法 ============

    async def list_all_creative_moderation(
        self,
        state_filter: str | None = None,
    ) -> JSONList:
        """
        获取所有创意审核状态（自动分页）
        
        Args:
            state_filter: 可选的状态过滤
        """
        all_creatives: JSONList = []
        start_index = 0
        page_size = 1000

        while True:
            creatives = await self.list_creative_moderation(
                state_filter=state_filter,
                start_index=start_index,
                count=page_size,
            )

            if not creatives:
                break

            all_creatives.extend(creatives)

            if len(creatives) < page_size:
                break

            start_index += len(creatives)

        return all_creatives

    async def get_pending_creatives(self) -> JSONList:
        """获取待审核的创意"""
        return await self.list_creative_moderation(state_filter="PENDING")

    async def get_approved_creatives(self) -> JSONList:
        """获取已通过的创意"""
        return await self.list_creative_moderation(state_filter="APPROVED")

    async def get_rejected_creatives(self) -> JSONList:
        """获取被拒绝的创意"""
        return await self.list_creative_moderation(state_filter="REJECTED")

    async def get_creative_moderation_by_id(
        self,
        creative_id: str,
    ) -> JSONData | None:
        """
        根据 ID 获取单个创意的审核状态
        
        注意：这是通过 list 端点过滤实现的，官方没有单独的 get by id 端点
        """
        # 由于官方没有按 ID 获取的端点，需要遍历列表
        all_creatives = await self.list_all_creative_moderation()
        for creative in all_creatives:
            if creative.get("creativeId") == creative_id:
                return creative
        return None

    async def count_by_status(self) -> JSONData:
        """统计各状态的创意数量"""
        all_creatives = await self.list_all_creative_moderation()
        
        counts = {"PENDING": 0, "APPROVED": 0, "REJECTED": 0, "OTHER": 0}
        for creative in all_creatives:
            state = creative.get("state", "OTHER")
            if state in counts:
                counts[state] += 1
            else:
                counts["OTHER"] += 1
        
        return counts

    async def get_rejection_reasons(self, creative_id: str) -> list[str]:
        """获取创意被拒绝的原因"""
        creative = await self.get_creative_moderation_by_id(creative_id)
        if creative and creative.get("state") == "REJECTED":
            return creative.get("moderationReasons", [])
        return []
