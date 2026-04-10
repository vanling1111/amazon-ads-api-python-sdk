"""
Amazon Ads API 统一客户端 - v2.2 完整分级架构

API 分级:
- L1 (Core): sp, sb, sd, dsp, accounts - OpenAPI 验证，生产可用
- L2 (Reference): reference.* - 官方文档确认，非 OpenAPI
- L3 (Services): services.* - 产品级聚合
- L4 (Experimental): experimental.* - Beta/实验性

使用示例:
    client = AmazonAdsClient(
        client_id="xxx",
        client_secret="xxx",
        refresh_token="xxx",
        profile_id="123456789",
        region="NA"
    )

    # L1 Core
    campaigns = await client.sp.campaigns.list_campaigns()
    profiles = await client.accounts.profiles.list_profiles()

    # L1 Cross-cutting
    await client.eligibility.check_product_eligibility(...)
    await client.locations.list_locations(...)
    await client.exports.export_campaigns(...)
    await client.product_selector.get_product_metadata(...)
    await client.audiences_discovery.list_audiences(...)

    # L2 Reference
    await client.reference.amc.administration.get_accounts()
    await client.reference.amc.queries.run_query(...)
    await client.reference.unified.campaigns.create(...)
    await client.reference.stream.list_subscriptions(...)
    await client.reference.posts.create_post(...)

    # L3 Services
    await client.services.reporting.reports_v3.create_report(...)
    await client.services.common.stores.get_asin_metrics(...)
    await client.services.insights.keyword_insights.get_sp_keyword_recommendations(...)

    # L4 Experimental
    await client.experimental.ad_library.list_ads(...)
    await client.experimental.sponsored_tv.campaigns.create_campaigns(...)
"""

from __future__ import annotations

import warnings
from typing import TYPE_CHECKING, Self, Optional

from .base import BaseAdsClient, AdsRegion, ProfileID, AmazonAdsError


# ============================================================
# L1 Core Modules
# ============================================================

class _SPModule:
    """Sponsored Products 模块 (L1 - OpenAPI 验证)"""

    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._campaigns = None
        self._ad_groups = None
        self._keywords = None
        self._product_ads = None
        self._targeting = None
        self._budget_rules = None
        self._optimization = None
        self._recommendations = None
        self._theme = None
        self._promotion_groups = None
        self._global_recs = None

    @property
    def campaigns(self):
        if self._campaigns is None:
            from .core.sp.campaigns import SPCampaignsAPI
            self._campaigns = self._client._create_client(SPCampaignsAPI)
        return self._campaigns

    @property
    def ad_groups(self):
        if self._ad_groups is None:
            from .core.sp.ad_groups import SPAdGroupsAPI
            self._ad_groups = self._client._create_client(SPAdGroupsAPI)
        return self._ad_groups

    @property
    def keywords(self):
        if self._keywords is None:
            from .core.sp.keywords import SPKeywordsAPI
            self._keywords = self._client._create_client(SPKeywordsAPI)
        return self._keywords

    @property
    def product_ads(self):
        if self._product_ads is None:
            from .core.sp.product_ads import SPProductAdsAPI
            self._product_ads = self._client._create_client(SPProductAdsAPI)
        return self._product_ads

    @property
    def targeting(self):
        if self._targeting is None:
            from .core.sp.targeting import SPTargetingAPI
            self._targeting = self._client._create_client(SPTargetingAPI)
        return self._targeting

    @property
    def budget_rules(self):
        if self._budget_rules is None:
            from .core.sp.budget_rules import SPBudgetRulesAPI
            self._budget_rules = self._client._create_client(SPBudgetRulesAPI)
        return self._budget_rules

    @property
    def optimization(self):
        if self._optimization is None:
            from .core.sp.campaign_optimization import SPCampaignOptimizationAPI
            self._optimization = self._client._create_client(SPCampaignOptimizationAPI)
        return self._optimization

    @property
    def recommendations(self):
        if self._recommendations is None:
            from .core.sp.recommendations import SPRecommendationsAPI
            self._recommendations = self._client._create_client(SPRecommendationsAPI)
        return self._recommendations

    @property
    def theme(self):
        if self._theme is None:
            from .core.sp.theme_targeting import SPThemeTargetingAPI
            self._theme = self._client._create_client(SPThemeTargetingAPI)
        return self._theme

    @property
    def promotion_groups(self):
        if self._promotion_groups is None:
            from .core.sp.target_promotion_groups import SPTargetPromotionGroupsAPI
            self._promotion_groups = self._client._create_client(SPTargetPromotionGroupsAPI)
        return self._promotion_groups

    @property
    def global_recs(self):
        if self._global_recs is None:
            from .core.sp.global_recommendations import SPGlobalRecommendationsAPI
            self._global_recs = self._client._create_client(SPGlobalRecommendationsAPI)
        return self._global_recs


