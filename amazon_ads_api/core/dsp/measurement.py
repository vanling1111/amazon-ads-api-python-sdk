"""
Amazon DSP - Measurement API (异步版本)

官方端点 (30个):
- 资格检查 (4个)
- 受众研究 (4个)
- 品牌提升 (4个)
- 创意测试 (4个)
- 全渠道指标 (4个)
- 通用测量 (3个)
- 调研 (3个)
- 供应商产品 (4个)

官方规范: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Measurement_prod_3p.json
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class DSPMeasurementAPI(BaseAdsClient):
    """
    DSP Measurement API (全异步)
    
    用于管理 DSP 测量研究，包括品牌提升、受众研究、创意测试等。
    """

    # ============ 资格检查 ============

    async def check_audience_research_eligibility(
        self,
        advertiser_id: str,
        **kwargs,
    ) -> JSONData:
        """
        检查受众研究资格
        
        官方端点: POST /dsp/measurement/eligibility/audienceResearch
        """
        body: JSONData = {"advertiserId": advertiser_id}
        body.update(kwargs)
        result = await self.post("/dsp/measurement/eligibility/audienceResearch", json_data=body)
        return result if isinstance(result, dict) else {}

    async def check_brand_lift_eligibility(
        self,
        advertiser_id: str,
        **kwargs,
    ) -> JSONData:
        """
        检查品牌提升研究资格
        
        官方端点: POST /dsp/measurement/eligibility/brandLift
        """
        body: JSONData = {"advertiserId": advertiser_id}
        body.update(kwargs)
        result = await self.post("/dsp/measurement/eligibility/brandLift", json_data=body)
        return result if isinstance(result, dict) else {}

    async def check_creative_testing_eligibility(
        self,
        advertiser_id: str,
        **kwargs,
    ) -> JSONData:
        """
        检查创意测试资格
        
        官方端点: POST /dsp/measurement/eligibility/creativeTesting
        """
        body: JSONData = {"advertiserId": advertiser_id}
        body.update(kwargs)
        result = await self.post("/dsp/measurement/eligibility/creativeTesting", json_data=body)
        return result if isinstance(result, dict) else {}

    async def check_omnichannel_metrics_eligibility(
        self,
        advertiser_id: str,
        **kwargs,
    ) -> JSONData:
        """
        检查全渠道指标资格
        
        官方端点: POST /dsp/measurement/eligibility/omnichannelMetrics
        """
        body: JSONData = {"advertiserId": advertiser_id}
        body.update(kwargs)
        result = await self.post("/dsp/measurement/eligibility/omnichannelMetrics", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ 受众研究 ============

    async def list_audience_research_studies(self, **kwargs) -> JSONData:
        """
        列出受众研究
        
        官方端点: GET /dsp/measurement/studies/audienceResearch
        """
        result = await self.get("/dsp/measurement/studies/audienceResearch", params=kwargs)
        return result if isinstance(result, dict) else {"studies": []}

    async def create_audience_research_study(
        self,
        name: str,
        advertiser_id: str,
        **kwargs,
    ) -> JSONData:
        """
        创建受众研究
        
        官方端点: POST /dsp/measurement/studies/audienceResearch
        """
        body: JSONData = {"name": name, "advertiserId": advertiser_id}
        body.update(kwargs)
        result = await self.post("/dsp/measurement/studies/audienceResearch", json_data=body)
        return result if isinstance(result, dict) else {}

    async def update_audience_research_study(
        self,
        study_id: str,
        updates: JSONData,
    ) -> JSONData:
        """
        更新受众研究
        
        官方端点: PUT /dsp/measurement/studies/audienceResearch/{studyId}
        """
        result = await self.put(
            f"/dsp/measurement/studies/audienceResearch/{study_id}",
            json_data=updates
        )
        return result if isinstance(result, dict) else {}

    async def get_audience_research_result(self, study_id: str) -> JSONData:
        """
        获取受众研究结果
        
        官方端点: GET /dsp/measurement/studies/audienceResearch/{studyId}/result
        """
        result = await self.get(f"/dsp/measurement/studies/audienceResearch/{study_id}/result")
        return result if isinstance(result, dict) else {}

    # ============ 品牌提升 ============

    async def list_brand_lift_studies(self, **kwargs) -> JSONData:
        """
        列出品牌提升研究
        
        官方端点: GET /dsp/measurement/studies/brandLift
        """
        result = await self.get("/dsp/measurement/studies/brandLift", params=kwargs)
        return result if isinstance(result, dict) else {"studies": []}

    async def create_brand_lift_study(
        self,
        name: str,
        advertiser_id: str,
        **kwargs,
    ) -> JSONData:
        """
        创建品牌提升研究
        
        官方端点: POST /dsp/measurement/studies/brandLift
        """
        body: JSONData = {"name": name, "advertiserId": advertiser_id}
        body.update(kwargs)
        result = await self.post("/dsp/measurement/studies/brandLift", json_data=body)
        return result if isinstance(result, dict) else {}

    async def update_brand_lift_study(self, updates: JSONData) -> JSONData:
        """
        更新品牌提升研究
        
        官方端点: PUT /dsp/measurement/studies/brandLift
        """
        result = await self.put("/dsp/measurement/studies/brandLift", json_data=updates)
        return result if isinstance(result, dict) else {}

    async def get_brand_lift_result(self, study_id: str) -> JSONData:
        """
        获取品牌提升研究结果
        
        官方端点: GET /measurement/studies/brandLift/{studyId}/result
        """
        result = await self.get(f"/measurement/studies/brandLift/{study_id}/result")
        return result if isinstance(result, dict) else {}

    # ============ 创意测试 ============

    async def list_creative_testing_studies(self, **kwargs) -> JSONData:
        """
        列出创意测试研究
        
        官方端点: GET /dsp/measurement/studies/creativeTesting
        """
        result = await self.get("/dsp/measurement/studies/creativeTesting", params=kwargs)
        return result if isinstance(result, dict) else {"studies": []}

    async def create_creative_testing_study(
        self,
        name: str,
        advertiser_id: str,
        **kwargs,
    ) -> JSONData:
        """
        创建创意测试研究
        
        官方端点: POST /dsp/measurement/studies/creativeTesting
        """
        body: JSONData = {"name": name, "advertiserId": advertiser_id}
        body.update(kwargs)
        result = await self.post("/dsp/measurement/studies/creativeTesting", json_data=body)
        return result if isinstance(result, dict) else {}

    async def update_creative_testing_study(
        self,
        study_id: str,
        updates: JSONData,
    ) -> JSONData:
        """
        更新创意测试研究
        
        官方端点: PUT /dsp/measurement/studies/creativeTesting/{studyId}
        """
        result = await self.put(
            f"/dsp/measurement/studies/creativeTesting/{study_id}",
            json_data=updates
        )
        return result if isinstance(result, dict) else {}

    async def get_creative_testing_result(self, study_id: str) -> JSONData:
        """
        获取创意测试结果
        
        官方端点: GET /dsp/measurement/studies/creativeTesting/{studyId}/result
        """
        result = await self.get(f"/dsp/measurement/studies/creativeTesting/{study_id}/result")
        return result if isinstance(result, dict) else {}

    # ============ 全渠道指标 ============

    async def list_omnichannel_metrics_studies(self, **kwargs) -> JSONData:
        """
        列出全渠道指标研究
        
        官方端点: GET /dsp/measurement/studies/omnichannelMetrics
        """
        result = await self.get("/dsp/measurement/studies/omnichannelMetrics", params=kwargs)
        return result if isinstance(result, dict) else {"studies": []}

    async def create_omnichannel_metrics_study(
        self,
        name: str,
        advertiser_id: str,
        **kwargs,
    ) -> JSONData:
        """
        创建全渠道指标研究
        
        官方端点: POST /dsp/measurement/studies/omnichannelMetrics
        """
        body: JSONData = {"name": name, "advertiserId": advertiser_id}
        body.update(kwargs)
        result = await self.post("/dsp/measurement/studies/omnichannelMetrics", json_data=body)
        return result if isinstance(result, dict) else {}

    async def update_omnichannel_metrics_study(self, updates: JSONData) -> JSONData:
        """
        更新全渠道指标研究
        
        官方端点: PUT /dsp/measurement/studies/omnichannelMetrics
        """
        result = await self.put("/dsp/measurement/studies/omnichannelMetrics", json_data=updates)
        return result if isinstance(result, dict) else {}

    async def get_omnichannel_metrics_result(self, study_id: str) -> JSONData:
        """
        获取全渠道指标结果
        
        官方端点: GET /dsp/measurement/studies/omnichannelMetrics/{studyId}/result
        """
        result = await self.get(f"/dsp/measurement/studies/omnichannelMetrics/{study_id}/result")
        return result if isinstance(result, dict) else {}

    # ============ 通用测量 ============

    async def check_planning_eligibility(self, **kwargs) -> JSONData:
        """
        检查规划资格
        
        官方端点: POST /measurement/planning/eligibility
        """
        result = await self.post("/measurement/planning/eligibility", json_data=kwargs)
        return result if isinstance(result, dict) else {}

    async def delete_studies(self, study_ids: list[str]) -> JSONData:
        """
        删除研究
        
        官方端点: DELETE /measurement/studies
        """
        result = await self.delete("/measurement/studies", params={"studyIds": study_ids})
        return result if isinstance(result, dict) else {}

    async def list_studies(self, **kwargs) -> JSONData:
        """
        列出所有研究
        
        官方端点: GET /measurement/studies
        """
        result = await self.get("/measurement/studies", params=kwargs)
        return result if isinstance(result, dict) else {"studies": []}

    # ============ 调研 ============

    async def list_surveys(self, **kwargs) -> JSONData:
        """
        列出调研
        
        官方端点: GET /measurement/studies/surveys
        """
        result = await self.get("/measurement/studies/surveys", params=kwargs)
        return result if isinstance(result, dict) else {"surveys": []}

    async def create_survey(self, survey_data: JSONData) -> JSONData:
        """
        创建调研
        
        官方端点: POST /measurement/studies/surveys
        """
        result = await self.post("/measurement/studies/surveys", json_data=survey_data)
        return result if isinstance(result, dict) else {}

    async def update_survey(self, survey_data: JSONData) -> JSONData:
        """
        更新调研
        
        官方端点: PUT /measurement/studies/surveys
        """
        result = await self.put("/measurement/studies/surveys", json_data=survey_data)
        return result if isinstance(result, dict) else {}

    # ============ 供应商产品 ============

    async def list_vendor_products(self, **kwargs) -> JSONData:
        """
        列出供应商产品
        
        官方端点: POST /measurement/vendorProducts/list
        """
        result = await self.post("/measurement/vendorProducts/list", json_data=kwargs)
        return result if isinstance(result, dict) else {"products": []}

    async def list_omnichannel_brands(self, **kwargs) -> JSONData:
        """
        列出全渠道品牌
        
        官方端点: POST /measurement/vendorProducts/omnichannelMetrics/brands/list
        """
        result = await self.post(
            "/measurement/vendorProducts/omnichannelMetrics/brands/list",
            json_data=kwargs
        )
        return result if isinstance(result, dict) else {"brands": []}

    async def get_vendor_policies(self) -> JSONData:
        """
        获取供应商政策
        
        官方端点: GET /measurement/vendorProducts/policies
        """
        result = await self.get("/measurement/vendorProducts/policies")
        return result if isinstance(result, dict) else {}

    async def get_survey_question_templates(self) -> JSONData:
        """
        获取调研问题模板
        
        官方端点: GET /measurement/vendorProducts/surveyQuestionTemplates
        """
        result = await self.get("/measurement/vendorProducts/surveyQuestionTemplates")
        return result if isinstance(result, dict) else {"templates": []}
