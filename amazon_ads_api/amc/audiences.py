"""
Amazon Marketing Cloud Audiences API (异步版本)
AMC受众管理
"""

from typing import Any
from ..base import BaseAdsClient, JSONData


class AMCAudiencesAPI(BaseAdsClient):
    """AMC Audiences API (全异步)"""

    # ==================== 受众管理 ====================

    async def list_audiences(
        self,
        state: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取受众列表"""
        params: dict[str, Any] = {"maxResults": max_results}
        if state:
            params["state"] = state
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/amc/audiences", params=params)
        return result if isinstance(result, dict) else {"audiences": []}

    async def create_audience(
        self,
        name: str,
        query_id: str,
        description: str | None = None,
        ttl_days: int = 365,
        destinations: list[str] | None = None,
    ) -> JSONData:
        """创建受众"""
        data: dict[str, Any] = {
            "name": name,
            "queryId": query_id,
            "ttlDays": ttl_days,
        }
        if description:
            data["description"] = description
        if destinations:
            data["destinations"] = destinations

        result = await self.post("/amc/audiences", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_audience(self, audience_id: str) -> JSONData:
        """获取受众详情"""
        result = await self.get(f"/amc/audiences/{audience_id}")
        return result if isinstance(result, dict) else {}

    async def update_audience(
        self,
        audience_id: str,
        name: str | None = None,
        description: str | None = None,
        ttl_days: int | None = None,
    ) -> JSONData:
        """更新受众"""
        data: dict[str, Any] = {}
        if name:
            data["name"] = name
        if description:
            data["description"] = description
        if ttl_days:
            data["ttlDays"] = ttl_days

        result = await self.put(f"/amc/audiences/{audience_id}", json_data=data)
        return result if isinstance(result, dict) else {}

    async def delete_audience(self, audience_id: str) -> JSONData:
        """删除受众"""
        result = await self.delete(f"/amc/audiences/{audience_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 受众刷新 ====================

    async def refresh_audience(self, audience_id: str) -> JSONData:
        """刷新受众数据"""
        result = await self.post(f"/amc/audiences/{audience_id}/refresh")
        return result if isinstance(result, dict) else {}

    async def get_refresh_status(
        self,
        audience_id: str,
        refresh_id: str,
    ) -> JSONData:
        """获取刷新状态"""
        result = await self.get(f"/amc/audiences/{audience_id}/refreshes/{refresh_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 受众分析 ====================

    async def get_audience_size(self, audience_id: str) -> JSONData:
        """获取受众规模"""
        result = await self.get(f"/amc/audiences/{audience_id}/size")
        return result if isinstance(result, dict) else {}

    async def get_audience_overlap(self, audience_ids: list[str]) -> JSONData:
        """获取受众重叠分析"""
        params = {"audienceIds": ",".join(audience_ids)}
        result = await self.get("/amc/audiences/overlap", params=params)
        return result if isinstance(result, dict) else {}

    # ==================== 目标配置 ====================

    async def add_destination(
        self,
        audience_id: str,
        destination: str,
    ) -> JSONData:
        """添加投放目标"""
        data = {"destination": destination}
        result = await self.post(f"/amc/audiences/{audience_id}/destinations", json_data=data)
        return result if isinstance(result, dict) else {}

    async def remove_destination(
        self,
        audience_id: str,
        destination: str,
    ) -> JSONData:
        """移除投放目标"""
        result = await self.delete(f"/amc/audiences/{audience_id}/destinations/{destination}")
        return result if isinstance(result, dict) else {}
