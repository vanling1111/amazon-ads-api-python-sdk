"""
Amazon Ads API Python SDK

完整覆盖 Amazon Ads API 的 Python SDK，100% API 覆盖率。

安装：
    pip install amazon-ads-api

快速开始：
    ```python
    from amazon_ads_api import AmazonAdsClient, AdsRegion
    
    # 创建客户端
    client = AmazonAdsClient(
        client_id="xxx",
        client_secret="xxx",
        refresh_token="xxx",
        region=AdsRegion.NA,
    )
    
    # 设置Profile
    client.with_profile("123456789")
    
    # SP操作
    campaigns = client.sp.campaigns.list_campaigns()
    keywords = client.sp.keywords.list_keywords(campaign_id="xxx")
    
    # SB操作
    sb_campaigns = client.sb.campaigns.list_campaigns()
    
    # DSP操作
    orders = client.dsp.orders.list_orders(advertiser_id="xxx")
    
    # 报告
    report = client.reporting.reports.create_and_wait_report(
        report_type="spCampaigns",
        time_unit="DAILY",
        start_date="2024-01-01",
        end_date="2024-01-31",
        metrics=["impressions", "clicks", "spend"],
    )
    
    # 账户
    profiles = client.accounts.profiles.list_profiles()
    portfolios = client.accounts.portfolios.list_portfolios()
    ```
"""

# ============ 基础类 ============
from .base import (
    BaseAdsClient,
    AdsRegion,
    AmazonAdsError,
)

# ============ 统一客户端 ============
from .client import (
    AmazonAdsClient,
    AdsAPIClient,  # 兼容别名
)

# ============ SP (Sponsored Products) ============
from .sp import (
    SPCampaignsAPI,
    SPAdGroupsAPI,
    SPKeywordsAPI,
    SPTargetingAPI,
    SPBudgetRulesAPI,
    SPRecommendationsAPI,
    SPProductEligibilityAPI,
    SPThemeTargetingAPI,
)

# ============ SB (Sponsored Brands) ============
from .sb import (
    SBCampaignsAPI,
    SBAdsAPI,
    SBKeywordsAPI,
    SBCreativesAPI,
    SBBrandVideoAPI,
    SBModerationAPI,
)

# ============ SD (Sponsored Display) ============
from .sd import (
    SDCampaignsAPI,
    SDTargetingAPI,
    SDCreativesAPI,
    SDAudiencesAPI,
    SDModerationAPI,
)

# ============ DSP ============
from .dsp import (
    DSPAudiencesAPI,
    DSPAdvertisersAPI,
    DSPOrdersAPI,
    DSPLineItemsAPI,
    DSPCreativesAPI,
    DSPInventoryAPI,
    DSPMeasurementAPI,
    DSPConversionsAPI,
    DSPTargetKPIAPI,
)

# ============ Reporting ============
from .reporting import (
    ReportsV3API,
    BrandMetricsAPI,
    StoresAnalyticsAPI,
    MarketingMixModelingAPI,
)

# ============ Accounts ============
from .accounts import (
    ProfilesAPI,
    PortfoliosAPI,
    BillingAPI,
    AccountBudgetsAPI,
    TestAccountsAPI,
)

# ============ Common ============
from .common import (
    AttributionAPI,
    StoresAPI,
    AssetsAPI,
    HistoryAPI,
)

# ============ Insights ============
from .insights import (
    CategoryInsightsAPI,
    KeywordInsightsAPI,
    AudienceInsightsAPI,
)

# ============ Recommendations ============
from .recommendations import (
    PartnerOpportunitiesAPI,
    TacticalRecommendationsAPI,
    PersonaBuilderAPI,
)

# ============ Data Provider ============
from .data_provider import (
    DataProviderMetadataAPI,
    DataProviderRecordsAPI,
    HashedRecordsAPI,
)

# ============ Moderation ============
from .moderation import (
    PreModerationAPI,
    UnifiedModerationAPI,
)

# ============ AMC ============
from .amc import (
    AMCQueriesAPI,
    AMCAudiencesAPI,
    AMCWorkflowsAPI,
)

# ============ Sponsored TV ============
from .sponsored_tv import (
    SponsoredTVCampaignsAPI,
    SponsoredTVAdGroupsAPI,
    SponsoredTVAdsAPI,
    SponsoredTVCreativesAPI,
    SponsoredTVTargetingAPI,
)

# ============ Retail Ad Service ============
from .retail_ad_service import (
    RASCampaignsAPI,
    RASAdGroupsAPI,
    RASProductAdsAPI,
    RASTargetsAPI,
)

# ============ Eligibility ============
from .eligibility import EligibilityAPI

# ============ Locations ============
from .locations import LocationsAPI

