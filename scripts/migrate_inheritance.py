"""
Migrate hand-written API files to inherit from generated clients.

For each file that currently inherits BaseAdsClient, changes it to inherit
from the appropriate generated client class with a fallback to BaseAdsClient
if the generated code is not available.
"""

import ast
import os
import re
import sys

SDK_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API_DIR = os.path.join(SDK_ROOT, "amazon_ads_api")

# Mapping: hand-written file path (relative to amazon_ads_api/) -> (clients_module, ClassName)
FILE_TO_CLIENT = {
    # ── SP ──
    "core/sp/campaigns.py": ("clients_sp", "SpClient"),
    "core/sp/ad_groups.py": ("clients_sp", "SpClient"),
    "core/sp/budget_rules.py": ("clients_sp", "SpClient"),
    "core/sp/campaign_optimization.py": ("clients_sp", "SpClient"),
    "core/sp/global_recommendations.py": ("clients_sp", "SpClient"),
    "core/sp/keywords.py": ("clients_sp", "SpClient"),
    "core/sp/product_ads.py": ("clients_sp", "SpClient"),
    "core/sp/recommendations.py": ("clients_sp", "SpClient"),
    "core/sp/target_promotion_groups.py": ("clients_sp", "SpClient"),
    "core/sp/targeting.py": ("clients_sp", "SpClient"),
    "core/sp/theme_targeting.py": ("clients_sp", "SpClient"),
    # ── SB ──
    "core/sb/ads.py": ("clients_sb", "SbClient"),
    "core/sb/brand_video.py": ("clients_sb", "SbClient"),
    "core/sb/campaigns.py": ("clients_sb", "SbClient"),
    "core/sb/creatives.py": ("clients_sb", "SbClient"),
    "core/sb/forecasts.py": ("clients_sb", "SbClient"),
    "core/sb/keywords.py": ("clients_sb", "SbClient"),
    "core/sb/legacy_migration.py": ("clients_sb", "SbClient"),
    "core/sb/media.py": ("clients_sb", "SbClient"),
    "core/sb/moderation.py": ("clients_sb", "SbClient"),
    "core/sb/optimization.py": ("clients_sb", "SbClient"),
    "core/sb/reports_v2.py": ("clients_sb", "SbClient"),
    "core/sb/stores.py": ("clients_sb", "SbClient"),
    "core/sb/targeting.py": ("clients_sb", "SbClient"),
    "core/sb/themes.py": ("clients_sb", "SbClient"),
    # ── SD ──
    "core/sd/audiences.py": ("clients_sd", "SdClient"),
    "core/sd/brand_safety.py": ("clients_sd", "SdClient"),
    "core/sd/campaigns.py": ("clients_sd", "SdClient"),
    "core/sd/creatives.py": ("clients_sd", "SdClient"),
    "core/sd/locations.py": ("clients_sd", "SdClient"),
    "core/sd/moderation.py": ("clients_sd", "SdClient"),
    "core/sd/optimization.py": ("clients_sd", "SdClient"),
    "core/sd/reports.py": ("clients_sd", "SdClient"),
    "core/sd/targeting.py": ("clients_sd", "SdClient"),
    # ── DSP ──
    "core/dsp/advertisers.py": ("clients_dsp_v3", "DspV3Client"),
    "core/dsp/audiences.py": ("clients_dsp_audiences", "DspAudiencesClient"),
    "core/dsp/campaigns.py": ("clients_dsp_campaigns", "DspCampaignsClient"),
    "core/dsp/conversions.py": ("clients_conversions", "ConversionsClient"),
    "core/dsp/measurement.py": ("clients_dsp_measurement", "DspMeasurementClient"),
    "core/dsp/target_kpi.py": ("clients_dsp_target_kpi", "DspTargetKpiClient"),
    # ── Accounts ──
    "core/accounts/advertising_accounts.py": ("clients_advertising_accounts", "AdvertisingAccountsClient"),
    "core/accounts/billing.py": ("clients_billing", "BillingClient"),
    "core/accounts/budgets.py": ("clients_billing", "BillingClient"),
    "core/accounts/portfolios.py": ("clients_portfolios", "PortfoliosClient"),
    "core/accounts/profiles.py": ("clients_profiles", "ProfilesClient"),
    "core/accounts/test_accounts.py": ("clients_test_accounts", "TestAccountsClient"),
    # ── Core other ──
    "core/audiences/audiences_discovery.py": ("clients_audiences", "AudiencesClient"),
    "core/eligibility/eligibility.py": ("clients_eligibility", "EligibilityClient"),
    "core/exports/exports.py": ("clients_exports", "ExportsClient"),
    "core/locations/locations.py": ("clients_locations", "LocationsClient"),
    "core/products/product_selector.py": ("clients_product_selector", "ProductSelectorClient"),
    # ── Experimental ──
    "experimental/sponsored_tv/ad_groups.py": ("clients_stv", "StvClient"),
    "experimental/sponsored_tv/ads.py": ("clients_stv", "StvClient"),
    "experimental/sponsored_tv/campaigns.py": ("clients_stv", "StvClient"),
    "experimental/sponsored_tv/creatives.py": ("clients_stv", "StvClient"),
    "experimental/sponsored_tv/targeting.py": ("clients_stv", "StvClient"),
    "experimental/ad_library/ad_library.py": ("clients_ad_library", "AdLibraryClient"),
    "experimental/brand_home/brand_home.py": ("clients_brand_home", "BrandHomeClient"),
    "experimental/localization/localization.py": ("clients_localization", "LocalizationClient"),
    "experimental/moderation/pre_moderation.py": ("clients_pre_moderation", "PreModerationClient"),
    "experimental/moderation/unified_moderation.py": ("clients_moderation", "ModerationClient"),
    "experimental/partner_opportunities/partner_opportunities.py": ("clients_partner_opportunities", "PartnerOpportunitiesClient"),
    "experimental/persona_builder/persona_builder.py": ("clients_persona_builder", "PersonaBuilderClient"),
    # ── Reference ──
    "reference/amc/administration.py": ("clients_amc_administration", "AmcAdministrationClient"),
    "reference/amc/audiences.py": ("clients_amc_advertiser_audiences", "AmcAdvertiserAudiencesClient"),
    "reference/amc/reporting.py": ("clients_amc_workflow", "AmcWorkflowClient"),
    "reference/data_provider/audience_metadata.py": ("clients_data_provider", "DataProviderClient"),
    "reference/data_provider/hashed_records.py": ("clients_hashed_records", "HashedRecordsClient"),
    "reference/posts/posts.py": ("clients_posts", "PostsClient"),
    "reference/retail_ad_service/ad_groups.py": ("clients_retail_ad_service", "RetailAdServiceClient"),
    "reference/retail_ad_service/campaigns.py": ("clients_retail_ad_service", "RetailAdServiceClient"),
    "reference/retail_ad_service/product_ads.py": ("clients_retail_ad_service", "RetailAdServiceClient"),
    "reference/retail_ad_service/targets.py": ("clients_retail_ad_service", "RetailAdServiceClient"),
    "reference/stream/subscriptions.py": ("clients_marketing_stream", "MarketingStreamClient"),
    "reference/unified_api/unified_api.py": None,  # Keep BaseAdsClient - unified API not generated
    # ── Services ──
    "services/ads_data_manager/ads_data_manager.py": ("clients_ads_data_manager", "AdsDataManagerClient"),
    "services/brand_associations/brand_associations.py": ("clients_brand_associations", "BrandAssociationsClient"),
    "services/common/assets.py": ("clients_creative_assets", "CreativeAssetsClient"),
    "services/common/attribution.py": ("clients_attribution", "AttributionClient"),
    "services/common/history.py": ("clients_change_history", "ChangeHistoryClient"),
    "services/common/stores.py": ("clients_stores", "StoresClient"),
    "services/insights/audience_insights.py": ("clients_insights", "InsightsClient"),
    "services/insights/keyword_insights.py": ("clients_insights", "InsightsClient"),
    "services/media_planning/reach_forecasting.py": ("clients_reach_planning", "ReachPlanningClient"),
    "services/recommendations/recommendations.py": ("clients_recommendations", "RecommendationsClient"),
    "services/reporting/brand_metrics.py": ("clients_brand_metrics", "BrandMetricsClient"),
    "services/reporting/mmm.py": ("clients_mmm", "MmmClient"),
    "services/reporting/reports_v3.py": ("clients_reporting", "ReportingClient"),
    "services/reporting/stores_analytics.py": ("clients_stores", "StoresClient"),
}


