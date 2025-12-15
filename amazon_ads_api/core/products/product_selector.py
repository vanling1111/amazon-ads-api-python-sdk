"""
Amazon Ads Product Selector API (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/product-selector
OpenAPI Spec: ProductSelector_prod_3p.json

产品元数据查询
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


# Content-Type 常量
PRODUCT_METADATA_REQUEST = "application/vnd.productmetadatarequest.v1+json"
PRODUCT_METADATA_RESPONSE = "application/vnd.productmetadataresponse.v1+json"


class ProductSelectorAPI(BaseAdsClient):
    """
    Product Selector API (全异步)
    
    官方端点 (共1个):
    - POST /product/metadata - 获取产品元数据
    
    支持的商家类型:
    - Seller（卖家）
    - Vendor（供应商）
    - Author（作者）
    """

    async def get_product_metadata(
        self,
        page_index: int = 0,
        page_size: int = 50,
        asins: list[str] | None = None,
        skus: list[str] | None = None,
        search_str: str | None = None,
        ad_type: str | None = None,
        check_eligibility: bool = False,
        check_item_details: bool = False,
        is_global_store_selection: bool = False,
        sort_by: str | None = None,
        sort_order: str = "DESC",
        cursor_token: str | None = None,
        locale: str | None = None,
    ) -> JSONData:
        """
        获取产品元数据
        
        POST /product/metadata
        
        Args:
            page_index: 页索引（从0开始）
            page_size: 每页数量（1-300，默认50）
            asins: ASIN 列表（最多300个，不能与 skus/search_str 同时使用）
            skus: SKU 列表（最多300个，不能与 asins/search_str 同时使用）
            search_str: 搜索字符串（产品标题模糊搜索，不能与 asins/skus 同时使用）
            ad_type: 广告类型（检查资格时必需）
                - SP: Sponsored Products
                - SB: Sponsored Brands
                - SD: Sponsored Display
            check_eligibility: 是否检查广告资格
            check_item_details: 是否返回产品详情（名称、图片、价格）
            is_global_store_selection: 是否只返回全球开店商品
            sort_by: 排序方式（仅 SP 卖家支持）
                - SUGGESTED: 推荐排序（最可能产生点击）
                - CREATED_DATE: 创建日期排序
            sort_order: 排序顺序
                - ASC: 升序
                - DESC: 降序（推荐排序必须是 DESC）
            cursor_token: 分页 token（用于推荐排序或作者账户）
            locale: 响应语言（如 "zh_CN"）
        
        Returns:
            {
                "ProductMetadataList": [
                    {
                        "asin": "B0018OFKJS",
                        "sku": "SKU1",
                        "title": "产品名称",
                        "brand": "品牌",
                        "category": "类目",
                        "imageUrl": "https://...",
                        "availability": "IN_STOCK",
                        "eligibilityStatus": "ELIGIBLE",
                        "ineligibilityCodes": [],
                        "ineligibilityReasons": [],
                        "priceToPay": {"amount": 3.99, "currency": "USD"},
                        "basisPrice": {"amount": 6.99, "currency": "USD"},
                        "bestSellerRank": "36",
                        "createdDate": "Jul 1, 2021",
                        "variationList": ["ASIN1", "ASIN2"],
                        "globalStoreSetting": {"catalogSourceCountryCode": "US"}
                    }
                ],
                "cursorToken": "..."
            }
            
        库存状态 (availability):
            - IN_STOCK: 有库存
            - IN_STOCK_SCARCE: 库存紧张
            - OUT_OF_STOCK: 缺货
            - PREORDER: 预售
            - LEADTIME: 需要交付时间
            - AVAILABLE_DATE: 未来某日期可用
        """
        body: JSONData = {
            "pageIndex": page_index,
            "pageSize": page_size,
        }
        
        # 只能使用一种输入方式
        if asins:
            body["asins"] = asins[:300]
        elif skus:
            body["skus"] = skus[:300]
        elif search_str:
            body["searchStr"] = search_str[:200]
        
        if ad_type:
            body["adType"] = ad_type
        if check_eligibility:
            body["checkEligibility"] = True
        if check_item_details:
            body["checkItemDetails"] = True
        if is_global_store_selection:
            body["isGlobalStoreSelection"] = True
        if sort_by:
            body["sortBy"] = sort_by
        if sort_order != "DESC":
            body["sortOrder"] = sort_order
        if cursor_token:
            body["cursorToken"] = cursor_token
        if locale:
            body["locale"] = locale
        
        result = await self.post(
            "/product/metadata",
            json_data=body,
            content_type=PRODUCT_METADATA_REQUEST,
            accept=PRODUCT_METADATA_RESPONSE
        )
        return result if isinstance(result, dict) else {"ProductMetadataList": []}

    # ============ 便捷方法 ============

    async def get_products_by_asins(
        self,
        asins: list[str],
        check_eligibility: bool = False,
        ad_type: str = "SP",
    ) -> JSONList:
        """
        按 ASIN 批量获取产品信息
        
        Args:
            asins: ASIN 列表（最多300个）
            check_eligibility: 是否检查广告资格
            ad_type: 广告类型（检查资格时使用）
        """
        result = await self.get_product_metadata(
            asins=asins,
            page_index=0,
            page_size=len(asins),
            check_eligibility=check_eligibility,
            check_item_details=True,
            ad_type=ad_type if check_eligibility else None,
        )
        return result.get("ProductMetadataList", [])

    async def get_products_by_skus(
        self,
        skus: list[str],
        check_eligibility: bool = False,
    ) -> JSONList:
        """
        按 SKU 批量获取产品信息
        
        Args:
            skus: SKU 列表（最多300个）
            check_eligibility: 是否检查广告资格
        """
        result = await self.get_product_metadata(
            skus=skus,
            page_index=0,
            page_size=len(skus),
            check_eligibility=check_eligibility,
            check_item_details=True,
            ad_type="SP" if check_eligibility else None,
        )
        return result.get("ProductMetadataList", [])

    async def search_products(
        self,
        query: str,
        page_size: int = 50,
        check_eligibility: bool = False,
    ) -> JSONList:
        """
        搜索产品（按标题模糊匹配）
        
        Args:
            query: 搜索关键词
            page_size: 返回数量
            check_eligibility: 是否检查广告资格
        """
        result = await self.get_product_metadata(
            search_str=query,
            page_index=0,
            page_size=page_size,
            check_eligibility=check_eligibility,
            check_item_details=True,
            ad_type="SP" if check_eligibility else None,
        )
        return result.get("ProductMetadataList", [])

    async def get_suggested_products(
        self,
        page_size: int = 50,
        cursor_token: str | None = None,
    ) -> JSONData:
        """
        获取推荐产品（最可能产生点击的产品）
        
        仅支持 SP 卖家
        """
        return await self.get_product_metadata(
            page_index=0,
            page_size=page_size,
            sort_by="SUGGESTED",
            sort_order="DESC",
            check_item_details=True,
            cursor_token=cursor_token,
        )

    async def get_eligible_products(
        self,
        ad_type: str = "SP",
        page_size: int = 50,
        page_index: int = 0,
    ) -> JSONList:
        """
        获取符合广告资格的产品
        
        Args:
            ad_type: SP, SB, SD
        """
        result = await self.get_product_metadata(
            page_index=page_index,
            page_size=page_size,
            check_eligibility=True,
            check_item_details=True,
            ad_type=ad_type,
        )
        
        # 过滤出符合资格的产品
        products = result.get("ProductMetadataList", [])
        return [p for p in products if p.get("eligibilityStatus") == "ELIGIBLE"]

    async def check_asin_eligibility(self, asin: str, ad_type: str = "SP") -> JSONData:
        """
        检查单个 ASIN 的广告资格
        """
        products = await self.get_products_by_asins(
            asins=[asin],
            check_eligibility=True,
            ad_type=ad_type,
        )
        return products[0] if products else {}

    async def get_all_products(
        self,
        page_size: int = 300,
        max_pages: int = 35,  # 最多 10500 个产品
    ) -> JSONList:
        """
        获取所有产品（自动分页）
        
        注意：结果最多 10000 个产品
        """
        all_products: JSONList = []
        
        for page_index in range(max_pages):
            result = await self.get_product_metadata(
                page_index=page_index,
                page_size=page_size,
                check_item_details=True,
            )
            
            products = result.get("ProductMetadataList", [])
            if not products:
                break
            
            all_products.extend(products)
            
            # 检查是否还有更多数据
            if len(products) < page_size:
                break
        
        return all_products
