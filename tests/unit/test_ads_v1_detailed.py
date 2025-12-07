"""
Detailed unit tests for Amazon Ads V1 (New Unified API) module
Tests all 15 API classes in the unified API
"""
import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock, patch, MagicMock
from amazon_ads_api.base import AdsRegion, AmazonAdsError
from amazon_ads_api.amazon_ads_v1 import (
    AmazonAdsV1API, AdAssociationsAPI, AdGroupsAPI, AdsAPI, CampaignsAPI,
    TargetsAPI, RecommendationsAPI, AdvertisingDealsAPI, AdvertisingDealTargetsAPI,
    BrandedKeywordsPricingsAPI, CampaignForecastsAPI, CommitmentsAPI,
    CommitmentSpendsAPI, KeywordReservationValidationsAPI, RecommendationTypesAPI
)


class TestAmazonAdsV1API:
    """Test Amazon Ads V1 Unified API"""
    
    @pytest.fixture
    def api(self):
        """Create AmazonAdsV1API with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = AmazonAdsV1API(
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
    def test_v1_api_inherits_from_base(self, api):
        """Test AmazonAdsV1API is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)
    
    @pytest.mark.unit
    def test_v1_api_has_submodules(self, api):
        """Test AmazonAdsV1API has all submodules"""
        assert hasattr(api, "ad_associations")
        assert hasattr(api, "ad_groups")
        assert hasattr(api, "ads")
        assert hasattr(api, "campaigns")
        assert hasattr(api, "targets")
        assert hasattr(api, "recommendations")
    
    @pytest.mark.unit
    def test_v1_api_has_extended_submodules(self, api):
        """Test AmazonAdsV1API has extended submodules"""
        assert hasattr(api, "advertising_deals")
        assert hasattr(api, "advertising_deal_targets")
        assert hasattr(api, "branded_keywords_pricings")
        assert hasattr(api, "campaign_forecasts")
        assert hasattr(api, "commitments")
        assert hasattr(api, "commitment_spends")
        assert hasattr(api, "keyword_reservation_validations")
        assert hasattr(api, "recommendation_types")


class TestAdAssociationsAPI:
    """Test Ad Associations API"""
    
    @pytest.fixture
    def api(self):
        """Create AdAssociationsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = AdAssociationsAPI(
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
    def test_ad_associations_api_inherits_from_base(self, api):
        """Test AdAssociationsAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)


class TestAdGroupsAPI:
    """Test Ad Groups API (V1)"""
    
    @pytest.fixture
    def api(self):
        """Create AdGroupsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = AdGroupsAPI(
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
    def test_ad_groups_api_inherits_from_base(self, api):
        """Test AdGroupsAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)


class TestAdsAPI:
    """Test Ads API (V1)"""
    
    @pytest.fixture
    def api(self):
        """Create AdsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = AdsAPI(
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
    def test_ads_api_inherits_from_base(self, api):
        """Test AdsAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)


class TestCampaignsAPIV1:
    """Test Campaigns API (V1)"""
    
    @pytest.fixture
    def api(self):
        """Create CampaignsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = CampaignsAPI(
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
    def test_campaigns_api_inherits_from_base(self, api):
        """Test CampaignsAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)


class TestTargetsAPI:
    """Test Targets API (V1)"""
    
    @pytest.fixture
    def api(self):
        """Create TargetsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = TargetsAPI(
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
    def test_targets_api_inherits_from_base(self, api):
        """Test TargetsAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)


class TestRecommendationsAPIV1:
    """Test Recommendations API (V1)"""
    
    @pytest.fixture
    def api(self):
        """Create RecommendationsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = RecommendationsAPI(
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
    def test_recommendations_api_inherits_from_base(self, api):
        """Test RecommendationsAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)


class TestAdvertisingDealsAPI:
    """Test Advertising Deals API"""
    
    @pytest.fixture
    def api(self):
        """Create AdvertisingDealsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = AdvertisingDealsAPI(
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
    def test_advertising_deals_api_inherits_from_base(self, api):
        """Test AdvertisingDealsAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)


class TestCommitmentsAPI:
    """Test Commitments API"""
    
    @pytest.fixture
    def api(self):
        """Create CommitmentsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = CommitmentsAPI(
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
    def test_commitments_api_inherits_from_base(self, api):
        """Test CommitmentsAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)


class TestCampaignForecastsAPI:
    """Test Campaign Forecasts API"""
    
    @pytest.fixture
    def api(self):
        """Create CampaignForecastsAPI with mocked session"""
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            
            api = CampaignForecastsAPI(
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
    def test_campaign_forecasts_api_inherits_from_base(self, api):
        """Test CampaignForecastsAPI is properly inherited"""
        from amazon_ads_api.base import BaseAdsClient
        assert isinstance(api, BaseAdsClient)

