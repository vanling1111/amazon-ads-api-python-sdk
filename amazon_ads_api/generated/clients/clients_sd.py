"""Auto-generated async API client. Do not edit manually.

Source: SponsoredDisplay_prod_3p.json
Title:  Sponsored Display
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_sd import *  # noqa: F403
except ImportError:
    pass


class SdClient(BaseAdsClient):
    """Auto-generated from SponsoredDisplay_prod_3p.json (22 operations)"""

    async def delete_brand_safety_deny_list(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """DELETE /sd/brandSafety/deny

        Archives all of the domains in the Brand Safety Deny List. It can take several hours from the time a domain is deleted t
        """
        endpoint = "/sd/brandSafety/deny"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.delete(endpoint, params=params)

    async def list_domains(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None) -> JSONData | JSONList:
        """GET /sd/brandSafety/deny

        Gets a list of websites/apps that are on the advertiser's Brand Safety Deny List.
        """
        endpoint = "/sd/brandSafety/deny"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        return await self.get(endpoint, params=params)

    async def create_brand_safety_deny_list_domains(self, body: SDBrandSafetyPostRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/brandSafety/deny

        Creates one or more domains to add to a Brand Safety Deny List. The Brand Safety Deny List is at the advertiser level. I
        """
        endpoint = "/sd/brandSafety/deny"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def list_request_status(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/brandSafety/status

        List status of all requests
        """
        endpoint = "/sd/brandSafety/status"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def get_request_results(self, request_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, start_index: str | None = None, count: str | None = None) -> JSONData | JSONList:
        """GET /sd/brandSafety/{requestId}/results

        Gets the results for the given request
        """
        endpoint = f"/sd/brandSafety/{request_id}/results"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if start_index is not None:
            params["startIndex"] = start_index
        if count is not None:
            params["count"] = count
        return await self.get(endpoint, params=params)

    async def get_request_status(self, request_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/brandSafety/{requestId}/status

        Gets the status of the given request
        """
        endpoint = f"/sd/brandSafety/{request_id}/status"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def get_sd_budget_rules_for_advertiser(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, next_token: str | None = None, page_size: str | None = None) -> JSONData | JSONList:
        """GET /sd/budgetRules

        Get all budget rules created by an advertiser
        """
        endpoint = "/sd/budgetRules"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if next_token is not None:
            params["nextToken"] = next_token
        if page_size is not None:
            params["pageSize"] = page_size
        return await self.get(endpoint, params=params)

    async def create_budget_rules_for_sd_campaigns(self, body: CreateSDBudgetRulesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/budgetRules

        Creates one or more budget rules.
        """
        endpoint = "/sd/budgetRules"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def update_budget_rules_for_sd_campaigns(self, body: UpdateSDBudgetRulesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /sd/budgetRules

        Update one or more budget rules.
        """
        endpoint = "/sd/budgetRules"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params)

    async def get_budget_rule_by_rule_id_for_sd_campaigns(self, budget_rule_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/budgetRules/{budgetRuleId}

        Gets a budget rule specified by identifier.
        """
        endpoint = f"/sd/budgetRules/{budget_rule_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def get_campaigns_associated_with_sd_budget_rule(self, budget_rule_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, next_token: str | None = None, page_size: str | None = None) -> JSONData | JSONList:
        """GET /sd/budgetRules/{budgetRuleId}/campaigns

        Gets all the campaigns associated with a budget rule
        """
        endpoint = f"/sd/budgetRules/{budget_rule_id}/campaigns"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if next_token is not None:
            params["nextToken"] = next_token
        if page_size is not None:
            params["pageSize"] = page_size
        return await self.get(endpoint, params=params)

    async def sd_campaigns_budget_usage(self, body: BudgetUsageCampaignRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/campaigns/budget/usage

        Budget usage API for SD campaigns
        """
        endpoint = "/sd/campaigns/budget/usage"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sdcampaignbudgetusage.v1+json")

    async def get_sd_budget_recommendations(self, body: SDBudgetRecommendationsRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /sd/campaigns/budgetRecommendations

        Returns recommended daily budget and estimated missed opportunities for campaigns
        """
        endpoint = "/sd/campaigns/budgetRecommendations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sdbudgetrecommendations.v3+json")

    async def list_associated_budget_rules_for_sd_campaigns(self, campaign_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/campaigns/{campaignId}/budgetRules

        Gets a list of budget rules associated to a campaign specified by identifier.
        """
        endpoint = f"/sd/campaigns/{campaign_id}/budgetRules"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def create_associated_budget_rules_for_sd_campaigns(self, campaign_id: str, body: CreateAssociatedBudgetRulesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/campaigns/{campaignId}/budgetRules

        Associates one or more budget rules to a campaign specified by identifer.
        """
        endpoint = f"/sd/campaigns/{campaign_id}/budgetRules"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def disassociate_associated_budget_rule_for_sd_campaigns(self, campaign_id: str, budget_rule_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """DELETE /sd/campaigns/{campaignId}/budgetRules/{budgetRuleId}

        Disassociates a budget rule specified by identifier from a campaign specified by identifier.
        """
        endpoint = f"/sd/campaigns/{campaign_id}/budgetRules/{budget_rule_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.delete(endpoint, params=params)

    async def get_headline_recommendations_for_sd(self, body: SDHeadlineRecommendationRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/recommendations/creative/headline

        You can use this Sponsored Display API to retrieve creative headline recommendations from an array of ASINs.  **Requires
        """
        endpoint = "/sd/recommendations/creative/headline"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sdheadlinerecommendationrequest.v4.0+json")

    async def get_snapshot_by_id(self, snapshot_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/snapshots/{snapshotId}

        **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign_view']
        """
        endpoint = f"/sd/snapshots/{snapshot_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def download_snapshot_by_id(self, snapshot_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sd/snapshots/{snapshotId}/download

        **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign_view']
        """
        endpoint = f"/sd/snapshots/{snapshot_id}/download"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def get_target_bid_recommendations(self, body: SDTargetingBidRecommendationsRequestV31 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/targets/bid/recommendations

        Returns a set of bid recommendations for targeting clauses
        """
        endpoint = "/sd/targets/bid/recommendations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sdtargetingrecommendations.v3.1+json")

    async def get_target_recommendations(self, body: SDTargetingRecommendationsRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, locale: str | None = None) -> JSONData | JSONList:
        """POST /sd/targets/recommendations

        Returns a set of recommended products and categories to target
        """
        endpoint = "/sd/targets/recommendations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if locale is not None:
            params["locale"] = locale
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sdtargetingrecommendations.v3.0+json")

    async def create_snapshot(self, record_type: str, body: SnapshotRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sd/{recordType}/snapshot

        **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign_view']
        """
        endpoint = f"/sd/{record_type}/snapshot"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

