"""
Amazon DSP API 模块

官方文档: https://advertising.amazon.com/API/docs/en-us/reference/api-overview
OpenAPI 规范: https://advertising.amazon.com/API/docs/en-us/reference/openapi-download

官方端点统计:
- Advertisers: 2 个端点 (只读)
- Campaigns/AdGroups: 6 个端点
- Audiences: 1 个端点
- Target KPI: 1 个端点
- Measurement: 30 个端点
- Conversions: 17 个端点
- 总计: 57 个端点
"""

from .advertisers import DSPAdvertisersAPI
from .audiences import DSPAudiencesAPI
from .campaigns import DSPCampaignsAPI
from .conversions import DSPConversionsAPI
from .measurement import DSPMeasurementAPI
from .target_kpi import DSPTargetKPIAPI

__all__ = [
    "DSPAdvertisersAPI",
    "DSPAudiencesAPI",
    "DSPCampaignsAPI",
    "DSPConversionsAPI",
    "DSPMeasurementAPI",
    "DSPTargetKPIAPI",
]
