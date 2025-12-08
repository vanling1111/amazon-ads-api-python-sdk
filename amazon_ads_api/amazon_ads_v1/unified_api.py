"""
Amazon Ads API v1 - 统一API (异步版本)

这是Amazon 2024-2025年推出的全新统一API架构
端点前缀: /adsApi/v1/
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient, JSONData


class AmazonAdsV1API(BaseAdsClient):
    """
    Amazon Ads API v1 统一入口 (全异步)
    
    提供跨所有Amazon广告产品的统一模型
    覆盖所有官方资源
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 核心资源
        self.ad_associations = AdAssociationsAPI(*args, **kwargs)
        self.ad_groups = AdGroupsAPI(*args, **kwargs)
        self.ads = AdsAPI(*args, **kwargs)
        self.campaigns = CampaignsAPI(*args, **kwargs)
        self.targets = TargetsAPI(*args, **kwargs)
        self.recommendations = RecommendationsAPI(*args, **kwargs)
        # 扩展资源（根据官方 2025 API 规范）
        self.advertising_deals = AdvertisingDealsAPI(*args, **kwargs)
        self.advertising_deal_targets = AdvertisingDealTargetsAPI(*args, **kwargs)
        self.branded_keywords_pricings = BrandedKeywordsPricingsAPI(*args, **kwargs)
        self.campaign_forecasts = CampaignForecastsAPI(*args, **kwargs)
        self.commitments = CommitmentsAPI(*args, **kwargs)
        self.commitment_spends = CommitmentSpendsAPI(*args, **kwargs)
        self.keyword_reservation_validations = KeywordReservationValidationsAPI(*args, **kwargs)
        self.recommendation_types = RecommendationTypesAPI(*args, **kwargs)


class AdAssociationsAPI(BaseAdsClient):
    """Ad Associations API (全异步)"""
    
    async def create(
        self,
        ad_associations: List[Dict[str, Any]],
    ) -> JSONData:
        """创建Ad Association"""
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
        """查询Ad Association"""
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
        """更新Ad Association"""
        result = await self.post(
            "/adsApi/v1/update/adAssociations",
            json_data={"adAssociations": ad_associations}
        )
        return result if isinstance(result, dict) else {}
    
    async def delete(
        self,
        ad_association_ids: List[str],
    ) -> JSONData:
        """删除Ad Association"""
        result = await self.post(
            "/adsApi/v1/delete/adAssociations",
            json_data={"adAssociationIds": ad_association_ids}
        )
        return result if isinstance(result, dict) else {}


class AdGroupsAPI(BaseAdsClient):
    """Ad Groups API v1 (全异步)"""
    
    async def create(
        self,
        ad_groups: List[Dict[str, Any]],
    ) -> JSONData:
        """创建Ad Group"""
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
        """查询Ad Group"""
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
        """更新Ad Group"""
        result = await self.post(
            "/adsApi/v1/update/adGroups",
            json_data={"adGroups": ad_groups}
        )
        return result if isinstance(result, dict) else {}
    
    async def delete(
        self,
        ad_group_ids: List[str],
    ) -> JSONData:
        """删除Ad Group"""
        result = await self.post(
            "/adsApi/v1/delete/adGroups",
            json_data={"adGroupIds": ad_group_ids}
        )
        return result if isinstance(result, dict) else {}


class AdsAPI(BaseAdsClient):
    """Ads API v1 (全异步)"""
    
    async def create(
        self,
        ads: List[Dict[str, Any]],
    ) -> JSONData:
        """创建Ad"""
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
        """查询Ad"""
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
        """更新Ad"""
        result = await self.post(
            "/adsApi/v1/update/ads",
            json_data={"ads": ads}
        )
        return result if isinstance(result, dict) else {}
    
    async def delete(
        self,
        ad_ids: List[str],
    ) -> JSONData:
        """删除Ad"""
        result = await self.post(
            "/adsApi/v1/delete/ads",
            json_data={"adIds": ad_ids}
        )
        return result if isinstance(result, dict) else {}


