"""
Amazon Ads API 统一客户端 - v2 分级架构

API 分级:
- L1 (Core): sp, sb, sd, dsp, accounts - OpenAPI 验证，生产可用
- L2 (Reference): reference.* - 官方文档确认，非 OpenAPI
- L3 (Services): services.* - 产品级聚合
- L4 (Experimental): experimental().* - Beta/实验性

使用示例:
    client = AmazonAdsClient(
        client_id="xxx",
        client_secret="xxx",
        refresh_token="xxx",
        profile_id="123456789",
        region="NA"
    )
    
    # L1 Core APIs (默认访问，最安全)
    campaigns = await client.sp.campaigns.list()
    
    # L2 Reference APIs (显式命名空间)
    result = await client.reference.amc.run_query(...)
    
    # L3 Service APIs
    report = await client.services.reporting.create_report(...)
    
    # L4 Experimental APIs (需确认风险)
    exp = client.experimental(acknowledge_risk=True)
    await exp.sponsored_tv.create_campaign(...)
"""

from __future__ import annotations

import warnings
from typing import TYPE_CHECKING, Self, Optional

from .base import BaseAdsClient, AdsRegion, ProfileID, AmazonAdsError

if TYPE_CHECKING:
    # L1 Core
    from .core.sp.campaigns import SPCampaignsAPI
    from .core.sp.ad_groups import SPAdGroupsAPI
    from .core.sp.keywords import SPKeywordsAPI
    from .core.sp.targeting import SPTargetingAPI
    from .core.sp.budget_rules import SPBudgetRulesAPI
    from .core.sp.campaign_optimization import SPCampaignOptimizationAPI
    from .core.sp.recommendations import SPRecommendationsAPI
    from .core.sp.product_eligibility import SPProductEligibilityAPI
    from .core.sp.theme_targeting import SPThemeTargetingAPI
    from .core.sp.target_promotion_groups import SPTargetPromotionGroupsAPI
    from .core.sp.global_recommendations import SPGlobalRecommendationsAPI
    
    from .core.sb.campaigns import SBCampaignsAPI
    from .core.sb.keywords import SBKeywordsAPI
    from .core.sb.ads import SBAdsAPI
    from .core.sb.creatives import SBCreativesAPI
    from .core.sb.brand_video import SBBrandVideoAPI
    from .core.sb.moderation import SBModerationAPI
    from .core.sb.optimization import SBOptimizationAPI
    from .core.sb.forecasts import SBForecastsAPI
    from .core.sb.targeting import SBTargetingAPI
    from .core.sb.legacy_migration import SBLegacyMigrationAPI
    
    from .core.sd.campaigns import SDCampaignsAPI
    from .core.sd.targeting import SDTargetingAPI
    from .core.sd.audiences import SDAudiencesAPI
    from .core.sd.creatives import SDCreativesAPI
    from .core.sd.moderation import SDModerationAPI
    
    from .core.dsp.campaigns import DSPCampaignsAPI
    from .core.dsp.advertisers import DSPAdvertisersAPI
    from .core.dsp.audiences import DSPAudiencesAPI
    from .core.dsp.conversions import DSPConversionsAPI
    from .core.dsp.measurement import DSPMeasurementAPI
    
    from .core.accounts.profiles import ProfilesAPI
    from .core.accounts.portfolios import PortfoliosAPI
    from .core.accounts.billing import BillingAPI


# ============================================================
# L1 Core Modules
# ============================================================

