"""Auto-generated Pydantic models. Do not edit manually.

Source: Measurement_prod_3p.json
Title:  Measurement
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class AdTypeV1(StrEnum):
    DSP = "DSP"


class AssetTypeV1M2(StrEnum):
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class AssetV1M2(BaseModel):
    """The Amazon Creative Asset Library asset identifier. Refer https://advertising.amazon.com/API/docs/en-us/creative-asset-library"""
    asset_id: Optional[str] = Field(None, alias="assetId", description="The assetId.")
    asset_type: Optional["AssetTypeV1M2"] = Field(None, alias="assetType")
    version: Optional[str] = Field(None, description="The version of the asset.")

    model_config = {'populate_by_name': True}


class AudienceSelectionOperatorV1M2(StrEnum):
    AND = "AND"
    OR = "OR"


class AudienceSegmentV1M2(BaseModel):
    """The model for holding an Audience Segment."""
    segment_id: Optional[str] = Field(None, alias="segmentId", description="ID for the audience segment. This ID can be fetched from these APIs- https://advertising.amazon.com/API/docs/en-us/audie")

    model_config = {'populate_by_name': True}


class AudienceGroupV1M2(BaseModel):
    """The model for holding Audiece selection within a group. The expression within an audience group will be evaluated using the IntraGroupOperator. The InterGroupOperator will be applied on the output of """
    audience_segments: Optional[list["AudienceSegmentV1M2"]] = Field(None, alias="audienceSegments", description="List of audience segments in this group.")
    inter_group_operator: Optional["AudienceSelectionOperatorV1M2"] = Field(None, alias="interGroupOperator")
    intra_group_operator: Optional["AudienceSelectionOperatorV1M2"] = Field(None, alias="intraGroupOperator")

    model_config = {'populate_by_name': True}


class SurveyQuestionObjectiveTypeV1(StrEnum):
    AD_RECALL = "AD_RECALL"
    ASSOCIATION = "ASSOCIATION"
    ATTITUDES = "ATTITUDES"
    AWARENESS = "AWARENESS"
    BEHAVIORS = "BEHAVIORS"
    FAMILIARITY = "FAMILIARITY"
    FAVORABILITY = "FAVORABILITY"
    INTENT = "INTENT"
    PREFERENCE = "PREFERENCE"


class SurveyResponseResultV1Segmenttype(StrEnum):
    AGE = "AGE"
    AUDIENCES = "AUDIENCES"
    CHANNEL = "CHANNEL"
    FREQUENCY = "FREQUENCY"
    GENDER = "GENDER"
    HOUSEHOLD_INCOME = "HOUSEHOLD_INCOME"
    OVERALL = "OVERALL"


class SurveyResponseResultV1(BaseModel):
    """The rate of response for each response in Survey question."""
    ad_exposed_group_response_rate: Optional[float] = Field(None, alias="adExposedGroupResponseRate", description="The percent of people in ad exposed group choosing this response.")
    control_group_response_rate: Optional[float] = Field(None, alias="controlGroupResponseRate", description="The percent of people in control group choosing this response.")
    is_qualifying_response: Optional[bool] = Field(None, alias="isQualifyingResponse", description="Is the response a qualifying response. Used in calculating Brand Lift.")
    margin_of_error: Optional[float] = Field(None, alias="marginOfError", description="The percentage of margin of error for this response.")
    question_objective: Optional["SurveyQuestionObjectiveTypeV1"] = Field(None, alias="questionObjective")
    question_response: Optional[str] = Field(None, alias="questionResponse", description="The response choosen by Survey audience.")
    question_sequence: Optional[float] = Field(None, alias="questionSequence", description="Sequence number of the question in the Survey.")
    question_text: Optional[str] = Field(None, alias="questionText", description="Text of the Survey question.")
    response_rate: Optional[float] = Field(None, alias="responseRate", description="The percentage of people choosing this response.")
    segment_type: Optional[SurveyResponseResultV1Segmenttype] = Field(None, alias="segmentType", description="The segment type to which this response data belongs to.")
    segment_value: Optional[str] = Field(None, alias="segmentValue", description="The segment value to which this response data belongs to. Would be corresponding to the above segmentType field.")
    statistical_significance: Optional[float] = Field(None, alias="statisticalSignificance", description="The significance percentage for the response data in this segment.")

    model_config = {'populate_by_name': True}


class AudienceResearchStudyResultV1M2(BaseModel):
    """The result of Audience Research study."""
    study_id: Optional[str] = Field(None, alias="studyId", description="The canonical Id of Study.")
    survey_responses: Optional[list["SurveyResponseResultV1"]] = Field(None, alias="surveyResponses", description="Detailed response rate for each response in Survey question aggregated by different segments.")
    total_responses: Optional[float] = Field(None, alias="totalResponses", description="Total number of responses received in the Survey.")

    model_config = {'populate_by_name': True}


class AudienceTargetingGroupV1M2(BaseModel):
    """The model for holding Audiece targeting group. The includedAudienceGroups and excludedAudienceGroups are always joined with AND operator."""
    excluded_audience_groups: Optional[list["AudienceGroupV1M2"]] = Field(None, alias="excludedAudienceGroups", description="List of audience groups to be excluded from the targeted audience.")
    included_audience_groups: Optional[list["AudienceGroupV1M2"]] = Field(None, alias="includedAudienceGroups", description="List of audience groups to be included in the targeted audience.")

    model_config = {'populate_by_name': True}


class VendorTypeV1(StrEnum):
    AMAZON = "AMAZON"


class FundingTypeV1(StrEnum):
    COMPLIMENTARY = "COMPLIMENTARY"


class BaseEligibilityRequestV1(BaseModel):
    """The request object of measurement eligibility check."""
    funding_type_filters: Optional[list["FundingTypeV1"]] = Field(None, alias="fundingTypeFilters", description="FundingType filters to be applied when checking eligibility status. If not supplied we will check against all available ")
    vendor_product_id_filters: Optional[list[str]] = Field(None, alias="vendorProductIdFilters", description="VendorProduct identifier filters to be applied when checking eligibility status. If not supplied we will check against a")
    vendor_type_filters: Optional[list["VendorTypeV1"]] = Field(None, alias="vendorTypeFilters", description="VendorType filters to be applied when checking eligibility status. If not supplied we will check against all available v")

    model_config = {'populate_by_name': True}


class VendorTypeV1M1(StrEnum):
    AMAZON = "AMAZON"
    DYNATA = "DYNATA"
    KANTAR = "KANTAR"
    LUCID = "LUCID"
    MACROMILL = "MACROMILL"
    NIELSEN = "NIELSEN"
    UPWAVE = "UPWAVE"


class FundingTypeV1M1(StrEnum):
    COMPLIMENTARY = "COMPLIMENTARY"
    THIRD_PARTY_PAYMENT = "THIRD_PARTY_PAYMENT"


class BaseEligibilityRequestV1M1(BaseModel):
    """The request object of measurement eligibility check."""
    funding_type_filters: Optional[list["FundingTypeV1M1"]] = Field(None, alias="fundingTypeFilters", description="FundingType filters to be applied when checking eligibility status. If not supplied we will check against all available ")
    vendor_product_id_filters: Optional[list[str]] = Field(None, alias="vendorProductIdFilters", description="VendorProduct identifier filters to be applied when checking eligibility status. If not supplied we will check against a")
    vendor_type_filters: Optional[list["VendorTypeV1M1"]] = Field(None, alias="vendorTypeFilters", description="VendorType filters to be applied when checking eligibility status. If not supplied we will check against all available v")

    model_config = {'populate_by_name': True}


class VendorTypeV1M2(StrEnum):
    AMAZON = "AMAZON"
    OMNICHANNEL_METRICS = "OMNICHANNEL_METRICS"


class FundingTypeV1M2(StrEnum):
    COMPLIMENTARY = "COMPLIMENTARY"
    CPM = "CPM"
    FLAT_RATE = "FLAT_RATE"


class BaseEligibilityRequestV1M2(BaseModel):
    """The request object of measurement eligibility check."""
    funding_type_filters: Optional[list["FundingTypeV1M2"]] = Field(None, alias="fundingTypeFilters", description="FundingType filters to be applied when checking eligibility status. If not supplied we will check against all available ")
    vendor_product_id_filters: Optional[list[str]] = Field(None, alias="vendorProductIdFilters", description="VendorProduct identifier filters to be applied when checking eligibility status. If not supplied we will check against a")
    vendor_type_filters: Optional[list["VendorTypeV1M2"]] = Field(None, alias="vendorTypeFilters", description="VendorType filters to be applied when checking eligibility status. If not supplied we will check against all available v")

    model_config = {'populate_by_name': True}


class VendorTypeV1M3(StrEnum):
    AMAZON = "AMAZON"
    DYNATA = "DYNATA"
    KANTAR = "KANTAR"
    LUCID = "LUCID"
    MACROMILL = "MACROMILL"
    NIELSEN = "NIELSEN"
    OMNICHANNEL_METRICS = "OMNICHANNEL_METRICS"
    UPWAVE = "UPWAVE"


class FundingTypeV1M3(StrEnum):
    COMPLIMENTARY = "COMPLIMENTARY"
    CPM = "CPM"
    THIRD_PARTY_PAYMENT = "THIRD_PARTY_PAYMENT"


class BaseEligibilityRequestV1M3(BaseModel):
    """The request object of measurement eligibility check."""
    funding_type_filters: Optional[list["FundingTypeV1M3"]] = Field(None, alias="fundingTypeFilters", description="FundingType filters to be applied when checking eligibility status. If not supplied we will check against all available ")
    vendor_product_id_filters: Optional[list[str]] = Field(None, alias="vendorProductIdFilters", description="VendorProduct identifier filters to be applied when checking eligibility status. If not supplied we will check against a")
    vendor_type_filters: Optional[list["VendorTypeV1M3"]] = Field(None, alias="vendorTypeFilters", description="VendorType filters to be applied when checking eligibility status. If not supplied we will check against all available v")

    model_config = {'populate_by_name': True}


