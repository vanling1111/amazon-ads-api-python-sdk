"""
Brand Home API - 品牌主页 (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/brand-home
官方规范: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/BrandHome_prod_3p.json

官方端点 (共2个):
- POST /brand/stores/v1/storePages/list - 列出商店页面
- POST /brand/stores/v1/stores/list - 列出商店
"""

from typing import Literal
from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


# Content-Type
BH_STORES_LIST_CONTENT_TYPE = "application/vnd.bhstoreslist.v1+json"
BH_PAGES_LIST_CONTENT_TYPE = "application/brandStores.ListPages.v1+json"

# 标识符类型
IdentifierType = Literal["ASIN", "BRAND_AID_ID", "ENTITY_ID", "GCOR", "NODE", "STORE"]


class BrandHomeAPI(BaseAdsClient):
    """
    Brand Home API - 管理品牌主页 (全异步)
    
    API Tier: L1
    Source: OpenAPI
    OpenAPI Spec: BrandHome_prod_3p.json
    Stability: 高
    
    官方端点 (共2个):
    - POST /brand/stores/v1/storePages/list - 列出商店页面
    - POST /brand/stores/v1/stores/list - 列出商店
    """

    async def list_store_pages(
        self,
        identifier: str,
        identifier_type: IdentifierType,
        *,
        max_results: int = 30,
        next_token: str | None = None,
    ) -> JSONData:
        """
        列出商店页面
        
        官方端点: POST /brand/stores/v1/storePages/list
        官方规范: BrandHome_prod_3p.json
        
        Args:
            identifier: 请求的商店标识符 (支持 brand/sub-entityId 和 storeId)
            identifier_type: 标识符类型 (ASIN, BRAND_AID_ID, ENTITY_ID, GCOR, NODE, STORE)
            max_results: 每页最大数量 (1-30, 默认30)
            next_token: 分页令牌
            
        Returns:
            {
                "storePages": [
                    {
                        "pageId": "...",
                        "pageName": "...",
                        "pageUrl": "...",
                        ...
                    }
                ],
                "nextToken": "..."
            }
        """
        request_body: JSONData = {
            "identifier": identifier,
            "identifierType": identifier_type,
        }
        
        if max_results != 30:
            request_body["maxResults"] = max_results
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post(
            "/brand/stores/v1/storePages/list",
            json_data=request_body,
            content_type=BH_PAGES_LIST_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {"storePages": []}

    async def list_stores(
        self,
        *,
        identifier: str | None = None,
        identifier_type: IdentifierType | None = None,
        max_results: int = 30,
        next_token: str | None = None,
    ) -> JSONData:
        """
        列出商店
        
        官方端点: POST /brand/stores/v1/stores/list
        官方规范: BrandHome_prod_3p.json
        
        Args:
            identifier: 可选 - 请求的实体标识符 (支持 Advertiser entityId)
            identifier_type: 可选 - 标识符类型
            max_results: 每页最大数量 (1-30, 默认30)
            next_token: 分页令牌
            
        Returns:
            {
                "stores": [
                    {
                        "storeId": "...",
                        "storeName": "...",
                        "storeUrl": "...",
                        ...
                    }
                ],
                "nextToken": "..."
            }
        """
        request_body: JSONData = {}
        
        if identifier:
            request_body["identifier"] = identifier
        if identifier_type:
            request_body["identifierType"] = identifier_type
        if max_results != 30:
            request_body["maxResults"] = max_results
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post(
            "/brand/stores/v1/stores/list",
            json_data=request_body if request_body else None,
            content_type=BH_STORES_LIST_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {"stores": []}

    # ============ 便捷方法 ============

    async def list_all_stores(
        self,
        identifier: str | None = None,
        identifier_type: IdentifierType | None = None,
    ) -> JSONList:
        """
        获取所有商店 (自动分页)
        
        Args:
            identifier: 可选 - 实体标识符
            identifier_type: 可选 - 标识符类型
            
        Returns:
            所有商店列表
        """
        all_stores: JSONList = []
        next_token = None
        
        while True:
            result = await self.list_stores(
                identifier=identifier,
                identifier_type=identifier_type,
                max_results=30,
                next_token=next_token,
            )
            stores = result.get("stores", [])
            all_stores.extend(stores)
            
            next_token = result.get("nextToken")
            if not next_token or not stores:
                break
        
        return all_stores

    async def list_all_store_pages(
        self,
        identifier: str,
        identifier_type: IdentifierType,
    ) -> JSONList:
        """
        获取所有商店页面 (自动分页)
        
        Args:
            identifier: 商店标识符
            identifier_type: 标识符类型
            
        Returns:
            所有商店页面列表
        """
        all_pages: JSONList = []
        next_token = None
        
        while True:
            result = await self.list_store_pages(
                identifier=identifier,
                identifier_type=identifier_type,
                max_results=30,
                next_token=next_token,
            )
            pages = result.get("storePages", [])
            all_pages.extend(pages)
            
            next_token = result.get("nextToken")
            if not next_token or not pages:
                break
        
        return all_pages

    async def get_store_by_entity_id(self, entity_id: str) -> JSONData | None:
        """
        根据 Entity ID 获取商店
        
        Args:
            entity_id: 实体 ID
            
        Returns:
            商店信息，未找到返回 None
        """
        result = await self.list_stores(
            identifier=entity_id,
            identifier_type="ENTITY_ID",
            max_results=1,
        )
        stores = result.get("stores", [])
        return stores[0] if stores else None
