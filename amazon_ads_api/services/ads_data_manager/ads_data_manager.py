"""
Ads Data Manager API - 广告数据管理器 (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/ads-data-manager
用于管理和上传第一方数据用于广告定向
"""

from typing import Any, Dict, List, Optional
from amazon_ads_api.base import BaseAdsClient, JSONData


class AdsDataManagerAPI(BaseAdsClient):
    """
    Ads Data Manager API (全异步)
    
    用于管理广告商的第一方数据，包括：
    - 客户数据上传
    - 数据段管理
    - 匹配率报告
    """
    
    # ==================== 数据源管理 ====================
    
    async def create_data_source(
        self,
        *,
        name: str,
        description: Optional[str] = None,
        data_type: str = "CUSTOMER_DATA",
    ) -> JSONData:
        """创建数据源"""
        request_body: Dict[str, Any] = {
            "name": name,
            "dataType": data_type,
        }
        if description:
            request_body["description"] = description
            
        result = await self.post(
            "/adsDataManager/dataSources",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {}
    
    async def list_data_sources(
        self,
        *,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """获取数据源列表"""
        params: Dict[str, Any] = {"maxResults": max_results}
        if next_token:
            params["nextToken"] = next_token
        result = await self.get("/adsDataManager/dataSources", params=params)
        return result if isinstance(result, dict) else {"dataSources": []}
    
    async def get_data_source(
        self,
        data_source_id: str,
    ) -> JSONData:
        """获取数据源详情"""
        result = await self.get(f"/adsDataManager/dataSources/{data_source_id}")
        return result if isinstance(result, dict) else {}
    
    async def update_data_source(
        self,
        data_source_id: str,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> JSONData:
        """更新数据源"""
        request_body: Dict[str, Any] = {}
        if name:
            request_body["name"] = name
        if description:
            request_body["description"] = description
            
        result = await self.put(
            f"/adsDataManager/dataSources/{data_source_id}",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {}
    
    async def delete_data_source(
        self,
        data_source_id: str,
    ) -> JSONData:
        """删除数据源"""
        result = await self.delete(f"/adsDataManager/dataSources/{data_source_id}")
        return result if isinstance(result, dict) else {}
    
    # ==================== 数据上传 ====================
    
    async def create_upload_url(
        self,
        data_source_id: str,
        *,
        file_name: str,
        content_type: str = "text/csv",
    ) -> JSONData:
        """获取数据上传URL"""
        result = await self.post(
            f"/adsDataManager/dataSources/{data_source_id}/uploads",
            json_data={
                "fileName": file_name,
                "contentType": content_type,
            }
        )
        return result if isinstance(result, dict) else {}
    
    async def list_uploads(
        self,
        data_source_id: str,
        *,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """获取上传历史"""
        params: Dict[str, Any] = {"maxResults": max_results}
        if next_token:
            params["nextToken"] = next_token
        result = await self.get(
            f"/adsDataManager/dataSources/{data_source_id}/uploads",
            params=params
        )
        return result if isinstance(result, dict) else {"uploads": []}
    
    async def get_upload_status(
        self,
        data_source_id: str,
        upload_id: str,
    ) -> JSONData:
        """获取上传状态"""
        result = await self.get(
            f"/adsDataManager/dataSources/{data_source_id}/uploads/{upload_id}"
        )
        return result if isinstance(result, dict) else {}
    
    # ==================== 数据段管理 ====================
    
    async def create_segment(
        self,
        data_source_id: str,
        *,
        name: str,
        description: Optional[str] = None,
        ttl_days: int = 30,
    ) -> JSONData:
        """创建数据段"""
        request_body: Dict[str, Any] = {
            "name": name,
            "ttlDays": ttl_days,
        }
        if description:
            request_body["description"] = description
            
        result = await self.post(
            f"/adsDataManager/dataSources/{data_source_id}/segments",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {}
    
    async def list_segments(
        self,
        data_source_id: str,
        *,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """获取数据段列表"""
        params: Dict[str, Any] = {"maxResults": max_results}
        if next_token:
            params["nextToken"] = next_token
        result = await self.get(
            f"/adsDataManager/dataSources/{data_source_id}/segments",
            params=params
        )
        return result if isinstance(result, dict) else {"segments": []}
    
    async def get_segment(
        self,
        data_source_id: str,
        segment_id: str,
    ) -> JSONData:
        """获取数据段详情"""
        result = await self.get(
            f"/adsDataManager/dataSources/{data_source_id}/segments/{segment_id}"
        )
        return result if isinstance(result, dict) else {}
    
    async def delete_segment(
        self,
        data_source_id: str,
        segment_id: str,
    ) -> JSONData:
        """删除数据段"""
        result = await self.delete(
            f"/adsDataManager/dataSources/{data_source_id}/segments/{segment_id}"
        )
        return result if isinstance(result, dict) else {}
    
    # ==================== 匹配率报告 ====================
    
    async def get_match_rate_report(
        self,
        data_source_id: str,
        *,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取匹配率报告"""
        result = await self.get(
            f"/adsDataManager/dataSources/{data_source_id}/matchRateReport",
            params={
                "startDate": start_date,
                "endDate": end_date,
            }
        )
        return result if isinstance(result, dict) else {}
