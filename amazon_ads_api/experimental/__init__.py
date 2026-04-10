"""
Amazon Ads API - Experimental APIs (L4)

⚠️ 警告: 实验性/Beta API

这些 API 可能：
- 处于 Beta 阶段
- 随时可能变更
- 没有稳定性保证
- 仅在特定区域可用
- 依赖 UI 行为

使用方式:
    # 必须显式确认风险
    exp = client.experimental(acknowledge_risk=True)
    exp.sponsored_tv.create_campaign(...)

包含:
- sponsored_tv: Sponsored TV (beta)
- moderation: Pre-moderation, Unified Moderation
- localization: Localization
- ad_library: Ad Library
- brand_home: Brand Home
"""

import warnings
from typing import TYPE_CHECKING

def _warn_experimental(api_name: str):
    """发出实验性 API 警告"""
    warnings.warn(
        f"'{api_name}' 是实验性 API (L4)，可能不稳定或随时变更。"
        "生产环境使用需谨慎。",
        UserWarning,
        stacklevel=3
    )

# Sponsored TV
from .sponsored_tv.campaigns import SponsoredTVCampaignsAPI
from .sponsored_tv.ad_groups import SponsoredTVAdGroupsAPI
from .sponsored_tv.ads import SponsoredTVAdsAPI
from .sponsored_tv.creatives import SponsoredTVCreativesAPI
from .sponsored_tv.targeting import SponsoredTVTargetingAPI

# Moderation
from .moderation.pre_moderation import PreModerationAPI
from .moderation.unified_moderation import UnifiedModerationAPI

# Localization
from .localization.localization import LocalizationAPI

# Ad Library
from .ad_library.ad_library import AdLibraryAPI

# Brand Home
from .brand_home.brand_home import BrandHomeAPI

__all__ = [
    "_warn_experimental",
    # Sponsored TV
    "SponsoredTVCampaignsAPI",
    "SponsoredTVAdGroupsAPI",
    "SponsoredTVAdsAPI",
    "SponsoredTVCreativesAPI",
    "SponsoredTVTargetingAPI",
    # Moderation
    "PreModerationAPI",
    "UnifiedModerationAPI",
    # Localization
    "LocalizationAPI",
    # Ad Library
    "AdLibraryAPI",
    # Brand Home
    "BrandHomeAPI",
]
