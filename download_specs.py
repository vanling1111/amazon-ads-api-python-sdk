"""
Download all Amazon Ads OpenAPI specification files.

Uses only stdlib (urllib) so no external dependencies are needed.
Last verified: 2026-04-10 — 79 spec files from 3 CDN domains.
"""
import urllib.request
import ssl
import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest"
BASE2 = "https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us"
BASE3 = "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest"

# URL -> local filename (for non-standard naming)
SPEC_MAP: dict[str, str] = {
    # ── Account & Profile Management ──
    f"{BASE}/AccountManagement_prod_3p.json": None,
    f"{BASE}/Advertisers_prod_3p.json": None,
    f"{BASE}/AdvertisingAccounts_prod_3p.json": None,
    f"{BASE}/AdvertisingTestAccount_prod_3p.json": None,
    f"{BASE}/ManagerAccount_prod_3p.json": None,
    f"{BASE}/Profiles_prod_3p.json": None,
    f"{BASE3}/AdvertisingInvitations_prod_3p.json": None,
    f"{BASE}/AdvertisingUserPermissionsManagement_prod_3p.json": None,

    # ── AMC (Amazon Marketing Cloud) ──
    f"{BASE}/AMCAdministration_prod_3p.json": None,
    f"{BASE}/AMCCustomModels_prod_3p.json": None,
    f"{BASE}/WorkflowManagementService_prod_3p.json": None,  # AMC Reporting
    f"{BASE}/Rule-BasedAudiences_prod_3p.json": None,  # AMC RBA
    f"{BASE}/Advertiseraudiences_prod_3p.json": None,  # AMC Advertiser Audiences
    f"{BASE}/AdvertiserDataUpload_prod_3p.json": None,  # AMC Data Upload

    # ── Unified API & Campaign Management ──
    f"{BASE}/AmazonAdsAPIALLMerged_prod_3p.json": None,  # Amazon Ads API v1
    f"{BASE}/CampaignManagement_prod_3p.json": None,

    # ── Sponsored Products / Brands / Display / TV ──
    f"{BASE}/SponsoredProducts_prod_3p.json": None,
    f"{BASE}/SponsoredBrands_prod_3p.json": None,
    f"{BASE}/SponsoredBrandsCategoryBenchmark_prod_3p.json": None,
    f"{BASE}/SponsoredDisplay_prod_3p.json": None,
    f"{BASE}/SponsoredTV_prod_3p.json": None,
    f"{BASE2}/sponsored-brands/4-0/openapi.json": "SponsoredBrands_v4_openapi.json",
    f"{BASE2}/sponsored-brands/3-0/openapi.yaml": "SponsoredBrands_v3_openapi.yaml",
    f"{BASE2}/sponsored-display/3-0/openapi.yaml": "SponsoredDisplay_v3_openapi.yaml",

    # ── DSP ──
    f"{BASE}/DSPCampaignManagement_prod_3p.json": None,
    f"{BASE}/DSPGuidance_prod_3p.json": None,
    f"{BASE}/DSPQuickActions_prod_3p.json": None,
    f"{BASE}/DSPReports_prod_3p.json": None,
    f"{BASE}/Measurement_prod_3p.json": None,  # DSP Measurement
    f"{BASE}/BidModifiers_prod_3p.json": None,  # DSP Bid Modifiers
    f"{BASE}/CombinedAudienceAPI_prod_3p.json": None,  # DSP Combined Audiences
    f"{BASE}/ConversionsAPI_prod_3p.json": None,  # DSP Conversions
    f"{BASE}/D16GDspApiActionableInsights_prod_3p.json": None,  # DSP Frequency Savings Insight
    f"{BASE}/D16GFMApiFrequencyGroupV1_prod_3p.json": None,  # DSP Frequency Groups
    f"{BASE}/D16GFMApiFrequencyGroupAssociationV1_prod_3p.json": None,  # DSP Frequency Group Associations
    f"{BASE}/D16GDspApiCampaignInsightsV1_prod_3p.json": None,  # DSP Performance+ Insights
    f"{BASE2}/dsp/3-0/advertiser.yaml": "DSP_Advertiser_v3_openapi.yaml",
    f"{BASE2}/dsp/2-2/reports_previous.yaml": "DSP_Reports_v2_openapi.yaml",

    # ── Retail Ad Service ──
    f"{BASE}/AmazonAdvertiserAPIforRetailAdService_prod_3p.json": None,
    f"{BASE}/RetailerIdentityAPIforRetailAdService_prod_3p.json": None,

    # ── Targeting & Eligibility ──
    f"{BASE}/AdGroupTargeting-ProductCategory_prod_3p.json": None,
    f"{BASE}/Discovery-AdvertisedProductCategories-V1_prod_3p.json": None,
    f"{BASE}/Eligibility_prod_3p.json": None,
    f"{BASE}/ProductSelector_prod_3p.json": None,
    f"{BASE}/TargetableEntities_prod_3p.json": None,

    # ── Audiences & Recommendations ──
    f"{BASE}/Audiences_prod_3p.json": None,
    f"{BASE}/Recommendations_prod_3p.json": None,

    # ── Billing & Reporting ──
    f"{BASE}/AdvertisingBilling_prod_3p.json": None,
    f"{BASE}/Billing_prod_3p.json": None,
    f"{BASE}/OfflineReport_prod_3p.json": None,  # V3 Reporting
    # Reporting_prod_3p.json: empty stub (0 paths, 0 schemas), removed from specs/

    # ── Brand & Creative ──
    f"{BASE}/BrandAidV2_prod_3p.json": None,  # Brand Associations
    f"{BASE}/BrandBenchmarks_prod_3p.json": None,
    f"{BASE}/BrandHome_prod_3p.json": None,
    f"{BASE}/BrandMetrics_prod_3p.json": None,
    f"{BASE}/Moderation_prod_3p.json": None,
    f"{BASE}/PreModeration_prod_3p.json": None,
    f"{BASE2}/creative-asset-library/creative-asset-library-openapi.yaml": "CreativeAssetLibrary_openapi.yaml",

    # ── Exports & Streams ──
    f"{BASE}/AmazonAdsAPIExports_prod_3p.json": None,
    f"{BASE}/AmazonMarketingStream_prod_3p.json": None,

    # ── Insights, Analytics & Attribution ──
    f"{BASE}/AmazonAttribution_prod_3p.json": None,
    f"{BASE}/Insights_prod_3p.json": None,
    f"{BASE}/MarketingMixModeling_prod_3p.json": None,
    f"{BASE}/Diagnostics_prod_3p.json": None,  # Campaign Diagnostics
    f"{BASE}/MediaInsightsHub_prod_3p.json": None,  # Historic Reach
    f"{BASE}/ReachPlanningService_prod_3p.json": None,  # Reach & Performance Forecasting
    f"{BASE}/PersonaBuilderAPI_prod_3p.json": None,

    # ── Data & Content ──
    f"{BASE}/AdLibraryAPI_prod_3p.json": None,
    f"{BASE}/AdsDataManager_prod_3p.json": None,
    f"{BASE}/DataProvider_prod_3p.json": None,
    f"{BASE}/HashedRecords_prod_3p.json": None,
    f"{BASE}/Localization_prod_3p.json": None,
    f"{BASE}/Locations_prod_3p.json": None,
    f"{BASE}/PartnerOpportunities_prod_3p.json": None,
    f"{BASE}/Posts_prod_3p.json": None,
    f"{BASE}/ValidationConfigurationsAPI_prod_3p.json": None,
    f"{BASE}/Changehistory_prod_3p.json": None,

    # ── Stores & Portfolios ──
    f"{BASE}/Portfolios_prod_3p.json": None,
    f"{BASE}/Stores_prod_3p.json": None,
}

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE


def download_spec(url: str, local_name: str | None, output_dir: Path) -> tuple[str, bool, str]:
    filename = local_name or url.rsplit("/", 1)[-1]
    output_path = output_dir / filename
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=30) as resp:
            data = resp.read()
            output_path.write_bytes(data)
        return filename, True, f"{len(data)} bytes"
    except Exception as e:
        return filename, False, str(e)


def main():
    output_dir = Path("specs")
    output_dir.mkdir(exist_ok=True)

    success = fail = 0
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {
            pool.submit(download_spec, url, local_name, output_dir): url
            for url, local_name in SPEC_MAP.items()
        }
        for future in as_completed(futures):
            filename, ok, info = future.result()
            if ok:
                print(f"[OK]   {filename} ({info})")
                success += 1
            else:
                print(f"[FAIL] {filename} - {info}")
                fail += 1

    total = len(list(output_dir.glob("*")))
    print(f"\nDone: {success} succeeded, {fail} failed, {total} total files in {output_dir}/")


if __name__ == "__main__":
    main()
