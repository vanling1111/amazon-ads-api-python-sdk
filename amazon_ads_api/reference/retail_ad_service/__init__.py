"""Retail Ad Service API - 零售广告服务"""

from .campaigns import RASCampaignsAPI
from .ad_groups import RASAdGroupsAPI
from .product_ads import RASProductAdsAPI
from .targets import RASTargetsAPI

__all__ = [
    "RASCampaignsAPI",
    "RASAdGroupsAPI",
    "RASProductAdsAPI",
    "RASTargetsAPI",
]

