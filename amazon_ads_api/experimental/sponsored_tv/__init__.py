"""Sponsored TV API - 电视广告"""

from .campaigns import SponsoredTVCampaignsAPI
from .ad_groups import SponsoredTVAdGroupsAPI
from .ads import SponsoredTVAdsAPI
from .creatives import SponsoredTVCreativesAPI
from .targeting import SponsoredTVTargetingAPI

__all__ = [
    "SponsoredTVCampaignsAPI",
    "SponsoredTVAdGroupsAPI",
    "SponsoredTVAdsAPI",
    "SponsoredTVCreativesAPI",
    "SponsoredTVTargetingAPI",
]

