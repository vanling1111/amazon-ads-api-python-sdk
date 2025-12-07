"""
Product Selector API

官方文档: https://advertising.amazon.com/API/docs/en-us/products
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/ProductSelector_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class ProductSelectorAPI(BaseAdsClient):
    """Product Selector API - 产品选择器
    
    获取可用于广告的产品元数据。
    """
    
    # ==================== 产品搜索 ====================
    
    async def search_products(
        self,
        query: str,
        max_results: int = 100,
        filters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """搜索产品
        
        Args:
            query: 搜索关键词（ASIN、SKU或产品名称）
            max_results: 最大结果数
            filters: 过滤条件
            
        Returns:
            产品搜索结果
        """
        data = {
            "query": query,
            "maxResults": max_results,
        }
        if filters:
            data["filters"] = filters
            
        return await self._make_request(
            "POST",
            "/products/search",
            json=data,
        )
    
    async def get_products_by_asins(
        self,
        asins: List[str],
    ) -> List[Dict[str, Any]]:
        """根据ASIN获取产品信息
        
        Args:
            asins: ASIN列表
            
        Returns:
            产品信息列表
        """
        data = {"asins": asins}
        response = await self._make_request(
            "POST",
            "/products/byAsins",
            json=data,
        )
        return response.get("products", [])
    
    async def get_products_by_skus(
        self,
        skus: List[str],
    ) -> List[Dict[str, Any]]:
        """根据SKU获取产品信息
        
        Args:
            skus: SKU列表
            
        Returns:
            产品信息列表
        """
        data = {"skus": skus}
        response = await self._make_request(
            "POST",
            "/products/bySkus",
            json=data,
        )
        return response.get("products", [])
    
    # ==================== 产品详情 ====================
    
    async def get_product_metadata(
        self,
        asin: str,
    ) -> Dict[str, Any]:
        """获取产品元数据
        
        Args:
            asin: 产品ASIN
            
        Returns:
            产品元数据
        """
        return await self._make_request(
            "GET",
            f"/products/{asin}/metadata",
        )
    
    async def get_product_categories(
        self,
        asin: str,
    ) -> List[Dict[str, Any]]:
        """获取产品类目
        
        Args:
            asin: 产品ASIN
            
        Returns:
            类目列表
        """
        response = await self._make_request(
            "GET",
            f"/products/{asin}/categories",
        )
        return response.get("categories", [])
    
    # ==================== 产品列表 ====================
    
    async def list_advertised_products(
        self,
        state: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取已投放广告的产品列表
        
        Args:
            state: 状态 (ACTIVE, PAUSED, ARCHIVED)
            max_results: 最大结果数
            next_token: 分页token
            
        Returns:
            产品列表
        """
        params = {"maxResults": max_results}
        if state:
            params["state"] = state
        if next_token:
            params["nextToken"] = next_token
            
        return await self._make_request(
            "GET",
            "/products/advertised",
            params=params,
        )
    
    async def list_eligible_products(
        self,
        ad_type: str,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取可投放广告的产品列表
        
        Args:
            ad_type: 广告类型 (SP, SB, SD)
            max_results: 最大结果数
            next_token: 分页token
            
        Returns:
            可投放广告的产品列表
        """
        params = {
            "adType": ad_type,
            "maxResults": max_results,
        }
        if next_token:
            params["nextToken"] = next_token
            
        return await self._make_request(
            "GET",
            "/products/eligible",
            params=params,
        )
    
    # ==================== 品牌和类目 ====================
    
    async def list_brands(self) -> List[Dict[str, Any]]:
        """获取品牌列表
        
        Returns:
            品牌列表
        """
        response = await self._make_request(
            "GET",
            "/products/brands",
        )
        return response.get("brands", [])
    
    async def list_categories(
        self,
        parent_id: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """获取类目列表
        
        Args:
            parent_id: 父类目ID（获取子类目）
            
        Returns:
            类目列表
        """
        params = {}
        if parent_id:
            params["parentId"] = parent_id
            
        response = await self._make_request(
            "GET",
            "/products/categories",
            params=params if params else None,
        )
        return response.get("categories", [])

