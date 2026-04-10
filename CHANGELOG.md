# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2026-04-10

### Added
- **Code generation system** (`codegen/`) — custom Python generator producing Pydantic v2 models and async clients from OpenAPI specs
  - `spec_parser.py` — JSON/YAML OpenAPI parser with $ref resolution
  - `model_generator.py` — Pydantic v2 model generation (StrEnum, Field alias, allOf/oneOf)
  - `client_generator.py` — Async client method generation inheriting BaseAdsClient
  - `conflict_resolver.py` — Multi-version spec endpoint conflict resolution
  - `spec_config.yaml` — Configuration for 86 specs (80 active)
- **5,018 auto-generated Pydantic model classes** in `amazon_ads_api/generated/models/`
- **650 auto-generated async API methods** in `amazon_ads_api/generated/clients/`
- **CI/CD workflows**:
  - `ci.yml` — Lint, test, codegen validation on push/PR (Python 3.11-3.13 matrix)
  - `check-spec-updates.yml` — Daily spec update detection with auto GitHub Issue creation
- `scripts/check_spec_updates.py` — Spec freshness checker (HEAD or full hash comparison)
- `scripts/regenerate.sh` — One-command regeneration
- `scripts/migrate_inheritance.py` — Bulk inheritance migration tool
- 17 new codegen unit tests (79 total tests, 100% pass rate)

### Changed
- All 88 hand-written API files now inherit from generated clients (was: BaseAdsClient directly)
- Expanded API spec coverage from 59 to 86 OpenAPI specs (642+ unique endpoints)
- `pyproject.toml` — added `pydantic>=2.0.0` dependency, `pyyaml>=6.0.0` dev dependency

### Removed
- `specs/Reporting_prod_3p.json` — empty stub (0 paths)
- Root-level debug JSON/YAML files

## [2.0.0] - 2025-01-15

### Added
- Initial release of Amazon Ads API Python SDK
- Support for 59 official Amazon Ads API endpoints
- 100% coverage verification against official OpenAPI specs
- Async/await support with httpx
- Automatic OAuth2 token refresh
- Rate limiting and retry mechanisms
- Comprehensive error handling
- Unit tests (62 tests, 100% pass rate)
- Integration tests (6 tests, 100% pass rate)
- End-to-end tests (5 tests, 100% pass rate)

### Core APIs (L1 - OpenAPI Verified)
- **Sponsored Products (SP)**: Campaigns, Ad Groups, Keywords, Product Ads, Negative Keywords, Campaign Negative Keywords, Targets, Negative Targets, Budget Rules, Budget Recommendations
- **Sponsored Brands (SB)**: Campaigns, Ad Groups, Keywords, Product Targeting, Brand Video, Creatives, Moderation, Landing Pages
- **Sponsored Display (SD)**: Campaigns, Ad Groups, Product Ads, Targets, Creative Assets, Budget Rules, Forecast
- **DSP**: Advertisers, Audiences, Campaigns, Conversions, Measurement, Target KPI
- **Accounts**: Profiles, Portfolios, Budgets, Billing, Advertising Accounts, Test Accounts
- **Audiences**: Audience Discovery, Product Selector
- **Exports**: Data Exports, Report Exports
- **Eligibility**: Campaign Eligibility, Keyword Eligibility
- **Locations**: Location Targeting

### Reference APIs (L2 - Official Documentation)
- **Amazon Marketing Cloud (AMC)**: Administration, Reporting, Audiences
- **Attribution**: Attribution Tags, Publishers, Reports
- **Data Provider**: Data Sets, Uploads
- **Unified API**: Amazon Ads API v1 (campaigns, keywords, recommendations, forecasts, etc.)
- **Posts**: Sponsored Posts API
- **Retail Ad Service**: Orders, Line Items, Creatives
- **Marketing Stream**: Real-time data streaming

### Service APIs (L3 - Product Level)
- **Reporting**: Reports v2, Reports v3, MMM (Marketing Mix Modeling), Offline Reports
- **Recommendations**: Campaign Recommendations, Keyword Recommendations, Budget Recommendations
- **Insights**: Brand Insights, Product Insights, Audience Insights
- **Common Services**: Change History, Creative Asset Library, Stores
- **Media Planning**: Reach Forecasting, Media Planning Tools
- **Brand Associations**: Brand Safety, Brand Suitability
- **Ads Data Manager**: Data Sources, Audiences

### Experimental APIs (L4 - Beta)
- **Ad Library**: Ad Repository Management
- **Brand Home**: Store Pages, Brand Stores
- **Localization**: Currency, Keyword, Product, Targeting Expression Localization
- **Moderation**: Pre-moderation, Creative Moderation
- **Partner Opportunities**: Partner Network
- **Persona Builder**: Audience Persona
- **Sponsored TV**: TV Campaigns, Formats

### Infrastructure
- Automated coverage verification scripts
- Deep verification for duplicate detection
- Comprehensive test suite (unit/integration/e2e)
- OpenAPI spec synchronization (59 specs)
- Documentation generation

## [0.1.0] - 2025-01-15

### Added
- Initial alpha release
- Basic API client structure
- OAuth2 authentication
- Core SP/SB/SD APIs

### Fixed
- Multiple path errors in AMC APIs
- Incorrect endpoint implementations in Ad Library, Brand Home, Localization
- HTTP method mismatches in Unified API
- Missing endpoints in Advertising Accounts API

### Changed
- Migrated from requests to httpx for async support
- Restructured project to 4-tier architecture (L1/L2/L3/L4)
- Improved error handling and retry logic
- Enhanced token management with automatic refresh

## [0.0.1] - 2025-01-01

### Added
- Project initialization
- Basic project structure
- Initial README and LICENSE

---

## Version Strategy

- **MAJOR**: Breaking API changes
- **MINOR**: New features, new API endpoints
- **PATCH**: Bug fixes, documentation updates

## Links

- [Repository](https://github.com/vanling1111/amazon-ads-api-python-sdk)
- [Issues](https://github.com/vanling1111/amazon-ads-api-python-sdk/issues)
- [Pull Requests](https://github.com/vanling1111/amazon-ads-api-python-sdk/pulls)

