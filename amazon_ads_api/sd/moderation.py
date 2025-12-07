"""
Sponsored Display - Creative Moderation API
SD创意审核管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SDModerationAPI(BaseAdsClient):
    """SD Creative Moderation API"""

    # ============ Creative Moderation Status ============

    def get_creative_moderation_status(self, creative_id: str) -> JSONData:
        """
        获取创意审核状态
        
        Returns:
            {
                "creativeId": "xxx",
                "moderationStatus": "APPROVED" | "PENDING" | "REJECTED",
                "reasons": [...],
                "recommendations": [...]
            }
        """
        result = self.get(f"/sd/moderation/creatives/{creative_id}")
        return result if isinstance(result, dict) else {}

    def get_batch_creative_moderation_status(
        self,
        creative_ids: list[str],
    ) -> JSONList:
        """批量获取创意审核状态"""
        result = self.post("/sd/moderation/creatives/batch", json_data={
            "creativeIds": creative_ids
        })
        return result if isinstance(result, list) else []

    def submit_creative_for_moderation(self, creative_id: str) -> JSONData:
        """提交创意审核"""
        result = self.post(f"/sd/moderation/creatives/{creative_id}/submit")
        return result if isinstance(result, dict) else {}

    def request_moderation_review(
        self,
        creative_id: str,
        comments: str | None = None,
    ) -> JSONData:
        """请求重新审核"""
        body: JSONData = {}
        if comments:
            body["comments"] = comments

        result = self.post(
            f"/sd/moderation/creatives/{creative_id}/review",
            json_data=body
        )
        return result if isinstance(result, dict) else {}

    # ============ Pre-validation ============

    def validate_headline(self, headline: str) -> JSONData:
        """验证标题"""
        result = self.post("/sd/moderation/validate/headline", json_data={
            "headline": headline
        })
        return result if isinstance(result, dict) else {}

    def validate_logo(self, logo_asset_id: str) -> JSONData:
        """验证Logo"""
        result = self.post("/sd/moderation/validate/logo", json_data={
            "logoAssetId": logo_asset_id
        })
        return result if isinstance(result, dict) else {}

    def validate_custom_image(self, image_asset_id: str) -> JSONData:
        """验证自定义图片"""
        result = self.post("/sd/moderation/validate/customImage", json_data={
            "imageAssetId": image_asset_id
        })
        return result if isinstance(result, dict) else {}

    def validate_creative_complete(
        self,
        headline: str,
        logo_asset_id: str | None = None,
        custom_image_asset_id: str | None = None,
    ) -> JSONData:
        """
        完整验证创意
        
        在创建前验证所有元素
        """
        body: JSONData = {"headline": headline}
        if logo_asset_id:
            body["logoAssetId"] = logo_asset_id
        if custom_image_asset_id:
            body["customImageAssetId"] = custom_image_asset_id

        result = self.post("/sd/moderation/validate/complete", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ Policy Information ============

    def get_creative_policies(self) -> JSONList:
        """获取创意政策列表"""
        result = self.get("/sd/moderation/policies")
        return result if isinstance(result, list) else []

    def get_headline_requirements(self) -> JSONData:
        """获取标题要求"""
        result = self.get("/sd/moderation/requirements/headline")
        return result if isinstance(result, dict) else {}

    def get_logo_requirements(self) -> JSONData:
        """获取Logo要求"""
        result = self.get("/sd/moderation/requirements/logo")
        return result if isinstance(result, dict) else {}

    def get_custom_image_requirements(self) -> JSONData:
        """获取自定义图片要求"""
        result = self.get("/sd/moderation/requirements/customImage")
        return result if isinstance(result, dict) else {}

    def get_prohibited_content(self) -> JSONList:
        """获取禁止内容列表"""
        result = self.get("/sd/moderation/prohibitedContent")
        return result if isinstance(result, list) else []

    # ============ Moderation History ============

    def get_moderation_history(
        self,
        creative_id: str,
        max_results: int = 50,
    ) -> JSONList:
        """获取审核历史"""
        result = self.get(f"/sd/moderation/creatives/{creative_id}/history", params={
            "maxResults": max_results
        })
        return result if isinstance(result, list) else []

    # ============ Appeal ============

    def submit_appeal(
        self,
        creative_id: str,
        reason: str,
        supporting_documents: list[str] | None = None,
    ) -> JSONData:
        """
        提交申诉
        
        Args:
            reason: 申诉原因
            supporting_documents: 支持文档的资产ID列表
        """
        body: JSONData = {
            "creativeId": creative_id,
            "reason": reason,
        }
        if supporting_documents:
            body["supportingDocuments"] = supporting_documents

        result = self.post("/sd/moderation/appeals", json_data=body)
        return result if isinstance(result, dict) else {}

    def get_appeal_status(self, appeal_id: str) -> JSONData:
        """获取申诉状态"""
        result = self.get(f"/sd/moderation/appeals/{appeal_id}")
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    def get_pending_creatives(self) -> JSONList:
        """获取待审核的创意"""
        # 获取所有创意
        creatives_result = self.get("/sd/creatives", params={"maxResults": 100})
        creatives = (
            creatives_result.get("creatives", [])
            if isinstance(creatives_result, dict) else []
        )

        pending = []
        for creative in creatives:
            creative_id = creative.get("creativeId")
            if not creative_id:
                continue

            status = self.get_creative_moderation_status(creative_id)
            if status.get("moderationStatus") == "PENDING":
                pending.append({**creative, "moderation": status})

        return pending

    def get_rejected_creatives_with_details(self) -> JSONList:
        """获取被拒绝的创意及详情"""
        creatives_result = self.get("/sd/creatives", params={"maxResults": 100})
        creatives = (
            creatives_result.get("creatives", [])
            if isinstance(creatives_result, dict) else []
        )

        rejected = []
        for creative in creatives:
            creative_id = creative.get("creativeId")
            if not creative_id:
                continue

            status = self.get_creative_moderation_status(creative_id)
            if status.get("moderationStatus") == "REJECTED":
                rejected.append({
                    **creative,
                    "moderation": status,
                    "reasons": status.get("reasons", []),
                    "recommendations": status.get("recommendations", []),
                })

        return rejected

    def pre_validate_all(
        self,
        headline: str,
        logo_asset_id: str | None = None,
        custom_image_asset_id: str | None = None,
    ) -> JSONData:
        """
        预验证所有创意元素
        
        返回综合验证结果
        """
        results = {
            "headline": self.validate_headline(headline),
        }

        if logo_asset_id:
            results["logo"] = self.validate_logo(logo_asset_id)

        if custom_image_asset_id:
            results["customImage"] = self.validate_custom_image(custom_image_asset_id)

        # 完整验证
        results["complete"] = self.validate_creative_complete(
            headline=headline,
            logo_asset_id=logo_asset_id,
            custom_image_asset_id=custom_image_asset_id,
        )

        # 判断是否全部通过
        all_valid = all(
            r.get("valid", True) for r in results.values() if isinstance(r, dict)
        )
        results["allValid"] = all_valid

        return results

