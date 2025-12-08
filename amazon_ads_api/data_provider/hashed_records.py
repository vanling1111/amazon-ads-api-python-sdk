"""
Amazon Ads Hashed Records API (异步版本)
哈希记录管理
"""

from typing import Any
from ..base import BaseAdsClient, JSONData, JSONList


class HashedRecordsAPI(BaseAdsClient):
    """Hashed Records API (全异步)"""

    # ==================== 哈希记录上传 ====================

    async def upload_hashed_records(
        self,
        audience_id: str,
        records: list[dict[str, Any]],
        hash_type: str = "SHA256",
    ) -> JSONData:
        """上传哈希记录"""
        data = {
            "audienceId": audience_id,
            "records": records,
            "hashType": hash_type,
        }
        result = await self.post("/hashedRecords", json_data=data)
        return result if isinstance(result, dict) else {}

    async def upload_hashed_records_batch(
        self,
        audience_id: str,
        file_url: str,
        hash_type: str = "SHA256",
    ) -> JSONData:
        """批量上传哈希记录"""
        data = {
            "audienceId": audience_id,
            "fileUrl": file_url,
            "hashType": hash_type,
        }
        result = await self.post("/hashedRecords/batch", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_upload_status(self, upload_id: str) -> JSONData:
        """获取上传状态"""
        result = await self.get(f"/hashedRecords/uploads/{upload_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 受众管理 ====================

    async def list_hashed_audiences(self) -> JSONList:
        """获取哈希受众列表"""
        response = await self.get("/hashedRecords/audiences")
        if isinstance(response, dict):
            return response.get("audiences", [])
        return []

    async def create_hashed_audience(
        self,
        name: str,
        description: str | None = None,
        ttl_days: int = 365,
    ) -> JSONData:
        """创建哈希受众"""
        data: dict[str, Any] = {
            "name": name,
            "ttlDays": ttl_days,
        }
        if description:
            data["description"] = description

        result = await self.post("/hashedRecords/audiences", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_hashed_audience(self, audience_id: str) -> JSONData:
        """获取哈希受众详情"""
        result = await self.get(f"/hashedRecords/audiences/{audience_id}")
        return result if isinstance(result, dict) else {}

    async def delete_hashed_audience(self, audience_id: str) -> JSONData:
        """删除哈希受众"""
        result = await self.delete(f"/hashedRecords/audiences/{audience_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 记录删除 ====================

    async def remove_hashed_records(
        self,
        audience_id: str,
        records: list[dict[str, Any]],
    ) -> JSONData:
        """从受众中移除哈希记录"""
        data = {
            "audienceId": audience_id,
            "records": records,
        }
        result = await self.post("/hashedRecords/remove", json_data=data)
        return result if isinstance(result, dict) else {}
