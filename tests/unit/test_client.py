"""
Unit tests for AmazonAdsClient
"""
import pytest
from unittest.mock import Mock, patch, MagicMock
from amazon_ads_api import AmazonAdsClient, AdsRegion


class TestAmazonAdsClient:
    """Test AmazonAdsClient unified client"""
    
    @pytest.fixture
    def mock_session(self):
        """Create mock session"""
        with patch("requests.Session") as mock:
            session = MagicMock()
            # Mock token response
            token_response = MagicMock()
            token_response.json.return_value = {
                "access_token": "test_token",
                "expires_in": 3600,
            }
            token_response.ok = True
            session.post.return_value = token_response
            mock.return_value = session
            yield session
    
    @pytest.mark.unit
    def test_client_creation(self, mock_credentials, mock_session):
        """Test client creation"""
        client = AmazonAdsClient(
            client_id=mock_credentials["client_id"],
            client_secret=mock_credentials["client_secret"],
            refresh_token=mock_credentials["refresh_token"],
            region=AdsRegion.NA,
        )
        
        assert client is not None
    
    @pytest.mark.unit
    def test_sp_module_access(self, mock_credentials, mock_session):
        """Test SP module access"""
        client = AmazonAdsClient(
            client_id=mock_credentials["client_id"],
            client_secret=mock_credentials["client_secret"],
            refresh_token=mock_credentials["refresh_token"],
            region=AdsRegion.NA,
        )
        
        assert hasattr(client, "sp")
        assert hasattr(client.sp, "campaigns")
        assert hasattr(client.sp, "ad_groups")
        assert hasattr(client.sp, "keywords")
        assert hasattr(client.sp, "targeting")
    
    @pytest.mark.unit
    def test_sb_module_access(self, mock_credentials, mock_session):
        """Test SB module access"""
        client = AmazonAdsClient(
            client_id=mock_credentials["client_id"],
            client_secret=mock_credentials["client_secret"],
            refresh_token=mock_credentials["refresh_token"],
            region=AdsRegion.NA,
        )
        
        assert hasattr(client, "sb")
        assert hasattr(client.sb, "campaigns")
        assert hasattr(client.sb, "ads")
        assert hasattr(client.sb, "keywords")
    
    @pytest.mark.unit
    def test_sd_module_access(self, mock_credentials, mock_session):
        """Test SD module access"""
        client = AmazonAdsClient(
            client_id=mock_credentials["client_id"],
            client_secret=mock_credentials["client_secret"],
            refresh_token=mock_credentials["refresh_token"],
            region=AdsRegion.NA,
        )
        
        assert hasattr(client, "sd")
        assert hasattr(client.sd, "campaigns")
        assert hasattr(client.sd, "targeting")
    
    @pytest.mark.unit
    def test_dsp_module_access(self, mock_credentials, mock_session):
        """Test DSP module access"""
        client = AmazonAdsClient(
            client_id=mock_credentials["client_id"],
            client_secret=mock_credentials["client_secret"],
            refresh_token=mock_credentials["refresh_token"],
            region=AdsRegion.NA,
        )
        
        assert hasattr(client, "dsp")
        assert hasattr(client.dsp, "audiences")
        assert hasattr(client.dsp, "orders")
        assert hasattr(client.dsp, "line_items")
    
    @pytest.mark.unit
    def test_reporting_module_access(self, mock_credentials, mock_session):
        """Test Reporting module access"""
        client = AmazonAdsClient(
            client_id=mock_credentials["client_id"],
            client_secret=mock_credentials["client_secret"],
            refresh_token=mock_credentials["refresh_token"],
            region=AdsRegion.NA,
        )
        
        assert hasattr(client, "reporting")
        assert hasattr(client.reporting, "reports")
        assert hasattr(client.reporting, "brand_metrics")
    
    @pytest.mark.unit
    def test_accounts_module_access(self, mock_credentials, mock_session):
        """Test Accounts module access"""
        client = AmazonAdsClient(
            client_id=mock_credentials["client_id"],
            client_secret=mock_credentials["client_secret"],
            refresh_token=mock_credentials["refresh_token"],
            region=AdsRegion.NA,
        )
        
        assert hasattr(client, "accounts")
        assert hasattr(client.accounts, "profiles")
        assert hasattr(client.accounts, "portfolios")
    
    @pytest.mark.unit
    def test_amc_module_access(self, mock_credentials, mock_session):
        """Test AMC module access"""
        client = AmazonAdsClient(
            client_id=mock_credentials["client_id"],
            client_secret=mock_credentials["client_secret"],
            refresh_token=mock_credentials["refresh_token"],
            region=AdsRegion.NA,
        )
        
        assert hasattr(client, "amc")
        assert hasattr(client.amc, "queries")
        assert hasattr(client.amc, "audiences")
    
    @pytest.mark.unit
    def test_ads_v1_module_access(self, mock_credentials, mock_session):
        """Test Amazon Ads V1 module access"""
        client = AmazonAdsClient(
            client_id=mock_credentials["client_id"],
            client_secret=mock_credentials["client_secret"],
            refresh_token=mock_credentials["refresh_token"],
            region=AdsRegion.NA,
        )
        
        assert hasattr(client, "ads_v1")
    
    @pytest.mark.unit
    def test_all_direct_modules(self, mock_credentials, mock_session):
        """Test all direct module access"""
        client = AmazonAdsClient(
            client_id=mock_credentials["client_id"],
            client_secret=mock_credentials["client_secret"],
            refresh_token=mock_credentials["refresh_token"],
            region=AdsRegion.NA,
        )
        
        direct_modules = [
            "eligibility", "locations", "exports", "manager_accounts",
            "posts", "product_metadata", "audiences_discovery", "ads_v1",
            "ad_library", "brand_home", "localization", "ads_data_manager",
            "brand_associations"
        ]
        
        for module in direct_modules:
            assert hasattr(client, module), f"Missing module: {module}"


