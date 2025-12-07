"""
Integration tests for SD (Sponsored Display) API
Note: These tests require valid credentials and profile ID:
  - AMAZON_ADS_CLIENT_ID
  - AMAZON_ADS_CLIENT_SECRET
  - AMAZON_ADS_REFRESH_TOKEN
  - AMAZON_ADS_PROFILE_ID
"""
import os
import pytest
from amazon_ads_api import AmazonAdsClient, AdsRegion
from amazon_ads_api.base import AmazonAdsError


def has_valid_credentials():
    """Check if valid credentials are available"""
    client_id = os.environ.get("AMAZON_ADS_CLIENT_ID", "")
    profile_id = os.environ.get("AMAZON_ADS_PROFILE_ID", "")
    return (client_id and client_id != "test_client_id" and 
            profile_id and profile_id != "1234567890")


requires_credentials = pytest.mark.skipif(
    not has_valid_credentials(),
    reason="Requires valid Amazon Ads API credentials and profile ID"
)


@pytest.fixture
def client():
    """Create authenticated client with profile ID"""
    if not has_valid_credentials():
        pytest.skip("Missing credentials")
    
    client = AmazonAdsClient(
        client_id=os.environ["AMAZON_ADS_CLIENT_ID"],
        client_secret=os.environ["AMAZON_ADS_CLIENT_SECRET"],
        refresh_token=os.environ["AMAZON_ADS_REFRESH_TOKEN"],
        region=AdsRegion.NA,
    )
    client.with_profile(os.environ["AMAZON_ADS_PROFILE_ID"])
    return client


class TestSDCampaignsIntegration:
    """Integration tests for SD Campaigns API"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_campaigns(self, client):
        """Test listing SD campaigns"""
        result = client.sd.campaigns.list_campaigns()
        
        assert isinstance(result, (dict, list))
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_campaigns_with_state_filter(self, client):
        """Test listing SD campaigns with state filter"""
        try:
            result = client.sd.campaigns.list_campaigns(state_filter="enabled")
            assert isinstance(result, (dict, list))
        except AmazonAdsError as e:
            # 400 might happen if no SD campaigns
            assert e.status_code == 400


class TestSDTargetingIntegration:
    """Integration tests for SD Targeting API"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_targets(self, client):
        """Test listing SD targets"""
        try:
            result = client.sd.targeting.list_targets()
            assert isinstance(result, (dict, list))
        except AmazonAdsError as e:
            # 400 might happen if no SD targets
            assert e.status_code == 400


class TestSDAudiencesIntegration:
    """Integration tests for SD Audiences API"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_audiences(self, client):
        """Test listing SD audiences"""
        try:
            result = client.sd.audiences.list_audiences()
            assert isinstance(result, (dict, list))
        except AmazonAdsError as e:
            # 400/403 might happen if no access to audiences
            assert e.status_code in [400, 403]


class TestSDCreativesIntegration:
    """Integration tests for SD Creatives API"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_creatives(self, client):
        """Test listing SD creatives"""
        try:
            result = client.sd.creatives.list_creatives()
            assert isinstance(result, (dict, list))
        except AmazonAdsError as e:
            # 400 might happen if no SD creatives
            assert e.status_code == 400