class _SBModule:
    """Sponsored Brands 模块 (L1 - OpenAPI 验证)"""

    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._campaigns = None
        self._keywords = None
        self._ads = None
        self._creatives = None
        self._brand_video = None
        self._moderation = None
        self._optimization = None
        self._forecasts = None
        self._targeting = None
        self._themes = None
        self._media = None
        self._reports_v2 = None
        self._legacy_migration = None
        self._stores = None

    @property
    def campaigns(self):
        if self._campaigns is None:
            from .core.sb.campaigns import SBCampaignsAPI
            self._campaigns = self._client._create_client(SBCampaignsAPI)
        return self._campaigns

    @property
    def keywords(self):
        if self._keywords is None:
            from .core.sb.keywords import SBKeywordsAPI
            self._keywords = self._client._create_client(SBKeywordsAPI)
        return self._keywords

    @property
    def ads(self):
        if self._ads is None:
            from .core.sb.ads import SBAdsAPI
            self._ads = self._client._create_client(SBAdsAPI)
        return self._ads

    @property
    def creatives(self):
        if self._creatives is None:
            from .core.sb.creatives import SBCreativesAPI
            self._creatives = self._client._create_client(SBCreativesAPI)
        return self._creatives

    @property
    def brand_video(self):
        if self._brand_video is None:
            from .core.sb.brand_video import SBBrandVideoAPI
            self._brand_video = self._client._create_client(SBBrandVideoAPI)
        return self._brand_video

    @property
    def moderation(self):
        if self._moderation is None:
            from .core.sb.moderation import SBModerationAPI
            self._moderation = self._client._create_client(SBModerationAPI)
        return self._moderation

    @property
    def optimization(self):
        if self._optimization is None:
            from .core.sb.optimization import SBOptimizationAPI
            self._optimization = self._client._create_client(SBOptimizationAPI)
        return self._optimization

    @property
    def forecasts(self):
        if self._forecasts is None:
            from .core.sb.forecasts import SBForecastsAPI
            self._forecasts = self._client._create_client(SBForecastsAPI)
        return self._forecasts

    @property
    def targeting(self):
        if self._targeting is None:
            from .core.sb.targeting import SBTargetingAPI
            self._targeting = self._client._create_client(SBTargetingAPI)
        return self._targeting

    @property
    def themes(self):
        if self._themes is None:
            from .core.sb.themes import SBThemesAPI
            self._themes = self._client._create_client(SBThemesAPI)
        return self._themes

    @property
    def media(self):
        if self._media is None:
            from .core.sb.media import SBMediaAPI
            self._media = self._client._create_client(SBMediaAPI)
        return self._media

    @property
    def reports_v2(self):
        if self._reports_v2 is None:
            from .core.sb.reports_v2 import SBReportsV2API
            self._reports_v2 = self._client._create_client(SBReportsV2API)
        return self._reports_v2

    @property
    def legacy_migration(self):
        if self._legacy_migration is None:
            from .core.sb.legacy_migration import SBLegacyMigrationAPI
            self._legacy_migration = self._client._create_client(SBLegacyMigrationAPI)
        return self._legacy_migration

    @property
    def stores(self):
        if self._stores is None:
            from .core.sb.stores import SBStoresAPI
            self._stores = self._client._create_client(SBStoresAPI)
        return self._stores