class TestClientChaining:
    """Test method chaining"""
    
    @pytest.fixture
    def mock_session(self):
        """Create mock session"""
        with patch("requests.Session") as mock:
            session = MagicMock()
            token_response = MagicMock()
            token_response.json.return_value = {
                "access_token": "test_token",
                "expires_in": 3600,
            }
            token_response.ok = True
            session.post.return_value = token_response
            mock.return_value = session
            yield session
    
    @pytest.mark.unit
    def test_with_profile_chaining(self, mock_credentials, mock_session):
        """Test with_profile returns self for chaining"""
        client = AmazonAdsClient(
            client_id=mock_credentials["client_id"],
            client_secret=mock_credentials["client_secret"],
            refresh_token=mock_credentials["refresh_token"],
            region=AdsRegion.NA,
        )
        
        result = client.with_profile("123456")
        assert result is client


class TestModuleLazyLoading:
    """Test lazy loading of modules"""
    
    @pytest.fixture
    def mock_session(self):
        """Create mock session"""
        with patch("requests.Session") as mock:
            session = MagicMock()
            token_response = MagicMock()
            token_response.json.return_value = {
                "access_token": "test_token",
                "expires_in": 3600,
            }
            token_response.ok = True
            session.post.return_value = token_response
            mock.return_value = session
            yield session
    
    @pytest.mark.unit
    def test_lazy_loading(self, mock_credentials, mock_session):
        """Test that modules are lazily loaded"""
        client = AmazonAdsClient(
            client_id=mock_credentials["client_id"],
            client_secret=mock_credentials["client_secret"],
            refresh_token=mock_credentials["refresh_token"],
            region=AdsRegion.NA,
        )
        
        # First access should create the module
        sp1 = client.sp
        # Second access should return the same instance
        sp2 = client.sp
        assert sp1 is sp2


class TestClientModuleCount:
    """Test client has expected number of modules"""
    
    @pytest.fixture
    def mock_session(self):
        """Create mock session"""
        with patch("requests.Session") as mock:
            session = MagicMock()
            token_response = MagicMock()
            token_response.json.return_value = {
                "access_token": "test_token",
                "expires_in": 3600,
            }
            token_response.ok = True
            session.post.return_value = token_response
            mock.return_value = session
            yield session
    
    @pytest.mark.unit
    def test_main_module_groups(self, mock_credentials, mock_session):
        """Test main module groups exist"""
        client = AmazonAdsClient(
            client_id=mock_credentials["client_id"],
            client_secret=mock_credentials["client_secret"],
            refresh_token=mock_credentials["refresh_token"],
            region=AdsRegion.NA,
        )
        
        main_modules = ["sp", "sb", "sd", "dsp", "reporting", "accounts", 
                        "common", "insights", "recommendations", "data_provider",
                        "moderation", "amc", "st", "ras", "media_planning", "stream"]
        
        for module in main_modules:
            assert hasattr(client, module), f"Missing main module: {module}"