class _SPModule:
    """Sponsored Products 模块 (L1 - OpenAPI 验证)"""
    
    API_TIER = "L1"
    API_SOURCE = "openapi"
    
    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._campaigns: Optional["SPCampaignsAPI"] = None
        self._ad_groups: Optional["SPAdGroupsAPI"] = None
        self._keywords: Optional["SPKeywordsAPI"] = None
        self._targeting: Optional["SPTargetingAPI"] = None
        self._budget_rules: Optional["SPBudgetRulesAPI"] = None
        self._optimization: Optional["SPCampaignOptimizationAPI"] = None
        self._recommendations: Optional["SPRecommendationsAPI"] = None
        self._eligibility: Optional["SPProductEligibilityAPI"] = None
        self._theme: Optional["SPThemeTargetingAPI"] = None
        self._promotion_groups: Optional["SPTargetPromotionGroupsAPI"] = None
        self._global_recs: Optional["SPGlobalRecommendationsAPI"] = None
    
    @property
    def campaigns(self) -> "SPCampaignsAPI":
        """SP Campaigns API"""
        if self._campaigns is None:
            from .core.sp.campaigns import SPCampaignsAPI
            self._campaigns = self._client._create_client(SPCampaignsAPI)
        return self._campaigns
    
    @property
    def ad_groups(self) -> "SPAdGroupsAPI":
        """SP Ad Groups API"""
        if self._ad_groups is None:
            from .core.sp.ad_groups import SPAdGroupsAPI
            self._ad_groups = self._client._create_client(SPAdGroupsAPI)
        return self._ad_groups
    
    @property
    def keywords(self) -> "SPKeywordsAPI":
        """SP Keywords API"""
        if self._keywords is None:
            from .core.sp.keywords import SPKeywordsAPI
            self._keywords = self._client._create_client(SPKeywordsAPI)
        return self._keywords
    
    @property
    def targeting(self) -> "SPTargetingAPI":
        """SP Targeting API"""
        if self._targeting is None:
            from .core.sp.targeting import SPTargetingAPI
            self._targeting = self._client._create_client(SPTargetingAPI)
        return self._targeting
    
    @property
    def budget_rules(self) -> "SPBudgetRulesAPI":
        """SP Budget Rules API"""
        if self._budget_rules is None:
            from .core.sp.budget_rules import SPBudgetRulesAPI
            self._budget_rules = self._client._create_client(SPBudgetRulesAPI)
        return self._budget_rules
    
    @property
    def optimization(self) -> "SPCampaignOptimizationAPI":
        """SP Campaign Optimization API"""
        if self._optimization is None:
            from .core.sp.campaign_optimization import SPCampaignOptimizationAPI
            self._optimization = self._client._create_client(SPCampaignOptimizationAPI)
        return self._optimization
    
    @property
    def recommendations(self) -> "SPRecommendationsAPI":
        """SP Recommendations API"""
        if self._recommendations is None:
            from .core.sp.recommendations import SPRecommendationsAPI
            self._recommendations = self._client._create_client(SPRecommendationsAPI)
        return self._recommendations


class _SBModule:
    """Sponsored Brands 模块 (L1 - OpenAPI 验证)"""
    
    API_TIER = "L1"
    API_SOURCE = "openapi"
    
    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._campaigns: Optional["SBCampaignsAPI"] = None
        self._keywords: Optional["SBKeywordsAPI"] = None
        self._ads: Optional["SBAdsAPI"] = None
        self._creatives: Optional["SBCreativesAPI"] = None
        self._brand_video: Optional["SBBrandVideoAPI"] = None
        self._moderation: Optional["SBModerationAPI"] = None
        self._optimization: Optional["SBOptimizationAPI"] = None
        self._forecasts: Optional["SBForecastsAPI"] = None
        self._targeting: Optional["SBTargetingAPI"] = None
    
    @property
    def campaigns(self) -> "SBCampaignsAPI":
        """SB Campaigns API"""
        if self._campaigns is None:
            from .core.sb.campaigns import SBCampaignsAPI
            self._campaigns = self._client._create_client(SBCampaignsAPI)
        return self._campaigns
    
    @property
    def keywords(self) -> "SBKeywordsAPI":
        """SB Keywords API"""
        if self._keywords is None:
            from .core.sb.keywords import SBKeywordsAPI
            self._keywords = self._client._create_client(SBKeywordsAPI)
        return self._keywords
    
    @property
    def ads(self) -> "SBAdsAPI":
        """SB Ads API"""
        if self._ads is None:
            from .core.sb.ads import SBAdsAPI
            self._ads = self._client._create_client(SBAdsAPI)
        return self._ads
    
    @property
    def creatives(self) -> "SBCreativesAPI":
        """SB Creatives API"""
        if self._creatives is None:
            from .core.sb.creatives import SBCreativesAPI
            self._creatives = self._client._create_client(SBCreativesAPI)
        return self._creatives
    
    @property
    def moderation(self) -> "SBModerationAPI":
        """SB Moderation API"""
        if self._moderation is None:
            from .core.sb.moderation import SBModerationAPI
            self._moderation = self._client._create_client(SBModerationAPI)
        return self._moderation


