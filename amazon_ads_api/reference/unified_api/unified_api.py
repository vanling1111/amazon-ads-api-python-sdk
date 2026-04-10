"""
Amazon Ads API v1 - 统一API (异步版本)

官方 Spec: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p.json
验证日期: 2024-12-15

官方端点 (共40个):
- 核心资源: campaigns, adGroups, ads, targets, adAssociations
- SB 专属: advertisingDeals/sb, advertisingDealTargets/sb, recommendations/sb, etc.
- DSP 专属: commitments/dsp, campaignForecasts/dsp, commitmentSpends/dsp
- 扩展: adExtensions
"""

from typing import Any, Dict, List, Optional
from amazon_ads_api.base import BaseAdsClient, JSONData


class AmazonAdsV1API(BaseAdsClient):
    """
    Amazon Ads API v1 统一入口 (全异步)
    
    官方验证: 40个端点
    提供跨所有Amazon广告产品的统一模型
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 核心资源
        self.ad_associations = AdAssociationsAPI(*args, **kwargs)
        self.ad_groups = AdGroupsAPI(*args, **kwargs)
        self.ads = AdsAPI(*args, **kwargs)
        self.campaigns = CampaignsAPI(*args, **kwargs)
        self.targets = TargetsAPI(*args, **kwargs)
        self.ad_extensions = AdExtensionsAPI(*args, **kwargs)
        # SB 专属资源
        self.sb_advertising_deals = SBAdvertisingDealsAPI(*args, **kwargs)
        self.sb_advertising_deal_targets = SBAdvertisingDealTargetsAPI(*args, **kwargs)
        self.sb_branded_keywords_pricings = SBBrandedKeywordsPricingsAPI(*args, **kwargs)
        self.sb_keyword_reservation_validations = SBKeywordReservationValidationsAPI(*args, **kwargs)
        self.sb_recommendations = SBRecommendationsAPI(*args, **kwargs)
        self.sb_recommendation_types = SBRecommendationTypesAPI(*args, **kwargs)
        # DSP 专属资源
        self.dsp_commitments = DSPCommitmentsAPI(*args, **kwargs)
        self.dsp_commitment_spends = DSPCommitmentSpendsAPI(*args, **kwargs)
        self.dsp_campaign_forecasts = DSPCampaignForecastsAPI(*args, **kwargs)


# ==================== 核心资源 ====================

class AdAssociationsAPI(BaseAdsClient):
    """Ad Associations API (全异步)
    
    官方端点:
    - POST /adsApi/v1/create/adAssociations
    - POST /adsApi/v1/query/adAssociations
    - POST /adsApi/v1/update/adAssociations
    - POST /adsApi/v1/delete/adAssociations
    """
    
    async def create(
        self,
        ad_associations: List[Dict[str, Any]],
    ) -> JSONData:
        """创建 Ad Association - POST /adsApi/v1/create/adAssociations"""
        result = await self.post(
            "/adsApi/v1/create/adAssociations",
            json_data={"adAssociations": ad_associations}
        )
        return result if isinstance(result, dict) else {}
    
    async def query(
        self,
        *,
        ad_association_ids: Optional[List[str]] = None,
        ad_group_ids: Optional[List[str]] = None,
        ad_ids: Optional[List[str]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """查询 Ad Association - POST /adsApi/v1/query/adAssociations"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if ad_association_ids:
            request_body["adAssociationIdFilter"] = {"include": ad_association_ids}
        if ad_group_ids:
            request_body["adGroupIdFilter"] = {"include": ad_group_ids}
        if ad_ids:
            request_body["adIdFilter"] = {"include": ad_ids}
        if next_token:
            request_body["nextToken"] = next_token
            
        result = await self.post(
            "/adsApi/v1/query/adAssociations",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"adAssociations": []}
    
    async def update(
        self,
        ad_associations: List[Dict[str, Any]],
    ) -> JSONData:
        """更新 Ad Association - POST /adsApi/v1/update/adAssociations"""
        result = await self.post(
            "/adsApi/v1/update/adAssociations",
            json_data={"adAssociations": ad_associations}
        )
        return result if isinstance(result, dict) else {}
    
    async def delete(
        self,
        ad_association_ids: List[str],
    ) -> JSONData:
        """删除 Ad Association - POST /adsApi/v1/delete/adAssociations"""
        result = await self.post(
            "/adsApi/v1/delete/adAssociations",
            json_data={"adAssociationIds": ad_association_ids}
        )
        return result if isinstance(result, dict) else {}


