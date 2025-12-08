"""
Amazon Ads Persona Builder API (异步版本)
人群画像构建
"""

from typing import Any
from ..base import BaseAdsClient, JSONData, JSONList


class PersonaBuilderAPI(BaseAdsClient):
    """Persona Builder API (全异步)"""

    # ==================== 人群画像管理 ====================

    async def list_personas(
        self,
        state: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取人群画像列表"""
        params: dict[str, Any] = {"maxResults": max_results}
        if state:
            params["state"] = state
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/personas", params=params)
        return result if isinstance(result, dict) else {"personas": []}

    async def create_persona(
        self,
        name: str,
        description: str | None = None,
        demographics: dict[str, Any] | None = None,
        interests: list[str] | None = None,
        behaviors: list[str] | None = None,
        purchase_history: dict[str, Any] | None = None,
    ) -> JSONData:
        """创建人群画像"""
        data: dict[str, Any] = {"name": name}
        if description:
            data["description"] = description
        if demographics:
            data["demographics"] = demographics
        if interests:
            data["interests"] = interests
        if behaviors:
            data["behaviors"] = behaviors
        if purchase_history:
            data["purchaseHistory"] = purchase_history

        result = await self.post("/personas", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_persona(self, persona_id: str) -> JSONData:
        """获取画像详情"""
        result = await self.get(f"/personas/{persona_id}")
        return result if isinstance(result, dict) else {}

    async def update_persona(
        self,
        persona_id: str,
        name: str | None = None,
        description: str | None = None,
        demographics: dict[str, Any] | None = None,
        interests: list[str] | None = None,
        behaviors: list[str] | None = None,
    ) -> JSONData:
        """更新人群画像"""
        data: dict[str, Any] = {}
        if name:
            data["name"] = name
        if description:
            data["description"] = description
        if demographics:
            data["demographics"] = demographics
        if interests:
            data["interests"] = interests
        if behaviors:
            data["behaviors"] = behaviors

        result = await self.put(f"/personas/{persona_id}", json_data=data)
        return result if isinstance(result, dict) else {}

    async def delete_persona(self, persona_id: str) -> JSONData:
        """删除人群画像"""
        result = await self.delete(f"/personas/{persona_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 画像分析 ====================

    async def get_persona_size(self, persona_id: str) -> JSONData:
        """获取画像人群规模"""
        result = await self.get(f"/personas/{persona_id}/size")
        return result if isinstance(result, dict) else {}

    async def get_persona_insights(self, persona_id: str) -> JSONData:
        """获取画像洞察"""
        result = await self.get(f"/personas/{persona_id}/insights")
        return result if isinstance(result, dict) else {}

    async def compare_personas(self, persona_ids: list[str]) -> JSONData:
        """比较多个画像"""
        params = {"personaIds": ",".join(persona_ids)}
        result = await self.get("/personas/compare", params=params)
        return result if isinstance(result, dict) else {}

    # ==================== 画像属性 ====================

    async def list_available_demographics(self) -> JSONList:
        """获取可用人口统计属性"""
        response = await self.get("/personas/demographics")
        if isinstance(response, dict):
            return response.get("demographics", [])
        return []

    async def list_available_interests(self) -> JSONList:
        """获取可用兴趣标签"""
        response = await self.get("/personas/interests")
        if isinstance(response, dict):
            return response.get("interests", [])
        return []

    async def list_available_behaviors(self) -> JSONList:
        """获取可用行为标签"""
        response = await self.get("/personas/behaviors")
        if isinstance(response, dict):
            return response.get("behaviors", [])
        return []
