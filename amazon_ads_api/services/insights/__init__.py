"""
Insights API模块

官方文档: https://advertising.amazon.com/API/docs
OpenAPI规范: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Insights_prod_3p.json

⚠️ 官方 Insights API 只有一个端点:
   GET /insights/audiences/{audienceId}/overlappingAudiences

注意: keyword_insights.py 中的方法实际调用的是 SP/SB 的 keyword recommendations API，
      不是 Insights API。为了向后兼容保留在此模块中。
"""

from .keyword_insights import KeywordInsightsAPI
from .audience_insights import AudienceInsightsAPI

__all__ = ["KeywordInsightsAPI", "AudienceInsightsAPI"]
