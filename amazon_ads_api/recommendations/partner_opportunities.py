"""
Amazon Ads Partner Opportunities API (异步版本)
合作机会管理
"""

from typing import Any
from ..base import BaseAdsClient, JSONData, JSONList


class PartnerOpportunitiesAPI(BaseAdsClient):
    """Partner Opportunities API (全异步)"""

    # ==================== 机会发现 ====================

    async def list_opportunities(
        self,
        opportunity_type: str | None = None,
        state: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取合作机会列表"""
        params: dict[str, Any] = {"maxResults": max_results}
        if opportunity_type:
            params["opportunityType"] = opportunity_type
        if state:
            params["state"] = state
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/opportunities", params=params)
        return result if isinstance(result, dict) else {"opportunities": []}

    async def get_opportunity(self, opportunity_id: str) -> JSONData:
        """获取机会详情"""
        result = await self.get(f"/opportunities/{opportunity_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 机会操作 ====================

    async def accept_opportunity(
        self,
        opportunity_id: str,
        config: dict[str, Any] | None = None,
    ) -> JSONData:
        """接受合作机会"""
        data = {}
        if config:
            data["config"] = config

        result = await self.post(
            f"/opportunities/{opportunity_id}/accept",
            json_data=data if data else None,
        )
        return result if isinstance(result, dict) else {}

    async def dismiss_opportunity(
        self,
        opportunity_id: str,
        reason: str | None = None,
    ) -> JSONData:
        """拒绝合作机会"""
        data = {}
        if reason:
            data["reason"] = reason

        result = await self.post(
            f"/opportunities/{opportunity_id}/dismiss",
            json_data=data if data else None,
        )
        return result if isinstance(result, dict) else {}

    async def mark_opportunity_viewed(self, opportunity_id: str) -> JSONData:
        """标记机会为已查看"""
        result = await self.post(f"/opportunities/{opportunity_id}/view")
        return result if isinstance(result, dict) else {}

    # ==================== 机会分析 ====================

    async def get_opportunity_impact(self, opportunity_id: str) -> JSONData:
        """获取机会预估影响"""
        result = await self.get(f"/opportunities/{opportunity_id}/impact")
        return result if isinstance(result, dict) else {}

    async def list_opportunity_types(self) -> JSONList:
        """获取可用机会类型列表"""
        response = await self.get("/opportunities/types")
        if isinstance(response, dict):
            return response.get("types", [])
        return []