class _SDModule:
    """Sponsored Display 模块 (L1 - OpenAPI 验证)"""

    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._campaigns = None
        self._targeting = None
        self._audiences = None
        self._creatives = None
        self._moderation = None
        self._reports = None
        self._optimization = None
        self._locations = None
        self._brand_safety = None

    @property
    def campaigns(self):
        if self._campaigns is None:
            from .core.sd.campaigns import SDCampaignsAPI
            self._campaigns = self._client._create_client(SDCampaignsAPI)
        return self._campaigns

    @property
    def targeting(self):
        if self._targeting is None:
            from .core.sd.targeting import SDTargetingAPI
            self._targeting = self._client._create_client(SDTargetingAPI)
        return self._targeting

    @property
    def audiences(self):
        if self._audiences is None:
            from .core.sd.audiences import SDAudienceTargetingAPI
            self._audiences = self._client._create_client(SDAudienceTargetingAPI)
        return self._audiences

    @property
    def creatives(self):
        if self._creatives is None:
            from .core.sd.creatives import SDCreativesAPI
            self._creatives = self._client._create_client(SDCreativesAPI)
        return self._creatives

    @property
    def moderation(self):
        if self._moderation is None:
            from .core.sd.moderation import SDModerationAPI
            self._moderation = self._client._create_client(SDModerationAPI)
        return self._moderation

    @property
    def reports(self):
        if self._reports is None:
            from .core.sd.reports import SDReportsAPI
            self._reports = self._client._create_client(SDReportsAPI)
        return self._reports

    @property
    def optimization(self):
        if self._optimization is None:
            from .core.sd.optimization import SDOptimizationAPI
            self._optimization = self._client._create_client(SDOptimizationAPI)
        return self._optimization

    @property
    def locations(self):
        if self._locations is None:
            from .core.sd.locations import SDLocationsAPI
            self._locations = self._client._create_client(SDLocationsAPI)
        return self._locations

    @property
    def brand_safety(self):
        if self._brand_safety is None:
            from .core.sd.brand_safety import SDBrandSafetyAPI
            self._brand_safety = self._client._create_client(SDBrandSafetyAPI)
        return self._brand_safety


class _DSPModule:
    """Amazon DSP 模块 (L1 - OpenAPI 验证)"""

    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._campaigns = None
        self._advertisers = None
        self._audiences = None
        self._conversions = None
        self._measurement = None
        self._target_kpi = None

    @property
    def campaigns(self):
        if self._campaigns is None:
            from .core.dsp.campaigns import DSPCampaignsAPI
            self._campaigns = self._client._create_client(DSPCampaignsAPI)
        return self._campaigns

    @property
    def advertisers(self):
        if self._advertisers is None:
            from .core.dsp.advertisers import DSPAdvertisersAPI
            self._advertisers = self._client._create_client(DSPAdvertisersAPI)
        return self._advertisers

    @property
    def audiences(self):
        if self._audiences is None:
            from .core.dsp.audiences import DSPAudiencesAPI
            self._audiences = self._client._create_client(DSPAudiencesAPI)
        return self._audiences

    @property
    def conversions(self):
        if self._conversions is None:
            from .core.dsp.conversions import DSPConversionsAPI
            self._conversions = self._client._create_client(DSPConversionsAPI)
        return self._conversions

    @property
    def measurement(self):
        if self._measurement is None:
            from .core.dsp.measurement import DSPMeasurementAPI
            self._measurement = self._client._create_client(DSPMeasurementAPI)
        return self._measurement

    @property
    def target_kpi(self):
        if self._target_kpi is None:
            from .core.dsp.target_kpi import DSPTargetKPIAPI
            self._target_kpi = self._client._create_client(DSPTargetKPIAPI)
        return self._target_kpi