class _SDModule:
    """Sponsored Display 模块 (L1 - OpenAPI 验证)"""
    
    API_TIER = "L1"
    API_SOURCE = "openapi"
    
    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._campaigns: Optional["SDCampaignsAPI"] = None
        self._targeting: Optional["SDTargetingAPI"] = None
        self._audiences: Optional["SDAudiencesAPI"] = None
        self._creatives: Optional["SDCreativesAPI"] = None
        self._moderation: Optional["SDModerationAPI"] = None
    
    @property
    def campaigns(self) -> "SDCampaignsAPI":
        """SD Campaigns API"""
        if self._campaigns is None:
            from .core.sd.campaigns import SDCampaignsAPI
            self._campaigns = self._client._create_client(SDCampaignsAPI)
        return self._campaigns
    
    @property
    def targeting(self) -> "SDTargetingAPI":
        """SD Targeting API"""
        if self._targeting is None:
            from .core.sd.targeting import SDTargetingAPI
            self._targeting = self._client._create_client(SDTargetingAPI)
        return self._targeting
    
    @property
    def audiences(self) -> "SDAudiencesAPI":
        """SD Audiences API"""
        if self._audiences is None:
            from .core.sd.audiences import SDAudiencesAPI
            self._audiences = self._client._create_client(SDAudiencesAPI)
        return self._audiences
    
    @property
    def creatives(self) -> "SDCreativesAPI":
        """SD Creatives API"""
        if self._creatives is None:
            from .core.sd.creatives import SDCreativesAPI
            self._creatives = self._client._create_client(SDCreativesAPI)
        return self._creatives


class _DSPModule:
    """Amazon DSP 模块 (L1 - OpenAPI 验证)"""
    
    API_TIER = "L1"
    API_SOURCE = "openapi"
    
    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._campaigns: Optional["DSPCampaignsAPI"] = None
        self._advertisers: Optional["DSPAdvertisersAPI"] = None
        self._audiences: Optional["DSPAudiencesAPI"] = None
        self._conversions: Optional["DSPConversionsAPI"] = None
        self._measurement: Optional["DSPMeasurementAPI"] = None
    
    @property
    def campaigns(self) -> "DSPCampaignsAPI":
        """DSP Campaigns API"""
        if self._campaigns is None:
            from .core.dsp.campaigns import DSPCampaignsAPI
            self._campaigns = self._client._create_client(DSPCampaignsAPI)
        return self._campaigns
    
    @property
    def advertisers(self) -> "DSPAdvertisersAPI":
        """DSP Advertisers API"""
        if self._advertisers is None:
            from .core.dsp.advertisers import DSPAdvertisersAPI
            self._advertisers = self._client._create_client(DSPAdvertisersAPI)
        return self._advertisers
    
    @property
    def audiences(self) -> "DSPAudiencesAPI":
        """DSP Audiences API"""
        if self._audiences is None:
            from .core.dsp.audiences import DSPAudiencesAPI
            self._audiences = self._client._create_client(DSPAudiencesAPI)
        return self._audiences
    
    @property
    def conversions(self) -> "DSPConversionsAPI":
        """DSP Conversions API"""
        if self._conversions is None:
            from .core.dsp.conversions import DSPConversionsAPI
            self._conversions = self._client._create_client(DSPConversionsAPI)
        return self._conversions
    
    @property
    def measurement(self) -> "DSPMeasurementAPI":
        """DSP Measurement API"""
        if self._measurement is None:
            from .core.dsp.measurement import DSPMeasurementAPI
            self._measurement = self._client._create_client(DSPMeasurementAPI)
        return self._measurement


class _AccountsModule:
    """账户管理模块 (L1 - OpenAPI 验证)"""
    
    API_TIER = "L1"
    API_SOURCE = "openapi"
    
    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._profiles: Optional["ProfilesAPI"] = None
        self._portfolios: Optional["PortfoliosAPI"] = None
        self._billing: Optional["BillingAPI"] = None
    
    @property
    def profiles(self) -> "ProfilesAPI":
        """Profiles API"""
        if self._profiles is None:
            from .core.accounts.profiles import ProfilesAPI
            self._profiles = self._client._create_client(ProfilesAPI)
        return self._profiles
    
    @property
    def portfolios(self) -> "PortfoliosAPI":
        """Portfolios API"""
        if self._portfolios is None:
            from .core.accounts.portfolios import PortfoliosAPI
            self._portfolios = self._client._create_client(PortfoliosAPI)
        return self._portfolios
    
    @property
    def billing(self) -> "BillingAPI":
        """Billing API"""
        if self._billing is None:
            from .core.accounts.billing import BillingAPI
            self._billing = self._client._create_client(BillingAPI)
        return self._billing


