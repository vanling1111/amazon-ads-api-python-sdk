"""
Recommendations API 模块

官方文档: https://advertising.amazon.com/API/docs
OpenAPI规范: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Recommendations_prod_3p.json

官方端点 (共3个):
- POST /recommendations/apply - 应用推荐
- POST /recommendations/list - 列出推荐
- PUT /recommendations/{recommendationId} - 更新推荐
"""

from .recommendations import RecommendationsAPI

__all__ = ["RecommendationsAPI"]