class CampaignsAPI(BaseAdsClient):
    """Campaigns API v1 (全异步)"""
    
    async def create(
        self,
        campaigns: List[Dict[str, Any]],
    ) -> JSONData:
        """创建Campaign"""
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
        """查询Campaign"""
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
        """更新Campaign"""
        result = await self.post(
            "/adsApi/v1/update/campaigns",
            json_data={"campaigns": campaigns}
        )
        return result if isinstance(result, dict) else {}
    
    async def delete(
        self,
        campaign_ids: List[str],
    ) -> JSONData:
        """删除Campaign"""
        result = await self.post(
            "/adsApi/v1/delete/campaigns",
            json_data={"campaignIds": campaign_ids}
        )
        return result if isinstance(result, dict) else {}


class TargetsAPI(BaseAdsClient):
    """Targets API v1 (全异步)"""
    
    async def create(
        self,
        targets: List[Dict[str, Any]],
    ) -> JSONData:
        """创建Target"""
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
        """查询Target"""
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
        """更新Target"""
        result = await self.post(
            "/adsApi/v1/update/targets",
            json_data={"targets": targets}
        )
        return result if isinstance(result, dict) else {}
    
    async def delete(
        self,
        target_ids: List[str],
    ) -> JSONData:
        """删除Target"""
        result = await self.post(
            "/adsApi/v1/delete/targets",
            json_data={"targetIds": target_ids}
        )
        return result if isinstance(result, dict) else {}


class RecommendationsAPI(BaseAdsClient):
    """Recommendations API v1 (扩展) (全异步)"""
    
    async def get_recommendations(
        self,
        *,
        recommendation_type: Optional[str] = None,
        entity_type: Optional[str] = None,
        entity_ids: Optional[List[str]] = None,
        max_results: int = 100,
    ) -> JSONData:
        """获取推荐"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if recommendation_type:
            request_body["recommendationType"] = recommendation_type
        if entity_type:
            request_body["entityType"] = entity_type
        if entity_ids:
            request_body["entityIds"] = entity_ids
            
        result = await self.post(
            "/adsApi/v1/recommendations",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"recommendations": []}


class AdvertisingDealsAPI(BaseAdsClient):
    """Advertising Deals API v1 - 广告交易 (全异步)"""
    
    async def create(
        self,
        advertising_deals: List[Dict[str, Any]],
    ) -> JSONData:
        """创建广告交易"""
        result = await self.post(
            "/adsApi/v1/create/advertisingDeals",
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
        """查询广告交易"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        if deal_ids:
            request_body["dealIdFilter"] = {"include": deal_ids}
        if states:
            request_body["stateFilter"] = {"include": states}
        if next_token:
            request_body["nextToken"] = next_token
        result = await self.post(
            "/adsApi/v1/query/advertisingDeals",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"advertisingDeals": []}
    
    async def update(
        self,
        advertising_deals: List[Dict[str, Any]],
    ) -> JSONData:
        """更新广告交易"""
        result = await self.post(
            "/adsApi/v1/update/advertisingDeals",
            json_data={"advertisingDeals": advertising_deals}
        )
        return result if isinstance(result, dict) else {}
    
    async def delete(
        self,
        deal_ids: List[str],
    ) -> JSONData:
        """删除广告交易"""
        result = await self.post(
            "/adsApi/v1/delete/advertisingDeals",
            json_data={"dealIds": deal_ids}
        )
        return result if isinstance(result, dict) else {}


