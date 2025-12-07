"""
Hashed Records API

官方文档: https://advertising.amazon.com/API/docs/en-us/data-provider
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/HashedRecords_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class HashedRecordsAPI(BaseAdsClient):
    """Hashed Records API - 哈希记录管理
    
    上传和管理哈希后的用户数据记录。
    """
    
    # ==================== 哈希记录上传 ====================
    
    async def upload_hashed_records(
        self,
        audience_id: str,
        records: List[Dict[str, Any]],
        hash_type: str = "SHA256",
    ) -> Dict[str, Any]:
        """上传哈希记录
        
        Args:
            audience_id: 受众ID
            records: 哈希记录列表，每个包含:
                - hashedEmail: 哈希后的邮箱（可选）
                - hashedPhone: 哈希后的电话（可选）
                - hashedMaid: 哈希后的移动广告ID（可选）
            hash_type: 哈希类型 (SHA256)
            
        Returns:
            上传结果
        """
        data = {
            "audienceId": audience_id,
            "records": records,
            "hashType": hash_type,
        }
        return await self._make_request(
            "POST",
            "/hashedRecords",
            json=data,
        )
    
    async def upload_hashed_records_batch(
        self,
        audience_id: str,
        file_url: str,
        hash_type: str = "SHA256",
    ) -> Dict[str, Any]:
        """批量上传哈希记录
        
        Args:
            audience_id: 受众ID
            file_url: 数据文件URL
            hash_type: 哈希类型
            
        Returns:
            上传任务信息
        """
        data = {
            "audienceId": audience_id,
            "fileUrl": file_url,
            "hashType": hash_type,
        }
        return await self._make_request(
            "POST",
            "/hashedRecords/batch",
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
            f"/hashedRecords/uploads/{upload_id}",
        )
    
    # ==================== 受众管理 ====================
    
    async def list_hashed_audiences(self) -> List[Dict[str, Any]]:
        """获取哈希受众列表
        
        Returns:
            受众列表
        """
        response = await self._make_request(
            "GET",
            "/hashedRecords/audiences",
        )
        return response.get("audiences", [])
    
    async def create_hashed_audience(
        self,
        name: str,
        description: Optional[str] = None,
        ttl_days: int = 365,
    ) -> Dict[str, Any]:
        """创建哈希受众
        
        Args:
            name: 受众名称
            description: 描述
            ttl_days: 数据保留天数
            
        Returns:
            创建的受众
        """
        data = {
            "name": name,
            "ttlDays": ttl_days,
        }
        if description:
            data["description"] = description
            
        return await self._make_request(
            "POST",
            "/hashedRecords/audiences",
            json=data,
        )
    
    async def get_hashed_audience(
        self,
        audience_id: str,
    ) -> Dict[str, Any]:
        """获取哈希受众详情
        
        Args:
            audience_id: 受众ID
            
        Returns:
            受众详情
        """
        return await self._make_request(
            "GET",
            f"/hashedRecords/audiences/{audience_id}",
        )
    
    async def delete_hashed_audience(
        self,
        audience_id: str,
    ) -> None:
        """删除哈希受众
        
        Args:
            audience_id: 受众ID
        """
        await self._make_request(
            "DELETE",
            f"/hashedRecords/audiences/{audience_id}",
        )
    
    # ==================== 记录删除 ====================
    
    async def remove_hashed_records(
        self,
        audience_id: str,
        records: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """从受众中移除哈希记录
        
        Args:
            audience_id: 受众ID
            records: 要移除的记录列表
            
        Returns:
            移除结果
        """
        data = {
            "audienceId": audience_id,
            "records": records,
        }
        return await self._make_request(
            "POST",
            "/hashedRecords/remove",
            json=data,
        )

