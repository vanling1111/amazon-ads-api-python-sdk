"""
Amazon Ads Data Provider Records API (异步版本)
数据记录管理
"""

from typing import Any
from ..base import BaseAdsClient, JSONData


class DataProviderRecordsAPI(BaseAdsClient):
    """Data Provider Records API (全异步)"""

    # ==================== 记录上传 ====================

    async def upload_records(
        self,
        source_id: str,
        records: list[dict[str, Any]],
    ) -> JSONData:
        """上传数据记录"""
        data = {
            "sourceId": source_id,
            "records": records,
        }
        result = await self.post("/dataProvider/records", json_data=data)
        return result if isinstance(result, dict) else {}

    async def upload_records_batch(
        self,
        source_id: str,
        file_url: str,
        file_format: str = "JSON",
    ) -> JSONData:
        """批量上传数据记录"""
        data = {
            "sourceId": source_id,
            "fileUrl": file_url,
            "fileFormat": file_format,
        }
        result = await self.post("/dataProvider/records/batch", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_upload_status(self, upload_id: str) -> JSONData:
        """获取上传状态"""
        result = await self.get(f"/dataProvider/records/uploads/{upload_id}")
        return result if isinstance(result, dict) else {}

    # ==================== 记录查询 ====================

    async def list_records(
        self,
        source_id: str,
        start_date: str | None = None,
        end_date: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取数据记录列表"""
        params: dict[str, Any] = {
            "sourceId": source_id,
            "maxResults": max_results,
        }
        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/dataProvider/records", params=params)
        return result if isinstance(result, dict) else {"records": []}

    # ==================== 用户删除 ====================

    async def delete_user_data(
        self,
        user_identifiers: list[dict[str, Any]],
    ) -> JSONData:
        """删除用户数据"""
        data = {"userIdentifiers": user_identifiers}
        result = await self.post("/dataProvider/users/delete", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_deletion_status(self, deletion_id: str) -> JSONData:
        """获取删除状态"""
        result = await self.get(f"/dataProvider/users/delete/{deletion_id}")
        return result if isinstance(result, dict) else {}
