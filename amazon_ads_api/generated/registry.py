"""Auto-generated client registry. Do not edit manually."""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from amazon_ads_api.client import AmazonAdsClient

_MODULE_CLIENTS: dict[str, tuple[str, str]] = {
    "account_management": ("amazon_ads_api.generated.clients.clients_account_management", "AccountManagementClient"),
    "ad_library": ("amazon_ads_api.generated.clients.clients_ad_library", "AdLibraryClient"),
    "ads_data_manager": ("amazon_ads_api.generated.clients.clients_ads_data_manager", "AdsDataManagerClient"),
    "advertisers": ("amazon_ads_api.generated.clients.clients_advertisers", "AdvertisersClient"),
    "advertising_accounts": ("amazon_ads_api.generated.clients.clients_advertising_accounts", "AdvertisingAccountsClient"),
    "amc_administration": ("amazon_ads_api.generated.clients.clients_amc_administration", "AmcAdministrationClient"),
    "amc_advertiser_audiences": ("amazon_ads_api.generated.clients.clients_amc_advertiser_audiences", "AmcAdvertiserAudiencesClient"),
    "amc_custom_models": ("amazon_ads_api.generated.clients.clients_amc_custom_models", "AmcCustomModelsClient"),
    "amc_data_upload": ("amazon_ads_api.generated.clients.clients_amc_data_upload", "AmcDataUploadClient"),
    "amc_rule_based_audiences": ("amazon_ads_api.generated.clients.clients_amc_rule_based_audiences", "AmcRuleBasedAudiencesClient"),
    "amc_workflow": ("amazon_ads_api.generated.clients.clients_amc_workflow", "AmcWorkflowClient"),
    "attribution": ("amazon_ads_api.generated.clients.clients_attribution", "AttributionClient"),
    "audiences": ("amazon_ads_api.generated.clients.clients_audiences", "AudiencesClient"),
    "billing": ("amazon_ads_api.generated.clients.clients_billing", "BillingClient"),
    "brand_associations": ("amazon_ads_api.generated.clients.clients_brand_associations", "BrandAssociationsClient"),
    "brand_benchmarks": ("amazon_ads_api.generated.clients.clients_brand_benchmarks", "BrandBenchmarksClient"),
    "brand_home": ("amazon_ads_api.generated.clients.clients_brand_home", "BrandHomeClient"),
    "brand_metrics": ("amazon_ads_api.generated.clients.clients_brand_metrics", "BrandMetricsClient"),
    "campaign_management": ("amazon_ads_api.generated.clients.clients_campaign_management", "CampaignManagementClient"),
    "change_history": ("amazon_ads_api.generated.clients.clients_change_history", "ChangeHistoryClient"),
    "conversions": ("amazon_ads_api.generated.clients.clients_conversions", "ConversionsClient"),
    "creative_assets": ("amazon_ads_api.generated.clients.clients_creative_assets", "CreativeAssetsClient"),
    "data_provider": ("amazon_ads_api.generated.clients.clients_data_provider", "DataProviderClient"),
    "data_provider_v2": ("amazon_ads_api.generated.clients.clients_data_provider_v2", "DataProviderV2Client"),
    "diagnostics": ("amazon_ads_api.generated.clients.clients_diagnostics", "DiagnosticsClient"),
    "discovery_categories": ("amazon_ads_api.generated.clients.clients_discovery_categories", "DiscoveryCategoriesClient"),
    "dsp_actionable_insights": ("amazon_ads_api.generated.clients.clients_dsp_actionable_insights", "DspActionableInsightsClient"),
    "dsp_audiences": ("amazon_ads_api.generated.clients.clients_dsp_audiences", "DspAudiencesClient"),
    "dsp_bid_modifiers": ("amazon_ads_api.generated.clients.clients_dsp_bid_modifiers", "DspBidModifiersClient"),
    "dsp_campaign_insights": ("amazon_ads_api.generated.clients.clients_dsp_campaign_insights", "DspCampaignInsightsClient"),
    "dsp_campaigns": ("amazon_ads_api.generated.clients.clients_dsp_campaigns", "DspCampaignsClient"),
    "dsp_combined_audiences": ("amazon_ads_api.generated.clients.clients_dsp_combined_audiences", "DspCombinedAudiencesClient"),
    "dsp_frequency_associations": ("amazon_ads_api.generated.clients.clients_dsp_frequency_associations", "DspFrequencyAssociationsClient"),
    "dsp_frequency_groups": ("amazon_ads_api.generated.clients.clients_dsp_frequency_groups", "DspFrequencyGroupsClient"),
    "dsp_guidance": ("amazon_ads_api.generated.clients.clients_dsp_guidance", "DspGuidanceClient"),
    "dsp_measurement": ("amazon_ads_api.generated.clients.clients_dsp_measurement", "DspMeasurementClient"),
    "dsp_product_category": ("amazon_ads_api.generated.clients.clients_dsp_product_category", "DspProductCategoryClient"),
    "dsp_quick_actions": ("amazon_ads_api.generated.clients.clients_dsp_quick_actions", "DspQuickActionsClient"),
    "dsp_reports": ("amazon_ads_api.generated.clients.clients_dsp_reports", "DspReportsClient"),
    "dsp_reports_v2": ("amazon_ads_api.generated.clients.clients_dsp_reports_v2", "DspReportsV2Client"),
    "dsp_target_kpi": ("amazon_ads_api.generated.clients.clients_dsp_target_kpi", "DspTargetKpiClient"),
    "dsp_v3": ("amazon_ads_api.generated.clients.clients_dsp_v3", "DspV3Client"),
    "eligibility": ("amazon_ads_api.generated.clients.clients_eligibility", "EligibilityClient"),
    "exports": ("amazon_ads_api.generated.clients.clients_exports", "ExportsClient"),
    "hashed_records": ("amazon_ads_api.generated.clients.clients_hashed_records", "HashedRecordsClient"),
    "insights": ("amazon_ads_api.generated.clients.clients_insights", "InsightsClient"),
    "invitations": ("amazon_ads_api.generated.clients.clients_invitations", "InvitationsClient"),
    "localization": ("amazon_ads_api.generated.clients.clients_localization", "LocalizationClient"),
    "locations": ("amazon_ads_api.generated.clients.clients_locations", "LocationsClient"),
    "manager_accounts": ("amazon_ads_api.generated.clients.clients_manager_accounts", "ManagerAccountsClient"),
    "marketing_stream": ("amazon_ads_api.generated.clients.clients_marketing_stream", "MarketingStreamClient"),
    "media_insights": ("amazon_ads_api.generated.clients.clients_media_insights", "MediaInsightsClient"),
    "mmm": ("amazon_ads_api.generated.clients.clients_mmm", "MmmClient"),
    "moderation": ("amazon_ads_api.generated.clients.clients_moderation", "ModerationClient"),
    "partner_opportunities": ("amazon_ads_api.generated.clients.clients_partner_opportunities", "PartnerOpportunitiesClient"),
    "persona_builder": ("amazon_ads_api.generated.clients.clients_persona_builder", "PersonaBuilderClient"),
    "portfolios": ("amazon_ads_api.generated.clients.clients_portfolios", "PortfoliosClient"),
    "posts": ("amazon_ads_api.generated.clients.clients_posts", "PostsClient"),
    "pre_moderation": ("amazon_ads_api.generated.clients.clients_pre_moderation", "PreModerationClient"),
    "product_selector": ("amazon_ads_api.generated.clients.clients_product_selector", "ProductSelectorClient"),
    "profiles": ("amazon_ads_api.generated.clients.clients_profiles", "ProfilesClient"),
    "profiles_v3": ("amazon_ads_api.generated.clients.clients_profiles_v3", "ProfilesV3Client"),
    "reach_planning": ("amazon_ads_api.generated.clients.clients_reach_planning", "ReachPlanningClient"),
    "recommendations": ("amazon_ads_api.generated.clients.clients_recommendations", "RecommendationsClient"),
    "reporting": ("amazon_ads_api.generated.clients.clients_reporting", "ReportingClient"),
    "retail_ad_service": ("amazon_ads_api.generated.clients.clients_retail_ad_service", "RetailAdServiceClient"),
    "retail_identity": ("amazon_ads_api.generated.clients.clients_retail_identity", "RetailIdentityClient"),
    "sb": ("amazon_ads_api.generated.clients.clients_sb", "SbClient"),
    "sb_benchmarks": ("amazon_ads_api.generated.clients.clients_sb_benchmarks", "SbBenchmarksClient"),
    "sd": ("amazon_ads_api.generated.clients.clients_sd", "SdClient"),
    "sd_v3": ("amazon_ads_api.generated.clients.clients_sd_v3", "SdV3Client"),
    "sp": ("amazon_ads_api.generated.clients.clients_sp", "SpClient"),
    "stores": ("amazon_ads_api.generated.clients.clients_stores", "StoresClient"),
    "stv": ("amazon_ads_api.generated.clients.clients_stv", "StvClient"),
    "targetable_entities": ("amazon_ads_api.generated.clients.clients_targetable_entities", "TargetableEntitiesClient"),
    "test_accounts": ("amazon_ads_api.generated.clients.clients_test_accounts", "TestAccountsClient"),
    "unified_ga": ("amazon_ads_api.generated.clients.clients_unified_ga", "UnifiedGaClient"),
    "user_permissions": ("amazon_ads_api.generated.clients.clients_user_permissions", "UserPermissionsClient"),
}


class GeneratedAPIs:
    """Lazy access to every OpenAPI-generated client module.

    Example::

        await client.generated.marketing_stream.create_stream_subscription(body={...})
        await client.generated.sp.create_campaign(...)
    """

    def __init__(self, client: "AmazonAdsClient") -> None:
        self._client = client
        self._instances: dict[str, Any] = {}

    @staticmethod
    def module_names() -> tuple[str, ...]:
        return tuple(sorted(_MODULE_CLIENTS))

    def __getattr__(self, name: str) -> Any:
        if name.startswith("_"):
            raise AttributeError(name)
        if name not in _MODULE_CLIENTS:
            raise AttributeError(
                f"unknown generated module {name!r}; "
                f"available: {', '.join(self.module_names())}"
            )
        cached = self._instances.get(name)
        if cached is not None:
            return cached
        module_path, class_name = _MODULE_CLIENTS[name]
        module = importlib.import_module(module_path)
        cls = getattr(module, class_name)
        instance = self._client._create_client(cls)
        self._instances[name] = instance
        return instance

    def __dir__(self) -> list[str]:
        return sorted(set(super().__dir__()) | set(_MODULE_CLIENTS))


__all__ = ["GeneratedAPIs", "_MODULE_CLIENTS"]
