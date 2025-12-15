"""
Sponsored Display API 模块

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi
"""

from .campaigns import SDCampaignsAPI
from .targeting import SDTargetingAPI
from .creatives import SDCreativesAPI
from .audiences import SDAudiencesAPI
from .moderation import SDModerationAPI
from .optimization import SDOptimizationAPI
from .brand_safety import SDBrandSafetyAPI
from .locations import SDLocationsAPI
from .reports import SDReportsAPI

__all__ = [
    "SDCampaignsAPI",
    "SDTargetingAPI",
    "SDCreativesAPI",
    "SDAudiencesAPI",
    "SDModerationAPI",
    "SDOptimizationAPI",
    "SDBrandSafetyAPI",
    "SDLocationsAPI",
    "SDReportsAPI",
]
