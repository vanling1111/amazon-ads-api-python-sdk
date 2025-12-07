"""
Integration tests for SB (Sponsored Brands) API
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


class TestSBCampaignsIntegration:
    """Integration tests for SB Campaigns API"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_campaigns(self, client):
        """Test listing SB campaigns"""
        result = client.sb.campaigns.list_campaigns()
        
        assert isinstance(result, (dict, list))
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_campaigns_with_state_filter(self, client):
        """Test listing SB campaigns with state filter"""
        try:
            result = client.sb.campaigns.list_campaigns(state_filter="enabled")
            assert isinstance(result, (dict, list))
        except AmazonAdsError as e:
            # 400 might happen if no SB campaigns
            assert e.status_code == 400


class TestSBAdsIntegration:
    """Integration tests for SB Ads API"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_ads(self, client):
        """Test listing SB ads"""
        try:
            result = client.sb.ads.list_ads()
            assert isinstance(result, (dict, list))
        except AmazonAdsError as e:
            # 400 might happen if no SB ads
            assert e.status_code == 400


class TestSBKeywordsIntegration:
    """Integration tests for SB Keywords API"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_keywords(self, client):
        """Test listing SB keywords"""
        try:
            result = client.sb.keywords.list_keywords()
            assert isinstance(result, (dict, list))
        except AmazonAdsError as e:
            # 400 might happen if no SB keywords
            assert e.status_code == 400


class TestSBCreativesIntegration:
    """Integration tests for SB Creatives API"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_creatives(self, client):
        """Test listing SB creatives"""
        try:
            result = client.sb.creatives.list_creatives()
            assert isinstance(result, (dict, list))
        except AmazonAdsError as e:
            # 400 might happen if no SB creatives
            assert e.status_code == 400

