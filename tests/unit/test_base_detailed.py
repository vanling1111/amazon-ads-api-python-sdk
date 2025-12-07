"""
Detailed unit tests for BaseAdsClient
Tests HTTP methods, authentication, error handling, rate limiting
"""
import pytest
import time
from datetime import datetime, timedelta
from unittest.mock import Mock, patch, MagicMock, PropertyMock
from amazon_ads_api.base import BaseAdsClient, AdsRegion, AmazonAdsError


class ConcreteAdsClient(BaseAdsClient):
    """Concrete implementation for testing"""
    pass


class TestTokenRefresh:
    """Test OAuth2 token refresh functionality"""
    
    @pytest.fixture
    def client(self):
        """Create client with mocked session"""
        with patch("requests.Session"):
            client = ConcreteAdsClient(
                client_id="test_client_id",
                client_secret="test_client_secret",
                refresh_token="test_refresh_token",
                region=AdsRegion.NA,
            )
            return client
    
    @pytest.mark.unit
    def test_refresh_token_success(self, client):
        """Test successful token refresh"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.json.return_value = {
            "access_token": "new_access_token",
            "expires_in": 3600,
        }
        
        with patch("requests.post", return_value=mock_response):
            token = client._refresh_access_token()
        
        assert token == "new_access_token"
        assert client._access_token == "new_access_token"
        assert client._token_expires_at is not None
    
    @pytest.mark.unit
    def test_refresh_token_failure(self, client):
        """Test token refresh failure"""
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 401
        mock_response.text = '{"error": "invalid_grant"}'
        mock_response.json.return_value = {"error": "invalid_grant"}
        
        with patch("requests.post", return_value=mock_response):
            with pytest.raises(AmazonAdsError) as exc_info:
                client._refresh_access_token()
        
        assert exc_info.value.status_code == 401
        assert "Failed to refresh token" in exc_info.value.message
    
    @pytest.mark.unit
    def test_get_access_token_when_none(self, client):
        """Test get_access_token refreshes when token is None"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.json.return_value = {
            "access_token": "new_token",
            "expires_in": 3600,
        }
        
        assert client._access_token is None
        
        with patch("requests.post", return_value=mock_response):
            token = client._get_access_token()
        
        assert token == "new_token"
    
    @pytest.mark.unit
    def test_get_access_token_when_expired(self, client):
        """Test get_access_token refreshes when token is expired"""
        client._access_token = "old_token"
        client._token_expires_at = datetime.now() - timedelta(minutes=5)  # Expired
        
        mock_response = Mock()
        mock_response.ok = True
        mock_response.json.return_value = {
            "access_token": "new_token",
            "expires_in": 3600,
        }
        
        with patch("requests.post", return_value=mock_response):
            token = client._get_access_token()
        
        assert token == "new_token"
    
    @pytest.mark.unit
    def test_get_access_token_when_valid(self, client):
        """Test get_access_token returns cached token when valid"""
        client._access_token = "valid_token"
        client._token_expires_at = datetime.now() + timedelta(hours=1)  # Valid
        
        # Should not call refresh
        with patch("requests.post") as mock_post:
            token = client._get_access_token()
            mock_post.assert_not_called()
        
        assert token == "valid_token"


class TestHeaders:
    """Test header construction"""
    
    @pytest.fixture
    def client(self):
        """Create client with valid token"""
        with patch("requests.Session"):
            client = ConcreteAdsClient(
                client_id="test_client_id",
                client_secret="test_client_secret",
                refresh_token="test_refresh_token",
                region=AdsRegion.NA,
            )
            client._access_token = "test_token"
            client._token_expires_at = datetime.now() + timedelta(hours=1)
            return client
    
    @pytest.mark.unit
    def test_headers_without_profile(self, client):
        """Test headers without profile ID"""
        headers = client._get_headers()
        
        assert "Authorization" in headers
        assert headers["Authorization"] == "Bearer test_token"
        assert headers["Amazon-Advertising-API-ClientId"] == "test_client_id"
        assert headers["Content-Type"] == "application/json"
        assert "Amazon-Advertising-API-Scope" not in headers
    
    @pytest.mark.unit
    def test_headers_with_profile(self, client):
        """Test headers with profile ID"""
        client.profile_id = "1234567890"
        headers = client._get_headers()
        
        assert headers["Amazon-Advertising-API-Scope"] == "1234567890"


