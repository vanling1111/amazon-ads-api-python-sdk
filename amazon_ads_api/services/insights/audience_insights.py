"""
Amazon Ads Audience Insights API

官方文档: https://advertising.amazon.com/API/docs/en-us/reference
OpenAPI规范: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Insights_prod_3p.json

⚠️ 官方只有一个端点: GET /insights/audiences/{audienceId}/overlappingAudiences
"""

from typing import Literal
from amazon_ads_api.base import BaseAdsClient, JSONData


# Content-Type 常量
INSIGHTS_V2_CONTENT_TYPE = "application/vnd.insightsaudiencesoverlap.v2+json"


class AudienceInsightsAPI(BaseAdsClient):
    """
    Audience Insights API
    
    官方端点 (共1个):
    - GET /insights/audiences/{audienceId}/overlappingAudiences
    """

    async def get_overlapping_audiences(
        self,
        audience_id: str,
        ad_type: Literal["DSP", "SD"],
        advertiser_id: str | None = None,
        minimum_overlap_affinity: float | None = None,
        maximum_overlap_affinity: float | None = None,
        audience_category: list[str] | None = None,
        max_results: int = 30,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取与指定受众重叠的受众列表
        
        官方端点: GET /insights/audiences/{audienceId}/overlappingAudiences
        
        Args:
            audience_id: 受众ID
            ad_type: 广告类型 ("DSP" 或 "SD")
            advertiser_id: 广告主ID (DSP必填，SD可选)
            minimum_overlap_affinity: 最小亲和度过滤
            maximum_overlap_affinity: 最大亲和度过滤
            audience_category: 受众类别过滤 (最多20个)
            max_results: 最大结果数 (1-500，默认30)
            next_token: 分页token
            
        Returns:
            {
                "marketplace": str,
                "nextToken": str | None,
                "overlappingAudiences": [
                    {
                        "affinity": float,
                        "audienceMetadata": {
                            "audienceId": str,
                            "category": str,
                            "name": str,
                            "audienceForecast": {...}
                        }
                    }
                ],
                "requestedAudienceMetadata": {...}
            }
        """
        params: dict = {
            "adType": ad_type,
            "maxResults": max_results,
        }
        
        if advertiser_id:
            params["advertiserId"] = advertiser_id
        if minimum_overlap_affinity is not None:
            params["minimumOverlapAffinity"] = minimum_overlap_affinity
        if maximum_overlap_affinity is not None:
            params["maximumOverlapAffinity"] = maximum_overlap_affinity
        if audience_category:
            params["audienceCategory"] = ",".join(audience_category[:20])
        if next_token:
            params["nextToken"] = next_token
        
        result = await self.get(
            f"/insights/audiences/{audience_id}/overlappingAudiences",
            params=params,
            accept=INSIGHTS_V2_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def get_all_overlapping_audiences(
        self,
        audience_id: str,
        ad_type: Literal["DSP", "SD"],
        advertiser_id: str | None = None,
        max_pages: int = 10,
    ) -> list[JSONData]:
        """
        获取所有重叠受众（自动分页）
        
        Args:
            audience_id: 受众ID
            ad_type: 广告类型
            advertiser_id: 广告主ID
            max_pages: 最大页数限制
            
        Returns:
            所有重叠受众列表
        """
        all_audiences = []
        next_token = None
        
        for _ in range(max_pages):
            result = await self.get_overlapping_audiences(
                audience_id=audience_id,
                ad_type=ad_type,
                advertiser_id=advertiser_id,
                max_results=500,
                next_token=next_token,
            )
            
            audiences = result.get("overlappingAudiences", [])
            all_audiences.extend(audiences)
            
            next_token = result.get("nextToken")
            if not next_token:
                break
        
        return all_audiences
