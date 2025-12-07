"""
Detailed unit tests for Reporting module
Tests Reports V3, Brand Metrics, Stores Analytics
"""
import pytest
import gzip
import json
from datetime import datetime, timedelta
from unittest.mock import Mock, patch, MagicMock
from amazon_ads_api.base import AdsRegion, AmazonAdsError
from amazon_ads_api.reporting import ReportsV3API, BrandMetricsAPI, StoresAnalyticsAPI


class TestReportsV3API:
    """Test Reports V3 API"""
    
    @pytest.fixture
    def api(self):
        """Create ReportsV3API with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = ReportsV3API(
                client_id="test_client_id",
                client_secret="test_client_secret",
                refresh_token="test_refresh_token",
                region=AdsRegion.NA,
            )
            api._access_token = "test_token"
            api._token_expires_at = datetime.now() + timedelta(hours=1)
            api.session = mock_session
            api.profile_id = "1234567890"
            return api
    
    @pytest.mark.unit
    def test_reports_api_inherits_from_base(self, api):
        """Test ReportsV3API is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)
    
    @pytest.mark.unit
    def test_reports_api_has_correct_base_url(self, api):
        """Test ReportsV3API uses correct base URL"""
        assert api.base_url == "https://advertising-api.amazon.com"


class TestBrandMetricsAPI:
    """Test Brand Metrics API"""
    
    @pytest.fixture
    def api(self):
        """Create BrandMetricsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = BrandMetricsAPI(
                client_id="test_client_id",
                client_secret="test_client_secret",
                refresh_token="test_refresh_token",
                region=AdsRegion.NA,
            )
            api._access_token = "test_token"
            api._token_expires_at = datetime.now() + timedelta(hours=1)
            api.session = mock_session
            api.profile_id = "1234567890"
            return api
    
    @pytest.mark.unit
    def test_brand_metrics_api_inherits_from_base(self, api):
        """Test BrandMetricsAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)


class TestStoresAnalyticsAPI:
    """Test Stores Analytics API"""
    
    @pytest.fixture
    def api(self):
        """Create StoresAnalyticsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = StoresAnalyticsAPI(
                client_id="test_client_id",
                client_secret="test_client_secret",
                refresh_token="test_refresh_token",
                region=AdsRegion.NA,
            )
            api._access_token = "test_token"
            api._token_expires_at = datetime.now() + timedelta(hours=1)
            api.session = mock_session
            api.profile_id = "1234567890"
            return api
    
    @pytest.mark.unit
    def test_stores_analytics_api_inherits_from_base(self, api):
        """Test StoresAnalyticsAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)

