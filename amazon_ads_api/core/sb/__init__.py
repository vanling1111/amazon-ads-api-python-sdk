"""
Sponsored Brands API 模块

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi
"""

from .campaigns import SBCampaignsAPI
from .ads import SBAdsAPI
from .keywords import SBKeywordsAPI
from .creatives import SBCreativesAPI
from .brand_video import SBBrandVideoAPI
from .moderation import SBModerationAPI
from .optimization import SBOptimizationAPI
from .forecasts import SBForecastsAPI
from .targeting import SBTargetingAPI
from .legacy_migration import SBLegacyMigrationAPI

__all__ = [
    "SBCampaignsAPI",
    "SBAdsAPI",
    "SBKeywordsAPI",
    "SBCreativesAPI",
    "SBBrandVideoAPI",
    "SBModerationAPI",
    "SBOptimizationAPI",
    "SBForecastsAPI",
    "SBTargetingAPI",
    "SBLegacyMigrationAPI",
]
