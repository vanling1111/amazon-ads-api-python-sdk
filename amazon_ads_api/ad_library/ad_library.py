"""
Ad Library API - 广告库服务

提供广告内容的搜索和查看功能，包括：
- 广告搜索
- 广告详情获取
- 广告筛选

官方文档: https://advertising.amazon.com/API/docs/en-us/ad-library
"""

from typing import Any, Dict, List, Optional
from enum import Enum

from ..base import BaseAdsClient


class AdType(str, Enum):
    """广告类型"""
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    DSP = "DSP"


class NameMatchType(str, Enum):
    """名称匹配类型"""
    EXACT = "EXACT"
    CONTAINS = "CONTAINS"
    STARTS_WITH = "STARTS_WITH"


class AdLibraryAPI(BaseAdsClient):
    """
    Ad Library API - 广告库
    
    用于搜索和查看Amazon平台上的广告内容
    """
    
    # ==================== 广告搜索 ====================
    
    async def list_ads(
        self,
        *,
        advertiser_name: Optional[str] = None,
        name_match_type: Optional[NameMatchType] = None,
        ad_types: Optional[List[AdType]] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        marketplace_ids: Optional[List[str]] = None,
        page_token: Optional[str] = None,
        page_size: int = 100,
    ) -> Dict[str, Any]:
        """
        搜索广告列表
        
        Args:
            advertiser_name: 广告主名称筛选
            name_match_type: 名称匹配类型
            ad_types: 广告类型筛选
            start_date: 开始日期 (YYYY-MM-DD)
            end_date: 结束日期 (YYYY-MM-DD)
            marketplace_ids: 市场ID列表
            page_token: 分页令牌
            page_size: 每页数量
            
        Returns:
            广告列表响应
        """
        request_body = {
            "pageSize": page_size,
        }
        
        if advertiser_name:
            request_body["advertiserName"] = advertiser_name
        if name_match_type:
            request_body["nameMatchType"] = name_match_type.value
        if ad_types:
            request_body["adTypes"] = [t.value for t in ad_types]
        if start_date:
            request_body["startDate"] = start_date
        if end_date:
            request_body["endDate"] = end_date
        if marketplace_ids:
            request_body["marketplaceIds"] = marketplace_ids
        if page_token:
            request_body["pageToken"] = page_token
            
        return await self._request(
            "POST",
            "/adLibrary/ads/list",
            json=request_body
        )
    
    async def get_ads_by_id(
        self,
        ad_ids: List[str],
    ) -> Dict[str, Any]:
        """
        根据ID获取广告详情
        
        Args:
            ad_ids: 广告ID列表
            
        Returns:
            广告详情响应
        """
        return await self._request(
            "POST",
            "/adLibrary/ads",
            json={"adIds": ad_ids}
        )
    
    # ==================== 广告主搜索 ====================
    
    async def search_advertisers(
        self,
        *,
        query: str,
        marketplace_ids: Optional[List[str]] = None,
        page_size: int = 100,
    ) -> Dict[str, Any]:
        """
        搜索广告主
        
        Args:
            query: 搜索关键词
            marketplace_ids: 市场ID列表
            page_size: 每页数量
            
        Returns:
            广告主列表响应
        """
        request_body = {
            "query": query,
            "pageSize": page_size,
        }
        
        if marketplace_ids:
            request_body["marketplaceIds"] = marketplace_ids
            
        return await self._request(
            "POST",
            "/adLibrary/advertisers/search",
            json=request_body
        )
    
    # ==================== 统计信息 ====================
    
    async def get_ad_statistics(
        self,
        *,
        advertiser_id: str,
        start_date: str,
        end_date: str,
        granularity: str = "DAILY",
    ) -> Dict[str, Any]:
        """
        获取广告统计信息
        
        Args:
            advertiser_id: 广告主ID
            start_date: 开始日期
            end_date: 结束日期
            granularity: 时间粒度 (DAILY, WEEKLY, MONTHLY)
            
        Returns:
            统计信息响应
        """
        return await self._request(
            "POST",
            "/adLibrary/statistics",
            json={
                "advertiserId": advertiser_id,
                "startDate": start_date,
                "endDate": end_date,
                "granularity": granularity,
            }
        )
    
    # ==================== 类别和筛选 ====================
    
    async def get_categories(
        self,
        marketplace_id: str,
    ) -> Dict[str, Any]:
        """
        获取可用的广告类别
        
        Args:
            marketplace_id: 市场ID
            
        Returns:
            类别列表响应
        """
        return await self._request(
            "GET",
            f"/adLibrary/categories",
            params={"marketplaceId": marketplace_id}
        )
    
    async def get_filters(
        self,
        marketplace_id: str,
    ) -> Dict[str, Any]:
        """
        获取可用的筛选选项
        
        Args:
            marketplace_id: 市场ID
            
        Returns:
            筛选选项响应
        """
        return await self._request(
            "GET",
            f"/adLibrary/filters",
            params={"marketplaceId": marketplace_id}
        )

