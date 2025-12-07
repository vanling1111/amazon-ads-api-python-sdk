"""
Amazon Ads API 统一客户端
组合所有模块，提供统一入口

设计原则：
- S: 每个模块职责单一
- O: 通过组合扩展新模块
- L: 模块可替换
- I: 按需使用模块接口
- D: 依赖抽象BaseAdsClient
"""

from typing import Self

from .base import BaseAdsClient, AdsRegion, ProfileID, AmazonAdsError

# SP模块
from .sp.campaigns import SPCampaignsAPI
from .sp.ad_groups import SPAdGroupsAPI
from .sp.keywords import SPKeywordsAPI
from .sp.targeting import SPTargetingAPI
from .sp.budget_rules import SPBudgetRulesAPI
from .sp.recommendations import SPRecommendationsAPI
from .sp.product_eligibility import SPProductEligibilityAPI
from .sp.theme_targeting import SPThemeTargetingAPI

# SB模块
from .sb.campaigns import SBCampaignsAPI
from .sb.ads import SBAdsAPI
from .sb.keywords import SBKeywordsAPI
from .sb.creatives import SBCreativesAPI
from .sb.brand_video import SBBrandVideoAPI
from .sb.moderation import SBModerationAPI

# SD模块
from .sd.campaigns import SDCampaignsAPI
from .sd.targeting import SDTargetingAPI
from .sd.creatives import SDCreativesAPI
from .sd.audiences import SDAudiencesAPI
from .sd.moderation import SDModerationAPI

# DSP模块
from .dsp.audiences import DSPAudiencesAPI
from .dsp.advertisers import DSPAdvertisersAPI
from .dsp.orders import DSPOrdersAPI
from .dsp.line_items import DSPLineItemsAPI
from .dsp.creatives import DSPCreativesAPI
from .dsp.inventory import DSPInventoryAPI
from .dsp.measurement import DSPMeasurementAPI
from .dsp.conversions import DSPConversionsAPI
from .dsp.target_kpi import DSPTargetKPIAPI

# Reporting模块
from .reporting.reports_v3 import ReportsV3API
from .reporting.brand_metrics import BrandMetricsAPI
from .reporting.stores_analytics import StoresAnalyticsAPI
from .reporting.mmm import MarketingMixModelingAPI

# Accounts模块
from .accounts.profiles import ProfilesAPI
from .accounts.portfolios import PortfoliosAPI
from .accounts.billing import BillingAPI
from .accounts.budgets import AccountBudgetsAPI
from .accounts.test_accounts import TestAccountsAPI

# Common模块
from .common.attribution import AttributionAPI
from .common.stores import StoresAPI
from .common.assets import AssetsAPI
from .common.history import HistoryAPI

# Eligibility模块
from .eligibility.eligibility import EligibilityAPI

# Insights模块
from .insights.category_insights import CategoryInsightsAPI
from .insights.keyword_insights import KeywordInsightsAPI
from .insights.audience_insights import AudienceInsightsAPI

# Recommendations模块
from .recommendations.partner_opportunities import PartnerOpportunitiesAPI
from .recommendations.tactical import TacticalRecommendationsAPI
from .recommendations.persona_builder import PersonaBuilderAPI

# Data Provider模块
from .data_provider.metadata import DataProviderMetadataAPI
from .data_provider.records import DataProviderRecordsAPI
from .data_provider.hashed_records import HashedRecordsAPI

# Products模块
from .products.product_selector import ProductSelectorAPI

# Moderation模块
from .moderation.pre_moderation import PreModerationAPI
from .moderation.unified_moderation import UnifiedModerationAPI

# Stream模块
from .stream.subscriptions import MarketingStreamAPI

# Locations模块
from .locations.locations import LocationsAPI

# Exports模块
from .exports.exports import ExportsAPI

# Media Planning模块
from .media_planning.reach_forecasting import ReachForecastingAPI

# AMC模块
from .amc.queries import AMCQueriesAPI
from .amc.audiences import AMCAudiencesAPI
from .amc.workflows import AMCWorkflowsAPI

# Sponsored TV模块
from .sponsored_tv.campaigns import SponsoredTVCampaignsAPI
from .sponsored_tv.ad_groups import SponsoredTVAdGroupsAPI
from .sponsored_tv.ads import SponsoredTVAdsAPI
from .sponsored_tv.creatives import SponsoredTVCreativesAPI
from .sponsored_tv.targeting import SponsoredTVTargetingAPI

# Retail Ad Service模块
from .retail_ad_service.campaigns import RASCampaignsAPI
from .retail_ad_service.ad_groups import RASAdGroupsAPI
from .retail_ad_service.product_ads import RASProductAdsAPI
from .retail_ad_service.targets import RASTargetsAPI

# Manager Accounts模块
from .manager_accounts.manager_accounts import ManagerAccountsAPI

# Posts模块
from .posts.posts import PostsAPI

# Product Metadata模块
from .product_metadata.product_metadata import ProductMetadataAPI

# Audiences Discovery模块
from .audiences_discovery.audiences_discovery import AudiencesDiscoveryAPI

# Amazon Ads V1模块
from .amazon_ads_v1.unified_api import AmazonAdsV1API

# Ad Library模块
from .ad_library.ad_library import AdLibraryAPI

# Brand Home模块
from .brand_home.brand_home import BrandHomeAPI

# Localization模块
from .localization.localization import LocalizationAPI