class TestHTTPMethods:
    """Test HTTP request methods"""
    
    @pytest.fixture
    def client(self):
        """Create client with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            client = ConcreteAdsClient(
                client_id="test_client_id",
                client_secret="test_client_secret",
                refresh_token="test_refresh_token",
                region=AdsRegion.NA,
            )
            client._access_token = "test_token"
            client._token_expires_at = datetime.now() + timedelta(hours=1)
            client.session = mock_session
            return client
    
    @pytest.mark.unit
    def test_get_request(self, client):
        """Test GET request"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        client.session.request.return_value = mock_response
        
        result = client.get("/test/endpoint", params={"key": "value"})
        
        client.session.request.assert_called_once()
        call_args = client.session.request.call_args
        assert call_args.kwargs["method"] == "GET"
        assert "/test/endpoint" in call_args.kwargs["url"]
        assert call_args.kwargs["params"] == {"key": "value"}
        assert result == {"data": "test"}
    
    @pytest.mark.unit
    def test_post_request(self, client):
        """Test POST request"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {"created": True}
        client.session.request.return_value = mock_response
        
        result = client.post("/test/endpoint", json_data={"name": "test"})
        
        call_args = client.session.request.call_args
        assert call_args.kwargs["method"] == "POST"
        assert call_args.kwargs["json"] == {"name": "test"}
        assert result == {"created": True}
    
    @pytest.mark.unit
    def test_put_request(self, client):
        """Test PUT request"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {"updated": True}
        client.session.request.return_value = mock_response
        
        result = client.put("/test/endpoint", json_data={"state": "paused"})
        
        call_args = client.session.request.call_args
        assert call_args.kwargs["method"] == "PUT"
        assert result == {"updated": True}
    
    @pytest.mark.unit
    def test_delete_request(self, client):
        """Test DELETE request"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 204
        client.session.request.return_value = mock_response
        
        result = client.delete("/test/endpoint/123")
        
        call_args = client.session.request.call_args
        assert call_args.kwargs["method"] == "DELETE"
        assert result == {}
    
    @pytest.mark.unit
    def test_request_with_correct_url(self, client):
        """Test request constructs correct URL"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        client.session.request.return_value = mock_response
        
        client.get("/sp/campaigns")
        
        call_args = client.session.request.call_args
        expected_url = "https://advertising-api.amazon.com/sp/campaigns"
        assert call_args.kwargs["url"] == expected_url


class TestErrorHandling:
    """Test error handling"""
    
    @pytest.fixture
    def client(self):
        """Create client with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            client = ConcreteAdsClient(
                client_id="test_client_id",
                client_secret="test_client_secret",
                refresh_token="test_refresh_token",
                region=AdsRegion.NA,
            )
            client._access_token = "test_token"
            client._token_expires_at = datetime.now() + timedelta(hours=1)
            client.session = mock_session
            return client
    
    @pytest.mark.unit
    def test_400_bad_request(self, client):
        """Test 400 Bad Request error"""
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 400
        mock_response.text = '{"message": "Invalid parameter"}'
        mock_response.json.return_value = {"message": "Invalid parameter"}
        client.session.request.return_value = mock_response
        
        with pytest.raises(AmazonAdsError) as exc_info:
            client.get("/test")
        
        assert exc_info.value.status_code == 400
    
    @pytest.mark.unit
    def test_401_unauthorized(self, client):
        """Test 401 Unauthorized error"""
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 401
        mock_response.text = '{"message": "Unauthorized"}'
        mock_response.json.return_value = {"message": "Unauthorized"}
        client.session.request.return_value = mock_response
        
        with pytest.raises(AmazonAdsError) as exc_info:
            client.get("/test")
        
        assert exc_info.value.status_code == 401
    
    @pytest.mark.unit
    def test_403_forbidden(self, client):
        """Test 403 Forbidden error"""
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 403
        mock_response.text = '{"message": "Access denied"}'
        mock_response.json.return_value = {"message": "Access denied"}
        client.session.request.return_value = mock_response
        
        with pytest.raises(AmazonAdsError) as exc_info:
            client.get("/test")
        
        assert exc_info.value.status_code == 403
    
    @pytest.mark.unit
    def test_404_not_found(self, client):
        """Test 404 Not Found error"""
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 404
        mock_response.text = '{"message": "Resource not found"}'
        mock_response.json.return_value = {"message": "Resource not found"}
        client.session.request.return_value = mock_response
        
        with pytest.raises(AmazonAdsError) as exc_info:
            client.get("/campaigns/nonexistent")
        
        assert exc_info.value.status_code == 404
    
    @pytest.mark.unit
    def test_500_internal_server_error(self, client):
        """Test 500 Internal Server Error"""
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 500
        mock_response.text = '{"message": "Internal error"}'
        mock_response.json.return_value = {"message": "Internal error"}
        client.session.request.return_value = mock_response
        
        with pytest.raises(AmazonAdsError) as exc_info:
            client.get("/test")
        
        assert exc_info.value.status_code == 500


class TestRateLimiting:
    """Test rate limit handling"""
    
    @pytest.fixture
    def client(self):
        """Create client with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            client = ConcreteAdsClient(
                client_id="test_client_id",
                client_secret="test_client_secret",
                refresh_token="test_refresh_token",
                region=AdsRegion.NA,
            )
            client._access_token = "test_token"
            client._token_expires_at = datetime.now() + timedelta(hours=1)
            client.session = mock_session
            return client
    
    @pytest.mark.unit
    def test_429_rate_limit(self, client):
        """Test 429 Rate Limit error"""
        mock_response = Mock()
        mock_response.status_code = 429
        mock_response.headers = {"Retry-After": "5"}
        client.session.request.return_value = mock_response
        
        with patch("time.sleep"):
            with pytest.raises(AmazonAdsError) as exc_info:
                client.get("/test")
        
        assert exc_info.value.status_code == 429
        assert "retry_after" in exc_info.value.details


