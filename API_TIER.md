# Amazon Ads API 分级治理规范

> **核心原则**: 「不在 OpenAPI ≠ 虚假 API」，但必须分级治理
> **创建日期**: 2024-12-14
> **适用范围**: amazon-ads-api-python-sdk 全模块

---

## 📊 API 可信等级定义

### L1: OpenAPI Verified (Gold) 🥇

| 特征 | 说明 |
|------|------|
| **来源** | 官方 OpenAPI 下载目录 |
| **规范** | 有完整的 OpenAPI/Swagger 规范文件 |
| **稳定性** | 高，变更有版本控制 |
| **验证方式** | 可自动对比 spec vs 实现 |
| **目录位置** | `amazon_ads_api/core/` |
| **暴露方式** | 默认暴露，`client.sp.xxx()` |

**典型 API**:
- Sponsored Products (SP)
- Sponsored Brands (SB)
- Sponsored Display (SD)
- DSP (部分)
- Profiles
- Portfolios
- Attribution
- Reporting v3

---

### L2: API Reference Only (Silver) 🥈

| 特征 | 说明 |
|------|------|
| **来源** | 官方 API Reference 侧边栏 |
| **规范** | 无 OpenAPI，但有文档页面 |
| **稳定性** | 中等，官方维护但可能变动 |
| **验证方式** | 手动对比文档 |
| **目录位置** | `amazon_ads_api/reference/` |
| **暴露方式** | 显式访问，`client.reference.amc.xxx()` |

**典型 API**:
- Amazon Marketing Cloud (AMC) - 6 个模块
- Amazon Marketing Stream
- Sponsored TV (非 beta 部分)
- Retail Ad Service

---

### L3: Product-level / Aggregated (Bronze) 🥉

| 特征 | 说明 |
|------|------|
| **来源** | 官方文档，但非协议级 API |
| **规范** | 可能有 OpenAPI，但是高层抽象 |
| **稳定性** | 中等，随产品演进 |
| **验证方式** | 文档 + 实测 |
| **目录位置** | `amazon_ads_api/services/` |
| **暴露方式** | 服务层访问，`client.services.insights.xxx()` |

**典型 API**:
- Insights / Overlapping Audiences
- Recommendations
- Brand Metrics
- Brand Benchmarks
- Ads Data Manager
- Exports

---

### L4: Experimental / UI-bound (Red) 🔴

| 特征 | 说明 |
|------|------|
| **来源** | 文档存在，但标 beta/preview 或 UI 绑定 |
| **规范** | 可能不完整或频繁变动 |
| **稳定性** | 低，随时可能变更或下线 |
| **验证方式** | 仅实测，无保证 |
| **目录位置** | `amazon_ads_api/experimental/` |
| **暴露方式** | 必须显式导入，`from amazon_ads_api.experimental import xxx` |

**典型 API**:
- Sponsored TV Campaign management **beta**
- Performance+ insights **(beta)**
- Advertiser audiences **(beta)**
- Moderation / Pre-moderation
- Localization
- Ad library
- Brand Home
- Posts

---

## 🏗️ 目录结构规范

```
amazon_ads_api/
├── core/                      # L1 - OpenAPI verified
│   ├── sp/                    # Sponsored Products
│   │   ├── campaigns.py
│   │   ├── ad_groups.py
│   │   ├── keywords.py
│   │   └── targeting.py
│   ├── sb/                    # Sponsored Brands
│   ├── sd/                    # Sponsored Display
│   ├── dsp/                   # DSP (OpenAPI 部分)
│   ├── accounts/              # Profiles, Portfolios
│   └── reporting/             # Reporting v3
│
├── reference/                 # L2 - API Reference only
│   ├── amc/                   # Amazon Marketing Cloud
│   │   ├── administration.py
│   │   ├── reporting.py
│   │   ├── audiences.py
│   │   ├── data_upload.py
│   │   └── custom_models.py
│   ├── stream/                # Amazon Marketing Stream
│   ├── sponsored_tv/          # Sponsored TV (稳定部分)
│   └── retail_ad_service/     # Retail Ad Service
│
├── services/                  # L3 - Product-level
│   ├── insights/              # Audience Insights
│   ├── recommendations/       # Recommendations
│   ├── brand_metrics/         # Brand Metrics
│   ├── ads_data_manager/      # Ads Data Manager
│   └── exports/               # Exports
│
├── experimental/              # L4 - Beta / UI-bound
│   ├── moderation/            # Moderation APIs
│   ├── localization/          # Localization
│   ├── ad_library/            # Ad Library
│   ├── brand_home/            # Brand Home
│   └── posts/                 # Posts
│
├── common/                    # 共享基础设施
│   ├── base.py                # BaseAdsClient
│   ├── auth.py                # OAuth
│   └── http.py                # HTTP 层
│
└── client.py                  # 统一入口
```

---

## 🎯 SDK 暴露策略

### 默认暴露 (L1)

```python
from amazon_ads_api import AdsClient

client = AdsClient(...)

# L1 直接访问
campaigns = await client.sp.campaigns.list()
reports = await client.reporting.create_report(...)
```

### 显式访问 (L2)