# Ads Data Manager模块
from .ads_data_manager.ads_data_manager import AdsDataManagerAPI

# Brand Associations模块
from .brand_associations.brand_associations import BrandAssociationsAPI


class AmazonAdsClient:
    """
    Amazon Ads API 统一客户端
    
    使用示例:
    ```python
    client = AmazonAdsClient(
        client_id="xxx",
        client_secret="xxx",
        refresh_token="xxx",
        region=AdsRegion.NA,
    )
    
    # 设置Profile
    client.with_profile("123456789")
    
    # 使用SP模块
    campaigns = client.sp.campaigns.list_campaigns()
    
    # 使用报告模块
    report = client.reporting.reports.get_campaign_performance_report(
        ad_product="SP",
        start_date="2024-01-01",
        end_date="2024-01-31",
    )
    
    # 使用DSP模块
    orders = client.dsp.orders.list_orders(advertiser_id="xxx")
    
    # 使用Insights模块
    keywords = client.insights.keywords.search_keywords("running shoes")
    
    # 使用Eligibility模块
    eligibility = client.eligibility.check_product_eligibility(["B00XXX"])
    ```
    """

    __slots__ = (
        "_client_id", "_client_secret", "_refresh_token",
        "_region", "_profile_id", "_max_retries", "_timeout",
        "_sp", "_sb", "_sd", "_dsp", "_reporting", "_accounts", 
        "_common", "_eligibility", "_insights", "_recommendations",
        "_data_provider", "_products", "_moderation", "_stream",
        "_locations", "_exports", "_media_planning", "_amc",
        # 新增模块
        "_st", "_ras", "_manager_accounts", "_posts", "_product_metadata",
        "_audiences_discovery", "_ads_v1", "_ad_library", "_brand_home",
        "_localization", "_ads_data_manager", "_brand_associations"
    )

    def __init__(
        self,
        client_id: str = "",
        client_secret: str = "",
        refresh_token: str = "",
        region: AdsRegion = AdsRegion.NA,
        profile_id: ProfileID | None = None,
        max_retries: int = 3,
        timeout: int = 30,
    ) -> None:
        self._client_id = client_id
        self._client_secret = client_secret
        self._refresh_token = refresh_token
        self._region = region
        self._profile_id = profile_id
        self._max_retries = max_retries
        self._timeout = timeout

        # 延迟初始化的模块容器
        self._sp: "_SPModule | None" = None
        self._sb: "_SBModule | None" = None
        self._sd: "_SDModule | None" = None
        self._dsp: "_DSPModule | None" = None
        self._reporting: "_ReportingModule | None" = None
        self._accounts: "_AccountsModule | None" = None
        self._common: "_CommonModule | None" = None
        self._eligibility: "EligibilityAPI | None" = None
        self._insights: "_InsightsModule | None" = None
        self._recommendations: "_RecommendationsModule | None" = None
        self._data_provider: "_DataProviderModule | None" = None
        self._products: "_ProductsModule | None" = None
        self._moderation: "_ModerationModule | None" = None
        self._stream: "_StreamModule | None" = None
        self._locations: "LocationsAPI | None" = None
        self._exports: "ExportsAPI | None" = None
        self._media_planning: "_MediaPlanningModule | None" = None
        self._amc: "_AMCModule | None" = None
        
        # 新增模块
        self._st: "_STModule | None" = None
        self._ras: "_RASModule | None" = None
        self._manager_accounts: "ManagerAccountsAPI | None" = None
        self._posts: "PostsAPI | None" = None
        self._product_metadata: "ProductMetadataAPI | None" = None
        self._audiences_discovery: "AudiencesDiscoveryAPI | None" = None
        self._ads_v1: "AmazonAdsV1API | None" = None
        self._ad_library: "AdLibraryAPI | None" = None
        self._brand_home: "BrandHomeAPI | None" = None
        self._ads_data_manager: "AdsDataManagerAPI | None" = None
        self._brand_associations: "BrandAssociationsAPI | None" = None
        self._localization: "LocalizationAPI | None" = None

    def _create_client(self, cls: type[BaseAdsClient]) -> BaseAdsClient:
        """创建子客户端实例"""
        return cls(
            client_id=self._client_id,
            client_secret=self._client_secret,
            refresh_token=self._refresh_token,
            region=self._region,
            profile_id=self._profile_id,
            max_retries=self._max_retries,
            timeout=self._timeout,
        )

    def with_profile(self, profile_id: ProfileID) -> Self:
        """设置Profile ID"""
        self._profile_id = profile_id
        # 重置所有模块以应用新Profile
        self._sp = None
        self._sb = None
        self._sd = None
        self._dsp = None
        self._reporting = None
        self._accounts = None
        self._common = None
        self._eligibility = None
        self._insights = None
        self._recommendations = None
        self._data_provider = None
        self._products = None
        self._moderation = None
        self._stream = None
        self._locations = None
        self._exports = None
        self._media_planning = None
        self._amc = None
        # 新增模块
        self._st = None
        self._ras = None
        self._manager_accounts = None
        self._posts = None
        self._product_metadata = None
        self._audiences_discovery = None
        self._ads_v1 = None
        self._ad_library = None
        self._brand_home = None
        self._localization = None
        return self

    # ============ 模块访问器（懒加载） ============

    @property
    def sp(self) -> "_SPModule":
        """Sponsored Products 模块"""
        if self._sp is None:
            self._sp = _SPModule(self)
        return self._sp

    @property
    def sb(self) -> "_SBModule":
        """Sponsored Brands 模块"""
        if self._sb is None:
            self._sb = _SBModule(self)
        return self._sb

    @property
    def sd(self) -> "_SDModule":
        """Sponsored Display 模块"""
        if self._sd is None:
            self._sd = _SDModule(self)
        return self._sd

    @property
    def dsp(self) -> "_DSPModule":
        """Amazon DSP 模块"""
        if self._dsp is None:
            self._dsp = _DSPModule(self)
        return self._dsp

    @property
    def reporting(self) -> "_ReportingModule":
        """Reporting 模块"""
        if self._reporting is None:
            self._reporting = _ReportingModule(self)
        return self._reporting

    @property
    def accounts(self) -> "_AccountsModule":
        """Accounts 模块"""
        if self._accounts is None:
            self._accounts = _AccountsModule(self)
        return self._accounts

    @property
    def common(self) -> "_CommonModule":
        """Common 模块"""
        if self._common is None:
            self._common = _CommonModule(self)
        return self._common

    @property
    def eligibility(self) -> "EligibilityAPI":
        """Eligibility 模块"""
        if self._eligibility is None:
            self._eligibility = self._create_client(EligibilityAPI)  # type: ignore
        return self._eligibility

    @property
    def insights(self) -> "_InsightsModule":
        """Insights 模块"""
        if self._insights is None:
            self._insights = _InsightsModule(self)
        return self._insights

    @property
    def recommendations(self) -> "_RecommendationsModule":
        """Recommendations 模块"""
        if self._recommendations is None:
            self._recommendations = _RecommendationsModule(self)
        return self._recommendations

    @property
    def data_provider(self) -> "_DataProviderModule":
        """Data Provider 模块"""
        if self._data_provider is None:
            self._data_provider = _DataProviderModule(self)
        return self._data_provider

    @property
    def products(self) -> "_ProductsModule":
        """Products 模块"""
        if self._products is None:
            self._products = _ProductsModule(self)
        return self._products

    @property
    def moderation(self) -> "_ModerationModule":
        """Moderation 模块"""
        if self._moderation is None:
            self._moderation = _ModerationModule(self)
        return self._moderation

    @property
    def stream(self) -> "_StreamModule":
        """Amazon Marketing Stream 模块"""
        if self._stream is None:
            self._stream = _StreamModule(self)
        return self._stream

    @property
    def locations(self) -> "LocationsAPI":
        """Locations 模块"""
        if self._locations is None:
            self._locations = self._create_client(LocationsAPI)  # type: ignore
        return self._locations

    @property
    def exports(self) -> "ExportsAPI":
        """Exports 模块"""
        if self._exports is None:
            self._exports = self._create_client(ExportsAPI)  # type: ignore
        return self._exports

    @property
    def media_planning(self) -> "_MediaPlanningModule":
        """Media Planning 模块"""
        if self._media_planning is None:
            self._media_planning = _MediaPlanningModule(self)
        return self._media_planning

    @property
    def amc(self) -> "_AMCModule":
        """Amazon Marketing Cloud 模块"""
        if self._amc is None:
            self._amc = _AMCModule(self)
        return self._amc

    # ============ 新增模块访问器 ============

    @property
    def st(self) -> "_STModule":
        """Sponsored TV 模块"""
        if self._st is None:
            self._st = _STModule(self)
        return self._st

    @property
    def ras(self) -> "_RASModule":
        """Retail Ad Service 模块"""
        if self._ras is None:
            self._ras = _RASModule(self)
        return self._ras

    @property
    def manager_accounts(self) -> "ManagerAccountsAPI":
        """Manager Accounts 模块"""
        if self._manager_accounts is None:
            self._manager_accounts = self._create_client(ManagerAccountsAPI)  # type: ignore
        return self._manager_accounts

    @property
    def posts(self) -> "PostsAPI":
        """Posts 模块"""
        if self._posts is None:
            self._posts = self._create_client(PostsAPI)  # type: ignore
        return self._posts

    @property
    def product_metadata(self) -> "ProductMetadataAPI":
        """Product Metadata 模块"""
        if self._product_metadata is None:
            self._product_metadata = self._create_client(ProductMetadataAPI)  # type: ignore
        return self._product_metadata

    @property
    def audiences_discovery(self) -> "AudiencesDiscoveryAPI":
        """Audiences Discovery 模块"""
        if self._audiences_discovery is None:
            self._audiences_discovery = self._create_client(AudiencesDiscoveryAPI)  # type: ignore
        return self._audiences_discovery

    @property
    def ads_v1(self) -> "AmazonAdsV1API":
        """Amazon Ads API v1 统一模块"""
        if self._ads_v1 is None:
            self._ads_v1 = self._create_client(AmazonAdsV1API)  # type: ignore
        return self._ads_v1

    @property
    def ad_library(self) -> "AdLibraryAPI":
        """Ad Library 模块"""
        if self._ad_library is None:
            self._ad_library = self._create_client(AdLibraryAPI)  # type: ignore
        return self._ad_library

    @property
    def brand_home(self) -> "BrandHomeAPI":
        """Brand Home 模块"""
        if self._brand_home is None:
            self._brand_home = self._create_client(BrandHomeAPI)  # type: ignore
        return self._brand_home

    @property
    def localization(self) -> "LocalizationAPI":
        """Localization 本地化模块"""
        if self._localization is None:
            self._localization = self._create_client(LocalizationAPI)  # type: ignore
        return self._localization

    @property
    def ads_data_manager(self) -> "AdsDataManagerAPI":
        """Ads Data Manager 广告数据管理模块"""
        if self._ads_data_manager is None:
            self._ads_data_manager = self._create_client(AdsDataManagerAPI)  # type: ignore
        return self._ads_data_manager

    @property
    def brand_associations(self) -> "BrandAssociationsAPI":
        """Brand Associations 品牌关联模块"""
        if self._brand_associations is None:
            self._brand_associations = self._create_client(BrandAssociationsAPI)  # type: ignore
        return self._brand_associations

    # ============ IAdsApiClient 接口实现（供依赖注入使用） ============
    # 这些方法代理到模块化API，保持接口抽象

    def list_campaigns(self, state_filter: str | None = None) -> list:
        """获取SP Campaign列表"""
        result = self.sp.campaigns.list_campaigns(state_filter=state_filter)
        return result.get("campaigns", [])

    def get_campaign(self, campaign_id: str) -> dict:
        """获取单个Campaign"""
        return self.sp.campaigns.get_campaign(campaign_id)

    def update_campaign(self, campaign_id: str, updates: dict) -> dict:
        """更新Campaign"""
        updates["campaignId"] = campaign_id
        result = self.sp.campaigns.update_campaigns([updates])
        campaigns = result.get("campaigns", {}).get("success", [])
        return campaigns[0] if campaigns else {}

    def list_keywords(self, campaign_id: str | None = None) -> list:
        """获取关键词列表"""
        result = self.sp.keywords.list_keywords(campaign_id=campaign_id)
        return result.get("keywords", [])

    def get_keyword(self, keyword_id: str) -> dict:
        """获取单个关键词"""
        return self.sp.keywords.get_keyword(keyword_id)

    def update_keyword_bid(self, keyword_id: str, new_bid: float) -> dict:
        """更新关键词竞价"""
        return self.sp.keywords.update_bid(keyword_id, new_bid)

    def create_keyword(self, keyword_data: dict) -> dict:
        """创建关键词"""
        result = self.sp.keywords.create_keywords([keyword_data])
        keywords = result.get("keywords", {}).get("success", [])
        return keywords[0] if keywords else {}

    def list_negative_keywords(
        self,
        campaign_id: str | None = None,
        ad_group_id: str | None = None,
    ) -> list:
        """获取否定关键词列表"""
        result = self.sp.keywords.list_negative_keywords(
            campaign_id=campaign_id,
            ad_group_id=ad_group_id,
        )
        return result.get("negativeKeywords", [])

    def create_negative_keyword(self, keyword_data: dict) -> dict:
        """创建否定关键词"""
        result = self.sp.keywords.create_negative_keywords([keyword_data])
        keywords = result.get("negativeKeywords", {}).get("success", [])
        return keywords[0] if keywords else {}

    def list_ad_groups(self, campaign_id: str | None = None) -> list:
        """获取广告组列表"""
        result = self.sp.ad_groups.list_ad_groups(campaign_id=campaign_id)
        return result.get("adGroups", [])

    def get_report(
        self,
        record_type: str,
        report_date: str,
        metrics: list[str],
    ) -> list:
        """获取报表"""
        return self.reporting.reports.create_and_wait_report(
            report_type=f"sp{record_type.capitalize()}",
            time_unit="DAILY",
            start_date=report_date,
            end_date=report_date,
            metrics=metrics,
        )

    def get_keyword_recommendations(
        self,
        asin: str | None = None,
        asins: list[str] | None = None,
        max_recommendations: int = 100,
    ) -> list:
        """获取关键词建议"""
        target_asins = asins or ([asin] if asin else [])
        result = self.sp.recommendations.get_keyword_recommendations(
            asins=target_asins,
            max_recommendations=max_recommendations,
        )
        return result.get("recommendations", [])

    def get_bid_recommendations(self, keyword_ids: list[str]) -> list:
        """获取竞价建议"""
        return self.sp.recommendations.get_keyword_bid_recommendations(keyword_ids)


