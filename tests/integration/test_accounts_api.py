"""
Integration tests for Accounts API (Profiles, Portfolios, Billing)
Note: These tests require valid credentials:
  - AMAZON_ADS_CLIENT_ID
  - AMAZON_ADS_CLIENT_SECRET
  - AMAZON_ADS_REFRESH_TOKEN
  - AMAZON_ADS_PROFILE_ID (optional for some tests)
"""
import os
import pytest
from amazon_ads_api import AmazonAdsClient, AdsRegion
from amazon_ads_api.base import AmazonAdsError


def has_valid_credentials():
    """Check if valid credentials are available"""
    client_id = os.environ.get("AMAZON_ADS_CLIENT_ID", "")
    return client_id and client_id != "test_client_id"


def has_profile_id():
    """Check if profile ID is available"""
    profile_id = os.environ.get("AMAZON_ADS_PROFILE_ID", "")
    return profile_id and profile_id != "1234567890"


requires_credentials = pytest.mark.skipif(
    not has_valid_credentials(),
    reason="Requires valid Amazon Ads API credentials"
)

requires_profile = pytest.mark.skipif(
    not has_profile_id(),
    reason="Requires AMAZON_ADS_PROFILE_ID"
)


@pytest.fixture
def client():
    """Create authenticated client"""
    if not has_valid_credentials():
        pytest.skip("Missing credentials")
    
    client = AmazonAdsClient(
        client_id=os.environ["AMAZON_ADS_CLIENT_ID"],
        client_secret=os.environ["AMAZON_ADS_CLIENT_SECRET"],
        refresh_token=os.environ["AMAZON_ADS_REFRESH_TOKEN"],
        region=AdsRegion.NA,
    )
    return client


@pytest.fixture
def client_with_profile():
    """Create authenticated client with profile ID"""
    if not has_valid_credentials() or not has_profile_id():
        pytest.skip("Missing credentials or profile ID")
    
    client = AmazonAdsClient(
        client_id=os.environ["AMAZON_ADS_CLIENT_ID"],
        client_secret=os.environ["AMAZON_ADS_CLIENT_SECRET"],
        refresh_token=os.environ["AMAZON_ADS_REFRESH_TOKEN"],
        region=AdsRegion.NA,
    )
    client.with_profile(os.environ["AMAZON_ADS_PROFILE_ID"])
    return client


class TestProfilesIntegration:
    """Integration tests for Profiles API"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_profiles(self, client):
        """Test listing all profiles"""
        profiles = client.accounts.profiles.list_profiles()
        
        assert isinstance(profiles, list)
        
        # Verify structure if profiles exist
        if len(profiles) > 0:
            profile = profiles[0]
            assert "profileId" in profile
            assert "countryCode" in profile
            assert "currencyCode" in profile
    
    @requires_credentials
    @requires_profile
    @pytest.mark.integration
    def test_get_profile(self, client):
        """Test getting a specific profile"""
        profile_id = os.environ["AMAZON_ADS_PROFILE_ID"]
        
        profile = client.accounts.profiles.get_profile(profile_id)
        
        assert isinstance(profile, dict)
        assert str(profile.get("profileId")) == profile_id
    
    @requires_credentials
    @pytest.mark.integration
    def test_get_nonexistent_profile(self, client):
        """Test getting a profile that doesn't exist"""
        with pytest.raises(AmazonAdsError) as exc_info:
            client.accounts.profiles.get_profile("9999999999999")
        
        assert exc_info.value.status_code in [400, 403, 404]


class TestPortfoliosIntegration:
    """Integration tests for Portfolios API"""
    
    @requires_credentials
    @requires_profile
    @pytest.mark.integration
    def test_list_portfolios(self, client_with_profile):
        """Test listing portfolios"""
        result = client_with_profile.accounts.portfolios.list_portfolios()
        
        assert isinstance(result, (dict, list))
    
    @requires_credentials
    @requires_profile
    @pytest.mark.integration
    def test_list_portfolios_with_state_filter(self, client_with_profile):
        """Test listing portfolios with state filter"""
        try:
            result = client_with_profile.accounts.portfolios.list_portfolios(state_filter="enabled")
            assert isinstance(result, (dict, list))
        except AmazonAdsError as e:
            # 400 might happen if API doesn't support filter
            assert e.status_code == 400


class TestBillingIntegration:
    """Integration tests for Billing API"""
    
    @requires_credentials
    @requires_profile
    @pytest.mark.integration
    def test_get_billing_status(self, client_with_profile):
        """Test getting billing status"""
        try:
            result = client_with_profile.accounts.billing.get_billing_status()
            assert isinstance(result, dict)
        except AmazonAdsError as e:
            # 403/404 might happen if no billing access
            assert e.status_code in [400, 403, 404]


class TestAccountBudgetsIntegration:
    """Integration tests for Account Budgets API"""
    
    @requires_credentials
    @requires_profile
    @pytest.mark.integration
    def test_list_budgets(self, client_with_profile):
        """Test listing account budgets"""
        try:
            result = client_with_profile.accounts.budgets.list_budgets()
            assert isinstance(result, (dict, list))
        except AmazonAdsError as e:
            # 403/404 might happen if no budget access
            assert e.status_code in [400, 403, 404]

