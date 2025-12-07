# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-07

### Added

- Initial release with 100% Amazon Ads API coverage
- **101 API classes** across 30 modules
- SP (Sponsored Products) module - 8 classes
  - SPCampaignsAPI, SPAdGroupsAPI, SPKeywordsAPI, SPTargetingAPI
  - SPBudgetRulesAPI, SPRecommendationsAPI, SPProductEligibilityAPI, SPThemeTargetingAPI
- SB (Sponsored Brands) module - 6 classes
  - SBCampaignsAPI, SBAdsAPI, SBKeywordsAPI, SBCreativesAPI, SBBrandVideoAPI, SBModerationAPI
- SD (Sponsored Display) module - 5 classes
  - SDCampaignsAPI, SDTargetingAPI, SDCreativesAPI, SDAudiencesAPI, SDModerationAPI
- DSP module - 9 classes
  - DSPAudiencesAPI, DSPAdvertisersAPI, DSPOrdersAPI, DSPLineItemsAPI
  - DSPCreativesAPI, DSPInventoryAPI, DSPMeasurementAPI, DSPConversionsAPI, DSPTargetKPIAPI
- Reporting module - 4 classes
  - ReportsV3API, BrandMetricsAPI, StoresAnalyticsAPI, MarketingMixModelingAPI
- Accounts module - 5 classes
  - ProfilesAPI, PortfoliosAPI, BillingAPI, AccountBudgetsAPI, TestAccountsAPI
- Common module - 4 classes
  - AttributionAPI, StoresAPI, AssetsAPI, HistoryAPI
- Insights module - 3 classes
  - CategoryInsightsAPI, KeywordInsightsAPI, AudienceInsightsAPI
- Recommendations module - 3 classes
  - PartnerOpportunitiesAPI, TacticalRecommendationsAPI, PersonaBuilderAPI
- Data Provider module - 3 classes
  - DataProviderMetadataAPI, DataProviderRecordsAPI, HashedRecordsAPI
- Moderation module - 2 classes
  - PreModerationAPI, UnifiedModerationAPI
- AMC module - 3 classes
  - AMCQueriesAPI, AMCAudiencesAPI, AMCWorkflowsAPI
- Sponsored TV module - 5 classes
  - SponsoredTVCampaignsAPI, SponsoredTVAdGroupsAPI, SponsoredTVAdsAPI
  - SponsoredTVCreativesAPI, SponsoredTVTargetingAPI
- Retail Ad Service module - 4 classes
  - RASCampaignsAPI, RASAdGroupsAPI, RASProductAdsAPI, RASTargetsAPI
- Amazon Ads V1 module (New Unified API) - 15 classes
  - AmazonAdsV1API, AdAssociationsAPI, AdGroupsAPI, AdsAPI, CampaignsAPI
  - TargetsAPI, RecommendationsAPI, AdvertisingDealsAPI, AdvertisingDealTargetsAPI
  - BrandedKeywordsPricingsAPI, CampaignForecastsAPI, CommitmentsAPI
  - CommitmentSpendsAPI, KeywordReservationValidationsAPI, RecommendationTypesAPI
- Other modules - 16 classes
  - EligibilityAPI, LocationsAPI, ExportsAPI, MarketingStreamAPI
  - ReachForecastingAPI, ManagerAccountsAPI, PostsAPI, ProductMetadataAPI
  - AudiencesDiscoveryAPI, AdLibraryAPI, BrandHomeAPI, LocalizationAPI
  - AdsDataManagerAPI, BrandAssociationsAPI, ProductSelectorAPI
  - AdType (Enum), NameMatchType (Enum)

### Features

- OAuth2 authentication with automatic token refresh
- Automatic retry with exponential backoff (tenacity)
- Rate limit handling
- Unified client with lazy-loaded modules
- Full type hints support
- Comprehensive test suite (unit + integration)
- Support for all regions (NA, EU, FE)

### Documentation

- Complete README with usage examples
- API module structure documentation
- Installation instructions
- Authentication guide

---

## [Unreleased]

### Planned

- Async client support (asyncio/httpx)
- Batch operations optimization
- Response caching
- Webhook support for Marketing Stream