# ============ 模块容器类 ============

class _SPModule:
    """SP模块容器"""

    __slots__ = (
        "_parent", "_campaigns", "_ad_groups", "_keywords",
        "_targeting", "_budget_rules", "_recommendations",
        "_product_eligibility", "_theme_targeting"
    )

    def __init__(self, parent: AmazonAdsClient) -> None:
        self._parent = parent
        self._campaigns: SPCampaignsAPI | None = None
        self._ad_groups: SPAdGroupsAPI | None = None
        self._keywords: SPKeywordsAPI | None = None
        self._targeting: SPTargetingAPI | None = None
        self._budget_rules: SPBudgetRulesAPI | None = None
        self._recommendations: SPRecommendationsAPI | None = None
        self._product_eligibility: SPProductEligibilityAPI | None = None
        self._theme_targeting: SPThemeTargetingAPI | None = None

    @property
    def campaigns(self) -> SPCampaignsAPI:
        if self._campaigns is None:
            self._campaigns = self._parent._create_client(SPCampaignsAPI)  # type: ignore
        return self._campaigns

    @property
    def ad_groups(self) -> SPAdGroupsAPI:
        if self._ad_groups is None:
            self._ad_groups = self._parent._create_client(SPAdGroupsAPI)  # type: ignore
        return self._ad_groups

    @property
    def keywords(self) -> SPKeywordsAPI:
        if self._keywords is None:
            self._keywords = self._parent._create_client(SPKeywordsAPI)  # type: ignore
        return self._keywords

    @property
    def targeting(self) -> SPTargetingAPI:
        if self._targeting is None:
            self._targeting = self._parent._create_client(SPTargetingAPI)  # type: ignore
        return self._targeting

    @property
    def budget_rules(self) -> SPBudgetRulesAPI:
        if self._budget_rules is None:
            self._budget_rules = self._parent._create_client(SPBudgetRulesAPI)  # type: ignore
        return self._budget_rules

    @property
    def recommendations(self) -> SPRecommendationsAPI:
        if self._recommendations is None:
            self._recommendations = self._parent._create_client(SPRecommendationsAPI)  # type: ignore
        return self._recommendations

    @property
    def product_eligibility(self) -> SPProductEligibilityAPI:
        """产品广告资格检查"""
        if self._product_eligibility is None:
            self._product_eligibility = self._parent._create_client(SPProductEligibilityAPI)  # type: ignore
        return self._product_eligibility

    @property
    def theme_targeting(self) -> SPThemeTargetingAPI:
        """主题/品类定向"""
        if self._theme_targeting is None:
            self._theme_targeting = self._parent._create_client(SPThemeTargetingAPI)  # type: ignore
        return self._theme_targeting


