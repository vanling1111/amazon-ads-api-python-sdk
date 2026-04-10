"""
Pytest 配置和共享 fixtures

提供测试所需的 mock 对象和辅助函数
"""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from typing import Any, Dict

# 配置 pytest-asyncio
pytest_plugins = ('pytest_asyncio',)


# ============ Mock Responses ============

MOCK_PROFILE = {
    "profileId": 123456789,
    "countryCode": "US",
    "currencyCode": "USD",
    "dailyBudget": 1000.0,
    "timezone": "America/Los_Angeles",
    "accountInfo": {
        "marketplaceStringId": "ATVPDKIKX0DER",
        "id": "ENTITY123",
        "type": "seller",
        "name": "Test Account",
        "validPaymentMethod": True
    }
}

MOCK_CAMPAIGN = {
    "campaignId": "campaign123",
    "name": "Test Campaign",
    "state": "enabled",
    "budget": 100.0,
    "budgetType": "DAILY",
    "startDate": "2024-01-01"
}

MOCK_AD_GROUP = {
    "adGroupId": "adgroup123",
    "campaignId": "campaign123",
    "name": "Test Ad Group",
    "state": "enabled",
    "defaultBid": 1.0
}

MOCK_KEYWORD = {
    "keywordId": "keyword123",
    "campaignId": "campaign123",
    "adGroupId": "adgroup123",
    "state": "enabled",
    "keywordText": "test keyword",
    "matchType": "BROAD",
    "bid": 0.75
}

MOCK_REPORT = {
    "reportId": "report123",
    "status": "COMPLETED",
    "url": "https://example.com/report.json"
}


# ============ Fixtures ============

@pytest.fixture
def mock_http_response():
    """创建 mock HTTP 响应"""
    def _create_response(data: Any, status_code: int = 200):
        response = MagicMock()
        response.status_code = status_code
        response.json.return_value = data
        response.text = str(data)
        return response
    return _create_response


@pytest.fixture
def mock_async_client():
    """创建 mock 异步客户端"""
    client = AsyncMock()
    return client


@pytest.fixture
def mock_credentials():
    """测试凭证"""
    return {
        "client_id": "test_client_id",
        "client_secret": "test_client_secret",
        "refresh_token": "test_refresh_token",
        "profile_id": "123456789",
        "region": "NA"
    }


@pytest.fixture
def mock_profile():
    """Mock Profile 数据"""
    return MOCK_PROFILE.copy()


@pytest.fixture
def mock_campaign():
    """Mock Campaign 数据"""
    return MOCK_CAMPAIGN.copy()


@pytest.fixture
def mock_ad_group():
    """Mock Ad Group 数据"""
    return MOCK_AD_GROUP.copy()


@pytest.fixture
def mock_keyword():
    """Mock Keyword 数据"""
    return MOCK_KEYWORD.copy()


@pytest.fixture
def mock_report():
    """Mock Report 数据"""
    return MOCK_REPORT.copy()


# ============ Test Helpers ============

class MockResponse:
    """Mock HTTP Response 类"""
    
    def __init__(self, data: Any, status_code: int = 200):
        self.data = data
        self.status_code = status_code
        self._json = data
    
    async def json(self):
        return self._json
    
    async def text(self):
        return str(self.data)
    
    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception(f"HTTP Error: {self.status_code}")


def create_mock_api_client(response_data: Any, status_code: int = 200):
    """创建返回指定数据的 mock API 客户端"""
    async def mock_request(*args, **kwargs):
        return MockResponse(response_data, status_code)
    
    client = AsyncMock()
    client.get = mock_request
    client.post = mock_request
    client.put = mock_request
    client.delete = mock_request
    client.patch = mock_request
    
    return client


# ============ Test Categories ============

def pytest_configure(config):
    """注册自定义 markers"""
    config.addinivalue_line(
        "markers", "unit: 单元测试 - 不需要网络"
    )
    config.addinivalue_line(
        "markers", "integration: 集成测试 - 需要真实凭证"
    )
    config.addinivalue_line(
        "markers", "e2e: 端到端测试 - 完整流程"
    )
    config.addinivalue_line(
        "markers", "slow: 慢速测试"
    )