class _AccountsModule:
    """账户管理模块 (L1 - OpenAPI 验证)"""

    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._profiles = None
        self._portfolios = None
        self._billing = None
        self._budgets = None
        self._advertising = None
        self._test = None

    @property
    def profiles(self):
        if self._profiles is None:
            from .core.accounts.profiles import ProfilesAPI
            self._profiles = self._client._create_client(ProfilesAPI)
        return self._profiles

    @property
    def portfolios(self):
        if self._portfolios is None:
            from .core.accounts.portfolios import PortfoliosAPI
            self._portfolios = self._client._create_client(PortfoliosAPI)
        return self._portfolios

    @property
    def billing(self):
        if self._billing is None:
            from .core.accounts.billing import BillingAPI
            self._billing = self._client._create_client(BillingAPI)
        return self._billing

    @property
    def budgets(self):
        if self._budgets is None:
            from .core.accounts.budgets import AccountBudgetsAPI
            self._budgets = self._client._create_client(AccountBudgetsAPI)
        return self._budgets

    @property
    def advertising(self):
        if self._advertising is None:
            from .core.accounts.advertising_accounts import AdvertisingAccountsAPI
            self._advertising = self._client._create_client(AdvertisingAccountsAPI)
        return self._advertising

    @property
    def test(self):
        if self._test is None:
            from .core.accounts.test_accounts import TestAccountsAPI
            self._test = self._client._create_client(TestAccountsAPI)
        return self._test


# ============================================================
# L2 Reference Sub-Modules
# ============================================================

class _AMCModule:
    """AMC 子模块 — administration, audiences, reporting"""

    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._administration = None
        self._audiences = None
        self._reporting = None

    @property
    def administration(self):
        if self._administration is None:
            from .reference.amc.administration import AMCAdministrationAPI
            self._administration = self._client._create_client(AMCAdministrationAPI)
        return self._administration

    @property
    def audiences(self):
        if self._audiences is None:
            from .reference.amc.audiences import AMCAudiencesAPI
            self._audiences = self._client._create_client(AMCAudiencesAPI)
        return self._audiences

    @property
    def reporting(self):
        if self._reporting is None:
            from .reference.amc.reporting import AMCReportingAPI
            self._reporting = self._client._create_client(AMCReportingAPI)
        return self._reporting


class _RetailAdServiceModule:
    """Retail Ad Service 子模块"""

    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._campaigns = None
        self._ad_groups = None
        self._product_ads = None
        self._targets = None

    @property
    def campaigns(self):
        if self._campaigns is None:
            from .reference.retail_ad_service.campaigns import RASCampaignsAPI
            self._campaigns = self._client._create_client(RASCampaignsAPI)
        return self._campaigns

    @property
    def ad_groups(self):
        if self._ad_groups is None:
            from .reference.retail_ad_service.ad_groups import RASAdGroupsAPI
            self._ad_groups = self._client._create_client(RASAdGroupsAPI)
        return self._ad_groups

    @property
    def product_ads(self):
        if self._product_ads is None:
            from .reference.retail_ad_service.product_ads import RASProductAdsAPI
            self._product_ads = self._client._create_client(RASProductAdsAPI)
        return self._product_ads

    @property
    def targets(self):
        if self._targets is None:
            from .reference.retail_ad_service.targets import RASTargetsAPI
            self._targets = self._client._create_client(RASTargetsAPI)
        return self._targets