class AdvertisingDealTargetsAPI(BaseAdsClient):
    """Advertising Deal Targets API v1 - 广告交易定向 (全异步)"""
    
    async def create(
        self,
        deal_targets: List[Dict[str, Any]],
    ) -> JSONData:
        """创建交易定向"""
        result = await self.post(
            "/adsApi/v1/create/advertisingDealTargets",
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
        """查询交易定向"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        if deal_target_ids:
            request_body["dealTargetIdFilter"] = {"include": deal_target_ids}
        if deal_ids:
            request_body["dealIdFilter"] = {"include": deal_ids}
        if next_token:
            request_body["nextToken"] = next_token
        result = await self.post(
            "/adsApi/v1/query/advertisingDealTargets",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"advertisingDealTargets": []}
    
    async def update(
        self,
        deal_targets: List[Dict[str, Any]],
    ) -> JSONData:
        """更新交易定向"""
        result = await self.post(
            "/adsApi/v1/update/advertisingDealTargets",
            json_data={"advertisingDealTargets": deal_targets}
        )
        return result if isinstance(result, dict) else {}
    
    async def delete(
        self,
        deal_target_ids: List[str],
    ) -> JSONData:
        """删除交易定向"""
        result = await self.post(
            "/adsApi/v1/delete/advertisingDealTargets",
            json_data={"dealTargetIds": deal_target_ids}
        )
        return result if isinstance(result, dict) else {}


class BrandedKeywordsPricingsAPI(BaseAdsClient):
    """Branded Keywords Pricings API v1 - 品牌关键词定价 (全异步)"""
    
    async def query(
        self,
        *,
        keywords: List[str],
        marketplace_id: str,
    ) -> JSONData:
        """查询品牌关键词定价"""
        result = await self.post(
            "/adsApi/v1/query/brandedKeywordsPricings",
            json_data={
                "keywords": keywords,
                "marketplaceId": marketplace_id,
            }
        )
        return result if isinstance(result, dict) else {"pricings": []}


class CampaignForecastsAPI(BaseAdsClient):
    """Campaign Forecasts API v1 - 广告活动预测 (全异步)"""
    
    async def create(
        self,
        forecasts: List[Dict[str, Any]],
    ) -> JSONData:
        """创建广告活动预测"""
        result = await self.post(
            "/adsApi/v1/create/campaignForecasts",
            json_data={"campaignForecasts": forecasts}
        )
        return result if isinstance(result, dict) else {}
    
    async def query(
        self,
        *,
        forecast_ids: Optional[List[str]] = None,
        campaign_ids: Optional[List[str]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """查询广告活动预测"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        if forecast_ids:
            request_body["forecastIdFilter"] = {"include": forecast_ids}
        if campaign_ids:
            request_body["campaignIdFilter"] = {"include": campaign_ids}
        if next_token:
            request_body["nextToken"] = next_token
        result = await self.post(
            "/adsApi/v1/query/campaignForecasts",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"campaignForecasts": []}


class CommitmentsAPI(BaseAdsClient):
    """Commitments API v1 - 承诺 (全异步)"""
    
    async def create(
        self,
        commitments: List[Dict[str, Any]],
    ) -> JSONData:
        """创建承诺"""
        result = await self.post(
            "/adsApi/v1/create/commitments",
            json_data={"commitments": commitments}
        )
        return result if isinstance(result, dict) else {}
    
    async def query(
        self,
        *,
        commitment_ids: Optional[List[str]] = None,
        states: Optional[List[str]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """查询承诺"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        if commitment_ids:
            request_body["commitmentIdFilter"] = {"include": commitment_ids}
        if states:
            request_body["stateFilter"] = {"include": states}
        if next_token:
            request_body["nextToken"] = next_token
        result = await self.post(
            "/adsApi/v1/query/commitments",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"commitments": []}
    
    async def update(
        self,
        commitments: List[Dict[str, Any]],
    ) -> JSONData:
        """更新承诺"""
        result = await self.post(
            "/adsApi/v1/update/commitments",
            json_data={"commitments": commitments}
        )
        return result if isinstance(result, dict) else {}


class CommitmentSpendsAPI(BaseAdsClient):
    """Commitment Spends API v1 - 承诺支出 (全异步)"""
    
    async def query(
        self,
        *,
        commitment_ids: Optional[List[str]] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
        """查询承诺支出"""
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
            "/adsApi/v1/query/commitmentSpends",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {"commitmentSpends": []}


class KeywordReservationValidationsAPI(BaseAdsClient):
    """Keyword Reservation Validations API v1 - 关键词预留验证 (全异步)"""
    
    async def validate(
        self,
        *,
        keywords: List[str],
        marketplace_id: str,
        ad_product: str,
    ) -> JSONData:
        """验证关键词预留"""
        result = await self.post(
            "/adsApi/v1/keywordReservationValidations",
            json_data={
                "keywords": keywords,
                "marketplaceId": marketplace_id,
                "adProduct": ad_product,
            }
        )
        return result if isinstance(result, dict) else {"validations": []}


class RecommendationTypesAPI(BaseAdsClient):
    """Recommendation Types API v1 - 推荐类型 (全异步)"""
    
    async def list(
        self,
        *,
        ad_product: Optional[str] = None,
    ) -> JSONData:
        """获取推荐类型列表"""
        params: Dict[str, Any] = {}
        if ad_product:
            params["adProduct"] = ad_product
        result = await self.get(
            "/adsApi/v1/recommendationTypes",
            params=params if params else None
        )
        return result if isinstance(result, dict) else {"recommendationTypes": []}