class _SBModule:
    """SB模块容器"""

    __slots__ = (
        "_parent", "_campaigns", "_ads", "_keywords", 
        "_creatives", "_brand_video", "_moderation"
    )

    def __init__(self, parent: AmazonAdsClient) -> None:
        self._parent = parent
        self._campaigns: SBCampaignsAPI | None = None
        self._ads: SBAdsAPI | None = None
        self._keywords: SBKeywordsAPI | None = None
        self._creatives: SBCreativesAPI | None = None
        self._brand_video: SBBrandVideoAPI | None = None
        self._moderation: SBModerationAPI | None = None

    @property
    def campaigns(self) -> SBCampaignsAPI:
        if self._campaigns is None:
            self._campaigns = self._parent._create_client(SBCampaignsAPI)  # type: ignore
        return self._campaigns

    @property
    def ads(self) -> SBAdsAPI:
        if self._ads is None:
            self._ads = self._parent._create_client(SBAdsAPI)  # type: ignore
        return self._ads

    @property
    def keywords(self) -> SBKeywordsAPI:
        if self._keywords is None:
            self._keywords = self._parent._create_client(SBKeywordsAPI)  # type: ignore
        return self._keywords

    @property
    def creatives(self) -> SBCreativesAPI:
        if self._creatives is None:
            self._creatives = self._parent._create_client(SBCreativesAPI)  # type: ignore
        return self._creatives

    @property
    def brand_video(self) -> SBBrandVideoAPI:
        """品牌视频广告"""
        if self._brand_video is None:
            self._brand_video = self._parent._create_client(SBBrandVideoAPI)  # type: ignore
        return self._brand_video

    @property
    def moderation(self) -> SBModerationAPI:
        """广告审核"""
        if self._moderation is None:
            self._moderation = self._parent._create_client(SBModerationAPI)  # type: ignore
        return self._moderation


