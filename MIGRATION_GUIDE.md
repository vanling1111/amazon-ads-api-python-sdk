# SDK v2.0 迁移指南

## 概述

v2.0 引入了 **API 分级治理架构**，将所有 API 按可信度分为 4 个等级：

| 等级 | 目录 | 可信度 | 说明 |
|------|------|--------|------|
| L1 Gold 🥇 | `core/` | ⭐⭐⭐⭐⭐ | OpenAPI 验证，生产可用 |
| L2 Silver 🥈 | `reference/` | ⭐⭐⭐⭐ | 官方文档确认 |
| L3 Bronze 🥉 | `services/` | ⭐⭐⭐ | 产品级聚合 |
| L4 Red 🔴 | `experimental/` | ⭐⭐ | Beta/实验性 |

## 变更摘要

### L1 Core APIs (无变化)

以下 API 访问方式**保持不变**：

```python
# v1.x 和 v2.0 相同
client.sp.campaigns.list_campaigns()
client.sb.campaigns.list_campaigns()
client.sd.campaigns.list_campaigns()
client.dsp.campaigns.list_campaigns()
client.accounts.profiles.list_profiles()
```

### L2 Reference APIs (需更新)

AMC、Stream 等 API 移到 `reference` 命名空间：

```python
# v1.x (旧)
client.amc.queries.execute_query(...)
client.stream.subscriptions.list()

# v2.0 (新)
client.reference.amc.queries.execute_query(...)
client.reference.stream.subscriptions.list()
client.reference.retail_ad_service.campaigns.list()
```

### L3 Services (需更新)

Reporting、Insights 等移到 `services` 命名空间：

```python
# v1.x (旧)
client.reporting.reports.create_report(...)
client.insights.keywords.get_ranking_keywords()

# v2.0 (新)
client.services.reporting.reports.create_report(...)
client.services.insights.keywords.get_ranking_keywords()
client.services.common.assets.upload_asset(...)
```

### L4 Experimental (需更新)

Sponsored TV、Moderation 等移到 `experimental` 命名空间：

```python
# v1.x (旧)
client.sponsored_tv.campaigns.list_campaigns()
client.moderation.pre_moderation.submit()

# v2.0 (新)
client.experimental.sponsored_tv.campaigns.list_campaigns()
client.experimental.moderation.pre_moderation.submit()
```

## 迁移步骤

### 1. 更新依赖

```bash
pip install --upgrade amazon-ads-api-python-sdk
```

### 2. 更新导入

```python
# 仍然使用同一个入口
from amazon_ads_api import AmazonAdsClient

# 直接导入特定 API 类（如需要）
from amazon_ads_api.core.sp.campaigns import SPCampaignsAPI
from amazon_ads_api.reference.amc.queries import AMCQueriesAPI
from amazon_ads_api.services.reporting.reports_v3 import ReportsV3API
from amazon_ads_api.experimental.sponsored_tv.campaigns import STVCampaignsAPI
```

### 3. 更新 API 调用

按上述对照表更新访问路径。

## 完整示例

```python
from amazon_ads_api import AmazonAdsClient

client = AmazonAdsClient(
    client_id="xxx",
    client_secret="xxx",
    refresh_token="xxx",
)
client.with_profile("your_profile_id")

# ========== L1 Core (直接访问，与 v1.x 相同) ==========
campaigns = client.sp.campaigns.list_campaigns()
profiles = client.accounts.profiles.list_profiles()

# ========== L2 Reference (新命名空间) ==========
amc_result = client.reference.amc.queries.execute_query(
    query="SELECT * FROM table"
)

# ========== L3 Services (新命名空间) ==========
report = client.services.reporting.reports.create_report(
    report_type="spCampaigns"
)

# ========== L4 Experimental (新命名空间) ==========
tv_campaigns = client.experimental.sponsored_tv.campaigns.list_campaigns()
```

## FAQ

### Q: 为什么要分级？

A: Amazon Ads API 生态碎片化严重，部分 API 有 OpenAPI 规范，部分只有文档，部分是 Beta。分级让用户清楚知道每个 API 的可靠性。

### Q: L4 API 能用于生产吗？

A: 可以，但需要了解风险。L4 API 可能随时变化或废弃。

### Q: 老代码不改会怎样？

A: v2.0 对 L1 API 保持向后兼容。L2-L4 API 的旧路径将显示废弃警告，建议迁移到新命名空间。

## 支持

- Issues: https://github.com/vanling1111/amazon-ads-api-python-sdk/issues
- Email: vanling1111@gmail.com