class StudySubmissionTypeV1(StrEnum):
    DRAFT = "DRAFT"
    SUBMISSION = "SUBMISSION"


class StudyStatusV1(StrEnum):
    APPROVED = "APPROVED"
    CANCELLED = "CANCELLED"
    DRAFT = "DRAFT"
    ENDED = "ENDED"
    INFEASIBLE = "INFEASIBLE"
    PENDING = "PENDING"
    REJECTED = "REJECTED"
    RUNNING = "RUNNING"


class BaseStudyV1Studyresultstatus(StrEnum):
    AVAILABLE = "AVAILABLE"


class BaseStudyV1(BaseModel):
    """The base study object."""
    comment: Optional[str] = Field(None, description="The approver's comment on why the study is approved/rejected.")
    create_date: Optional[str] = Field(None, alias="createDate", description="The study creation date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC.")
    end_date: Optional[str] = Field(None, alias="endDate", description="The study end date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. By default this will be the latest endDate o")
    external_reference_id: Optional[str] = Field(None, alias="externalReferenceId", description="Optional field. For some vendors, advertisers are required to provide this vendor assigned reference identifier for EXTE")
    id_: Optional[str] = Field(None, alias="id", description="The study canonical identifier. Immutable field. This is required for update.")
    last_updated_date: Optional[str] = Field(None, alias="lastUpdatedDate", description="The study last updated date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC.")
    name: Optional[str] = Field(None, description="The study name.")
    rejection_reasons: Optional[list[str]] = Field(None, alias="rejectionReasons", description="List of reasons for rejection, this will only be available if the status is REJECTED. This field is deprecated, use stat")
    review_date: Optional[str] = Field(None, alias="reviewDate", description="The study review date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The study start date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. By default this will be the earliest start")
    status: Optional["StudyStatusV1"] = None
    status_reasons: Optional[list[str]] = Field(None, alias="statusReasons", description="List of reasons for study status. For example, when study is marked Rejected or Ineligible, this field would be availabl")
    study_result_status: Optional[BaseStudyV1Studyresultstatus] = Field(None, alias="studyResultStatus", description="The status of result of the study.")
    submission_type: Optional["StudySubmissionTypeV1"] = Field(None, alias="submissionType")
    survey_id: Optional[str] = Field(None, alias="surveyId", description="The study survey canonical identifier.")
    vendor_product_id: Optional[str] = Field(None, alias="vendorProductId", description="Associated vendor product canonical identifier.")

    model_config = {'populate_by_name': True}


class ResourceLinkV1M1(BaseModel):
    """The link that can be used to access corresponding resources in advertising portal."""
    name: Optional[str] = Field(None, description="The resource name.")
    url: Optional[str] = Field(None, description="The resource url.")

    model_config = {'populate_by_name': True}


class BaseStudyV1M1Studyresultstatus(StrEnum):
    AVAILABLE = "AVAILABLE"


class BaseStudyV1M1(BaseModel):
    """The base study object."""
    comment: Optional[str] = Field(None, description="The approver's comment on why the study is approved/rejected.")
    create_date: Optional[str] = Field(None, alias="createDate", description="The study creation date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC.")
    end_date: Optional[str] = Field(None, alias="endDate", description="The study end date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. By default this will be the latest endDate o")
    external_reference_id: Optional[str] = Field(None, alias="externalReferenceId", description="Optional field. For some vendors, advertisers are required to provide this vendor assigned reference identifier for EXTE")
    id_: Optional[str] = Field(None, alias="id", description="The study canonical identifier. Immutable field. This is required for update.")
    last_updated_date: Optional[str] = Field(None, alias="lastUpdatedDate", description="The study last updated date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC.")
    links: Optional[list["ResourceLinkV1M1"]] = None
    name: Optional[str] = Field(None, description="The study name.")
    rejection_reasons: Optional[list[str]] = Field(None, alias="rejectionReasons", description="List of reasons for rejection, this will only be available if the status is REJECTED. This field is deprecated, use stat")
    review_date: Optional[str] = Field(None, alias="reviewDate", description="The study review date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The study start date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. By default this will be the earliest start")
    status: Optional["StudyStatusV1"] = None
    status_reasons: Optional[list[str]] = Field(None, alias="statusReasons", description="List of reasons for study status. For example, when study is marked Rejected or Ineligible, this field would be availabl")
    study_result_status: Optional[BaseStudyV1M1Studyresultstatus] = Field(None, alias="studyResultStatus", description="The status of result of the study.")
    submission_type: Optional["StudySubmissionTypeV1"] = Field(None, alias="submissionType")
    survey_id: Optional[str] = Field(None, alias="surveyId", description="The study survey canonical identifier.")
    vendor_product_id: Optional[str] = Field(None, alias="vendorProductId", description="Associated vendor product canonical identifier.")

    model_config = {'populate_by_name': True}


class BaseStudyV1M2Studyresultstatus(StrEnum):
    AVAILABLE = "AVAILABLE"


class BaseStudyV1M2(BaseModel):
    """The base study object."""
    comment: Optional[str] = Field(None, description="The approver's comment on why the study is approved/rejected.")
    create_date: Optional[str] = Field(None, alias="createDate", description="The study creation date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC.")
    end_date: Optional[str] = Field(None, alias="endDate", description="The study end date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. By default this will be the latest endDate o")
    external_reference_id: Optional[str] = Field(None, alias="externalReferenceId", description="Optional field. For some vendors, advertisers are required to provide this vendor assigned reference identifier for EXTE")
    last_updated_date: Optional[str] = Field(None, alias="lastUpdatedDate", description="The study last updated date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC.")
    name: Optional[str] = Field(None, description="The study name.")
    review_date: Optional[str] = Field(None, alias="reviewDate", description="The study review date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The study start date in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC. By default this will be the earliest start")
    status: Optional["StudyStatusV1"] = None
    status_reasons: Optional[list[str]] = Field(None, alias="statusReasons", description="List of reasons for study status. For example, when study is marked Rejected or Ineligible, this field would be availabl")
    study_result_status: Optional[BaseStudyV1M2Studyresultstatus] = Field(None, alias="studyResultStatus", description="The status of result of the study.")
    survey_id: Optional[str] = Field(None, alias="surveyId", description="The study survey canonical identifier.")
    vendor_product_id: Optional[str] = Field(None, alias="vendorProductId", description="Associated vendor product canonical identifier.")

    model_config = {'populate_by_name': True}


class BenchmarkCategoryV1(StrEnum):
    APPLIANCES = "APPLIANCES"
    APPS_AND_GAMES = "APPS_AND_GAMES"
    ARTS_CRAFTS_AND_SEWING = "ARTS_CRAFTS_AND_SEWING"
    AUTOMOTIVE = "AUTOMOTIVE"
    BABY = "BABY"
    BEAUTY_AND_PERSONAL_CARE = "BEAUTY_AND_PERSONAL_CARE"
    BEVERAGES = "BEVERAGES"
    BOOKS = "BOOKS"
    CELL_PHONES_AND_ACCESSORIES = "CELL_PHONES_AND_ACCESSORIES"
    CLOTHING_SHOES_AND_JEWELRY = "CLOTHING_SHOES_AND_JEWELRY"
    COMPUTERS_AND_ACCESSORIES = "COMPUTERS_AND_ACCESSORIES"
    DIGITAL_MUSIC = "DIGITAL_MUSIC"
    EDUCATION = "EDUCATION"
    ELECTRONICS = "ELECTRONICS"
    FINANCIAL_AND_INSURANCE = "FINANCIAL_AND_INSURANCE"
    FOOD = "FOOD"
    HEALTH_AND_HOUSEHOLD = "HEALTH_AND_HOUSEHOLD"
    HOME_AND_KITCHEN = "HOME_AND_KITCHEN"
    HOSPITALITY = "HOSPITALITY"
    KITCHEN_AND_DINING = "KITCHEN_AND_DINING"
    MOVIES_AND_TV = "MOVIES_AND_TV"
    OFFICE_PRODUCTS = "OFFICE_PRODUCTS"
    PATIO_LAWN_AND_GARDEN = "PATIO_LAWN_AND_GARDEN"
    PET_SUPPLIES = "PET_SUPPLIES"
    RESTAURANTS = "RESTAURANTS"
    SOFTWARE = "SOFTWARE"
    SPORTS_AND_OUTDOORS = "SPORTS_AND_OUTDOORS"
    TELECOMMUNICATIONS_SERVICES = "TELECOMMUNICATIONS_SERVICES"
    TOOLS_AND_HOME_IMPROVEMENT = "TOOLS_AND_HOME_IMPROVEMENT"
    TOYS_AND_GAMES = "TOYS_AND_GAMES"
    VIDEO_GAMES = "VIDEO_GAMES"


class BrandLiftSummaryV1(BaseModel):
    """Summary of Brand Lift achieved for an objective."""
    ad_exposed_group_rate: Optional[float] = Field(None, alias="adExposedGroupRate", description="Ad exposed group response rate.")
    benchmark_lift_rate: Optional[float] = Field(None, alias="benchmarkLiftRate", description="The benchmark lift rate for the selected product category in the Survey.")
    control_group_rate: Optional[float] = Field(None, alias="controlGroupRate", description="Control group response rate.")
    qualifying_responses: Optional[list[str]] = Field(None, alias="qualifyingResponses", description="Qualifying responses aggregated to measure the Brand Lift.")
    question_objective: Optional["SurveyQuestionObjectiveTypeV1"] = Field(None, alias="questionObjective")
    question_text: Optional[str] = Field(None, alias="questionText", description="Text of the Survey question.")
    statistical_significance: Optional[float] = Field(None, alias="statisticalSignificance", description="The significance percentage of achieved Brand Lift.")

    model_config = {'populate_by_name': True}