# ============================================================
# L2 Reference Module
# ============================================================

class _ReferenceAPIs:
    """
    L2: Reference APIs (非 OpenAPI 但官方文档确认)
    
    使用方式:
        client.reference.amc.run_query(...)
        client.reference.stream.subscribe(...)
    """
    
    API_TIER = "L2"
    API_SOURCE = "api-reference"
    
    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._amc = None
        self._stream = None
        self._attribution = None
        self._retail_ad = None
        self._posts = None
    
    @property
    def amc(self):
        """Amazon Marketing Cloud API (L2)"""
        if self._amc is None:
            from .reference.amc.queries import AMCQueriesAPI
            self._amc = self._client._create_client(AMCQueriesAPI)
        return self._amc
    
    @property
    def stream(self):
        """Amazon Marketing Stream API (L2)"""
        if self._stream is None:
            from .reference.stream.subscriptions import MarketingStreamAPI
            self._stream = self._client._create_client(MarketingStreamAPI)
        return self._stream
    
    @property
    def attribution(self):
        """Amazon Attribution API (L2)"""
        if self._attribution is None:
            from .services.common.attribution import AttributionAPI
            self._attribution = self._client._create_client(AttributionAPI)
        return self._attribution
    
    @property
    def retail_ad(self):
        """Retail Ad Service API (L2)"""
        if self._retail_ad is None:
            from .reference.retail_ad_service.campaigns import RASCampaignsAPI
            self._retail_ad = self._client._create_client(RASCampaignsAPI)
        return self._retail_ad
    
    @property
    def posts(self):
        """Posts API (L2)"""
        if self._posts is None:
            from .reference.posts.posts import PostsAPI
            self._posts = self._client._create_client(PostsAPI)
        return self._posts


# ============================================================
# L3 Services Module
# ============================================================

class _ServiceAPIs:
    """
    L3: Service APIs (产品级聚合)
    
    使用方式:
        client.services.reporting.create_report(...)
        client.services.insights.get_audience_insights(...)
    """
    
    API_TIER = "L3"
    API_SOURCE = "product-level"
    
    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._reporting = None
        self._insights = None
        self._recommendations = None
        self._assets = None
        self._history = None
    
    @property
    def reporting(self):
        """Reporting API (L3)"""
        if self._reporting is None:
            from .services.reporting.reports_v3 import ReportsV3API
            self._reporting = self._client._create_client(ReportsV3API)
        return self._reporting
    
    @property
    def insights(self):
        """Audience Insights API (L3)"""
        if self._insights is None:
            from .services.insights.audience_insights import AudienceInsightsAPI
            self._insights = self._client._create_client(AudienceInsightsAPI)
        return self._insights
    
    @property
    def recommendations(self):
        """Recommendations API (L3)"""
        if self._recommendations is None:
            from .services.recommendations.recommendations import RecommendationsAPI
            self._recommendations = self._client._create_client(RecommendationsAPI)
        return self._recommendations
    
    @property
    def assets(self):
        """Assets API (L3)"""
        if self._assets is None:
            from .services.common.assets import AssetsAPI
            self._assets = self._client._create_client(AssetsAPI)
        return self._assets
    
    @property
    def history(self):
        """History API (L3)"""
        if self._history is None:
            from .services.common.history import HistoryAPI
            self._history = self._client._create_client(HistoryAPI)
        return self._history


# ============================================================
# L4 Experimental Module  
# ============================================================

