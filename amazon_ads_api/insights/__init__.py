"""Insights API模块"""

from .category_insights import CategoryInsightsAPI
from .keyword_insights import KeywordInsightsAPI
from .audience_insights import AudienceInsightsAPI

__all__ = ["CategoryInsightsAPI", "KeywordInsightsAPI", "AudienceInsightsAPI"]

