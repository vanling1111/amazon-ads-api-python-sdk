"""
Sponsored Products API 模块

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod
"""

from .campaigns import SPCampaignsAPI
from .ad_groups import SPAdGroupsAPI
from .keywords import SPKeywordsAPI
from .targeting import SPTargetingAPI
from .budget_rules import SPBudgetRulesAPI
from .recommendations import SPRecommendationsAPI
from .theme_targeting import SPThemeTargetingAPI
from .campaign_optimization import SPCampaignOptimizationAPI
from .target_promotion_groups import SPTargetPromotionGroupsAPI
from .global_recommendations import SPGlobalRecommendationsAPI

__all__ = [
    "SPCampaignsAPI",
    "SPAdGroupsAPI",
    "SPKeywordsAPI",
    "SPTargetingAPI",
    "SPBudgetRulesAPI",
    "SPRecommendationsAPI",
    "SPThemeTargetingAPI",
    "SPCampaignOptimizationAPI",
    "SPTargetPromotionGroupsAPI",
    "SPGlobalRecommendationsAPI",
]