class _ExperimentalAPIs:
    """
    L4: Experimental APIs (Beta/实验性)
    
    ⚠️ 警告: 这些 API 可能不稳定，随时可能变更
    """
    
    API_TIER = "L4"
    API_SOURCE = "experimental"
    
    def __init__(self, client: "AmazonAdsClient"):
        self._client = client
        self._sponsored_tv = None
        self._moderation = None
        self._localization = None
        self._ad_library = None
        self._brand_home = None
    
    @property
    def sponsored_tv(self):
        """Sponsored TV API (L4 - Beta)"""
        warnings.warn(
            "Sponsored TV API 处于 Beta 阶段，可能不稳定或随时变更。",
            UserWarning,
            stacklevel=2
        )
        if self._sponsored_tv is None:
            from .experimental.sponsored_tv.campaigns import SponsoredTVCampaignsAPI
            self._sponsored_tv = self._client._create_client(SponsoredTVCampaignsAPI)
        return self._sponsored_tv
    
    @property
    def moderation(self):
        """Moderation API (L4 - UI-bound)"""
        warnings.warn(
            "Moderation API 可能依赖 UI 行为，不保证稳定性。",
            UserWarning,
            stacklevel=2
        )
        if self._moderation is None:
            from .experimental.moderation.unified_moderation import UnifiedModerationAPI
            self._moderation = self._client._create_client(UnifiedModerationAPI)
        return self._moderation
    
    @property
    def localization(self):
        """Localization API (L4)"""
        warnings.warn(
            "Localization API 文档不完整，可能不稳定。",
            UserWarning,
            stacklevel=2
        )
        if self._localization is None:
            from .experimental.localization.localization import LocalizationAPI
            self._localization = self._client._create_client(LocalizationAPI)
        return self._localization
    
    @property
    def ad_library(self):
        """Ad Library API (L4)"""
        warnings.warn(
            "Ad Library API 是实验性功能。",
            UserWarning,
            stacklevel=2
        )
        if self._ad_library is None:
            from .experimental.ad_library.ad_library import AdLibraryAPI
            self._ad_library = self._client._create_client(AdLibraryAPI)
        return self._ad_library
    
    @property
    def brand_home(self):
        """Brand Home API (L4)"""
        warnings.warn(
            "Brand Home API 是实验性功能。",
            UserWarning,
            stacklevel=2
        )
        if self._brand_home is None:
            from .experimental.brand_home.brand_home import BrandHomeAPI
            self._brand_home = self._client._create_client(BrandHomeAPI)
        return self._brand_home


# ============================================================
# Main Client
# ============================================================

