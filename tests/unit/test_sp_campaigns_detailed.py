"""
Detailed unit tests for SP Campaigns API
Tests all methods, parameters, and responses
"""
import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock, patch, MagicMock
from amazon_ads_api.base import AdsRegion, AmazonAdsError
from amazon_ads_api.sp.campaigns import SPCampaignsAPI


class TestSPCampaignsListCampaigns:
    """Test list_campaigns method"""
    
    @pytest.fixture
    def api(self):
        """Create SPCampaignsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = SPCampaignsAPI(
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
    def test_list_campaigns_default_params(self, api):
        """Test list_campaigns with default parameters"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "campaigns": [
                {"campaignId": "123", "name": "Test Campaign", "state": "enabled"}
            ],
            "nextToken": None,
        }
        api.session.request.return_value = mock_response
        
        result = api.list_campaigns()
        
        call_args = api.session.request.call_args
        assert call_args.kwargs["method"] == "POST"
        assert "/sp/campaigns/list" in call_args.kwargs["url"]
        assert call_args.kwargs["json"]["maxResults"] == 100
        assert "campaigns" in result
    
    @pytest.mark.unit
    def test_list_campaigns_with_state_filter(self, api):
        """Test list_campaigns with state filter"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {"campaigns": [], "nextToken": None}
        api.session.request.return_value = mock_response
        
        api.list_campaigns(state_filter="enabled")
        
        call_args = api.session.request.call_args
        assert call_args.kwargs["json"]["stateFilter"] == "enabled"
    
    @pytest.mark.unit
    def test_list_campaigns_with_name_filter(self, api):
        """Test list_campaigns with name filter"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {"campaigns": [], "nextToken": None}
        api.session.request.return_value = mock_response
        
        api.list_campaigns(name_filter="Test")
        
        call_args = api.session.request.call_args
        assert call_args.kwargs["json"]["name"] == "Test"
    
    @pytest.mark.unit
    def test_list_campaigns_with_pagination(self, api):
        """Test list_campaigns with pagination token"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {"campaigns": [], "nextToken": "token2"}
        api.session.request.return_value = mock_response
        
        api.list_campaigns(next_token="token1")
        
        call_args = api.session.request.call_args
        assert call_args.kwargs["json"]["nextToken"] == "token1"
    
    @pytest.mark.unit
    def test_list_campaigns_with_max_results(self, api):
        """Test list_campaigns with custom max results"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {"campaigns": [], "nextToken": None}
        api.session.request.return_value = mock_response
        
        api.list_campaigns(max_results=50)
        
        call_args = api.session.request.call_args
        assert call_args.kwargs["json"]["maxResults"] == 50


class TestSPCampaignsGetCampaign:
    """Test get_campaign method"""
    
    @pytest.fixture
    def api(self):
        """Create SPCampaignsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = SPCampaignsAPI(
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
    def test_get_campaign_success(self, api):
        """Test get_campaign returns campaign details"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "campaignId": "123456789",
            "name": "Test Campaign",
            "state": "enabled",
            "dailyBudget": 100.0,
            "startDate": "20240101",
        }
        api.session.request.return_value = mock_response
        
        result = api.get_campaign("123456789")
        
        call_args = api.session.request.call_args
        assert call_args.kwargs["method"] == "GET"
        assert "/sp/campaigns/123456789" in call_args.kwargs["url"]
        assert result["campaignId"] == "123456789"
        assert result["name"] == "Test Campaign"
    
    @pytest.mark.unit
    def test_get_campaign_not_found(self, api):
        """Test get_campaign when campaign not found"""
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 404
        mock_response.text = '{"message": "Campaign not found"}'
        mock_response.json.return_value = {"message": "Campaign not found"}
        api.session.request.return_value = mock_response
        
        with pytest.raises(AmazonAdsError) as exc_info:
            api.get_campaign("nonexistent")
        
        assert exc_info.value.status_code == 404


