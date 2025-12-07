"""
Amazon Ads API Python SDK - Complete Import Tests
Tests ALL 96+ API classes
"""
import sys


def test_all_imports():
    """Test all API class imports"""
    
    all_imports = []
    failed = []
    
    # ============ Base Classes ============
    print("\n[1/30] Base classes...")
    try:
        from amazon_ads_api.base import BaseAdsClient, AdsRegion, AmazonAdsError
        all_imports.extend(["BaseAdsClient", "AdsRegion", "AmazonAdsError"])
        print("  OK: BaseAdsClient, AdsRegion, AmazonAdsError")
    except Exception as e:
        failed.append(("base", str(e)))
        print(f"  FAIL: {e}")

    # ============ Main Client ============
    print("\n[2/30] Main client...")
    try:
        from amazon_ads_api.client import AmazonAdsClient, AdsAPIClient
        all_imports.extend(["AmazonAdsClient", "AdsAPIClient"])
        print("  OK: AmazonAdsClient, AdsAPIClient")
    except Exception as e:
        failed.append(("client", str(e)))
        print(f"  FAIL: {e}")

    # ============ SP Module (8 classes) ============
    print("\n[3/30] SP (Sponsored Products) module...")
    try:
        from amazon_ads_api.sp import (
            SPCampaignsAPI, SPAdGroupsAPI, SPKeywordsAPI, SPTargetingAPI,
            SPBudgetRulesAPI, SPRecommendationsAPI, SPProductEligibilityAPI,
            SPThemeTargetingAPI
        )
        classes = ["SPCampaignsAPI", "SPAdGroupsAPI", "SPKeywordsAPI", "SPTargetingAPI",
                   "SPBudgetRulesAPI", "SPRecommendationsAPI", "SPProductEligibilityAPI",
                   "SPThemeTargetingAPI"]
        all_imports.extend(classes)
        print(f"  OK: {len(classes)} classes")
    except Exception as e:
        failed.append(("sp", str(e)))
        print(f"  FAIL: {e}")

    # ============ SB Module (6 classes) ============
    print("\n[4/30] SB (Sponsored Brands) module...")
    try:
        from amazon_ads_api.sb import (
            SBCampaignsAPI, SBAdsAPI, SBKeywordsAPI, SBCreativesAPI,
            SBBrandVideoAPI, SBModerationAPI
        )
        classes = ["SBCampaignsAPI", "SBAdsAPI", "SBKeywordsAPI", "SBCreativesAPI",
                   "SBBrandVideoAPI", "SBModerationAPI"]
        all_imports.extend(classes)
        print(f"  OK: {len(classes)} classes")
    except Exception as e:
        failed.append(("sb", str(e)))
        print(f"  FAIL: {e}")

    # ============ SD Module (5 classes) ============
    print("\n[5/30] SD (Sponsored Display) module...")
    try:
        from amazon_ads_api.sd import (
            SDCampaignsAPI, SDTargetingAPI, SDCreativesAPI,
            SDAudiencesAPI, SDModerationAPI
        )
        classes = ["SDCampaignsAPI", "SDTargetingAPI", "SDCreativesAPI",
                   "SDAudiencesAPI", "SDModerationAPI"]
        all_imports.extend(classes)
        print(f"  OK: {len(classes)} classes")
    except Exception as e:
        failed.append(("sd", str(e)))
        print(f"  FAIL: {e}")

    # ============ DSP Module (9 classes) ============
    print("\n[6/30] DSP module...")
    try:
        from amazon_ads_api.dsp import (
            DSPAudiencesAPI, DSPAdvertisersAPI, DSPOrdersAPI, DSPLineItemsAPI,
            DSPCreativesAPI, DSPInventoryAPI, DSPMeasurementAPI,
            DSPConversionsAPI, DSPTargetKPIAPI
        )
        classes = ["DSPAudiencesAPI", "DSPAdvertisersAPI", "DSPOrdersAPI", "DSPLineItemsAPI",
                   "DSPCreativesAPI", "DSPInventoryAPI", "DSPMeasurementAPI",
                   "DSPConversionsAPI", "DSPTargetKPIAPI"]
        all_imports.extend(classes)
        print(f"  OK: {len(classes)} classes")
    except Exception as e:
        failed.append(("dsp", str(e)))
        print(f"  FAIL: {e}")

    # ============ Reporting Module (4 classes) ============
    print("\n[7/30] Reporting module...")
    try:
        from amazon_ads_api.reporting import (
            ReportsV3API, BrandMetricsAPI, StoresAnalyticsAPI, MarketingMixModelingAPI
        )
        classes = ["ReportsV3API", "BrandMetricsAPI", "StoresAnalyticsAPI", "MarketingMixModelingAPI"]
        all_imports.extend(classes)
        print(f"  OK: {len(classes)} classes")
    except Exception as e:
        failed.append(("reporting", str(e)))
        print(f"  FAIL: {e}")

    # ============ Accounts Module (5 classes) ============
    print("\n[8/30] Accounts module...")
    try:
        from amazon_ads_api.accounts import (
            ProfilesAPI, PortfoliosAPI, BillingAPI, AccountBudgetsAPI, TestAccountsAPI
        )
        classes = ["ProfilesAPI", "PortfoliosAPI", "BillingAPI", "AccountBudgetsAPI", "TestAccountsAPI"]
        all_imports.extend(classes)
        print(f"  OK: {len(classes)} classes")
    except Exception as e:
        failed.append(("accounts", str(e)))
        print(f"  FAIL: {e}")

    # ============ Common Module (4 classes) ============
    print("\n[9/30] Common module...")
    try:
        from amazon_ads_api.common import (
            AttributionAPI, StoresAPI, AssetsAPI, HistoryAPI
        )
        classes = ["AttributionAPI", "StoresAPI", "AssetsAPI", "HistoryAPI"]
        all_imports.extend(classes)
        print(f"  OK: {len(classes)} classes")
    except Exception as e:
        failed.append(("common", str(e)))
        print(f"  FAIL: {e}")

    # ============ Eligibility Module (1 class) ============
    print("\n[10/30] Eligibility module...")
    try:
        from amazon_ads_api.eligibility import EligibilityAPI
        all_imports.append("EligibilityAPI")
        print("  OK: EligibilityAPI")
    except Exception as e:
        failed.append(("eligibility", str(e)))
        print(f"  FAIL: {e}")

    # ============ Insights Module (3 classes) ============
    print("\n[11/30] Insights module...")
    try:
        from amazon_ads_api.insights import (
            CategoryInsightsAPI, KeywordInsightsAPI, AudienceInsightsAPI
        )
        classes = ["CategoryInsightsAPI", "KeywordInsightsAPI", "AudienceInsightsAPI"]
        all_imports.extend(classes)
        print(f"  OK: {len(classes)} classes")
    except Exception as e:
        failed.append(("insights", str(e)))
        print(f"  FAIL: {e}")

    # ============ Recommendations Module (3 classes) ============
    print("\n[12/30] Recommendations module...")
    try:
        from amazon_ads_api.recommendations import (
            PartnerOpportunitiesAPI, TacticalRecommendationsAPI, PersonaBuilderAPI
        )
        classes = ["PartnerOpportunitiesAPI", "TacticalRecommendationsAPI", "PersonaBuilderAPI"]
        all_imports.extend(classes)
        print(f"  OK: {len(classes)} classes")
    except Exception as e:
        failed.append(("recommendations", str(e)))
        print(f"  FAIL: {e}")

    # ============ Data Provider Module (3 classes) ============
    print("\n[13/30] Data Provider module...")
    try:
        from amazon_ads_api.data_provider import (
            DataProviderMetadataAPI, DataProviderRecordsAPI, HashedRecordsAPI
        )
        classes = ["DataProviderMetadataAPI", "DataProviderRecordsAPI", "HashedRecordsAPI"]
        all_imports.extend(classes)
        print(f"  OK: {len(classes)} classes")
    except Exception as e:
        failed.append(("data_provider", str(e)))
        print(f"  FAIL: {e}")

    # ============ Products Module (1 class) ============
    print("\n[14/30] Products module...")
    try:
        from amazon_ads_api.products import ProductSelectorAPI
        all_imports.append("ProductSelectorAPI")
        print("  OK: ProductSelectorAPI")
    except Exception as e:
        failed.append(("products", str(e)))
        print(f"  FAIL: {e}")

    # ============ Moderation Module (2 classes) ============
    print("\n[15/30] Moderation module...")
    try:
        from amazon_ads_api.moderation import PreModerationAPI, UnifiedModerationAPI
        classes = ["PreModerationAPI", "UnifiedModerationAPI"]
        all_imports.extend(classes)
        print(f"  OK: {len(classes)} classes")
    except Exception as e:
        failed.append(("moderation", str(e)))
        print(f"  FAIL: {e}")

    # ============ Stream Module (1 class) ============
    print("\n[16/30] Stream module...")
    try:
        from amazon_ads_api.stream import MarketingStreamAPI
        all_imports.append("MarketingStreamAPI")
        print("  OK: MarketingStreamAPI")
    except Exception as e:
        failed.append(("stream", str(e)))
        print(f"  FAIL: {e}")

    # ============ Locations Module (1 class) ============
    print("\n[17/30] Locations module...")
    try:
        from amazon_ads_api.locations import LocationsAPI
        all_imports.append("LocationsAPI")
        print("  OK: LocationsAPI")
    except Exception as e:
        failed.append(("locations", str(e)))
        print(f"  FAIL: {e}")

    # ============ Exports Module (1 class) ============
    print("\n[18/30] Exports module...")
    try:
        from amazon_ads_api.exports import ExportsAPI
        all_imports.append("ExportsAPI")
        print("  OK: ExportsAPI")
    except Exception as e:
        failed.append(("exports", str(e)))
        print(f"  FAIL: {e}")

    # ============ Media Planning Module (1 class) ============
    print("\n[19/30] Media Planning module...")
    try:
        from amazon_ads_api.media_planning import ReachForecastingAPI
        all_imports.append("ReachForecastingAPI")
        print("  OK: ReachForecastingAPI")
    except Exception as e:
        failed.append(("media_planning", str(e)))
        print(f"  FAIL: {e}")

    # ============ AMC Module (3 classes) ============
    print("\n[20/30] AMC module...")
    try:
        from amazon_ads_api.amc import AMCQueriesAPI, AMCAudiencesAPI, AMCWorkflowsAPI
        classes = ["AMCQueriesAPI", "AMCAudiencesAPI", "AMCWorkflowsAPI"]
        all_imports.extend(classes)
        print(f"  OK: {len(classes)} classes")
    except Exception as e:
        failed.append(("amc", str(e)))
        print(f"  FAIL: {e}")

    # ============ Sponsored TV Module (5 classes) ============
    print("\n[21/30] Sponsored TV module...")
    try:
        from amazon_ads_api.sponsored_tv import (
            SponsoredTVCampaignsAPI, SponsoredTVAdGroupsAPI, SponsoredTVAdsAPI,
            SponsoredTVCreativesAPI, SponsoredTVTargetingAPI
        )
        classes = ["SponsoredTVCampaignsAPI", "SponsoredTVAdGroupsAPI", "SponsoredTVAdsAPI",
                   "SponsoredTVCreativesAPI", "SponsoredTVTargetingAPI"]
        all_imports.extend(classes)
        print(f"  OK: {len(classes)} classes")
    except Exception as e:
        failed.append(("sponsored_tv", str(e)))
        print(f"  FAIL: {e}")

    # ============ Retail Ad Service Module (4 classes) ============
    print("\n[22/30] Retail Ad Service module...")
    try:
        from amazon_ads_api.retail_ad_service import (
            RASCampaignsAPI, RASAdGroupsAPI, RASProductAdsAPI, RASTargetsAPI
        )
        classes = ["RASCampaignsAPI", "RASAdGroupsAPI", "RASProductAdsAPI", "RASTargetsAPI"]
        all_imports.extend(classes)
        print(f"  OK: {len(classes)} classes")
    except Exception as e:
        failed.append(("retail_ad_service", str(e)))
        print(f"  FAIL: {e}")

    # ============ Manager Accounts Module (1 class) ============
    print("\n[23/30] Manager Accounts module...")
    try:
        from amazon_ads_api.manager_accounts import ManagerAccountsAPI
        all_imports.append("ManagerAccountsAPI")
        print("  OK: ManagerAccountsAPI")
    except Exception as e:
        failed.append(("manager_accounts", str(e)))
        print(f"  FAIL: {e}")

    # ============ Posts Module (1 class) ============
    print("\n[24/30] Posts module...")
    try:
        from amazon_ads_api.posts import PostsAPI
        all_imports.append("PostsAPI")
        print("  OK: PostsAPI")
    except Exception as e:
        failed.append(("posts", str(e)))
        print(f"  FAIL: {e}")

    # ============ Product Metadata Module (1 class) ============
    print("\n[25/30] Product Metadata module...")
    try:
        from amazon_ads_api.product_metadata import ProductMetadataAPI
        all_imports.append("ProductMetadataAPI")
        print("  OK: ProductMetadataAPI")
    except Exception as e:
        failed.append(("product_metadata", str(e)))
        print(f"  FAIL: {e}")

    # ============ Audiences Discovery Module (1 class) ============
    print("\n[26/30] Audiences Discovery module...")
    try:
        from amazon_ads_api.audiences_discovery import AudiencesDiscoveryAPI
        all_imports.append("AudiencesDiscoveryAPI")
        print("  OK: AudiencesDiscoveryAPI")
    except Exception as e:
        failed.append(("audiences_discovery", str(e)))
        print(f"  FAIL: {e}")

    # ============ Amazon Ads V1 Module (15 classes) ============
    print("\n[27/30] Amazon Ads V1 module...")
    try:
        from amazon_ads_api.amazon_ads_v1 import (
            AmazonAdsV1API, AdAssociationsAPI, AdGroupsAPI, AdsAPI, CampaignsAPI,
            TargetsAPI, RecommendationsAPI, AdvertisingDealsAPI, AdvertisingDealTargetsAPI,
            BrandedKeywordsPricingsAPI, CampaignForecastsAPI, CommitmentsAPI,
            CommitmentSpendsAPI, KeywordReservationValidationsAPI, RecommendationTypesAPI
        )
        classes = ["AmazonAdsV1API", "AdAssociationsAPI", "AdGroupsAPI", "AdsAPI", "CampaignsAPI",
                   "TargetsAPI", "RecommendationsAPI", "AdvertisingDealsAPI", "AdvertisingDealTargetsAPI",
                   "BrandedKeywordsPricingsAPI", "CampaignForecastsAPI", "CommitmentsAPI",
                   "CommitmentSpendsAPI", "KeywordReservationValidationsAPI", "RecommendationTypesAPI"]
        all_imports.extend(classes)
        print(f"  OK: {len(classes)} classes")
    except Exception as e:
        failed.append(("amazon_ads_v1", str(e)))
        print(f"  FAIL: {e}")

    # ============ Ad Library Module (3 classes) ============
    print("\n[28/30] Ad Library module...")
    try:
        from amazon_ads_api.ad_library import AdLibraryAPI, AdType, NameMatchType
        classes = ["AdLibraryAPI", "AdType", "NameMatchType"]
        all_imports.extend(classes)
        print(f"  OK: {len(classes)} classes")
    except Exception as e:
        failed.append(("ad_library", str(e)))
        print(f"  FAIL: {e}")

    # ============ Brand Home Module (1 class) ============
    print("\n[29/30] Brand Home module...")
    try:
        from amazon_ads_api.brand_home import BrandHomeAPI
        all_imports.append("BrandHomeAPI")
        print("  OK: BrandHomeAPI")
    except Exception as e:
        failed.append(("brand_home", str(e)))
        print(f"  FAIL: {e}")

    # ============ Other Modules ============
    print("\n[30/30] Other modules (Localization, Ads Data Manager, Brand Associations)...")
    try:
        from amazon_ads_api.localization import LocalizationAPI
        from amazon_ads_api.ads_data_manager import AdsDataManagerAPI
        from amazon_ads_api.brand_associations import BrandAssociationsAPI
        classes = ["LocalizationAPI", "AdsDataManagerAPI", "BrandAssociationsAPI"]
        all_imports.extend(classes)
        print(f"  OK: {len(classes)} classes")
    except Exception as e:
        failed.append(("other", str(e)))
        print(f"  FAIL: {e}")

    # ============ Summary ============
    print("\n" + "=" * 60)
    print(f"TOTAL CLASSES IMPORTED: {len(all_imports)}")
    print("=" * 60)
    
    if failed:
        print(f"\nFAILED IMPORTS ({len(failed)}):")
        for module, error in failed:
            print(f"  - {module}: {error}")
        return 1
    else:
        print("\nALL IMPORTS SUCCESSFUL!")
        return 0


