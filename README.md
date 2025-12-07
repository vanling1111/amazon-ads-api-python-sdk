# Amazon Ads API Python SDK

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![API Coverage](https://img.shields.io/badge/API%20Coverage-100%25-brightgreen.svg)]()

**完整覆盖 Amazon Ads API 的 Python SDK**

## ✨ 特性

- 🎯 **100% API 覆盖** - 支持所有 Amazon Ads API 端点
- 🚀 **简洁易用** - 统一客户端入口，链式调用
- 🔄 **自动认证** - OAuth2 Token 自动刷新
- ⚡ **自动重试** - 内置指数退避重试机制
- 🛡️ **Rate Limit** - 自动处理限流
- 📊 **类型安全** - 完整的类型提示

## 📦 支持的 API 模块

| 模块 | 描述 | 状态 |
|------|------|------|
| **SP** | Sponsored Products | ✅ |
| **SB** | Sponsored Brands | ✅ |
| **SD** | Sponsored Display | ✅ |
| **DSP** | Amazon DSP | ✅ |
| **Reporting** | 报告 API | ✅ |
| **Accounts** | 账户管理 | ✅ |
| **Insights** | 洞察分析 | ✅ |
| **AMC** | Amazon Marketing Cloud | ✅ |
| **Sponsored TV** | 电视广告 | ✅ |
| **Retail Ad Service** | 零售广告 | ✅ |
| **+ 20 更多模块** | 完整覆盖 | ✅ |

## 🚀 快速开始

### 安装

```bash
# 从本地安装
pip install -e /path/to/amazon-ads-api-python-sdk

# 或发布到 PyPI 后
pip install amazon-ads-api
```

### 基础使用

```python
from amazon_ads_api import AmazonAdsClient, AdsRegion

# 创建客户端
client = AmazonAdsClient(
    client_id="your_client_id",
    client_secret="your_client_secret",
    refresh_token="your_refresh_token",
    region=AdsRegion.NA,  # NA, EU, FE
)

# 设置 Profile ID
client.with_profile("your_profile_id")

# 获取 SP Campaigns
campaigns = client.sp.campaigns.list_campaigns()
print(campaigns)

# 获取关键词
keywords = client.sp.keywords.list_keywords(campaign_id="123456")

# 更新竞价
client.sp.keywords.update_bid(keyword_id="789", new_bid=1.50)
```

### 高级用法

```python
# DSP 广告
orders = client.dsp.orders.list_orders(advertiser_id="xxx")
line_items = client.dsp.line_items.list_line_items(order_id="xxx")

# 报告
report = client.reporting.reports.create_and_wait_report(
    report_type="spCampaigns",
    time_unit="DAILY",
    start_date="2024-01-01",
    end_date="2024-01-31",
    metrics=["impressions", "clicks", "spend", "sales14d"],
)

# 洞察
keyword_insights = client.insights.keywords.search_keywords("running shoes")
category_insights = client.insights.category.get_category_metrics(category_id="123")

# AMC 查询
query_result = client.amc.queries.execute_query(
    query="SELECT * FROM your_table WHERE date > '2024-01-01'"
)

# Sponsored TV
tv_campaigns = client.st.campaigns.list_campaigns()
```

## 📖 API 文档

### 模块结构

```
client
├── sp                    # Sponsored Products
│   ├── campaigns
│   ├── ad_groups
│   ├── keywords
│   ├── targeting
│   ├── budget_rules
│   ├── recommendations
│   ├── product_eligibility
│   └── theme_targeting
├── sb                    # Sponsored Brands
│   ├── campaigns
│   ├── ads
│   ├── keywords
│   ├── creatives
│   ├── brand_video
│   └── moderation
├── sd                    # Sponsored Display
│   ├── campaigns
│   ├── targeting
│   ├── creatives
│   ├── audiences
│   └── moderation
├── dsp                   # Amazon DSP
│   ├── audiences
│   ├── advertisers
│   ├── orders
│   ├── line_items
│   ├── creatives
│   ├── inventory
│   ├── measurement
│   ├── conversions
│   └── target_kpi
├── reporting             # Reporting
│   ├── reports
│   ├── brand_metrics
│   ├── stores_analytics
│   └── mmm
├── accounts              # Accounts
│   ├── profiles
│   ├── portfolios
│   ├── billing
│   ├── budgets
│   └── test_accounts
├── insights              # Insights
│   ├── category
│   ├── keywords
│   └── audience
├── amc                   # Amazon Marketing Cloud
│   ├── queries
│   ├── audiences
│   └── workflows
├── st                    # Sponsored TV
├── ras                   # Retail Ad Service
├── eligibility           # Eligibility
├── recommendations       # Recommendations
├── data_provider         # Data Provider
├── products              # Products
├── moderation            # Moderation
├── stream                # Marketing Stream
├── locations             # Locations
├── exports               # Exports
├── media_planning        # Media Planning
├── manager_accounts      # Manager Accounts
├── posts                 # Posts
├── product_metadata      # Product Metadata
├── audiences_discovery   # Audiences Discovery
├── ads_v1                # Amazon Ads API v1
├── ad_library            # Ad Library
├── brand_home            # Brand Home
├── localization          # Localization
├── ads_data_manager      # Ads Data Manager
└── brand_associations    # Brand Associations
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

# 运行测试
pytest

# 覆盖率报告
pytest --cov=amazon_ads_api --cov-report=html
```

## 📝 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📞 支持

- 📧 Email: support@example.com
- 📖 文档: [GitHub Wiki](https://github.com/yourusername/amazon-ads-api-python-sdk/wiki)
- 🐛 问题: [GitHub Issues](https://github.com/yourusername/amazon-ads-api-python-sdk/issues)

