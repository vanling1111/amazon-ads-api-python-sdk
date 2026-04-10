# Amazon Ads API Python SDK

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![API Coverage](https://img.shields.io/badge/API%20Coverage-650%20endpoints-brightgreen.svg)]()
[![Tests](https://img.shields.io/badge/Tests-79%20Passing-brightgreen.svg)]()

Full-coverage async Python SDK for Amazon Ads API with auto-generated typed models and tiered API governance.

## Architecture

```
┌──────────────────────────────────────────────────────┐
│  Hand-written convenience layer (core/ reference/ …) │  ← Friendly API
├──────────────────────────────────────────────────────┤
│  Auto-generated thin clients (650 async methods)     │  ← 1:1 with spec
├──────────────────────────────────────────────────────┤
│  Auto-generated Pydantic models (5,000+ classes)     │  ← Type-safe
├──────────────────────────────────────────────────────┤
│  BaseAdsClient (httpx async, retry, rate-limit)      │  ← Foundation
└──────────────────────────────────────────────────────┘
```

- **86 OpenAPI specs** parsed, **80 active** for code generation
- **650 API operations** covered across all Amazon Ads products
- **5,000+ Pydantic models** with full type safety and `alias` support
- **L1–L4 tiered governance** separating production-ready from experimental APIs

## Quick Start

```bash
pip install amazon-ads-api
```

```python
from amazon_ads_api import AmazonAdsClient, AdsRegion

client = AmazonAdsClient(
    client_id="your_client_id",
    client_secret="your_client_secret",
    refresh_token="your_refresh_token",
    profile_id="your_profile_id",
    region=AdsRegion.NA,
)

# High-level convenience methods
campaigns = await client.sp.campaigns.list_campaigns(state_filter="ENABLED")

# Or use auto-generated typed methods directly
from amazon_ads_api.generated.models.models_sp import (
    SponsoredProductsListSponsoredProductsCampaignsRequestContent,
)
result = await client.sp.campaigns.list_sponsored_products_campaigns(
    body=SponsoredProductsListSponsoredProductsCampaignsRequestContent(
        max_results=50,
    )
)
```

## API Tier System

| Tier | Directory | Confidence | Count | Description |
|------|-----------|-----------|-------|-------------|
| **L1** | `core/` | Production | ~270 | OpenAPI-verified, full coverage |
| **L2** | `reference/` | Stable | ~30 | Official docs confirmed |
| **L3** | `services/` | Aggregated | ~15 | Product-level wrappers |
| **L4** | `experimental/` | Beta | ~20 | Experimental, requires opt-in |

```python
# L1 – direct access (safest)
campaigns = await client.sp.campaigns.list_campaigns()

# L2 – explicit namespace
result = await client.reference.amc.queries.execute_query(...)

# L3 – service layer
report = await client.services.reporting.reports.create_report(...)

# L4 – requires risk acknowledgment
exp = client.experimental(acknowledge_risk=True)
await exp.sponsored_tv.campaigns.list_campaigns()
```

## Covered Products

| Product | Spec | Endpoints | Generated |
|---------|------|-----------|-----------|
| Sponsored Products | `SponsoredProducts_prod_3p.json` | 80 | models + client |
| Sponsored Brands | `SponsoredBrands_v4_openapi.json` | 53 | models + client |
| Sponsored Display | `SponsoredDisplay_prod_3p.json` + v3 YAML | 76 | models + client |
| Sponsored TV | `SponsoredTV_prod_3p.json` | 26 | models + client |
| DSP | 14 independent specs | ~60 | models + clients |
| AMC | 6 independent specs | ~95 | models + clients |
| Accounts/Profiles | Multiple specs | ~30 | models + clients |
| Reporting | `OfflineReport_prod_3p.json` | 3 | models + client |
| + 60 more modules | See `codegen/spec_config.yaml` | ... | ... |

## Code Generation

The SDK ships with a custom Python code generator that reads OpenAPI specs and produces
Pydantic v2 models and async client classes. Generated code lives in `amazon_ads_api/generated/`.

### Regenerate after spec updates

```bash
# Download latest specs
python download_specs.py

# Regenerate all models and clients (~1.3s)
python -m codegen.generate

# Generate only one module
python -m codegen.generate --spec sp

# Dry run (parse + conflict resolution, no file output)
python -m codegen.generate --dry-run
```

### Generator components

| Module | Purpose |
|--------|---------|
| `codegen/spec_parser.py` | Parse JSON/YAML OpenAPI specs, extract paths + schemas |
| `codegen/model_generator.py` | Generate Pydantic v2 models from schemas |
| `codegen/client_generator.py` | Generate async client methods from paths |
| `codegen/conflict_resolver.py` | Resolve duplicate endpoints across specs |
| `codegen/spec_config.yaml` | Controls which specs are active and how they map to modules |
| `codegen/generate.py` | Main entry point |

### How inheritance works

Each hand-written API class inherits from the corresponding generated client:

```python
# amazon_ads_api/core/sp/campaigns.py
from amazon_ads_api.generated.clients.clients_sp import SpClient as _GenBase

class SPCampaignsAPI(_GenBase):
    """Inherits 80 auto-generated raw methods, adds convenience methods."""

    async def list_campaigns(self, state_filter=None, ...):
        """User-friendly wrapper with auto-pagination, filters, etc."""
        ...
```

If the generated code is not available, classes fall back to `BaseAdsClient`.

## Multi-Account Support

Each `AmazonAdsClient` instance is fully isolated and safe for concurrent use:

```python
import asyncio

client1 = AmazonAdsClient(profile_id="profile-123", ...)
client2 = AmazonAdsClient(profile_id="profile-456", ...)

campaigns1, campaigns2 = await asyncio.gather(
    client1.sp.campaigns.list_campaigns(),
    client2.sp.campaigns.list_campaigns(),
)
```

## Authentication

1. Register with Amazon Ads Partner Network
2. Create a Login with Amazon (LwA) application
3. Request Amazon Ads API permissions
4. Obtain Client ID, Client Secret, and Refresh Token via OAuth2

| Region | Endpoint |
|--------|----------|
| NA | `https://advertising-api.amazon.com` |
| EU | `https://advertising-api-eu.amazon.com` |
| FE | `https://advertising-api-fe.amazon.com` |

## Testing

```bash
pip install -e ".[dev]"

# Run all unit tests (79 tests)
pytest tests/unit/ -v

# Run only codegen tests
pytest tests/unit/test_codegen.py -v

# Run with coverage
pytest --cov=amazon_ads_api --cov-report=html
```

## Project Structure

```
amazon-ads-api-python-sdk/
├── specs/                          # 86 OpenAPI spec files
├── codegen/                        # Code generator
│   ├── spec_config.yaml            # Spec selection & mapping
│   ├── spec_parser.py
│   ├── model_generator.py
│   ├── client_generator.py
│   ├── conflict_resolver.py
│   └── generate.py
├── amazon_ads_api/
│   ├── base.py                     # BaseAdsClient (httpx async)
│   ├── client.py                   # L1-L4 entry point
│   ├── generated/                  # Auto-generated (157 files)
│   │   ├── models/                 # 80 Pydantic model files
│   │   └── clients/                # 77 async client files
│   ├── core/                       # L1 hand-written wrappers
│   ├── reference/                  # L2
│   ├── services/                   # L3
│   └── experimental/               # L4
├── tests/
│   ├── unit/                       # 79 unit tests
│   └── integration/
├── scripts/
│   ├── regenerate.sh               # One-command regeneration
│   └── migrate_inheritance.py      # Inheritance migration tool
└── pyproject.toml
```

## License

MIT

## Contributing

1. Fork this repo
2. Create a feature branch
3. After spec changes, run `python -m codegen.generate` to regenerate
4. Run `pytest tests/unit/` to verify
5. Submit a Pull Request
