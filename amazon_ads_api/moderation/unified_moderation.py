"""
Amazon Ads Unified Moderation API (异步版本)
统一审核
"""

from typing import Any
from ..base import BaseAdsClient, JSONData, JSONList


class UnifiedModerationAPI(BaseAdsClient):
    """Unified Moderation API (全异步)"""

    # ==================== 审核状态 ====================

    async def get_moderation_status(
        self,
        entity_type: str,
        entity_id: str,
    ) -> JSONData:
        """获取审核状态"""
        params = {
            "entityType": entity_type,
            "entityId": entity_id,
        }
        result = await self.get("/moderation/status", params=params)
        return result if isinstance(result, dict) else {}

    async def list_moderation_results(
        self,
        entity_type: str | None = None,
        status: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取审核结果列表"""
        params: dict[str, Any] = {"maxResults": max_results}
        if entity_type:
            params["entityType"] = entity_type
        if status:
            params["status"] = status
        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/moderation/results", params=params)
        return result if isinstance(result, dict) else {"results": []}

    # ==================== 审核详情 ====================

    async def get_rejection_reasons(
        self,
        entity_type: str,
        entity_id: str,
    ) -> JSONList:
        """获取拒绝原因"""
        params = {
            "entityType": entity_type,
            "entityId": entity_id,
        }
        response = await self.get("/moderation/rejections", params=params)
        if isinstance(response, dict):
            return response.get("reasons", [])
        return []

    # ==================== 申诉 ====================

    async def submit_appeal(
        self,
        entity_type: str,
        entity_id: str,
        appeal_reason: str,
        supporting_documents: list[str] | None = None,
    ) -> JSONData:
        """提交申诉"""
        data: dict[str, Any] = {
            "entityType": entity_type,
            "entityId": entity_id,
            "appealReason": appeal_reason,
        }
        if supporting_documents:
            data["supportingDocuments"] = supporting_documents

        result = await self.post("/moderation/appeals", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_appeal_status(self, appeal_id: str) -> JSONData:
        """获取申诉状态"""
        result = await self.get(f"/moderation/appeals/{appeal_id}")
        return result if isinstance(result, dict) else {}
