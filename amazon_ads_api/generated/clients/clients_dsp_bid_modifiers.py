"""Auto-generated async API client. Do not edit manually.

Source: BidModifiers_prod_3p.json
Title:  Bid Modifiers
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_dsp_bid_modifiers import *  # noqa: F403
except ImportError:
    pass


class DspBidModifiersClient(BaseAdsClient):
    """Auto-generated from BidModifiers_prod_3p.json (7 operations)"""

    async def create_bid_modifier_rule(self, body: BidModifiersServiceCreateBidModifierRuleRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/rules/bidmodifier

        Creates a bid adjustment rule and returns a unique ID which can be used to associate the bid adjustment rule with adgrou
        """
        endpoint = "/dsp/rules/bidmodifier"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspbidmodifier.v1+json")

    async def list_bid_modifier_rules(self, body: BidModifiersServiceListBidModifierRulesRequestContent | dict[str, Any] | None = None, active: str | None = None, include_rule_expression: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/rules/bidmodifier/list

        Returns a list of active bid adjustment rule(s) belonging to the specified Ads AccountId. You can use a single adGroupId
        """
        endpoint = "/dsp/rules/bidmodifier/list"
        params: dict[str, Any] = {}
        if active is not None:
            params["active"] = active
        if include_rule_expression is not None:
            params["includeRuleExpression"] = include_rule_expression
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspbidmodifier.v1+json")

    async def delete_bid_modifier_rule(self, bid_modifier_rule_id: str, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """DELETE /dsp/rules/bidmodifier/{bidModifierRuleId}

        Deletes a bid adjustment rule if it is not currently associated with adgroups. After deletion, the bid  modifier rule ca
        """
        endpoint = f"/dsp/rules/bidmodifier/{bid_modifier_rule_id}"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.delete(endpoint, params=params)

    async def get_bid_modifier_rule(self, bid_modifier_rule_id: str, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /dsp/rules/bidmodifier/{bidModifierRuleId}

        Returns all data about a bid adjustment rule using its unique ID. The unique ID (UUID) is returned by CreateBidModifierR
        """
        endpoint = f"/dsp/rules/bidmodifier/{bid_modifier_rule_id}"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def delete_bid_modifier_rule_association(self, bid_modifier_rule_id: str, ad_group_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """DELETE /dsp/rules/bidmodifier/{bidModifierRuleId}/associations

        Removes the association between bid adjustment rule and an adgroup, but does not delete the bid modifier rule. The rule 
        """
        endpoint = f"/dsp/rules/bidmodifier/{bid_modifier_rule_id}/associations"
        params: dict[str, Any] = {}
        if ad_group_id is not None:
            params["adGroupId"] = ad_group_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.delete(endpoint, params=params)

    async def create_bid_modifier_rule_association(self, bid_modifier_rule_id: str, ad_group_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /dsp/rules/bidmodifier/{bidModifierRuleId}/associations

        Associates a bid adjustment rule with an adgroup. Association requests are fulfilled immediately, however it can take ~1
        """
        endpoint = f"/dsp/rules/bidmodifier/{bid_modifier_rule_id}/associations"
        params: dict[str, Any] = {}
        if ad_group_id is not None:
            params["adGroupId"] = ad_group_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.put(endpoint, params=params)

    async def get_bid_modifier_rule_associations(self, bid_modifier_rule_id: str, body: BidModifiersServiceGetBidModifierRuleAssociationsRequestContent | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/rules/bidmodifier/{bidModifierRuleId}/associations/list

        Returns a list of adgroup associations (active, inactive and audienceViolation) for a given bid adjustment rule using it
        """
        endpoint = f"/dsp/rules/bidmodifier/{bid_modifier_rule_id}/associations/list"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspbidmodifier.v1+json")