def migrate_file(rel_path: str, client_info: tuple[str, str] | None) -> str:
    """Migrate a single file. Returns status string."""
    abs_path = os.path.join(API_DIR, rel_path)
    if not os.path.exists(abs_path):
        return "SKIP (not found)"

    if client_info is None:
        return "SKIP (keep BaseAdsClient)"

    clients_module, client_class = client_info

    with open(abs_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "from amazon_ads_api.generated" in content:
        return "SKIP (already migrated)"

    old_import = "from amazon_ads_api.base import BaseAdsClient"
    if old_import not in content:
        old_import_alt = "from amazon_ads_api.base import BaseAdsClient,"
        if old_import_alt in content:
            old_import = old_import_alt
        else:
            return f"SKIP (no BaseAdsClient import found)"

    # Build new import block
    new_import_lines = []

    # Keep remaining base imports (JSONData, JSONList, etc.)
    import_match = re.search(r"from amazon_ads_api\.base import (.+?)$", content, re.MULTILINE)
    if import_match:
        imports_str = import_match.group(1)
        other_imports = [
            i.strip() for i in imports_str.split(",")
            if i.strip() and i.strip() != "BaseAdsClient"
        ]
        if other_imports:
            new_import_lines.append(f"from amazon_ads_api.base import {', '.join(other_imports)}")

    # Add the generated client import with fallback
    new_import_lines.append("")
    new_import_lines.append("try:")
    new_import_lines.append(f"    from amazon_ads_api.generated.clients.{clients_module} import {client_class} as _GenBase")
    new_import_lines.append("except ImportError:")
    new_import_lines.append("    from amazon_ads_api.base import BaseAdsClient as _GenBase  # type: ignore[assignment]")

    # Replace the old import line
    full_old_import_line = import_match.group(0) if import_match else old_import
    new_content = content.replace(full_old_import_line, "\n".join(new_import_lines))

    # Replace class inheritance: (BaseAdsClient) -> (_GenBase)
    new_content = re.sub(
        r"\(BaseAdsClient\)",
        "(_GenBase)",
        new_content,
    )

    if new_content == content:
        return "SKIP (no changes needed)"

    with open(abs_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    return "OK"


def main():
    migrated = 0
    skipped = 0
    errors = 0

    for rel_path, client_info in sorted(FILE_TO_CLIENT.items()):
        status = migrate_file(rel_path, client_info)
        prefix = "  " if status.startswith("OK") else "  "
        print(f"{prefix}[{status}] {rel_path}")
        if status == "OK":
            migrated += 1
        elif status.startswith("SKIP"):
            skipped += 1
        else:
            errors += 1

    print(f"\nMigrated: {migrated}, Skipped: {skipped}, Errors: {errors}")

    # Validate syntax of all migrated files
    print("\nValidating syntax...")
    syntax_errors = 0
    for rel_path in FILE_TO_CLIENT:
        abs_path = os.path.join(API_DIR, rel_path)
        if not os.path.exists(abs_path):
            continue
        with open(abs_path, "r") as f:
            code = f.read()
        try:
            ast.parse(code)
        except SyntaxError as e:
            print(f"  SYNTAX ERROR: {rel_path} line {e.lineno}: {e.msg}")
            syntax_errors += 1

    if syntax_errors == 0:
        print(f"  All {migrated + skipped} files pass syntax check")
    else:
        print(f"  {syntax_errors} syntax errors found!")


if __name__ == "__main__":
    main()