class AdGroupsAPI(BaseAdsClient):
    """Ad Groups API v1 (全异步)
    
    官方端点:
    - POST /adsApi/v1/create/adGroups
    - POST /adsApi/v1/query/adGroups
    - POST /adsApi/v1/update/adGroups
    - POST /adsApi/v1/delete/adGroups
    """
    
    async def create(
        self,
        ad_groups: List[Dict[str, Any]],
    ) -> JSONData:
        """创建 Ad Group - POST /adsApi/v1/create/adGroups"""
        result = await self.post(
            "/adsApi/v1/create/adGroups",
            json_data={"adGroups": ad_groups}
        )
        return result if isinstance(result, dict) else {}
    
    async def query(
        self,
        *,
        ad_group_ids: Optional[List[str]] = None,
        campaign_ids: Optional[List[str]] = None,
        ad_product: Optional[str] = None,
        states: Optional[List[str]] = None,
        name_filter: Optional[Dict[str, Any]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """查询 Ad Group - POST /adsApi/v1/query/adGroups"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if ad_group_ids:
            request_body["adGroupIdFilter"] = {"include": ad_group_ids}
        if campaign_ids:
            request_body["campaignIdFilter"] = {"include": campaign_ids}
        if ad_product:
            request_body["adProductFilter"] = {"include": [ad_product]}
        if states:
            request_body["stateFilter"] = {"include": states}
        if name_filter:
            request_body["nameFilter"] = name_filter
        if next_token:
            request_body["nextToken"] = next_token
            
        result = await self.post(
            "/adsApi/v1/query/adGroups",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"adGroups": []}
    
    async def update(
        self,
        ad_groups: List[Dict[str, Any]],
    ) -> JSONData:
        """更新 Ad Group - POST /adsApi/v1/update/adGroups"""
        result = await self.post(
            "/adsApi/v1/update/adGroups",
            json_data={"adGroups": ad_groups}
        )
        return result if isinstance(result, dict) else {}
    
    async def delete(
        self,
        ad_group_ids: List[str],
    ) -> JSONData:
        """删除 Ad Group - POST /adsApi/v1/delete/adGroups"""
        result = await self.post(
            "/adsApi/v1/delete/adGroups",
            json_data={"adGroupIds": ad_group_ids}
        )
        return result if isinstance(result, dict) else {}


class AdsAPI(BaseAdsClient):
    """Ads API v1 (全异步)
    
    官方端点:
    - POST /adsApi/v1/create/ads
    - POST /adsApi/v1/query/ads
    - POST /adsApi/v1/update/ads
    - POST /adsApi/v1/delete/ads
    """
    
    async def create(
        self,
        ads: List[Dict[str, Any]],
    ) -> JSONData:
        """创建 Ad - POST /adsApi/v1/create/ads"""
        result = await self.post(
            "/adsApi/v1/create/ads",
            json_data={"ads": ads}
        )
        return result if isinstance(result, dict) else {}
    
    async def query(
        self,
        *,
        ad_ids: Optional[List[str]] = None,
        ad_group_ids: Optional[List[str]] = None,
        campaign_ids: Optional[List[str]] = None,
        ad_product: Optional[str] = None,
        states: Optional[List[str]] = None,
        name_filter: Optional[Dict[str, Any]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """查询 Ad - POST /adsApi/v1/query/ads"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if ad_ids:
            request_body["adIdFilter"] = {"include": ad_ids}
        if ad_group_ids:
            request_body["adGroupIdFilter"] = {"include": ad_group_ids}
        if campaign_ids:
            request_body["campaignIdFilter"] = {"include": campaign_ids}
        if ad_product:
            request_body["adProductFilter"] = {"include": [ad_product]}
        if states:
            request_body["stateFilter"] = {"include": states}
        if name_filter:
            request_body["nameFilter"] = name_filter
        if next_token:
            request_body["nextToken"] = next_token
            
        result = await self.post(
            "/adsApi/v1/query/ads",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"ads": []}
    
    async def update(
        self,
        ads: List[Dict[str, Any]],
    ) -> JSONData:
        """更新 Ad - POST /adsApi/v1/update/ads"""
        result = await self.post(
            "/adsApi/v1/update/ads",
            json_data={"ads": ads}
        )
        return result if isinstance(result, dict) else {}
    
    async def delete(
        self,
        ad_ids: List[str],
    ) -> JSONData:
        """删除 Ad - POST /adsApi/v1/delete/ads"""
        result = await self.post(
            "/adsApi/v1/delete/ads",
            json_data={"adIds": ad_ids}
        )
        return result if isinstance(result, dict) else {}


class CampaignsAPI(BaseAdsClient):
    """Campaigns API v1 (全异步)
    
    官方端点:
    - POST /adsApi/v1/create/campaigns
    - POST /adsApi/v1/query/campaigns
    - POST /adsApi/v1/update/campaigns
    - POST /adsApi/v1/delete/campaigns
    """
    
    async def create(
        self,
        campaigns: List[Dict[str, Any]],
    ) -> JSONData:
        """创建 Campaign - POST /adsApi/v1/create/campaigns"""
        result = await self.post(
            "/adsApi/v1/create/campaigns",
            json_data={"campaigns": campaigns}
        )
        return result if isinstance(result, dict) else {}
    
    async def query(
        self,
        *,
        campaign_ids: Optional[List[str]] = None,
        portfolio_ids: Optional[List[str]] = None,
        ad_product: Optional[str] = None,
        states: Optional[List[str]] = None,
        name_filter: Optional[Dict[str, Any]] = None,
        goal_filter: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """查询 Campaign - POST /adsApi/v1/query/campaigns"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if campaign_ids:
            request_body["campaignIdFilter"] = {"include": campaign_ids}
        if portfolio_ids:
            request_body["portfolioIdFilter"] = {"include": portfolio_ids}
        if ad_product:
            request_body["adProductFilter"] = {"include": [ad_product]}
        if states:
            request_body["stateFilter"] = {"include": states}
        if name_filter:
            request_body["nameFilter"] = name_filter
        if goal_filter:
            request_body["goalFilter"] = {"include": [goal_filter]}
        if next_token:
            request_body["nextToken"] = next_token
            
        result = await self.post(
            "/adsApi/v1/query/campaigns",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"campaigns": []}
    
    async def update(
        self,
        campaigns: List[Dict[str, Any]],
    ) -> JSONData:
        """更新 Campaign - POST /adsApi/v1/update/campaigns"""
        result = await self.post(
            "/adsApi/v1/update/campaigns",
            json_data={"campaigns": campaigns}
        )
        return result if isinstance(result, dict) else {}
    
    async def delete(
        self,
        campaign_ids: List[str],
    ) -> JSONData:
        """删除 Campaign - POST /adsApi/v1/delete/campaigns"""
        result = await self.post(
            "/adsApi/v1/delete/campaigns",
            json_data={"campaignIds": campaign_ids}
        )
        return result if isinstance(result, dict) else {}


class TargetsAPI(BaseAdsClient):
    """Targets API v1 (全异步)
    
    官方端点:
    - POST /adsApi/v1/create/targets
    - POST /adsApi/v1/query/targets
    - POST /adsApi/v1/update/targets
    - POST /adsApi/v1/delete/targets
    """
    
    async def create(
        self,
        targets: List[Dict[str, Any]],
    ) -> JSONData:
        """创建 Target - POST /adsApi/v1/create/targets"""
        result = await self.post(
            "/adsApi/v1/create/targets",
            json_data={"targets": targets}
        )
        return result if isinstance(result, dict) else {}
    
    async def query(
        self,
        *,
        target_ids: Optional[List[str]] = None,
        ad_group_ids: Optional[List[str]] = None,
        campaign_ids: Optional[List[str]] = None,
        ad_product: Optional[str] = None,
        states: Optional[List[str]] = None,
        target_type: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """查询 Target - POST /adsApi/v1/query/targets"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if target_ids:
            request_body["targetIdFilter"] = {"include": target_ids}
        if ad_group_ids:
            request_body["adGroupIdFilter"] = {"include": ad_group_ids}
        if campaign_ids:
            request_body["campaignIdFilter"] = {"include": campaign_ids}
        if ad_product:
            request_body["adProductFilter"] = {"include": [ad_product]}
        if states:
            request_body["stateFilter"] = {"include": states}
        if target_type:
            request_body["targetTypeFilter"] = {"include": [target_type]}
        if next_token:
            request_body["nextToken"] = next_token
            
        result = await self.post(
            "/adsApi/v1/query/targets",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"targets": []}
    
    async def update(
        self,
        targets: List[Dict[str, Any]],
    ) -> JSONData:
        """更新 Target - POST /adsApi/v1/update/targets"""
        result = await self.post(
            "/adsApi/v1/update/targets",
            json_data={"targets": targets}
        )
        return result if isinstance(result, dict) else {}
    
    async def delete(
        self,
        target_ids: List[str],
    ) -> JSONData:
        """删除 Target - POST /adsApi/v1/delete/targets"""
        result = await self.post(
            "/adsApi/v1/delete/targets",
            json_data={"targetIds": target_ids}
        )
        return result if isinstance(result, dict) else {}


class AdExtensionsAPI(BaseAdsClient):
    """Ad Extensions API v1 (全异步)
    
    官方端点:
    - POST /adsApi/v1/query/adExtensions
    - POST /adsApi/v1/update/adExtensions
    """
    
    async def query(
        self,
        *,
        ad_extension_ids: Optional[List[str]] = None,
        ad_ids: Optional[List[str]] = None,
        ad_group_ids: Optional[List[str]] = None,
        campaign_ids: Optional[List[str]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """查询 Ad Extension - POST /adsApi/v1/query/adExtensions"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if ad_extension_ids:
            request_body["adExtensionIdFilter"] = {"include": ad_extension_ids}
        if ad_ids:
            request_body["adIdFilter"] = {"include": ad_ids}
        if ad_group_ids:
            request_body["adGroupIdFilter"] = {"include": ad_group_ids}
        if campaign_ids:
            request_body["campaignIdFilter"] = {"include": campaign_ids}
        if next_token:
            request_body["nextToken"] = next_token
            
        result = await self.post(
            "/adsApi/v1/query/adExtensions",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"adExtensions": []}
    
    async def update(
        self,
        ad_extensions: List[Dict[str, Any]],
    ) -> JSONData:
        """更新 Ad Extension - POST /adsApi/v1/update/adExtensions"""
        result = await self.post(
            "/adsApi/v1/update/adExtensions",
            json_data={"adExtensions": ad_extensions}
        )
        return result if isinstance(result, dict) else {}


# ==================== SB 专属资源 ====================

class SBAdvertisingDealsAPI(BaseAdsClient):
    """SB Advertising Deals API v1 (全异步)
    
    官方端点:
    - POST /adsApi/v1/create/advertisingDeals/sb
    - POST /adsApi/v1/query/advertisingDeals/sb
    - POST /adsApi/v1/update/advertisingDeals/sb
    - POST /adsApi/v1/delete/advertisingDeals/sb
    """
    
    async def create(
        self,
        advertising_deals: List[Dict[str, Any]],
    ) -> JSONData:
        """创建广告交易 - POST /adsApi/v1/create/advertisingDeals/sb"""
        result = await self.post(
            "/adsApi/v1/create/advertisingDeals/sb",
            json_data={"advertisingDeals": advertising_deals}
        )
        return result if isinstance(result, dict) else {}
    
    async def query(
        self,
        *,
        deal_ids: Optional[List[str]] = None,
        states: Optional[List[str]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """查询广告交易 - POST /adsApi/v1/query/advertisingDeals/sb"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        if deal_ids:
            request_body["dealIdFilter"] = {"include": deal_ids}
        if states:
            request_body["stateFilter"] = {"include": states}
        if next_token:
            request_body["nextToken"] = next_token
        result = await self.post(
            "/adsApi/v1/query/advertisingDeals/sb",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"advertisingDeals": []}
    
    async def update(
        self,
        advertising_deals: List[Dict[str, Any]],
    ) -> JSONData:
        """更新广告交易 - POST /adsApi/v1/update/advertisingDeals/sb"""
        result = await self.post(
            "/adsApi/v1/update/advertisingDeals/sb",
            json_data={"advertisingDeals": advertising_deals}
        )
        return result if isinstance(result, dict) else {}
    
    async def delete(
        self,
        deal_ids: List[str],
    ) -> JSONData:
        """删除广告交易 - POST /adsApi/v1/delete/advertisingDeals/sb"""
        result = await self.post(
            "/adsApi/v1/delete/advertisingDeals/sb",
            json_data={"dealIds": deal_ids}
        )
        return result if isinstance(result, dict) else {}


class SBAdvertisingDealTargetsAPI(BaseAdsClient):
    """SB Advertising Deal Targets API v1 (全异步)
    
    官方端点:
    - POST /adsApi/v1/create/advertisingDealTargets/sb
    - POST /adsApi/v1/query/advertisingDealTargets/sb
    - POST /adsApi/v1/delete/advertisingDealTargets/sb
    """
    
    async def create(
        self,
        deal_targets: List[Dict[str, Any]],
    ) -> JSONData:
        """创建交易定向 - POST /adsApi/v1/create/advertisingDealTargets/sb"""
        result = await self.post(
            "/adsApi/v1/create/advertisingDealTargets/sb",
            json_data={"advertisingDealTargets": deal_targets}
        )
        return result if isinstance(result, dict) else {}
    
    async def query(
        self,
        *,
        deal_target_ids: Optional[List[str]] = None,
        deal_ids: Optional[List[str]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """查询交易定向 - POST /adsApi/v1/query/advertisingDealTargets/sb"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        if deal_target_ids:
            request_body["dealTargetIdFilter"] = {"include": deal_target_ids}
        if deal_ids:
            request_body["dealIdFilter"] = {"include": deal_ids}
        if next_token:
            request_body["nextToken"] = next_token
        result = await self.post(
            "/adsApi/v1/query/advertisingDealTargets/sb",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"advertisingDealTargets": []}
    
    async def delete(
        self,
        deal_target_ids: List[str],
    ) -> JSONData:
        """删除交易定向 - POST /adsApi/v1/delete/advertisingDealTargets/sb"""
        result = await self.post(
            "/adsApi/v1/delete/advertisingDealTargets/sb",
            json_data={"dealTargetIds": deal_target_ids}
        )
        return result if isinstance(result, dict) else {}


class SBBrandedKeywordsPricingsAPI(BaseAdsClient):
    """SB Branded Keywords Pricings API v1 (全异步)
    
    官方端点:
    - POST /adsApi/v1/create/brandedKeywordsPricings/sb
    """
    
    async def create(
        self,
        *,
        keywords: List[str],
        marketplace_id: str,
    ) -> JSONData:
        """查询品牌关键词定价 - POST /adsApi/v1/create/brandedKeywordsPricings/sb"""
        result = await self.post(
            "/adsApi/v1/create/brandedKeywordsPricings/sb",
            json_data={
                "keywords": keywords,
                "marketplaceId": marketplace_id,
            }
        )
        return result if isinstance(result, dict) else {"pricings": []}


class SBKeywordReservationValidationsAPI(BaseAdsClient):
    """SB Keyword Reservation Validations API v1 (全异步)
    
    官方端点:
    - POST /adsApi/v1/create/keywordReservationValidations/sb
    """
    
    async def validate(
        self,
        *,
        keywords: List[str],
        marketplace_id: str,
        ad_product: str = "SPONSORED_BRANDS",
    ) -> JSONData:
        """验证关键词预留 - POST /adsApi/v1/create/keywordReservationValidations/sb"""
        result = await self.post(
            "/adsApi/v1/create/keywordReservationValidations/sb",
            json_data={
                "keywords": keywords,
                "marketplaceId": marketplace_id,
                "adProduct": ad_product,
            }
        )
        return result if isinstance(result, dict) else {"validations": []}


class SBRecommendationsAPI(BaseAdsClient):
    """SB Recommendations API v1 (全异步)
    
    官方端点:
    - POST /adsApi/v1/create/recommendations/sb
    """
    
    async def create(
        self,
        *,
        recommendation_type: str,
        entity_type: Optional[str] = None,
        entity_ids: Optional[List[str]] = None,
        max_results: int = 100,
    ) -> JSONData:
        """获取推荐 - POST /adsApi/v1/create/recommendations/sb"""
        request_body: Dict[str, Any] = {
            "recommendationType": recommendation_type,
            "maxResults": max_results,
        }
        
        if entity_type:
            request_body["entityType"] = entity_type
        if entity_ids:
            request_body["entityIds"] = entity_ids
            
        result = await self.post(
            "/adsApi/v1/create/recommendations/sb",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"recommendations": []}


class SBRecommendationTypesAPI(BaseAdsClient):
    """SB Recommendation Types API v1 (全异步)
    
    官方端点:
    - POST /adsApi/v1/query/recommendationTypes/sb
    """
    
    async def query(
        self,
        *,
        ad_product: Optional[str] = None,
    ) -> JSONData:
        """获取推荐类型列表 - POST /adsApi/v1/query/recommendationTypes/sb"""
        request_body: Dict[str, Any] = {}
        if ad_product:
            request_body["adProduct"] = ad_product
        result = await self.post(
            "/adsApi/v1/query/recommendationTypes/sb",
            json_data=request_body if request_body else None
        )
        return result if isinstance(result, dict) else {"recommendationTypes": []}


# ==================== DSP 专属资源 ====================

class DSPCommitmentsAPI(BaseAdsClient):
    """DSP Commitments API v1 (全异步)
    
    官方端点:
    - GET /adsApi/v1/commitments/dsp
    - POST /adsApi/v1/create/commitments/dsp
    - POST /adsApi/v1/retrieve/commitments/dsp
    - POST /adsApi/v1/update/commitments/dsp
    """
    
    async def list(self) -> JSONData:
        """获取承诺列表 - GET /adsApi/v1/commitments/dsp"""
        result = await self.get("/adsApi/v1/commitments/dsp")
        return result if isinstance(result, dict) else {"commitments": []}
    
    async def create(
        self,
        commitments: List[Dict[str, Any]],
    ) -> JSONData:
        """创建承诺 - POST /adsApi/v1/create/commitments/dsp"""
        result = await self.post(
            "/adsApi/v1/create/commitments/dsp",
            json_data={"commitments": commitments}
        )
        return result if isinstance(result, dict) else {}
    
    async def retrieve(
        self,
        *,
        commitment_ids: Optional[List[str]] = None,
        states: Optional[List[str]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """检索承诺 - POST /adsApi/v1/retrieve/commitments/dsp"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        if commitment_ids:
            request_body["commitmentIdFilter"] = {"include": commitment_ids}
        if states:
            request_body["stateFilter"] = {"include": states}
        if next_token:
            request_body["nextToken"] = next_token
        result = await self.post(
            "/adsApi/v1/retrieve/commitments/dsp",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"commitments": []}
    
    async def update(
        self,
        commitments: List[Dict[str, Any]],
    ) -> JSONData:
        """更新承诺 - POST /adsApi/v1/update/commitments/dsp"""
        result = await self.post(
            "/adsApi/v1/update/commitments/dsp",
            json_data={"commitments": commitments}
        )
        return result if isinstance(result, dict) else {}


class DSPCommitmentSpendsAPI(BaseAdsClient):
    """DSP Commitment Spends API v1 (全异步)
    
    官方端点:
    - POST /adsApi/v1/retrieve/commitmentSpends/dsp
    """
    
    async def retrieve(
        self,
        *,
        commitment_ids: Optional[List[str]] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """检索承诺支出 - POST /adsApi/v1/retrieve/commitmentSpends/dsp"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        if commitment_ids:
            request_body["commitmentIdFilter"] = {"include": commitment_ids}
        if start_date:
            request_body["startDate"] = start_date
        if end_date:
            request_body["endDate"] = end_date
        if next_token:
            request_body["nextToken"] = next_token
        result = await self.post(
            "/adsApi/v1/retrieve/commitmentSpends/dsp",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"commitmentSpends": []}


class DSPCampaignForecastsAPI(BaseAdsClient):
    """DSP Campaign Forecasts API v1 (全异步)
    
    官方端点:
    - POST /adsApi/v1/retrieve/campaignForecasts/dsp
    """
    
    async def retrieve(
        self,
        *,
        forecast_ids: Optional[List[str]] = None,
        campaign_ids: Optional[List[str]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """检索广告活动预测 - POST /adsApi/v1/retrieve/campaignForecasts/dsp"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        if forecast_ids:
            request_body["forecastIdFilter"] = {"include": forecast_ids}
        if campaign_ids:
            request_body["campaignIdFilter"] = {"include": campaign_ids}
        if next_token:
            request_body["nextToken"] = next_token
        result = await self.post(
            "/adsApi/v1/retrieve/campaignForecasts/dsp",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"campaignForecasts": []}