class _DataProviderModule:
    """Data Provider 子模块"""

    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._audience_metadata = None
        self._hashed_records = None

    @property
    def audience_metadata(self):
        if self._audience_metadata is None:
            from .reference.data_provider.audience_metadata import AudienceMetadataAPI
            self._audience_metadata = self._client._create_client(AudienceMetadataAPI)
        return self._audience_metadata

    @property
    def hashed_records(self):
        if self._hashed_records is None:
            from .reference.data_provider.hashed_records import HashedRecordsAPI
            self._hashed_records = self._client._create_client(HashedRecordsAPI)
        return self._hashed_records


class _ReferenceAPIs:
    """L2: Reference APIs (非 OpenAPI 但官方文档确认)"""

    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._amc = None
        self._stream = None
        self._attribution = None
        self._retail_ad_service = None
        self._posts = None
        self._data_provider = None
        self._unified = None

    @property
    def amc(self) -> _AMCModule:
        if self._amc is None:
            self._amc = _AMCModule(self._client)
        return self._amc

    @property
    def stream(self):
        if self._stream is None:
            from .reference.stream.subscriptions import MarketingStreamAPI
            self._stream = self._client._create_client(MarketingStreamAPI)
        return self._stream

    @property
    def attribution(self):
        if self._attribution is None:
            from .services.common.attribution import AttributionAPI
            self._attribution = self._client._create_client(AttributionAPI)
        return self._attribution

    @property
    def retail_ad_service(self) -> _RetailAdServiceModule:
        if self._retail_ad_service is None:
            self._retail_ad_service = _RetailAdServiceModule(self._client)
        return self._retail_ad_service

    @property
    def posts(self):
        if self._posts is None:
            from .reference.posts.posts import PostsAPI
            self._posts = self._client._create_client(PostsAPI)
        return self._posts

    @property
    def data_provider(self) -> _DataProviderModule:
        if self._data_provider is None:
            self._data_provider = _DataProviderModule(self._client)
        return self._data_provider

    @property
    def unified(self):
        """Amazon Ads v1 Unified API"""
        if self._unified is None:
            from .reference.unified_api.unified_api import AmazonAdsV1API
            self._unified = self._client._create_client(AmazonAdsV1API)
        return self._unified


# ============================================================
# L3 Services Sub-Modules
# ============================================================

class _ReportingModule:
    """Reporting 子模块 — reports_v3, stores_analytics, brand_metrics, mmm"""

    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._reports_v3 = None
        self._stores_analytics = None
        self._brand_metrics = None
        self._mmm = None

    @property
    def reports_v3(self):
        if self._reports_v3 is None:
            from .services.reporting.reports_v3 import ReportsV3API
            self._reports_v3 = self._client._create_client(ReportsV3API)
        return self._reports_v3

    @property
    def stores_analytics(self):
        if self._stores_analytics is None:
            from .services.reporting.stores_analytics import StoresAnalyticsAPI
            self._stores_analytics = self._client._create_client(StoresAnalyticsAPI)
        return self._stores_analytics

    @property
    def brand_metrics(self):
        if self._brand_metrics is None:
            from .services.reporting.brand_metrics import BrandMetricsAPI
            self._brand_metrics = self._client._create_client(BrandMetricsAPI)
        return self._brand_metrics

    @property
    def mmm(self):
        if self._mmm is None:
            from .services.reporting.mmm import MarketingMixModelingAPI
            self._mmm = self._client._create_client(MarketingMixModelingAPI)
        return self._mmm


class _InsightsModule:
    """Insights 子模块 — audience_insights, keyword_insights"""

    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._audience_insights = None
        self._keyword_insights = None

    @property
    def audience_insights(self):
        if self._audience_insights is None:
            from .services.insights.audience_insights import AudienceInsightsAPI
            self._audience_insights = self._client._create_client(AudienceInsightsAPI)
        return self._audience_insights

    @property
    def keyword_insights(self):
        if self._keyword_insights is None:
            from .services.insights.keyword_insights import KeywordInsightsAPI
            self._keyword_insights = self._client._create_client(KeywordInsightsAPI)
        return self._keyword_insights


