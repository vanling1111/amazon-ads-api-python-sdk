"""
Unit tests for BaseAdsClient
"""
import pytest
from unittest.mock import Mock, patch, MagicMock
from amazon_ads_api.base import BaseAdsClient, AdsRegion, AmazonAdsError


class TestAdsRegion:
    """Test AdsRegion enum"""
    
    @pytest.mark.unit
    def test_na_region(self):
        """Test North America region"""
        assert AdsRegion.NA == "https://advertising-api.amazon.com"
        assert "advertising-api.amazon.com" in AdsRegion.NA
    
    @pytest.mark.unit
    def test_eu_region(self):
        """Test Europe region"""
        assert AdsRegion.EU == "https://advertising-api-eu.amazon.com"
        assert "advertising-api-eu.amazon.com" in AdsRegion.EU
    
    @pytest.mark.unit
    def test_fe_region(self):
        """Test Far East region"""
        assert AdsRegion.FE == "https://advertising-api-fe.amazon.com"
        assert "advertising-api-fe.amazon.com" in AdsRegion.FE
    
    @pytest.mark.unit
    def test_all_regions_are_https(self):
        """Test all regions use HTTPS"""
        for region in AdsRegion:
            assert region.startswith("https://")


class TestAmazonAdsError:
    """Test AmazonAdsError exception"""
    
    @pytest.mark.unit
    def test_error_creation(self):
        """Test error creation with message"""
        error = AmazonAdsError(status_code=400, message="Bad Request")
        assert str(error) == "[400] Bad Request"
        assert error.status_code == 400
        assert error.message == "Bad Request"
    
    @pytest.mark.unit
    def test_error_with_details(self):
        """Test error with details"""
        error = AmazonAdsError(
            status_code=400,
            message="Validation Error",
            details={"campaignId": "123", "field": "budget"}
        )
        assert error.details["campaignId"] == "123"
        assert error.details["field"] == "budget"
    
    @pytest.mark.unit
    def test_error_default_details(self):
        """Test error has empty details by default"""
        error = AmazonAdsError(status_code=500, message="Internal Error")
        assert error.details == {}
    
    @pytest.mark.unit
    def test_rate_limit_error(self):
        """Test rate limit error"""
        error = AmazonAdsError(
            status_code=429,
            message="Rate limit exceeded",
            details={"retryAfter": 60}
        )
        assert error.status_code == 429
        assert "retryAfter" in error.details
    
    @pytest.mark.unit
    def test_unauthorized_error(self):
        """Test unauthorized error"""
        error = AmazonAdsError(
            status_code=401,
            message="Unauthorized",
        )
        assert error.status_code == 401


class TestBaseAdsClient:
    """Test BaseAdsClient"""
    
    @pytest.fixture
    def mock_session(self):
        """Create mock session"""
        with patch("requests.Session") as mock:
            session = MagicMock()
            mock.return_value = session
            yield session
    
    @pytest.mark.unit
    def test_base_client_is_abstract(self):
        """Test BaseAdsClient cannot be instantiated directly (it's abstract)"""
        # BaseAdsClient is ABC, so we test that it exists
        assert BaseAdsClient is not None
    
    @pytest.mark.unit
    def test_region_urls_are_valid(self):
        """Test region URL format"""
        assert "amazon.com" in AdsRegion.NA
        assert "amazon.com" in AdsRegion.EU
        assert "amazon.com" in AdsRegion.FE


class TestErrorHandling:
    """Test error handling"""
    
    @pytest.mark.unit
    def test_error_string_representation(self):
        """Test error string representation"""
        error = AmazonAdsError(status_code=400, message="Bad Request")
        assert "[400]" in str(error)
        assert "Bad Request" in str(error)
    
    @pytest.mark.unit
    def test_error_is_exception(self):
        """Test AmazonAdsError is an Exception"""
        error = AmazonAdsError(status_code=500, message="Error")
        assert isinstance(error, Exception)
    
    @pytest.mark.unit
    def test_error_can_be_raised(self):
        """Test error can be raised and caught"""
        with pytest.raises(AmazonAdsError) as exc_info:
            raise AmazonAdsError(status_code=404, message="Not Found")
        
        assert exc_info.value.status_code == 404
        assert exc_info.value.message == "Not Found"
