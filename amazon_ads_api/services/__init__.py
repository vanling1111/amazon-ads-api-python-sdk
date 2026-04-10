"""
Amazon Ads API - Service APIs (L3)

产品级聚合 API，提供便捷的高层抽象。

使用方式:
    from amazon_ads_api.services.reporting import ReportsV3API
    
或通过 Client:
    client.services.reporting.create_report(...)

包含:
- reporting: Reports v3, Brand Metrics, MMM, Stores Analytics
- insights: Audience Insights, Keyword Insights
- recommendations: Recommendations
- common: Assets, History, Stores, Attribution
- media_planning: Reach Forecasting
- brand_associations: Brand Associations
- ads_data_manager: Ads Data Manager
"""

# Reporting
from .reporting.reports_v3 import ReportsV3API
from .reporting.brand_metrics import BrandMetricsAPI
from .reporting.mmm import MarketingMixModelingAPI
from .reporting.stores_analytics import StoresAnalyticsAPI

# Insights
from .insights.audience_insights import AudienceInsightsAPI
from .insights.keyword_insights import KeywordInsightsAPI

# Recommendations
from .recommendations.recommendations import RecommendationsAPI

# Common
from .common.assets import AssetsAPI
from .common.history import HistoryAPI
from .common.stores import StoresAPI
from .common.attribution import AttributionAPI

# Media Planning
from .media_planning.reach_forecasting import ReachForecastingAPI

# Brand Associations
from .brand_associations.brand_associations import BrandAssociationsAPI

# Ads Data Manager
from .ads_data_manager.ads_data_manager import AdsDataManagerAPI

__all__ = [
    # Reporting
    "ReportsV3API",
    "BrandMetricsAPI",
    "MarketingMixModelingAPI",
    "StoresAnalyticsAPI",
    # Insights
    "AudienceInsightsAPI",
    "KeywordInsightsAPI",
    # Recommendations
    "RecommendationsAPI",
    # Common
    "AssetsAPI",
    "HistoryAPI",
    "StoresAPI",
    "AttributionAPI",
    # Media Planning
    "ReachForecastingAPI",
    # Brand Associations
    "BrandAssociationsAPI",
    # Ads Data Manager
    "AdsDataManagerAPI",
]
