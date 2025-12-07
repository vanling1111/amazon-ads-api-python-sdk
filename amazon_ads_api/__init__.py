"""
Amazon Ads API Python SDK

完整覆盖 Amazon Ads API 的 Python SDK，100% API 覆盖率。

安装：
    pip install amazon-ads-api

快速开始：
    ```python
    from amazon_ads_api import AmazonAdsClient, AdsRegion
    
    # 创建客户端
    client = AmazonAdsClient(
        client_id="xxx",
        client_secret="xxx",
        refresh_token="xxx",
        region=AdsRegion.NA,
    )
    
    # 设置Profile
    client.with_profile("123456789")
    
    # SP操作
    campaigns = client.sp.campaigns.list_campaigns()
    keywords = client.sp.keywords.list_keywords(campaign_id="xxx")
    
    # SB操作
    sb_campaigns = client.sb.campaigns.list_campaigns()
    
    # DSP操作
    orders = client.dsp.orders.list_orders(advertiser_id="xxx")
    
    # 报告
    report = client.reporting.reports.create_and_wait_report(
        report_type="spCampaigns",
        time_unit="DAILY",
        start_date="2024-01-01",
        end_date="2024-01-31",
        metrics=["impressions", "clicks", "spend"],
    )
    
    # 账户
    profiles = client.accounts.profiles.list_profiles()
    portfolios = client.accounts.portfolios.list_portfolios()
    ```
"""

# 基础类
from .base import (
    BaseAdsClient,
    AdsRegion,
    AmazonAdsError,
)

# 统一客户端
from .client import (
    AmazonAdsClient,
    AdsAPIClient,  # 兼容别名
)

# SP模块
from .sp import (
    SPCampaignsAPI,
    SPAdGroupsAPI,
    SPKeywordsAPI,
    SPTargetingAPI,
    SPBudgetRulesAPI,
    SPRecommendationsAPI,
)

# SB模块
from .sb import (
    SBCampaignsAPI,
    SBAdsAPI,
    SBKeywordsAPI,
    SBCreativesAPI,
)

# SD模块
from .sd import (
    SDCampaignsAPI,
    SDTargetingAPI,
    SDCreativesAPI,
)

# DSP模块
from .dsp import (
    DSPAudiencesAPI,
)

# Reporting模块
from .reporting import (
    ReportsV3API,
    BrandMetricsAPI,
)

# Accounts模块
from .accounts import (
    ProfilesAPI,
    PortfoliosAPI,
    BillingAPI,
)

# Common模块
from .common import (
    AttributionAPI,
    StoresAPI,
    AssetsAPI,
    HistoryAPI,
)

__version__ = "1.0.0"

__all__ = [
    # 版本
    "__version__",
    # 基础
    "BaseAdsClient",
    "AdsRegion",
    "AmazonAdsError",
    # 客户端
    "AmazonAdsClient",
    "AdsAPIClient",
    # SP
    "SPCampaignsAPI",
    "SPAdGroupsAPI",
    "SPKeywordsAPI",
    "SPTargetingAPI",
    "SPBudgetRulesAPI",
    "SPRecommendationsAPI",
    # SB
    "SBCampaignsAPI",
    "SBAdsAPI",
    "SBKeywordsAPI",
    "SBCreativesAPI",
    # SD
    "SDCampaignsAPI",
    "SDTargetingAPI",
    "SDCreativesAPI",
    # DSP
    "DSPAudiencesAPI",
    # Reporting
    "ReportsV3API",
    "BrandMetricsAPI",
    # Accounts
    "ProfilesAPI",
    "PortfoliosAPI",
    "BillingAPI",
    # Common
    "AttributionAPI",
    "StoresAPI",
    "AssetsAPI",
    "HistoryAPI",
]
