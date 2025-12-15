"""
Amazon Ads Billing API (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/billing
OpenAPI Spec: AdvertisingBilling_prod_3p.json

账单、发票、支付管理
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


# Content-Type 常量
BILLING_DOCUMENTS_V1 = "application/vnd.billingDocuments.v1+json"
BILLING_NOTIFICATIONS_V1 = "application/vnd.billingnotifications.v1+json"
BILLING_STATUS_V1 = "application/vnd.bulkgetbillingstatusrequestbody.v1+json"
PAYMENT_AGREEMENTS_V1 = "application/vnd.paymentagreements.v1+json"
PAYMENT_METHODS_V1 = "application/vnd.paymentmethods.v1+json"
PAYMENT_PROFILES_V1 = "application/vnd.paymentprofiles.v1+json"
BILLING_PROFILE_V1 = "application/vnd.billingProfile.v1+json"
BILLING_PROFILE_USAGE_V1 = "application/vnd.billingProfileUsage.v1+json"
BILLING_STATEMENT_V1 = "application/vnd.createbillingstatementsrequest.v1+json"
BILLING_INVOICE_SUMMARY_V1 = "application/vnd.billingInvoiceSummary.v1+json"
INVOICE_V1 = "application/vnd.invoice.v1.1+json"
INVOICES_V1 = "application/vnd.invoices.v1+json"


class BillingAPI(BaseAdsClient):
    """
    Billing API (全异步)
    
    官方端点共 18 个:
    - Billing Documents: 1
    - Billing Notifications: 1
    - Billing Status: 1
    - Payment Agreements: 2
    - Payment Methods: 1
    - Payment Profiles: 1
    - Billing Profiles: 3
    - Billing Profile Usages: 2
    - Billing Statements: 2
    - Invoice Summaries: 1
    - Invoices: 3
    """

    # ============ Billing Documents ============

    async def get_document(
        self,
        document_id: str,
        doc_types: list[str],
    ) -> JSONData:
        """
        获取账单文档
        
        GET /billing/documents/{documentId}
        
        Args:
            document_id: 文档ID
            doc_types: 文档类型列表
                - CREDIT_MEMO
                - GIS_CREDIT_MEMO
                - GIS_INVOICE
                - INVOICE
                - PAYMENT_COMPLEMENT
                - PREPAYMENT_RECEIPT
        
        Returns:
            {
                "availableDocuments": [...],
                "unavailableDocuments": [...]
            }
        """
        params = {"docType": doc_types}
        result = await self.get(
            f"/billing/documents/{document_id}",
            params=params,
            accept=BILLING_DOCUMENTS_V1
        )
        return result if isinstance(result, dict) else {}

    # ============ Billing Notifications ============

    async def get_billing_notifications(
        self,
        advertiser_marketplaces: list[dict],
        locale: str = "en_US",
    ) -> JSONData:
        """
        获取账单通知
        
        POST /billing/notifications
        
        Args:
            advertiser_marketplaces: [
                {"advertiserId": "A123...", "marketplaceId": "A2NODRKZP88ZB9"}
            ]
            locale: 语言 (en_US, ja_JP, de_DE, etc.)
        
        Returns:
            {
                "success": [...],
                "error": [...]
            }
        """
        body: JSONData = {
            "advertiserMarketplaces": advertiser_marketplaces,
            "locale": locale,
        }
        result = await self.post(
            "/billing/notifications",
            json_data=body,
            content_type=BILLING_NOTIFICATIONS_V1
        )
        return result if isinstance(result, dict) else {}

    # ============ Billing Status ============

    async def get_billing_statuses(
        self,
        advertiser_marketplaces: list[dict],
        locale: str | None = None,
    ) -> JSONData:
        """
        获取账单状态
        
        POST /billing/statuses
        
        Args:
            advertiser_marketplaces: [
                {"advertiserId": "A123...", "marketplaceId": "A2NODRKZP88ZB9"}
            ]
            locale: 语言
        
        Returns:
            {
                "success": [{"advertiserMarketplace": {...}, "billingStatus": {...}}],
                "error": [...]
            }
        """
        body: JSONData = {"advertiserMarketplaces": advertiser_marketplaces}
        if locale:
            body["locale"] = locale
        
        result = await self.post(
            "/billing/statuses",
            json_data=body,
            content_type=BILLING_STATUS_V1
        )
        return result if isinstance(result, dict) else {}

    # ============ Payment Agreements ============

    async def create_payment_agreements(
        self,
        payment_agreements: list[dict],
    ) -> JSONData:
        """
        创建或更新支付协议
        
        POST /billing/paymentAgreements
        
        Args:
            payment_agreements: 支付协议列表
        """
        result = await self.post(
            "/billing/paymentAgreements",
            json_data=payment_agreements,
            content_type="application/json",
            accept=PAYMENT_AGREEMENTS_V1
        )
        return result if isinstance(result, dict) else {}

    async def list_payment_agreements(
        self,
        agreement_type: str,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取支付协议列表
        
        POST /billing/paymentAgreements/list
        
        Args:
            agreement_type: 协议类型
            next_token: 分页 token
        """
        params = {"agreementType": agreement_type}
        if next_token:
            params["nextToken"] = next_token
        
        result = await self.post(
            "/billing/paymentAgreements/list",
            params=params,
            accept=PAYMENT_AGREEMENTS_V1
        )
        return result if isinstance(result, dict) else {}

    # ============ Payment Methods ============

    async def list_payment_methods(
        self,
        criteria_type: str,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取支付方式列表
        
        POST /billing/paymentMethods/list
        
        Args:
            criteria_type: 筛选条件类型
            next_token: 分页 token
        """
        params = {"criteriaType": criteria_type}
        if next_token:
            params["nextToken"] = next_token
        
        result = await self.post(
            "/billing/paymentMethods/list",
            params=params,
            accept=PAYMENT_METHODS_V1
        )
        return result if isinstance(result, dict) else {}

    # ============ Payment Profiles ============

    async def create_payment_profiles(
        self,
        payment_profiles: list[dict],
    ) -> JSONData:
        """
        创建或更新支付配置
        
        POST /billing/paymentProfiles
        
        Args:
            payment_profiles: 支付配置列表
        """
        result = await self.post(
            "/billing/paymentProfiles",
            json_data=payment_profiles,
            content_type="application/json",
            accept=PAYMENT_PROFILES_V1
        )
        return result if isinstance(result, dict) else {}

    # ============ Billing Profiles ============

    async def create_billing_profiles(
        self,
        billing_profiles: list[dict],
    ) -> JSONData:
        """
        创建账单配置
        
        POST /billingProfiles
        
        Args:
            billing_profiles: [
                {
                    "billingParty": "BRAND_OWNER" | "AGENCY",
                    "isBillTo": true,
                    "billingName": "...",
                    "address": {...},
                    "taxInformation": {...}
                }
            ]
        """
        body = {"billingProfiles": billing_profiles}
        result = await self.post(
            "/billingProfiles",
            json_data=body,
            content_type="application/json",
            accept=BILLING_PROFILE_V1
        )
        return result if isinstance(result, dict) else {}

    async def update_billing_profiles(
        self,
        billing_profiles: list[dict],
    ) -> JSONData:
        """
        更新账单配置
        
        PUT /billingProfiles
        
        Args:
            billing_profiles: [
                {
                    "billingProfileId": "xxx",
                    "billingName": "...",
                    "address": {...}
                }
            ]
        """
        body = {"billingProfiles": billing_profiles}
        result = await self.put(
            "/billingProfiles",
            json_data=body,
            content_type="application/json",
            accept=BILLING_PROFILE_V1
        )
        return result if isinstance(result, dict) else {}

    async def list_billing_profiles(
        self,
        billing_profile_ids: list[str] | None = None,
        default_only: bool = False,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取账单配置列表
        
        POST /billingProfiles/list
        
        Args:
            billing_profile_ids: 配置 ID 过滤
            default_only: 仅获取默认配置
            max_results: 最大结果数
            next_token: 分页 token
        """
        body: JSONData = {"maxResults": max_results}
        
        filters: JSONData = {}
        if billing_profile_ids:
            filters["billingProfileIdFilter"] = billing_profile_ids
        if default_only:
            filters["defaultBillingProfileFilter"] = True
        if filters:
            body["filters"] = filters
        
        if next_token:
            body["nextToken"] = next_token
        
        result = await self.post(
            "/billingProfiles/list",
            json_data=body,
            content_type=BILLING_PROFILE_V1
        )
        return result if isinstance(result, dict) else {}

    # ============ Billing Profile Usages ============

    async def apply_billing_profile(
        self,
        billing_profile_id: str,
        advertisers: list[dict],
    ) -> JSONData:
        """
        关联账单配置到国家/地区
        
        POST /billingProfileUsages
        
        Args:
            billing_profile_id: 账单配置 ID
            advertisers: [{"countryCode": "US"}, {"countryCode": "DE"}]
        """
        body: JSONData = {
            "billingProfileId": billing_profile_id,
            "advertisers": advertisers,
        }
        result = await self.post(
            "/billingProfileUsages",
            json_data=body,
            content_type=BILLING_PROFILE_USAGE_V1
        )
        return result if isinstance(result, dict) else {}

    async def list_billing_profile_usages(
        self,
        advertiser_filter: list[dict] | None = None,
        expand_billing_profile: bool = False,
        expand_fallback: bool = False,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取账单配置关联列表
        
        POST /billingProfileUsages/list
        
        Args:
            advertiser_filter: [{"countryCode": "US"}]
            expand_billing_profile: 展开配置详情
            expand_fallback: 展开回退配置
            max_results: 最大结果数
            next_token: 分页 token
        """
        body: JSONData = {
            "expandBillingProfile": expand_billing_profile,
            "expandFallbackBillingProfile": expand_fallback,
            "maxResults": max_results,
        }
        
        if advertiser_filter:
            body["filters"] = {"advertiserFilter": advertiser_filter}
        
        if next_token:
            body["nextToken"] = next_token
        
        result = await self.post(
            "/billingProfileUsages/list",
            json_data=body,
            content_type=BILLING_PROFILE_USAGE_V1
        )
        return result if isinstance(result, dict) else {}

    # ============ Billing Statements ============

    async def create_billing_statement(
        self,
        start_date: str,
        end_date: str,
        locale: str,
        country_codes: list[str] | None = None,
        file_format: str = "CSV",
    ) -> JSONData:
        """
        创建账单报表
        
        POST /billingStatements
        
        Args:
            start_date: 开始日期 (YYYY-MM-DD)
            end_date: 结束日期 (YYYY-MM-DD)
            locale: 语言 (en_US, ja_JP, etc.)
            country_codes: 国家代码列表
            file_format: 文件格式 (CSV)
        
        Returns:
            {
                "billingStatementRequestId": "xxx",
                "details": "..."
            }
        """
        body: JSONData = {
            "startDate": start_date,
            "endDate": end_date,
            "locale": locale,
            "format": file_format,
        }
        if country_codes:
            body["countryCodes"] = country_codes
        
        result = await self.post(
            "/billingStatements",
            json_data=body,
            content_type=BILLING_STATEMENT_V1
        )
        return result if isinstance(result, dict) else {}

    async def get_billing_statement(
        self,
        billing_statement_request_id: str,
    ) -> JSONData:
        """
        获取账单报表状态和下载链接
        
        GET /billingStatements/{billingStatementRequestId}
        
        Args:
            billing_statement_request_id: 报表请求 ID
        
        Returns:
            {
                "reportStatus": "SUCCESS" | "IN_PROGRESS" | "FAILED",
                "s3DownloadLink": "https://...",
                "details": "..."
            }
        """
        result = await self.get(
            f"/billingStatements/{billing_statement_request_id}",
            accept=BILLING_STATEMENT_V1
        )
        return result if isinstance(result, dict) else {}

    # ============ Invoice Summaries ============

    async def list_invoice_summaries(
        self,
        filters: JSONData | None = None,
        sort: JSONData | None = None,
        aggregations: list[dict] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取账单摘要列表
        
        POST /invoiceSummaries/list
        
        Args:
            filters: 过滤条件
            sort: 排序条件
            aggregations: 聚合查询
            max_results: 最大结果数
            next_token: 分页 token
        """
        body: JSONData = {"maxResults": max_results}
        
        if filters:
            body["filters"] = filters
        if sort:
            body["sort"] = sort
        if aggregations:
            body["aggregations"] = aggregations
        if next_token:
            body["nextToken"] = next_token
        
        result = await self.post(
            "/invoiceSummaries/list",
            json_data=body,
            content_type=BILLING_INVOICE_SUMMARY_V1
        )
        return result if isinstance(result, dict) else {}

    # ============ Invoices ============

    async def list_invoices(
        self,
        invoice_statuses: list[str] | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        count: int = 100,
        cursor: str | None = None,
    ) -> JSONData:
        """
        获取发票列表
        
        GET /invoices
        
        Args:
            invoice_statuses: 发票状态过滤
                - ISSUED
                - PAID_IN_FULL
                - PAID_IN_PART
                - WRITTEN_OFF
            start_date: 开始日期 (ISO-8601)
            end_date: 结束日期 (ISO-8601)
            count: 每页数量 (最大 100)
            cursor: 分页游标
        
        Returns:
            {
                "invoiceSummaries": [...],
                "nextCursor": "...",
                "previousCursor": "..."
            }
        """
        params: JSONData = {}
        
        if invoice_statuses:
            params["invoiceStatuses"] = ",".join(invoice_statuses)
        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date
        if cursor:
            params["cursor"] = cursor
        else:
            params["count"] = count
        
        result = await self.get(
            "/invoices",
            params=params,
            accept=INVOICES_V1
        )
        return result if isinstance(result, dict) else {}

    async def get_invoice(self, invoice_id: str) -> JSONData:
        """
        获取发票详情
        
        GET /invoices/{invoiceId}
        
        Args:
            invoice_id: 发票 ID
        
        Returns:
            完整发票对象，包含:
            - invoiceSummary
            - invoiceLines
            - payments
            - taxDetail
            - adjustments
            - promotions
            - portfolios
        """
        result = await self.get(
            f"/invoices/{invoice_id}",
            accept=INVOICE_V1
        )
        return result if isinstance(result, dict) else {}

    async def pay_invoices(
        self,
        invoice_ids: list[str] | None = None,
        pay_all: bool = False,
    ) -> JSONData:
        """
        支付发票
        
        POST /billing/invoices/pay
        
        Args:
            invoice_ids: 要支付的发票 ID 列表
            pay_all: 支付所有未付发票
        """
        body: JSONData = {}
        if invoice_ids:
            body["invoiceIds"] = invoice_ids
        if pay_all:
            body["payAll"] = True
        
        result = await self.post(
            "/billing/invoices/pay",
            json_data=body,
            content_type="application/json",
            accept=INVOICES_V1
        )
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def get_all_invoices(
        self,
        invoice_statuses: list[str] | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> JSONList:
        """
        获取所有发票（自动分页）
        """
        all_invoices: JSONList = []
        cursor = None
        
        while True:
            result = await self.list_invoices(
                invoice_statuses=invoice_statuses,
                start_date=start_date,
                end_date=end_date,
                cursor=cursor,
            )
            invoices = result.get("invoiceSummaries", [])
            all_invoices.extend(invoices)
            
            cursor = result.get("nextCursor")
            if not cursor:
                break
        
        return all_invoices

    async def get_unpaid_invoices(self) -> JSONList:
        """获取未付发票"""
        return await self.get_all_invoices(
            invoice_statuses=["ISSUED", "PAID_IN_PART"]
        )

    async def get_billing_profile_agreement_content(
        self,
        agreement_id: str,
        language: str = "en_US",
    ) -> JSONData:
        """
        获取账单配置协议内容
        
        GET /billingProfileAgreementContents/{billingProfileAgreementContentId}
        
        Args:
            agreement_id: 协议 ID
            language: 语言
        
        Returns:
            {"content": "HTML内容..."}
        """
        result = await self.get(
            f"/billingProfileAgreementContents/{agreement_id}",
            params={"languageOfPreference": language}
        )
        return result if isinstance(result, dict) else {}
