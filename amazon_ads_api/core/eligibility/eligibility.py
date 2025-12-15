"""
Amazon Ads Eligibility API (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/eligibility
OpenAPI Spec: Eligibility_prod_3p.json

广告资格检查
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


# Content-Type 常量
PROGRAM_ELIGIBILITY_V2 = "application/vnd.programeligibility.v2+json"


class EligibilityAPI(BaseAdsClient):
    """
    Eligibility API (全异步)
    
    官方端点 (共2个):
    - POST /eligibility/product/list - 检查产品广告资格
    - POST /eligibility/programs - 检查项目资格
    """

    # ============ Product Eligibility ============

    async def check_product_eligibility(
        self,
        products: list[dict],
        ad_type: str = "sp",
        locale: str | None = None,
    ) -> JSONData:
        """
        检查产品广告资格
        
        POST /eligibility/product/list
        
        Args:
            products: 产品列表，每个产品包含:
                - asin: 必需，Amazon 产品标识符
                - sku: 可选，卖家产品标识符
                - globalStoreSetting: 可选，全球开店设置
                    - catalogSourceCountryCode: 源市场国家代码
            ad_type: 广告类型
                - "sp": Sponsored Products
                - "sb": Sponsored Brands
                - "sd": Sponsored Display
                - "dsp": Demand Side Platform
            locale: 响应语言，如 "en_US"
        
        Returns:
            {
                "productResponseList": [
                    {
                        "productDetails": {"asin": "B001...", "sku": "..."},
                        "overallStatus": "ELIGIBLE" | "ELIGIBLE_WITH_WARNING" | "INELIGIBLE",
                        "eligibilityStatusList": [
                            {
                                "name": "OUT_OF_STOCK",
                                "message": "Product is out of stock",
                                "severity": "INELIGIBLE",
                                "helpUrl": "https://..."
                            }
                        ]
                    }
                ]
            }
            
        状态说明:
            - ELIGIBLE: 产品可以投放广告
            - ELIGIBLE_WITH_WARNING: 产品可投放但可能不会获得展示
            - INELIGIBLE: 产品不能投放广告
            
        不符资格原因:
            - ADULT_PRODUCT: 成人产品
            - CLOSED_CATEGORY: 关闭的类目
            - INELIGIBLE_CONDITION: 不符合条件
            - INELIGIBLE_OFFER: 不符合的报价
            - INELIGIBLE_PRODUCT_COST: 价格不符合
            - LISTING_SUPRESSED: 列表被屏蔽
            - MISSING_IMAGE: 缺少图片
            - MISSING_TITLE: 缺少标题
            - NOT_IN_BUYBOX: 没有购买按钮
            - OUT_OF_STOCK: 缺货
            - RESTRICTED_CATEGORY: 受限类目
            - VARIATION_PARENT: 变体父商品
        """
        body: JSONData = {
            "adType": ad_type,
            "productDetailsList": products,
        }
        
        if locale:
            body["locale"] = locale
        
        result = await self.post("/eligibility/product/list", json_data=body)
        return result if isinstance(result, dict) else {"productResponseList": []}

    async def check_program_eligibility(
        self,
        skip_all_billing_checks: bool = False,
    ) -> JSONData:
        """
        检查账户项目资格 (v1)
        
        POST /eligibility/programs
        
        Args:
            skip_all_billing_checks: 是否跳过账单检查
        
        Returns:
            {
                "eligibilityStatusMap": {
                    "SB": {
                        "eligible": true/false,
                        "reasons": [
                            {
                                "code": "NO_BRAND_RELATIONS",
                                "description": "...",
                                "level": "INELIGIBLE" | "INELIGIBLE_WITH_RESOLUTION"
                            }
                        ]
                    },
                    "SD": {...},
                    "DTC": {...},
                    "MAAS": {...},
                    "SPOT": {...}
                }
            }
            
        项目说明:
            - SB: Sponsored Brands
            - SD: Sponsored Display
            - DTC: Direct to Consumer
            - MAAS: Marketing as a Service
            - SPOT: Sponsored Products
        """
        body: JSONData = {}
        
        if skip_all_billing_checks:
            body["skipChecks"] = {"skipAllBillingChecks": True}
        
        result = await self.post("/eligibility/programs", json_data=body)
        return result if isinstance(result, dict) else {"eligibilityStatusMap": {}}

    async def check_program_eligibility_v2(
        self,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        检查账户项目资格 (v2 - 支持分页和多市场)
        
        POST /eligibility/programs
        Content-Type: application/vnd.programeligibility.v2+json
        
        Args:
            max_results: 最大结果数 (1-100)
            next_token: 分页 token
        
        Returns:
            {
                "eligibilityStatusLists": [
                    {
                        "marketplaceId": "ATVPDKIKX0DER",
                        "eligibilityStatusList": [
                            {
                                "adProgram": "SB",
                                "eligible": false,
                                "reasons": [...]
                            }
                        ]
                    }
                ],
                "nextToken": "..."
            }
        """
        body: JSONData = {"maxResults": max_results}
        
        if next_token:
            body["nextToken"] = next_token
        
        result = await self.post(
            "/eligibility/programs",
            json_data=body,
            content_type=PROGRAM_ELIGIBILITY_V2,
            accept=PROGRAM_ELIGIBILITY_V2
        )
        return result if isinstance(result, dict) else {"eligibilityStatusLists": []}

    # ============ 便捷方法 ============

    async def check_asin_eligibility(
        self,
        asin: str,
        ad_type: str = "sp",
    ) -> JSONData:
        """
        检查单个 ASIN 的广告资格
        
        Args:
            asin: Amazon 产品标识符
            ad_type: 广告类型 (sp, sb, sd, dsp)
        """
        result = await self.check_product_eligibility(
            products=[{"asin": asin}],
            ad_type=ad_type
        )
        responses = result.get("productResponseList", [])
        return responses[0] if responses else {}

    async def check_asins_eligibility(
        self,
        asins: list[str],
        ad_type: str = "sp",
    ) -> JSONData:
        """
        批量检查 ASIN 广告资格
        
        Args:
            asins: ASIN 列表（最多 50 个）
            ad_type: 广告类型
        """
        products = [{"asin": asin} for asin in asins[:50]]
        return await self.check_product_eligibility(products=products, ad_type=ad_type)

    async def get_eligible_asins(
        self,
        asins: list[str],
        ad_type: str = "sp",
    ) -> list[str]:
        """
        过滤出符合广告资格的 ASIN
        
        Returns:
            符合资格的 ASIN 列表
        """
        result = await self.check_asins_eligibility(asins, ad_type)
        eligible_asins = []
        
        for response in result.get("productResponseList", []):
            if response.get("overallStatus") in ["ELIGIBLE", "ELIGIBLE_WITH_WARNING"]:
                asin = response.get("productDetails", {}).get("asin")
                if asin:
                    eligible_asins.append(asin)
        
        return eligible_asins

    async def is_asin_eligible(self, asin: str, ad_type: str = "sp") -> bool:
        """检查单个 ASIN 是否符合广告资格"""
        result = await self.check_asin_eligibility(asin, ad_type)
        status = result.get("overallStatus", "")
        return status in ["ELIGIBLE", "ELIGIBLE_WITH_WARNING"]

    async def is_eligible_for_program(self, program: str) -> bool:
        """
        检查是否有资格投放特定广告项目
        
        Args:
            program: SB, SD, DTC, MAAS, SPOT
        """
        result = await self.check_program_eligibility()
        status_map = result.get("eligibilityStatusMap", {})
        program_status = status_map.get(program.upper(), {})
        return program_status.get("eligible", False)

    async def is_eligible_for_sb(self) -> bool:
        """检查是否有资格投放 Sponsored Brands"""
        return await self.is_eligible_for_program("SB")

    async def is_eligible_for_sd(self) -> bool:
        """检查是否有资格投放 Sponsored Display"""
        return await self.is_eligible_for_program("SD")

    async def is_eligible_for_sp(self) -> bool:
        """检查是否有资格投放 Sponsored Products"""
        return await self.is_eligible_for_program("SPOT")

    async def get_ineligibility_reasons(self, program: str) -> list[dict]:
        """
        获取特定项目不符资格的原因
        
        Returns:
            [
                {"code": "NO_BRAND_RELATIONS", "description": "...", "level": "..."}
            ]
        """
        result = await self.check_program_eligibility()
        status_map = result.get("eligibilityStatusMap", {})
        program_status = status_map.get(program.upper(), {})
        return program_status.get("reasons", [])
