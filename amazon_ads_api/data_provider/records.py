"""
Data Provider Records API

官方文档: https://advertising.amazon.com/API/docs/en-us/data-provider
OpenAPI: https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/data-provider/openapi.yaml
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class DataProviderRecordsAPI(BaseAdsClient):
    """Data Provider Records API - 数据记录管理
    
    上传和管理数据提供商的数据记录。
    """
    
    # ==================== 记录上传 ====================
    
    async def upload_records(
        self,
        source_id: str,
        records: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """上传数据记录
        
        Args:
            source_id: 数据源ID
            records: 数据记录列表
            
        Returns:
            上传结果
        """
        data = {
            "sourceId": source_id,
            "records": records,
        }
        return await self._make_request(
            "POST",
            "/dataProvider/records",
            json=data,
        )
    
    async def upload_records_batch(
        self,
        source_id: str,
        file_url: str,
        file_format: str = "JSON",
    ) -> Dict[str, Any]:
        """批量上传数据记录
        
        Args:
            source_id: 数据源ID
            file_url: 数据文件URL
            file_format: 文件格式 (JSON, CSV)
            
        Returns:
            上传任务信息
        """
        data = {
            "sourceId": source_id,
            "fileUrl": file_url,
            "fileFormat": file_format,
        }
        return await self._make_request(
            "POST",
            "/dataProvider/records/batch",
            json=data,
        )
    
    async def get_upload_status(
        self,
        upload_id: str,
    ) -> Dict[str, Any]:
        """获取上传状态
        
        Args:
            upload_id: 上传任务ID
            
        Returns:
            上传状态
        """
        return await self._make_request(
            "GET",
            f"/dataProvider/records/uploads/{upload_id}",
        )
    
    # ==================== 记录查询 ====================
    
    async def list_records(
        self,
        source_id: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取数据记录列表
        
        Args:
            source_id: 数据源ID
            start_date: 开始日期
            end_date: 结束日期
            max_results: 最大结果数
            next_token: 分页token
            
        Returns:
            记录列表
        """
        params = {
            "sourceId": source_id,
            "maxResults": max_results,
        }
        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date
        if next_token:
            params["nextToken"] = next_token
            
        return await self._make_request(
            "GET",
            "/dataProvider/records",
            params=params,
        )
    
    # ==================== 用户删除 ====================
    
    async def delete_user_data(
        self,
        user_identifiers: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """删除用户数据
        
        Args:
            user_identifiers: 用户标识符列表，每个包含:
                - type: 标识符类型 (EMAIL, PHONE, etc.)
                - value: 哈希后的标识符值
                
        Returns:
            删除结果
        """
        data = {"userIdentifiers": user_identifiers}
        return await self._make_request(
            "POST",
            "/dataProvider/users/delete",
            json=data,
        )
    
    async def get_deletion_status(
        self,
        deletion_id: str,
    ) -> Dict[str, Any]:
        """获取删除状态
        
        Args:
            deletion_id: 删除请求ID
            
        Returns:
            删除状态
        """
        return await self._make_request(
            "GET",
            f"/dataProvider/users/delete/{deletion_id}",
        )