def test_client_modules():
    """Test that client exposes all modules"""
    print("\n" + "=" * 60)
    print("Testing AmazonAdsClient module access...")
    print("=" * 60)
    
    from amazon_ads_api import AmazonAdsClient, AdsRegion
    
    client = AmazonAdsClient(
        client_id="test",
        client_secret="test",
        refresh_token="test",
        region=AdsRegion.NA,
    )
    
    modules = [
        ("sp", ["campaigns", "ad_groups", "keywords", "targeting", "budget_rules", 
                "recommendations", "product_eligibility", "theme_targeting"]),
        ("sb", ["campaigns", "ads", "keywords", "creatives", "brand_video", "moderation"]),
        ("sd", ["campaigns", "targeting", "creatives", "audiences", "moderation"]),
        ("dsp", ["audiences", "advertisers", "orders", "line_items", "creatives",
                 "inventory", "measurement", "conversions", "target_kpi"]),
        ("reporting", ["reports", "brand_metrics", "stores_analytics", "mmm"]),
        ("accounts", ["profiles", "portfolios", "billing", "budgets", "test_accounts"]),
        ("common", ["attribution", "stores", "assets", "history"]),
        ("insights", ["category", "keywords", "audience"]),
        ("recommendations", ["partner", "tactical", "persona"]),
        ("data_provider", ["metadata", "records", "hashed"]),
        ("moderation", ["pre", "unified"]),
        ("amc", ["queries", "audiences", "workflows"]),
        ("st", ["campaigns", "ad_groups", "ads", "creatives", "targeting"]),
        ("ras", ["campaigns", "ad_groups", "product_ads", "targets"]),
        ("media_planning", ["reach"]),
        ("stream", ["subscriptions"]),
    ]
    
    all_ok = True
    total_submodules = 0
    
    for module_name, submodules in modules:
        module = getattr(client, module_name, None)
        if module is None:
            print(f"  FAIL: client.{module_name} not found")
            all_ok = False
            continue
            
        for sub in submodules:
            total_submodules += 1
            if hasattr(module, sub):
                print(f"  OK: client.{module_name}.{sub}")
            else:
                print(f"  FAIL: client.{module_name}.{sub} not found")
                all_ok = False
    
    # Direct module access
    direct_modules = [
        "eligibility", "locations", "exports", "manager_accounts",
        "posts", "product_metadata", "audiences_discovery", "ads_v1",
        "ad_library", "brand_home", "localization", "ads_data_manager",
        "brand_associations"
    ]
    
    for mod in direct_modules:
        total_submodules += 1
        if hasattr(client, mod):
            print(f"  OK: client.{mod}")
        else:
            print(f"  FAIL: client.{mod} not found")
            all_ok = False
    
    print(f"\nTotal submodules tested: {total_submodules}")
    return 0 if all_ok else 1


def main():
    print("=" * 60)
    print("Amazon Ads API Python SDK - COMPLETE Test Suite")
    print("=" * 60)
    
    result1 = test_all_imports()
    result2 = test_client_modules()
    
    print("\n" + "=" * 60)
    if result1 == 0 and result2 == 0:
        print("ALL TESTS PASSED!")
    else:
        print("SOME TESTS FAILED!")
    print("=" * 60)
    
    return result1 or result2


if __name__ == "__main__":
    sys.exit(main())