class _SDModule:
    """SD模块容器"""

    __slots__ = (
        "_parent", "_campaigns", "_targeting", "_creatives",
        "_audiences", "_moderation"
    )

    def __init__(self, parent: AmazonAdsClient) -> None:
        self._parent = parent
        self._campaigns: SDCampaignsAPI | None = None
        self._targeting: SDTargetingAPI | None = None
        self._creatives: SDCreativesAPI | None = None
        self._audiences: SDAudiencesAPI | None = None
        self._moderation: SDModerationAPI | None = None

    @property
    def campaigns(self) -> SDCampaignsAPI:
        if self._campaigns is None:
            self._campaigns = self._parent._create_client(SDCampaignsAPI)  # type: ignore
        return self._campaigns

    @property
    def targeting(self) -> SDTargetingAPI:
        if self._targeting is None:
            self._targeting = self._parent._create_client(SDTargetingAPI)  # type: ignore
        return self._targeting

    @property
    def creatives(self) -> SDCreativesAPI:
        if self._creatives is None:
            self._creatives = self._parent._create_client(SDCreativesAPI)  # type: ignore
        return self._creatives

    @property
    def audiences(self) -> SDAudiencesAPI:
        """受众定向"""
        if self._audiences is None:
            self._audiences = self._parent._create_client(SDAudiencesAPI)  # type: ignore
        return self._audiences

    @property
    def moderation(self) -> SDModerationAPI:
        """创意审核"""
        if self._moderation is None:
            self._moderation = self._parent._create_client(SDModerationAPI)  # type: ignore
        return self._moderation


