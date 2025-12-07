"""
Detailed unit tests for AMC (Amazon Marketing Cloud) module
Tests Queries, Audiences, and Workflows
"""
import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock, patch, MagicMock
from amazon_ads_api.base import AdsRegion, AmazonAdsError
from amazon_ads_api.amc import AMCQueriesAPI, AMCAudiencesAPI, AMCWorkflowsAPI


class TestAMCQueriesAPI:
    """Test AMC Queries API"""
    
    @pytest.fixture
    def api(self):
        """Create AMCQueriesAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = AMCQueriesAPI(
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
    def test_queries_api_inherits_from_base(self, api):
        """Test AMCQueriesAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)
    
    @pytest.mark.unit
    def test_queries_api_has_session(self, api):
        """Test AMCQueriesAPI has session"""
        assert api.session is not None
    
    @pytest.mark.unit
    def test_queries_api_profile_id(self, api):
        """Test AMCQueriesAPI profile ID"""
        assert api.profile_id == "1234567890"


class TestAMCAudiencesAPI:
    """Test AMC Audiences API"""
    
    @pytest.fixture
    def api(self):
        """Create AMCAudiencesAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = AMCAudiencesAPI(
                client_id="test_client_id",
                client_secret="test_client_secret",
                refresh_token="test_refresh_token",
                region=AdsRegion.NA,
            )
            api._access_token = "test_token"
            api._token_expires_at = datetime.now() + timedelta(hours=1)
            api.session = mock_session
            return api
    
    @pytest.mark.unit
    def test_audiences_api_inherits_from_base(self, api):
        """Test AMCAudiencesAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)


class TestAMCWorkflowsAPI:
    """Test AMC Workflows API"""
    
    @pytest.fixture
    def api(self):
        """Create AMCWorkflowsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = AMCWorkflowsAPI(
                client_id="test_client_id",
                client_secret="test_client_secret",
                refresh_token="test_refresh_token",
                region=AdsRegion.NA,
            )
            api._access_token = "test_token"
            api._token_expires_at = datetime.now() + timedelta(hours=1)
            api.session = mock_session
            return api
    
    @pytest.mark.unit
    def test_workflows_api_inherits_from_base(self, api):
        """Test AMCWorkflowsAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)

