"""
Localization API - 本地化 (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/localization
官方规范: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Localization_prod_3p.json

官方端点 (共4个):
- POST /currencies/localize - 本地化货币
- POST /keywords/localize - 本地化关键词
- POST /products/localize - 本地化产品
- POST /targetingExpression/localize - 本地化定向表达式
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class LocalizationAPI(BaseAdsClient):
    """
    Localization API - 广告内容本地化 (全异步)
    
    API Tier: L1
    Source: OpenAPI
    OpenAPI Spec: Localization_prod_3p.json
    Stability: 高
    
    官方端点 (共4个):
    - POST /currencies/localize - 本地化货币
    - POST /keywords/localize - 本地化关键词
    - POST /products/localize - 本地化产品
    - POST /targetingExpression/localize - 本地化定向表达式
    """

    async def localize_currencies(
        self,
        localize_currency_requests: list[dict[str, Any]],
    ) -> JSONData:
        """
        本地化货币
        
        官方端点: POST /currencies/localize
        官方规范: Localization_prod_3p.json
        
        Args:
            localize_currency_requests: 货币本地化请求列表
                [
                    {
                        "sourceCurrency": "USD",
                        "targetCurrency": "EUR",
                        "amount": 100.0,
                        ...
                    }
                ]
            
        Returns:
            本地化结果
        """
        result = await self.post(
            "/currencies/localize",
            json_data={"localizeCurrencyRequests": localize_currency_requests},
        )
        return result if isinstance(result, dict) else {}

    async def localize_keywords(
        self,
        localize_keyword_requests: list[dict[str, Any]],
    ) -> JSONData:
        """
        本地化关键词
        
        官方端点: POST /keywords/localize
        官方规范: Localization_prod_3p.json
        
        Args:
            localize_keyword_requests: 关键词本地化请求列表
                [
                    {
                        "sourceKeyword": "running shoes",
                        "sourceLocale": "en_US",
                        "targetLocale": "de_DE",
                        ...
                    }
                ]
            
        Returns:
            本地化结果 (包含翻译后的关键词)
        """
        result = await self.post(
            "/keywords/localize",
            json_data={"localizeKeywordRequests": localize_keyword_requests},
        )
        return result if isinstance(result, dict) else {}

    async def localize_products(
        self,
        localize_product_requests: list[dict[str, Any]],
    ) -> JSONData:
        """
        本地化产品
        
        官方端点: POST /products/localize
        官方规范: Localization_prod_3p.json
        
        Args:
            localize_product_requests: 产品本地化请求列表
                [
                    {
                        "sourceAsin": "B08N5WRWNW",
                        "sourceMarketplaceId": "ATVPDKIKX0DER",
                        "targetMarketplaceId": "A1PA6795UKMFR9",
                        ...
                    }
                ]
            
        Returns:
            本地化结果 (包含目标市场的产品映射)
        """
        result = await self.post(
            "/products/localize",
            json_data={"localizeProductRequests": localize_product_requests},
        )
        return result if isinstance(result, dict) else {}

    async def localize_targeting_expression(
        self,
        localize_targeting_expression_requests: list[dict[str, Any]],
    ) -> JSONData:
        """
        本地化定向表达式
        
        官方端点: POST /targetingExpression/localize
        官方规范: Localization_prod_3p.json
        
        Args:
            localize_targeting_expression_requests: 定向表达式本地化请求列表
                [
                    {
                        "sourceTargetingExpression": {...},
                        "sourceLocale": "en_US",
                        "targetLocale": "de_DE",
                        ...
                    }
                ]
            
        Returns:
            本地化结果 (包含翻译后的定向表达式)
        """
        result = await self.post(
            "/targetingExpression/localize",
            json_data={"localizeTargetingExpressionRequests": localize_targeting_expression_requests},
        )
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def localize_keyword(
        self,
        keyword: str,
        source_locale: str,
        target_locale: str,
    ) -> str | None:
        """
        翻译单个关键词
        
        Args:
            keyword: 源关键词
            source_locale: 源语言区域 (如 "en_US")
            target_locale: 目标语言区域 (如 "de_DE")
            
        Returns:
            翻译后的关键词，失败返回 None
        """
        result = await self.localize_keywords([
            {
                "sourceKeyword": keyword,
                "sourceLocale": source_locale,
                "targetLocale": target_locale,
            }
        ])
        responses = result.get("localizeKeywordResponses", [])
        if responses and responses[0].get("success"):
            return responses[0].get("targetKeyword")
        return None

    async def localize_product(
        self,
        asin: str,
        source_marketplace_id: str,
        target_marketplace_id: str,
    ) -> str | None:
        """
        获取产品在目标市场的 ASIN
        
        Args:
            asin: 源 ASIN
            source_marketplace_id: 源市场 ID
            target_marketplace_id: 目标市场 ID
            
        Returns:
            目标市场的 ASIN，未找到返回 None
        """
        result = await self.localize_products([
            {
                "sourceAsin": asin,
                "sourceMarketplaceId": source_marketplace_id,
                "targetMarketplaceId": target_marketplace_id,
            }
        ])
        responses = result.get("localizeProductResponses", [])
        if responses and responses[0].get("success"):
            return responses[0].get("targetAsin")
        return None

    async def convert_currency(
        self,
        amount: float,
        source_currency: str,
        target_currency: str,
    ) -> float | None:
        """
        货币转换
        
        Args:
            amount: 金额
            source_currency: 源货币 (如 "USD")
            target_currency: 目标货币 (如 "EUR")
            
        Returns:
            转换后的金额，失败返回 None
        """
        result = await self.localize_currencies([
            {
                "sourceCurrency": source_currency,
                "targetCurrency": target_currency,
                "amount": amount,
            }
        ])
        responses = result.get("localizeCurrencyResponses", [])
        if responses and responses[0].get("success"):
            return responses[0].get("targetAmount")
        return None
