"""
Amazon Marketing Cloud (AMC) API 模块

官方文档:
- AMC Administration: https://advertising.amazon.com/API/docs/en-us/amc-administration
- AMC Reporting: https://advertising.amazon.com/API/docs/en-us/amc-reporting
- AMC Rule-Based Audiences: https://advertising.amazon.com/API/docs/en-us/amc-rba

官方端点统计:
- Administration: 21 端点
- Reporting: 17 端点
- Audiences: 6 端点
- 总计: 44 端点
"""

from .administration import AMCAdministrationAPI
from .reporting import AMCReportingAPI
from .audiences import AMCAudiencesAPI

__all__ = [
    "AMCAdministrationAPI",
    "AMCReportingAPI",
    "AMCAudiencesAPI",
]