class _CommonServicesModule:
    """Common Services 子模块 — stores, assets, history, attribution"""

    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._stores = None
        self._assets = None
        self._history = None
        self._attribution = None

    @property
    def stores(self):
        if self._stores is None:
            from .services.common.stores import StoresAPI
            self._stores = self._client._create_client(StoresAPI)
        return self._stores

    @property
    def assets(self):
        if self._assets is None:
            from .services.common.assets import AssetsAPI
            self._assets = self._client._create_client(AssetsAPI)
        return self._assets

    @property
    def history(self):
        if self._history is None:
            from .services.common.history import HistoryAPI
            self._history = self._client._create_client(HistoryAPI)
        return self._history

    @property
    def attribution(self):
        if self._attribution is None:
            from .services.common.attribution import AttributionAPI
            self._attribution = self._client._create_client(AttributionAPI)
        return self._attribution


class _MediaPlanningModule:
    """Media Planning 子模块"""

    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._reach_forecasting = None

    @property
    def reach_forecasting(self):
        if self._reach_forecasting is None:
            from .services.media_planning.reach_forecasting import ReachForecastingAPI
            self._reach_forecasting = self._client._create_client(ReachForecastingAPI)
        return self._reach_forecasting


class _ServiceAPIs:
    """L3: Service APIs (产品级聚合)"""

    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._reporting = None
        self._insights = None
        self._recommendations = None
        self._common = None
        self._media_planning = None
        self._ads_data_manager = None
        self._brand_associations = None

    @property
    def reporting(self) -> _ReportingModule:
        if self._reporting is None:
            self._reporting = _ReportingModule(self._client)
        return self._reporting

    @property
    def insights(self) -> _InsightsModule:
        if self._insights is None:
            self._insights = _InsightsModule(self._client)
        return self._insights

    @property
    def recommendations(self):
        if self._recommendations is None:
            from .services.recommendations.recommendations import RecommendationsAPI
            self._recommendations = self._client._create_client(RecommendationsAPI)
        return self._recommendations

    @property
    def common(self) -> _CommonServicesModule:
        if self._common is None:
            self._common = _CommonServicesModule(self._client)
        return self._common

    @property
    def media_planning(self) -> _MediaPlanningModule:
        if self._media_planning is None:
            self._media_planning = _MediaPlanningModule(self._client)
        return self._media_planning

    @property
    def ads_data_manager(self):
        if self._ads_data_manager is None:
            from .services.ads_data_manager.ads_data_manager import AdsDataManagerAPI
            self._ads_data_manager = self._client._create_client(AdsDataManagerAPI)
        return self._ads_data_manager

    @property
    def brand_associations(self):
        if self._brand_associations is None:
            from .services.brand_associations.brand_associations import BrandAssociationsAPI
            self._brand_associations = self._client._create_client(BrandAssociationsAPI)
        return self._brand_associations


# ============================================================
# L4 Experimental Sub-Modules
# ============================================================

class _SponsoredTVModule:
    """Sponsored TV 子模块"""

    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._campaigns = None
        self._ad_groups = None
        self._ads = None
        self._targeting = None
        self._creatives = None

    @property
    def campaigns(self):
        if self._campaigns is None:
            from .experimental.sponsored_tv.campaigns import SponsoredTVCampaignsAPI
            self._campaigns = self._client._create_client(SponsoredTVCampaignsAPI)
        return self._campaigns

    @property
    def ad_groups(self):
        if self._ad_groups is None:
            from .experimental.sponsored_tv.ad_groups import SponsoredTVAdGroupsAPI
            self._ad_groups = self._client._create_client(SponsoredTVAdGroupsAPI)
        return self._ad_groups

    @property
    def ads(self):
        if self._ads is None:
            from .experimental.sponsored_tv.ads import SponsoredTVAdsAPI
            self._ads = self._client._create_client(SponsoredTVAdsAPI)
        return self._ads

    @property
    def targeting(self):
        if self._targeting is None:
            from .experimental.sponsored_tv.targeting import SponsoredTVTargetingAPI
            self._targeting = self._client._create_client(SponsoredTVTargetingAPI)
        return self._targeting

    @property
    def creatives(self):
        if self._creatives is None:
            from .experimental.sponsored_tv.creatives import SponsoredTVCreativesAPI
            self._creatives = self._client._create_client(SponsoredTVCreativesAPI)
        return self._creatives


