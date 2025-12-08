"""
Sponsored Display - Creative Moderation API (异步版本)
SD创意审核管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SDModerationAPI(BaseAdsClient):
    """SD Creative Moderation API (全异步)"""

    # ============ Creative Moderation Status ============

    async def get_creative_moderation_status(self, creative_id: str) -> JSONData:
        """获取创意审核状态"""
        result = await self.get(f"/sd/moderation/creatives/{creative_id}")
        return result if isinstance(result, dict) else {}

    async def get_batch_creative_moderation_status(
        self,
        creative_ids: list[str],
    ) -> JSONList:
        """批量获取创意审核状态"""
        result = await self.post("/sd/moderation/creatives/batch", json_data={
            "creativeIds": creative_ids
        })
        return result if isinstance(result, list) else []

    async def submit_creative_for_moderation(self, creative_id: str) -> JSONData:
        """提交创意审核"""
        result = await self.post(f"/sd/moderation/creatives/{creative_id}/submit")
        return result if isinstance(result, dict) else {}

    async def request_moderation_review(
        self,
        creative_id: str,
        comments: str | None = None,
    ) -> JSONData:
        """请求重新审核"""
        body: JSONData = {}
        if comments:
            body["comments"] = comments

        result = await self.post(
            f"/sd/moderation/creatives/{creative_id}/review",
            json_data=body
        )
        return result if isinstance(result, dict) else {}

    # ============ Pre-validation ============

    async def validate_headline(self, headline: str) -> JSONData:
        """验证标题"""
        result = await self.post("/sd/moderation/validate/headline", json_data={
            "headline": headline
        })
        return result if isinstance(result, dict) else {}

    async def validate_logo(self, logo_asset_id: str) -> JSONData:
        """验证Logo"""
        result = await self.post("/sd/moderation/validate/logo", json_data={
            "logoAssetId": logo_asset_id
        })
        return result if isinstance(result, dict) else {}

    async def validate_custom_image(self, image_asset_id: str) -> JSONData:
        """验证自定义图片"""
        result = await self.post("/sd/moderation/validate/customImage", json_data={
            "imageAssetId": image_asset_id
        })
        return result if isinstance(result, dict) else {}

    async def validate_creative_complete(
        self,
        headline: str,
        logo_asset_id: str | None = None,
        custom_image_asset_id: str | None = None,
    ) -> JSONData:
        """完整验证创意"""
        body: JSONData = {"headline": headline}
        if logo_asset_id:
            body["logoAssetId"] = logo_asset_id
        if custom_image_asset_id:
            body["customImageAssetId"] = custom_image_asset_id

        result = await self.post("/sd/moderation/validate/complete", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ Policy Information ============

    async def get_creative_policies(self) -> JSONList:
        """获取创意政策列表"""
        result = await self.get("/sd/moderation/policies")
        return result if isinstance(result, list) else []

    async def get_headline_requirements(self) -> JSONData:
        """获取标题要求"""
        result = await self.get("/sd/moderation/requirements/headline")
        return result if isinstance(result, dict) else {}

    async def get_logo_requirements(self) -> JSONData:
        """获取Logo要求"""
        result = await self.get("/sd/moderation/requirements/logo")
        return result if isinstance(result, dict) else {}

    async def get_custom_image_requirements(self) -> JSONData:
        """获取自定义图片要求"""
        result = await self.get("/sd/moderation/requirements/customImage")
        return result if isinstance(result, dict) else {}

    async def get_prohibited_content(self) -> JSONList:
        """获取禁止内容列表"""
        result = await self.get("/sd/moderation/prohibitedContent")
        return result if isinstance(result, list) else []

    # ============ Moderation History ============

    async def get_moderation_history(
        self,
        creative_id: str,
        max_results: int = 50,
    ) -> JSONList:
        """获取审核历史"""
        result = await self.get(f"/sd/moderation/creatives/{creative_id}/history", params={
            "maxResults": max_results
        })
        return result if isinstance(result, list) else []

    # ============ Appeal ============

    async def submit_appeal(
        self,
        creative_id: str,
        reason: str,
        supporting_documents: list[str] | None = None,
    ) -> JSONData:
        """提交申诉"""
        body: JSONData = {
            "creativeId": creative_id,
            "reason": reason,
        }
        if supporting_documents:
            body["supportingDocuments"] = supporting_documents

        result = await self.post("/sd/moderation/appeals", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_appeal_status(self, appeal_id: str) -> JSONData:
        """获取申诉状态"""
        result = await self.get(f"/sd/moderation/appeals/{appeal_id}")
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def get_pending_creatives(self) -> JSONList:
        """获取待审核的创意"""
        creatives_result = await self.get("/sd/creatives", params={"maxResults": 100})
        creatives = (
            creatives_result.get("creatives", [])
            if isinstance(creatives_result, dict) else []
        )

        pending = []
        for creative in creatives:
            creative_id = creative.get("creativeId")
            if not creative_id:
                continue

            status = await self.get_creative_moderation_status(creative_id)
            if status.get("moderationStatus") == "PENDING":
                pending.append({**creative, "moderation": status})

        return pending

    async def get_rejected_creatives_with_details(self) -> JSONList:
        """获取被拒绝的创意及详情"""
        creatives_result = await self.get("/sd/creatives", params={"maxResults": 100})
        creatives = (
            creatives_result.get("creatives", [])
            if isinstance(creatives_result, dict) else []
        )

        rejected = []
        for creative in creatives:
            creative_id = creative.get("creativeId")
            if not creative_id:
                continue

            status = await self.get_creative_moderation_status(creative_id)
            if status.get("moderationStatus") == "REJECTED":
                rejected.append({
                    **creative,
                    "moderation": status,
                    "reasons": status.get("reasons", []),
                    "recommendations": status.get("recommendations", []),
                })

        return rejected

    async def pre_validate_all(
        self,
        headline: str,
        logo_asset_id: str | None = None,
        custom_image_asset_id: str | None = None,
    ) -> JSONData:
        """预验证所有创意元素"""
        results = {
            "headline": await self.validate_headline(headline),
        }

        if logo_asset_id:
            results["logo"] = await self.validate_logo(logo_asset_id)

        if custom_image_asset_id:
            results["customImage"] = await self.validate_custom_image(custom_image_asset_id)

        results["complete"] = await self.validate_creative_complete(
            headline=headline,
            logo_asset_id=logo_asset_id,
            custom_image_asset_id=custom_image_asset_id,
        )

        all_valid = all(
            r.get("valid", True) for r in results.values() if isinstance(r, dict)
        )
        results["allValid"] = all_valid

        return results