class BrandLiftStudyResultV1(BaseModel):
    """The result of Brand Lift study."""
    brand_lift_summary: Optional[list["BrandLiftSummaryV1"]] = Field(None, alias="brandLiftSummary", description="Summary of Brand Lift achieved for each objective.")
    study_id: Optional[str] = Field(None, alias="studyId", description="The canonical Id of Study.")
    survey_responses: Optional[list["SurveyResponseResultV1"]] = Field(None, alias="surveyResponses", description="Detailed response rate for each response in Survey question aggregated by different segments.")
    total_responses: Optional[float] = Field(None, alias="totalResponses", description="Total number of responses received in the Survey.")

    model_config = {'populate_by_name': True}


class SurveyQuestionObjectiveTypeV1M1(StrEnum):
    AD_RECALL = "AD_RECALL"
    AGE = "AGE"
    AMAZON_SERVICE_USAGE = "AMAZON_SERVICE_USAGE"
    ATTITUDES = "ATTITUDES"
    AWARENESS = "AWARENESS"
    BEHAVIORS = "BEHAVIORS"
    CHILDREN_IN_HOUSEHOLD = "CHILDREN_IN_HOUSEHOLD"
    CONSIDERATION = "CONSIDERATION"
    EDUCATION = "EDUCATION"
    ETHNICITY = "ETHNICITY"
    FAMILIARITY = "FAMILIARITY"
    FAVORABILITY = "FAVORABILITY"
    GENDER = "GENDER"
    HOUSEHOLD_INCOME = "HOUSEHOLD_INCOME"
    HOUSEHOLD_SIZE = "HOUSEHOLD_SIZE"
    INTENT = "INTENT"
    IN_MARKET_STATUS = "IN_MARKET_STATUS"
    PREFERENCE = "PREFERENCE"
    PURCHASE_FREQUENCY = "PURCHASE_FREQUENCY"
    PURCHASE_HISTORY = "PURCHASE_HISTORY"
    PURCHASE_LOCATION = "PURCHASE_LOCATION"
    TIME_ONLINE = "TIME_ONLINE"
    TV_MEDIA_CONSUMPTION = "TV_MEDIA_CONSUMPTION"
    UNAIDED_AWARENESS = "UNAIDED_AWARENESS"


class BrandLiftSummaryV1M1(BaseModel):
    """Summary of Brand Lift achieved for an objective."""
    ad_exposed_group_rate: Optional[float] = Field(None, alias="adExposedGroupRate", description="Ad exposed group response rate.")
    benchmark_lift_rate: Optional[float] = Field(None, alias="benchmarkLiftRate", description="The benchmark lift rate for the selected product category in the Survey.")
    control_group_rate: Optional[float] = Field(None, alias="controlGroupRate", description="Control group response rate.")
    qualifying_responses: Optional[list[str]] = Field(None, alias="qualifyingResponses", description="Qualifying responses aggregated to measure the Brand Lift.")
    question_objective: Optional["SurveyQuestionObjectiveTypeV1M1"] = Field(None, alias="questionObjective")
    question_text: Optional[str] = Field(None, alias="questionText", description="Text of the Survey question.")
    statistical_significance: Optional[float] = Field(None, alias="statisticalSignificance", description="The significance percentage of achieved Brand Lift.")

    model_config = {'populate_by_name': True}


class SurveyResponseResultV1M1Segmenttype(StrEnum):
    AGE = "AGE"
    AUDIENCES = "AUDIENCES"
    CHANNEL = "CHANNEL"
    FREQUENCY = "FREQUENCY"
    GENDER = "GENDER"
    HOUSEHOLD_INCOME = "HOUSEHOLD_INCOME"
    OVERALL = "OVERALL"


class SurveyResponseResultV1M1(BaseModel):
    """The rate of response for each response in Survey question."""
    ad_exposed_group_response_rate: Optional[float] = Field(None, alias="adExposedGroupResponseRate", description="The percent of people in ad exposed group choosing this response.")
    control_group_response_rate: Optional[float] = Field(None, alias="controlGroupResponseRate", description="The percent of people in control group choosing this response.")
    is_qualifying_response: Optional[bool] = Field(None, alias="isQualifyingResponse", description="Is the response a qualifying response. Used in calculating Brand Lift.")
    question_objective: Optional["SurveyQuestionObjectiveTypeV1M1"] = Field(None, alias="questionObjective")
    question_response: Optional[str] = Field(None, alias="questionResponse", description="The response choosen by Survey audience.")
    question_sequence: Optional[float] = Field(None, alias="questionSequence", description="Sequence number of the question in the Survey.")
    question_text: Optional[str] = Field(None, alias="questionText", description="Text of the Survey question.")
    response_rate: Optional[float] = Field(None, alias="responseRate", description="The percentage of people choosing this response.")
    segment_type: Optional[SurveyResponseResultV1M1Segmenttype] = Field(None, alias="segmentType", description="The segment type to which this response data belongs to.")
    segment_value: Optional[str] = Field(None, alias="segmentValue", description="The segment value to which this response data belongs to. Would be corresponding to the above segmentType field.")
    statistical_significance: Optional[float] = Field(None, alias="statisticalSignificance", description="The significance percentage for the response data in this segment.")

    model_config = {'populate_by_name': True}


class BrandLiftStudyResultV1M1(BaseModel):
    """The result of Brand Lift study."""
    brand_lift_summary: Optional[list["BrandLiftSummaryV1M1"]] = Field(None, alias="brandLiftSummary", description="Summary of Brand Lift achieved for each objective.")
    study_id: Optional[str] = Field(None, alias="studyId", description="The canonical Id of Study.")
    survey_responses: Optional[list["SurveyResponseResultV1M1"]] = Field(None, alias="surveyResponses", description="Detailed response rate for each response in Survey question aggregated by different segments.")
    total_responses: Optional[float] = Field(None, alias="totalResponses", description="Total number of responses received in the Survey.")

    model_config = {'populate_by_name': True}


class DSPCampaignPlanningMetadataV1M2(BaseModel):
    """The basic model for all DSP CAMPAIGN_PLANNING objective studies."""
    advertiser_id: Optional[str] = Field(None, alias="advertiserId", description="The associated advertiser identifier. Immutable field.")

    model_config = {'populate_by_name': True}


class DSPAudienceResearchMetadataV1M2(BaseModel):
    """The basic model for all DSP AUDIENCE_RESEARCH objective studies."""
    audience_targeting_group: Optional["AudienceTargetingGroupV1M2"] = Field(None, alias="audienceTargetingGroup")
    brand_name: Optional[str] = Field(None, alias="brandName", description="The study brand name.")
    peer_names: Optional[list[str]] = Field(None, alias="peerNames", description="A list of peer names for the study brand.")
    product_category: Optional[str] = Field(None, alias="productCategory", description="The study product category.")

    model_config = {'populate_by_name': True}


class CreateDSPAudienceResearchStudyV1M2(BaseModel):
    """Create DSP AUDIENCE_RESEARCH study object."""
    pass


class DSPCreativeTestingMetadataV1M2(BaseModel):
    """The basic model for all DSP CREATIVE_TESTING objective studies."""
    assets: Optional[list["AssetV1M2"]] = Field(None, description="A list of assets to be used for the creative testing study as part of either the survey question or the response. In cas")
    audience_targeting_group: Optional["AudienceTargetingGroupV1M2"] = Field(None, alias="audienceTargetingGroup")
    brand_name: Optional[str] = Field(None, alias="brandName", description="The study brand name.")
    product_category: Optional[str] = Field(None, alias="productCategory", description="Optional study product category.")

    model_config = {'populate_by_name': True}


class CreateDSPCreativeTestingStudyV1M2(BaseModel):
    """Create DSP CREATIVE_TESTING study object."""
    pass


class SurveyQuestionResponseV1M2Responsetype(StrEnum):
    ASSET = "ASSET"
    TEXT = "TEXT"


class SurveyQuestionResponseV1M2(BaseModel):
    """The survey question response chosen by Survey audience."""
    asset: Optional["AssetV1M2"] = None
    response_type: Optional[SurveyQuestionResponseV1M2Responsetype] = Field(None, alias="responseType", description="The type of response.")
    response_value: Optional[str] = Field(None, alias="responseValue", description="The response text if the question response type is TEXT.")

    model_config = {'populate_by_name': True}


class SurveyResponseResultV1M2Segmenttype(StrEnum):
    AGE = "AGE"
    AUDIENCES = "AUDIENCES"
    CHANNEL = "CHANNEL"
    FREQUENCY = "FREQUENCY"
    GENDER = "GENDER"
    HOUSEHOLD_INCOME = "HOUSEHOLD_INCOME"
    OVERALL = "OVERALL"