class _ModerationModule:
    """Moderation 子模块 — pre_moderation, unified_moderation"""

    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._pre_moderation = None
        self._unified_moderation = None

    @property
    def pre_moderation(self):
        if self._pre_moderation is None:
            from .experimental.moderation.pre_moderation import PreModerationAPI
            self._pre_moderation = self._client._create_client(PreModerationAPI)
        return self._pre_moderation

    @property
    def unified_moderation(self):
        if self._unified_moderation is None:
            from .experimental.moderation.unified_moderation import UnifiedModerationAPI
            self._unified_moderation = self._client._create_client(UnifiedModerationAPI)
        return self._unified_moderation


class _ExperimentalAPIs:
    """L4: Experimental APIs (Beta/实验性)"""

    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._sponsored_tv = None
        self._moderation = None
        self._localization = None
        self._ad_library = None
        self._brand_home = None
        self._persona_builder = None
        self._partner_opportunities = None

    @property
    def sponsored_tv(self) -> _SponsoredTVModule:
        if self._sponsored_tv is None:
            self._sponsored_tv = _SponsoredTVModule(self._client)
        return self._sponsored_tv

    @property
    def moderation(self) -> _ModerationModule:
        if self._moderation is None:
            self._moderation = _ModerationModule(self._client)
        return self._moderation

    @property
    def localization(self):
        if self._localization is None:
            from .experimental.localization.localization import LocalizationAPI
            self._localization = self._client._create_client(LocalizationAPI)
        return self._localization

    @property
    def ad_library(self):
        if self._ad_library is None:
            from .experimental.ad_library.ad_library import AdLibraryAPI
            self._ad_library = self._client._create_client(AdLibraryAPI)
        return self._ad_library

    @property
    def brand_home(self):
        if self._brand_home is None:
            from .experimental.brand_home.brand_home import BrandHomeAPI
            self._brand_home = self._client._create_client(BrandHomeAPI)
        return self._brand_home

    @property
    def persona_builder(self):
        if self._persona_builder is None:
            from .experimental.persona_builder.persona_builder import PersonaBuilderAPI
            self._persona_builder = self._client._create_client(PersonaBuilderAPI)
        return self._persona_builder

    @property
    def partner_opportunities(self):
        if self._partner_opportunities is None:
            from .experimental.partner_opportunities.partner_opportunities import PartnerOpportunitiesAPI
            self._partner_opportunities = self._client._create_client(PartnerOpportunitiesAPI)
        return self._partner_opportunities


# ============================================================
# Main Client
# ============================================================

