"""
Unit tests for SP (Sponsored Products) module
"""
import pytest
from unittest.mock import Mock, patch, MagicMock
from amazon_ads_api import AmazonAdsClient, AdsRegion
from amazon_ads_api.sp import (
    SPCampaignsAPI, SPAdGroupsAPI, SPKeywordsAPI, SPTargetingAPI,
    SPBudgetRulesAPI, SPRecommendationsAPI, SPProductEligibilityAPI,
    SPThemeTargetingAPI
)


class TestSPCampaignsAPI:
    """Test SP Campaigns API"""
    
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
    def test_campaigns_api_exists(self, mock_credentials, mock_session):
        """Test SPCampaignsAPI class exists"""
        assert SPCampaignsAPI is not None
    
    @pytest.mark.unit
    def test_campaigns_accessible_via_client(self, mock_credentials, mock_session):
        """Test campaigns accessible via client.sp.campaigns"""
        client = AmazonAdsClient(
            client_id=mock_credentials["client_id"],
            client_secret=mock_credentials["client_secret"],
            refresh_token=mock_credentials["refresh_token"],
            region=AdsRegion.NA,
        )
        
        assert hasattr(client.sp, "campaigns")
        assert client.sp.campaigns is not None


class TestSPAdGroupsAPI:
    """Test SP Ad Groups API"""
    
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
    def test_ad_groups_api_exists(self):
        """Test SPAdGroupsAPI class exists"""
        assert SPAdGroupsAPI is not None
    
    @pytest.mark.unit
    def test_ad_groups_accessible_via_client(self, mock_credentials, mock_session):
        """Test ad_groups accessible via client.sp.ad_groups"""
        client = AmazonAdsClient(
            client_id=mock_credentials["client_id"],
            client_secret=mock_credentials["client_secret"],
            refresh_token=mock_credentials["refresh_token"],
            region=AdsRegion.NA,
        )
        
        assert hasattr(client.sp, "ad_groups")


class TestSPKeywordsAPI:
    """Test SP Keywords API"""
    
    @pytest.mark.unit
    def test_keywords_api_exists(self):
        """Test SPKeywordsAPI class exists"""
        assert SPKeywordsAPI is not None


class TestSPTargetingAPI:
    """Test SP Targeting API"""
    
    @pytest.mark.unit
    def test_targeting_api_exists(self):
        """Test SPTargetingAPI class exists"""
        assert SPTargetingAPI is not None


class TestSPBudgetRulesAPI:
    """Test SP Budget Rules API"""
    
    @pytest.mark.unit
    def test_budget_rules_api_exists(self):
        """Test SPBudgetRulesAPI class exists"""
        assert SPBudgetRulesAPI is not None


class TestSPRecommendationsAPI:
    """Test SP Recommendations API"""
    
    @pytest.mark.unit
    def test_recommendations_api_exists(self):
        """Test SPRecommendationsAPI class exists"""
        assert SPRecommendationsAPI is not None


class TestSPProductEligibilityAPI:
    """Test SP Product Eligibility API"""
    
    @pytest.mark.unit
    def test_product_eligibility_api_exists(self):
        """Test SPProductEligibilityAPI class exists"""
        assert SPProductEligibilityAPI is not None


class TestSPThemeTargetingAPI:
    """Test SP Theme Targeting API"""
    
    @pytest.mark.unit
    def test_theme_targeting_api_exists(self):
        """Test SPThemeTargetingAPI class exists"""
        assert SPThemeTargetingAPI is not None


class TestSPModuleIntegrity:
    """Test SP module integrity"""
    
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
    def test_all_sp_submodules(self, mock_credentials, mock_session):
        """Test all SP submodules are accessible"""
        client = AmazonAdsClient(
            client_id=mock_credentials["client_id"],
            client_secret=mock_credentials["client_secret"],
            refresh_token=mock_credentials["refresh_token"],
            region=AdsRegion.NA,
        )
        
        sp_submodules = [
            "campaigns", "ad_groups", "keywords", "targeting",
            "budget_rules", "recommendations", "product_eligibility",
            "theme_targeting"
        ]
        
        for submodule in sp_submodules:
            assert hasattr(client.sp, submodule), f"Missing SP submodule: {submodule}"

