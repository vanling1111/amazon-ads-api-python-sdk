"""
Amazon Ads API - Reference APIs (L2)

官方文档确认但不在 OpenAPI 目录中的 API。
可信度较高，需要显式命名空间访问。

使用方式:
    from amazon_ads_api.reference.amc import AMCQueriesAPI
    
或通过 Client:
    client.reference.amc.run_query(...)

包含:
- amc: Amazon Marketing Cloud (AMC)
- stream: Amazon Marketing Stream
- retail_ad_service: Retail Ad Service
- attribution: Amazon Attribution (从 common 迁移)
- posts: Posts API
- unified_api: Amazon Ads API v1
- data_provider: Data Provider
"""

# AMC
from .amc.administration import AMCAdministrationAPI
from .amc.reporting import AMCReportingAPI
from .amc.audiences import AMCAudiencesAPI

# Stream
from .stream.subscriptions import MarketingStreamAPI

# Retail Ad Service
from .retail_ad_service.campaigns import RASCampaignsAPI
from .retail_ad_service.ad_groups import RASAdGroupsAPI
from .retail_ad_service.product_ads import RASProductAdsAPI
from .retail_ad_service.targets import RASTargetsAPI

# Posts
from .posts.posts import PostsAPI

# Data Provider
from .data_provider.audience_metadata import AudienceMetadataAPI
from .data_provider.hashed_records import HashedRecordsAPI

# Unified API (Amazon Ads v1)
from .unified_api.unified_api import AmazonAdsV1API

__all__ = [
    # AMC
    "AMCAdministrationAPI",
    "AMCReportingAPI",
    "AMCAudiencesAPI",
    # Stream
    "MarketingStreamAPI",
    # Retail Ad Service
    "RASCampaignsAPI",
    "RASAdGroupsAPI",
    "RASProductAdsAPI",
    "RASTargetsAPI",
    # Posts
    "PostsAPI",
    # Data Provider
    "AudienceMetadataAPI",
    "HashedRecordsAPI",
    # Unified API
    "AmazonAdsV1API",
]