class TestReportDownload:
    """Test report download functionality"""
    
    @pytest.fixture
    def client(self):
        """Create client with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            client = ConcreteAdsClient(
                client_id="test_client_id",
                client_secret="test_client_secret",
                refresh_token="test_refresh_token",
                region=AdsRegion.NA,
            )
            client.session = mock_session
            return client
    
    @pytest.mark.unit
    def test_download_report_success(self, client):
        """Test successful report download"""
        import gzip
        import json
        
        test_data = [{"campaign": "test", "impressions": 100}]
        compressed = gzip.compress(json.dumps(test_data).encode())
        
        mock_response = Mock()
        mock_response.ok = True
        mock_response.content = compressed
        client.session.get.return_value = mock_response
        
        result = client.download_report("https://example.com/report.gz")
        
        assert result == test_data
    
    @pytest.mark.unit
    def test_download_report_failure(self, client):
        """Test report download failure"""
        mock_response = Mock()
        mock_response.ok = False
        client.session.get.return_value = mock_response
        
        result = client.download_report("https://example.com/report.gz")
        
        assert result == []
    
    @pytest.mark.unit
    def test_download_report_invalid_gzip(self, client):
        """Test report download with invalid gzip"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.content = b"not gzip data"
        client.session.get.return_value = mock_response
        
        result = client.download_report("https://example.com/report.gz")
        
        assert result == []


class TestWithProfile:
    """Test with_profile method"""
    
    @pytest.mark.unit
    def test_with_profile_sets_profile_id(self):
        """Test with_profile sets profile ID"""
        with patch("requests.Session"):
            client = ConcreteAdsClient(
                client_id="test",
                client_secret="test",
                refresh_token="test",
                region=AdsRegion.NA,
            )
        
        client.with_profile("1234567890")
        
        assert client.profile_id == "1234567890"
    
    @pytest.mark.unit
    def test_with_profile_returns_self(self):
        """Test with_profile returns self for chaining"""
        with patch("requests.Session"):
            client = ConcreteAdsClient(
                client_id="test",
                client_secret="test",
                refresh_token="test",
                region=AdsRegion.NA,
            )
        
        result = client.with_profile("1234567890")
        
        assert result is client
    
    @pytest.mark.unit
    def test_with_profile_chaining(self):
        """Test method chaining with with_profile"""
        with patch("requests.Session"):
            client = ConcreteAdsClient(
                client_id="test",
                client_secret="test",
                refresh_token="test",
                region=AdsRegion.NA,
            )
        
        # Should be able to chain
        result = client.with_profile("123").with_profile("456")
        assert result.profile_id == "456"

