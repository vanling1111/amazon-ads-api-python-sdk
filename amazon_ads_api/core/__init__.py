"""
Amazon Ads API - Core APIs (L1)

OpenAPI 验证的核心 API，可信度最高，生产可用。

使用方式:
    from amazon_ads_api.core.sp import SPCampaignsAPI
    from amazon_ads_api.core.sb import SBCampaignsAPI
    
或通过 Client:
    client.sp.campaigns.list()

包含:
- sp: Sponsored Products
- sb: Sponsored Brands
- sd: Sponsored Display
- dsp: Amazon DSP
- accounts: Profiles, Portfolios, Billing
- audiences: Audiences Discovery
- eligibility: Eligibility
- exports: Exports
- products: Products
- locations: Locations
"""

# SP
from .sp.campaigns import SPCampaignsAPI
from .sp.ad_groups import SPAdGroupsAPI
from .sp.keywords import SPKeywordsAPI
from .sp.targeting import SPTargetingAPI
from .sp.budget_rules import SPBudgetRulesAPI
from .sp.campaign_optimization import SPCampaignOptimizationAPI
from .sp.recommendations import SPRecommendationsAPI
from .sp.theme_targeting import SPThemeTargetingAPI
from .sp.target_promotion_groups import SPTargetPromotionGroupsAPI
from .sp.global_recommendations import SPGlobalRecommendationsAPI

# SB
from .sb.campaigns import SBCampaignsAPI
from .sb.keywords import SBKeywordsAPI
from .sb.ads import SBAdsAPI
from .sb.creatives import SBCreativesAPI
from .sb.brand_video import SBBrandVideoAPI
from .sb.moderation import SBModerationAPI
from .sb.optimization import SBOptimizationAPI
from .sb.forecasts import SBForecastsAPI
from .sb.targeting import SBTargetingAPI
from .sb.legacy_migration import SBLegacyMigrationAPI

# SD
from .sd.campaigns import SDCampaignsAPI
from .sd.targeting import SDTargetingAPI
from .sd.audiences import SDAudiencesAPI
from .sd.creatives import SDCreativesAPI
from .sd.moderation import SDModerationAPI
from .sd.optimization import SDOptimizationAPI
from .sd.brand_safety import SDBrandSafetyAPI
from .sd.locations import SDLocationsAPI
from .sd.reports import SDReportsAPI

# DSP
from .dsp.campaigns import DSPCampaignsAPI
from .dsp.advertisers import DSPAdvertisersAPI
from .dsp.audiences import DSPAudiencesAPI
from .dsp.conversions import DSPConversionsAPI
from .dsp.measurement import DSPMeasurementAPI
from .dsp.target_kpi import DSPTargetKPIAPI

# Accounts
from .accounts.profiles import ProfilesAPI
from .accounts.portfolios import PortfoliosAPI
from .accounts.billing import BillingAPI
from .accounts.budgets import AccountBudgetsAPI
from .accounts.test_accounts import TestAccountsAPI

# Other L1 modules
from .audiences.audiences_discovery import AudiencesDiscoveryAPI
from .eligibility.eligibility import EligibilityAPI
from .exports.exports import ExportsAPI
from .products.product_selector import ProductSelectorAPI
from .locations.locations import LocationsAPI

__all__ = [
    # SP
    "SPCampaignsAPI",
    "SPAdGroupsAPI",
    "SPKeywordsAPI",
    "SPTargetingAPI",
    "SPBudgetRulesAPI",
    "SPCampaignOptimizationAPI",
    "SPRecommendationsAPI",
    "SPThemeTargetingAPI",
    "SPTargetPromotionGroupsAPI",
    "SPGlobalRecommendationsAPI",
    # SB
    "SBCampaignsAPI",
    "SBKeywordsAPI",
    "SBAdsAPI",
    "SBCreativesAPI",
    "SBBrandVideoAPI",
    "SBModerationAPI",
    "SBOptimizationAPI",
    "SBForecastsAPI",
    "SBTargetingAPI",
    "SBLegacyMigrationAPI",
    # SD
    "SDCampaignsAPI",
    "SDTargetingAPI",
    "SDAudiencesAPI",
    "SDCreativesAPI",
    "SDModerationAPI",
    "SDOptimizationAPI",
    "SDBrandSafetyAPI",
    "SDLocationsAPI",
    "SDReportsAPI",
    # DSP
    "DSPCampaignsAPI",
    "DSPAdvertisersAPI",
    "DSPAudiencesAPI",
    "DSPConversionsAPI",
    "DSPMeasurementAPI",
    "DSPTargetKPIAPI",
    # Accounts
    "ProfilesAPI",
    "PortfoliosAPI",
    "BillingAPI",
    "AccountBudgetsAPI",
    "TestAccountsAPI",
    # Other
    "AudiencesDiscoveryAPI",
    "EligibilityAPI",
    "ExportsAPI",
    "ProductSelectorAPI",
    "LocationsAPI",
]