class SurveyResponseResultV1M2(BaseModel):
    """The rate of response for each response in Survey question."""
    ad_exposed_group_response_rate: Optional[float] = Field(None, alias="adExposedGroupResponseRate", description="The percent of people in ad exposed group choosing this response.")
    control_group_response_rate: Optional[float] = Field(None, alias="controlGroupResponseRate", description="The percent of people in control group choosing this response.")
    is_qualifying_response: Optional[bool] = Field(None, alias="isQualifyingResponse", description="Is the response a qualifying response. Used in calculating Brand Lift.")
    margin_of_error: Optional[float] = Field(None, alias="marginOfError", description="The percentage of margin of error for this response.")
    question_asset: Optional["AssetV1M2"] = Field(None, alias="questionAsset")
    question_objective: Optional["SurveyQuestionObjectiveTypeV1"] = Field(None, alias="questionObjective")
    question_response: Optional["SurveyQuestionResponseV1M2"] = Field(None, alias="questionResponse")
    question_sequence: Optional[float] = Field(None, alias="questionSequence", description="Sequence number of the question in the Survey.")
    question_text: Optional[str] = Field(None, alias="questionText", description="Text of the Survey question.")
    response_rate: Optional[float] = Field(None, alias="responseRate", description="The percentage of people choosing this response.")
    segment_type: Optional[SurveyResponseResultV1M2Segmenttype] = Field(None, alias="segmentType", description="The segment type to which this response data belongs to.")
    segment_value: Optional[str] = Field(None, alias="segmentValue", description="The segment value to which this response data belongs to. Would be corresponding to the above segmentType field.")
    statistical_significance: Optional[float] = Field(None, alias="statisticalSignificance", description="The significance percentage for the response data in this segment.")

    model_config = {'populate_by_name': True}


class CreativeTestingStudyResultV1M2(BaseModel):
    """The result of Creative Testing study."""
    study_id: Optional[str] = Field(None, alias="studyId", description="The canonical Id of Study.")
    survey_responses: Optional[list["SurveyResponseResultV1M2"]] = Field(None, alias="surveyResponses", description="Detailed response rate for each response in Survey question aggregated by different segments.")
    total_responses: Optional[float] = Field(None, alias="totalResponses", description="Total number of responses received in the Survey.")

    model_config = {'populate_by_name': True}


class SurveyQuestionTypeV1(StrEnum):
    FREE_TEXT = "FREE_TEXT"
    MULTI_SELECT = "MULTI_SELECT"
    RATING = "RATING"
    SINGLE_ASSET_SELECT = "SINGLE_ASSET_SELECT"
    SINGLE_SELECT = "SINGLE_SELECT"


