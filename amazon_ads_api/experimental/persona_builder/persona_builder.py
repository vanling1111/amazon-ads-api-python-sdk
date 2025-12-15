"""
Amazon Ads Persona Builder API (异步版本)

官方 Spec: PersonaBuilder.json
验证日期: 2024-12-15

官方端点数: 5
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData


class PersonaBuilderAPI(BaseAdsClient):
    """
    Persona Builder API (全异步)
    
    API Tier: L1
    Source: OpenAPI
    OpenAPI_SPEC: PersonaBuilder.json
    Stability: Beta
    
    用于获取受众洞察，构建用户画像。
    官方验证: 5个端点
    """

    async def get_banded_size(
        self,
        audience_ids: list[str],
        marketplace_id: str | None = None,
    ) -> JSONData:
        """
        获取受众分级规模
        
        官方端点: POST /insights/bandedSize
        
        Args:
            audience_ids: 受众 ID 列表
            marketplace_id: 市场 ID
            
        Returns:
            受众规模分级信息
        """
        body: dict[str, Any] = {"audienceIds": audience_ids}
        
        if marketplace_id:
            body["marketplaceId"] = marketplace_id
        
        result = await self.post("/insights/bandedSize", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_demographics(
        self,
        audience_ids: list[str],
        marketplace_id: str | None = None,
        dimensions: list[str] | None = None,
    ) -> JSONData:
        """
        获取受众人口统计数据
        
        官方端点: POST /insights/demographics
        
        Args:
            audience_ids: 受众 ID 列表
            marketplace_id: 市场 ID
            dimensions: 维度列表 (AGE, GENDER, INCOME, EDUCATION 等)
            
        Returns:
            人口统计洞察数据
        """
        body: dict[str, Any] = {"audienceIds": audience_ids}
        
        if marketplace_id:
            body["marketplaceId"] = marketplace_id
        if dimensions:
            body["dimensions"] = dimensions
        
        result = await self.post("/insights/demographics", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_prime_video_insights(
        self,
        audience_ids: list[str],
        marketplace_id: str | None = None,
    ) -> JSONData:
        """
        获取受众 Prime Video 观看洞察
        
        官方端点: POST /insights/primeVideo
        
        Args:
            audience_ids: 受众 ID 列表
            marketplace_id: 市场 ID
            
        Returns:
            Prime Video 观看偏好洞察
        """
        body: dict[str, Any] = {"audienceIds": audience_ids}
        
        if marketplace_id:
            body["marketplaceId"] = marketplace_id
        
        result = await self.post("/insights/primeVideo", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_top_categories_purchased(
        self,
        audience_ids: list[str],
        marketplace_id: str | None = None,
        max_results: int = 10,
    ) -> JSONData:
        """
        获取受众购买的热门品类
        
        官方端点: POST /insights/topCategoriesPurchased
        
        Args:
            audience_ids: 受众 ID 列表
            marketplace_id: 市场 ID
            max_results: 返回的品类数量
            
        Returns:
            热门购买品类列表
        """
        body: dict[str, Any] = {
            "audienceIds": audience_ids,
            "maxResults": max_results,
        }
        
        if marketplace_id:
            body["marketplaceId"] = marketplace_id
        
        result = await self.post("/insights/topCategoriesPurchased", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_top_overlapping_audiences(
        self,
        audience_ids: list[str],
        marketplace_id: str | None = None,
        max_results: int = 10,
    ) -> JSONData:
        """
        获取与指定受众重叠度最高的其他受众
        
        官方端点: POST /insights/topOverlappingAudiences
        
        Args:
            audience_ids: 受众 ID 列表
            marketplace_id: 市场 ID
            max_results: 返回的受众数量
            
        Returns:
            重叠受众列表及重叠度指标
        """
        body: dict[str, Any] = {
            "audienceIds": audience_ids,
            "maxResults": max_results,
        }
        
        if marketplace_id:
            body["marketplaceId"] = marketplace_id
        
        result = await self.post("/insights/topOverlappingAudiences", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def get_complete_persona(
        self,
        audience_ids: list[str],
        marketplace_id: str | None = None,
    ) -> JSONData:
        """
        获取完整的用户画像（聚合所有洞察）
        
        Args:
            audience_ids: 受众 ID 列表
            marketplace_id: 市场 ID
            
        Returns:
            {
                "bandedSize": {...},
                "demographics": {...},
                "primeVideo": {...},
                "topCategories": {...},
                "overlappingAudiences": {...}
            }
        """
        # 并行获取所有洞察
        results = await self.parallel_execute([
            self.get_banded_size(audience_ids, marketplace_id),
            self.get_demographics(audience_ids, marketplace_id),
            self.get_prime_video_insights(audience_ids, marketplace_id),
            self.get_top_categories_purchased(audience_ids, marketplace_id),
            self.get_top_overlapping_audiences(audience_ids, marketplace_id),
        ])
        
        return {
            "bandedSize": results[0] if not isinstance(results[0], Exception) else {},
            "demographics": results[1] if not isinstance(results[1], Exception) else {},
            "primeVideo": results[2] if not isinstance(results[2], Exception) else {},
            "topCategories": results[3] if not isinstance(results[3], Exception) else {},
            "overlappingAudiences": results[4] if not isinstance(results[4], Exception) else {},
        }

