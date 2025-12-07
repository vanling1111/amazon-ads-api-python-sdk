"""
Pytest Configuration and Shared Fixtures
"""
import os
import pytest
from unittest.mock import Mock, patch, MagicMock
from typing import Dict, Any


# ============ Mock Response Class ============

class MockResponse:
    """Mock HTTP Response for testing"""
    
    def __init__(
        self,
        json_data: Dict[str, Any] | list | None = None,
        status_code: int = 200,
        text: str = "",
        content: bytes = b"",
    ):
        self._json_data = json_data
        self.status_code = status_code
        self.text = text
        self.content = content
        self.ok = 200 <= status_code < 300
        self.headers = {"Content-Type": "application/json"}
    
    def json(self):
        return self._json_data
    
    def raise_for_status(self):
        if not self.ok:
            raise Exception(f"HTTP Error: {self.status_code}")


# ============ Fixtures ============

@pytest.fixture
def mock_credentials():
    """Mock API credentials"""
    return {
        "client_id": "test_client_id",
        "client_secret": "test_client_secret",
        "refresh_token": "test_refresh_token",
        "profile_id": "1234567890",
    }


@pytest.fixture
def mock_token_response():
    """Mock OAuth token response"""
    return MockResponse(
        json_data={
            "access_token": "test_access_token_12345",
            "token_type": "Bearer",
            "expires_in": 3600,
            "refresh_token": "test_refresh_token",
        }
    )


@pytest.fixture
def mock_profiles_response():
    """Mock profiles list response"""
    return MockResponse(
        json_data=[
            {
                "profileId": "1234567890",
                "countryCode": "US",
                "currencyCode": "USD",
                "timezone": "America/Los_Angeles",
                "accountInfo": {
                    "marketplaceStringId": "ATVPDKIKX0DER",
                    "id": "ENTITYID123",
                    "type": "seller",
                    "name": "Test Seller",
                },
            }
        ]
    )


@pytest.fixture
def mock_campaigns_response():
    """Mock campaigns list response"""
    return MockResponse(
        json_data={
            "campaigns": [
                {
                    "campaignId": "123456789",
                    "name": "Test Campaign 1",
                    "state": "enabled",
                    "budget": 100.0,
                    "budgetType": "daily",
                    "startDate": "20240101",
                },
                {
                    "campaignId": "987654321",
                    "name": "Test Campaign 2",
                    "state": "paused",
                    "budget": 50.0,
                    "budgetType": "daily",
                    "startDate": "20240115",
                },
            ],
            "totalResults": 2,
        }
    )


@pytest.fixture
def mock_ad_groups_response():
    """Mock ad groups list response"""
    return MockResponse(
        json_data={
            "adGroups": [
                {
                    "adGroupId": "111111111",
                    "campaignId": "123456789",
                    "name": "Test Ad Group 1",
                    "state": "enabled",
                    "defaultBid": 1.0,
                },
            ],
            "totalResults": 1,
        }
    )


@pytest.fixture
def mock_keywords_response():
    """Mock keywords list response"""
    return MockResponse(
        json_data={
            "keywords": [
                {
                    "keywordId": "222222222",
                    "adGroupId": "111111111",
                    "campaignId": "123456789",
                    "keywordText": "test keyword",
                    "matchType": "broad",
                    "state": "enabled",
                    "bid": 0.75,
                },
            ],
            "totalResults": 1,
        }
    )


@pytest.fixture
def mock_report_response():
    """Mock report creation response"""
    return MockResponse(
        json_data={
            "reportId": "report_123456",
            "status": "IN_PROGRESS",
        }
    )


@pytest.fixture
def mock_report_status_response():
    """Mock report status response"""
    return MockResponse(
        json_data={
            "reportId": "report_123456",
            "status": "COMPLETED",
            "url": "https://example.com/report.json.gz",
        }
    )


@pytest.fixture
def mock_session():
    """Mock requests session"""
    with patch("requests.Session") as mock:
        session = MagicMock()
        mock.return_value = session
        yield session


@pytest.fixture
def mock_httpx_client():
    """Mock httpx client"""
    with patch("httpx.Client") as mock:
        client = MagicMock()
        mock.return_value = client
        yield client


# ============ Environment Setup ============

@pytest.fixture(scope="session", autouse=True)
def setup_test_env():
    """Setup test environment variables"""
    os.environ.setdefault("AMAZON_ADS_CLIENT_ID", "test_client_id")
    os.environ.setdefault("AMAZON_ADS_CLIENT_SECRET", "test_client_secret")
    os.environ.setdefault("AMAZON_ADS_REFRESH_TOKEN", "test_refresh_token")
    os.environ.setdefault("AMAZON_ADS_PROFILE_ID", "1234567890")


# ============ Skip Markers ============

def pytest_configure(config):
    """Configure custom markers"""
    config.addinivalue_line("markers", "unit: Unit tests")
    config.addinivalue_line("markers", "integration: Integration tests")
    config.addinivalue_line("markers", "slow: Slow tests")


# ============ Helper Functions ============

def create_mock_response(data, status=200):
    """Helper to create mock responses"""
    return MockResponse(json_data=data, status_code=status)

