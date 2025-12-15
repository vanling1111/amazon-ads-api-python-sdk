# Amazon Ads API Python SDK

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![API Coverage](https://img.shields.io/badge/API%20Coverage-335+-brightgreen.svg)]()
[![L1 Verified](https://img.shields.io/badge/L1%20Verified-270%20APIs-gold.svg)]()
[![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)]()

**企业级 Amazon Ads API Python SDK - 分级治理的 API 覆盖**

## 🆕 API 分级体系 (Tiered API Model)

本 SDK 采用**业界首创的 API 分级治理体系**，解决 Amazon Ads API 碎片化问题：

| 等级 | 目录 | 可信度 | 数量 | 说明 |
|------|------|--------|------|------|
| **L1 Gold** 🥇 | `core/` | ⭐⭐⭐⭐⭐ | ~270 | OpenAPI 验证，生产可用 |
| **L2 Silver** 🥈 | `reference/` | ⭐⭐⭐⭐ | ~30 | 官方文档确认，需显式访问 |
| **L3 Bronze** 🥉 | `services/` | ⭐⭐⭐ | ~15 | 产品级聚合，便利封装 |
| **L4 Red** 🔴 | `experimental/` | ⭐⭐ | ~20 | Beta/实验性，需确认风险 |

```python
# L1: 默认访问（最安全）
campaigns = client.sp.campaigns.list()

# L2: 显式命名空间（官方但非 OpenAPI）
result = client.reference.amc.run_query(...)

# L3: 服务层
report = client.services.reporting.create_report(...)

# L4: 需确认风险
exp = client.experimental(acknowledge_risk=True)
exp.sponsored_tv.create_campaign(...)
```

## ✨ 特性

- 🏆 **API 分级治理** - L1~L4 可信度分级，告别虚假 API
- 🎯 **335+ API 覆盖** - 覆盖全部 Amazon Ads API 产品线
- 🔍 **OpenAPI 验证** - L1 API 100% OpenAPI 规范验证
- 🚀 **简洁易用** - 统一客户端入口，链式调用
- 🔄 **自动认证** - OAuth2 Token 自动刷新
- ⚡ **自动重试** - 内置指数退避重试机制
- 🛡️ **Rate Limit** - 自动处理限流
- 📊 **类型安全** - 完整的类型提示
- 🧪 **完整测试** - 单元测试 + 集成测试

## 📦 API 模块总览

### 🥇 L1: Core APIs (OpenAPI 验证)

| 模块 | 描述 | 端点数 | OpenAPI |
|------|------|--------|---------|
| **sp/** | Sponsored Products | ~80 | ✅ v3 |
| **sb/** | Sponsored Brands | ~50 | ✅ v4 |
| **sd/** | Sponsored Display | ~40 | ✅ v3 |
| **dsp/** | Amazon DSP | ~60 | ✅ v3 |
| **accounts/** | Profiles, Portfolios, Billing | ~15 | ✅ |
| **audiences/** | Audiences Discovery | ~5 | ✅ |
| **eligibility/** | Eligibility | ~3 | ✅ |
| **exports/** | Exports | ~5 | ✅ |
| **products/** | Product Selector, Metadata | ~10 | ✅ |

### 🥈 L2: Reference APIs (官方文档确认)

| 模块 | 描述 | 端点数 | 文档 |
|------|------|--------|------|
| **amc/** | Amazon Marketing Cloud | ~20 | API Reference |
| **stream/** | Amazon Marketing Stream | ~5 | API Reference |
| **retail_ad/** | Retail Ad Service | ~15 | API Reference |
| **attribution/** | Amazon Attribution | ~5 | API Reference |
| **posts/** | Posts | ~5 | API Reference |

### 🥉 L3: Service APIs (产品级聚合)

| 模块 | 描述 | 说明 |
|------|------|------|
| **reporting/** | Reports v3, Brand Metrics | 便利封装 |
| **insights/** | Audience/Keyword Insights | 高层抽象 |
| **recommendations/** | Recommendations | 聚合服务 |

### 🔴 L4: Experimental APIs (Beta/实验性)

| 模块 | 描述 | 状态 |
|------|------|------|
| **sponsored_tv/** | Sponsored TV | Beta |
| **moderation/** | Creative Moderation | UI-bound |
| **localization/** | Localization | 不稳定 |

## 🚀 快速开始

### 安装

```bash
# 从 PyPI 安装
pip install amazon-ads-api

# 或从 GitHub 安装最新版
pip install git+https://github.com/vanling1111/amazon-ads-api-python-sdk.git
```

### 基础使用

```python
from amazon_ads_api import AmazonAdsClient, AdsRegion

# 创建客户端
client = AmazonAdsClient(
    client_id="your_client_id",
    client_secret="your_client_secret",
    refresh_token="your_refresh_token",
    profile_id="your_profile_id",  # 必需
    region=AdsRegion.NA,  # NA, EU, FE
)

# 获取 SP Campaigns
campaigns = await client.sp.campaigns.list_campaigns()
print(campaigns)

# 获取关键词
keywords = await client.sp.keywords.list_keywords(campaign_id="123456")

# 更新竞价
await client.sp.keywords.update_bid(keyword_id="789", new_bid=1.50)
```

## 🏢 Multi-Account Support

This SDK is **multi-account capable** and designed for concurrent use:

✅ **What the SDK provides:**
- Multiple Amazon Ads accounts/profiles can run concurrently
- Each `AmazonAdsClient` instance is completely isolated
- Safe for async concurrent operations
- Handles authentication, rate limiting, and retries per-client

❌ **What the SDK does NOT manage:**
- SaaS tenant or user management
- Persistent OAuth token storage
- Account authorization flows
- User-to-profile permission mapping

**These are responsibilities of your application's Service layer.**

### Example: Multiple Profiles Concurrently

```python
import asyncio
from amazon_ads_api import AmazonAdsClient, AdsRegion

# Create independent clients for different profiles
client1 = AmazonAdsClient(
    client_id='...',
    client_secret='...',
    refresh_token='token_for_profile_1',
    profile_id='profile-123',
    region=AdsRegion.NA
)

client2 = AmazonAdsClient(
    client_id='...',
    client_secret='...',
    refresh_token='token_for_profile_2',
    profile_id='profile-456',
    region=AdsRegion.NA
)

# Concurrent operations are safe!
campaigns1, campaigns2 = await asyncio.gather(
    client1.sp.campaigns.list_campaigns(),
    client2.sp.campaigns.list_campaigns()
)
```

### For SaaS Applications

If you're building a multi-tenant SaaS platform:
1. Your **database** stores user-to-profile mappings
2. Your **Service layer** validates user permissions
3. Your **Service layer** creates one `AmazonAdsClient` per profile
4. Your **API layer** enforces tenant boundaries

**See [examples/saas_integration.py](examples/saas_integration.py) for a complete example.**

### 高级用法 - v2.0 分级访问

```python
# ========== L1 Core APIs (直接访问) ==========
# Sponsored Products
campaigns = client.sp.campaigns.list_campaigns()
keywords = client.sp.keywords.list_keywords(campaign_id="123")

# Sponsored Brands
sb_campaigns = client.sb.campaigns.list_campaigns()

# Sponsored Display
sd_campaigns = client.sd.campaigns.list_campaigns()

# DSP
dsp_campaigns = client.dsp.campaigns.list_campaigns(advertiser_id="xxx")
dsp_audiences = client.dsp.audiences.list_audiences()

# Accounts
profiles = client.accounts.profiles.list_profiles()
portfolios = client.accounts.portfolios.list_portfolios()

# ========== L2 Reference APIs (显式命名空间) ==========
# Amazon Marketing Cloud
query_result = client.reference.amc.queries.execute_query(
    query="SELECT * FROM your_table WHERE date > '2024-01-01'"
)

# Marketing Stream
subscriptions = client.reference.stream.subscriptions.list()

# Retail Ad Service
ras_campaigns = client.reference.retail_ad_service.campaigns.list()

# ========== L3 Services (产品级聚合) ==========
# Reports
report = client.services.reporting.reports.create_report(
    report_type="spCampaigns",
    time_unit="DAILY",
    start_date="2024-01-01",
    end_date="2024-01-31",
)

# Insights
keyword_insights = client.services.insights.keywords.get_ranking_keywords()

# Common utilities
assets = client.services.common.assets.upload_asset(...)

# ========== L4 Experimental (需确认风险) ==========
# Sponsored TV (Beta)
tv_campaigns = client.experimental.sponsored_tv.campaigns.list_campaigns()

# Pre-moderation
moderation = client.experimental.moderation.pre_moderation.submit()
```

## 📖 API 文档

### v2.0 模块结构 (分级架构)

```
client
├── sp                    # L1 - Sponsored Products
├── sb                    # L1 - Sponsored Brands
├── sd                    # L1 - Sponsored Display
├── dsp                   # L1 - Amazon DSP
├── accounts              # L1 - Profiles, Portfolios, Billing
│
├── reference/            # L2 - API Reference 确认
│   ├── amc               # Amazon Marketing Cloud
│   ├── stream            # Marketing Stream
│   ├── retail_ad_service # Retail Ad Service
│   ├── data_provider     # Data Provider
│   ├── posts             # Posts
│   └── unified_api       # Unified API
│
├── services/             # L3 - 产品级聚合
│   ├── reporting         # Reports V3, Brand Metrics, MMM
│   ├── insights          # Keyword/Audience Insights
│   ├── recommendations   # Recommendations
│   ├── common            # Assets, History, Stores
│   ├── brand_associations
│   ├── ads_data_manager
│   └── media_planning
│
└── experimental/         # L4 - Beta/实验性
    ├── sponsored_tv      # Sponsored TV (Beta)
    ├── moderation        # Pre/Unified Moderation
    ├── localization      # Localization
    ├── ad_library        # Ad Library
    └── brand_home        # Brand Home
```

### L1 Core 详细结构

```
core/
├── sp/                   # Sponsored Products (~80 endpoints)
│   ├── campaigns
│   ├── ad_groups
│   ├── keywords
│   ├── targeting
│   ├── budget_rules
│   ├── recommendations
│   ├── product_eligibility
│   ├── theme_targeting
│   ├── target_promotion_groups
│   └── global_recommendations
├── sb/                   # Sponsored Brands (~50 endpoints)
│   ├── campaigns
│   ├── ads
│   ├── keywords
│   ├── creatives
│   ├── brand_video
│   ├── moderation
│   ├── optimization
│   ├── forecasts
│   ├── targeting
│   └── legacy_migration
├── sd/                   # Sponsored Display (~40 endpoints)
│   ├── campaigns
│   ├── targeting
│   ├── creatives
│   ├── audiences
│   ├── moderation
│   ├── optimization
│   ├── brand_safety
│   ├── locations
│   └── reports
├── dsp/                  # Amazon DSP (~60 endpoints)
│   ├── campaigns
│   ├── advertisers
│   ├── audiences
│   ├── conversions
│   ├── measurement
│   └── target_kpi
├── accounts/             # Accounts (~15 endpoints)
│   ├── profiles
│   ├── portfolios
│   ├── billing
│   ├── budgets
│   └── test_accounts
├── audiences/            # Audiences Discovery
├── eligibility/          # Eligibility
├── exports/              # Exports
├── products/             # Product Selector
└── locations/            # Locations
```

## 🔧 配置选项

```python
client = AmazonAdsClient(
    client_id="xxx",
    client_secret="xxx",
    refresh_token="xxx",
    region=AdsRegion.NA,      # API 区域
    profile_id="123456",      # 可选，也可以后续设置
    max_retries=3,            # 最大重试次数
    timeout=30,               # 请求超时（秒）
)
```

## 🔐 认证

### 获取凭证

1. 注册 Amazon Ads Partner Network
2. 创建 Login with Amazon (LwA) 应用
3. 申请 Amazon Ads API 权限
4. 获取 Client ID, Client Secret
5. 通过 OAuth2 流程获取 Refresh Token

### 区域端点

| 区域 | 端点 |
|------|------|
| NA (北美) | `https://advertising-api.amazon.com` |
| EU (欧洲) | `https://advertising-api-eu.amazon.com` |
| FE (远东) | `https://advertising-api-fe.amazon.com` |

## 🧪 测试

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行所有测试
pytest

# 只运行单元测试
pytest tests/unit/

# 只运行集成测试
pytest tests/integration/

# 覆盖率报告
pytest --cov=amazon_ads_api --cov-report=html

# 运行导入测试
python tests/test_imports.py
```

### 测试结构

```
tests/
├── conftest.py              # 测试配置和fixtures
├── test_imports.py          # 导入测试 (101个类)
├── unit/                    # 单元测试
│   ├── test_base.py         # BaseAdsClient 测试
│   ├── test_client.py       # AmazonAdsClient 测试
│   ├── test_sp.py           # SP 模块测试
│   ├── test_sb.py           # SB 模块测试
│   └── ...
└── integration/             # 集成测试
    ├── test_auth.py         # 认证流程测试
    ├── test_sp_api.py       # SP API 集成测试
    └── ...
```

## 📝 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 提交 Pull Request

## 📞 支持

- 📧 Email: vanling1111@gmail.com
- 📖 文档: [GitHub Wiki](https://github.com/vanling1111/amazon-ads-api-python-sdk/wiki)
- 🐛 问题: [GitHub Issues](https://github.com/vanling1111/amazon-ads-api-python-sdk/issues)

## 📊 项目状态

- **API 类数量**: 101
- **模块数量**: 30
- **测试覆盖率**: 目标 >80%
- **Python 版本**: 3.13+

---

Made with ❤️ by [vanling1111](https://github.com/vanling1111)
