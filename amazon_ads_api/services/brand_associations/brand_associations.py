"""
Brand Associations API - 品牌关联 (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/amazon-ads/1-0/brand-associations
用于管理品牌与广告账户的关联关系
"""

from typing import Any, Dict, List, Optional
from amazon_ads_api.base import BaseAdsClient, JSONData


class BrandAssociationsAPI(BaseAdsClient):
    """
    Brand Associations API (全异步)
    
    用于管理品牌与广告账户的关联，包括：
    - 查询品牌关联
    - 创建品牌关联
    - 更新品牌关联状态
    """
    
    async def list_brand_associations(
        self,
        *,
        brand_entity_id: Optional[str] = None,
        association_status: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """
        获取品牌关联列表
        
        Args:
            brand_entity_id: 品牌实体ID筛选
            association_status: 关联状态筛选 (ACTIVE, PENDING, REJECTED)
            max_results: 每页数量
            next_token: 分页令牌
        """
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if brand_entity_id:
            request_body["brandEntityId"] = brand_entity_id
        if association_status:
            request_body["associationStatus"] = association_status
        if next_token:
            request_body["nextToken"] = next_token
            
        result = await self.post(
            "/adsApi/v1/query/brandAssociations",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"brandAssociations": []}
    
    async def get_brand_association(
        self,
        brand_association_id: str,
    ) -> JSONData:
        """获取品牌关联详情"""
        result = await self.get(f"/brands/associations/{brand_association_id}")
        return result if isinstance(result, dict) else {}
    
    async def create_brand_association(
        self,
        *,
        brand_entity_id: str,
        advertiser_id: str,
        association_type: str = "ADVERTISER",
    ) -> JSONData:
        """
        创建品牌关联
        
        Args:
            brand_entity_id: 品牌实体ID
            advertiser_id: 广告商ID
            association_type: 关联类型
        """
        result = await self.post(
            "/brands/associations",
            json_data={
                "brandEntityId": brand_entity_id,
                "advertiserId": advertiser_id,
                "associationType": association_type,
            }
        )
        return result if isinstance(result, dict) else {}
    
    async def update_brand_association(
        self,
        brand_association_id: str,
        *,
        status: str,
    ) -> JSONData:
        """
        更新品牌关联状态
        
        Args:
            brand_association_id: 品牌关联ID
            status: 新状态 (ACTIVE, INACTIVE)
        """
        result = await self.put(
            f"/brands/associations/{brand_association_id}",
            json_data={"status": status}
        )
        return result if isinstance(result, dict) else {}
    
    async def delete_brand_association(
        self,
        brand_association_id: str,
    ) -> JSONData:
        """删除品牌关联"""
        result = await self.delete(f"/brands/associations/{brand_association_id}")
        return result if isinstance(result, dict) else {}
    
    async def list_brands(
        self,
        *,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """获取可关联的品牌列表"""
        params: Dict[str, Any] = {"maxResults": max_results}
        if next_token:
            params["nextToken"] = next_token
        result = await self.get("/brands", params=params)
        return result if isinstance(result, dict) else {"brands": []}
    
    async def get_brand(
        self,
        brand_entity_id: str,
    ) -> JSONData:
        """获取品牌详情"""
        result = await self.get(f"/brands/{brand_entity_id}")
        return result if isinstance(result, dict) else {}
