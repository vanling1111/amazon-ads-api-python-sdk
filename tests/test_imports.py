"""
Amazon Ads API Python SDK - Import Tests
"""
import sys


def test_basic_imports():
    """Test basic imports"""
    print("[1/8] Testing basic imports...")
    from amazon_ads_api import AmazonAdsClient, AdsRegion, AmazonAdsError, __version__
    assert __version__ == "1.0.0"
    assert AmazonAdsClient is not None
    assert AdsRegion is not None
    assert AmazonAdsError is not None
    print(f"  OK: Version {__version__}")
    print(f"  OK: AmazonAdsClient")
    print(f"  OK: AdsRegion: {list(AdsRegion)}")
    print(f"  OK: AmazonAdsError")


def test_sp_module():
    """Test SP module imports"""
    print("\n[2/8] Testing SP (Sponsored Products) module...")
    from amazon_ads_api.sp import (
        SPCampaignsAPI,
        SPAdGroupsAPI,
        SPKeywordsAPI,
        SPTargetingAPI,
        SPBudgetRulesAPI,
        SPRecommendationsAPI,
    )
    print("  OK: SPCampaignsAPI")
    print("  OK: SPAdGroupsAPI")
    print("  OK: SPKeywordsAPI")
    print("  OK: SPTargetingAPI")
    print("  OK: SPBudgetRulesAPI")
    print("  OK: SPRecommendationsAPI")


def test_sb_module():
    """Test SB module imports"""
    print("\n[3/8] Testing SB (Sponsored Brands) module...")
    from amazon_ads_api.sb import (
        SBCampaignsAPI,
        SBAdsAPI,
        SBKeywordsAPI,
        SBCreativesAPI,
    )
    print("  OK: SBCampaignsAPI")
    print("  OK: SBAdsAPI")
    print("  OK: SBKeywordsAPI")
    print("  OK: SBCreativesAPI")


def test_sd_module():
    """Test SD module imports"""
    print("\n[4/8] Testing SD (Sponsored Display) module...")
    from amazon_ads_api.sd import (
        SDCampaignsAPI,
        SDTargetingAPI,
        SDCreativesAPI,
    )
    print("  OK: SDCampaignsAPI")
    print("  OK: SDTargetingAPI")
    print("  OK: SDCreativesAPI")


def test_dsp_module():
    """Test DSP module imports"""
    print("\n[5/8] Testing DSP module...")
    from amazon_ads_api.dsp import DSPAudiencesAPI
    print("  OK: DSPAudiencesAPI")


def test_reporting_module():
    """Test Reporting module imports"""
    print("\n[6/8] Testing Reporting module...")
    from amazon_ads_api.reporting import ReportsV3API, BrandMetricsAPI
    print("  OK: ReportsV3API")
    print("  OK: BrandMetricsAPI")


def test_accounts_module():
    """Test Accounts module imports"""
    print("\n[7/8] Testing Accounts module...")
    from amazon_ads_api.accounts import ProfilesAPI, PortfoliosAPI, BillingAPI
    print("  OK: ProfilesAPI")
    print("  OK: PortfoliosAPI")
    print("  OK: BillingAPI")


def test_client_instantiation():
    """Test client instantiation"""
    print("\n[8/8] Testing client instantiation...")
    from amazon_ads_api import AmazonAdsClient, AdsRegion

    client = AmazonAdsClient(
        client_id="test_client_id",
        client_secret="test_client_secret",
        refresh_token="test_refresh_token",
        region=AdsRegion.NA,
    )

    # Test lazy loading of modules
    assert client.sp is not None
    assert client.sb is not None
    assert client.sd is not None
    assert client.dsp is not None
    assert client.reporting is not None
    assert client.accounts is not None
    assert client.common is not None
    assert client.insights is not None
    assert client.amc is not None

    print("  OK: Client instantiation")
    print("  OK: client.sp")
    print("  OK: client.sb")
    print("  OK: client.sd")
    print("  OK: client.dsp")
    print("  OK: client.reporting")
    print("  OK: client.accounts")
    print("  OK: client.common")
    print("  OK: client.insights")
    print("  OK: client.amc")


def main():
    print("=" * 60)
    print("Amazon Ads API Python SDK - Full Test Suite")
    print("=" * 60)

    try:
        test_basic_imports()
        test_sp_module()
        test_sb_module()
        test_sd_module()
        test_dsp_module()
        test_reporting_module()
        test_accounts_module()
        test_client_instantiation()

        print("\n" + "=" * 60)
        print("ALL TESTS PASSED!")
        print("=" * 60)
        return 0
    except Exception as e:
        print(f"\nTEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())