# ============ Exports ============
from .exports import ExportsAPI

# ============ Marketing Stream ============
from .stream import MarketingStreamAPI

# ============ Media Planning ============
from .media_planning import ReachForecastingAPI

# ============ Manager Accounts ============
from .manager_accounts import ManagerAccountsAPI

# ============ Posts ============
from .posts import PostsAPI

# ============ Product Metadata ============
from .product_metadata import ProductMetadataAPI

# ============ Audiences Discovery ============
from .audiences_discovery import AudiencesDiscoveryAPI

# ============ Products ============
from .products import ProductSelectorAPI

# ============ Amazon Ads V1 ============
from .amazon_ads_v1 import AmazonAdsV1API

# ============ Ad Library ============
from .ad_library import (
    AdLibraryAPI,
    AdType,
    NameMatchType,
)

# ============ Brand Home ============
from .brand_home import BrandHomeAPI

# ============ Localization ============
from .localization import LocalizationAPI

# ============ Ads Data Manager ============
from .ads_data_manager import AdsDataManagerAPI

# ============ Brand Associations ============
from .brand_associations import BrandAssociationsAPI


__version__ = "1.0.0"

__all__ = [
    # 版本
    "__version__",
    # 基础
    "BaseAdsClient",
    "AdsRegion",
    "AmazonAdsError",
    # 客户端
    "AmazonAdsClient",
    "AdsAPIClient",
    # SP
    "SPCampaignsAPI",
    "SPAdGroupsAPI",
    "SPKeywordsAPI",
    "SPTargetingAPI",
    "SPBudgetRulesAPI",
    "SPRecommendationsAPI",
    "SPProductEligibilityAPI",
    "SPThemeTargetingAPI",
    # SB
    "SBCampaignsAPI",
    "SBAdsAPI",
    "SBKeywordsAPI",
    "SBCreativesAPI",
    "SBBrandVideoAPI",
    "SBModerationAPI",
    # SD
    "SDCampaignsAPI",
    "SDTargetingAPI",
    "SDCreativesAPI",
    "SDAudiencesAPI",
    "SDModerationAPI",
    # DSP
    "DSPAudiencesAPI",
    "DSPAdvertisersAPI",
    "DSPOrdersAPI",
    "DSPLineItemsAPI",
    "DSPCreativesAPI",
    "DSPInventoryAPI",
    "DSPMeasurementAPI",
    "DSPConversionsAPI",
    "DSPTargetKPIAPI",
    # Reporting
    "ReportsV3API",
    "BrandMetricsAPI",
    "StoresAnalyticsAPI",
    "MarketingMixModelingAPI",
    # Accounts
    "ProfilesAPI",
    "PortfoliosAPI",
    "BillingAPI",
    "AccountBudgetsAPI",
    "TestAccountsAPI",
    # Common
    "AttributionAPI",
    "StoresAPI",
    "AssetsAPI",
    "HistoryAPI",
    # Insights
    "CategoryInsightsAPI",
    "KeywordInsightsAPI",
    "AudienceInsightsAPI",
    # Recommendations
    "PartnerOpportunitiesAPI",
    "TacticalRecommendationsAPI",
    "PersonaBuilderAPI",
    # Data Provider
    "DataProviderMetadataAPI",
    "DataProviderRecordsAPI",
    "HashedRecordsAPI",
    # Moderation
    "PreModerationAPI",
    "UnifiedModerationAPI",
    # AMC
    "AMCQueriesAPI",
    "AMCAudiencesAPI",
    "AMCWorkflowsAPI",
    # Sponsored TV
    "SponsoredTVCampaignsAPI",
    "SponsoredTVAdGroupsAPI",
    "SponsoredTVAdsAPI",
    "SponsoredTVCreativesAPI",
    "SponsoredTVTargetingAPI",
    # Retail Ad Service
    "RASCampaignsAPI",
    "RASAdGroupsAPI",
    "RASProductAdsAPI",
    "RASTargetsAPI",
    # 其他
    "EligibilityAPI",
    "LocationsAPI",
    "ExportsAPI",
    "MarketingStreamAPI",
    "ReachForecastingAPI",
    "ManagerAccountsAPI",
    "PostsAPI",
    "ProductMetadataAPI",
    "AudiencesDiscoveryAPI",
    "ProductSelectorAPI",
    # Amazon Ads V1
    "AmazonAdsV1API",
    # Ad Library
    "AdLibraryAPI",
    "AdType",
    "NameMatchType",
    # Brand Home
    "BrandHomeAPI",
    # Localization
    "LocalizationAPI",
    # Ads Data Manager
    "AdsDataManagerAPI",
    # Brand Associations
    "BrandAssociationsAPI",
]