class _DSPModule:
    """DSP模块容器"""

    __slots__ = (
        "_parent", "_audiences", "_advertisers", "_orders",
        "_line_items", "_creatives", "_inventory", "_measurement",
        "_conversions", "_target_kpi"
    )

    def __init__(self, parent: AmazonAdsClient) -> None:
        self._parent = parent
        self._audiences: DSPAudiencesAPI | None = None
        self._advertisers: DSPAdvertisersAPI | None = None
        self._orders: DSPOrdersAPI | None = None
        self._line_items: DSPLineItemsAPI | None = None
        self._creatives: DSPCreativesAPI | None = None
        self._inventory: DSPInventoryAPI | None = None
        self._measurement: DSPMeasurementAPI | None = None
        self._conversions: DSPConversionsAPI | None = None
        self._target_kpi: DSPTargetKPIAPI | None = None

    @property
    def audiences(self) -> DSPAudiencesAPI:
        """受众管理"""
        if self._audiences is None:
            self._audiences = self._parent._create_client(DSPAudiencesAPI)  # type: ignore
        return self._audiences

    @property
    def advertisers(self) -> DSPAdvertisersAPI:
        """广告主管理"""
        if self._advertisers is None:
            self._advertisers = self._parent._create_client(DSPAdvertisersAPI)  # type: ignore
        return self._advertisers

    @property
    def orders(self) -> DSPOrdersAPI:
        """Order（Campaign）管理"""
        if self._orders is None:
            self._orders = self._parent._create_client(DSPOrdersAPI)  # type: ignore
        return self._orders

    @property
    def line_items(self) -> DSPLineItemsAPI:
        """Line Item管理"""
        if self._line_items is None:
            self._line_items = self._parent._create_client(DSPLineItemsAPI)  # type: ignore
        return self._line_items

    @property
    def creatives(self) -> DSPCreativesAPI:
        """创意管理"""
        if self._creatives is None:
            self._creatives = self._parent._create_client(DSPCreativesAPI)  # type: ignore
        return self._creatives

    @property
    def inventory(self) -> DSPInventoryAPI:
        """库存/Deal管理"""
        if self._inventory is None:
            self._inventory = self._parent._create_client(DSPInventoryAPI)  # type: ignore
        return self._inventory

    @property
    def measurement(self) -> DSPMeasurementAPI:
        """效果测量"""
        if self._measurement is None:
            self._measurement = self._parent._create_client(DSPMeasurementAPI)  # type: ignore
        return self._measurement

    @property
    def conversions(self) -> DSPConversionsAPI:
        """转化追踪"""
        if self._conversions is None:
            self._conversions = self._parent._create_client(DSPConversionsAPI)  # type: ignore
        return self._conversions

    @property
    def target_kpi(self) -> DSPTargetKPIAPI:
        """目标KPI建议"""
        if self._target_kpi is None:
            self._target_kpi = self._parent._create_client(DSPTargetKPIAPI)  # type: ignore
        return self._target_kpi


class _ReportingModule:
    """Reporting模块容器"""

    __slots__ = ("_parent", "_reports", "_brand_metrics", "_stores_analytics", "_mmm")

    def __init__(self, parent: AmazonAdsClient) -> None:
        self._parent = parent
        self._reports: ReportsV3API | None = None
        self._brand_metrics: BrandMetricsAPI | None = None
        self._stores_analytics: StoresAnalyticsAPI | None = None
        self._mmm: MarketingMixModelingAPI | None = None

    @property
    def reports(self) -> ReportsV3API:
        if self._reports is None:
            self._reports = self._parent._create_client(ReportsV3API)  # type: ignore
        return self._reports

    @property
    def brand_metrics(self) -> BrandMetricsAPI:
        if self._brand_metrics is None:
            self._brand_metrics = self._parent._create_client(BrandMetricsAPI)  # type: ignore
        return self._brand_metrics

    @property
    def stores_analytics(self) -> StoresAnalyticsAPI:
        """店铺分析"""
        if self._stores_analytics is None:
            self._stores_analytics = self._parent._create_client(StoresAnalyticsAPI)  # type: ignore
        return self._stores_analytics

    @property
    def mmm(self) -> MarketingMixModelingAPI:
        """营销组合建模"""
        if self._mmm is None:
            self._mmm = self._parent._create_client(MarketingMixModelingAPI)  # type: ignore
        return self._mmm


class _AccountsModule:
    """Accounts模块容器"""

    __slots__ = ("_parent", "_profiles", "_portfolios", "_billing", "_budgets", "_test_accounts")

    def __init__(self, parent: AmazonAdsClient) -> None:
        self._parent = parent
        self._profiles: ProfilesAPI | None = None
        self._portfolios: PortfoliosAPI | None = None
        self._billing: BillingAPI | None = None
        self._budgets: AccountBudgetsAPI | None = None
        self._test_accounts: TestAccountsAPI | None = None

    @property
    def profiles(self) -> ProfilesAPI:
        if self._profiles is None:
            self._profiles = self._parent._create_client(ProfilesAPI)  # type: ignore
        return self._profiles

    @property
    def portfolios(self) -> PortfoliosAPI:
        if self._portfolios is None:
            self._portfolios = self._parent._create_client(PortfoliosAPI)  # type: ignore
        return self._portfolios

    @property
    def billing(self) -> BillingAPI:
        if self._billing is None:
            self._billing = self._parent._create_client(BillingAPI)  # type: ignore
        return self._billing

    @property
    def budgets(self) -> AccountBudgetsAPI:
        """账户预算"""
        if self._budgets is None:
            self._budgets = self._parent._create_client(AccountBudgetsAPI)  # type: ignore
        return self._budgets

    @property
    def test_accounts(self) -> TestAccountsAPI:
        """测试账户"""
        if self._test_accounts is None:
            self._test_accounts = self._parent._create_client(TestAccountsAPI)  # type: ignore
        return self._test_accounts