class TestSPCampaignsCreateCampaigns:
    """Test create_campaigns method"""
    
    @pytest.fixture
    def api(self):
        """Create SPCampaignsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = SPCampaignsAPI(
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
    def test_create_campaigns_success(self, api):
        """Test create_campaigns successfully creates campaigns"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "campaigns": {
                "success": [{"campaignId": "123", "index": 0}],
                "error": [],
            }
        }
        api.session.request.return_value = mock_response
        
        campaigns = [
            {
                "name": "New Campaign",
                "targetingType": "MANUAL",
                "state": "enabled",
                "dailyBudget": 50.0,
                "startDate": "20240101",
                "bidding": {"strategy": "LEGACY_FOR_SALES"},
            }
        ]
        
        result = api.create_campaigns(campaigns)
        
        call_args = api.session.request.call_args
        assert call_args.kwargs["method"] == "POST"
        assert "/sp/campaigns" in call_args.kwargs["url"]
        assert call_args.kwargs["json"]["campaigns"] == campaigns
        assert len(result["campaigns"]["success"]) == 1
    
    @pytest.mark.unit
    def test_create_campaigns_with_errors(self, api):
        """Test create_campaigns handles partial errors"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "campaigns": {
                "success": [],
                "error": [
                    {
                        "index": 0,
                        "code": "INVALID_PARAMETER",
                        "message": "Invalid budget",
                    }
                ],
            }
        }
        api.session.request.return_value = mock_response
        
        result = api.create_campaigns([{"name": "Bad Campaign", "dailyBudget": -100}])
        
        assert len(result["campaigns"]["error"]) == 1
        assert result["campaigns"]["error"][0]["code"] == "INVALID_PARAMETER"


class TestSPCampaignsUpdateCampaigns:
    """Test update_campaigns method"""
    
    @pytest.fixture
    def api(self):
        """Create SPCampaignsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = SPCampaignsAPI(
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
    def test_update_campaigns_success(self, api):
        """Test update_campaigns successfully updates campaigns"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "campaigns": {
                "success": [{"campaignId": "123", "index": 0}],
                "error": [],
            }
        }
        api.session.request.return_value = mock_response
        
        result = api.update_campaigns([
            {"campaignId": "123", "state": "paused"}
        ])
        
        call_args = api.session.request.call_args
        assert call_args.kwargs["method"] == "PUT"


class TestSPCampaignsDeleteCampaign:
    """Test delete_campaign method"""
    
    @pytest.fixture
    def api(self):
        """Create SPCampaignsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = SPCampaignsAPI(
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
    def test_delete_campaign_success(self, api):
        """Test delete_campaign archives campaign"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 204
        api.session.request.return_value = mock_response
        
        result = api.delete_campaign("123456789")
        
        call_args = api.session.request.call_args
        assert call_args.kwargs["method"] == "DELETE"
        assert "/sp/campaigns/123456789" in call_args.kwargs["url"]


class TestSPCampaignsConvenienceMethods:
    """Test convenience methods"""
    
    @pytest.fixture
    def api(self):
        """Create SPCampaignsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = SPCampaignsAPI(
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
    def test_pause_campaign(self, api):
        """Test pause_campaign convenience method"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {"campaigns": {"success": [{"campaignId": "123"}], "error": []}}
        api.session.request.return_value = mock_response
        
        api.pause_campaign("123")
        
        call_args = api.session.request.call_args
        assert call_args.kwargs["json"]["campaigns"][0]["state"] == "paused"
    
    @pytest.mark.unit
    def test_enable_campaign(self, api):
        """Test enable_campaign convenience method"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {"campaigns": {"success": [{"campaignId": "123"}], "error": []}}
        api.session.request.return_value = mock_response
        
        api.enable_campaign("123")
        
        call_args = api.session.request.call_args
        assert call_args.kwargs["json"]["campaigns"][0]["state"] == "enabled"
    
    @pytest.mark.unit
    def test_update_budget(self, api):
        """Test update_budget convenience method"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {"campaigns": {"success": [{"campaignId": "123"}], "error": []}}
        api.session.request.return_value = mock_response
        
        api.update_budget("123", 150.0)
        
        call_args = api.session.request.call_args
        assert call_args.kwargs["json"]["campaigns"][0]["dailyBudget"] == 150.0


class TestSPCampaignsMultipleCampaigns:
    """Test operations with multiple campaigns"""
    
    @pytest.fixture
    def api(self):
        """Create SPCampaignsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = SPCampaignsAPI(
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
    def test_create_multiple_campaigns(self, api):
        """Test creating multiple campaigns at once"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "campaigns": {
                "success": [
                    {"campaignId": "1", "index": 0},
                    {"campaignId": "2", "index": 1},
                    {"campaignId": "3", "index": 2},
                ],
                "error": [],
            }
        }
        api.session.request.return_value = mock_response
        
        campaigns = [
            {"name": "Campaign 1", "targetingType": "MANUAL", "state": "enabled", "dailyBudget": 10.0},
            {"name": "Campaign 2", "targetingType": "AUTO", "state": "enabled", "dailyBudget": 20.0},
            {"name": "Campaign 3", "targetingType": "MANUAL", "state": "paused", "dailyBudget": 30.0},
        ]
        
        result = api.create_campaigns(campaigns)
        
        assert len(result["campaigns"]["success"]) == 3
    
    @pytest.mark.unit
    def test_update_multiple_campaigns(self, api):
        """Test updating multiple campaigns at once"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "campaigns": {
                "success": [
                    {"campaignId": "1", "index": 0},
                    {"campaignId": "2", "index": 1},
                ],
                "error": [],
            }
        }
        api.session.request.return_value = mock_response
        
        updates = [
            {"campaignId": "1", "state": "paused"},
            {"campaignId": "2", "dailyBudget": 100.0},
        ]
        
        result = api.update_campaigns(updates)
        
        call_args = api.session.request.call_args
        assert len(call_args.kwargs["json"]["campaigns"]) == 2

