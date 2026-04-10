"""Amazon Ads API v1 - 新统一API"""

from .unified_api import (
    AmazonAdsV1API,
    AdAssociationsAPI,
    AdGroupsAPI,
    AdsAPI,
    CampaignsAPI,
    TargetsAPI,
    AdExtensionsAPI,
    SBAdvertisingDealsAPI as AdvertisingDealsAPI,
    SBAdvertisingDealTargetsAPI as AdvertisingDealTargetsAPI,
    SBBrandedKeywordsPricingsAPI as BrandedKeywordsPricingsAPI,
    SBKeywordReservationValidationsAPI as KeywordReservationValidationsAPI,
    SBRecommendationsAPI as RecommendationsAPI,
    SBRecommendationTypesAPI as RecommendationTypesAPI,
    DSPCommitmentsAPI as CommitmentsAPI,
    DSPCommitmentSpendsAPI as CommitmentSpendsAPI,
    DSPCampaignForecastsAPI as CampaignForecastsAPI,
)

__all__ = [
    "AmazonAdsV1API",
    "AdAssociationsAPI",
    "AdGroupsAPI",
    "AdsAPI",
    "CampaignsAPI",
    "TargetsAPI",
    "AdExtensionsAPI",
    "RecommendationsAPI",
    "AdvertisingDealsAPI",
    "AdvertisingDealTargetsAPI",
    "BrandedKeywordsPricingsAPI",
    "CampaignForecastsAPI",
    "CommitmentsAPI",
    "CommitmentSpendsAPI",
    "KeywordReservationValidationsAPI",
    "RecommendationTypesAPI",
]