class _CommonModule:
    """Common模块容器"""

    __slots__ = ("_parent", "_attribution", "_stores", "_assets", "_history")

    def __init__(self, parent: AmazonAdsClient) -> None:
        self._parent = parent
        self._attribution: AttributionAPI | None = None
        self._stores: StoresAPI | None = None
        self._assets: AssetsAPI | None = None
        self._history: HistoryAPI | None = None

    @property
    def attribution(self) -> AttributionAPI:
        if self._attribution is None:
            self._attribution = self._parent._create_client(AttributionAPI)  # type: ignore
        return self._attribution

    @property
    def stores(self) -> StoresAPI:
        if self._stores is None:
            self._stores = self._parent._create_client(StoresAPI)  # type: ignore
        return self._stores

    @property
    def assets(self) -> AssetsAPI:
        if self._assets is None:
            self._assets = self._parent._create_client(AssetsAPI)  # type: ignore
        return self._assets

    @property
    def history(self) -> HistoryAPI:
        if self._history is None:
            self._history = self._parent._create_client(HistoryAPI)  # type: ignore
        return self._history


class _InsightsModule:
    """Insights模块容器"""

    __slots__ = ("_parent", "_category", "_keywords", "_audience")

    def __init__(self, parent: AmazonAdsClient) -> None:
        self._parent = parent
        self._category: CategoryInsightsAPI | None = None
        self._keywords: KeywordInsightsAPI | None = None
        self._audience: AudienceInsightsAPI | None = None

    @property
    def category(self) -> CategoryInsightsAPI:
        """品类洞察"""
        if self._category is None:
            self._category = self._parent._create_client(CategoryInsightsAPI)  # type: ignore
        return self._category

    @property
    def keywords(self) -> KeywordInsightsAPI:
        """关键词洞察"""
        if self._keywords is None:
            self._keywords = self._parent._create_client(KeywordInsightsAPI)  # type: ignore
        return self._keywords

    @property
    def audience(self) -> AudienceInsightsAPI:
        """受众洞察"""
        if self._audience is None:
            self._audience = self._parent._create_client(AudienceInsightsAPI)  # type: ignore
        return self._audience


class _RecommendationsModule:
    """Recommendations模块容器"""

    __slots__ = ("_parent", "_partner", "_tactical", "_persona")

    def __init__(self, parent: AmazonAdsClient) -> None:
        self._parent = parent
        self._partner: PartnerOpportunitiesAPI | None = None
        self._tactical: TacticalRecommendationsAPI | None = None
        self._persona: PersonaBuilderAPI | None = None

    @property
    def partner(self) -> PartnerOpportunitiesAPI:
        """合作机会"""
        if self._partner is None:
            self._partner = self._parent._create_client(PartnerOpportunitiesAPI)  # type: ignore
        return self._partner

    @property
    def tactical(self) -> TacticalRecommendationsAPI:
        """战术建议"""
        if self._tactical is None:
            self._tactical = self._parent._create_client(TacticalRecommendationsAPI)  # type: ignore
        return self._tactical

    @property
    def persona(self) -> PersonaBuilderAPI:
        """人群画像"""
        if self._persona is None:
            self._persona = self._parent._create_client(PersonaBuilderAPI)  # type: ignore
        return self._persona


class _DataProviderModule:
    """Data Provider模块容器"""

    __slots__ = ("_parent", "_metadata", "_records", "_hashed")

    def __init__(self, parent: AmazonAdsClient) -> None:
        self._parent = parent
        self._metadata: DataProviderMetadataAPI | None = None
        self._records: DataProviderRecordsAPI | None = None
        self._hashed: HashedRecordsAPI | None = None

    @property
    def metadata(self) -> DataProviderMetadataAPI:
        """数据源元数据"""
        if self._metadata is None:
            self._metadata = self._parent._create_client(DataProviderMetadataAPI)  # type: ignore
        return self._metadata

    @property
    def records(self) -> DataProviderRecordsAPI:
        """数据记录"""
        if self._records is None:
            self._records = self._parent._create_client(DataProviderRecordsAPI)  # type: ignore
        return self._records

    @property
    def hashed(self) -> HashedRecordsAPI:
        """哈希记录"""
        if self._hashed is None:
            self._hashed = self._parent._create_client(HashedRecordsAPI)  # type: ignore
        return self._hashed


class _ProductsModule:
    """Products模块容器"""

    __slots__ = ("_parent", "_selector")

    def __init__(self, parent: AmazonAdsClient) -> None:
        self._parent = parent
        self._selector: ProductSelectorAPI | None = None

    @property
    def selector(self) -> ProductSelectorAPI:
        """产品选择器"""
        if self._selector is None:
            self._selector = self._parent._create_client(ProductSelectorAPI)  # type: ignore
        return self._selector


class _ModerationModule:
    """Moderation模块容器"""

    __slots__ = ("_parent", "_pre", "_unified")

    def __init__(self, parent: AmazonAdsClient) -> None:
        self._parent = parent
        self._pre: PreModerationAPI | None = None
        self._unified: UnifiedModerationAPI | None = None

    @property
    def pre(self) -> PreModerationAPI:
        """预审核"""
        if self._pre is None:
            self._pre = self._parent._create_client(PreModerationAPI)  # type: ignore
        return self._pre

    @property
    def unified(self) -> UnifiedModerationAPI:
        """统一审核"""
        if self._unified is None:
            self._unified = self._parent._create_client(UnifiedModerationAPI)  # type: ignore
        return self._unified


