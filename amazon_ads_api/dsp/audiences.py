"""
Amazon DSP - Audiences API (异步版本)
DSP受众管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class DSPAudiencesAPI(BaseAdsClient):
    """DSP Audiences API (全异步)"""

    # ============ Audiences ============

    async def list_audiences(
        self,
        advertiser_id: str,
        audience_type: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取受众列表"""
        params: JSONData = {
            "advertiserId": advertiser_id,
            "maxResults": max_results,
        }
        if audience_type:
            params["audienceType"] = audience_type
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/dsp/audiences", params=params)
        return result if isinstance(result, dict) else {"audiences": []}

    async def get_audience(self, audience_id: str, advertiser_id: str) -> JSONData:
        """获取单个受众详情"""
        result = await self.get(f"/dsp/audiences/{audience_id}", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, dict) else {}

    async def create_audience(
        self,
        advertiser_id: str,
        name: str,
        audience_type: str,
        definition: JSONData,
    ) -> JSONData:
        """创建受众"""
        result = await self.post("/dsp/audiences", json_data={
            "advertiserId": advertiser_id,
            "name": name,
            "audienceType": audience_type,
            "definition": definition,
        })
        return result if isinstance(result, dict) else {}

    async def update_audience(
        self,
        audience_id: str,
        advertiser_id: str,
        updates: JSONData,
    ) -> JSONData:
        """更新受众"""
        result = await self.put(f"/dsp/audiences/{audience_id}", json_data={
            "advertiserId": advertiser_id,
            **updates,
        })
        return result if isinstance(result, dict) else {}

    async def delete_audience(self, audience_id: str, advertiser_id: str) -> JSONData:
        """删除受众"""
        return await self.delete(f"/dsp/audiences/{audience_id}?advertiserId={advertiser_id}")

    # ============ Audience Segments ============

    async def list_amazon_segments(
        self,
        advertiser_id: str,
        segment_type: str | None = None,
    ) -> JSONList:
        """获取Amazon预设受众分类"""
        params: JSONData = {"advertiserId": advertiser_id}
        if segment_type:
            params["segmentType"] = segment_type

        result = await self.get("/dsp/audiences/amazonSegments", params=params)
        return result if isinstance(result, list) else []

    async def get_segment_taxonomy(self, advertiser_id: str) -> JSONData:
        """获取受众分类树"""
        result = await self.get("/dsp/audiences/taxonomy", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, dict) else {}

    # ============ Lookalike Audiences ============

    async def create_lookalike_audience(
        self,
        advertiser_id: str,
        name: str,
        seed_audience_id: str,
        reach_percentage: int = 5,
    ) -> JSONData:
        """创建相似受众"""
        result = await self.post("/dsp/audiences/lookalike", json_data={
            "advertiserId": advertiser_id,
            "name": name,
            "seedAudienceId": seed_audience_id,
            "reachPercentage": reach_percentage,
        })
        return result if isinstance(result, dict) else {}

    # ============ Remarketing Audiences ============

    async def create_remarketing_audience(
        self,
        advertiser_id: str,
        name: str,
        pixel_id: str,
        lookback_days: int = 30,
        rules: list[dict] | None = None,
    ) -> JSONData:
        """创建再营销受众"""
        body: JSONData = {
            "advertiserId": advertiser_id,
            "name": name,
            "pixelId": pixel_id,
            "lookbackDays": lookback_days,
        }
        if rules:
            body["rules"] = rules

        result = await self.post("/dsp/audiences/remarketing", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ Audience Size Estimation ============

    async def estimate_audience_size(
        self,
        advertiser_id: str,
        definition: JSONData,
    ) -> JSONData:
        """预估受众规模"""
        result = await self.post("/dsp/audiences/estimate", json_data={
            "advertiserId": advertiser_id,
            "definition": definition,
        })
        return result if isinstance(result, dict) else {}

    # ============ Pixel Management ============

    async def list_pixels(self, advertiser_id: str) -> JSONList:
        """获取DSP Pixel列表"""
        result = await self.get("/dsp/pixels", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, list) else []

    async def get_pixel(self, pixel_id: str, advertiser_id: str) -> JSONData:
        """获取Pixel详情"""
        result = await self.get(f"/dsp/pixels/{pixel_id}", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, dict) else {}

    async def create_pixel(
        self,
        advertiser_id: str,
        name: str,
        pixel_type: str = "UNIVERSAL",
    ) -> JSONData:
        """创建Pixel"""
        result = await self.post("/dsp/pixels", json_data={
            "advertiserId": advertiser_id,
            "name": name,
            "pixelType": pixel_type,
        })
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def list_all_audiences(
        self,
        advertiser_id: str,
        audience_type: str | None = None,
    ) -> JSONList:
        """获取所有受众（自动分页）"""
        all_audiences = []
        next_token = None

        while True:
            result = await self.list_audiences(
                advertiser_id=advertiser_id,
                audience_type=audience_type,
                max_results=100,
                next_token=next_token,
            )
            audiences = result.get("audiences", [])
            all_audiences.extend(audiences)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_audiences
