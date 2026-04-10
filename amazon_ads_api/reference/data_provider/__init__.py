"""
Data Provider API 模块

官方文档: 
- Record management: https://advertising.amazon.com/API/docs/en-us/data-provider/openapi
- Hashed records: https://advertising.amazon.com/API/docs/en-us/data-provider/hashed-records

验证日期: 2024-12-15

官方端点 (共5个):
- POST /v2/dp/audiencemetadata/ - 创建受众
- GET /v2/dp/audiencemetadata/{audienceId} - 获取受众
- PUT /v2/dp/audiencemetadata/{audienceId} - 更新受众
- PATCH /v2/dp/audience - 关联/取消关联记录
- POST /dp/records/hashed - 上传哈希记录
"""

from .audience_metadata import AudienceMetadataAPI
from .hashed_records import HashedRecordsAPI

__all__ = [
    "AudienceMetadataAPI",
    "HashedRecordsAPI",
]
