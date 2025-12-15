"""
Download all Amazon Ads OpenAPI specification files
"""
import httpx
import asyncio
from pathlib import Path

# All 59 official OpenAPI spec files
SPEC_URLS = [
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/ADSP_Audiences.json",
    "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AMCAdministration_prod_3p.json",
    "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AMCAudiences_prod_3p.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/AMCReporting_prod_3p.json",
    "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AdLibraryAPI_prod_3p.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Advertisers.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/AdvertisingAccounts.json",
    "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AdvertisingBilling_prod_3p.json",
    "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p.json",
    "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIExports_prod_3p.json",
    "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonMarketingStream_prod_3p.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Attribution.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Audiences.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Billing.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/BrandHome_prod_3p.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/BrandMetrics.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/ChangeHistory.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/CreativeAssetLibrary.yaml",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/CreativeAssetLibrary_openapi.yaml",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/CreativeAssets.yaml",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/DSP_AdGroupCampaign.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/DSP_Advertiser_v3.yaml",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/DSP_Audiences.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/DSP_Conversions.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/DSP_Measurement.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/DSP_TargetKPI.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/DSP_v3.yaml",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/DataProvider.yaml",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Eligibility.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Exports.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/GoalSeekingBidder.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/HashedRecords.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Insights.json",
    "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Insights_prod_3p.json",
    "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Localization_prod_3p.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Locations.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/MMM.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/ManagerAccount.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/MarketingStream.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Moderation.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/OfflineReport.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/PartnerOpportunities.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/PersonaBuilder.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Portfolios.json",
    "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Posts_prod_3p.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/PreModeration.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/ProductSelector.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Profiles_v3.yaml",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/ReachForecasting.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Recommendations.json",
    "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Recommendations_prod_3p.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/SponsoredBrands_v3.yaml",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/SponsoredBrands_v4.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/SponsoredDisplay_v3.yaml",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/SponsoredProducts.json",
    "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json",
    "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredTV_prod_3p.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Stores.json",
    "https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/TestAccounts.json",
]

async def download_spec(client: httpx.AsyncClient, url: str, output_dir: Path):
    """Download a single spec file"""
    filename = url.split("/")[-1]
    output_path = output_dir / filename
    
    try:
        response = await client.get(url)
        response.raise_for_status()
        output_path.write_text(response.text, encoding="utf-8")
        print(f"[OK] Downloaded: {filename}")
    except Exception as e:
        print(f"[FAIL] Failed: {filename} - {e}")

async def main():
    """Download all spec files"""
    output_dir = Path("specs")
    output_dir.mkdir(exist_ok=True)
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        tasks = [download_spec(client, url, output_dir) for url in SPEC_URLS]
        await asyncio.gather(*tasks)
    
    print(f"\n[SUCCESS] Downloaded {len(list(output_dir.glob('*')))} spec files to {output_dir}/")

if __name__ == "__main__":
    asyncio.run(main())