class CustomSurveyQuestionV1(BaseModel):
    """The templated measurement survey question."""
    question_text: Optional[str] = Field(None, alias="questionText", description="The survey question text.")
    responses: Optional[list[str]] = None
    type_: Optional["SurveyQuestionTypeV1"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class DSPAudienceResearchEligibilityDataV1M2(BaseModel):
    """The audience research study eligibility data."""
    audience_targeting_group: Optional["AudienceTargetingGroupV1M2"] = Field(None, alias="audienceTargetingGroup")

    model_config = {'populate_by_name': True}


class DSPAudienceResearchEligibilityRequestV1M2(BaseModel):
    """The request object of DSP Audience Research study eligibility check."""
    pass


class DSPAudienceResearchStudyV1M2(BaseModel):
    """DSP AUDIENCE_RESEARCH study object."""
    pass


class DSPBrandLiftEligibilityDataV1(BaseModel):
    """The campaign study eligibility data."""
    current_study_id: Optional[str] = Field(None, alias="currentStudyId", description="Optional current study identifier, if provided orders are expected to be added into this study and the orders already as")
    excluded_line_item_ids: Optional[list[str]] = Field(None, alias="excludedLineItemIds", description="A list of canonical lineItem identifiers that are excluded from the eligibility check.")
    order_ids: Optional[list[str]] = Field(None, alias="orderIds", description="A list of canonical order identifiers. By default all lineItems in those orders will be included.")

    model_config = {'populate_by_name': True}


class DSPBrandLiftEligibilityRequestV1(BaseModel):
    """The request object of DSP brand lift eligibility check."""
    pass


class DSPBrandLiftEligibilityRequestV1M1(BaseModel):
    """The request object of DSP brand lift eligibility check."""
    pass


class DSPBrandLiftMetadataV1(BaseModel):
    """The basic model for all DSP BRAND_LIFT objective studies."""
    benchmark_category: Optional["BenchmarkCategoryV1"] = Field(None, alias="benchmarkCategory")
    brand_name: Optional[str] = Field(None, alias="brandName", description="The study brand name.")
    peer_names: Optional[list[str]] = Field(None, alias="peerNames", description="A list of peer names for the study brand.")
    product_category: Optional[str] = Field(None, alias="productCategory", description="The study product category.")

    model_config = {'populate_by_name': True}


class DSPBrandLiftMetadataV1M1(BaseModel):
    """The basic model for all DSP BRAND_LIFT objective studies."""
    benchmark_category: Optional["BenchmarkCategoryV1"] = Field(None, alias="benchmarkCategory")
    brand_name: Optional[str] = Field(None, alias="brandName", description="The study brand name.")
    peer_names: Optional[list[str]] = Field(None, alias="peerNames", description="A list of peer names for the study brand.")
    product_category: Optional[str] = Field(None, alias="productCategory", description="The study product category.")
    verb: Optional[str] = Field(None, description="The verb that will be used in the applicable survey questions to construct the question text.")

    model_config = {'populate_by_name': True}


class DSPCampaignMeasurementMetadataV1(BaseModel):
    """The basic model for all DSP CAMPAIGN_MEASUREMENT objective studies."""
    advertiser_id: Optional[str] = Field(None, alias="advertiserId", description="The associated advertiser identifier. Immutable field.")
    excluded_line_item_ids: Optional[list[str]] = Field(None, alias="excludedLineItemIds", description="A list of canonical lineItem identifiers that are excluded from the study.")
    order_ids: Optional[list[str]] = Field(None, alias="orderIds", description="A list of canonical order identifiers that are associated with the study. By default all lineItems in those orders will ")

    model_config = {'populate_by_name': True}


class DSPBrandLiftStudyV1(BaseModel):
    """DSP BRAND_LIFT study object."""
    pass


class DSPCampaignMeasurementMetadataV1M1(BaseModel):
    """The basic model for all DSP CAMPAIGN_MEASUREMENT objective studies."""
    advertiser_id: Optional[str] = Field(None, alias="advertiserId", description="The associated advertiser identifier. Immutable field.")
    excluded_line_item_ids: Optional[list[str]] = Field(None, alias="excludedLineItemIds", description="A list of canonical lineItem identifiers that are excluded from the study.")
    order_ids: Optional[list[str]] = Field(None, alias="orderIds", description="A list of canonical order identifiers that are associated with the study. By default all lineItems in those orders will ")

    model_config = {'populate_by_name': True}


class DSPBrandLiftStudyV1M1(BaseModel):
    """DSP BRAND_LIFT study object."""
    pass


class DSPCreativeTestingEligibilityDataV1M2(BaseModel):
    """The creative testing study eligibility data."""
    audience_targeting_group: Optional["AudienceTargetingGroupV1M2"] = Field(None, alias="audienceTargetingGroup")

    model_config = {'populate_by_name': True}


class DSPCreativeTestingEligibilityRequestV1M2(BaseModel):
    """The request object of DSP Creative Testing study eligibility check."""
    pass


class DSPCreativeTestingStudyV1M2(BaseModel):
    """DSP CREATIVE_TESTING study object."""
    pass


class DSPOmnichannelMetricsEligibilityDataV1M2(BaseModel):
    """The campaign study eligibility data."""
    brand_ids: Optional[list[str]] = Field(None, alias="brandIds", description="A list of canonical brand identifiers.")
    current_study_id: Optional[str] = Field(None, alias="currentStudyId", description="Optional current study identifier. If provided orders are expected to be added into this study and the orders already as")
    excluded_line_item_ids: Optional[list[str]] = Field(None, alias="excludedLineItemIds", description="A list of canonical lineItem identifiers that are excluded from the eligibility check.")
    order_ids: Optional[list[str]] = Field(None, alias="orderIds", description="A list of canonical order identifiers. By default all lineItems in those orders will be included.")

    model_config = {'populate_by_name': True}


class DSPOmnichannelMetricsEligibilityRequestV1M2(BaseModel):
    """The request object of DSP omnichannel metrics eligibility check."""
    pass


class DSPOmnichannelMetricsEligibilityRequestV1M3(BaseModel):
    """The request object of DSP omnichannel metrics eligibility check."""
    pass


class DSPOmnichannelMetricsMetadataV1M2(BaseModel):
    """The basic model for all DSP OMNICHANNEL_METRICS objective studies."""
    brand_ids: Optional[list[str]] = Field(None, alias="brandIds", description="A list of canonical brand ids to be tracked for off-Amazon conversions.")

    model_config = {'populate_by_name': True}


class DSPOmnichannelMetricsStudyV1M2(BaseModel):
    """DSP OMNICHANNEL_METRICS study object."""
    pass


class DSPOmnichannelMetricsStudyV1M3(BaseModel):
    """DSP OMNICHANNEL_METRICS study object."""
    pass


class EligibilityFieldV1(StrEnum):
    BUDGET = "BUDGET"
    END_TIME = "END_TIME"
    FLIGHT_LENGTH = "FLIGHT_LENGTH"
    GOAL = "GOAL"
    IMPRESSIONS = "IMPRESSIONS"
    LEAD_TIME = "LEAD_TIME"
    LOCALE = "LOCALE"
    ORDER = "ORDER"
    START_TIME = "START_TIME"


class EligibilityFieldV1M2(StrEnum):
    BUDGET = "BUDGET"
    BUYER_COUNT = "BUYER_COUNT"
    END_TIME = "END_TIME"
    FLIGHT_LENGTH = "FLIGHT_LENGTH"
    GOAL = "GOAL"
    IMPRESSIONS = "IMPRESSIONS"
    INDUSTRY = "INDUSTRY"
    LEAD_TIME = "LEAD_TIME"
    LOCALE = "LOCALE"
    ORDER = "ORDER"
    START_TIME = "START_TIME"


class EligibilityIssueSeverityV1(StrEnum):
    ERROR = "ERROR"
    WARNING = "WARNING"


class EligibilityIssueV1(BaseModel):
    """The list of eligibility issues."""
    code: Optional[str] = Field(None, description="An enumerated issue code for machine use.")
    field: Optional["EligibilityFieldV1"] = None
    message: Optional[str] = Field(None, description="A human-readable description of the issue with suggestions on how to resolve the issue.")
    severity: Optional["EligibilityIssueSeverityV1"] = None

    model_config = {'populate_by_name': True}


class EligibilityIssueV1M2(BaseModel):
    """The list of eligibility issues."""
    code: Optional[str] = Field(None, description="An enumerated issue code for machine use.")
    field: Optional["EligibilityFieldV1M2"] = None
    message: Optional[str] = Field(None, description="A human-readable description of the issue with suggestions on how to resolve the issue.")
    severity: Optional["EligibilityIssueSeverityV1"] = None

    model_config = {'populate_by_name': True}


class EligibilityMetadataV1(BaseModel):
    """The eligibility metadata."""
    budget: Optional[float] = Field(None, description="The total budget. Expressed in dollars.")
    end_date: Optional[str] = Field(None, alias="endDate", description="The latest end date of the associated orders in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC.")
    flight_length: Optional[int] = Field(None, alias="flightLength", description="The flight length of the associated orders. Expressed in days.")
    impressions: Optional[int] = Field(None, description="The total estimated impressions.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The earliest start date of associated orders in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC.")

    model_config = {'populate_by_name': True}


class EligibilityStatusV1(StrEnum):
    ELIGIBLE = "ELIGIBLE"
    ELIGIBLE_WITH_WARNING = "ELIGIBLE_WITH_WARNING"
    INELIGIBLE = "INELIGIBLE"


class VendorProductEligibilityV1(BaseModel):
    """The measurement eligibility details for a certain vendor product."""
    issues: Optional[list["EligibilityIssueV1"]] = Field(None, description="A list of issues will be provided if the status is INELIGIBLE or ELIGIBLE_WITH_WARNING.")
    status: Optional["EligibilityStatusV1"] = None
    vendor_product_id: Optional[str] = Field(None, alias="vendorProductId", description="vendor product canonical identifier.")

    model_config = {'populate_by_name': True}


class EligibilityResponseV1(BaseModel):
    """The eligibility check response object."""
    metadata: Optional["EligibilityMetadataV1"] = None
    next_token: Optional[str] = Field(None, alias="nextToken")
    vendor_product_eligibilities: Optional[list["VendorProductEligibilityV1"]] = Field(None, alias="vendorProductEligibilities")

    model_config = {'populate_by_name': True}


class VendorProductEligibilityV1M2(BaseModel):
    """The measurement eligibility details for a certain vendor product."""
    issues: Optional[list["EligibilityIssueV1M2"]] = Field(None, description="A list of issues will be provided if the status is INELIGIBLE or ELIGIBLE_WITH_WARNING.")
    status: Optional["EligibilityStatusV1"] = None
    vendor_product_id: Optional[str] = Field(None, alias="vendorProductId", description="vendor product canonical identifier.")

    model_config = {'populate_by_name': True}


class EligibilityResponseV1M2(BaseModel):
    """The eligibility check response object."""
    metadata: Optional["EligibilityMetadataV1"] = None
    next_token: Optional[str] = Field(None, alias="nextToken")
    vendor_product_eligibilities: Optional[list["VendorProductEligibilityV1M2"]] = Field(None, alias="vendorProductEligibilities")

    model_config = {'populate_by_name': True}


class SubErrorV1(BaseModel):
    """The sub error object."""
    error_type: str = Field(..., alias="errorType")
    field_name: Optional[str] = Field(None, alias="fieldName")
    message: str

    model_config = {'populate_by_name': True}


class ErrorV1(BaseModel):
    """The error response object."""
    errors: Optional[list["SubErrorV1"]] = None
    message: Optional[str] = Field(None, description="A human-readable description of the response.")
    request_id: Optional[str] = Field(None, alias="requestId", description="Request Id that uniquely identifies your request.")

    model_config = {'populate_by_name': True}


class SurveyQuestionPlaceholderFieldValueV1(BaseModel):
    is_qualifying: Optional[bool] = Field(None, alias="isQualifying", description="This is only required if the corresponding field is 'response', this will help to define if the response value will be c")
    value: Optional[str] = Field(None, description="The survey question placeholder field value.")

    model_config = {'populate_by_name': True}


class GridQuestionResponsesV1M1(BaseModel):
    """The grid question response object. Only applicable for SINGLE_SELECT_GRID type question."""
    columns: Optional[list["SurveyQuestionPlaceholderFieldValueV1"]] = None
    rows: Optional[list["SurveyQuestionPlaceholderFieldValueV1"]] = None

    model_config = {'populate_by_name': True}


class MeasurementCountryV1(StrEnum):
    AE = "AE"
    AU = "AU"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    ES = "ES"
    FR = "FR"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    UK = "UK"
    US = "US"


class MeasurementGoalV1(StrEnum):
    AWARENESS = "AWARENESS"
    CONSIDERATIONS_ON_AMAZON = "CONSIDERATIONS_ON_AMAZON"
    CONVERSIONS_OFF_AMAZON = "CONVERSIONS_OFF_AMAZON"
    ENGAGEMENT_WITH_MY_AD = "ENGAGEMENT_WITH_MY_AD"
    MOBILE_APP_INSTALLS = "MOBILE_APP_INSTALLS"
    PURCHASES_ON_AMAZON = "PURCHASES_ON_AMAZON"


class MeasurementLocaleV1(StrEnum):
    DE_DE = "DE_DE"
    EN_CA = "EN_CA"
    EN_GB = "EN_GB"
    EN_US = "EN_US"
    ES_ES = "ES_ES"
    ES_MX = "ES_MX"
    FR_FR = "FR_FR"
    IT_IT = "IT_IT"
    PT_BR = "PT_BR"


class MeasurementMarketplaceV1(BaseModel):
    """The marketplace with corresponding rules."""
    country: Optional["MeasurementCountryV1"] = None
    minimum_budget: Optional[float] = Field(None, alias="minimumBudget", description="The minimum budget. Expressed in dollars.")
    minimum_impressions: Optional[int] = Field(None, alias="minimumImpressions", description="The minimum impressions.")
    supported_locales: Optional[list["MeasurementLocaleV1"]] = Field(None, alias="supportedLocales")

    model_config = {'populate_by_name': True}


class OmnichannelMetricsBrandSearchRequestV1M2(BaseModel):
    """The request object to fetch brands to be used in the OMNICHANNEL_METRICS vendor product."""
    brand_id_filter: Optional[list[str]] = Field(None, alias="brandIdFilter", description="List of brandIds in the omnichannel metrics brand catalog. Either one of brandIdFilter or brandNameSearch should be prov")
    brand_name_search: Optional[str] = Field(None, alias="brandNameSearch", description="Text to search for eligible brands in the omnichannel metrics brand catalog. Either one of brandIdFilter or brandNameSea")

    model_config = {'populate_by_name': True}


class OmnichannelMetricsBrandV1M2(BaseModel):
    brand: Optional[str] = Field(None, description="The brand name.")
    category: Optional[str] = None
    company: Optional[str] = None
    id_: Optional[str] = Field(None, alias="id", description="The brand canonical Id")
    major_brand: Optional[str] = Field(None, alias="majorBrand")
    manufacturer: Optional[str] = None
    subcategory: Optional[str] = None

    model_config = {'populate_by_name': True}


class PaginatedBaseStudiesV1(BaseModel):
    """A list of studies."""
    measurements: Optional[list["BaseStudyV1"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class PaginatedBaseStudiesV1M1(BaseModel):
    """A list of studies."""
    measurements: Optional[list["BaseStudyV1M1"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class PaginatedDSPAudienceResearchStudiesV1M2(BaseModel):
    """A list of audience research studies."""
    measurements: Optional[list["DSPAudienceResearchStudyV1M2"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class PaginatedDSPBrandLiftStudiesV1(BaseModel):
    """A list of studies."""
    measurements: Optional[list["DSPBrandLiftStudyV1"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class PaginatedDSPBrandLiftStudiesV1M1(BaseModel):
    """A list of studies."""
    measurements: Optional[list["DSPBrandLiftStudyV1M1"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class PaginatedDSPCreativeTestingStudiesV1M2(BaseModel):
    """A list of creative testing studies."""
    measurements: Optional[list["DSPCreativeTestingStudyV1M2"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class PaginatedDSPOmnichannelMetricsStudiesV1M2(BaseModel):
    """A list of studies."""
    measurements: Optional[list["DSPOmnichannelMetricsStudyV1M2"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class PaginatedDSPOmnichannelMetricsStudiesV1M3(BaseModel):
    """A list of studies."""
    measurements: Optional[list["DSPOmnichannelMetricsStudyV1M3"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class PaginatedOmnichannelMetricsBrandsV1M2(BaseModel):
    brands: Optional[list["OmnichannelMetricsBrandV1M2"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of matched brands.")

    model_config = {'populate_by_name': True}


class SurveyQuestionPlaceholderAllowedRangeV1(BaseModel):
    """Allowed value range for placeholder."""
    maximum_value: Optional[int] = Field(None, alias="maximumValue", description="The maximum allowed value.")
    minimum_value: Optional[int] = Field(None, alias="minimumValue", description="The minimum allowed value.")
    parent_field: Optional[str] = Field(None, alias="parentField", description="The field name that this range depends on. Will be empty if this range is the default range.")
    parent_value: Optional[str] = Field(None, alias="parentValue", description="The field value that this range depends on. Will be empty if this range is the default range.")

    model_config = {'populate_by_name': True}


class PlaceholderValueTypeV1(StrEnum):
    INTEGER = "INTEGER"
    STRING = "STRING"


class SurveyQuestionPlaceholderAllowedValueV1(BaseModel):
    """Allowed values for placeholder."""
    parent_field: Optional[str] = Field(None, alias="parentField", description="The field name that this value list depends on. Will be empty if this is the default list.")
    parent_value: Optional[str] = Field(None, alias="parentValue", description="The field value that this value list depend on. Will be empty if this is the default list.")
    values: Optional[list[str]] = Field(None, description="Allowed values for placeholder.")

    model_config = {'populate_by_name': True}


class SurveyQuestionPlaceholderCandidateV1(BaseModel):
    """The placeholder candidate in Survey question."""
    allow_custom_value: Optional[bool] = Field(None, alias="allowCustomValue", description="Whether custom value is allowed for the placeholder.")
    allowed_value_ranges: Optional[list["SurveyQuestionPlaceholderAllowedRangeV1"]] = Field(None, alias="allowedValueRanges", description="Allowed value ranges for placeholder. Only applicable if the valueType is INTEGER.")
    allowed_values: Optional[list["SurveyQuestionPlaceholderAllowedValueV1"]] = Field(None, alias="allowedValues", description="Allowed values for placeholder. Will be empty if placeholder is free text field.")
    default_values: Optional[list[str]] = Field(None, alias="defaultValues", description="Default values that will be appended to the values list regardless.")
    field_name: Optional[str] = Field(None, alias="fieldName", description="The survey question placeholder field name.")
    inferred_fields: Optional[list[str]] = Field(None, alias="inferredFields", description="Where the placeholder values will be inferred from.")
    maximum_value_length: Optional[int] = Field(None, alias="maximumValueLength", description="The maximum allowed character length for each individual placeholder value.")
    minimum_value_length: Optional[int] = Field(None, alias="minimumValueLength", description="The minimum allowed character length for each individual placeholder value.")
    value_type: Optional["PlaceholderValueTypeV1"] = Field(None, alias="valueType")

    model_config = {'populate_by_name': True}


class SurveyQuestionTemplateV1(BaseModel):
    """Survey question template for vendor product."""
    id_: Optional[str] = Field(None, alias="id", description="The survey question template canonical Id.")
    locale: Optional["MeasurementLocaleV1"] = None
    maximum_qualifying_responses: Optional[int] = Field(None, alias="maximumQualifyingResponses", description="The maximum number of qualifying responses allowed for the question. This will be available if the qualifying responses ")
    maximum_question_responses: Optional[int] = Field(None, alias="maximumQuestionResponses", description="The maximum number of responses allowed for the question. This will be available if the question responses are not pre-d")
    minimum_qualifying_responses: Optional[int] = Field(None, alias="minimumQualifyingResponses", description="The minimum number of qualifying responses required for the question. This will be available if the qualifying responses")
    minimum_question_responses: Optional[int] = Field(None, alias="minimumQuestionResponses", description="The minimum number of responses required for the question. This will be available if the question responses are not pre-")
    objective_type: Optional["SurveyQuestionObjectiveTypeV1"] = Field(None, alias="objectiveType")
    placeholder_candidates: Optional[list["SurveyQuestionPlaceholderCandidateV1"]] = Field(None, alias="placeholderCandidates")
    qualifying_responses: Optional[list[str]] = Field(None, alias="qualifyingResponses", description="The pre-defined qualifying survey question responses with placeholders, this will help to define which responses will be")
    question_responses: Optional[list[str]] = Field(None, alias="questionResponses", description="The pre-defined survey question responses with placeholders.")
    question_text: Optional[str] = Field(None, alias="questionText", description="The survey question text with placeholders.")
    type_: Optional["SurveyQuestionTypeV1"] = Field(None, alias="type")
    vendor_product_id: Optional[str] = Field(None, alias="vendorProductId", description="The associated vendor product id.")

    model_config = {'populate_by_name': True}


class PaginatedSurveyQuestionTemplatesV1(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken")
    survey_question_templates: Optional[list["SurveyQuestionTemplateV1"]] = Field(None, alias="surveyQuestionTemplates")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of templates.")

    model_config = {'populate_by_name': True}


class SurveyQuestionCategoryV1M1(StrEnum):
    BRAND_KPI = "BRAND_KPI"
    CUSTOM = "CUSTOM"
    WEIGHTING = "WEIGHTING"


class SurveyQuestionTypeV1M1(StrEnum):
    FREE_TEXT = "FREE_TEXT"
    MULTI_SELECT = "MULTI_SELECT"
    RATING = "RATING"
    SINGLE_SELECT = "SINGLE_SELECT"
    SINGLE_SELECT_GRID = "SINGLE_SELECT_GRID"


class SurveyQuestionSubCategoryV1M1(StrEnum):
    BEHAVIOR = "BEHAVIOR"
    DEMOGRAPHIC = "DEMOGRAPHIC"
    PURCHASE_HISTORY = "PURCHASE_HISTORY"


class SurveyQuestionGridQuestionResponseV1M1(BaseModel):
    """The grid question response object. Only applicable for SINGLE_SELECT_GRID type question."""
    columns: Optional["SurveyQuestionPlaceholderCandidateV1"] = None
    rows: Optional["SurveyQuestionPlaceholderCandidateV1"] = None

    model_config = {'populate_by_name': True}


class SurveyQuestionTemplateV1M1(BaseModel):
    """Survey question template for vendor product."""
    category: Optional["SurveyQuestionCategoryV1M1"] = None
    grid_question_response: Optional["SurveyQuestionGridQuestionResponseV1M1"] = Field(None, alias="gridQuestionResponse")
    id_: Optional[str] = Field(None, alias="id", description="The survey question template canonical Id.")
    locale: Optional["MeasurementLocaleV1"] = None
    maximum_qualifying_responses: Optional[int] = Field(None, alias="maximumQualifyingResponses", description="The maximum number of qualifying responses allowed for the question. This will be available if the qualifying responses ")
    maximum_question_responses: Optional[int] = Field(None, alias="maximumQuestionResponses", description="The maximum number of responses allowed for the question. This will be available if the question responses are not pre-d")
    minimum_qualifying_responses: Optional[int] = Field(None, alias="minimumQualifyingResponses", description="The minimum number of qualifying responses required for the question. This will be available if the qualifying responses")
    minimum_question_responses: Optional[int] = Field(None, alias="minimumQuestionResponses", description="The minimum number of responses required for the question. This will be available if the question responses are not pre-")
    objective_type: Optional["SurveyQuestionObjectiveTypeV1M1"] = Field(None, alias="objectiveType")
    placeholder_candidates: Optional[list["SurveyQuestionPlaceholderCandidateV1"]] = Field(None, alias="placeholderCandidates")
    priority: Optional[int] = Field(None, description="The priority of the question. If present this will determine the ordering of questions in a survey. The check will be en")
    qualifying_responses: Optional[list[str]] = Field(None, alias="qualifyingResponses", description="The pre-defined qualifying survey question responses with placeholders, this will help to define which responses will be")
    question_responses: Optional[list[str]] = Field(None, alias="questionResponses", description="The pre-defined survey question responses with placeholders.")
    question_text: Optional[str] = Field(None, alias="questionText", description="The survey question text with placeholders.")
    sub_category: Optional["SurveyQuestionSubCategoryV1M1"] = Field(None, alias="subCategory")
    type_: Optional["SurveyQuestionTypeV1M1"] = Field(None, alias="type")
    vendor_product_id: Optional[str] = Field(None, alias="vendorProductId", description="The associated vendor product id.")

    model_config = {'populate_by_name': True}


class PaginatedSurveyQuestionTemplatesV1M1(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken")
    survey_question_templates: Optional[list["SurveyQuestionTemplateV1M1"]] = Field(None, alias="surveyQuestionTemplates")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of templates.")

    model_config = {'populate_by_name': True}


class SurveyQuestionPlaceholderV1(BaseModel):
    """The object specifying a placeholder in Survey question."""
    field_name: Optional[str] = Field(None, alias="fieldName", description="The survey question placeholder field name.")
    field_values: Optional[list["SurveyQuestionPlaceholderFieldValueV1"]] = Field(None, alias="fieldValues", description="The survey question placeholder field values.")

    model_config = {'populate_by_name': True}


class TemplatedSurveyQuestionV1(BaseModel):
    """The templated measurement survey question."""
    id_: Optional[str] = Field(None, alias="id", description="The survey question template canonical identifier.")
    placeholders: Optional[list["SurveyQuestionPlaceholderV1"]] = Field(None, description="List of question placeholders")

    model_config = {'populate_by_name': True}


class SurveyStatusV1(StrEnum):
    AVAILABLE = "AVAILABLE"
    DRAFT = "DRAFT"
    IN_USE = "IN_USE"


class SurveyV1(BaseModel):
    """The measurement survey."""
    custom_questions: Optional[list["CustomSurveyQuestionV1"]] = Field(None, alias="customQuestions", description="A list of custom survey questions.")
    id_: Optional[str] = Field(None, alias="id", description="The survey canonical identifier. Immutable field. This is required for update.")
    status: Optional["SurveyStatusV1"] = None
    study_id: Optional[str] = Field(None, alias="studyId", description="The associated study identifier. Survey needs to be created prior to the study creation.")
    templated_questions: Optional[list["TemplatedSurveyQuestionV1"]] = Field(None, alias="templatedQuestions", description="A list of templated survey questions.")
    vendor_product_id: Optional[str] = Field(None, alias="vendorProductId", description="The vendor product canonical identifier.")

    model_config = {'populate_by_name': True}


class PaginatedSurveysV1(BaseModel):
    """A list of study surveys."""
    next_token: Optional[str] = Field(None, alias="nextToken")
    surveys: Optional[list["SurveyV1"]] = None

    model_config = {'populate_by_name': True}


class TemplatedSurveyQuestionV1M1(BaseModel):
    """The templated measurement survey question."""
    grid_question_response: Optional["GridQuestionResponsesV1M1"] = Field(None, alias="gridQuestionResponse")
    id_: Optional[str] = Field(None, alias="id", description="The survey question template canonical identifier.")
    placeholders: Optional[list["SurveyQuestionPlaceholderV1"]] = Field(None, description="List of question placeholders")

    model_config = {'populate_by_name': True}


class SurveyV1M1(BaseModel):
    """The measurement survey."""
    custom_questions: Optional[list["CustomSurveyQuestionV1"]] = Field(None, alias="customQuestions", description="A list of custom survey questions.")
    id_: Optional[str] = Field(None, alias="id", description="The survey canonical identifier. Immutable field. This is required for update.")
    status: Optional["SurveyStatusV1"] = None
    study_id: Optional[str] = Field(None, alias="studyId", description="The associated study identifier. Survey needs to be created prior to the study creation.")
    templated_questions: Optional[list["TemplatedSurveyQuestionV1M1"]] = Field(None, alias="templatedQuestions", description="A list of templated survey questions.")
    vendor_product_id: Optional[str] = Field(None, alias="vendorProductId", description="The vendor product canonical identifier.")

    model_config = {'populate_by_name': True}


class PaginatedSurveysV1M1(BaseModel):
    """A list of study surveys."""
    next_token: Optional[str] = Field(None, alias="nextToken")
    surveys: Optional[list["SurveyV1M1"]] = None

    model_config = {'populate_by_name': True}


class VendorProductPolicyV1(BaseModel):
    """The policy rules will be enforced at vendor product level."""
    bench_mark_category_required: Optional[bool] = Field(None, alias="benchMarkCategoryRequired", description="Whether or not the benchMark category is required for measurement setup.")
    custom_question_allowed: Optional[bool] = Field(None, alias="customQuestionAllowed", description="Whether custom survey questions are allowed.")
    external_reference_id_required: Optional[bool] = Field(None, alias="externalReferenceIdRequired", description="Whether or not the vendor assigned external reference identifier is required for measurement setup.")
    lead_time: Optional[int] = Field(None, alias="leadTime", description="Days required for measurement configuration. It is recommended that the startDate of the campaign has sufficient padding")
    maximum_orders: Optional[int] = Field(None, alias="maximumOrders", description="The maximum number of order allowed for the product.")
    maximum_peer_names: Optional[int] = Field(None, alias="maximumPeerNames", description="The maximum number of peer names required for the product.")
    maximum_study_length: Optional[int] = Field(None, alias="maximumStudyLength", description="The maximum required length/duration of the study in days.")
    maximum_survey_questions: Optional[int] = Field(None, alias="maximumSurveyQuestions", description="The maximum number of survey questions required for the product.")
    minimum_orders: Optional[int] = Field(None, alias="minimumOrders", description="The maximum number of orders required for the product.")
    minimum_peer_names: Optional[int] = Field(None, alias="minimumPeerNames", description="The minimum number of peer names required for the product.")
    minimum_study_length: Optional[int] = Field(None, alias="minimumStudyLength", description="The minimum required length/duration of the study in days.")
    minimum_survey_questions: Optional[int] = Field(None, alias="minimumSurveyQuestions", description="The minimum number of survey questions required for the product.")
    required_question_objectives: Optional[list["SurveyQuestionObjectiveTypeV1"]] = Field(None, alias="requiredQuestionObjectives", description="The required question objectives that need to be included as part of the survey.")
    supported_goals: Optional[list["MeasurementGoalV1"]] = Field(None, alias="supportedGoals")
    supported_marketplaces: Optional[list["MeasurementMarketplaceV1"]] = Field(None, alias="supportedMarketplaces")
    vendor_approval_required: Optional[bool] = Field(None, alias="vendorApprovalRequired", description="Whether or not the vendor requires an additional sign off process to fully qualify for study.")
    vendor_product_id: Optional[str] = Field(None, alias="vendorProductId", description="vendor product canonical identifier.")

    model_config = {'populate_by_name': True}


class PaginatedVendorProductPoliciesV1(BaseModel):
    """A list of measurement vendor products policies."""
    next_token: Optional[str] = Field(None, alias="nextToken")
    policies: Optional[list["VendorProductPolicyV1"]] = None
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of vendor products.")

    model_config = {'populate_by_name': True}


class SurveyQuestionCategoryRequirementV1M1(BaseModel):
    """The requirement for specific survey question category."""
    category: Optional["SurveyQuestionCategoryV1M1"] = None
    maximum_questions: Optional[int] = Field(None, alias="maximumQuestions", description="The maximum number of questions required for the question category.")
    minimum_questions: Optional[int] = Field(None, alias="minimumQuestions", description="The minimum number of questions required for the question category.")

    model_config = {'populate_by_name': True}


class VendorProductPolicyV1M1(BaseModel):
    """The policy rules will be enforced at vendor product level."""
    bench_mark_category_required: Optional[bool] = Field(None, alias="benchMarkCategoryRequired", description="Whether or not the benchMark category is required for measurement setup.")
    custom_question_allowed: Optional[bool] = Field(None, alias="customQuestionAllowed", description="Whether custom survey questions are allowed.")
    external_reference_id_required: Optional[bool] = Field(None, alias="externalReferenceIdRequired", description="Whether or not the vendor assigned external reference identifier is required for measurement setup.")
    lead_time: Optional[int] = Field(None, alias="leadTime", description="Days required for measurement configuration. It is recommended that the startDate of the campaign has sufficient padding")
    maximum_orders: Optional[int] = Field(None, alias="maximumOrders", description="The maximum number of order allowed for the product.")
    maximum_peer_names: Optional[int] = Field(None, alias="maximumPeerNames", description="The maximum number of peer names required for the product.")
    maximum_study_length: Optional[int] = Field(None, alias="maximumStudyLength", description="The maximum required length/duration of the study in days.")
    maximum_survey_questions: Optional[int] = Field(None, alias="maximumSurveyQuestions", description="The maximum number of survey questions required for the product.")
    minimum_orders: Optional[int] = Field(None, alias="minimumOrders", description="The maximum number of orders required for the product.")
    minimum_peer_names: Optional[int] = Field(None, alias="minimumPeerNames", description="The minimum number of peer names required for the product.")
    minimum_study_length: Optional[int] = Field(None, alias="minimumStudyLength", description="The minimum required length/duration of the study in days.")
    minimum_survey_questions: Optional[int] = Field(None, alias="minimumSurveyQuestions", description="The minimum number of survey questions required for the product.")
    required_question_categories: Optional[list["SurveyQuestionCategoryRequirementV1M1"]] = Field(None, alias="requiredQuestionCategories", description="The requirements for survey question categories.")
    required_question_objectives: Optional[list["SurveyQuestionObjectiveTypeV1M1"]] = Field(None, alias="requiredQuestionObjectives", description="The required question objectives that need to be included as part of the survey.")
    supported_goals: Optional[list["MeasurementGoalV1"]] = Field(None, alias="supportedGoals")
    supported_marketplaces: Optional[list["MeasurementMarketplaceV1"]] = Field(None, alias="supportedMarketplaces")
    supported_verbs: Optional[list[str]] = Field(None, alias="supportedVerbs", description="List of supported verbs that can be used in survey questions.")
    vendor_approval_required: Optional[bool] = Field(None, alias="vendorApprovalRequired", description="Whether or not the vendor requires an additional sign off process to fully qualify for study.")
    vendor_product_id: Optional[str] = Field(None, alias="vendorProductId", description="vendor product canonical identifier.")
    verb_required: Optional[bool] = Field(None, alias="verbRequired", description="Whether or not a verb is required for measurement setup. It will be used in applicable survey questions to construct the")

    model_config = {'populate_by_name': True}


class PaginatedVendorProductPoliciesV1M1(BaseModel):
    """A list of measurement vendor products policies."""
    next_token: Optional[str] = Field(None, alias="nextToken")
    policies: Optional[list["VendorProductPolicyV1M1"]] = None
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of vendor products.")

    model_config = {'populate_by_name': True}


class StudyObjectiveV1(StrEnum):
    CAMPAIGN_MEASUREMENT = "CAMPAIGN_MEASUREMENT"
    CAMPAIGN_PLANNING = "CAMPAIGN_PLANNING"


class VendorProductTypeV1(StrEnum):
    SHOPPER_PANEL = "SHOPPER_PANEL"


class StudyTypeV1(StrEnum):
    BRAND_LIFT = "BRAND_LIFT"


class VendorProductV1(BaseModel):
    """The measurement vendor product."""
    ad_type: Optional["AdTypeV1"] = Field(None, alias="adType")
    funding_type: Optional["FundingTypeV1"] = Field(None, alias="fundingType")
    id_: Optional[str] = Field(None, alias="id", description="The vendor product identifier.")
    objective: Optional["StudyObjectiveV1"] = None
    study_type: Optional["StudyTypeV1"] = Field(None, alias="studyType")
    vendor_product_type: Optional["VendorProductTypeV1"] = Field(None, alias="vendorProductType")
    vendor_type: Optional["VendorTypeV1"] = Field(None, alias="vendorType")

    model_config = {'populate_by_name': True}


class PaginatedVendorProductsV1(BaseModel):
    """A list of measurement vendor products."""
    next_token: Optional[str] = Field(None, alias="nextToken")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of vendor products.")
    vendor_products: Optional[list["VendorProductV1"]] = Field(None, alias="vendorProducts")

    model_config = {'populate_by_name': True}


class VendorProductTypeV1M1(StrEnum):
    BRAND_LIFT_INSIGHTS = "BRAND_LIFT_INSIGHTS"
    DASH = "DASH"
    DIGITAL_BRAND_EFFECT = "DIGITAL_BRAND_EFFECT"
    DYNATA = "DYNATA"
    EXPANDED_VIEW_LITE = "EXPANDED_VIEW_LITE"
    LUCID = "LUCID"
    MACROMILL = "MACROMILL"
    SHOPPER_PANEL = "SHOPPER_PANEL"
    UPWAVE = "UPWAVE"


class VendorProductV1M1(BaseModel):
    """The measurement vendor product."""
    ad_type: Optional["AdTypeV1"] = Field(None, alias="adType")
    display_name: Optional[str] = Field(None, alias="displayName", description="The vendor product display name.")
    funding_type: Optional["FundingTypeV1M1"] = Field(None, alias="fundingType")
    id_: Optional[str] = Field(None, alias="id", description="The vendor product identifier.")
    objective: Optional["StudyObjectiveV1"] = None
    study_type: Optional["StudyTypeV1"] = Field(None, alias="studyType")
    vendor_product_type: Optional["VendorProductTypeV1M1"] = Field(None, alias="vendorProductType")
    vendor_type: Optional["VendorTypeV1M1"] = Field(None, alias="vendorType")

    model_config = {'populate_by_name': True}


class PaginatedVendorProductsV1M1(BaseModel):
    """A list of measurement vendor products."""
    next_token: Optional[str] = Field(None, alias="nextToken")
    total_results: Optional[int] = Field(None, alias="totalResults", description="The total number of vendor products.")
    vendor_products: Optional[list["VendorProductV1M1"]] = Field(None, alias="vendorProducts")

    model_config = {'populate_by_name': True}


class PlanningOrderMetadataV1M3(BaseModel):
    """Metadata around a hypothetical order."""
    budget: Optional[float] = Field(None, description="The total estimated budget of the order.")
    end_date: Optional[str] = Field(None, alias="endDate", description="The estimated end date of the order in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC.")
    goal: Optional["MeasurementGoalV1"] = None
    impressions: Optional[int] = Field(None, description="The total estimated impressions of the order.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The estimated start date of the order in ISO format (YYYY-MM-DDThh:mm:ssTZD). Timezone is UTC.")

    model_config = {'populate_by_name': True}


class StudyTypeV1M2(StrEnum):
    AUDIENCE_RESEARCH = "AUDIENCE_RESEARCH"
    BRAND_LIFT = "BRAND_LIFT"
    CREATIVE_TESTING = "CREATIVE_TESTING"
    OMNICHANNEL_METRICS = "OMNICHANNEL_METRICS"


class PlanningEligibilityDataV1M3(BaseModel):
    """The planning eligibility data."""
    advertiser_id: Optional[str] = Field(None, alias="advertiserId", description="The advertiserId.")
    locale: Optional["MeasurementLocaleV1"] = None
    order_metadata: Optional[list["PlanningOrderMetadataV1M3"]] = Field(None, alias="orderMetadata")
    study_type_filters: Optional[list["StudyTypeV1M2"]] = Field(None, alias="studyTypeFilters", description="StudyType identifier filters to be applied when checking eligibility status. If not supplied we will check against all a")

    model_config = {'populate_by_name': True}


class PlanningEligibilityRequestV1M3(BaseModel):
    """The request object of planning eligibility check."""
    pass


class PlanningEligibilityV1M3(BaseModel):
    """The request object of measurement eligibility check."""
    issues: Optional[list["EligibilityIssueV1M2"]] = Field(None, description="A list of issues will be provided if the status is INELIGIBLE or ELIGIBLE_WITH_WARNING.")
    rank: Optional[float] = Field(None, description="The lower the number, the more recommended the vendor product is.")
    status: Optional["EligibilityStatusV1"] = None
    vendor_product_id: Optional[str] = Field(None, alias="vendorProductId", description="Vendor product canonical identifier.")

    model_config = {'populate_by_name': True}


class PlanningEligibilityResponseV1M3(BaseModel):
    """The planning eligibility response object."""
    metadata: Optional["EligibilityMetadataV1"] = None
    next_token: Optional[str] = Field(None, alias="nextToken")
    vendor_product_eligibilities: Optional[list["PlanningEligibilityV1M3"]] = Field(None, alias="vendorProductEligibilities")

    model_config = {'populate_by_name': True}


class StudyResponseV1(BaseModel):
    """Study response."""
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    errors: Optional[list["SubErrorV1"]] = None
    index: Optional[int] = Field(None, description="The index of the object in the request, starting from 1.")
    message: Optional[str] = Field(None, description="A human-readable message of the code.")
    study_id: Optional[str] = Field(None, alias="studyId", description="The study canonical identifier.")

    model_config = {'populate_by_name': True}


class StudyResponsesV1(BaseModel):
    """Studies response."""
    request_id: Optional[str] = Field(None, alias="requestId", description="Request Id that uniquely identifies your request.")
    responses: Optional[list["StudyResponseV1"]] = None

    model_config = {'populate_by_name': True}


class SurveyErrorV1(BaseModel):
    """The survey error object."""
    error_type: str = Field(..., alias="errorType")
    field_name: Optional[str] = Field(None, alias="fieldName")
    message: str
    question_template_id: Optional[str] = Field(None, alias="questionTemplateId")

    model_config = {'populate_by_name': True}


class SurveyResponseV1(BaseModel):
    """Survey response."""
    code: Optional[str] = Field(None, description="An enumerated success or error code for machine use.")
    errors: Optional[list["SurveyErrorV1"]] = None
    index: Optional[int] = Field(None, description="The index of the object in the request, starting from 1.")
    message: Optional[str] = Field(None, description="A human-readable message of the code.")
    survey_id: Optional[str] = Field(None, alias="surveyId", description="The survey canonical identifier.")

    model_config = {'populate_by_name': True}


class SurveyResponsesV1(BaseModel):
    """Surveys response."""
    request_id: Optional[str] = Field(None, alias="requestId", description="Request Id that uniquely identifies your request.")
    responses: Optional[list["SurveyResponseV1"]] = None

    model_config = {'populate_by_name': True}


class UpdateDSPAudienceResearchStudyV1M2(BaseModel):
    """Update DSP AUDIENCE_RESEARCH study object."""
    pass


class UpdateDSPCreativeTestingStudyV1M2(BaseModel):
    """Update DSP CREATIVE_TESTING study object."""
    pass


class VendorProductRequestV1(BaseModel):
    """The request object to fetch measurement vendor products."""
    ad_type_filters: Optional[list["AdTypeV1"]] = Field(None, alias="adTypeFilters", description="AdType filters to be applied when fetching measurement vendor products. If not supplied we will include all available ve")
    funding_type_filters: Optional[list["FundingTypeV1"]] = Field(None, alias="fundingTypeFilters", description="FundingType filters to be applied when fetching measurement vendor products. If not supplied we will include all availab")
    objective_type_filters: Optional[list["StudyObjectiveV1"]] = Field(None, alias="objectiveTypeFilters", description="StudyObjective filters to be applied when fetching measurement vendor products. If not supplied we will include all avai")
    study_type_filters: Optional[list["StudyTypeV1"]] = Field(None, alias="studyTypeFilters", description="StudyType filters to be applied when fetching measurement vendor products. If not supplied we will include all available")
    vendor_product_id_filters: Optional[list[str]] = Field(None, alias="vendorProductIdFilters", description="VendorProduct identifier filters to be applied when fetching measurement vendor products. If not supplied we will includ")
    vendor_type_filters: Optional[list["VendorTypeV1"]] = Field(None, alias="vendorTypeFilters", description="VendorType filters to be applied when fetching measurement vendor products. If not supplied we will include all availabl")

    model_config = {'populate_by_name': True}


class VendorProductRequestV1M1(BaseModel):
    """The request object to fetch measurement vendor products."""
    ad_type_filters: Optional[list["AdTypeV1"]] = Field(None, alias="adTypeFilters", description="AdType filters to be applied when fetching measurement vendor products. If not supplied we will include all available ve")
    funding_type_filters: Optional[list["FundingTypeV1M1"]] = Field(None, alias="fundingTypeFilters", description="FundingType filters to be applied when fetching measurement vendor products. If not supplied we will include all availab")
    objective_type_filters: Optional[list["StudyObjectiveV1"]] = Field(None, alias="objectiveTypeFilters", description="StudyObjective filters to be applied when fetching measurement vendor products. If not supplied we will include all avai")
    study_type_filters: Optional[list["StudyTypeV1"]] = Field(None, alias="studyTypeFilters", description="StudyType filters to be applied when fetching measurement vendor products. If not supplied we will include all available")
    vendor_product_id_filters: Optional[list[str]] = Field(None, alias="vendorProductIdFilters", description="VendorProduct identifier filters to be applied when fetching measurement vendor products. If not supplied we will includ")
    vendor_type_filters: Optional[list["VendorTypeV1M1"]] = Field(None, alias="vendorTypeFilters", description="VendorType filters to be applied when fetching measurement vendor products. If not supplied we will include all availabl")

    model_config = {'populate_by_name': True}