class AmazonAdsClient:
    """
    Amazon Ads API 统一客户端 - v2 分级架构
    
    API 分级:
    - L1 (Core): sp, sb, sd, dsp, accounts - OpenAPI 验证，生产可用
    - L2 (Reference): reference.* - 官方文档确认，非 OpenAPI
    - L3 (Services): services.* - 产品级聚合
    - L4 (Experimental): experimental().* - Beta/实验性
    
    使用示例:
        client = AmazonAdsClient(
            client_id="xxx",
            client_secret="xxx",
            refresh_token="xxx",
            profile_id="123456789",
            region="NA"
        )
        
        # L1: 默认访问（最安全）
        campaigns = await client.sp.campaigns.list_campaigns()
        
        # L2: 显式命名空间
        result = await client.reference.amc.run_query(...)
        
        # L3: 服务层
        report = await client.services.reporting.create_report(...)
        
        # L4: 需确认风险
        exp = client.experimental(acknowledge_risk=True)
        await exp.sponsored_tv.create_campaign(...)
    """
    
    __slots__ = (
        "_client_id", "_client_secret", "_refresh_token",
        "_region", "_profile_id", "_max_retries", "_timeout",
        # L1 Core
        "_sp", "_sb", "_sd", "_dsp", "_accounts",
        # L2/L3/L4 containers
        "_reference", "_services", "_experimental_instance",
    )
    
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
        
        # L1 Core modules (lazy loaded)
        self._sp: Optional[_SPModule] = None
        self._sb: Optional[_SBModule] = None
        self._sd: Optional[_SDModule] = None
        self._dsp: Optional[_DSPModule] = None
        self._accounts: Optional[_AccountsModule] = None
        
        # L2/L3/L4 containers
        self._reference: Optional[_ReferenceAPIs] = None
        self._services: Optional[_ServiceAPIs] = None
        self._experimental_instance: Optional[_ExperimentalAPIs] = None
    
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
        """设置 Profile ID"""
        self._profile_id = profile_id
        # 重置所有模块以应用新 Profile
        self._sp = None
        self._sb = None
        self._sd = None
        self._dsp = None
        self._accounts = None
        self._reference = None
        self._services = None
        self._experimental_instance = None
        return self
    
    # ===== L1 Core APIs =====
    
    @property
    def sp(self) -> _SPModule:
        """
        Sponsored Products API (L1 - OpenAPI 验证)
        
        使用示例:
            campaigns = await client.sp.campaigns.list_campaigns()
            ad_groups = await client.sp.ad_groups.list_ad_groups(campaign_id="...")
        """
        if self._sp is None:
            self._sp = _SPModule(self)
        return self._sp
    
    @property
    def sb(self) -> _SBModule:
        """
        Sponsored Brands API (L1 - OpenAPI 验证)
        
        使用示例:
            campaigns = await client.sb.campaigns.list_campaigns()
            keywords = await client.sb.keywords.list_keywords(campaign_id="...")
        """
        if self._sb is None:
            self._sb = _SBModule(self)
        return self._sb
    
    @property
    def sd(self) -> _SDModule:
        """
        Sponsored Display API (L1 - OpenAPI 验证)
        
        使用示例:
            campaigns = await client.sd.campaigns.list_campaigns()
            targeting = await client.sd.targeting.list_targets()
        """
        if self._sd is None:
            self._sd = _SDModule(self)
        return self._sd
    
    @property
    def dsp(self) -> _DSPModule:
        """
        Amazon DSP API (L1 - OpenAPI 验证)
        
        使用示例:
            advertisers = await client.dsp.advertisers.list_advertisers()
            campaigns = await client.dsp.campaigns.list_campaigns()
        """
        if self._dsp is None:
            self._dsp = _DSPModule(self)
        return self._dsp
    
    @property
    def accounts(self) -> _AccountsModule:
        """
        账户管理 API (L1 - OpenAPI 验证)
        
        使用示例:
            profiles = await client.accounts.profiles.list_profiles()
            portfolios = await client.accounts.portfolios.list_portfolios()
        """
        if self._accounts is None:
            self._accounts = _AccountsModule(self)
        return self._accounts
    
    # ===== L2 Reference APIs =====
    
    @property
    def reference(self) -> _ReferenceAPIs:
        """
        Reference APIs (L2 - 官方文档确认，非 OpenAPI)
        
        包含:
        - amc: Amazon Marketing Cloud
        - stream: Amazon Marketing Stream
        - attribution: Amazon Attribution
        - retail_ad: Retail Ad Service
        - posts: Posts API
        
        使用示例:
            result = await client.reference.amc.run_query(...)
            await client.reference.stream.subscribe(...)
        """
        if self._reference is None:
            self._reference = _ReferenceAPIs(self)
        return self._reference
    
    # ===== L3 Service APIs =====
    
    @property
    def services(self) -> _ServiceAPIs:
        """
        Service APIs (L3 - 产品级聚合)
        
        包含:
        - reporting: 报告服务
        - insights: 洞察服务
        - recommendations: 推荐服务
        - assets: 资产管理
        - history: 变更历史
        
        使用示例:
            report = await client.services.reporting.create_report(...)
            insights = await client.services.insights.get_overlapping_audiences(...)
        """
        if self._services is None:
            self._services = _ServiceAPIs(self)
        return self._services
    
    # ===== L4 Experimental APIs =====
    
    def experimental(self, acknowledge_risk: bool = False) -> _ExperimentalAPIs:
        """
        Experimental APIs (L4 - Beta/实验性)
        
        ⚠️ 警告: 这些 API 可能不稳定，随时可能变更
        
        Args:
            acknowledge_risk: 必须设为 True 以确认了解风险
        
        Returns:
            _ExperimentalAPIs: 实验性 API 容器
        
        Raises:
            RuntimeError: 如果未确认风险
        
        使用示例:
            exp = client.experimental(acknowledge_risk=True)
            await exp.sponsored_tv.create_campaign(...)
        """
        if not acknowledge_risk:
            raise RuntimeError(
                "实验性 API 需要显式确认风险。\n"
                "请使用: client.experimental(acknowledge_risk=True)\n\n"
                "⚠️ 警告: L4 API 可能不稳定或随时变更，生产环境使用需谨慎。"
            )
        
        if self._experimental_instance is None:
            self._experimental_instance = _ExperimentalAPIs(self)
        return self._experimental_instance


# 导出
__all__ = [
    "AmazonAdsClient",
    "AmazonAdsError",
    "AdsRegion",
    "ProfileID",
    # L1 Modules
    "_SPModule",
    "_SBModule",
    "_SDModule",
    "_DSPModule",
    "_AccountsModule",
    # L2/L3/L4 Modules
    "_ReferenceAPIs",
    "_ServiceAPIs",
    "_ExperimentalAPIs",
]
