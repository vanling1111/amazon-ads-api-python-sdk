"""
Detailed unit tests for DSP module
Tests DSP Audiences, Orders, Line Items, and Creatives
"""
import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock, patch, MagicMock
from amazon_ads_api.base import AdsRegion, AmazonAdsError
from amazon_ads_api.dsp import (
    DSPAudiencesAPI, DSPAdvertisersAPI, DSPOrdersAPI, DSPLineItemsAPI,
    DSPCreativesAPI, DSPInventoryAPI, DSPMeasurementAPI
)


class TestDSPAudiencesAPI:
    """Test DSP Audiences API"""
    
    @pytest.fixture
    def api(self):
        """Create DSPAudiencesAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = DSPAudiencesAPI(
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
    def test_audiences_api_inherits_from_base(self, api):
        """Test DSPAudiencesAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)
    
    @pytest.mark.unit
    def test_audiences_api_has_session(self, api):
        """Test DSPAudiencesAPI has session"""
        assert api.session is not None


class TestDSPAdvertisersAPI:
    """Test DSP Advertisers API"""
    
    @pytest.fixture
    def api(self):
        """Create DSPAdvertisersAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = DSPAdvertisersAPI(
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
    def test_advertisers_api_inherits_from_base(self, api):
        """Test DSPAdvertisersAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)


class TestDSPOrdersAPI:
    """Test DSP Orders API"""
    
    @pytest.fixture
    def api(self):
        """Create DSPOrdersAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = DSPOrdersAPI(
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
    def test_orders_api_inherits_from_base(self, api):
        """Test DSPOrdersAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)


class TestDSPLineItemsAPI:
    """Test DSP Line Items API"""
    
    @pytest.fixture
    def api(self):
        """Create DSPLineItemsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = DSPLineItemsAPI(
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
    def test_line_items_api_inherits_from_base(self, api):
        """Test DSPLineItemsAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)


class TestDSPCreativesAPI:
    """Test DSP Creatives API"""
    
    @pytest.fixture
    def api(self):
        """Create DSPCreativesAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = DSPCreativesAPI(
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
    def test_creatives_api_inherits_from_base(self, api):
        """Test DSPCreativesAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)


class TestDSPInventoryAPI:
    """Test DSP Inventory API"""
    
    @pytest.fixture
    def api(self):
        """Create DSPInventoryAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = DSPInventoryAPI(
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
    def test_inventory_api_inherits_from_base(self, api):
        """Test DSPInventoryAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)


class TestDSPMeasurementAPI:
    """Test DSP Measurement API"""
    
    @pytest.fixture
    def api(self):
        """Create DSPMeasurementAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = DSPMeasurementAPI(
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
    def test_measurement_api_inherits_from_base(self, api):
        """Test DSPMeasurementAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)

