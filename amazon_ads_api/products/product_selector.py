"""
Amazon Ads Product Selector API (异步版本)
产品选择器
"""

from typing import Any
from ..base import BaseAdsClient, JSONData, JSONList


class ProductSelectorAPI(BaseAdsClient):
    """Product Selector API (全异步)"""

    # ==================== 产品搜索 ====================

    async def search_products(
        self,
        query: str,
        max_results: int = 100,
        filters: dict[str, Any] | None = None,
    ) -> JSONData:
        """搜索产品"""
        data: dict[str, Any] = {
            "query": query,
            "maxResults": max_results,
        }
        if filters:
            data["filters"] = filters

        result = await self.post("/products/search", json_data=data)
        return result if isinstance(result, dict) else {"products": []}

    async def get_products_by_asins(self, asins: list[str]) -> JSONList:
        """根据ASIN获取产品信息"""
        data = {"asins": asins}
        response = await self.post("/products/byAsins", json_data=data)
        if isinstance(response, dict):
            return response.get("products", [])
        return []

    async def get_products_by_skus(self, skus: list[str]) -> JSONList:
        """根据SKU获取产品信息"""
        data = {"skus": skus}
        response = await self.post("/products/bySkus", json_data=data)
        if isinstance(response, dict):
            return response.get("products", [])
        return []

    # ==================== 产品详情 ====================

    async def get_product_metadata(self, asin: str) -> JSONData:
        """获取产品元数据"""
        result = await self.get(f"/products/{asin}/metadata")
        return result if isinstance(result, dict) else {}

    async def get_product_categories(self, asin: str) -> JSONList:
        """获取产品类目"""
        response = await self.get(f"/products/{asin}/categories")
        if isinstance(response, dict):
            return response.get("categories", [])
        return []

    # ==================== 产品列表 ====================

    async def list_advertised_products(
        self,
        state: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取已投放广告的产品列表"""
        params: dict[str, Any] = {"maxResults": max_results}
        if state:
            params["state"] = state
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/products/advertised", params=params)
        return result if isinstance(result, dict) else {"products": []}

    async def list_eligible_products(
        self,
        ad_type: str,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取可投放广告的产品列表"""
        params: dict[str, Any] = {
            "adType": ad_type,
            "maxResults": max_results,
        }
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/products/eligible", params=params)
        return result if isinstance(result, dict) else {"products": []}

    # ==================== 品牌和类目 ====================

    async def list_brands(self) -> JSONList:
        """获取品牌列表"""
        response = await self.get("/products/brands")
        if isinstance(response, dict):
            return response.get("brands", [])
        return []

    async def list_categories(self, parent_id: str | None = None) -> JSONList:
        """获取类目列表"""
        params = {}
        if parent_id:
            params["parentId"] = parent_id

        response = await self.get("/products/categories", params=params if params else None)
        if isinstance(response, dict):
            return response.get("categories", [])
        return []
