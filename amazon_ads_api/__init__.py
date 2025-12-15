"""
Amazon Ads API Python SDK - v2 分级架构

API 分级体系:
- L1 (Core): OpenAPI 验证，生产可用 - core/
- L2 (Reference): 官方文档确认 - reference/
- L3 (Services): 产品级聚合 - services/
- L4 (Experimental): Beta/实验性 - experimental/

使用示例:
    from amazon_ads_api import AmazonAdsClient
    
    client = AmazonAdsClient(
        client_id="xxx",
        client_secret="xxx",
        refresh_token="xxx",
        profile_id="123456789"
    )
    
    # L1: 默认访问（最安全）
    campaigns = await client.sp.campaigns.list_campaigns()
    
    # L2: 显式命名空间
    result = await client.reference.amc.run_query(...)
    
    # L3: 服务层
    report = await client.services.reporting.create_report(...)
    
    # L4: 需确认风险
    exp = client.experimental(acknowledge_risk=True)
    await exp.sponsored_tv.create_campaign(...)

详细文档:
- API_TIER.md - 分级规则详解
- API_CLASSIFICATION.md - 335 个 API 分级列表
- README.md - 快速开始指南
"""

__version__ = "2.0.0"
__author__ = "Amazon Ads SDK Team"

# 主入口
from .client import AmazonAdsClient

# 基础类型
from .base import (
    BaseAdsClient,
    AdsRegion,
    ProfileID,
    AmazonAdsError,
)

# 导出所有公共 API
__all__ = [
    # 版本信息
    "__version__",
    "__author__",
    # 主入口
    "AmazonAdsClient",
    # 基础类型
    "BaseAdsClient",
    "AdsRegion",
    "ProfileID",
    "AmazonAdsError",
]
