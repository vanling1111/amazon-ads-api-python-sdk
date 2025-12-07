"""
Data Provider API 模块

官方文档: https://advertising.amazon.com/API/docs/en-us/data-provider
"""

from .metadata import DataProviderMetadataAPI
from .records import DataProviderRecordsAPI
from .hashed_records import HashedRecordsAPI

__all__ = [
    "DataProviderMetadataAPI",
    "DataProviderRecordsAPI",
    "HashedRecordsAPI",
]

