# Amazon Ads API SDK - Usage Examples

This directory contains practical examples for common use cases.

## 📁 Examples

### [`saas_integration.py`](saas_integration.py)

**Complete multi-tenant SaaS integration example**

Demonstrates:
- ✅ Multi-tenant architecture (Tenant → Account → Profile hierarchy)
- ✅ Permission validation (preventing cross-tenant access)
- ✅ Service layer for client management
- ✅ FastAPI API endpoints
- ✅ Concurrent multi-profile operations
- ✅ Database schema design

**Use this if you're building a SaaS platform** (like an Amazon Ads management tool).

---

## 🚀 Basic Usage

### Single Profile

```python
from amazon_ads_api import AmazonAdsClient, AdsRegion

client = AmazonAdsClient(
    client_id='your_client_id',
    client_secret='your_client_secret',
    refresh_token='your_refresh_token',
    profile_id='your_profile_id',
    region=AdsRegion.NA
)

# Get campaigns
campaigns = await client.sp.campaigns.list_campaigns()
print(campaigns)
```

### Multiple Profiles (Concurrent)

```python
import asyncio
from amazon_ads_api import AmazonAdsClient, AdsRegion

# Create independent clients
client1 = AmazonAdsClient(..., profile_id='profile-123')
client2 = AmazonAdsClient(..., profile_id='profile-456')

# Concurrent operations
campaigns1, campaigns2 = await asyncio.gather(
    client1.sp.campaigns.list_campaigns(),
    client2.sp.campaigns.list_campaigns()
)
```

---

## 📖 More Examples Coming Soon

- [ ] Async batch operations
- [ ] Report generation and download
- [ ] Campaign automation
- [ ] Keyword optimization
- [ ] Budget management
- [ ] Django integration
- [ ] Celery task integration

---

## 🤝 Contributing Examples

Have a useful example? Submit a PR!

1. Create a new `.py` file in `examples/`
2. Include docstrings and comments
3. Update this README
4. Ensure it runs without errors