```python
# L2 必须通过 reference
amc_result = await client.reference.amc.run_query(...)
stream = await client.reference.stream.subscribe(...)
```

### 服务层访问 (L3)

```python
# L3 通过 services
insights = await client.services.insights.get_overlapping(...)
recs = await client.services.recommendations.list(...)
```

### 实验性访问 (L4)

```python
# L4 必须单独导入，不暴露在主 client
from amazon_ads_api.experimental.moderation import ModerationAPI

moderation = ModerationAPI(auth)
result = await moderation.preview(...)  # ⚠️ 可能随时失效
```

---

## 📋 API 分级清单

### L1: OpenAPI Verified (Gold) 🥇

| 模块 | API 数量 | OpenAPI 规范 |
|------|---------|-------------|
| Sponsored Products | ~80 | SponsoredProducts_prod_3p.json |
| Sponsored Brands | ~60 | sponsored-brands/4-0/openapi.json |
| Sponsored Display | ~40 | sponsored-display/3-0/openapi.yaml |
| DSP Advertisers | ~10 | dsp/3-0/advertiser.yaml |
| DSP Audiences | ~5 | ADSPAudiences_prod_3p.json |
| DSP Conversions | ~17 | ConversionsAPI_prod_3p.json |
| DSP Measurement | ~30 | Measurement_prod_3p.json |
| Profiles | ~5 | profiles/3-0/openapi.yaml |
| Portfolios | ~5 | Portfolios_prod_3p.json |
| Attribution | ~5 | AmazonAttribution_prod_3p.json |
| Reporting v3 | ~5 | OfflineReport_prod_3p.json |
| Assets | ~6 | CreativeAssetLibrary_prod_3p.json |
| Stores | ~2 | Stores_prod_3p.json |
| Change History | ~1 | ChangeHistory_prod_3p.json |
| **总计** | **~270** | |

### L2: API Reference Only (Silver) 🥈

| 模块 | API 数量 | 文档 URL |
|------|---------|---------|
| AMC Administration | ? | /amc-administration |
| AMC Reporting | ? | /amc-reporting |
| AMC Rule-based Audiences | ? | /amc-rba |
| AMC Advertiser Data Upload | ? | /amc-advertiser-data-upload |
| AMC Custom Models | ? | /amc-custom-models |
| Amazon Marketing Stream | ? | /amazon-marketing-stream/openapi |
| Retail Ad Service | ? | /retail-ad-service |
| Retail Ad Service Identity | ? | /retail-ad-service/retailer-identity |
| **总计** | **~30+** | |

### L3: Product-level (Bronze) 🥉

| 模块 | API 数量 | 说明 |
|------|---------|------|
| Overlapping Audiences | 1 | Insights 唯一官方端点 |
| Recommendations | 3 | apply, list, update |
| Brand Metrics | 2 | create, get report |
| Brand Benchmarks | ? | 新发现 |
| Ads Data Manager | ? | 新发现 |
| Exports | ? | 新发现 |
| **总计** | **~15+** | |

### L4: Experimental (Red) 🔴

| 模块 | API 数量 | 风险等级 |
|------|---------|---------|
| Sponsored TV beta | ? | 高 |
| Performance+ insights (beta) | ? | 高 |
| Advertiser audiences (beta) | ? | 高 |
| Moderation | ? | 中 |
| Pre-moderation | ? | 中 |
| Localization | ? | 中 |
| Ad library | ? | 中 |
| Brand Home | ? | 低 |
| Posts | ? | 低 |
| DSP Frequency groups | ? | 中 |
| DSP Guidance | ? | 中 |
| **总计** | **~20+** | |

---

## 🚨 开发规则

### 1. 新 API 必须先定级

```
开发前必须回答：
1. 这个 API 有 OpenAPI 规范吗？ → L1
2. 这个 API 在 API Reference 有文档吗？ → L2
3. 这个 API 是产品级聚合吗？ → L3
4. 这个 API 是 beta 或 UI 绑定吗？ → L4
5. 以上都不是？ → ❌ 禁止实现
```

### 2. 代码内必须声明等级

```python
class AMCReportingAPI(BaseAdsClient):
    """
    AMC Reporting API
    
    API Tier: L2 (API Reference Only)
    Source: https://advertising.amazon.com/API/docs/en-us/amc-reporting
    OpenAPI: ❌ 不可用
    Stability: 中等
    """
    
    API_TIER = "L2"
    API_SOURCE = "api-reference"
    
    async def run_query(self, ...):
        ...
```

### 3. Claude 约束 Prompt

```
开发 Amazon Ads SDK 时必须遵守：

1. API 必须声明所属等级：L1/L2/L3/L4
2. L1：必须有 OpenAPI spec 验证
3. L2：必须标注 API Reference URL
4. L3：只允许 thin wrapper，不做业务逻辑
5. L4：必须放在 experimental/ 目录
6. 如果无法判断等级：禁止实现
7. 禁止"发明"不存在的 API 方法
8. 禁止在 L1 代码中添加 L3/L4 级别的便利方法
```

---

## 📝 版本历史

| 日期 | 更新内容 |
|------|---------|
| 2024-12-14 | 初始版本，定义 L1~L4 分级体系 |

