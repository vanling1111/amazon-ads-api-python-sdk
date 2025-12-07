"""
Amazon Marketing Cloud (AMC) API 模块

官方文档: https://advertising.amazon.com/API/docs/en-us/amc
"""

from .queries import AMCQueriesAPI
from .audiences import AMCAudiencesAPI
from .workflows import AMCWorkflowsAPI

__all__ = [
    "AMCQueriesAPI",
    "AMCAudiencesAPI",
    "AMCWorkflowsAPI",
]