class _StreamModule:
    """Marketing Stream模块容器"""

    __slots__ = ("_parent", "_subscriptions")

    def __init__(self, parent: AmazonAdsClient) -> None:
        self._parent = parent
        self._subscriptions: MarketingStreamAPI | None = None

    @property
    def subscriptions(self) -> MarketingStreamAPI:
        """订阅管理"""
        if self._subscriptions is None:
            self._subscriptions = self._parent._create_client(MarketingStreamAPI)  # type: ignore
        return self._subscriptions


class _MediaPlanningModule:
    """Media Planning模块容器"""

    __slots__ = ("_parent", "_reach")

    def __init__(self, parent: AmazonAdsClient) -> None:
        self._parent = parent
        self._reach: ReachForecastingAPI | None = None

    @property
    def reach(self) -> ReachForecastingAPI:
        """触达预测"""
        if self._reach is None:
            self._reach = self._parent._create_client(ReachForecastingAPI)  # type: ignore
        return self._reach


class _AMCModule:
    """Amazon Marketing Cloud模块容器"""

    __slots__ = ("_parent", "_queries", "_audiences", "_workflows")

    def __init__(self, parent: AmazonAdsClient) -> None:
        self._parent = parent
        self._queries: AMCQueriesAPI | None = None
        self._audiences: AMCAudiencesAPI | None = None
        self._workflows: AMCWorkflowsAPI | None = None

    @property
    def queries(self) -> AMCQueriesAPI:
        """SQL查询"""
        if self._queries is None:
            self._queries = self._parent._create_client(AMCQueriesAPI)  # type: ignore
        return self._queries

    @property
    def audiences(self) -> AMCAudiencesAPI:
        """自定义受众"""
        if self._audiences is None:
            self._audiences = self._parent._create_client(AMCAudiencesAPI)  # type: ignore
        return self._audiences

    @property
    def workflows(self) -> AMCWorkflowsAPI:
        """自动化工作流"""
        if self._workflows is None:
            self._workflows = self._parent._create_client(AMCWorkflowsAPI)  # type: ignore
        return self._workflows


class _STModule:
    """Sponsored TV模块容器"""

    __slots__ = ("_parent", "_campaigns", "_ad_groups", "_ads", "_creatives", "_targeting")

    def __init__(self, parent: AmazonAdsClient) -> None:
        self._parent = parent
        self._campaigns: SponsoredTVCampaignsAPI | None = None
        self._ad_groups: SponsoredTVAdGroupsAPI | None = None
        self._ads: SponsoredTVAdsAPI | None = None
        self._creatives: SponsoredTVCreativesAPI | None = None
        self._targeting: SponsoredTVTargetingAPI | None = None

    @property
    def campaigns(self) -> SponsoredTVCampaignsAPI:
        """Campaign管理"""
        if self._campaigns is None:
            self._campaigns = self._parent._create_client(SponsoredTVCampaignsAPI)  # type: ignore
        return self._campaigns

    @property
    def ad_groups(self) -> SponsoredTVAdGroupsAPI:
        """广告组管理"""
        if self._ad_groups is None:
            self._ad_groups = self._parent._create_client(SponsoredTVAdGroupsAPI)  # type: ignore
        return self._ad_groups

    @property
    def ads(self) -> SponsoredTVAdsAPI:
        """广告管理"""
        if self._ads is None:
            self._ads = self._parent._create_client(SponsoredTVAdsAPI)  # type: ignore
        return self._ads

    @property
    def creatives(self) -> SponsoredTVCreativesAPI:
        """创意管理"""
        if self._creatives is None:
            self._creatives = self._parent._create_client(SponsoredTVCreativesAPI)  # type: ignore
        return self._creatives

    @property
    def targeting(self) -> SponsoredTVTargetingAPI:
        """定向管理"""
        if self._targeting is None:
            self._targeting = self._parent._create_client(SponsoredTVTargetingAPI)  # type: ignore
        return self._targeting


class _RASModule:
    """Retail Ad Service模块容器"""

    __slots__ = ("_parent", "_campaigns", "_ad_groups", "_product_ads", "_targets")

    def __init__(self, parent: AmazonAdsClient) -> None:
        self._parent = parent
        self._campaigns: RASCampaignsAPI | None = None
        self._ad_groups: RASAdGroupsAPI | None = None
        self._product_ads: RASProductAdsAPI | None = None
        self._targets: RASTargetsAPI | None = None

    @property
    def campaigns(self) -> RASCampaignsAPI:
        """Campaign管理"""
        if self._campaigns is None:
            self._campaigns = self._parent._create_client(RASCampaignsAPI)  # type: ignore
        return self._campaigns

    @property
    def ad_groups(self) -> RASAdGroupsAPI:
        """广告组管理"""
        if self._ad_groups is None:
            self._ad_groups = self._parent._create_client(RASAdGroupsAPI)  # type: ignore
        return self._ad_groups

    @property
    def product_ads(self) -> RASProductAdsAPI:
        """产品广告管理"""
        if self._product_ads is None:
            self._product_ads = self._parent._create_client(RASProductAdsAPI)  # type: ignore
        return self._product_ads

    @property
    def targets(self) -> RASTargetsAPI:
        """定向管理"""
        if self._targets is None:
            self._targets = self._parent._create_client(RASTargetsAPI)  # type: ignore
        return self._targets


# 兼容旧代码的别名
AdsAPIClient = AmazonAdsClient
