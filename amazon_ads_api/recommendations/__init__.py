"""
Recommendations & Insights API 模块

官方文档: https://advertising.amazon.com/API/docs/en-us/guides/recommendations
"""

from .partner_opportunities import PartnerOpportunitiesAPI
from .tactical import TacticalRecommendationsAPI
from .persona_builder import PersonaBuilderAPI

__all__ = [
    "PartnerOpportunitiesAPI",
    "TacticalRecommendationsAPI",
    "PersonaBuilderAPI",
]

