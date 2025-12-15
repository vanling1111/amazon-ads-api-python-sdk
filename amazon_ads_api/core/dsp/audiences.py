"""
Amazon DSP - Audiences API (异步版本)

官方端点 (1个):
- POST /dsp/audiences - 创建受众

官方规范: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/ADSPAudiences_prod_3p.json

⚠️ 重要说明：
- 官方 API 仅支持创建受众，不支持列出/获取/更新/删除
- audienceType 必须是枚举值之一，不能使用 "CUSTOM"
- 所有字段都有严格的验证规则
"""

from typing import Literal
from uuid import uuid4
from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


# 官方定义的受众类型枚举
AudienceType = Literal[
    "PRODUCT_PURCHASES",
    "PRODUCT_SEARCH", 
    "PRODUCT_SIMS",
    "PRODUCT_VIEWS",
    "WHOLE_FOODS_MARKET_PURCHASES",
]

# 官方定义的国家代码枚举
CountryCode = Literal[
    "AE", "AU", "BR", "CA", "DE", "ES", "FR", "GB", 
    "IN", "IT", "JP", "MX", "NL", "SA", "SE", "TR", "US",
]


class DSPAudiencesAPI(BaseAdsClient):
    """
    DSP Audiences API (全异步)
    
    官方 API 仅支持创建受众，其他操作需通过 Amazon DSP 控制台完成。
    
    API Tier: L1
    Source: ADSPAudiences_prod_3p.json
    OpenAPI: ✅
    
    支持的受众类型:
    - PRODUCT_PURCHASES: 购买过指定产品的用户 (回溯 1-365 天)
    - PRODUCT_VIEWS: 浏览过指定产品的用户 (回溯 1-90 天)
    - PRODUCT_SEARCH: 搜索过指定产品的用户 (回溯 1-90 天)
    - PRODUCT_SIMS: 浏览过相似产品的用户 (回溯 1-90 天)
    - WHOLE_FOODS_MARKET_PURCHASES: Whole Foods 购买用户 (回溯 1-365 天)
    """

    # 各受众类型的回溯天数限制
    LOOKBACK_LIMITS = {
        "PRODUCT_PURCHASES": (1, 365),
        "PRODUCT_VIEWS": (1, 90),
        "PRODUCT_SEARCH": (1, 90),
        "PRODUCT_SIMS": (1, 90),
        "WHOLE_FOODS_MARKET_PURCHASES": (1, 365),
    }
    
    # 各受众类型的最大 ASIN 数量
    MAX_ASINS = {
        "PRODUCT_PURCHASES": 1000,
        "PRODUCT_VIEWS": 1000,
        "PRODUCT_SEARCH": 1000,
        "PRODUCT_SIMS": 1000,
        "WHOLE_FOODS_MARKET_PURCHASES": 500,
    }

    async def create_audience(
        self,
        advertiser_id: str,
        name: str,
        description: str,
        audience_type: AudienceType,
        asins: list[str],
        lookback: int,
        country: CountryCode | None = None,
        idempotency_key: str | None = None,
    ) -> JSONData:
        """
        创建 DSP 受众
        
        官方端点: POST /dsp/audiences
        Content-Type: application/vnd.dspaudiences.v1+json
        
        Args:
            advertiser_id: 广告主 ID (必填，作为查询参数)
            name: 受众名称 (1-128 字符)
            description: 受众描述 (1-1000 字符)
            audience_type: 受众类型，必须是以下之一:
                - PRODUCT_PURCHASES: 购买用户
                - PRODUCT_VIEWS: 浏览用户
                - PRODUCT_SEARCH: 搜索用户
                - PRODUCT_SIMS: 相似产品用户
                - WHOLE_FOODS_MARKET_PURCHASES: Whole Foods 购买用户
            asins: ASIN 列表 (1-1000 个，Whole Foods 最多 500 个)
            lookback: 回溯天数
                - PRODUCT_PURCHASES: 1-365 天
                - PRODUCT_VIEWS/SEARCH/SIMS: 1-90 天
                - WHOLE_FOODS_MARKET_PURCHASES: 1-365 天
            country: ISO Alpha-2 国家代码 (Global Account 必填)
            idempotency_key: 幂等键 (UUID 格式，可选，默认自动生成)
            
        Returns:
            {
                "success": [
                    {
                        "audienceId": "xxx",
                        "idempotencyKey": "xxx",
                        "index": 0
                    }
                ],
                "error": []
            }
            
        Raises:
            ValueError: 参数验证失败
        """
        # 参数验证
        self._validate_params(audience_type, asins, lookback, name, description)
        
        # 生成幂等键
        if not idempotency_key:
            idempotency_key = str(uuid4())
        
        # 构建规则
        rule = {
            "attributeType": "ASIN",
            "attributeValues": asins,
            "clause": "INCLUDE",
            "operator": "ONE_OF",
        }
        
        # 构建请求体
        body: JSONData = {
            "audienceType": audience_type,
            "name": name,
            "description": description,
            "lookback": lookback,
            "idempotencyKey": idempotency_key,
            "rules": [rule],
        }
        
        if country:
            body["country"] = country
        
        # 发送请求 (注意：请求体是数组)
        result = await self.post(
            "/dsp/audiences",
            json_data=[body],
            params={"advertiserId": advertiser_id},
            content_type="application/vnd.dspaudiences.v1+json",
            accept="application/vnd.dspaudiencesresponse.v1+json",
        )
        
        return result if isinstance(result, dict) else {"success": [], "error": []}

    def _validate_params(
        self,
        audience_type: str,
        asins: list[str],
        lookback: int,
        name: str,
        description: str,
    ) -> None:
        """验证参数"""
        # 验证受众类型
        valid_types = list(self.LOOKBACK_LIMITS.keys())
        if audience_type not in valid_types:
            raise ValueError(
                f"Invalid audience_type: {audience_type}. "
                f"Must be one of: {valid_types}"
            )
        
        # 验证名称
        if not name or len(name) < 1 or len(name) > 128:
            raise ValueError("name must be 1-128 characters")
        
        # 验证描述
        if not description or len(description) < 1 or len(description) > 1000:
            raise ValueError("description must be 1-1000 characters")
        
        # 验证 ASIN 数量
        max_asins = self.MAX_ASINS.get(audience_type, 1000)
        if not asins or len(asins) < 1 or len(asins) > max_asins:
            raise ValueError(
                f"asins must contain 1-{max_asins} items for {audience_type}"
            )
        
        # 验证回溯天数
        min_lookback, max_lookback = self.LOOKBACK_LIMITS.get(audience_type, (1, 365))
        if lookback < min_lookback or lookback > max_lookback:
            raise ValueError(
                f"lookback must be {min_lookback}-{max_lookback} days for {audience_type}"
            )

    # ============ 便捷方法 ============

    async def create_product_views_audience(
        self,
        advertiser_id: str,
        name: str,
        description: str,
        asins: list[str],
        lookback: int = 30,
        country: CountryCode | None = None,
    ) -> JSONData:
        """
        创建产品浏览受众
        
        定向浏览过指定产品的用户。
        
        Args:
            advertiser_id: 广告主 ID
            name: 受众名称
            description: 受众描述
            asins: ASIN 列表 (最多 1000 个)
            lookback: 回溯天数 (1-90，默认 30)
            country: 国家代码
        """
        return await self.create_audience(
            advertiser_id=advertiser_id,
            name=name,
            description=description,
            audience_type="PRODUCT_VIEWS",
            asins=asins,
            lookback=lookback,
            country=country,
        )

    async def create_product_purchases_audience(
        self,
        advertiser_id: str,
        name: str,
        description: str,
        asins: list[str],
        lookback: int = 180,
        country: CountryCode | None = None,
    ) -> JSONData:
        """
        创建产品购买受众
        
        定向购买过指定产品的用户。
        
        Args:
            advertiser_id: 广告主 ID
            name: 受众名称
            description: 受众描述
            asins: ASIN 列表 (最多 1000 个)
            lookback: 回溯天数 (1-365，默认 180)
            country: 国家代码
        """
        return await self.create_audience(
            advertiser_id=advertiser_id,
            name=name,
            description=description,
            audience_type="PRODUCT_PURCHASES",
            asins=asins,
            lookback=lookback,
            country=country,
        )

    async def create_product_search_audience(
        self,
        advertiser_id: str,
        name: str,
        description: str,
        asins: list[str],
        lookback: int = 30,
        country: CountryCode | None = None,
    ) -> JSONData:
        """
        创建产品搜索受众
        
        定向搜索过指定产品的用户。
        
        Args:
            advertiser_id: 广告主 ID
            name: 受众名称
            description: 受众描述
            asins: ASIN 列表 (最多 1000 个)
            lookback: 回溯天数 (1-90，默认 30)
            country: 国家代码
        """
        return await self.create_audience(
            advertiser_id=advertiser_id,
            name=name,
            description=description,
            audience_type="PRODUCT_SEARCH",
            asins=asins,
            lookback=lookback,
            country=country,
        )

    async def create_similar_products_audience(
        self,
        advertiser_id: str,
        name: str,
        description: str,
        asins: list[str],
        lookback: int = 30,
        country: CountryCode | None = None,
    ) -> JSONData:
        """
        创建相似产品受众
        
        定向浏览过相似产品的用户。
        
        Args:
            advertiser_id: 广告主 ID
            name: 受众名称
            description: 受众描述
            asins: ASIN 列表 (最多 1000 个)
            lookback: 回溯天数 (1-90，默认 30)
            country: 国家代码
        """
        return await self.create_audience(
            advertiser_id=advertiser_id,
            name=name,
            description=description,
            audience_type="PRODUCT_SIMS",
            asins=asins,
            lookback=lookback,
            country=country,
        )
