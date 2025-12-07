"""
Integration tests for DSP API
Note: These tests require valid DSP credentials and advertiser ID:
  - AMAZON_ADS_CLIENT_ID
  - AMAZON_ADS_CLIENT_SECRET
  - AMAZON_ADS_REFRESH_TOKEN
  - AMAZON_DSP_ADVERTISER_ID
"""
import os
import pytest
from amazon_ads_api import AmazonAdsClient, AdsRegion
from amazon_ads_api.base import AmazonAdsError


def has_dsp_credentials():
    """Check if valid DSP credentials are available"""
    client_id = os.environ.get("AMAZON_ADS_CLIENT_ID", "")
    advertiser_id = os.environ.get("AMAZON_DSP_ADVERTISER_ID", "")
    return (client_id and client_id != "test_client_id" and advertiser_id)


requires_dsp_credentials = pytest.mark.skipif(
    not has_dsp_credentials(),
    reason="Requires valid Amazon DSP credentials and advertiser ID"
)


@pytest.fixture
def dsp_client():
    """Create authenticated client for DSP"""
    if not has_dsp_credentials():
        pytest.skip("Missing DSP credentials")
    
    client = AmazonAdsClient(
        client_id=os.environ["AMAZON_ADS_CLIENT_ID"],
        client_secret=os.environ["AMAZON_ADS_CLIENT_SECRET"],
        refresh_token=os.environ["AMAZON_ADS_REFRESH_TOKEN"],
        region=AdsRegion.NA,
    )
    return client


class TestDSPAdvertisersIntegration:
    """Integration tests for DSP Advertisers API"""
    
    @requires_dsp_credentials
    @pytest.mark.integration
    def test_list_advertisers(self, dsp_client):
        """Test listing DSP advertisers"""
        result = dsp_client.dsp.advertisers.list_advertisers()
        
        assert isinstance(result, (dict, list))


class TestDSPOrdersIntegration:
    """Integration tests for DSP Orders API"""
    
    @requires_dsp_credentials
    @pytest.mark.integration
    def test_list_orders(self, dsp_client):
        """Test listing DSP orders"""
        advertiser_id = os.environ["AMAZON_DSP_ADVERTISER_ID"]
        
        result = dsp_client.dsp.orders.list_orders(advertiser_id=advertiser_id)
        
        assert isinstance(result, (dict, list))


class TestDSPAudiencesIntegration:
    """Integration tests for DSP Audiences API"""
    
    @requires_dsp_credentials
    @pytest.mark.integration
    def test_list_audiences(self, dsp_client):
        """Test listing DSP audiences"""
        advertiser_id = os.environ["AMAZON_DSP_ADVERTISER_ID"]
        
        try:
            result = dsp_client.dsp.audiences.list_audiences(advertiser_id=advertiser_id)
            assert isinstance(result, (dict, list))
        except AmazonAdsError as e:
            # 400 is expected if no audiences exist
            assert e.status_code in [400, 404]

