"""Auto-generated async API client. Do not edit manually.

Source: AdvertisingBilling_prod_3p.json
Title:  Advertising Billing
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_billing import *  # noqa: F403
except ImportError:
    pass


class BillingClient(BaseAdsClient):
    """Auto-generated from AdvertisingBilling_prod_3p.json (19 operations)"""

    async def get_document(self, document_id: str, doc_type: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """GET /billing/documents/{documentId}

        Gets billing document(s) with id.  **Authorized resource type**: Global Ad Account ID, Profile ID  **Parameter name**: A
        """
        endpoint = f"/billing/documents/{document_id}"
        params: dict[str, Any] = {}
        if doc_type is not None:
            params["docType"] = doc_type
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        return await self.get(endpoint, params=params)

    async def pay_invoices(self, body: AdPaymentsPayInvoicesInput | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /billing/invoices/pay

        Executes payment on a set of or all of an advertisers open invoices.  **Requires one of these permissions**: ['adv_billi
        """
        endpoint = "/billing/invoices/pay"
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

    async def bulk_get_billing_notifications(self, body: bulkGetBillingNotificationsRequestBody | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """POST /billing/notifications

        Get the billing notifications for a list advertising accounts.
        """
        endpoint = "/billing/notifications"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.billingnotifications.v1+json")

    async def create_payment_agreements(self, body: AdPaymentsCreatePaymentAgreementsInput | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """POST /billing/paymentAgreements

        Creates or updates payment agreements.  **Authorized resource type**: Global Ad Account ID, Profile ID  **Parameter name
        """
        endpoint = "/billing/paymentAgreements"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def get_payment_agreements(self, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_manager_account: str | None = None, next_token: str | None = None, agreement_type: str | None = None) -> JSONData | JSONList:
        """POST /billing/paymentAgreements/list

        Gets current payment agreement for a customer.  **Authorized resource type**: Global Ad Account ID, Profile ID  **Parame
        """
        endpoint = "/billing/paymentAgreements/list"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        if next_token is not None:
            params["nextToken"] = next_token
        if agreement_type is not None:
            params["agreementType"] = agreement_type
        return await self.post(endpoint, params=params)

    async def get_customer_payment_methods(self, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_advertising_api_manager_account: str | None = None, next_token: str | None = None, criteria_type: str | None = None) -> JSONData | JSONList:
        """POST /billing/paymentMethods/list

        Retrieves eligible payment methods for a customer.  **Authorized resource type**: Global Ad Account ID, Profile ID  **Pa
        """
        endpoint = "/billing/paymentMethods/list"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        if next_token is not None:
            params["nextToken"] = next_token
        if criteria_type is not None:
            params["criteriaType"] = criteria_type
        return await self.post(endpoint, params=params)

    async def create_payment_profiles(self, body: AdPaymentsCreatePaymentProfileInput | dict[str, Any] | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """POST /billing/paymentProfiles

        Creates or updates payment profiles.  **Authorized resource type**: Global Ad Account ID, Profile ID  **Parameter name**
        """
        endpoint = "/billing/paymentProfiles"
        params: dict[str, Any] = {}
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def bulk_get_billing_status(self, body: bulkGetBillingStatusesRequestBody | dict[str, Any] | None = None) -> JSONData | JSONList:
        """POST /billing/statuses

        Get the billing status for a list of advertising accounts.
        """
        endpoint = "/billing/statuses"
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, content_type="application/vnd.bulkgetbillingstatusrequestbody.v1+json")

    async def get_billing_profile_agreement_content(self, billing_profile_agreement_content_id: str, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_manager_account: str | None = None, language_of_preference: str | None = None) -> JSONData | JSONList:
        """GET /billingProfileAgreementContents/{billingProfileAgreementContentId}

        API to fetch agreement contents related to billing profiles.
        """
        endpoint = f"/billingProfileAgreementContents/{billing_profile_agreement_content_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        if language_of_preference is not None:
            params["languageOfPreference"] = language_of_preference
        return await self.get(endpoint, params=params)

    async def apply_billing_profile(self, body: ApplyBillingProfileRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """POST /billingProfileUsages

        API to link one or more countries with a billing profile. This association is known as 'applying' a billing profile.
        """
        endpoint = "/billingProfileUsages"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.billingProfileUsage.v1+json")

    async def get_billing_profile_usages(self, body: GetBillingProfileUsageRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """POST /billingProfileUsages/list

        Lists the billing profiles linked to each country of global ads account.
        """
        endpoint = "/billingProfileUsages/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.billingProfileUsage.v1+json")

    async def create_billing_profiles(self, body: CreateBillingProfilesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """POST /billingProfiles

        API to create one or more billing profile(s).
        """
        endpoint = "/billingProfiles"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def update_billing_profiles(self, body: UpdateBillingProfilesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """PUT /billingProfiles

        API to update one or more billing profile(s).
        """
        endpoint = "/billingProfiles"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params)

    async def get_billing_profiles(self, body: GetBillingProfilesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """POST /billingProfiles/list

        Fetches billing profiles present under the global account.
        """
        endpoint = "/billingProfiles/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.billingProfile.v1+json")

    async def create_billing_statement(self, body: CreateBillingStatementRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """POST /billingStatements

        API to request billing statement generation for an Advertising account.
        """
        endpoint = "/billingStatements"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.createbillingstatementsrequest.v1+json")

    async def get_billing_statement(self, billing_statement_request_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """GET /billingStatements/{billingStatementRequestId}

        API to fetch the latest status of Billing Statements creation request and billing statement download link if available.
        """
        endpoint = f"/billingStatements/{billing_statement_request_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        return await self.get(endpoint, params=params)

    async def get_billing_invoice_summaries(self, body: BillingInvoiceSummariesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_manager_account: str | None = None) -> JSONData | JSONList:
        """POST /invoiceSummaries/list

        Lists the billing invoice summary(s) in a global ads account as per the search and aggregation parameters passed in the
        """
        endpoint = "/invoiceSummaries/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_manager_account is not None:
            params["Amazon-Advertising-API-Manager-Account"] = amazon_advertising_api_manager_account
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.billingInvoiceSummary.v1+json")

    async def get_advertiser_invoices(self, invoice_statuses: str | None = None, start_date: str | None = None, end_date: str | None = None, count: str | None = None, cursor: str | None = None) -> JSONData | JSONList:
        """GET /invoices

        Get invoices for advertiser
        """
        endpoint = "/invoices"
        params: dict[str, Any] = {}
        if invoice_statuses is not None:
            params["invoiceStatuses"] = invoice_statuses
        if start_date is not None:
            params["startDate"] = start_date
        if end_date is not None:
            params["endDate"] = end_date
        if count is not None:
            params["count"] = count
        if cursor is not None:
            params["cursor"] = cursor
        return await self.get(endpoint, params=params)

    async def get_invoice(self, invoice_id: str) -> JSONData | JSONList:
        """GET /invoices/{invoiceId}

        Get invoice data by invoice ID
        """
        endpoint = f"/invoices/{invoice_id}"
        return await self.get(endpoint)