class AmazonAdsClient:
    """
    Amazon Ads API 统一客户端 - v2.2 完整分级架构

    所有 API 通过分级属性树访问:
    - L1 (Core): client.sp.*, client.sb.*, client.sd.*, client.dsp.*, client.accounts.*
    - L1 (Cross-cutting): client.eligibility, client.locations, client.exports, etc.
    - L2 (Reference): client.reference.amc.*, client.reference.unified.*, etc.
    - L3 (Services): client.services.reporting.*, client.services.common.*, etc.
    - L4 (Experimental): client.experimental.sponsored_tv.*, etc.
    """

    def __init__(
        self,
        client_id: str = "",
        client_secret: str = "",
        refresh_token: str = "",
        profile_id: ProfileID | None = None,
        region: AdsRegion | str = AdsRegion.NA,
        max_retries: int = 3,
        timeout: int = 30,
    ) -> None:
        self._client_id = client_id
        self._client_secret = client_secret
        self._refresh_token = refresh_token
        self._profile_id = profile_id
        self._region = region if isinstance(region, AdsRegion) else AdsRegion(region)
        self._max_retries = max_retries
        self._timeout = timeout

        self._sp: Optional[_SPModule] = None
        self._sb: Optional[_SBModule] = None
        self._sd: Optional[_SDModule] = None
        self._dsp: Optional[_DSPModule] = None
        self._accounts: Optional[_AccountsModule] = None
        self._eligibility = None
        self._audiences_discovery = None
        self._product_selector = None
        self._locations = None
        self._exports = None

        self._reference: Optional[_ReferenceAPIs] = None
        self._services: Optional[_ServiceAPIs] = None
        self._experimental_instance: Optional[_ExperimentalAPIs] = None

    def _create_client(self, cls: type[BaseAdsClient]) -> BaseAdsClient:
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
        self._profile_id = profile_id
        self._sp = None
        self._sb = None
        self._sd = None
        self._dsp = None
        self._accounts = None
        self._eligibility = None
        self._audiences_discovery = None
        self._product_selector = None
        self._locations = None
        self._exports = None
        self._reference = None
        self._services = None
        self._experimental_instance = None
        return self

    # ===== L1 Core Modules =====

    @property
    def sp(self) -> _SPModule:
        if self._sp is None:
            self._sp = _SPModule(self)
        return self._sp

    @property
    def sb(self) -> _SBModule:
        if self._sb is None:
            self._sb = _SBModule(self)
        return self._sb

    @property
    def sd(self) -> _SDModule:
        if self._sd is None:
            self._sd = _SDModule(self)
        return self._sd

    @property
    def dsp(self) -> _DSPModule:
        if self._dsp is None:
            self._dsp = _DSPModule(self)
        return self._dsp

    @property
    def accounts(self) -> _AccountsModule:
        if self._accounts is None:
            self._accounts = _AccountsModule(self)
        return self._accounts

    # ===== L1 Cross-cutting APIs =====

    @property
    def eligibility(self):
        if self._eligibility is None:
            from .core.eligibility.eligibility import EligibilityAPI
            self._eligibility = self._create_client(EligibilityAPI)
        return self._eligibility

    @property
    def audiences_discovery(self):
        if self._audiences_discovery is None:
            from .core.audiences.audiences_discovery import AudiencesDiscoveryAPI
            self._audiences_discovery = self._create_client(AudiencesDiscoveryAPI)
        return self._audiences_discovery

    @property
    def product_selector(self):
        if self._product_selector is None:
            from .core.products.product_selector import ProductSelectorAPI
            self._product_selector = self._create_client(ProductSelectorAPI)
        return self._product_selector

    @property
    def locations(self):
        if self._locations is None:
            from .core.locations.locations import LocationsAPI
            self._locations = self._create_client(LocationsAPI)
        return self._locations

    @property
    def exports(self):
        if self._exports is None:
            from .core.exports.exports import ExportsAPI
            self._exports = self._create_client(ExportsAPI)
        return self._exports

    # ===== L2 Reference APIs =====

    @property
    def reference(self) -> _ReferenceAPIs:
        if self._reference is None:
            self._reference = _ReferenceAPIs(self)
        return self._reference

    # ===== L3 Service APIs =====

    @property
    def services(self) -> _ServiceAPIs:
        if self._services is None:
            self._services = _ServiceAPIs(self)
        return self._services

    # ===== L4 Experimental APIs =====

    @property
    def experimental(self) -> _ExperimentalAPIs:
        if self._experimental_instance is None:
            self._experimental_instance = _ExperimentalAPIs(self)
        return self._experimental_instance


__all__ = [
    "AmazonAdsClient",
    "AmazonAdsError",
    "AdsRegion",
    "ProfileID",
]
