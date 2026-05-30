"""Auto-generated Pydantic models. Do not edit manually.

Source: AmazonAdsAPIALLMerged_prod_3p.json
Title:  Amazon Ads API ALL Merged
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401



class AcrossGroupOperator(StrEnum):
    ALL = "ALL"
    ANY = "ANY"


class LanguageLocale(StrEnum):
    AK_GH = "ak_GH"
    AM_ET = "am_ET"
    AN_ES = "an_ES"
    AR_AE = "ar_AE"
    AS_IN = "as_IN"
    AV_RU = "av_RU"
    AY_BO = "ay_BO"
    BA_RU = "ba_RU"
    BE_BY = "be_BY"
    BG_BG = "bg_BG"
    BH_IN = "bh_IN"
    BI_VU = "bi_VU"
    BM_ML = "bm_ML"
    BO_CN = "bo_CN"
    BS_BA = "bs_BA"
    CA_ES = "ca_ES"
    CE_RU = "ce_RU"
    CH_GU = "ch_GU"
    DE_DE = "de_DE"
    EL_GR = "el_GR"
    EN_US = "en_US"
    EO_INT = "eo_INT"
    ES_ES = "es_ES"
    ET_EE = "et_EE"
    EU_ES = "eu_ES"
    FA_IR = "fa_IR"
    FI_FI = "fi_FI"
    FJ_FJ = "fj_FJ"
    FO_FO = "fo_FO"
    FR_FR = "fr_FR"
    FY_NL = "fy_NL"
    GA_IE = "ga_IE"
    GD_GB = "gd_GB"
    GL_ES = "gl_ES"
    GN_PY = "gn_PY"
    GU_IN = "gu_IN"
    GV_IM = "gv_IM"
    HA_NG = "ha_NG"
    HE_IL = "he_IL"
    HI_IN = "hi_IN"
    HO_PG = "ho_PG"
    HR_HR = "hr_HR"
    HT_HT = "ht_HT"
    HU_HU = "hu_HU"
    HY_AM = "hy_AM"
    HZ_NA = "hz_NA"
    IA_INT = "ia_INT"
    ID_ID = "id_ID"
    IE_INT = "ie_INT"
    IG_NG = "ig_NG"
    II_CN = "ii_CN"
    IK_US = "ik_US"
    IO_INT = "io_INT"
    IS_IS = "is_IS"
    IT_IT = "it_IT"
    IU_CA = "iu_CA"
    JA_JP = "ja_JP"
    JV_ID = "jv_ID"
    KA_GE = "ka_GE"
    KG_CD = "kg_CD"
    KI_KE = "ki_KE"
    KJ_NA = "kj_NA"
    KK_KZ = "kk_KZ"
    KL_GL = "kl_GL"
    KM_KH = "km_KH"
    KN_IN = "kn_IN"
    KO_KR = "ko_KR"
    KR_NG = "kr_NG"
    KS_IN = "ks_IN"
    KU_TR = "ku_TR"
    KV_RU = "kv_RU"
    KW_GB = "kw_GB"
    KY_KG = "ky_KG"
    LA_VA = "la_VA"
    LB_LU = "lb_LU"
    LG_UG = "lg_UG"
    LI_NL = "li_NL"
    LN_CD = "ln_CD"
    LO_LA = "lo_LA"
    LT_LT = "lt_LT"
    LU_CD = "lu_CD"
    LV_LV = "lv_LV"
    MG_MG = "mg_MG"
    MH_MH = "mh_MH"
    MI_NZ = "mi_NZ"
    MK_MK = "mk_MK"
    ML_IN = "ml_IN"
    MN_MN = "mn_MN"
    MR_IN = "mr_IN"
    MS_MY = "ms_MY"
    MT_MT = "mt_MT"
    MY_MM = "my_MM"
    NA_NR = "na_NR"
    NB_NO = "nb_NO"
    ND_ZW = "nd_ZW"
    NE_NP = "ne_NP"
    NG_NA = "ng_NA"
    NL_NL = "nl_NL"
    NN_NO = "nn_NO"
    NO_NO = "no_NO"
    NR_ZA = "nr_ZA"
    NV_US = "nv_US"
    NY_MW = "ny_MW"
    OC_FR = "oc_FR"
    OJ_CA = "oj_CA"
    OM_ET = "om_ET"
    OR_IN = "or_IN"
    OS_RU = "os_RU"
    PA_IN = "pa_IN"
    PI_IN = "pi_IN"
    PL_PL = "pl_PL"
    PS_AF = "ps_AF"
    PT_PT = "pt_PT"
    QU_PE = "qu_PE"
    RM_CH = "rm_CH"
    RN_BI = "rn_BI"
    RO_RO = "ro_RO"
    RU_RU = "ru_RU"
    RW_RW = "rw_RW"
    SA_IN = "sa_IN"
    SC_IT = "sc_IT"
    SD_PK = "sd_PK"
    SE_NO = "se_NO"
    SG_CF = "sg_CF"
    SI_LK = "si_LK"
    SK_SK = "sk_SK"
    SL_SI = "sl_SI"
    SM_WS = "sm_WS"
    SN_ZW = "sn_ZW"
    SO_SO = "so_SO"
    SQ_AL = "sq_AL"
    SR_RS = "sr_RS"
    SS_SZ = "ss_SZ"
    ST_LS = "st_LS"
    SU_ID = "su_ID"
    SV_SE = "sv_SE"
    SW_TZ = "sw_TZ"
    TA_IN = "ta_IN"
    TE_IN = "te_IN"
    TG_TJ = "tg_TJ"
    TH_TH = "th_TH"
    TI_ET = "ti_ET"
    TK_TM = "tk_TM"
    TL_PH = "tl_PH"
    TN_BW = "tn_BW"
    TO_TO = "to_TO"
    TR_TR = "tr_TR"
    TS_ZA = "ts_ZA"
    TT_RU = "tt_RU"
    TW_GH = "tw_GH"
    TY_PF = "ty_PF"
    UG_CN = "ug_CN"
    UK_UA = "uk_UA"
    UR_PK = "ur_PK"
    UZ_UZ = "uz_UZ"
    VE_ZA = "ve_ZA"
    VI_VN = "vi_VN"
    VO_INT = "vo_INT"
    WA_BE = "wa_BE"
    WO_SN = "wo_SN"
    XH_ZA = "xh_ZA"
    YI_IL = "yi_IL"
    YO_NG = "yo_NG"
    ZA_CN = "za_CN"
    ZH_CN = "zh_CN"
    ZU_ZA = "zu_ZA"


class Video(BaseModel):
    asset_id: str = Field(..., alias="assetId", description="The asset library ID associated with the video asset.")
    asset_version: str = Field(..., alias="assetVersion", description="The asset library version associated with the video asset.")
    description: Optional[str] = Field(None, description="The description of the video content.")
    headline: Optional[str] = Field(None, description="The headline/custom text associated with the video.")

    model_config = {'populate_by_name': True}


class CreativeTrackingUrl(BaseModel):
    url: str = Field(..., description="A url to be triggered for tracking events.")

    model_config = {'populate_by_name': True}


class Marketplace(StrEnum):
    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IE = "IE"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"
    ZA = "ZA"


class GlobalStoreSettings(BaseModel):
    catalog_source_marketplace: Optional["Marketplace"] = Field(None, alias="catalogSourceMarketplace")

    model_config = {'populate_by_name': True}


class AdvertisedProductMarketplaceSetting(BaseModel):
    global_store_setting: Optional["GlobalStoreSettings"] = Field(None, alias="globalStoreSetting")
    marketplace: "Marketplace"
    product_id: str = Field(..., alias="productId", description="The identifier of the product advertised.")
    resolved_product_id: Optional[str] = Field(None, alias="resolvedProductId", description="The identifier of product associated with the advertised product. It's a read-only field.")

    model_config = {'populate_by_name': True}


class ProductIdType(StrEnum):
    ASIN = "ASIN"
    SKU = "SKU"


class AdvertisedProducts(BaseModel):
    global_store_setting: Optional["GlobalStoreSettings"] = Field(None, alias="globalStoreSetting")
    marketplace_settings: Optional[list["AdvertisedProductMarketplaceSetting"]] = Field(None, alias="marketplaceSettings", description="List of advertised product selectively applied at the given marketplace level")
    product_id: Optional[str] = Field(None, alias="productId", description="The identifier of the advertised product.")
    product_id_type: "ProductIdType" = Field(..., alias="productIdType")
    resolved_product_id: Optional[str] = Field(None, alias="resolvedProductId", description="The identifier of product associated with the advertised product. It's a read-only field.")
    resolved_product_id_type: Optional["ProductIdType"] = Field(None, alias="resolvedProductIdType")

    model_config = {'populate_by_name': True}


class LearnMoreVideoCallToActionSettings(BaseModel):
    url: str = Field(..., description="The url to drive users to learn more via the video CallToAction.")

    model_config = {'populate_by_name': True}


class DeepLinkingBehavior(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class ClickToUrlVideoCallToActionSettings(BaseModel):
    deep_linking_behavior: "DeepLinkingBehavior" = Field(..., alias="deepLinkingBehavior")
    url: str = Field(..., description="The url to redirect the user via the video CallToAction.")

    model_config = {'populate_by_name': True}


class VideoCallToAction(BaseModel):
    pass


class OnlineVideoSettings(BaseModel):
    call_to_actions: Optional[list["VideoCallToAction"]] = Field(None, alias="callToActions", description="The call to actions for this video.")
    click_tracking_urls: Optional[list["CreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    impression_tracking_urls: Optional[list["CreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    language: "LanguageLocale"
    products: Optional["AdvertisedProducts"] = None
    videos: "Video"

    model_config = {'populate_by_name': True}


class VideoLandingPageType(StrEnum):
    DETAIL_PAGE = "DETAIL_PAGE"
    MOMENT = "MOMENT"
    OFF_AMAZON_LINK = "OFF_AMAZON_LINK"
    STORE = "STORE"


class VideoLandingPage(BaseModel):
    landing_page_type: "VideoLandingPageType" = Field(..., alias="landingPageType")
    landing_page_url: Optional[str] = Field(None, alias="landingPageUrl", description="The URL of landing page where the ad directs.")

    model_config = {'populate_by_name': True}


class ModerationStatus(StrEnum):
    APPROVED_WITH_EXCEPTIONS = "APPROVED_WITH_EXCEPTIONS"
    PENDING_TRANSLATION = "PENDING_TRANSLATION"
    PUBLISHED = "PUBLISHED"
    REJECTED_BY_MODERATION = "REJECTED_BY_MODERATION"
    SUBMITTED_FOR_MODERATION = "SUBMITTED_FOR_MODERATION"


class CreativeStatus(BaseModel):
    moderation_status: "ModerationStatus" = Field(..., alias="moderationStatus")

    model_config = {'populate_by_name': True}


class StreamingTvSettings(BaseModel):
    call_to_actions: Optional[list["VideoCallToAction"]] = Field(None, alias="callToActions", description="The call to actions for this video.")
    impression_tracking_urls: Optional[list["CreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    landing_page: Optional["VideoLandingPage"] = Field(None, alias="landingPage")
    language: Optional["LanguageLocale"] = None
    moderation_status: Optional["CreativeStatus"] = Field(None, alias="moderationStatus")
    products: Optional[list["AdvertisedProducts"]] = Field(None, description="The product advertised on this video creative.")
    videos: "Video"

    model_config = {'populate_by_name': True}


class VideoCreative(BaseModel):
    online_video_settings: Optional["OnlineVideoSettings"] = Field(None, alias="onlineVideoSettings")
    streaming_tv_settings: Optional["StreamingTvSettings"] = Field(None, alias="streamingTvSettings")

    model_config = {'populate_by_name': True}


class ClickToAppDisplayCallToActionSettings(BaseModel):
    """A CTA that directs a customer to a provided url."""
    deep_linking_behavior: "DeepLinkingBehavior" = Field(..., alias="deepLinkingBehavior")
    url: str = Field(..., description="The app that customers are directed to.")

    model_config = {'populate_by_name': True}


class ClickToUrlDisplayCallToActionSettings(BaseModel):
    """A CTA that directs a customer to a provided url."""
    deep_linking_behavior: "DeepLinkingBehavior" = Field(..., alias="deepLinkingBehavior")
    url: str = Field(..., description="The application url that customers are directed to.")

    model_config = {'populate_by_name': True}


class DisplayCallToAction(BaseModel):
    pass


class AdChoicesPosition(StrEnum):
    BOTTOM_LEFT = "BOTTOM_LEFT"
    BOTTOM_RIGHT = "BOTTOM_RIGHT"
    TOP_LEFT = "TOP_LEFT"
    TOP_RIGHT = "TOP_RIGHT"


class Size(BaseModel):
    height: int = Field(..., description="The height of the creative placement.")
    width: int = Field(..., description="The width of the creative placement.")

    model_config = {'populate_by_name': True}


class FormatProperties(BaseModel):
    apply_border: Optional[bool] = Field(None, alias="applyBorder", description="Apply a boarder to the image to fit rules for some supplies.")
    height: Optional[int] = Field(None, description="The height (in pixels) of the cropped image.")
    left: Optional[int] = Field(None, description="The number of pixels from the left of the image where the crop should begin.")
    top: Optional[int] = Field(None, description="The number of pixels from the top of the image where the crop should begin.")
    width: Optional[int] = Field(None, description="The width (in pixels) of the cropped image.")

    model_config = {'populate_by_name': True}


class Image(BaseModel):
    asset_id: str = Field(..., alias="assetId", description="The asset library ID associated with the image asset.")
    asset_version: str = Field(..., alias="assetVersion", description="The asset library version associated with the image asset.")
    format_properties: Optional[list["FormatProperties"]] = Field(None, alias="formatProperties", description="The cropping and positioning properties associated with the asset.")

    model_config = {'populate_by_name': True}


class StandardDisplaySettings(BaseModel):
    ad_choices_position: "AdChoicesPosition" = Field(..., alias="adChoicesPosition")
    call_to_action: Optional["DisplayCallToAction"] = Field(None, alias="callToAction")
    click_tracking_urls: Optional[list["CreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    creative_sizes: list["Size"] = Field(..., alias="creativeSizes", description="The list of placement sizes this creative should serve on.")
    custom_images: list["Image"] = Field(..., alias="customImages", description="The custom images to use for the standard display experience.")
    impression_tracking_urls: Optional[list["CreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    language: "LanguageLocale"

    model_config = {'populate_by_name': True}


class DisplayCreative(BaseModel):
    standard_display_settings: Optional["StandardDisplaySettings"] = Field(None, alias="standardDisplaySettings")

    model_config = {'populate_by_name': True}


class ThirdPartyDisplaySettings(BaseModel):
    ad_choices_position: "AdChoicesPosition" = Field(..., alias="adChoicesPosition")
    additional_html: Optional[str] = Field(None, alias="additionalHtml", description="Additional html to be included along with the creative when rendered.")
    click_tracking_urls: Optional[list["CreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    creative_sizes: Optional[list["Size"]] = Field(None, alias="creativeSizes", description="The list of placement sizes this creative should serve on. Required for non publisher hosted creatives (when publisherHo")
    impression_tracking_urls: Optional[list["CreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    language: "LanguageLocale"
    third_party_tag_hosting_source: Optional[str] = Field(None, alias="thirdPartyTagHostingSource", description="The html tag to use to fetch this creative from the 3p ad server. Required for non publisher hosted creatives (when publ")

    model_config = {'populate_by_name': True}


class ThirdPartyVideoSettings(BaseModel):
    impression_tracking_urls: Optional[list["CreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    language: "LanguageLocale"
    vast_url: Optional[str] = Field(None, alias="vastUrl", description="The url to use to fetch the VAST XML for this video creative. Required for non publisher hosted creatives (when publishe")

    model_config = {'populate_by_name': True}


class ThirdPartyCreative(BaseModel):
    third_party_display_settings: Optional["ThirdPartyDisplaySettings"] = Field(None, alias="thirdPartyDisplaySettings")
    third_party_video_settings: Optional["ThirdPartyVideoSettings"] = Field(None, alias="thirdPartyVideoSettings")

    model_config = {'populate_by_name': True}


class SpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""
    optimize_text: bool = Field(..., alias="optimizeText", description="If the advertiser wants text they provided to be optimized by Amazon or not.")
    videos: list["Video"] = Field(..., description="The video asset(s) to use for the Sponsored Product experience.")

    model_config = {'populate_by_name': True}


class ProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""
    advertised_product: "AdvertisedProducts" = Field(..., alias="advertisedProduct")
    headline: Optional[str] = Field(None, description="The headline/custom text associated with the ad creative.")
    spotlight_videos: Optional["SpotlightVideoSettings"] = Field(None, alias="spotlightVideos")

    model_config = {'populate_by_name': True}


class ProductCreative(BaseModel):
    product_creative_settings: "ProductCreativeSettings" = Field(..., alias="productCreativeSettings")

    model_config = {'populate_by_name': True}


class Audio(BaseModel):
    asset_id: str = Field(..., alias="assetId", description="The asset library ID associated with the audio asset.")
    asset_version: str = Field(..., alias="assetVersion", description="The asset library version associated with the audio asset.")

    model_config = {'populate_by_name': True}


class StandardAudioExperienceSettings(BaseModel):
    audio: "Audio"
    impression_tracking_urls: Optional[list["CreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded. Urls cannot exceed 2048 characters.")
    language: "LanguageLocale"
    products: Optional[list["AdvertisedProducts"]] = Field(None, description="The product(s) being advertised.")

    model_config = {'populate_by_name': True}


class AudioCreative(BaseModel):
    """| AudioCreative | Description | |------|------| | `standardAudioSettings` | The standard audio experience settings. See the Audio Spec for more info: https://advertising.amazon.com/en-us/resources/ad-"""
    pass


class ComponentInventoryType(StrEnum):
    DISPLAY = "DISPLAY"
    NATIVE = "NATIVE"


class CreativeOptimizationGoalKpi(StrEnum):
    CLICK_THROUGH_RATE = "CLICK_THROUGH_RATE"
    DETAIL_PAGE_VIEW_RATE = "DETAIL_PAGE_VIEW_RATE"
    PURCHASE_RATE = "PURCHASE_RATE"


class ResponsiveSizingBehavior(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class BrandStoreCallToActionType(StrEnum):
    BUY_NOW = "BUY_NOW"
    DISCOVER_MORE = "DISCOVER_MORE"
    LEARN_MORE = "LEARN_MORE"
    SEE_DETAILS = "SEE_DETAILS"
    SHOP_NOW = "SHOP_NOW"


class BrandStoreCallToActionSettings(BaseModel):
    """A CTA that directs a customer to a provided url."""
    call_to_action_type: Optional[list["BrandStoreCallToActionType"]] = Field(None, alias="callToActionType", description="Type of CallToAction for BrandStore.")
    deep_linking_behavior: Optional["DeepLinkingBehavior"] = Field(None, alias="deepLinkingBehavior")
    url: str = Field(..., description="The application url that customers are directed to.")

    model_config = {'populate_by_name': True}


class BrandStoreCallToAction(BaseModel):
    pass


class BrandStoreSettings(BaseModel):
    additional_html: Optional[str] = Field(None, alias="additionalHtml", description="Additional HTML to include with the render response for display inventory targets.")
    body_text: Optional[list[str]] = Field(None, alias="bodyText", description="The body text to use for the Brand Store Creative experience.")
    brand: str = Field(..., description="The brand of the product(s) being advertised.")
    call_to_actions: "BrandStoreCallToAction" = Field(..., alias="callToActions")
    click_tracking_urls: Optional[list["CreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    creative_sizes: Optional[list["Size"]] = Field(None, alias="creativeSizes", description="The placement sizes this creative should serve on.")
    disclaimers: Optional[str] = Field(None, description="The disclaimers to use for the Brand Store Creative experience.")
    headlines: list[str] = Field(..., description="The headline(s) to use for the Brand Store Creative experience.")
    impression_tracking_urls: Optional[list["CreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    inventory_types: list["ComponentInventoryType"] = Field(..., alias="inventoryTypes", description="The inventory types this creative should serve on.")
    language: "LanguageLocale"
    logos: Optional["Image"] = None
    optimization_goal_kpi: "CreativeOptimizationGoalKpi" = Field(..., alias="optimizationGoalKpi")
    responsive_sizing_behavior: "ResponsiveSizingBehavior" = Field(..., alias="responsiveSizingBehavior")
    square_images: list["Image"] = Field(..., alias="squareImages", description="The square image(s) to use.")
    tall_images: list["Image"] = Field(..., alias="tallImages", description="The tall image(s) to use.")
    wide_images: list["Image"] = Field(..., alias="wideImages", description="The wide image(s) to use.")

    model_config = {'populate_by_name': True}


class ProductVideoSettings(BaseModel):
    """An ad with a creative that includes a video."""
    brand: Optional[str] = Field(None, description="The name of the brand being advertised.")
    brand_logos: Optional[list["Image"]] = Field(None, alias="brandLogos", description="The brand logo image assets to be used in the ad.")
    enable_creative_auto_translation: Optional[bool] = Field(None, alias="enableCreativeAutoTranslation", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    headlines: Optional[list[str]] = Field(None, description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you ")
    landing_page: Optional["VideoLandingPage"] = Field(None, alias="landingPage")
    moderation_status: Optional["CreativeStatus"] = Field(None, alias="moderationStatus")
    products: Optional[list["AdvertisedProducts"]] = Field(None, description="The products featured in the video ad.")
    untranslated_headlines: Optional[list[str]] = Field(None, alias="untranslatedHeadlines", description="The headline entered by the advertiser.")
    untranslated_videos: list["Video"] = Field(..., alias="untranslatedVideos", description="The original video assets submitted as part of the creative.")
    videos: list["Video"] = Field(..., description="The video assets used in the ad.")

    model_config = {'populate_by_name': True}


class ProductCollectionCreativePropertiesToOptimize(StrEnum):
    HEADLINE = "HEADLINE"


class ProductCollectionLandingPageType(StrEnum):
    ASIN_LIST = "ASIN_LIST"
    CUSTOM_URL = "CUSTOM_URL"
    STORE = "STORE"


class LandingPageAsins(BaseModel):
    asins: list[str] = Field(..., description="For landing page of type ASIN_LIST, the list of ASINs used to create the landing page.")

    model_config = {'populate_by_name': True}


class ProductCollectionLandingPage(BaseModel):
    landing_page_asins: Optional["LandingPageAsins"] = Field(None, alias="landingPageAsins")
    landing_page_type: "ProductCollectionLandingPageType" = Field(..., alias="landingPageType")
    landing_page_url: Optional[str] = Field(None, alias="landingPageUrl", description="The URL associated to the landing page. Read only if landingPageType is ASIN_LIST")

    model_config = {'populate_by_name': True}


class ProductCollectionSettings(BaseModel):
    """An ad creative that contains multiple products and a custom image."""
    brand: str = Field(..., description="The name of the brand being advertised.")
    brand_logos: list["Image"] = Field(..., alias="brandLogos", description="The brand logo image assets to be used in the ad.")
    creative_properties_to_optimize: Optional[list["ProductCollectionCreativePropertiesToOptimize"]] = Field(None, alias="creativePropertiesToOptimize", description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.")
    custom_images: list["Image"] = Field(..., alias="customImages", description="The set of custom images featured in the ad.")
    enable_creative_auto_translation: Optional[bool] = Field(None, alias="enableCreativeAutoTranslation", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    headlines: list[str] = Field(..., description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you ")
    landing_page: "ProductCollectionLandingPage" = Field(..., alias="landingPage")
    moderation_status: Optional["CreativeStatus"] = Field(None, alias="moderationStatus")
    products: Optional[list["AdvertisedProducts"]] = Field(None, description="The products featured in the ad.")
    untranslated_headlines: Optional[list[str]] = Field(None, alias="untranslatedHeadlines", description="The headlines entered by the advertiser.")

    model_config = {'populate_by_name': True}


class Background(BaseModel):
    color: Optional[str] = Field(None, description="The color hex code of the background.")

    model_config = {'populate_by_name': True}


class ComponentLandingPageType(StrEnum):
    OFF_AMAZON_LINK = "OFF_AMAZON_LINK"


class ComponentLandingPage(BaseModel):
    landing_page_type: "ComponentLandingPageType" = Field(..., alias="landingPageType")
    landing_page_url: str = Field(..., alias="landingPageUrl", description="The URL of landing page where the ad directs.")

    model_config = {'populate_by_name': True}


class AssetBasedCreativeCallToActionType(StrEnum):
    BOOK_NOW = "BOOK_NOW"
    BUY_NOW = "BUY_NOW"
    DISCOVER_MORE = "DISCOVER_MORE"
    DOWNLOAD_NOW = "DOWNLOAD_NOW"
    EXPLORE_NOW = "EXPLORE_NOW"
    GET_APP = "GET_APP"
    GET_QUOTE = "GET_QUOTE"
    LEARN_MORE = "LEARN_MORE"
    PRE_ORDER_NOW = "PRE_ORDER_NOW"
    SEE_DETAILS = "SEE_DETAILS"
    SHOP_NOW = "SHOP_NOW"
    SIGN_UP_NOW = "SIGN_UP_NOW"
    SUBSCRIBE_NOW = "SUBSCRIBE_NOW"


class AssetBasedCreativeCallToActionSettings(BaseModel):
    """A CTA that directs a customer to a provided url."""
    call_to_action_type: Optional[list["AssetBasedCreativeCallToActionType"]] = Field(None, alias="callToActionType", description="Type of CallToAction for AssetBasedCreative.")
    deep_linking_behavior: Optional["DeepLinkingBehavior"] = Field(None, alias="deepLinkingBehavior")
    url: str = Field(..., description="The application url that customers are directed to.")

    model_config = {'populate_by_name': True}


class AssetBasedCreativeCallToAction(BaseModel):
    pass


class AssetBasedCreativeSettings(BaseModel):
    additional_html: Optional[str] = Field(None, alias="additionalHtml", description="Additional HTML to include with the render response for display inventory targets.")
    backgrounds: Optional[list["Background"]] = Field(None, description="The background which is displayed on the ad.")
    body_text: Optional[list[str]] = Field(None, alias="bodyText", description="The body text to use for the Asset Based Creative experience.")
    brand: Optional[str] = Field(None, description="The brand of the product(s) being advertised.")
    call_to_actions: Optional["AssetBasedCreativeCallToAction"] = Field(None, alias="callToActions")
    click_tracking_urls: Optional[list["CreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    creative_sizes: Optional[list["Size"]] = Field(None, alias="creativeSizes", description="The placement sizes this creative should serve on.")
    custom_videos: Optional["Video"] = Field(None, alias="customVideos")
    disclaimers: Optional[str] = Field(None, description="The disclaimers to use for the Asset Based Creative experience.")
    enable_creative_auto_translation: Optional[bool] = Field(None, alias="enableCreativeAutoTranslation", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    has_terms_and_conditions: Optional[bool] = Field(None, alias="hasTermsAndConditions", description="Indicates that the ad promotes a free product or service and has qualifying terms and conditions applicable to the custo")
    headlines: list[str] = Field(..., description="The headline(s) to use for the Asset Based Creative experience.")
    images: Optional[list["Image"]] = Field(None, description="The image(s) to use.")
    impression_tracking_urls: Optional[list["CreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    inventory_types: Optional[list["ComponentInventoryType"]] = Field(None, alias="inventoryTypes", description="The inventory types this creative should serve on.")
    landing_page: Optional["ComponentLandingPage"] = Field(None, alias="landingPage")
    language: Optional["LanguageLocale"] = None
    logos: Optional[list["Image"]] = Field(None, description="The logos to use for the Asset Based Creative experience.")
    moderation_status: Optional["CreativeStatus"] = Field(None, alias="moderationStatus")
    optimization_goal_kpi: Optional["CreativeOptimizationGoalKpi"] = Field(None, alias="optimizationGoalKpi")
    responsive_sizing_behavior: Optional["ResponsiveSizingBehavior"] = Field(None, alias="responsiveSizingBehavior")
    square_images: Optional[list["Image"]] = Field(None, alias="squareImages", description="The square image(s) to use.")
    tall_images: Optional[list["Image"]] = Field(None, alias="tallImages", description="The tall image(s) to use.")
    untranslated_headlines: Optional[list[str]] = Field(None, alias="untranslatedHeadlines", description="The headline entered by the advertiser.")
    wide_images: Optional[list["Image"]] = Field(None, alias="wideImages", description="The wide image(s) to use.")

    model_config = {'populate_by_name': True}


class SupportedThirdPartySellers(StrEnum):
    ALL = "ALL"
    NONE = "NONE"


class ResponsiveEcommerceCreativePropertiesToOptimize(StrEnum):
    HEADLINE = "HEADLINE"


class ResponsiveEcommerceAdVariations(StrEnum):
    ADD_TO_CART = "ADD_TO_CART"
    COUPON = "COUPON"
    CUSTOMER_REVIEWS = "CUSTOMER_REVIEWS"
    SHOP_NOW = "SHOP_NOW"


class ResponsiveEcommerceLandingPageType(StrEnum):
    MOMENT = "MOMENT"
    STORE = "STORE"


class ResponsiveEcommerceLandingPage(BaseModel):
    landing_page_type: "ResponsiveEcommerceLandingPageType" = Field(..., alias="landingPageType")
    landing_page_url: str = Field(..., alias="landingPageUrl", description="The URL of landing page where the ad directs.")

    model_config = {'populate_by_name': True}


class ResponsiveEcommerceSettings(BaseModel):
    click_tracking_urls: Optional[list["CreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    creative_properties_to_optimize: Optional[list["ResponsiveEcommerceCreativePropertiesToOptimize"]] = Field(None, alias="creativePropertiesToOptimize", description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.")
    creative_sizes: Optional[list["Size"]] = Field(None, alias="creativeSizes", description="The placement sizes this creative should serve on.")
    disclaimers: Optional[str] = Field(None, description="The disclaimer to use for the Responsive eCommerce experience.")
    enable_creative_auto_translation: Optional[bool] = Field(None, alias="enableCreativeAutoTranslation", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    headlines: Optional[str] = Field(None, description="The headline to use for the Responsive eCommerce experience.")
    images: Optional[list["Image"]] = Field(None, description="The image(s) to use.")
    impression_tracking_urls: Optional[list["CreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    inventory_types: Optional[list["ComponentInventoryType"]] = Field(None, alias="inventoryTypes", description="The inventory types this creative should serve on.")
    landing_page: Optional["ResponsiveEcommerceLandingPage"] = Field(None, alias="landingPage")
    language: Optional["LanguageLocale"] = None
    logos: Optional["Image"] = None
    moderation_status: Optional["CreativeStatus"] = Field(None, alias="moderationStatus")
    optimization_goal_kpi: Optional["CreativeOptimizationGoalKpi"] = Field(None, alias="optimizationGoalKpi")
    products: Optional[list["AdvertisedProducts"]] = Field(None, description="The products advertised for the Responsive eCommerce experience.")
    rec_ad_variations: Optional[list["ResponsiveEcommerceAdVariations"]] = Field(None, alias="recAdVariations", description="The rendering variations selected for the Responsive eCommerce experience.")
    responsive_sizing_behavior: Optional["ResponsiveSizingBehavior"] = Field(None, alias="responsiveSizingBehavior")
    supported_third_party_sellers: Optional["SupportedThirdPartySellers"] = Field(None, alias="supportedThirdPartySellers")
    untranslated_headlines: Optional[str] = Field(None, alias="untranslatedHeadlines", description="The headline entered by the advertiser.")

    model_config = {'populate_by_name': True}


class StoreSpotlightLandingPageType(StrEnum):
    STORE = "STORE"


class StoreSpotlightLandingPage(BaseModel):
    landing_page_type: "StoreSpotlightLandingPageType" = Field(..., alias="landingPageType")
    landing_page_url: str = Field(..., alias="landingPageUrl", description="The URL of landing page where the ad directs.")

    model_config = {'populate_by_name': True}


class StoreSpotlightCreativePropertiesToOptimize(StrEnum):
    HEADLINE = "HEADLINE"


class CardCreativeElement(BaseModel):
    headline: str = Field(..., description="The headline used for the card.")
    landing_page: "StoreSpotlightLandingPage" = Field(..., alias="landingPage")
    products: "AdvertisedProducts"

    model_config = {'populate_by_name': True}


class StoreSpotlightSettings(BaseModel):
    """An ad creative that contains ASINs within a brand Store."""
    brand: str = Field(..., description="The name of the brand being advertised.")
    brand_logos: list["Image"] = Field(..., alias="brandLogos", description="The brand logo image assets to be used in the ad.")
    cards: list["CardCreativeElement"] = Field(..., description="The sub-elements of the creative. Each card highlights a different ASIN associated to a brand Store.")
    creative_properties_to_optimize: Optional[list["StoreSpotlightCreativePropertiesToOptimize"]] = Field(None, alias="creativePropertiesToOptimize", description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.")
    enable_creative_auto_translation: Optional[bool] = Field(None, alias="enableCreativeAutoTranslation", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    headlines: list[str] = Field(..., description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you ")
    landing_page: "StoreSpotlightLandingPage" = Field(..., alias="landingPage")
    moderation_status: Optional["CreativeStatus"] = Field(None, alias="moderationStatus")
    untranslated_headlines: Optional[list[str]] = Field(None, alias="untranslatedHeadlines", description="The headline entered by the advertiser.")

    model_config = {'populate_by_name': True}


class CollectionLandingPageType(StrEnum):
    ASIN_LIST = "ASIN_LIST"
    STORE = "STORE"


class CollectionLandingPage(BaseModel):
    landing_page_type: "CollectionLandingPageType" = Field(..., alias="landingPageType")
    landing_page_url: Optional[str] = Field(None, alias="landingPageUrl", description="The URL associated to the landing page.")

    model_config = {'populate_by_name': True}


class SharedCollectionSettings(BaseModel):
    """Settings shared by all collection types."""
    brand: str = Field(..., description="The name of the brand being advertised.")
    brand_logos: Optional["Image"] = Field(None, alias="brandLogos")
    moderation_status: Optional["CreativeStatus"] = Field(None, alias="moderationStatus")

    model_config = {'populate_by_name': True}


class ManualCollectionSettings(BaseModel):
    """Settings for manually curated collections."""
    landing_page: "CollectionLandingPage" = Field(..., alias="landingPage")
    product_inclusions: list["AdvertisedProducts"] = Field(..., alias="productInclusions", description="The products featured in the ad. Required for manual collections.")
    shared_settings: "SharedCollectionSettings" = Field(..., alias="sharedSettings")

    model_config = {'populate_by_name': True}


class AutoCollectionSettings(BaseModel):
    """Settings for automatically generated collections."""
    product_exclusions: Optional[list["AdvertisedProducts"]] = Field(None, alias="productExclusions", description="Products to exclude from auto collection.")
    shared_settings: "SharedCollectionSettings" = Field(..., alias="sharedSettings")

    model_config = {'populate_by_name': True}


class ComponentCreative(BaseModel):
    asset_based_creative_settings: Optional["AssetBasedCreativeSettings"] = Field(None, alias="assetBasedCreativeSettings")
    auto_collection_settings: Optional["AutoCollectionSettings"] = Field(None, alias="autoCollectionSettings")
    brand_store_settings: Optional["BrandStoreSettings"] = Field(None, alias="brandStoreSettings")
    manual_collection_settings: Optional["ManualCollectionSettings"] = Field(None, alias="manualCollectionSettings")
    product_collection_settings: Optional["ProductCollectionSettings"] = Field(None, alias="productCollectionSettings")
    product_video_settings: Optional["ProductVideoSettings"] = Field(None, alias="productVideoSettings")
    responsive_ecommerce_settings: Optional["ResponsiveEcommerceSettings"] = Field(None, alias="responsiveEcommerceSettings")
    store_spotlight_settings: Optional["StoreSpotlightSettings"] = Field(None, alias="storeSpotlightSettings")

    model_config = {'populate_by_name': True}


class Creative(BaseModel):
    pass


class DeliveryStatus(StrEnum):
    DELIVERING = "DELIVERING"
    LIMITED = "LIMITED"
    NOT_DELIVERING = "NOT_DELIVERING"
    UNAVAILABLE = "UNAVAILABLE"


class DeliveryReason(StrEnum):
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_INELIGIBLE = "ADVERTISER_INELIGIBLE"
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"
    ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT = "ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT"
    ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET = "ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET"
    ADVERTISER_OUT_OF_PREPAY_BALANCE = "ADVERTISER_OUT_OF_PREPAY_BALANCE"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    AD_ARCHIVED = "AD_ARCHIVED"
    AD_CREATION_FAILED = "AD_CREATION_FAILED"
    AD_CREATION_IN_PROGRESS = "AD_CREATION_IN_PROGRESS"
    AD_CREATIVES_NOT_RUNNING = "AD_CREATIVES_NOT_RUNNING"
    AD_EXTENSION_ARCHIVED = "AD_EXTENSION_ARCHIVED"
    AD_EXTENSION_PAUSED = "AD_EXTENSION_PAUSED"
    AD_EXTENSION_POLICING_PENDING_REVIEW = "AD_EXTENSION_POLICING_PENDING_REVIEW"
    AD_EXTENSION_POLICING_SUSPENDED = "AD_EXTENSION_POLICING_SUSPENDED"
    AD_GROUPS_NOT_RUNNING = "AD_GROUPS_NOT_RUNNING"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_ENDED = "AD_GROUP_ENDED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_INELIGIBLE_GOAL_KPI = "AD_GROUP_INELIGIBLE_GOAL_KPI"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    AD_GROUP_MISSING_CONVERSION_TRACKING_SELECTIONS = "AD_GROUP_MISSING_CONVERSION_TRACKING_SELECTIONS"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_PENDING_REVIEW = "AD_GROUP_PENDING_REVIEW"
    AD_GROUP_PENDING_START_DATE = "AD_GROUP_PENDING_START_DATE"
    AD_GROUP_POLICING_PENDING_REVIEW = "AD_GROUP_POLICING_PENDING_REVIEW"
    AD_GROUP_POLICING_SUSPENDED = "AD_GROUP_POLICING_SUSPENDED"
    AD_GROUP_REJECTED = "AD_GROUP_REJECTED"
    AD_GROUP_TOO_FEW_CONVERSION_TRACKING_SELECTIONS = "AD_GROUP_TOO_FEW_CONVERSION_TRACKING_SELECTIONS"
    AD_GROUP_TOO_MANY_CONVERSION_TRACKING_SELECTIONS = "AD_GROUP_TOO_MANY_CONVERSION_TRACKING_SELECTIONS"
    AD_INELIGIBLE = "AD_INELIGIBLE"
    AD_MISSING_DECORATION = "AD_MISSING_DECORATION"
    AD_MISSING_IMAGE = "AD_MISSING_IMAGE"
    AD_NOT_APPROVED_FOR_ALL_AD_GROUPS = "AD_NOT_APPROVED_FOR_ALL_AD_GROUPS"
    AD_NOT_ASSOCIATED_WITH_AD_GROUP = "AD_NOT_ASSOCIATED_WITH_AD_GROUP"
    AD_NOT_DELIVERING = "AD_NOT_DELIVERING"
    AD_PAUSED = "AD_PAUSED"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    AD_POLICING_SUSPENDED = "AD_POLICING_SUSPENDED"
    BRAND_INELIGIBLE = "BRAND_INELIGIBLE"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_END_DATE_REACHED = "CAMPAIGN_END_DATE_REACHED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_PENDING_REVIEW = "CAMPAIGN_PENDING_REVIEW"
    CAMPAIGN_PENDING_START_DATE = "CAMPAIGN_PENDING_START_DATE"
    CAMPAIGN_POLICING_SUSPENDED = "CAMPAIGN_POLICING_SUSPENDED"
    CAMPAIGN_REJECTED = "CAMPAIGN_REJECTED"
    CREATIVE_MISSING_ASSET = "CREATIVE_MISSING_ASSET"
    CREATIVE_PENDING_REVIEW = "CREATIVE_PENDING_REVIEW"
    CREATIVE_REJECTED = "CREATIVE_REJECTED"
    LANDING_PAGE_INELIGIBLE = "LANDING_PAGE_INELIGIBLE"
    LANDING_PAGE_NOT_AVAILABLE = "LANDING_PAGE_NOT_AVAILABLE"
    MODERATION_ADULT_NOVELTY_POLICY_VIOLATION = "MODERATION_ADULT_NOVELTY_POLICY_VIOLATION"
    MODERATION_ADULT_PRODUCT_POLICY_VIOLATION = "MODERATION_ADULT_PRODUCT_POLICY_VIOLATION"
    MODERATION_ADULT_SOFTLINES_POLICY_VIOLATION = "MODERATION_ADULT_SOFTLINES_POLICY_VIOLATION"
    MODERATION_CLAIM_WEIGHTLOSS_POLICY_VIOLATION = "MODERATION_CLAIM_WEIGHTLOSS_POLICY_VIOLATION"
    MODERATION_CONTENT_NUDITY_POLICY_VIOLATION = "MODERATION_CONTENT_NUDITY_POLICY_VIOLATION"
    MODERATION_CONTENT_PROVOCATIVE_POLICY_VIOLATION = "MODERATION_CONTENT_PROVOCATIVE_POLICY_VIOLATION"
    MODERATION_CONTENT_SMOKING_POLICY_VIOLATION = "MODERATION_CONTENT_SMOKING_POLICY_VIOLATION"
    MODERATION_CRITICAL_EVENTS_POLICY_VIOLATION = "MODERATION_CRITICAL_EVENTS_POLICY_VIOLATION"
    MODERATION_ERROR_404 = "MODERATION_ERROR_404"
    MODERATION_GRAPHICAL_SEXUAL_IMAGES_POLICY_VIOLATION = "MODERATION_GRAPHICAL_SEXUAL_IMAGES_POLICY_VIOLATION"
    MODERATION_HFSS_PRODUCT_POLICY_VIOLATION = "MODERATION_HFSS_PRODUCT_POLICY_VIOLATION"
    MODERATION_LANGUAGE_OFFENSIVE_POLICY_VIOLATION = "MODERATION_LANGUAGE_OFFENSIVE_POLICY_VIOLATION"
    MODERATION_NOT_COMPLIANT_TO_AD_POLICY = "MODERATION_NOT_COMPLIANT_TO_AD_POLICY"
    MODERATION_SMOKING_RELATED_POLICY_VIOLATION = "MODERATION_SMOKING_RELATED_POLICY_VIOLATION"
    NOT_BUYABLE = "NOT_BUYABLE"
    NOT_IN_BUYBOX = "NOT_IN_BUYBOX"
    NOT_IN_POLICY = "NOT_IN_POLICY"
    NO_INVENTORY = "NO_INVENTORY"
    NO_PURCHASABLE_OFFER = "NO_PURCHASABLE_OFFER"
    OTHER = "OTHER"
    OUT_OF_REWARD_BUDGET = "OUT_OF_REWARD_BUDGET"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    PIR_RULE_EXCLUDED = "PIR_RULE_EXCLUDED"
    PORTFOLIO_ARCHIVED = "PORTFOLIO_ARCHIVED"
    PORTFOLIO_END_DATE_REACHED = "PORTFOLIO_END_DATE_REACHED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    PORTFOLIO_PAUSED = "PORTFOLIO_PAUSED"
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"
    SECURITY_SCAN_PENDING_REVIEW = "SECURITY_SCAN_PENDING_REVIEW"
    SECURITY_SCAN_REJECTED = "SECURITY_SCAN_REJECTED"
    SPEND_LIMIT_EXCEEDED = "SPEND_LIMIT_EXCEEDED"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"
    TARGET_ARCHIVED = "TARGET_ARCHIVED"
    TARGET_BLOCKED = "TARGET_BLOCKED"
    TARGET_PAUSED = "TARGET_PAUSED"
    TARGET_POLICING_SUSPENDED = "TARGET_POLICING_SUSPENDED"


class StatusMarketplaceSetting(BaseModel):
    delivery_reasons: Optional[list["DeliveryReason"]] = Field(None, alias="deliveryReasons", description="This is the list of reasons behind the delivery status.")
    delivery_status: "DeliveryStatus" = Field(..., alias="deliveryStatus")
    marketplace: "Marketplace"

    model_config = {'populate_by_name': True}


class Status(BaseModel):
    delivery_reasons: Optional[list["DeliveryReason"]] = Field(None, alias="deliveryReasons", description="This is the list of reasons behind the delivery status.")
    delivery_status: "DeliveryStatus" = Field(..., alias="deliveryStatus")
    marketplace_settings: Optional[list["StatusMarketplaceSetting"]] = Field(None, alias="marketplaceSettings", description="The list of marketplace level delivery status and reasons of global resources, for all the marketplaces the global resou")

    model_config = {'populate_by_name': True}


class AdProduct(StrEnum):
    AMAZON_DSP = "AMAZON_DSP"
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"
    SPONSORED_TELEVISION = "SPONSORED_TELEVISION"


class MarketplaceScope(StrEnum):
    GLOBAL = "GLOBAL"
    SINGLE_MARKETPLACE = "SINGLE_MARKETPLACE"


class AdType(StrEnum):
    AUDIO = "AUDIO"
    COMPONENT = "COMPONENT"
    DISPLAY = "DISPLAY"
    PRODUCT_AD = "PRODUCT_AD"
    THIRD_PARTY = "THIRD_PARTY"
    VIDEO = "VIDEO"


class State(StrEnum):
    ARCHIVED = "ARCHIVED"
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


class Tag(BaseModel):
    key: str = Field(..., description="A custom key value pair entered by the advertiser.")
    value: str = Field(..., description="A custom key value pair entered by the advertiser.")

    model_config = {'populate_by_name': True}


class MarketplaceAdFieldOverrides(BaseModel):
    state: Optional["State"] = None
    tags: Optional[list["Tag"]] = Field(None, description="Open ended labels with a key value pair applied to the ad")

    model_config = {'populate_by_name': True}


class MarketplaceAdConfigurations(BaseModel):
    ad_id: str = Field(..., alias="adId", description="Represents marketplace ad id (Ex: adId-US) associated to global ad (Ex: adId-Global)")
    marketplace: "Marketplace"
    overrides: "MarketplaceAdFieldOverrides"

    model_config = {'populate_by_name': True}


class Ad(BaseModel):
    active_creative: Optional["Creative"] = Field(None, alias="activeCreative")
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="The ad group associated with the ad.")
    ad_id: str = Field(..., alias="adId", description="The identifier of the ad.")
    ad_product: "AdProduct" = Field(..., alias="adProduct")
    ad_type: "AdType" = Field(..., alias="adType")
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="The campaign associated with the ad. It's a read-only field.")
    creation_date_time: str = Field(..., alias="creationDateTime", description="The date time that the ad was created.")
    creative: "Creative"
    global_ad_id: Optional[str] = Field(None, alias="globalAdId", description="The global ad identifier that manages this marketplace ad.")
    last_updated_date_time: str = Field(..., alias="lastUpdatedDateTime", description="The date time that the ad was last updated.")
    marketplace_configurations: Optional[list["MarketplaceAdConfigurations"]] = Field(None, alias="marketplaceConfigurations", description="List of marketplace-specific configurations for a global ad that enables overriding certain attributes at individual mar")
    marketplace_scope: Optional["MarketplaceScope"] = Field(None, alias="marketplaceScope")
    marketplaces: Optional[list["Marketplace"]] = Field(None, description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the ")
    name: Optional[str] = Field(None, description="The name of the ad.")
    state: "State"
    status: Optional["Status"] = None
    tags: Optional[list["Tag"]] = Field(None, description="Open ended labels with a key value pair applied to the ad")

    model_config = {'populate_by_name': True}


class AdAdGroupIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class AdAdIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class AdAdProductFilter(BaseModel):
    include: list["AdProduct"] = Field(..., description="| AdProduct | Description | | --- | --- | | `SPONSORED_PRODUCTS` | Sponsored Products ad product. | | `SPONSORED_BRANDS`")

    model_config = {'populate_by_name': True}


class AdAssociation(BaseModel):
    ad_association_id: str = Field(..., alias="adAssociationId", description="The unique identifier of the ad association.")
    ad_group_id: str = Field(..., alias="adGroupId", description="The ad group associated with the ad.")
    ad_id: str = Field(..., alias="adId", description="The ad Id  associated with the ad.")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The end date time for the ad association.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The start date time for the ad association.")
    state: "State"
    weight: Optional[int] = Field(None, description="The relative percentage of traffic which would be directed to the associated Ad Creative in the Ad Group.")

    model_config = {'populate_by_name': True}


class AdAssociationAdAssociationIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class AdAssociationAdGroupIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class AdAssociationAdIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class CreateState(StrEnum):
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


class AdAssociationCreate(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The ad group associated with the ad.")
    ad_id: str = Field(..., alias="adId", description="The ad Id  associated with the ad.")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The end date time for the ad association.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The start date time for the ad association.")
    state: "CreateState"
    weight: Optional[int] = Field(None, description="The relative percentage of traffic which would be directed to the associated Ad Creative in the Ad Group.")

    model_config = {'populate_by_name': True}


class ErrorCode(StrEnum):
    ACTION_NOT_SUPPORTED = "ACTION_NOT_SUPPORTED"
    ACTIVE_RESOURCE_LIMIT_EXCEEDED = "ACTIVE_RESOURCE_LIMIT_EXCEEDED"
    ARCHIVED_PARENT_CANNOT_CREATE = "ARCHIVED_PARENT_CANNOT_CREATE"
    ARCHIVED_PARENT_CANNOT_EDIT = "ARCHIVED_PARENT_CANNOT_EDIT"
    ARCHIVED_RESOURCE_CANNOT_EDIT = "ARCHIVED_RESOURCE_CANNOT_EDIT"
    ASSET_NOT_READY = "ASSET_NOT_READY"
    AUTOCREATED_ENTITY_CANNOT_EDIT = "AUTOCREATED_ENTITY_CANNOT_EDIT"
    BAD_REQUEST = "BAD_REQUEST"
    CONFLICT = "CONFLICT"
    CONTENT_TOO_LARGE = "CONTENT_TOO_LARGE"
    DATE_CANNOT_BE_IN_PAST = "DATE_CANNOT_BE_IN_PAST"
    DATE_CANNOT_BE_NULL = "DATE_CANNOT_BE_NULL"
    DATE_TOO_SOON = "DATE_TOO_SOON"
    DUPLICATE_FIELD_VALUE_FOUND = "DUPLICATE_FIELD_VALUE_FOUND"
    DUPLICATE_RESOURCE_ID_FOUND = "DUPLICATE_RESOURCE_ID_FOUND"
    DURATION_TOO_SHORT = "DURATION_TOO_SHORT"
    FEATURE_DISCONTINUED = "FEATURE_DISCONTINUED"
    FEATURE_NOT_AVAILABLE = "FEATURE_NOT_AVAILABLE"
    FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT = "FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT"
    FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT = "FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT"
    FIELD_SIZE_IS_OUT_OF_RANGE = "FIELD_SIZE_IS_OUT_OF_RANGE"
    FIELD_VALUE_CANNOT_EDIT = "FIELD_VALUE_CANNOT_EDIT"
    FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS = "FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS"
    FIELD_VALUE_CONTAINS_INVALID_CHARACTERS = "FIELD_VALUE_CONTAINS_INVALID_CHARACTERS"
    FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT = "FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT"
    FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT = "FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT"
    FIELD_VALUE_IS_EMPTY = "FIELD_VALUE_IS_EMPTY"
    FIELD_VALUE_IS_INVALID = "FIELD_VALUE_IS_INVALID"
    FIELD_VALUE_IS_NULL = "FIELD_VALUE_IS_NULL"
    FIELD_VALUE_IS_OUT_OF_RANGE = "FIELD_VALUE_IS_OUT_OF_RANGE"
    FIELD_VALUE_MISMATCH = "FIELD_VALUE_MISMATCH"
    FIELD_VALUE_MUST_BE_EMPTY_OR_NULL = "FIELD_VALUE_MUST_BE_EMPTY_OR_NULL"
    FIELD_VALUE_NOT_FOUND = "FIELD_VALUE_NOT_FOUND"
    FIELD_VALUE_NOT_UNIQUE = "FIELD_VALUE_NOT_UNIQUE"
    FORBIDDEN = "FORBIDDEN"
    GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_PORTFOLIO = "GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_PORTFOLIO"
    GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_STATE = "GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_STATE"
    GLOBAL_CAMPAIGN_SINGLE_ADGROUP_LIMIT = "GLOBAL_CAMPAIGN_SINGLE_ADGROUP_LIMIT"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    NOT_FOUND = "NOT_FOUND"
    PAYMENT_ISSUE = "PAYMENT_ISSUE"
    PRODUCT_INELIGIBLE = "PRODUCT_INELIGIBLE"
    RESOURCE_DOES_NOT_BELONG_TO_PARENT = "RESOURCE_DOES_NOT_BELONG_TO_PARENT"
    RESOURCE_ID_NOT_FOUND = "RESOURCE_ID_NOT_FOUND"
    RESOURCE_IS_EMPTY = "RESOURCE_IS_EMPTY"
    RESOURCE_IS_IN_TERMINAL_STATE = "RESOURCE_IS_IN_TERMINAL_STATE"
    RESOURCE_IS_NULL = "RESOURCE_IS_NULL"
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"
    TOTAL_RESOURCE_LIMIT_EXCEEDED = "TOTAL_RESOURCE_LIMIT_EXCEEDED"
    UNAUTHORIZED = "UNAUTHORIZED"
    UNSUPPORTED_MARKETPLACE = "UNSUPPORTED_MARKETPLACE"


class Error(BaseModel):
    code: "ErrorCode"
    field_location: Optional[str] = Field(None, alias="fieldLocation")
    message: str

    model_config = {'populate_by_name': True}


class ErrorsIndex(BaseModel):
    errors: list["Error"]
    index: int

    model_config = {'populate_by_name': True}


class AdAssociationMultiStatusSuccess(BaseModel):
    ad_association: "AdAssociation" = Field(..., alias="adAssociation")
    index: int

    model_config = {'populate_by_name': True}


class AdAssociationMultiStatusResponse(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    success: Optional[list["AdAssociationMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class AdAssociationSuccessResponse(BaseModel):
    ad_associations: Optional[list["AdAssociation"]] = Field(None, alias="adAssociations")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class UpdateState(StrEnum):
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


class AdAssociationUpdate(BaseModel):
    ad_association_id: str = Field(..., alias="adAssociationId", description="The unique identifier of the ad association.")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The end date time for the ad association.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The start date time for the ad association.")
    state: Optional["UpdateState"] = None
    weight: Optional[int] = Field(None, description="The relative percentage of traffic which would be directed to the associated Ad Creative in the Ad Group.")

    model_config = {'populate_by_name': True}


class AdCampaignIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class CreateCreativeTrackingUrl(BaseModel):
    url: str = Field(..., description="A url to be triggered for tracking events.")

    model_config = {'populate_by_name': True}


class CreateClickToAppDisplayCallToActionSettings(BaseModel):
    """A CTA that directs a customer to a provided url."""
    deep_linking_behavior: "DeepLinkingBehavior" = Field(..., alias="deepLinkingBehavior")
    url: str = Field(..., description="The app that customers are directed to.")

    model_config = {'populate_by_name': True}


class CreateClickToUrlDisplayCallToActionSettings(BaseModel):
    """A CTA that directs a customer to a provided url."""
    deep_linking_behavior: "DeepLinkingBehavior" = Field(..., alias="deepLinkingBehavior")
    url: str = Field(..., description="The application url that customers are directed to.")

    model_config = {'populate_by_name': True}


class CreateDisplayCallToAction(BaseModel):
    pass


class CreateFormatProperties(BaseModel):
    apply_border: Optional[bool] = Field(None, alias="applyBorder", description="Apply a boarder to the image to fit rules for some supplies.")
    height: Optional[int] = Field(None, description="The height (in pixels) of the cropped image.")
    left: Optional[int] = Field(None, description="The number of pixels from the left of the image where the crop should begin.")
    top: Optional[int] = Field(None, description="The number of pixels from the top of the image where the crop should begin.")
    width: Optional[int] = Field(None, description="The width (in pixels) of the cropped image.")

    model_config = {'populate_by_name': True}


class CreateImage(BaseModel):
    asset_id: str = Field(..., alias="assetId", description="The asset library ID associated with the image asset.")
    asset_version: str = Field(..., alias="assetVersion", description="The asset library version associated with the image asset.")
    format_properties: Optional[list["CreateFormatProperties"]] = Field(None, alias="formatProperties", description="The cropping and positioning properties associated with the asset.")

    model_config = {'populate_by_name': True}


class CreateSize(BaseModel):
    height: int = Field(..., description="The height of the creative placement.")
    width: int = Field(..., description="The width of the creative placement.")

    model_config = {'populate_by_name': True}


class CreateStandardDisplaySettings(BaseModel):
    ad_choices_position: "AdChoicesPosition" = Field(..., alias="adChoicesPosition")
    call_to_action: Optional["CreateDisplayCallToAction"] = Field(None, alias="callToAction")
    click_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    creative_sizes: list["CreateSize"] = Field(..., alias="creativeSizes", description="The list of placement sizes this creative should serve on.")
    custom_images: list["CreateImage"] = Field(..., alias="customImages", description="The custom images to use for the standard display experience.")
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    language: "LanguageLocale"

    model_config = {'populate_by_name': True}


class CreateDisplayCreative(BaseModel):
    standard_display_settings: Optional["CreateStandardDisplaySettings"] = Field(None, alias="standardDisplaySettings")

    model_config = {'populate_by_name': True}


class CreateAudio(BaseModel):
    asset_id: str = Field(..., alias="assetId", description="The asset library ID associated with the audio asset.")
    asset_version: str = Field(..., alias="assetVersion", description="The asset library version associated with the audio asset.")

    model_config = {'populate_by_name': True}


class CreateGlobalStoreSettings(BaseModel):
    catalog_source_marketplace: Optional["Marketplace"] = Field(None, alias="catalogSourceMarketplace")

    model_config = {'populate_by_name': True}


class CreateAdvertisedProductMarketplaceSetting(BaseModel):
    global_store_setting: Optional["CreateGlobalStoreSettings"] = Field(None, alias="globalStoreSetting")
    marketplace: "Marketplace"
    product_id: str = Field(..., alias="productId", description="The identifier of the product advertised.")

    model_config = {'populate_by_name': True}


class CreateAdvertisedProducts(BaseModel):
    global_store_setting: Optional["CreateGlobalStoreSettings"] = Field(None, alias="globalStoreSetting")
    marketplace_settings: Optional[list["CreateAdvertisedProductMarketplaceSetting"]] = Field(None, alias="marketplaceSettings", description="List of advertised product selectively applied at the given marketplace level")
    product_id: Optional[str] = Field(None, alias="productId", description="The identifier of the advertised product.")
    product_id_type: "ProductIdType" = Field(..., alias="productIdType")

    model_config = {'populate_by_name': True}


class CreateStandardAudioExperienceSettings(BaseModel):
    audio: "CreateAudio"
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded. Urls cannot exceed 2048 characters.")
    language: "LanguageLocale"
    products: Optional[list["CreateAdvertisedProducts"]] = Field(None, description="The product(s) being advertised.")

    model_config = {'populate_by_name': True}


class CreateAudioCreative(BaseModel):
    """| CreateAudioCreative | Description | | --- | --- | | `standardAudioSettings` | The standard audio experience settings. See the Audio Spec for more info: https://advertising.amazon.com/en-us/resources"""
    pass


class CreateThirdPartyDisplaySettings(BaseModel):
    ad_choices_position: "AdChoicesPosition" = Field(..., alias="adChoicesPosition")
    additional_html: Optional[str] = Field(None, alias="additionalHtml", description="Additional html to be included along with the creative when rendered.")
    click_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    creative_sizes: Optional[list["CreateSize"]] = Field(None, alias="creativeSizes", description="The list of placement sizes this creative should serve on. Required for non publisher hosted creatives (when publisherHo")
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    language: "LanguageLocale"
    third_party_tag_hosting_source: Optional[str] = Field(None, alias="thirdPartyTagHostingSource", description="The html tag to use to fetch this creative from the 3p ad server. Required for non publisher hosted creatives (when publ")

    model_config = {'populate_by_name': True}


class CreateThirdPartyVideoSettings(BaseModel):
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    language: "LanguageLocale"
    vast_url: Optional[str] = Field(None, alias="vastUrl", description="The url to use to fetch the VAST XML for this video creative. Required for non publisher hosted creatives (when publishe")

    model_config = {'populate_by_name': True}


class CreateThirdPartyCreative(BaseModel):
    third_party_display_settings: Optional["CreateThirdPartyDisplaySettings"] = Field(None, alias="thirdPartyDisplaySettings")
    third_party_video_settings: Optional["CreateThirdPartyVideoSettings"] = Field(None, alias="thirdPartyVideoSettings")

    model_config = {'populate_by_name': True}


class CreateBrandStoreCallToActionSettings(BaseModel):
    """A CTA that directs a customer to a provided url."""
    call_to_action_type: Optional[list["BrandStoreCallToActionType"]] = Field(None, alias="callToActionType", description="Type of CallToAction for BrandStore.")
    deep_linking_behavior: Optional["DeepLinkingBehavior"] = Field(None, alias="deepLinkingBehavior")
    url: str = Field(..., description="The application url that customers are directed to.")

    model_config = {'populate_by_name': True}


class CreateBrandStoreCallToAction(BaseModel):
    pass


class CreateBrandStoreSettings(BaseModel):
    additional_html: Optional[str] = Field(None, alias="additionalHtml", description="Additional HTML to include with the render response for display inventory targets.")
    body_text: Optional[list[str]] = Field(None, alias="bodyText", description="The body text to use for the Brand Store Creative experience.")
    brand: str = Field(..., description="The brand of the product(s) being advertised.")
    call_to_actions: "CreateBrandStoreCallToAction" = Field(..., alias="callToActions")
    click_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    creative_sizes: Optional[list["CreateSize"]] = Field(None, alias="creativeSizes", description="The placement sizes this creative should serve on.")
    disclaimers: Optional[str] = Field(None, description="The disclaimers to use for the Brand Store Creative experience.")
    headlines: list[str] = Field(..., description="The headline(s) to use for the Brand Store Creative experience.")
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    inventory_types: list["ComponentInventoryType"] = Field(..., alias="inventoryTypes", description="The inventory types this creative should serve on.")
    language: "LanguageLocale"
    logos: Optional["CreateImage"] = None
    optimization_goal_kpi: "CreativeOptimizationGoalKpi" = Field(..., alias="optimizationGoalKpi")
    responsive_sizing_behavior: "ResponsiveSizingBehavior" = Field(..., alias="responsiveSizingBehavior")
    square_images: list["CreateImage"] = Field(..., alias="squareImages", description="The square image(s) to use.")
    tall_images: list["CreateImage"] = Field(..., alias="tallImages", description="The tall image(s) to use.")
    wide_images: list["CreateImage"] = Field(..., alias="wideImages", description="The wide image(s) to use.")

    model_config = {'populate_by_name': True}


class CreateVideoLandingPage(BaseModel):
    landing_page_type: "VideoLandingPageType" = Field(..., alias="landingPageType")
    landing_page_url: Optional[str] = Field(None, alias="landingPageUrl", description="The URL of landing page where the ad directs.")

    model_config = {'populate_by_name': True}


class CreateVideo(BaseModel):
    asset_id: str = Field(..., alias="assetId", description="The asset library ID associated with the video asset.")
    asset_version: str = Field(..., alias="assetVersion", description="The asset library version associated with the video asset.")
    description: Optional[str] = Field(None, description="The description of the video content.")
    headline: Optional[str] = Field(None, description="The headline/custom text associated with the video.")

    model_config = {'populate_by_name': True}


class CreateProductVideoSettings(BaseModel):
    """An ad with a creative that includes a video."""
    brand: Optional[str] = Field(None, description="The name of the brand being advertised.")
    brand_logos: Optional[list["CreateImage"]] = Field(None, alias="brandLogos", description="The brand logo image assets to be used in the ad.")
    enable_creative_auto_translation: Optional[bool] = Field(None, alias="enableCreativeAutoTranslation", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    headlines: Optional[list[str]] = Field(None, description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you ")
    landing_page: Optional["CreateVideoLandingPage"] = Field(None, alias="landingPage")
    products: Optional[list["CreateAdvertisedProducts"]] = Field(None, description="The products featured in the video ad.")
    videos: list["CreateVideo"] = Field(..., description="The video assets used in the ad.")

    model_config = {'populate_by_name': True}


class CreateCollectionLandingPage(BaseModel):
    landing_page_type: "CollectionLandingPageType" = Field(..., alias="landingPageType")
    landing_page_url: Optional[str] = Field(None, alias="landingPageUrl", description="The URL associated to the landing page.")

    model_config = {'populate_by_name': True}


class CreateSharedCollectionSettings(BaseModel):
    """Settings shared by all collection types."""
    brand: str = Field(..., description="The name of the brand being advertised.")
    brand_logos: Optional["CreateImage"] = Field(None, alias="brandLogos")

    model_config = {'populate_by_name': True}


class CreateManualCollectionSettings(BaseModel):
    """Settings for manually curated collections."""
    landing_page: "CreateCollectionLandingPage" = Field(..., alias="landingPage")
    product_inclusions: list["CreateAdvertisedProducts"] = Field(..., alias="productInclusions", description="The products featured in the ad. Required for manual collections.")
    shared_settings: "CreateSharedCollectionSettings" = Field(..., alias="sharedSettings")

    model_config = {'populate_by_name': True}


class CreateLandingPageAsins(BaseModel):
    asins: list[str] = Field(..., description="For landing page of type ASIN_LIST, the list of ASINs used to create the landing page.")

    model_config = {'populate_by_name': True}


class CreateProductCollectionLandingPage(BaseModel):
    landing_page_asins: Optional["CreateLandingPageAsins"] = Field(None, alias="landingPageAsins")
    landing_page_type: "ProductCollectionLandingPageType" = Field(..., alias="landingPageType")
    landing_page_url: Optional[str] = Field(None, alias="landingPageUrl", description="The URL associated to the landing page. Read only if landingPageType is ASIN_LIST")

    model_config = {'populate_by_name': True}


class CreateProductCollectionSettings(BaseModel):
    """An ad creative that contains multiple products and a custom image."""
    brand: str = Field(..., description="The name of the brand being advertised.")
    brand_logos: list["CreateImage"] = Field(..., alias="brandLogos", description="The brand logo image assets to be used in the ad.")
    creative_properties_to_optimize: Optional[list["ProductCollectionCreativePropertiesToOptimize"]] = Field(None, alias="creativePropertiesToOptimize", description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.")
    custom_images: list["CreateImage"] = Field(..., alias="customImages", description="The set of custom images featured in the ad.")
    enable_creative_auto_translation: Optional[bool] = Field(None, alias="enableCreativeAutoTranslation", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    headlines: list[str] = Field(..., description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you ")
    landing_page: "CreateProductCollectionLandingPage" = Field(..., alias="landingPage")
    products: Optional[list["CreateAdvertisedProducts"]] = Field(None, description="The products featured in the ad.")

    model_config = {'populate_by_name': True}


class CreateComponentLandingPage(BaseModel):
    landing_page_type: "ComponentLandingPageType" = Field(..., alias="landingPageType")
    landing_page_url: str = Field(..., alias="landingPageUrl", description="The URL of landing page where the ad directs.")

    model_config = {'populate_by_name': True}


class CreateAssetBasedCreativeCallToActionSettings(BaseModel):
    """A CTA that directs a customer to a provided url."""
    call_to_action_type: Optional[list["AssetBasedCreativeCallToActionType"]] = Field(None, alias="callToActionType", description="Type of CallToAction for AssetBasedCreative.")
    deep_linking_behavior: Optional["DeepLinkingBehavior"] = Field(None, alias="deepLinkingBehavior")
    url: str = Field(..., description="The application url that customers are directed to.")

    model_config = {'populate_by_name': True}


class CreateAssetBasedCreativeCallToAction(BaseModel):
    pass


class CreateAssetBasedCreativeSettings(BaseModel):
    additional_html: Optional[str] = Field(None, alias="additionalHtml", description="Additional HTML to include with the render response for display inventory targets.")
    body_text: Optional[list[str]] = Field(None, alias="bodyText", description="The body text to use for the Asset Based Creative experience.")
    brand: Optional[str] = Field(None, description="The brand of the product(s) being advertised.")
    call_to_actions: Optional["CreateAssetBasedCreativeCallToAction"] = Field(None, alias="callToActions")
    click_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    creative_sizes: Optional[list["CreateSize"]] = Field(None, alias="creativeSizes", description="The placement sizes this creative should serve on.")
    custom_videos: Optional["CreateVideo"] = Field(None, alias="customVideos")
    disclaimers: Optional[str] = Field(None, description="The disclaimers to use for the Asset Based Creative experience.")
    headlines: list[str] = Field(..., description="The headline(s) to use for the Asset Based Creative experience.")
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    inventory_types: Optional[list["ComponentInventoryType"]] = Field(None, alias="inventoryTypes", description="The inventory types this creative should serve on.")
    landing_page: Optional["CreateComponentLandingPage"] = Field(None, alias="landingPage")
    language: Optional["LanguageLocale"] = None
    logos: Optional[list["CreateImage"]] = Field(None, description="The logos to use for the Asset Based Creative experience.")
    optimization_goal_kpi: Optional["CreativeOptimizationGoalKpi"] = Field(None, alias="optimizationGoalKpi")
    responsive_sizing_behavior: Optional["ResponsiveSizingBehavior"] = Field(None, alias="responsiveSizingBehavior")
    square_images: Optional[list["CreateImage"]] = Field(None, alias="squareImages", description="The square image(s) to use.")
    tall_images: Optional[list["CreateImage"]] = Field(None, alias="tallImages", description="The tall image(s) to use.")
    wide_images: Optional[list["CreateImage"]] = Field(None, alias="wideImages", description="The wide image(s) to use.")

    model_config = {'populate_by_name': True}


class CreateResponsiveEcommerceLandingPage(BaseModel):
    landing_page_type: "ResponsiveEcommerceLandingPageType" = Field(..., alias="landingPageType")
    landing_page_url: str = Field(..., alias="landingPageUrl", description="The URL of landing page where the ad directs.")

    model_config = {'populate_by_name': True}


class CreateResponsiveEcommerceSettings(BaseModel):
    click_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    creative_properties_to_optimize: Optional[list["ResponsiveEcommerceCreativePropertiesToOptimize"]] = Field(None, alias="creativePropertiesToOptimize", description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.")
    creative_sizes: Optional[list["CreateSize"]] = Field(None, alias="creativeSizes", description="The placement sizes this creative should serve on.")
    disclaimers: Optional[str] = Field(None, description="The disclaimer to use for the Responsive eCommerce experience.")
    headlines: Optional[str] = Field(None, description="The headline to use for the Responsive eCommerce experience.")
    images: Optional[list["CreateImage"]] = Field(None, description="The image(s) to use.")
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    inventory_types: Optional[list["ComponentInventoryType"]] = Field(None, alias="inventoryTypes", description="The inventory types this creative should serve on.")
    landing_page: Optional["CreateResponsiveEcommerceLandingPage"] = Field(None, alias="landingPage")
    language: Optional["LanguageLocale"] = None
    logos: Optional["CreateImage"] = None
    optimization_goal_kpi: Optional["CreativeOptimizationGoalKpi"] = Field(None, alias="optimizationGoalKpi")
    products: Optional[list["CreateAdvertisedProducts"]] = Field(None, description="The products advertised for the Responsive eCommerce experience.")
    rec_ad_variations: Optional[list["ResponsiveEcommerceAdVariations"]] = Field(None, alias="recAdVariations", description="The rendering variations selected for the Responsive eCommerce experience.")
    responsive_sizing_behavior: Optional["ResponsiveSizingBehavior"] = Field(None, alias="responsiveSizingBehavior")
    supported_third_party_sellers: Optional["SupportedThirdPartySellers"] = Field(None, alias="supportedThirdPartySellers")

    model_config = {'populate_by_name': True}


class CreateAutoCollectionSettings(BaseModel):
    """Settings for automatically generated collections."""
    product_exclusions: Optional[list["CreateAdvertisedProducts"]] = Field(None, alias="productExclusions", description="Products to exclude from auto collection.")
    shared_settings: "CreateSharedCollectionSettings" = Field(..., alias="sharedSettings")

    model_config = {'populate_by_name': True}


class CreateStoreSpotlightLandingPage(BaseModel):
    landing_page_type: "StoreSpotlightLandingPageType" = Field(..., alias="landingPageType")
    landing_page_url: str = Field(..., alias="landingPageUrl", description="The URL of landing page where the ad directs.")

    model_config = {'populate_by_name': True}


class CreateCardCreativeElement(BaseModel):
    headline: str = Field(..., description="The headline used for the card.")
    landing_page: "CreateStoreSpotlightLandingPage" = Field(..., alias="landingPage")
    products: "CreateAdvertisedProducts"

    model_config = {'populate_by_name': True}


class CreateStoreSpotlightSettings(BaseModel):
    """An ad creative that contains ASINs within a brand Store."""
    brand: str = Field(..., description="The name of the brand being advertised.")
    brand_logos: list["CreateImage"] = Field(..., alias="brandLogos", description="The brand logo image assets to be used in the ad.")
    cards: list["CreateCardCreativeElement"] = Field(..., description="The sub-elements of the creative. Each card highlights a different ASIN associated to a brand Store.")
    creative_properties_to_optimize: Optional[list["StoreSpotlightCreativePropertiesToOptimize"]] = Field(None, alias="creativePropertiesToOptimize", description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.")
    enable_creative_auto_translation: Optional[bool] = Field(None, alias="enableCreativeAutoTranslation", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    headlines: list[str] = Field(..., description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you ")
    landing_page: "CreateStoreSpotlightLandingPage" = Field(..., alias="landingPage")

    model_config = {'populate_by_name': True}


class CreateComponentCreative(BaseModel):
    asset_based_creative_settings: Optional["CreateAssetBasedCreativeSettings"] = Field(None, alias="assetBasedCreativeSettings")
    auto_collection_settings: Optional["CreateAutoCollectionSettings"] = Field(None, alias="autoCollectionSettings")
    brand_store_settings: Optional["CreateBrandStoreSettings"] = Field(None, alias="brandStoreSettings")
    manual_collection_settings: Optional["CreateManualCollectionSettings"] = Field(None, alias="manualCollectionSettings")
    product_collection_settings: Optional["CreateProductCollectionSettings"] = Field(None, alias="productCollectionSettings")
    product_video_settings: Optional["CreateProductVideoSettings"] = Field(None, alias="productVideoSettings")
    responsive_ecommerce_settings: Optional["CreateResponsiveEcommerceSettings"] = Field(None, alias="responsiveEcommerceSettings")
    store_spotlight_settings: Optional["CreateStoreSpotlightSettings"] = Field(None, alias="storeSpotlightSettings")

    model_config = {'populate_by_name': True}


class CreateLearnMoreVideoCallToActionSettings(BaseModel):
    url: str = Field(..., description="The url to drive users to learn more via the video CallToAction.")

    model_config = {'populate_by_name': True}


class CreateClickToUrlVideoCallToActionSettings(BaseModel):
    deep_linking_behavior: "DeepLinkingBehavior" = Field(..., alias="deepLinkingBehavior")
    url: str = Field(..., description="The url to redirect the user via the video CallToAction.")

    model_config = {'populate_by_name': True}


class CreateVideoCallToAction(BaseModel):
    pass


class CreateStreamingTvSettings(BaseModel):
    call_to_actions: Optional[list["CreateVideoCallToAction"]] = Field(None, alias="callToActions", description="The call to actions for this video.")
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    landing_page: Optional["CreateVideoLandingPage"] = Field(None, alias="landingPage")
    language: Optional["LanguageLocale"] = None
    products: Optional[list["CreateAdvertisedProducts"]] = Field(None, description="The product advertised on this video creative.")
    videos: "CreateVideo"

    model_config = {'populate_by_name': True}


class CreateOnlineVideoSettings(BaseModel):
    call_to_actions: Optional[list["CreateVideoCallToAction"]] = Field(None, alias="callToActions", description="The call to actions for this video.")
    click_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    language: "LanguageLocale"
    products: Optional["CreateAdvertisedProducts"] = None
    videos: "CreateVideo"

    model_config = {'populate_by_name': True}


class CreateVideoCreative(BaseModel):
    online_video_settings: Optional["CreateOnlineVideoSettings"] = Field(None, alias="onlineVideoSettings")
    streaming_tv_settings: Optional["CreateStreamingTvSettings"] = Field(None, alias="streamingTvSettings")

    model_config = {'populate_by_name': True}


class CreateSpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""
    optimize_text: bool = Field(..., alias="optimizeText", description="If the advertiser wants text they provided to be optimized by Amazon or not.")
    videos: list["CreateVideo"] = Field(..., description="The video asset(s) to use for the Sponsored Product experience.")

    model_config = {'populate_by_name': True}


class CreateProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""
    advertised_product: "CreateAdvertisedProducts" = Field(..., alias="advertisedProduct")
    headline: Optional[str] = Field(None, description="The headline/custom text associated with the ad creative.")
    spotlight_videos: Optional["CreateSpotlightVideoSettings"] = Field(None, alias="spotlightVideos")

    model_config = {'populate_by_name': True}


class CreateProductCreative(BaseModel):
    product_creative_settings: "CreateProductCreativeSettings" = Field(..., alias="productCreativeSettings")

    model_config = {'populate_by_name': True}


class CreateCreative(BaseModel):
    pass


class CreateTag(BaseModel):
    key: str = Field(..., description="A custom key value pair entered by the advertiser.")
    value: str = Field(..., description="A custom key value pair entered by the advertiser.")

    model_config = {'populate_by_name': True}


class CreateMarketplaceAdFieldOverrides(BaseModel):
    state: Optional["State"] = None
    tags: Optional[list["CreateTag"]] = Field(None, description="Open ended labels with a key value pair applied to the ad")

    model_config = {'populate_by_name': True}


class CreateMarketplaceAdConfigurations(BaseModel):
    marketplace: "Marketplace"
    overrides: "CreateMarketplaceAdFieldOverrides"

    model_config = {'populate_by_name': True}


class AdCreate(BaseModel):
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="The ad group associated with the ad.")
    ad_product: "AdProduct" = Field(..., alias="adProduct")
    ad_type: "AdType" = Field(..., alias="adType")
    creative: "CreateCreative"
    marketplace_configurations: Optional[list["CreateMarketplaceAdConfigurations"]] = Field(None, alias="marketplaceConfigurations", description="List of marketplace-specific configurations for a global ad that enables overriding certain attributes at individual mar")
    marketplace_scope: Optional["MarketplaceScope"] = Field(None, alias="marketplaceScope")
    marketplaces: Optional[list["Marketplace"]] = Field(None, description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the ")
    name: Optional[str] = Field(None, description="The name of the ad.")
    state: "CreateState"
    tags: Optional[list["CreateTag"]] = Field(None, description="Open ended labels with a key value pair applied to the ad")

    model_config = {'populate_by_name': True}


class AdExtensionType(StrEnum):
    PROMPTS = "PROMPTS"
    VIDEO = "VIDEO"


class AdExtensionStatus(StrEnum):
    OPTED_OUT = "OPTED_OUT"


class VideoType(StrEnum):
    SPOTLIGHT = "SPOTLIGHT"


class VideoExtension(BaseModel):
    """Video Ad Extension"""
    rendered_asset_id: Optional[str] = Field(None, alias="renderedAssetId", description="The video asset ID rendered in the ad.")
    rendered_cover_image_url: Optional[str] = Field(None, alias="renderedCoverImageUrl", description="The image displayed over the video player before the video is played.")
    video_type: "VideoType" = Field(..., alias="videoType")

    model_config = {'populate_by_name': True}


class PromptExtension(BaseModel):
    """Prompts Ad Extension"""
    prompt_text: str = Field(..., alias="promptText", description="The prompt text rendered in the ads")

    model_config = {'populate_by_name': True}


class AdExtensionSettings(BaseModel):
    pass


class AdExtension(BaseModel):
    ad_extension_id: str = Field(..., alias="adExtensionId", description="A unique identifier for the ad_extension.")
    ad_extension_settings: "AdExtensionSettings" = Field(..., alias="adExtensionSettings")
    ad_extension_status: Optional["AdExtensionStatus"] = Field(None, alias="adExtensionStatus")
    ad_extension_type: "AdExtensionType" = Field(..., alias="adExtensionType")
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="A unique identifier for the ad group associated with the ad_extension.")
    ad_id: Optional[str] = Field(None, alias="adId", description="A unique identifier for the ad associated with the ad_extension.")
    ad_product: "AdProduct" = Field(..., alias="adProduct")
    creation_date_time: str = Field(..., alias="creationDateTime", description="The date time the ad_extension was created.")
    last_updated_date_time: str = Field(..., alias="lastUpdatedDateTime", description="The date time the ad_extension was last updated.")
    marketplace_scope: "MarketplaceScope" = Field(..., alias="marketplaceScope")
    marketplaces: list["Marketplace"] = Field(..., description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same ")
    state: "State"
    status: Optional["Status"] = None

    model_config = {'populate_by_name': True}


class AdExtensionAdExtensionIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class AdExtensionAdExtensionStatusFilter(BaseModel):
    include: list["AdExtensionStatus"] = Field(..., description="| AdExtensionStatus | Description | | --- | --- | | `OPTED_OUT` | If the advertiser has opted out of this Ad Extension. ")

    model_config = {'populate_by_name': True}


class AdExtensionAdExtensionTypeFilter(BaseModel):
    include: list["AdExtensionType"] = Field(..., description="| AdExtensionType | Description | | --- | --- | | `PROMPTS` | Enables Prompt based Ad Extension. | | `VIDEO` | Enables V")

    model_config = {'populate_by_name': True}


class AdExtensionAdGroupIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class AdExtensionAdIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class AdExtensionAdProductFilter(BaseModel):
    include: list["AdProduct"] = Field(..., description="| AdProduct | Description | | --- | --- | | `SPONSORED_PRODUCTS` | Sponsored Products ad product. | | `SPONSORED_BRANDS`")

    model_config = {'populate_by_name': True}


class CreatePromptExtension(BaseModel):
    """Prompts Ad Extension"""
    prompt_text: str = Field(..., alias="promptText", description="The prompt text rendered in the ads")

    model_config = {'populate_by_name': True}


class CreateVideoExtension(BaseModel):
    """Video Ad Extension"""
    pass


class CreateAdExtensionSettings(BaseModel):
    pass


class AdExtensionCreate(BaseModel):
    ad_extension_settings: "CreateAdExtensionSettings" = Field(..., alias="adExtensionSettings")
    ad_extension_status: Optional["AdExtensionStatus"] = Field(None, alias="adExtensionStatus")
    ad_extension_type: "AdExtensionType" = Field(..., alias="adExtensionType")
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="A unique identifier for the ad group associated with the ad_extension.")
    ad_id: Optional[str] = Field(None, alias="adId", description="A unique identifier for the ad associated with the ad_extension.")
    ad_product: "AdProduct" = Field(..., alias="adProduct")
    marketplace_scope: "MarketplaceScope" = Field(..., alias="marketplaceScope")
    marketplaces: list["Marketplace"] = Field(..., description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same ")
    state: "CreateState"

    model_config = {'populate_by_name': True}


class AdExtensionPartialIndex(BaseModel):
    ad_extension: "AdExtension" = Field(..., alias="adExtension")
    errors: list["Error"]
    index: int

    model_config = {'populate_by_name': True}


class AdExtensionMultiStatusSuccess(BaseModel):
    ad_extension: "AdExtension" = Field(..., alias="adExtension")
    index: int

    model_config = {'populate_by_name': True}


class AdExtensionMultiStatusResponseWithPartialErrors(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    partial_success: Optional[list["AdExtensionPartialIndex"]] = Field(None, alias="partialSuccess")
    success: Optional[list["AdExtensionMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class AdExtensionStateFilter(BaseModel):
    include: list["State"] = Field(..., description="| State | Description | | --- | --- | | `ENABLED` | The object is set active by user and eligible for delivery. | | `PAU")

    model_config = {'populate_by_name': True}


class AdExtensionSuccessResponse(BaseModel):
    ad_extensions: Optional[list["AdExtension"]] = Field(None, alias="adExtensions")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class AdExtensionUpdate(BaseModel):
    ad_extension_id: str = Field(..., alias="adExtensionId", description="A unique identifier for the ad_extension.")
    marketplaces: Optional[list["Marketplace"]] = Field(None, description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same ")
    state: Optional["UpdateState"] = None

    model_config = {'populate_by_name': True}


class TacticsConvertersExclusionType(StrEnum):
    NO_EXCLUSION = "NO_EXCLUSION"
    RECENT_CONVERTERS = "RECENT_CONVERTERS"


class SiteLanguage(StrEnum):
    AR = "AR"
    BN = "BN"
    CS = "CS"
    DA = "DA"
    DE = "DE"
    EN = "EN"
    ES = "ES"
    FI = "FI"
    FR = "FR"
    GU = "GU"
    HI = "HI"
    IT = "IT"
    JA = "JA"
    KN = "KN"
    ML = "ML"
    MR = "MR"
    NL = "NL"
    NO = "NO"
    OTHER = "OTHER"
    PA = "PA"
    PL = "PL"
    PT = "PT"
    SV = "SV"
    TA = "TA"
    TE = "TE"
    TR = "TR"
    ZH = "ZH"


class TimeZoneType(StrEnum):
    ADVERTISER_REGION = "ADVERTISER_REGION"
    VIEWER = "VIEWER"


class VideoCompletionTier(StrEnum):
    ALL_TIERS = "ALL_TIERS"
    GREATER_THAN_10_PERCENT = "GREATER_THAN_10_PERCENT"
    GREATER_THAN_20_PERCENT = "GREATER_THAN_20_PERCENT"
    GREATER_THAN_30_PERCENT = "GREATER_THAN_30_PERCENT"
    GREATER_THAN_40_PERCENT = "GREATER_THAN_40_PERCENT"
    GREATER_THAN_50_PERCENT = "GREATER_THAN_50_PERCENT"
    GREATER_THAN_60_PERCENT = "GREATER_THAN_60_PERCENT"
    GREATER_THAN_70_PERCENT = "GREATER_THAN_70_PERCENT"
    GREATER_THAN_80_PERCENT = "GREATER_THAN_80_PERCENT"
    GREATER_THAN_90_PERCENT = "GREATER_THAN_90_PERCENT"


class AutomatedTargetingTactic(StrEnum):
    AWARENESS = "AWARENESS"
    CUSTOMER_ACQUISITION = "CUSTOMER_ACQUISITION"
    MAXIMIZE_PERFORMANCE = "MAXIMIZE_PERFORMANCE"
    PROSPECTING = "PROSPECTING"
    REMARKETING = "REMARKETING"
    RETENTION = "RETENTION"
    SEARCH = "SEARCH"


class ViewabilityTier(StrEnum):
    ALL_TIERS = "ALL_TIERS"
    GREATER_THAN_40_PERCENT = "GREATER_THAN_40_PERCENT"
    GREATER_THAN_50_PERCENT = "GREATER_THAN_50_PERCENT"
    GREATER_THAN_60_PERCENT = "GREATER_THAN_60_PERCENT"
    GREATER_THAN_70_PERCENT = "GREATER_THAN_70_PERCENT"
    LESS_THAN_40_PERCENT = "LESS_THAN_40_PERCENT"


class AmazonViewability(BaseModel):
    include_unmeasurable_impressions: bool = Field(..., alias="includeUnmeasurableImpressions", description="Must be false if viewabilityTier is set to ALL_TIERS. You can set to true to include impressions that can not be measure")
    viewability_tier: "ViewabilityTier" = Field(..., alias="viewabilityTier")

    model_config = {'populate_by_name': True}


class UserLocationSignal(StrEnum):
    CURRENT = "CURRENT"
    MULTIPLE_SIGNALS = "MULTIPLE_SIGNALS"


class DefaultAudienceTargetingMatchType(StrEnum):
    EXACT = "EXACT"
    SIMILAR = "SIMILAR"


class TargetingSettings(BaseModel):
    amazon_viewability: "AmazonViewability" = Field(..., alias="amazonViewability")
    automated_targeting_tactic: Optional["AutomatedTargetingTactic"] = Field(None, alias="automatedTargetingTactic")
    default_audience_targeting_match_type: Optional["DefaultAudienceTargetingMatchType"] = Field(None, alias="defaultAudienceTargetingMatchType")
    enable_language_targeting: Optional[bool] = Field(None, alias="enableLanguageTargeting", description="If set to true, creatives will only target supply where the content language matches the creative language.")
    site_language: Optional["SiteLanguage"] = Field(None, alias="siteLanguage")
    tactics_converters_exclusion_type: Optional["TacticsConvertersExclusionType"] = Field(None, alias="tacticsConvertersExclusionType")
    targeted_pg_deal_id: Optional[str] = Field(None, alias="targetedPGDealId", description="DealId to be targeted by the Ad Group being created. If you are creating an ad group targeting a programmatic guaranteed")
    time_zone_type: "TimeZoneType" = Field(..., alias="timeZoneType")
    user_location_signal: "UserLocationSignal" = Field(..., alias="userLocationSignal")
    video_completion_tier: Optional["VideoCompletionTier"] = Field(None, alias="videoCompletionTier")

    model_config = {'populate_by_name': True}


class MarketplaceAdGroupFieldOverrides(BaseModel):
    name: Optional[str] = Field(None, description="The name of the ad group for this marketplace")
    state: Optional["State"] = None
    tags: Optional[list["Tag"]] = Field(None, description="Marketplace specific tags for the ad group")

    model_config = {'populate_by_name': True}


class MarketplaceAdGroupConfigurations(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="Represents marketplace adGroup id (Ex: adGroupId-US) associated to global adGroup (Ex: adGroupId-Global)")
    marketplace: "Marketplace"
    overrides: "MarketplaceAdGroupFieldOverrides"

    model_config = {'populate_by_name': True}


class FrequencyTargetingSetting(StrEnum):
    HOUSEHOLD = "HOUSEHOLD"
    USER = "USER"


class TimeUnit(StrEnum):
    DAYS = "DAYS"
    HOURS = "HOURS"
    MINUTES = "MINUTES"


class Frequency(BaseModel):
    event_max_count: int = Field(..., alias="eventMaxCount", description="The maximum number of times an EventType is served per user. For ADSP ad group, maximum supported value is 500.")
    frequency_targeting_setting: "FrequencyTargetingSetting" = Field(..., alias="frequencyTargetingSetting")
    time_count: int = Field(..., alias="timeCount", description="The value associated with the time and unit of time for this frequency cap.")
    time_unit: "TimeUnit" = Field(..., alias="timeUnit")

    model_config = {'populate_by_name': True}


class CreativeType(StrEnum):
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class DeliveryProfile(StrEnum):
    ASAP = "ASAP"
    EVEN = "EVEN"
    PACE_AHEAD = "PACE_AHEAD"


class Pacing(BaseModel):
    delivery_profile: "DeliveryProfile" = Field(..., alias="deliveryProfile")

    model_config = {'populate_by_name': True}


class BudgetAllocation(StrEnum):
    AUTO = "AUTO"
    MANUAL = "MANUAL"


class AdGroupBudgetSettings(BaseModel):
    budget_allocation: Optional["BudgetAllocation"] = Field(None, alias="budgetAllocation")
    daily_min_spend_value: Optional[float] = Field(None, alias="dailyMinSpendValue", description="Denotes the daily minimum spend on the ad group in local currency.")

    model_config = {'populate_by_name': True}


class BidStrategy(StrEnum):
    MANUAL = "MANUAL"
    NEW_TO_BRAND = "NEW_TO_BRAND"
    PRIORITIZE_KPI_TARGET = "PRIORITIZE_KPI_TARGET"
    RULE_BASED = "RULE_BASED"
    SALES_DOWN_ONLY = "SALES_DOWN_ONLY"
    SALES_UP_AND_DOWN = "SALES_UP_AND_DOWN"
    SPEND_BUDGET_IN_FULL = "SPEND_BUDGET_IN_FULL"
    USE_CAMPAIGN_STRATEGY = "USE_CAMPAIGN_STRATEGY"


class KPI(StrEnum):
    ADD_TO_CART = "ADD_TO_CART"
    APPLICATIONS = "APPLICATIONS"
    CHECKOUTS = "CHECKOUTS"
    CLICKS = "CLICKS"
    CLICK_THROUGH_RATE = "CLICK_THROUGH_RATE"
    COMBINED_RETURN_ON_AD_SPEND = "COMBINED_RETURN_ON_AD_SPEND"
    CONTACTS = "CONTACTS"
    COST_PER_ACTION = "COST_PER_ACTION"
    COST_PER_CLICK = "COST_PER_CLICK"
    COST_PER_CONVERSION_OFF_AMAZON = "COST_PER_CONVERSION_OFF_AMAZON"
    COST_PER_DETAIL_PAGE_VIEW = "COST_PER_DETAIL_PAGE_VIEW"
    COST_PER_FIRST_APP_OPEN = "COST_PER_FIRST_APP_OPEN"
    COST_PER_INSTALL = "COST_PER_INSTALL"
    COST_PER_SIGN_UP = "COST_PER_SIGN_UP"
    COST_PER_VIDEO_COMPLETION = "COST_PER_VIDEO_COMPLETION"
    DETAIL_PAGE_VIEW_RATE = "DETAIL_PAGE_VIEW_RATE"
    FREQUENCY_AVERAGE = "FREQUENCY_AVERAGE"
    LEADS = "LEADS"
    OTHER = "OTHER"
    PAGE_VIEWS = "PAGE_VIEWS"
    PURCHASES = "PURCHASES"
    REACH = "REACH"
    RETURN_ON_AD_SPEND = "RETURN_ON_AD_SPEND"
    ROAS = "ROAS"
    ROAS_COMBINED = "ROAS_COMBINED"
    ROAS_PROMOTED = "ROAS_PROMOTED"
    SEARCH = "SEARCH"
    SIGN_UP = "SIGN_UP"
    SUBSCRIBE = "SUBSCRIBE"
    TOP_OF_SEARCH_IMPRESSION_SHARE = "TOP_OF_SEARCH_IMPRESSION_SHARE"
    TOTAL_RETURN_ON_AD_SPEND = "TOTAL_RETURN_ON_AD_SPEND"
    VIDEO_COMPLETION_RATE = "VIDEO_COMPLETION_RATE"


class AdGroupGoalSettings(BaseModel):
    kpi: Optional["KPI"] = None

    model_config = {'populate_by_name': True}


class Optimization(BaseModel):
    bid_strategy: Optional["BidStrategy"] = Field(None, alias="bidStrategy")
    budget_settings: Optional["AdGroupBudgetSettings"] = Field(None, alias="budgetSettings")
    goal_settings: Optional["AdGroupGoalSettings"] = Field(None, alias="goalSettings")

    model_config = {'populate_by_name': True}


class FeesThirdPartyProvider(StrEnum):
    COM_SCORE = "COM_SCORE"
    CPM_1 = "CPM_1"
    CPM_2 = "CPM_2"
    CPM_3 = "CPM_3"
    DOUBLE_CLICK_CAMPAIGN_MANAGER = "DOUBLE_CLICK_CAMPAIGN_MANAGER"
    DOUBLE_VERIFY = "DOUBLE_VERIFY"
    INTEGRAL_AD_SCIENCE = "INTEGRAL_AD_SCIENCE"


class FeeType(StrEnum):
    AMAZON_AUDIENCE = "AMAZON_AUDIENCE"
    AMAZON_DSP = "AMAZON_DSP"
    MANAGED_SERVICE_FEE = "MANAGED_SERVICE_FEE"
    OMNICHANNEL_METRICS = "OMNICHANNEL_METRICS"
    THIRD_PARTY_APPLIED = "THIRD_PARTY_APPLIED"
    THIRD_PARTY_AUDIENCE = "THIRD_PARTY_AUDIENCE"
    THIRD_PARTY_TARGETING = "THIRD_PARTY_TARGETING"


class CurrencyCode(StrEnum):
    AED = "AED"
    ARS = "ARS"
    AUD = "AUD"
    BGN = "BGN"
    BHD = "BHD"
    BOB = "BOB"
    BRL = "BRL"
    CAD = "CAD"
    CHF = "CHF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    CRC = "CRC"
    CZK = "CZK"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EGP = "EGP"
    EUR = "EUR"
    GBP = "GBP"
    GTQ = "GTQ"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    JMD = "JMD"
    JPY = "JPY"
    KRW = "KRW"
    KWD = "KWD"
    MAD = "MAD"
    MXN = "MXN"
    MXP = "MXP"
    MYR = "MYR"
    NGN = "NGN"
    NOK = "NOK"
    NZD = "NZD"
    PAB = "PAB"
    PEN = "PEN"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    THB = "THB"
    TND = "TND"
    TRY = "TRY"
    TWD = "TWD"
    UAH = "UAH"
    USD = "USD"
    UYU = "UYU"
    VND = "VND"
    ZAR = "ZAR"


class FeeValueType(StrEnum):
    FIXED_CPM = "FIXED_CPM"
    PERCENTAGE_OF_BUDGET = "PERCENTAGE_OF_BUDGET"
    PERCENTAGE_OF_SUPPLY_COST = "PERCENTAGE_OF_SUPPLY_COST"


class Fee(BaseModel):
    add_to_budget_spent_amount: bool = Field(..., alias="addToBudgetSpentAmount", description="Applies only to THIRD_PARTY_APPLIED_FEE. When set to true, third-party applied fees are are added on top of the total ad")
    currency_code: "CurrencyCode" = Field(..., alias="currencyCode")
    fee_type: "FeeType" = Field(..., alias="feeType")
    fee_value: float = Field(..., alias="feeValue", description="The fee amount expressed as the feeValueType. AMAZON_AUDIENCE_FEE AND THIRD_PARTY_AUDIENCE_FEE is in the currency of the")
    fee_value_type: "FeeValueType" = Field(..., alias="feeValueType")
    third_party_provider: "FeesThirdPartyProvider" = Field(..., alias="thirdPartyProvider")

    model_config = {'populate_by_name': True}


class CreativeRotationType(StrEnum):
    RANDOM = "RANDOM"
    WEIGHTED = "WEIGHTED"


class AdSettings(BaseModel):
    product_attribute_set_refinement_configuration_id: Optional[str] = Field(None, alias="productAttributeSetRefinementConfigurationId", description="Identifier for the product attribute configuration set associated with this ad group.")

    model_config = {'populate_by_name': True}


class InventoryType(StrEnum):
    AAP_MOBILE_APP = "AAP_MOBILE_APP"
    AMAZON_MOBILE_DISPLAY = "AMAZON_MOBILE_DISPLAY"
    AUDIO = "AUDIO"
    AUDIO_AMAZON_DEAL = "AUDIO_AMAZON_DEAL"
    DISPLAY = "DISPLAY"
    LIVE_EVENTS = "LIVE_EVENTS"
    ONLINE_VIDEO = "ONLINE_VIDEO"
    PODCAST = "PODCAST"
    STANDARD_DISPLAY = "STANDARD_DISPLAY"
    STREAMING_TV = "STREAMING_TV"
    STREAMING_TV_AMAZON_DEAL = "STREAMING_TV_AMAZON_DEAL"
    VIDEO = "VIDEO"


class AdGroupBidMarketplaceSetting(BaseModel):
    currency_code: "CurrencyCode" = Field(..., alias="currencyCode")
    default_bid: Optional[float] = Field(None, alias="defaultBid", description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the")
    marketplace: "Marketplace"

    model_config = {'populate_by_name': True}


class AdGroupBid(BaseModel):
    base_bid: Optional[float] = Field(None, alias="baseBid", description="The lower bound bid used for the ads in the ad group.")
    currency_code: Optional["CurrencyCode"] = Field(None, alias="currencyCode")
    default_bid: Optional[float] = Field(None, alias="defaultBid", description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the")
    marketplace_settings: Optional[list["AdGroupBidMarketplaceSetting"]] = Field(None, alias="marketplaceSettings", description="The bid associated with the ad group at specified marketplace level. Either one of bid or marketplaceSettings should alw")
    max_average_bid: Optional[float] = Field(None, alias="maxAverageBid", description="The max average bid that will be targeted on the ad group across all of the bids (a single bid could be lower or higher ")

    model_config = {'populate_by_name': True}


class Recurrence(StrEnum):
    DAILY = "DAILY"
    LIFETIME = "LIFETIME"
    MONTHLY = "MONTHLY"


class BudgetType(StrEnum):
    MONETARY = "MONETARY"


class MonetaryBudget(BaseModel):
    currency_code: "CurrencyCode" = Field(..., alias="currencyCode")
    rule_value: Optional[float] = Field(None, alias="ruleValue", description="The monetary amount of the budget when a budget rule is applied.")
    value: float = Field(..., description="The monetary amount of the budget cap in the given currency.")

    model_config = {'populate_by_name': True}


class MonetaryBudgetMarketplaceSetting(BaseModel):
    marketplace: "Marketplace"
    monetary_budget: "MonetaryBudget" = Field(..., alias="monetaryBudget")

    model_config = {'populate_by_name': True}


class MonetaryBudgetValue(BaseModel):
    marketplace_settings: Optional[list["MonetaryBudgetMarketplaceSetting"]] = Field(None, alias="marketplaceSettings", description="List of Monetary Budget values selectively applied at the given marketplace level")
    monetary_budget: Optional["MonetaryBudget"] = Field(None, alias="monetaryBudget")

    model_config = {'populate_by_name': True}


class BudgetValue(BaseModel):
    pass


class Budget(BaseModel):
    budget_type: "BudgetType" = Field(..., alias="budgetType")
    budget_value: "BudgetValue" = Field(..., alias="budgetValue")
    recurrence_time_period: "Recurrence" = Field(..., alias="recurrenceTimePeriod")

    model_config = {'populate_by_name': True}


class AdGroup(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The unique identifier of the ad group.")
    ad_product: "AdProduct" = Field(..., alias="adProduct")
    ad_settings: Optional["AdSettings"] = Field(None, alias="adSettings")
    advertised_product_category_ids: Optional[list[str]] = Field(None, alias="advertisedProductCategoryIds", description="The array of identifiers of advertised product categories associated with the ad group. For VIDEO ad group type only one")
    bid: Optional["AdGroupBid"] = None
    budgets: Optional[list["Budget"]] = Field(None, description="An object containing budget details for the ad group.")
    campaign_id: str = Field(..., alias="campaignId", description="The unique identifier of the campaign the ad group belongs to.")
    creation_date_time: str = Field(..., alias="creationDateTime", description="The date time that the ad group was created.")
    creative_rotation_type: Optional["CreativeRotationType"] = Field(None, alias="creativeRotationType")
    creative_type: Optional["CreativeType"] = Field(None, alias="creativeType")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The end date time for the ad group.")
    fees: Optional[list["Fee"]] = Field(None, description="The fees associated with the ad group.")
    frequencies: Optional[list["Frequency"]] = Field(None, description="An object containing frequency details for the ad group.")
    global_ad_group_id: Optional[str] = Field(None, alias="globalAdGroupId", description="The global adGroup identifier that manages this marketplace adGroup.")
    inventory_type: Optional["InventoryType"] = Field(None, alias="inventoryType")
    last_updated_date_time: str = Field(..., alias="lastUpdatedDateTime", description="The date time that the ad group was last updated.")
    marketplace_configurations: Optional[list["MarketplaceAdGroupConfigurations"]] = Field(None, alias="marketplaceConfigurations", description="List of marketplace-specific configurations for a global ad group that enables overriding certain attributes at individu")
    marketplace_scope: Optional["MarketplaceScope"] = Field(None, alias="marketplaceScope")
    marketplaces: Optional[list["Marketplace"]] = Field(None, description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces ")
    name: str = Field(..., description="The name of the ad group.")
    optimization: Optional["Optimization"] = None
    pacing: Optional["Pacing"] = None
    purchase_order_number: Optional[str] = Field(None, alias="purchaseOrderNumber", description="The purchase order number associated with the ad group.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The start date time for the ad group.")
    state: "State"
    status: Optional["Status"] = None
    tags: Optional[list["Tag"]] = Field(None, description="Open ended labels with a key value pair applied to the ad group")
    targeting_settings: Optional["TargetingSettings"] = Field(None, alias="targetingSettings")

    model_config = {'populate_by_name': True}


class AdGroupAdGroupIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class AdGroupAdProductFilter(BaseModel):
    include: list["AdProduct"] = Field(..., description="| AdProduct | Description | | --- | --- | | `SPONSORED_PRODUCTS` | Sponsored Products ad product. | | `SPONSORED_BRANDS`")

    model_config = {'populate_by_name': True}


class AdGroupCampaignIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class CreateAdGroupGoalSettings(BaseModel):
    kpi: Optional["KPI"] = None

    model_config = {'populate_by_name': True}


class CreateAdGroupBudgetSettings(BaseModel):
    budget_allocation: Optional["BudgetAllocation"] = Field(None, alias="budgetAllocation")
    daily_min_spend_value: Optional[float] = Field(None, alias="dailyMinSpendValue", description="Denotes the daily minimum spend on the ad group in local currency.")

    model_config = {'populate_by_name': True}


class CreateOptimization(BaseModel):
    bid_strategy: Optional["BidStrategy"] = Field(None, alias="bidStrategy")
    budget_settings: Optional["CreateAdGroupBudgetSettings"] = Field(None, alias="budgetSettings")
    goal_settings: Optional["CreateAdGroupGoalSettings"] = Field(None, alias="goalSettings")

    model_config = {'populate_by_name': True}


class CreateFrequency(BaseModel):
    event_max_count: int = Field(..., alias="eventMaxCount", description="The maximum number of times an EventType is served per user. For ADSP ad group, maximum supported value is 500.")
    frequency_targeting_setting: "FrequencyTargetingSetting" = Field(..., alias="frequencyTargetingSetting")
    time_count: int = Field(..., alias="timeCount", description="The value associated with the time and unit of time for this frequency cap.")
    time_unit: "TimeUnit" = Field(..., alias="timeUnit")

    model_config = {'populate_by_name': True}


class CreateAdGroupBidMarketplaceSetting(BaseModel):
    currency_code: "CurrencyCode" = Field(..., alias="currencyCode")
    default_bid: Optional[float] = Field(None, alias="defaultBid", description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the")
    marketplace: "Marketplace"

    model_config = {'populate_by_name': True}


class CreateAdGroupBid(BaseModel):
    base_bid: Optional[float] = Field(None, alias="baseBid", description="The lower bound bid used for the ads in the ad group.")
    default_bid: Optional[float] = Field(None, alias="defaultBid", description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the")
    marketplace_settings: Optional[list["CreateAdGroupBidMarketplaceSetting"]] = Field(None, alias="marketplaceSettings", description="The bid associated with the ad group at specified marketplace level. Either one of bid or marketplaceSettings should alw")
    max_average_bid: Optional[float] = Field(None, alias="maxAverageBid", description="The max average bid that will be targeted on the ad group across all of the bids (a single bid could be lower or higher ")

    model_config = {'populate_by_name': True}


class CreateFee(BaseModel):
    add_to_budget_spent_amount: bool = Field(..., alias="addToBudgetSpentAmount", description="Applies only to THIRD_PARTY_APPLIED_FEE. When set to true, third-party applied fees are are added on top of the total ad")
    fee_type: "FeeType" = Field(..., alias="feeType")
    fee_value: float = Field(..., alias="feeValue", description="The fee amount expressed as the feeValueType. AMAZON_AUDIENCE_FEE AND THIRD_PARTY_AUDIENCE_FEE is in the currency of the")
    third_party_provider: "FeesThirdPartyProvider" = Field(..., alias="thirdPartyProvider")

    model_config = {'populate_by_name': True}


class CreatePacing(BaseModel):
    delivery_profile: "DeliveryProfile" = Field(..., alias="deliveryProfile")

    model_config = {'populate_by_name': True}


class CreateAmazonViewability(BaseModel):
    include_unmeasurable_impressions: bool = Field(..., alias="includeUnmeasurableImpressions", description="Must be false if viewabilityTier is set to ALL_TIERS. You can set to true to include impressions that can not be measure")
    viewability_tier: "ViewabilityTier" = Field(..., alias="viewabilityTier")

    model_config = {'populate_by_name': True}


class CreateTargetingSettings(BaseModel):
    amazon_viewability: "CreateAmazonViewability" = Field(..., alias="amazonViewability")
    automated_targeting_tactic: Optional["AutomatedTargetingTactic"] = Field(None, alias="automatedTargetingTactic")
    default_audience_targeting_match_type: Optional["DefaultAudienceTargetingMatchType"] = Field(None, alias="defaultAudienceTargetingMatchType")
    enable_language_targeting: Optional[bool] = Field(None, alias="enableLanguageTargeting", description="If set to true, creatives will only target supply where the content language matches the creative language.")
    tactics_converters_exclusion_type: Optional["TacticsConvertersExclusionType"] = Field(None, alias="tacticsConvertersExclusionType")
    targeted_pg_deal_id: Optional[str] = Field(None, alias="targetedPGDealId", description="DealId to be targeted by the Ad Group being created. If you are creating an ad group targeting a programmatic guaranteed")
    time_zone_type: "TimeZoneType" = Field(..., alias="timeZoneType")
    user_location_signal: "UserLocationSignal" = Field(..., alias="userLocationSignal")
    video_completion_tier: Optional["VideoCompletionTier"] = Field(None, alias="videoCompletionTier")

    model_config = {'populate_by_name': True}


class CreateMonetaryBudget(BaseModel):
    value: float = Field(..., description="The monetary amount of the budget cap in the given currency.")

    model_config = {'populate_by_name': True}


class CreateMonetaryBudgetMarketplaceSetting(BaseModel):
    marketplace: "Marketplace"
    monetary_budget: "CreateMonetaryBudget" = Field(..., alias="monetaryBudget")

    model_config = {'populate_by_name': True}


class CreateMonetaryBudgetValue(BaseModel):
    marketplace_settings: Optional[list["CreateMonetaryBudgetMarketplaceSetting"]] = Field(None, alias="marketplaceSettings", description="List of Monetary Budget values selectively applied at the given marketplace level")
    monetary_budget: Optional["CreateMonetaryBudget"] = Field(None, alias="monetaryBudget")

    model_config = {'populate_by_name': True}


class CreateBudgetValue(BaseModel):
    pass


class CreateBudget(BaseModel):
    budget_type: "BudgetType" = Field(..., alias="budgetType")
    budget_value: "CreateBudgetValue" = Field(..., alias="budgetValue")
    recurrence_time_period: "Recurrence" = Field(..., alias="recurrenceTimePeriod")

    model_config = {'populate_by_name': True}


class CreateMarketplaceAdGroupFieldOverrides(BaseModel):
    name: Optional[str] = Field(None, description="The name of the ad group for this marketplace")
    state: Optional["State"] = None
    tags: Optional[list["CreateTag"]] = Field(None, description="Marketplace specific tags for the ad group")

    model_config = {'populate_by_name': True}


class CreateMarketplaceAdGroupConfigurations(BaseModel):
    marketplace: "Marketplace"
    overrides: "CreateMarketplaceAdGroupFieldOverrides"

    model_config = {'populate_by_name': True}


class CreateAdSettings(BaseModel):
    product_attribute_set_refinement_configuration_id: Optional[str] = Field(None, alias="productAttributeSetRefinementConfigurationId", description="Identifier for the product attribute configuration set associated with this ad group.")

    model_config = {'populate_by_name': True}


class AdGroupCreate(BaseModel):
    ad_product: "AdProduct" = Field(..., alias="adProduct")
    ad_settings: Optional["CreateAdSettings"] = Field(None, alias="adSettings")
    advertised_product_category_ids: Optional[list[str]] = Field(None, alias="advertisedProductCategoryIds", description="The array of identifiers of advertised product categories associated with the ad group. For VIDEO ad group type only one")
    bid: Optional["CreateAdGroupBid"] = None
    budgets: Optional[list["CreateBudget"]] = Field(None, description="An object containing budget details for the ad group.")
    campaign_id: str = Field(..., alias="campaignId", description="The unique identifier of the campaign the ad group belongs to.")
    creative_rotation_type: Optional["CreativeRotationType"] = Field(None, alias="creativeRotationType")
    creative_type: Optional["CreativeType"] = Field(None, alias="creativeType")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The end date time for the ad group.")
    fees: Optional[list["CreateFee"]] = Field(None, description="The fees associated with the ad group.")
    frequencies: Optional[list["CreateFrequency"]] = Field(None, description="An object containing frequency details for the ad group.")
    inventory_type: Optional["InventoryType"] = Field(None, alias="inventoryType")
    marketplace_configurations: Optional[list["CreateMarketplaceAdGroupConfigurations"]] = Field(None, alias="marketplaceConfigurations", description="List of marketplace-specific configurations for a global ad group that enables overriding certain attributes at individu")
    marketplace_scope: Optional["MarketplaceScope"] = Field(None, alias="marketplaceScope")
    marketplaces: Optional[list["Marketplace"]] = Field(None, description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces ")
    name: str = Field(..., description="The name of the ad group.")
    optimization: Optional["CreateOptimization"] = None
    pacing: Optional["CreatePacing"] = None
    purchase_order_number: Optional[str] = Field(None, alias="purchaseOrderNumber", description="The purchase order number associated with the ad group.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The start date time for the ad group.")
    state: "CreateState"
    tags: Optional[list["CreateTag"]] = Field(None, description="Open ended labels with a key value pair applied to the ad group")
    targeting_settings: Optional["CreateTargetingSettings"] = Field(None, alias="targetingSettings")

    model_config = {'populate_by_name': True}


class AdGroupMarketplaceScopeFilter(BaseModel):
    include: list["MarketplaceScope"] = Field(..., description="| MarketplaceScope | Description | | --- | --- | | `GLOBAL` |  | | `SINGLE_MARKETPLACE` |  |")

    model_config = {'populate_by_name': True}


class AdGroupMultiStatusSuccess(BaseModel):
    ad_group: "AdGroup" = Field(..., alias="adGroup")
    index: int

    model_config = {'populate_by_name': True}


class AdGroupPartialIndex(BaseModel):
    ad_group: "AdGroup" = Field(..., alias="adGroup")
    errors: list["Error"]
    index: int

    model_config = {'populate_by_name': True}


class AdGroupMultiStatusResponseWithPartialErrors(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    partial_success: Optional[list["AdGroupPartialIndex"]] = Field(None, alias="partialSuccess")
    success: Optional[list["AdGroupMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class AdGroupNameFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class AdGroupNameFilter(BaseModel):
    include: list[str]
    query_term_match_type: "AdGroupNameFilterType" = Field(..., alias="queryTermMatchType")

    model_config = {'populate_by_name': True}


class AdGroupStateFilter(BaseModel):
    include: list["State"] = Field(..., description="| State | Description | | --- | --- | | `ENABLED` | The object is set active by user and eligible for delivery. | | `PAU")

    model_config = {'populate_by_name': True}


class AdGroupSuccessResponse(BaseModel):
    ad_groups: Optional[list["AdGroup"]] = Field(None, alias="adGroups")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class UpdatePacing(BaseModel):
    delivery_profile: Optional["DeliveryProfile"] = Field(None, alias="deliveryProfile")

    model_config = {'populate_by_name': True}


class UpdateAdSettings(BaseModel):
    product_attribute_set_refinement_configuration_id: Optional[str] = Field(None, alias="productAttributeSetRefinementConfigurationId", description="Identifier for the product attribute configuration set associated with this ad group.")

    model_config = {'populate_by_name': True}


class UpdateAdGroupBudgetSettings(BaseModel):
    budget_allocation: Optional["BudgetAllocation"] = Field(None, alias="budgetAllocation")
    daily_min_spend_value: Optional[float] = Field(None, alias="dailyMinSpendValue", description="Denotes the daily minimum spend on the ad group in local currency.")

    model_config = {'populate_by_name': True}


class UpdateAdGroupGoalSettings(BaseModel):
    kpi: Optional["KPI"] = None

    model_config = {'populate_by_name': True}


class UpdateOptimization(BaseModel):
    bid_strategy: Optional["BidStrategy"] = Field(None, alias="bidStrategy")
    budget_settings: Optional["UpdateAdGroupBudgetSettings"] = Field(None, alias="budgetSettings")
    goal_settings: Optional["UpdateAdGroupGoalSettings"] = Field(None, alias="goalSettings")

    model_config = {'populate_by_name': True}


class UpdateAdGroupBid(BaseModel):
    base_bid: Optional[float] = Field(None, alias="baseBid", description="The lower bound bid used for the ads in the ad group.")
    default_bid: Optional[float] = Field(None, alias="defaultBid", description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the")
    marketplace_settings: Optional[list["CreateAdGroupBidMarketplaceSetting"]] = Field(None, alias="marketplaceSettings", description="The bid associated with the ad group at specified marketplace level. Either one of bid or marketplaceSettings should alw")
    max_average_bid: Optional[float] = Field(None, alias="maxAverageBid", description="The max average bid that will be targeted on the ad group across all of the bids (a single bid could be lower or higher ")

    model_config = {'populate_by_name': True}


class UpdateAmazonViewability(BaseModel):
    include_unmeasurable_impressions: Optional[bool] = Field(None, alias="includeUnmeasurableImpressions", description="Must be false if viewabilityTier is set to ALL_TIERS. You can set to true to include impressions that can not be measure")
    viewability_tier: Optional["ViewabilityTier"] = Field(None, alias="viewabilityTier")

    model_config = {'populate_by_name': True}


class UpdateTargetingSettings(BaseModel):
    amazon_viewability: Optional["UpdateAmazonViewability"] = Field(None, alias="amazonViewability")
    default_audience_targeting_match_type: Optional["DefaultAudienceTargetingMatchType"] = Field(None, alias="defaultAudienceTargetingMatchType")
    enable_language_targeting: Optional[bool] = Field(None, alias="enableLanguageTargeting", description="If set to true, creatives will only target supply where the content language matches the creative language.")
    tactics_converters_exclusion_type: Optional["TacticsConvertersExclusionType"] = Field(None, alias="tacticsConvertersExclusionType")
    targeted_pg_deal_id: Optional[str] = Field(None, alias="targetedPGDealId", description="DealId to be targeted by the Ad Group being created. If you are creating an ad group targeting a programmatic guaranteed")
    time_zone_type: Optional["TimeZoneType"] = Field(None, alias="timeZoneType")
    user_location_signal: Optional["UserLocationSignal"] = Field(None, alias="userLocationSignal")
    video_completion_tier: Optional["VideoCompletionTier"] = Field(None, alias="videoCompletionTier")

    model_config = {'populate_by_name': True}


class AdGroupUpdate(BaseModel):
    ad_group_id: str = Field(..., alias="adGroupId", description="The unique identifier of the ad group.")
    ad_product: Optional["AdProduct"] = Field(None, alias="adProduct")
    ad_settings: Optional["UpdateAdSettings"] = Field(None, alias="adSettings")
    advertised_product_category_ids: Optional[list[str]] = Field(None, alias="advertisedProductCategoryIds", description="The array of identifiers of advertised product categories associated with the ad group. For VIDEO ad group type only one")
    bid: Optional["UpdateAdGroupBid"] = None
    budgets: Optional[list["CreateBudget"]] = Field(None, description="An object containing budget details for the ad group.")
    creative_rotation_type: Optional["CreativeRotationType"] = Field(None, alias="creativeRotationType")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The end date time for the ad group.")
    fees: Optional[list["CreateFee"]] = Field(None, description="The fees associated with the ad group.")
    frequencies: Optional[list["CreateFrequency"]] = Field(None, description="An object containing frequency details for the ad group.")
    marketplace_configurations: Optional[list["CreateMarketplaceAdGroupConfigurations"]] = Field(None, alias="marketplaceConfigurations", description="List of marketplace-specific configurations for a global ad group that enables overriding certain attributes at individu")
    marketplace_scope: Optional["MarketplaceScope"] = Field(None, alias="marketplaceScope")
    marketplaces: Optional[list["Marketplace"]] = Field(None, description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces ")
    name: Optional[str] = Field(None, description="The name of the ad group.")
    optimization: Optional["UpdateOptimization"] = None
    pacing: Optional["UpdatePacing"] = None
    purchase_order_number: Optional[str] = Field(None, alias="purchaseOrderNumber", description="The purchase order number associated with the ad group.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The start date time for the ad group.")
    state: Optional["UpdateState"] = None
    tags: Optional[list["CreateTag"]] = Field(None, description="Open ended labels with a key value pair applied to the ad group")
    targeting_settings: Optional["UpdateTargetingSettings"] = Field(None, alias="targetingSettings")

    model_config = {'populate_by_name': True}


class VideoInitiationType(StrEnum):
    AUTOPLAY = "AUTOPLAY"
    UNKNOWN = "UNKNOWN"
    USER_INITIATED = "USER_INITIATED"


class AdInitiationTarget(BaseModel):
    """Target based on how the video ad will be started."""
    video_initiation_type: "VideoInitiationType" = Field(..., alias="videoInitiationType")

    model_config = {'populate_by_name': True}


class AdMarketplaceScopeFilter(BaseModel):
    include: list["MarketplaceScope"] = Field(..., description="| MarketplaceScope | Description | | --- | --- | | `GLOBAL` |  | | `SINGLE_MARKETPLACE` |  |")

    model_config = {'populate_by_name': True}


class AdPartialIndex(BaseModel):
    ad: "Ad"
    errors: list["Error"]
    index: int

    model_config = {'populate_by_name': True}


class AdMultiStatusSuccess(BaseModel):
    ad: "Ad"
    index: int

    model_config = {'populate_by_name': True}


class AdMultiStatusResponseWithPartialErrors(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    partial_success: Optional[list["AdPartialIndex"]] = Field(None, alias="partialSuccess")
    success: Optional[list["AdMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class AdNameFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class AdNameFilter(BaseModel):
    include: list[str]
    query_term_match_type: "AdNameFilterType" = Field(..., alias="queryTermMatchType")

    model_config = {'populate_by_name': True}


class AdPlayerSize(StrEnum):
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    SMALL = "SMALL"
    UNKNOWN = "UNKNOWN"


class AdPlayerSizeTarget(BaseModel):
    """Target based on the size of the ad player."""
    ad_player_size: "AdPlayerSize" = Field(..., alias="adPlayerSize")

    model_config = {'populate_by_name': True}


class AdStateFilter(BaseModel):
    include: list["State"] = Field(..., description="| State | Description | | --- | --- | | `ENABLED` | The object is set active by user and eligible for delivery. | | `PAU")

    model_config = {'populate_by_name': True}


class AdSuccessResponse(BaseModel):
    ads: Optional[list["Ad"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class UpdateGlobalStoreSettings(BaseModel):
    catalog_source_marketplace: Optional["Marketplace"] = Field(None, alias="catalogSourceMarketplace")

    model_config = {'populate_by_name': True}


class UpdateAdvertisedProducts(BaseModel):
    global_store_setting: Optional["UpdateGlobalStoreSettings"] = Field(None, alias="globalStoreSetting")
    marketplace_settings: Optional[list["CreateAdvertisedProductMarketplaceSetting"]] = Field(None, alias="marketplaceSettings", description="List of advertised product selectively applied at the given marketplace level")
    product_id: Optional[str] = Field(None, alias="productId", description="The identifier of the advertised product.")
    product_id_type: Optional["ProductIdType"] = Field(None, alias="productIdType")

    model_config = {'populate_by_name': True}


class UpdateSpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""
    optimize_text: Optional[bool] = Field(None, alias="optimizeText", description="If the advertiser wants text they provided to be optimized by Amazon or not.")
    videos: Optional[list["CreateVideo"]] = Field(None, description="The video asset(s) to use for the Sponsored Product experience.")

    model_config = {'populate_by_name': True}


class UpdateProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""
    advertised_product: Optional["UpdateAdvertisedProducts"] = Field(None, alias="advertisedProduct")
    spotlight_videos: Optional["UpdateSpotlightVideoSettings"] = Field(None, alias="spotlightVideos")

    model_config = {'populate_by_name': True}


class UpdateProductCreative(BaseModel):
    product_creative_settings: Optional["UpdateProductCreativeSettings"] = Field(None, alias="productCreativeSettings")

    model_config = {'populate_by_name': True}


class UpdateThirdPartyVideoSettings(BaseModel):
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    language: Optional["LanguageLocale"] = None
    vast_url: Optional[str] = Field(None, alias="vastUrl", description="The url to use to fetch the VAST XML for this video creative. Required for non publisher hosted creatives (when publishe")

    model_config = {'populate_by_name': True}


class UpdateThirdPartyDisplaySettings(BaseModel):
    ad_choices_position: Optional["AdChoicesPosition"] = Field(None, alias="adChoicesPosition")
    additional_html: Optional[str] = Field(None, alias="additionalHtml", description="Additional html to be included along with the creative when rendered.")
    click_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    creative_sizes: Optional[list["CreateSize"]] = Field(None, alias="creativeSizes", description="The list of placement sizes this creative should serve on. Required for non publisher hosted creatives (when publisherHo")
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    language: Optional["LanguageLocale"] = None
    third_party_tag_hosting_source: Optional[str] = Field(None, alias="thirdPartyTagHostingSource", description="The html tag to use to fetch this creative from the 3p ad server. Required for non publisher hosted creatives (when publ")

    model_config = {'populate_by_name': True}


class UpdateThirdPartyCreative(BaseModel):
    third_party_display_settings: Optional["UpdateThirdPartyDisplaySettings"] = Field(None, alias="thirdPartyDisplaySettings")
    third_party_video_settings: Optional["UpdateThirdPartyVideoSettings"] = Field(None, alias="thirdPartyVideoSettings")

    model_config = {'populate_by_name': True}


class UpdateVideo(BaseModel):
    asset_id: Optional[str] = Field(None, alias="assetId", description="The asset library ID associated with the video asset.")
    asset_version: Optional[str] = Field(None, alias="assetVersion", description="The asset library version associated with the video asset.")
    description: Optional[str] = Field(None, description="The description of the video content.")
    headline: Optional[str] = Field(None, description="The headline/custom text associated with the video.")

    model_config = {'populate_by_name': True}


class UpdateOnlineVideoSettings(BaseModel):
    call_to_actions: Optional[list["CreateVideoCallToAction"]] = Field(None, alias="callToActions", description="The call to actions for this video.")
    click_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    language: Optional["LanguageLocale"] = None
    products: Optional["UpdateAdvertisedProducts"] = None
    videos: Optional["UpdateVideo"] = None

    model_config = {'populate_by_name': True}


class UpdateStreamingTvSettings(BaseModel):
    call_to_actions: Optional[list["CreateVideoCallToAction"]] = Field(None, alias="callToActions", description="The call to actions for this video.")
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    language: Optional["LanguageLocale"] = None
    products: Optional[list["CreateAdvertisedProducts"]] = Field(None, description="The product advertised on this video creative.")
    videos: Optional["UpdateVideo"] = None

    model_config = {'populate_by_name': True}


class UpdateVideoCreative(BaseModel):
    online_video_settings: Optional["UpdateOnlineVideoSettings"] = Field(None, alias="onlineVideoSettings")
    streaming_tv_settings: Optional["UpdateStreamingTvSettings"] = Field(None, alias="streamingTvSettings")

    model_config = {'populate_by_name': True}


class UpdateAudio(BaseModel):
    asset_id: Optional[str] = Field(None, alias="assetId", description="The asset library ID associated with the audio asset.")
    asset_version: Optional[str] = Field(None, alias="assetVersion", description="The asset library version associated with the audio asset.")

    model_config = {'populate_by_name': True}


class UpdateStandardAudioExperienceSettings(BaseModel):
    audio: Optional["UpdateAudio"] = None
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded. Urls cannot exceed 2048 characters.")
    language: Optional["LanguageLocale"] = None
    products: Optional[list["CreateAdvertisedProducts"]] = Field(None, description="The product(s) being advertised.")

    model_config = {'populate_by_name': True}


class UpdateAudioCreative(BaseModel):
    """| UpdateAudioCreative | Description | | --- | --- | | `standardAudioSettings` | The standard audio experience settings. See the Audio Spec for more info: https://advertising.amazon.com/en-us/resources"""
    pass


class UpdateLandingPageAsins(BaseModel):
    asins: Optional[list[str]] = Field(None, description="For landing page of type ASIN_LIST, the list of ASINs used to create the landing page.")

    model_config = {'populate_by_name': True}


class UpdateProductCollectionLandingPage(BaseModel):
    landing_page_asins: Optional["UpdateLandingPageAsins"] = Field(None, alias="landingPageAsins")
    landing_page_type: Optional["ProductCollectionLandingPageType"] = Field(None, alias="landingPageType")
    landing_page_url: Optional[str] = Field(None, alias="landingPageUrl", description="The URL associated to the landing page. Read only if landingPageType is ASIN_LIST")

    model_config = {'populate_by_name': True}


class UpdateProductCollectionSettings(BaseModel):
    """An ad creative that contains multiple products and a custom image."""
    brand: Optional[str] = Field(None, description="The name of the brand being advertised.")
    brand_logos: Optional[list["CreateImage"]] = Field(None, alias="brandLogos", description="The brand logo image assets to be used in the ad.")
    creative_properties_to_optimize: Optional[list["ProductCollectionCreativePropertiesToOptimize"]] = Field(None, alias="creativePropertiesToOptimize", description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.")
    custom_images: Optional[list["CreateImage"]] = Field(None, alias="customImages", description="The set of custom images featured in the ad.")
    enable_creative_auto_translation: Optional[bool] = Field(None, alias="enableCreativeAutoTranslation", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    headlines: Optional[list[str]] = Field(None, description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you ")
    landing_page: Optional["UpdateProductCollectionLandingPage"] = Field(None, alias="landingPage")
    products: Optional[list["CreateAdvertisedProducts"]] = Field(None, description="The products featured in the ad.")

    model_config = {'populate_by_name': True}


class UpdateAssetBasedCreativeCallToActionSettings(BaseModel):
    """A CTA that directs a customer to a provided url."""
    call_to_action_type: Optional[list["AssetBasedCreativeCallToActionType"]] = Field(None, alias="callToActionType", description="Type of CallToAction for AssetBasedCreative.")
    deep_linking_behavior: Optional["DeepLinkingBehavior"] = Field(None, alias="deepLinkingBehavior")
    url: Optional[str] = Field(None, description="The application url that customers are directed to.")

    model_config = {'populate_by_name': True}


class UpdateAssetBasedCreativeCallToAction(BaseModel):
    pass


class UpdateAssetBasedCreativeSettings(BaseModel):
    additional_html: Optional[str] = Field(None, alias="additionalHtml", description="Additional HTML to include with the render response for display inventory targets.")
    body_text: Optional[list[str]] = Field(None, alias="bodyText", description="The body text to use for the Asset Based Creative experience.")
    brand: Optional[str] = Field(None, description="The brand of the product(s) being advertised.")
    call_to_actions: Optional["UpdateAssetBasedCreativeCallToAction"] = Field(None, alias="callToActions")
    click_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    creative_sizes: Optional[list["CreateSize"]] = Field(None, alias="creativeSizes", description="The placement sizes this creative should serve on.")
    custom_videos: Optional["UpdateVideo"] = Field(None, alias="customVideos")
    disclaimers: Optional[str] = Field(None, description="The disclaimers to use for the Asset Based Creative experience.")
    headlines: Optional[list[str]] = Field(None, description="The headline(s) to use for the Asset Based Creative experience.")
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    inventory_types: Optional[list["ComponentInventoryType"]] = Field(None, alias="inventoryTypes", description="The inventory types this creative should serve on.")
    language: Optional["LanguageLocale"] = None
    logos: Optional[list["CreateImage"]] = Field(None, description="The logos to use for the Asset Based Creative experience.")
    optimization_goal_kpi: Optional["CreativeOptimizationGoalKpi"] = Field(None, alias="optimizationGoalKpi")
    responsive_sizing_behavior: Optional["ResponsiveSizingBehavior"] = Field(None, alias="responsiveSizingBehavior")
    square_images: Optional[list["CreateImage"]] = Field(None, alias="squareImages", description="The square image(s) to use.")
    tall_images: Optional[list["CreateImage"]] = Field(None, alias="tallImages", description="The tall image(s) to use.")
    wide_images: Optional[list["CreateImage"]] = Field(None, alias="wideImages", description="The wide image(s) to use.")

    model_config = {'populate_by_name': True}


class UpdateImage(BaseModel):
    asset_id: Optional[str] = Field(None, alias="assetId", description="The asset library ID associated with the image asset.")
    asset_version: Optional[str] = Field(None, alias="assetVersion", description="The asset library version associated with the image asset.")
    format_properties: Optional[list["CreateFormatProperties"]] = Field(None, alias="formatProperties", description="The cropping and positioning properties associated with the asset.")

    model_config = {'populate_by_name': True}


class UpdateSharedCollectionSettings(BaseModel):
    """Settings shared by all collection types."""
    brand: Optional[str] = Field(None, description="The name of the brand being advertised.")
    brand_logos: Optional["UpdateImage"] = Field(None, alias="brandLogos")

    model_config = {'populate_by_name': True}


class UpdateAutoCollectionSettings(BaseModel):
    """Settings for automatically generated collections."""
    product_exclusions: Optional[list["CreateAdvertisedProducts"]] = Field(None, alias="productExclusions", description="Products to exclude from auto collection.")
    shared_settings: Optional["UpdateSharedCollectionSettings"] = Field(None, alias="sharedSettings")

    model_config = {'populate_by_name': True}


class UpdateCollectionLandingPage(BaseModel):
    landing_page_type: Optional["CollectionLandingPageType"] = Field(None, alias="landingPageType")
    landing_page_url: Optional[str] = Field(None, alias="landingPageUrl", description="The URL associated to the landing page.")

    model_config = {'populate_by_name': True}


class UpdateManualCollectionSettings(BaseModel):
    """Settings for manually curated collections."""
    landing_page: Optional["UpdateCollectionLandingPage"] = Field(None, alias="landingPage")
    product_inclusions: Optional[list["CreateAdvertisedProducts"]] = Field(None, alias="productInclusions", description="The products featured in the ad. Required for manual collections.")
    shared_settings: Optional["UpdateSharedCollectionSettings"] = Field(None, alias="sharedSettings")

    model_config = {'populate_by_name': True}


class UpdateVideoLandingPage(BaseModel):
    landing_page_type: Optional["VideoLandingPageType"] = Field(None, alias="landingPageType")
    landing_page_url: Optional[str] = Field(None, alias="landingPageUrl", description="The URL of landing page where the ad directs.")

    model_config = {'populate_by_name': True}


class UpdateProductVideoSettings(BaseModel):
    """An ad with a creative that includes a video."""
    brand: Optional[str] = Field(None, description="The name of the brand being advertised.")
    brand_logos: Optional[list["CreateImage"]] = Field(None, alias="brandLogos", description="The brand logo image assets to be used in the ad.")
    enable_creative_auto_translation: Optional[bool] = Field(None, alias="enableCreativeAutoTranslation", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    headlines: Optional[list[str]] = Field(None, description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you ")
    landing_page: Optional["UpdateVideoLandingPage"] = Field(None, alias="landingPage")
    products: Optional[list["CreateAdvertisedProducts"]] = Field(None, description="The products featured in the video ad.")
    videos: Optional[list["CreateVideo"]] = Field(None, description="The video assets used in the ad.")

    model_config = {'populate_by_name': True}


class UpdateBrandStoreCallToActionSettings(BaseModel):
    """A CTA that directs a customer to a provided url."""
    call_to_action_type: Optional[list["BrandStoreCallToActionType"]] = Field(None, alias="callToActionType", description="Type of CallToAction for BrandStore.")
    deep_linking_behavior: Optional["DeepLinkingBehavior"] = Field(None, alias="deepLinkingBehavior")
    url: Optional[str] = Field(None, description="The application url that customers are directed to.")

    model_config = {'populate_by_name': True}


class UpdateBrandStoreCallToAction(BaseModel):
    pass


class UpdateBrandStoreSettings(BaseModel):
    additional_html: Optional[str] = Field(None, alias="additionalHtml", description="Additional HTML to include with the render response for display inventory targets.")
    body_text: Optional[list[str]] = Field(None, alias="bodyText", description="The body text to use for the Brand Store Creative experience.")
    brand: Optional[str] = Field(None, description="The brand of the product(s) being advertised.")
    call_to_actions: Optional["UpdateBrandStoreCallToAction"] = Field(None, alias="callToActions")
    click_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    creative_sizes: Optional[list["CreateSize"]] = Field(None, alias="creativeSizes", description="The placement sizes this creative should serve on.")
    disclaimers: Optional[str] = Field(None, description="The disclaimers to use for the Brand Store Creative experience.")
    headlines: Optional[list[str]] = Field(None, description="The headline(s) to use for the Brand Store Creative experience.")
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    inventory_types: Optional[list["ComponentInventoryType"]] = Field(None, alias="inventoryTypes", description="The inventory types this creative should serve on.")
    language: Optional["LanguageLocale"] = None
    logos: Optional["UpdateImage"] = None
    optimization_goal_kpi: Optional["CreativeOptimizationGoalKpi"] = Field(None, alias="optimizationGoalKpi")
    responsive_sizing_behavior: Optional["ResponsiveSizingBehavior"] = Field(None, alias="responsiveSizingBehavior")
    square_images: Optional[list["CreateImage"]] = Field(None, alias="squareImages", description="The square image(s) to use.")
    tall_images: Optional[list["CreateImage"]] = Field(None, alias="tallImages", description="The tall image(s) to use.")
    wide_images: Optional[list["CreateImage"]] = Field(None, alias="wideImages", description="The wide image(s) to use.")

    model_config = {'populate_by_name': True}


class UpdateStoreSpotlightLandingPage(BaseModel):
    landing_page_type: Optional["StoreSpotlightLandingPageType"] = Field(None, alias="landingPageType")
    landing_page_url: Optional[str] = Field(None, alias="landingPageUrl", description="The URL of landing page where the ad directs.")

    model_config = {'populate_by_name': True}


class UpdateStoreSpotlightSettings(BaseModel):
    """An ad creative that contains ASINs within a brand Store."""
    brand: Optional[str] = Field(None, description="The name of the brand being advertised.")
    brand_logos: Optional[list["CreateImage"]] = Field(None, alias="brandLogos", description="The brand logo image assets to be used in the ad.")
    cards: Optional[list["CreateCardCreativeElement"]] = Field(None, description="The sub-elements of the creative. Each card highlights a different ASIN associated to a brand Store.")
    creative_properties_to_optimize: Optional[list["StoreSpotlightCreativePropertiesToOptimize"]] = Field(None, alias="creativePropertiesToOptimize", description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.")
    enable_creative_auto_translation: Optional[bool] = Field(None, alias="enableCreativeAutoTranslation", description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to trans")
    headlines: Optional[list[str]] = Field(None, description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you ")
    landing_page: Optional["UpdateStoreSpotlightLandingPage"] = Field(None, alias="landingPage")

    model_config = {'populate_by_name': True}


class UpdateResponsiveEcommerceSettings(BaseModel):
    click_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    creative_properties_to_optimize: Optional[list["ResponsiveEcommerceCreativePropertiesToOptimize"]] = Field(None, alias="creativePropertiesToOptimize", description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.")
    creative_sizes: Optional[list["CreateSize"]] = Field(None, alias="creativeSizes", description="The placement sizes this creative should serve on.")
    disclaimers: Optional[str] = Field(None, description="The disclaimer to use for the Responsive eCommerce experience.")
    headlines: Optional[str] = Field(None, description="The headline to use for the Responsive eCommerce experience.")
    images: Optional[list["CreateImage"]] = Field(None, description="The image(s) to use.")
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    inventory_types: Optional[list["ComponentInventoryType"]] = Field(None, alias="inventoryTypes", description="The inventory types this creative should serve on.")
    language: Optional["LanguageLocale"] = None
    logos: Optional["UpdateImage"] = None
    optimization_goal_kpi: Optional["CreativeOptimizationGoalKpi"] = Field(None, alias="optimizationGoalKpi")
    products: Optional[list["CreateAdvertisedProducts"]] = Field(None, description="The products advertised for the Responsive eCommerce experience.")
    rec_ad_variations: Optional[list["ResponsiveEcommerceAdVariations"]] = Field(None, alias="recAdVariations", description="The rendering variations selected for the Responsive eCommerce experience.")
    responsive_sizing_behavior: Optional["ResponsiveSizingBehavior"] = Field(None, alias="responsiveSizingBehavior")
    supported_third_party_sellers: Optional["SupportedThirdPartySellers"] = Field(None, alias="supportedThirdPartySellers")

    model_config = {'populate_by_name': True}


class UpdateComponentCreative(BaseModel):
    asset_based_creative_settings: Optional["UpdateAssetBasedCreativeSettings"] = Field(None, alias="assetBasedCreativeSettings")
    auto_collection_settings: Optional["UpdateAutoCollectionSettings"] = Field(None, alias="autoCollectionSettings")
    brand_store_settings: Optional["UpdateBrandStoreSettings"] = Field(None, alias="brandStoreSettings")
    manual_collection_settings: Optional["UpdateManualCollectionSettings"] = Field(None, alias="manualCollectionSettings")
    product_collection_settings: Optional["UpdateProductCollectionSettings"] = Field(None, alias="productCollectionSettings")
    product_video_settings: Optional["UpdateProductVideoSettings"] = Field(None, alias="productVideoSettings")
    responsive_ecommerce_settings: Optional["UpdateResponsiveEcommerceSettings"] = Field(None, alias="responsiveEcommerceSettings")
    store_spotlight_settings: Optional["UpdateStoreSpotlightSettings"] = Field(None, alias="storeSpotlightSettings")

    model_config = {'populate_by_name': True}


class UpdateClickToUrlDisplayCallToActionSettings(BaseModel):
    """A CTA that directs a customer to a provided url."""
    deep_linking_behavior: Optional["DeepLinkingBehavior"] = Field(None, alias="deepLinkingBehavior")
    url: Optional[str] = Field(None, description="The application url that customers are directed to.")

    model_config = {'populate_by_name': True}


class UpdateClickToAppDisplayCallToActionSettings(BaseModel):
    """A CTA that directs a customer to a provided url."""
    deep_linking_behavior: Optional["DeepLinkingBehavior"] = Field(None, alias="deepLinkingBehavior")
    url: Optional[str] = Field(None, description="The app that customers are directed to.")

    model_config = {'populate_by_name': True}


class UpdateDisplayCallToAction(BaseModel):
    pass


class UpdateStandardDisplaySettings(BaseModel):
    ad_choices_position: Optional["AdChoicesPosition"] = Field(None, alias="adChoicesPosition")
    call_to_action: Optional["UpdateDisplayCallToAction"] = Field(None, alias="callToAction")
    click_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="clickTrackingUrls", description="The third party urls to trigger when an click is recorded.")
    creative_sizes: Optional[list["CreateSize"]] = Field(None, alias="creativeSizes", description="The list of placement sizes this creative should serve on.")
    custom_images: Optional[list["CreateImage"]] = Field(None, alias="customImages", description="The custom images to use for the standard display experience.")
    impression_tracking_urls: Optional[list["CreateCreativeTrackingUrl"]] = Field(None, alias="impressionTrackingUrls", description="The third party urls to trigger when an impression is recorded.")
    language: Optional["LanguageLocale"] = None

    model_config = {'populate_by_name': True}


class UpdateDisplayCreative(BaseModel):
    standard_display_settings: Optional["UpdateStandardDisplaySettings"] = Field(None, alias="standardDisplaySettings")

    model_config = {'populate_by_name': True}


class UpdateCreative(BaseModel):
    pass


class AdUpdate(BaseModel):
    ad_id: str = Field(..., alias="adId", description="The identifier of the ad.")
    creative: Optional["UpdateCreative"] = None
    marketplace_configurations: Optional[list["CreateMarketplaceAdConfigurations"]] = Field(None, alias="marketplaceConfigurations", description="List of marketplace-specific configurations for a global ad that enables overriding certain attributes at individual mar")
    marketplace_scope: Optional["MarketplaceScope"] = Field(None, alias="marketplaceScope")
    marketplaces: Optional[list["Marketplace"]] = Field(None, description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the ")
    name: Optional[str] = Field(None, description="The name of the ad.")
    state: Optional["UpdateState"] = None
    tags: Optional[list["CreateTag"]] = Field(None, description="Open ended labels with a key value pair applied to the ad")

    model_config = {'populate_by_name': True}


class AdvertiserDomainList(BaseModel):
    """Targets domains based on list inherited from the advertiser."""
    inherit_from_advertiser: bool = Field(..., alias="inheritFromAdvertiser", description="Set to TRUE to inherit domain list from advertiser.")

    model_config = {'populate_by_name': True}


class AppType(StrEnum):
    MOBILE = "MOBILE"
    STREAMING_TV = "STREAMING_TV"


class AppTarget(BaseModel):
    """Target based on user application."""
    app_id: str = Field(..., alias="appId", description="The app identifier being targeted.")
    app_type: "AppType" = Field(..., alias="appType")

    model_config = {'populate_by_name': True}


class AudienceBidAdjustment(BaseModel):
    audience_id: str = Field(..., alias="audienceId", description="The unique identifier of the Audience to apply bid adjustment.")
    percentage: int = Field(..., description="The selection of the percentage change associated with a given audience and bid adjustment settings.")

    model_config = {'populate_by_name': True}


class InGroupOperator(StrEnum):
    ALL = "ALL"
    ANY = "ANY"


class MarketplaceStringValue(BaseModel):
    default_value: Optional[str] = Field(None, alias="defaultValue", description="The default value. Either the default value or the marketplace settings should always be specified")

    model_config = {'populate_by_name': True}


class AudienceTarget(BaseModel):
    """Target based on a specified audience ID."""
    across_group_operator: Optional["AcrossGroupOperator"] = Field(None, alias="acrossGroupOperator")
    audience_id: "MarketplaceStringValue" = Field(..., alias="audienceId")
    group_id: Optional[str] = Field(None, alias="groupId", description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences")
    in_group_operator: Optional["InGroupOperator"] = Field(None, alias="inGroupOperator")

    model_config = {'populate_by_name': True}


class AutoCreationSettings(BaseModel):
    auto_create_targets: Optional[bool] = Field(None, alias="autoCreateTargets", description="Gives Amazon permission to automatically create targets associated with the campaign based on the products being adverti")
    auto_manage_campaign: Optional[bool] = Field(None, alias="autoManageCampaign", description="Flag that allows Amazon to manage the lifecycle of your Campaign.")

    model_config = {'populate_by_name': True}


class AutoScaleGlobalCampaignSetting(StrEnum):
    AUTO = "AUTO"
    MANUAL = "MANUAL"


class AverageCompletionAndFullyViewableRateTargetingType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_10 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_10"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_20 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_20"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_25 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_25"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_30 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_30"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_35 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_35"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_40 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_40"


class BadGatewayResponseContent(BaseModel):
    code: str
    message: str

    model_config = {'populate_by_name': True}


class BadRequestResponseContent(BaseModel):
    code: "ErrorCode"
    message: str

    model_config = {'populate_by_name': True}


class CreativeBidAdjustmentType(StrEnum):
    SPOTLIGHT = "SPOTLIGHT"


class CreativeBidAdjustment(BaseModel):
    creative_type: Optional["CreativeBidAdjustmentType"] = Field(None, alias="creativeType")
    percentage: int = Field(..., description="The selection of the percentage change associated with the creative type and bid adjustment settings.")

    model_config = {'populate_by_name': True}


class Placement(StrEnum):
    HOME_PAGE = "HOME_PAGE"
    PRODUCT_PAGE = "PRODUCT_PAGE"
    REST_OF_SEARCH = "REST_OF_SEARCH"
    SITE_AMAZON_BUSINESS = "SITE_AMAZON_BUSINESS"
    TOP_OF_SEARCH = "TOP_OF_SEARCH"


class PlacementBidAdjustment(BaseModel):
    percentage: int = Field(..., description="The selection of the percentage change associated with a given placement and bid adjustment settings.")
    placement: "Placement"

    model_config = {'populate_by_name': True}


class ShopperSegment(StrEnum):
    NEW_TO_BRAND = "NEW_TO_BRAND"


class ShopperSegmentBidAdjustment(BaseModel):
    percentage: int = Field(..., description="The selection of the percentage change associated with a given shopper segment and bid adjustment settings.")
    shopper_segment: "ShopperSegment" = Field(..., alias="shopperSegment")

    model_config = {'populate_by_name': True}


class BidAdjustments(BaseModel):
    audience_bid_adjustments: Optional[list["AudienceBidAdjustment"]] = Field(None, alias="audienceBidAdjustments", description="Bid Adjustments based on the audiences")
    creative_bid_adjustments: Optional[list["CreativeBidAdjustment"]] = Field(None, alias="creativeBidAdjustments", description="Bid Adjustments based on ads being shown as a creative. Range of bid adjustment value would be 0:900")
    placement_bid_adjustments: Optional[list["PlacementBidAdjustment"]] = Field(None, alias="placementBidAdjustments", description="Bid adjustments based on ad placements.")
    shopper_segment_bid_adjustments: Optional[list["ShopperSegmentBidAdjustment"]] = Field(None, alias="shopperSegmentBidAdjustments", description="Legacy SB field (marked for deprecation)")

    model_config = {'populate_by_name': True}


class BidSettings(BaseModel):
    bid_adjustments: Optional["BidAdjustments"] = Field(None, alias="bidAdjustments")
    bid_strategy: Optional["BidStrategy"] = Field(None, alias="bidStrategy")

    model_config = {'populate_by_name': True}


class BrandExposureViewabilityTargetingType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    BRAND_EXPOSURE_VIEWABILITY_GTE_10_SEC_AVG_DURATION = "BRAND_EXPOSURE_VIEWABILITY_GTE_10_SEC_AVG_DURATION"
    BRAND_EXPOSURE_VIEWABILITY_GTE_15_SEC_AVG_DURATION = "BRAND_EXPOSURE_VIEWABILITY_GTE_15_SEC_AVG_DURATION"
    BRAND_EXPOSURE_VIEWABILITY_GTE_5_SEC_AVG_DURATION = "BRAND_EXPOSURE_VIEWABILITY_GTE_5_SEC_AVG_DURATION"


class BrandSafetyCategory(StrEnum):
    ACCIDENTS_DISASTERS_AND_TRAGEDIES = "ACCIDENTS_DISASTERS_AND_TRAGEDIES"
    ALCOHOL_AND_RELATED_PRODUCTS = "ALCOHOL_AND_RELATED_PRODUCTS"
    BLOOD_GORE_VIOLENCE = "BLOOD_GORE_VIOLENCE"
    CRIME = "CRIME"
    DRUG_REFERENCES_OR_USE = "DRUG_REFERENCES_OR_USE"
    GAMBLING = "GAMBLING"
    HIGHLY_DEBATED_SOCIAL_ISSUES = "HIGHLY_DEBATED_SOCIAL_ISSUES"
    POLITICS = "POLITICS"
    PROFANITY = "PROFANITY"
    RELIGIOUS_CONTENT = "RELIGIOUS_CONTENT"
    SEXUAL_REFERENCES_AND_SUGGESTIVE = "SEXUAL_REFERENCES_AND_SUGGESTIVE"
    SHOCK_AND_HORROR = "SHOCK_AND_HORROR"
    TOBACCO_AND_RELATED_PRODUCTS = "TOBACCO_AND_RELATED_PRODUCTS"
    UNRATED_MEDIA_CONTENT = "UNRATED_MEDIA_CONTENT"
    WEAPONS = "WEAPONS"


class BrandSafetyCategoryTarget(BaseModel):
    """Target based on, if any, the classifications of unsuitable contexts that may pose a risk to a brand's reputation of content being viewed."""
    brand_safety_category: "BrandSafetyCategory" = Field(..., alias="brandSafetyCategory")

    model_config = {'populate_by_name': True}


class BrandSafetyTier(StrEnum):
    EXPANDED = "EXPANDED"
    RESTRICTIVE = "RESTRICTIVE"
    STANDARD = "STANDARD"


class BrandSafetyTierTarget(BaseModel):
    """Target based on the brand suitability risk levels of content being viewed."""
    brand_safety_tier: "BrandSafetyTier" = Field(..., alias="brandSafetyTier")

    model_config = {'populate_by_name': True}


class BrandStorePageInfo(BaseModel):
    """Structure containing the basic information of a store page"""
    tag: str = Field(..., description="Unique tag for the store page")
    title: str = Field(..., description="Title of the page")

    model_config = {'populate_by_name': True}


class BrandStore(BaseModel):
    page_infos: Optional[list["BrandStorePageInfo"]] = Field(None, alias="pageInfos", description="Collection of BrandStorePageInfo for all pages tied to the brand store")
    store_id: str = Field(..., alias="storeId", description="Unique identifier for the store")
    store_name: Optional[str] = Field(None, alias="storeName", description="The name of the store")

    model_config = {'populate_by_name': True}


class StoreEditionSchedule(BaseModel):
    """Schedule information for store edition"""
    end_at: Optional[str] = Field(None, alias="endAt", description="End time for the store edition")
    start_at: Optional[str] = Field(None, alias="startAt", description="Start time for the store edition")

    model_config = {'populate_by_name': True}


class BrandStoreEdition(BaseModel):
    edition_id: str = Field(..., alias="editionId", description="Unique identifier for the edition within the store")
    edition_name: str = Field(..., alias="editionName", description="Name of the store edition")
    store_edition_schedule: Optional["StoreEditionSchedule"] = Field(None, alias="storeEditionSchedule")
    store_id: str = Field(..., alias="storeId", description="Identifier of the associated store")

    model_config = {'populate_by_name': True}


class StorePageVersion(BaseModel):
    """Version information for a store page"""
    page_id: str = Field(..., alias="pageId", description="Identifier of the page")
    version: int = Field(..., description="Version number of the page")

    model_config = {'populate_by_name': True}


class StorePublishStatus(StrEnum):
    DRAFT = "DRAFT"
    REVIEW_IN_PROGRESS = "REVIEW_IN_PROGRESS"


class StorePublishState(StrEnum):
    DRAFT = "DRAFT"
    PUBLISH = "PUBLISH"


class BrandStoreEditionPublishVersion(BaseModel):
    edition_id: str = Field(..., alias="editionId", description="Reference to the store edition")
    pages: Optional[list["StorePageVersion"]] = Field(None, description="Collection of page versions included in this publish version")
    publish_state: "StorePublishState" = Field(..., alias="publishState")
    publish_status: "StorePublishStatus" = Field(..., alias="publishStatus")
    store_edition_publish_id: str = Field(..., alias="storeEditionPublishId", description="Unique identifier for the publish version")
    store_id: str = Field(..., alias="storeId", description="Identifier of the associated store")

    model_config = {'populate_by_name': True}


class BrandStoreEditionPublishVersionBrandStoreEditionIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class BrandStoreEditionPublishVersionBrandStoreIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class BrandStoreEditionPublishVersionMultiStatusSuccess(BaseModel):
    brand_store_edition_publish_version: "BrandStoreEditionPublishVersion" = Field(..., alias="brandStoreEditionPublishVersion")
    index: int

    model_config = {'populate_by_name': True}


class BrandStoreEditionPublishVersionMultiStatusResponse(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    success: Optional[list["BrandStoreEditionPublishVersionMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class BrandStoreEditionPublishVersionStorePublishStatusFilter(BaseModel):
    include: list["StorePublishStatus"] = Field(..., description="| PublishStatus | Description | | --- | --- | | `DRAFT` | Content is in draft state | | `REVIEW_IN_PROGRESS` | Content i")

    model_config = {'populate_by_name': True}


class BrandStoreEditionPublishVersionSuccessResponse(BaseModel):
    brand_store_edition_publish_versions: Optional[list["BrandStoreEditionPublishVersion"]] = Field(None, alias="brandStoreEditionPublishVersions")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class BrandStoreEditionPublishVersionUpdate(BaseModel):
    edition_id: Optional[str] = Field(None, alias="editionId", description="Reference to the store edition")
    publish_state: Optional["StorePublishState"] = Field(None, alias="publishState")
    store_edition_publish_id: str = Field(..., alias="storeEditionPublishId", description="Unique identifier for the publish version")
    store_id: Optional[str] = Field(None, alias="storeId", description="Identifier of the associated store")

    model_config = {'populate_by_name': True}


class BrandStoreEditionSuccessResponse(BaseModel):
    brand_store_editions: Optional[list["BrandStoreEdition"]] = Field(None, alias="brandStoreEditions")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class StorePageType(StrEnum):
    BRAND_STORE_PAGE = "BRAND_STORE_PAGE"
    LANDING_PAGE = "LANDING_PAGE"


class StoreWidgetType(StrEnum):
    BANNER = "BANNER"
    EDITORIAL_ROW = "EDITORIAL_ROW"
    GALLERY = "GALLERY"
    HERO = "HERO"
    LIVE_VIDEO = "LIVE_VIDEO"
    MULTI_MEDIA_CAROUSEL = "MULTI_MEDIA_CAROUSEL"
    PRODUCT_CAROUSEL = "PRODUCT_CAROUSEL"
    PRODUCT_COLLECTION = "PRODUCT_COLLECTION"
    PRODUCT_GRID = "PRODUCT_GRID"


class StoreWidgetSectionType(StrEnum):
    BANNER = "BANNER"
    BEST_SELLING = "BEST_SELLING"
    DEALS_AND_COUPONS = "DEALS_AND_COUPONS"
    EDITORIAL_ROW = "EDITORIAL_ROW"
    GALLERY = "GALLERY"
    HERO = "HERO"
    LIVE_VIDEO = "LIVE_VIDEO"
    MANUALLY_CURATED_PRODUCT_CAROUSEL = "MANUALLY_CURATED_PRODUCT_CAROUSEL"
    PREMIUM_BEST_SELLING = "PREMIUM_BEST_SELLING"
    PRODUCT_COLLECTION = "PRODUCT_COLLECTION"
    PRODUCT_GRID = "PRODUCT_GRID"
    RECOMMENDED = "RECOMMENDED"
    SHOP_THE_LOOK_CAROUSEL = "SHOP_THE_LOOK_CAROUSEL"


class CommonWidgetProperties(BaseModel):
    section_type: "StoreWidgetSectionType" = Field(..., alias="sectionType")
    widget_tag: str = Field(..., alias="widgetTag", description="The unique tag for the widget to help track on performance.")
    widget_type: "StoreWidgetType" = Field(..., alias="widgetType")

    model_config = {'populate_by_name': True}


class StoreImageShape(StrEnum):
    SQUARE = "SQUARE"


class StoreTileBorderSize(StrEnum):
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    NONE = "NONE"
    SMALL = "SMALL"


class StoreTileType(StrEnum):
    CUSTOM_CODE = "CUSTOM_CODE"
    EMPTY = "EMPTY"
    EXTERNAL_WIDGET = "EXTERNAL_WIDGET"
    IMAGE = "IMAGE"
    INTERACTIVE_IMAGE = "INTERACTIVE_IMAGE"
    PRODUCT = "PRODUCT"
    TEXT = "TEXT"
    VIDEO = "VIDEO"


class StoreTileTextSize(StrEnum):
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    MINI = "MINI"
    SMALL = "SMALL"


class StoreCallToActionType(StrEnum):
    BUTTON = "BUTTON"
    LINK = "LINK"


class StoreTextAlignment(StrEnum):
    CENTER = "CENTER"
    JUSTIFY = "JUSTIFY"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class StoreTileLayerContent(BaseModel):
    body_text: Optional[str] = Field(None, alias="bodyText", description="Body text for the layer.")
    bond_customer_service_link: Optional[bool] = Field(None, alias="bondCustomerServiceLink", description="Whether to include a customer service link.")
    call_to_action: Optional[str] = Field(None, alias="callToAction", description="Call to action text for the layer.")
    call_to_action_type: Optional["StoreCallToActionType"] = Field(None, alias="callToActionType")
    custom_url: Optional[str] = Field(None, alias="customUrl", description="Custom URL for the layer.")
    header_text: Optional[str] = Field(None, alias="headerText", description="Header text for the layer.")
    page_id: Optional[str] = Field(None, alias="pageId", description="Page identifier for the layer.")
    prefix_text: Optional[str] = Field(None, alias="prefixText", description="Prefix text for the layer.")
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="Single ASIN for the layer.")
    tile_text_alignment: Optional["StoreTextAlignment"] = Field(None, alias="tileTextAlignment")
    tile_text_size: Optional["StoreTileTextSize"] = Field(None, alias="tileTextSize")

    model_config = {'populate_by_name': True}


class StoreColorPalette(StrEnum):
    DEFAULT = "DEFAULT"
    DEFAULT_INVERTED = "DEFAULT_INVERTED"
    SOLID_BLACK = "SOLID_BLACK"
    SOLID_WHITE = "SOLID_WHITE"
    TRANSLUCENT_BLACK = "TRANSLUCENT_BLACK"
    TRANSLUCENT_WHITE = "TRANSLUCENT_WHITE"
    TRANSPARENT_BLACK = "TRANSPARENT_BLACK"
    TRANSPARENT_WHITE = "TRANSPARENT_WHITE"


class HorizontalPosition(StrEnum):
    CENTER = "CENTER"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class VerticalPosition(StrEnum):
    BOTTOM = "BOTTOM"
    MIDDLE = "MIDDLE"
    TOP = "TOP"


class StoreTilePosition(BaseModel):
    x: Optional["HorizontalPosition"] = None
    y: Optional["VerticalPosition"] = None

    model_config = {'populate_by_name': True}


class StoreTileLayer(BaseModel):
    color_palette: Optional["StoreColorPalette"] = Field(None, alias="colorPalette")
    content: Optional["StoreTileLayerContent"] = None
    cover_tile: Optional[bool] = Field(None, alias="coverTile", description="Whether the layer covers the entire tile.")
    margin: Optional["StoreTileBorderSize"] = None
    opacity: Optional[float] = Field(None, description="Opacity level of the layer.")
    out_of_bounds: Optional[bool] = Field(None, alias="outOfBounds", description="Whether the layer is out of bounds.")
    padding: Optional["StoreTileBorderSize"] = None
    position: Optional["StoreTilePosition"] = None
    tag: Optional[str] = Field(None, description="Unique tag for the tile layer to track performance.")
    type_: Optional["StoreTileType"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class StoreImageLayout(StrEnum):
    CONTAIN = "CONTAIN"
    COVER = "COVER"
    TEXT = "TEXT"


class StoreCropBoxData(BaseModel):
    height: Optional[float] = Field(None, description="Height of the crop box.")
    left: Optional[float] = Field(None, description="Left position of the crop box.")
    top: Optional[float] = Field(None, description="Top position of the crop box.")
    width: Optional[float] = Field(None, description="Width of the crop box.")

    model_config = {'populate_by_name': True}


class StoreBleedImageType(StrEnum):
    ALL = "ALL"
    CORNER = "CORNER"
    NONE = "NONE"
    SIDE = "SIDE"


class StoreVerticalAlign(StrEnum):
    BOTTOM = "BOTTOM"
    MIDDLE = "MIDDLE"
    TOP = "TOP"


class StoreCanvasData(BaseModel):
    canvas_height: Optional[float] = Field(None, alias="canvasHeight", description="Height in the canvas.")
    height: Optional[float] = Field(None, description="Height in the canvas.")
    left: Optional[float] = Field(None, description="Left position in the canvas.")
    natural_height: Optional[float] = Field(None, alias="naturalHeight", description="Natural height of the image.")
    natural_width: Optional[float] = Field(None, alias="naturalWidth", description="Natural width of the image.")
    top: Optional[float] = Field(None, description="Top position in the canvas.")
    width: Optional[float] = Field(None, description="Width in the canvas.")

    model_config = {'populate_by_name': True}


class StoreTextOption(StrEnum):
    TEXT_NEXT_TO_IMAGE = "TEXT_NEXT_TO_IMAGE"
    TEXT_OVER_IMAGE = "TEXT_OVER_IMAGE"


class StoreMobileImageWithTextContent(BaseModel):
    alt_text: Optional[str] = Field(None, alias="altText", description="Alternative text for the mobile image.")
    asset_id: Optional[str] = Field(None, alias="assetId", description="Asset identifier for mobile.")
    asset_tags: Optional[str] = Field(None, alias="assetTags", description="Tags associated with the mobile asset.")
    bleed_image: Optional["StoreBleedImageType"] = Field(None, alias="bleedImage")
    canvas_data: Optional["StoreCanvasData"] = Field(None, alias="canvasData")
    crop_box_data: Optional["StoreCropBoxData"] = Field(None, alias="cropBoxData")
    hide_title: Optional[bool] = Field(None, alias="hideTitle", description="Whether to hide the title on mobile.")
    image_height: Optional[float] = Field(None, alias="imageHeight", description="Height of the mobile image.")
    image_key: Optional[str] = Field(None, alias="imageKey", description="Key identifier for the mobile image.")
    image_offset_left: Optional[float] = Field(None, alias="imageOffsetLeft", description="Left offset for mobile image positioning.")
    image_offset_top: Optional[float] = Field(None, alias="imageOffsetTop", description="Top offset for mobile image positioning.")
    image_url: Optional[str] = Field(None, alias="imageUrl", description="URL of the mobile image.")
    image_width: Optional[float] = Field(None, alias="imageWidth", description="Width of the mobile image.")
    is_ai_gen: Optional[bool] = Field(None, alias="isAiGen", description="Whether the mobile image is AI-generated.")
    layout: Optional["StoreImageLayout"] = None
    render_tile_layers: Optional[bool] = Field(None, alias="renderTileLayers", description="Whether to render tile layers on mobile.")
    shape: Optional["StoreImageShape"] = None
    text: Optional[str] = Field(None, description="Text content for mobile.")
    text_align: Optional["StoreTextAlignment"] = Field(None, alias="textAlign")
    text_option: Optional["StoreTextOption"] = Field(None, alias="textOption")
    tile_layers: Optional[list["StoreTileLayer"]] = Field(None, alias="tileLayers", description="Layer configuration for the mobile tile.")
    title: Optional[str] = Field(None, description="Title for mobile display.")
    vertical_align: Optional["StoreVerticalAlign"] = Field(None, alias="verticalAlign")

    model_config = {'populate_by_name': True}


class StoreImageWithTextContent(BaseModel):
    alt_text: Optional[str] = Field(None, alias="altText", description="Alternative text for the image.")
    asset_id: Optional[str] = Field(None, alias="assetId", description="Asset identifier.")
    asset_tags: Optional[str] = Field(None, alias="assetTags", description="Tags associated with the asset.")
    bleed_image: Optional["StoreBleedImageType"] = Field(None, alias="bleedImage")
    call_to_action: Optional[str] = Field(None, alias="callToAction", description="Call to action text.")
    canvas_data: Optional["StoreCanvasData"] = Field(None, alias="canvasData")
    crop_box_data: Optional["StoreCropBoxData"] = Field(None, alias="cropBoxData")
    custom_url: Optional[str] = Field(None, alias="customUrl", description="Custom URL.")
    hide_title: Optional[bool] = Field(None, alias="hideTitle", description="Whether to hide the title.")
    image_height: Optional[float] = Field(None, alias="imageHeight", description="Height of the image.")
    image_key: Optional[str] = Field(None, alias="imageKey", description="Key identifier for the image.")
    image_offset_left: Optional[float] = Field(None, alias="imageOffsetLeft", description="Left offset for image positioning.")
    image_offset_top: Optional[float] = Field(None, alias="imageOffsetTop", description="Top offset for image positioning.")
    image_url: Optional[str] = Field(None, alias="imageUrl", description="URL of the image.")
    image_width: Optional[float] = Field(None, alias="imageWidth", description="Width of the image.")
    is_ai_gen: Optional[bool] = Field(None, alias="isAiGen", description="Whether the image is AI-generated.")
    layout: Optional["StoreImageLayout"] = None
    page_id: Optional[str] = Field(None, alias="pageId", description="Page identifier.")
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="Single ASIN for the image.")
    render_tile_layers: Optional[bool] = Field(None, alias="renderTileLayers", description="Whether to render tile layers.")
    shape: Optional["StoreImageShape"] = None
    text: Optional[str] = Field(None, description="Text content.")
    text_align: Optional["StoreTextAlignment"] = Field(None, alias="textAlign")
    text_option: Optional["StoreTextOption"] = Field(None, alias="textOption")
    tile_layers: Optional[list["StoreTileLayer"]] = Field(None, alias="tileLayers", description="Layer configuration for the tile.")
    title: Optional[str] = Field(None, description="Title of the image.")
    vertical_align: Optional["StoreVerticalAlign"] = Field(None, alias="verticalAlign")

    model_config = {'populate_by_name': True}


class StoreImageWithTextTileVariation(StrEnum):
    IMAGE_WITH_TEXT = "IMAGE_WITH_TEXT"


class StoreTileSize(StrEnum):
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    MINI = "MINI"
    SMALL = "SMALL"


class CommonTileProperties(BaseModel):
    size: "StoreTileSize"
    tag: str = Field(..., description="The unique tag for the tile to help track on performance.")
    type_: "StoreTileType" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class StoreImageWithTextTile(BaseModel):
    common_properties: "CommonTileProperties" = Field(..., alias="commonProperties")
    content: Optional["StoreImageWithTextContent"] = None
    flex_height: Optional[bool] = Field(None, alias="flexHeight", description="Whether the height is flexible.")
    mobile_content: Optional["StoreMobileImageWithTextContent"] = Field(None, alias="mobileContent")
    upload_mobile_image: Optional[bool] = Field(None, alias="uploadMobileImage", description="Whether to upload a mobile-specific image.")
    variation: "StoreImageWithTextTileVariation"

    model_config = {'populate_by_name': True}


class StoreImageWithTextWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    tiles: list["StoreImageWithTextTile"] = Field(..., description="The image with text tile configuration. Exactly one tile is required.")

    model_config = {'populate_by_name': True}


class StoreCallToActionData(BaseModel):
    custom_url: Optional[str] = Field(None, alias="customUrl", description="Custom URL for the call to action.")
    page_id: Optional[str] = Field(None, alias="pageId", description="Page identifier.")
    product_asin: Optional[str] = Field(None, alias="productAsin", description="ASIN for the call to action.")
    text: Optional[str] = Field(None, description="Call to action text.")

    model_config = {'populate_by_name': True}


class StoreCarouselSearch(BaseModel):
    include_out_of_stock: bool = Field(..., alias="includeOutOfStock", description="Whether to include out of stock items in search.")
    keyword: str = Field(..., description="Search keyword.")
    node: str = Field(..., description="Node identifier for search.")
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="List of ASINs for search filtering.")

    model_config = {'populate_by_name': True}


class StoreSlideType(StrEnum):
    ASIN = "ASIN"
    IMAGE = "IMAGE"


class StoreASINSlide(BaseModel):
    product_asin: str = Field(..., alias="productAsin", description="The ASIN of the product.")
    tag: str = Field(..., description="Unique tag for the slide which will be ASIN.")
    type_: "StoreSlideType" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class StoreCarouselContent(BaseModel):
    bulk: bool = Field(..., description="Whether this is a bulk configuration.")
    call_to_action_data: "StoreCallToActionData" = Field(..., alias="callToActionData")
    include_out_of_stock: bool = Field(..., alias="includeOutOfStock", description="Whether to include out of stock items.")
    keyword: str = Field(..., description="Keyword for product filtering.")
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="List of ASINs, maximum 500 unique items.")
    search: Optional["StoreCarouselSearch"] = None
    slides: Optional[list["StoreASINSlide"]] = Field(None, description="List of ASIN slides.")
    tag: str = Field(..., description="Unique tag for the content to track performance.")
    text: str = Field(..., description="Description text.")
    title: str = Field(..., description="Title of the carousel.")
    type_: "StoreWidgetSectionType" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class StoreManuallyCuratedProductCarouselWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    content: Optional["StoreCarouselContent"] = None

    model_config = {'populate_by_name': True}


class StoreShoppableTextOption(StrEnum):
    NO_TEXT_UNDER_INTERACTIVE_IMAGE = "NO_TEXT_UNDER_INTERACTIVE_IMAGE"
    TEXT_OVER_IMAGE = "TEXT_OVER_IMAGE"
    TEXT_UNDER_INTERACTIVE_IMAGE = "TEXT_UNDER_INTERACTIVE_IMAGE"


class Coordinates(BaseModel):
    x: Optional[float] = Field(None, description="X coordinate.")
    y: Optional[float] = Field(None, description="Y coordinate.")

    model_config = {'populate_by_name': True}


class StoreShoppablePoint(BaseModel):
    coordinates: "Coordinates"
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="Single ASIN for the point.")
    tag: Optional[str] = Field(None, description="Unique tag for the point.")
    type_: Optional["StoreTileType"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class StoreCroppedImage(BaseModel):
    alt_text: Optional[str] = Field(None, alias="altText", description="Alternative text for the image.")
    asset_id: Optional[str] = Field(None, alias="assetId", description="Asset identifier.")
    canvas_data: Optional["StoreCanvasData"] = Field(None, alias="canvasData")
    crop_box: Optional["StoreCropBoxData"] = Field(None, alias="cropBox")
    image_key: Optional[str] = Field(None, alias="imageKey", description="Key identifier for the image.")
    image_natural_height: Optional[float] = Field(None, alias="imageNaturalHeight", description="Natural height of the image.")
    image_natural_width: Optional[float] = Field(None, alias="imageNaturalWidth", description="Natural width of the image.")
    image_url: Optional[str] = Field(None, alias="imageUrl", description="URL of the image.")

    model_config = {'populate_by_name': True}


class StoreShoppableImageContent(BaseModel):
    cropped_image: Optional["StoreCroppedImage"] = Field(None, alias="croppedImage")
    points: Optional[list["StoreShoppablePoint"]] = Field(None, description="Interactive points on the image.")
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="Single ASIN for the point.")
    render_tile_layers: Optional[bool] = Field(None, alias="renderTileLayers", description="Whether to render tile layers.")
    text_option: Optional["StoreShoppableTextOption"] = Field(None, alias="textOption")
    tile_layers: Optional[list["StoreTileLayer"]] = Field(None, alias="tileLayers", description="Layer configuration for the tile.")

    model_config = {'populate_by_name': True}


class StoreShoppableImageTile(BaseModel):
    common_properties: "CommonTileProperties" = Field(..., alias="commonProperties")
    content: Optional["StoreShoppableImageContent"] = None

    model_config = {'populate_by_name': True}


class StoreShoppableImageWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    tiles: list["StoreShoppableImageTile"] = Field(..., description="The shoppable image tile configuration. Exactly one tile is required.")

    model_config = {'populate_by_name': True}


class StoreTextContent(BaseModel):
    bold: bool = Field(..., description="Whether text should be bold.")
    bond_customer_service_link: Optional[bool] = Field(None, alias="bondCustomerServiceLink", description="Whether to include customer service link.")
    call_to_action: Optional[str] = Field(None, alias="callToAction", description="Call to action text.")
    custom_url: Optional[str] = Field(None, alias="customUrl", description="Custom URL for the content.")
    page_id: Optional[str] = Field(None, alias="pageId", description="Identifier for the page.")
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="Single product ASIN for the content.")
    text: str = Field(..., description="Main text content.")
    text_align: Optional["StoreTextAlignment"] = Field(None, alias="textAlign")
    title: str = Field(..., description="Title of the content.")
    uppercase: bool = Field(..., description="Whether text should be uppercase.")

    model_config = {'populate_by_name': True}


class StoreTextTile(BaseModel):
    common_properties: "CommonTileProperties" = Field(..., alias="commonProperties")
    content: Optional["StoreTextContent"] = None

    model_config = {'populate_by_name': True}


class StoreTextWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    tiles: list["StoreTextTile"] = Field(..., description="Single text tile configuration.")

    model_config = {'populate_by_name': True}


class StoreBanners(BaseModel):
    black_lives_matter: bool = Field(..., alias="blackLivesMatter", description="Flag to display Black Lives Matter banner")
    stop_asian_hate: bool = Field(..., alias="stopAsianHate", description="Flag to display Stop Asian Hate banner")

    model_config = {'populate_by_name': True}


class StoreBannerContent(BaseModel):
    banners: Optional["StoreBanners"] = None
    tag: Optional[str] = Field(None, description="Unique tag for the content.")
    type_: Optional["StoreWidgetType"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class StoreBannerWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    content: "StoreBannerContent"

    model_config = {'populate_by_name': True}


class StoreMobileImageContent(BaseModel):
    alt_text: Optional[str] = Field(None, alias="altText", description="Alternative text for the mobile image.")
    asset_id: Optional[str] = Field(None, alias="assetId", description="Asset identifier for mobile.")
    asset_tags: Optional[str] = Field(None, alias="assetTags", description="Tags associated with the mobile asset.")
    bleed_image: Optional["StoreBleedImageType"] = Field(None, alias="bleedImage")
    canvas_data: Optional["StoreCanvasData"] = Field(None, alias="canvasData")
    crop_box_data: Optional["StoreCropBoxData"] = Field(None, alias="cropBoxData")
    hide_title: Optional[bool] = Field(None, alias="hideTitle", description="Whether to hide the title on mobile.")
    image_height: Optional[float] = Field(None, alias="imageHeight", description="Height of the mobile image.")
    image_key: Optional[str] = Field(None, alias="imageKey", description="Key identifier for the mobile image.")
    image_offset_left: Optional[float] = Field(None, alias="imageOffsetLeft", description="Left offset for mobile image positioning.")
    image_offset_top: Optional[float] = Field(None, alias="imageOffsetTop", description="Top offset for mobile image positioning.")
    image_url: Optional[str] = Field(None, alias="imageUrl", description="URL of the mobile image.")
    image_width: Optional[float] = Field(None, alias="imageWidth", description="Width of the mobile image.")
    is_ai_gen: Optional[bool] = Field(None, alias="isAiGen", description="Whether the mobile image is AI-generated.")
    layout: Optional["StoreImageLayout"] = None
    tile_layers: Optional[list[str]] = Field(None, alias="tileLayers", description="Layer configuration for the mobile tile.")
    title: Optional[str] = Field(None, description="Title for mobile display.")
    vertical_align: Optional["StoreVerticalAlign"] = Field(None, alias="verticalAlign")

    model_config = {'populate_by_name': True}


class StoreImageTextAlign(StrEnum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class StoreImageContent(BaseModel):
    alt_text: Optional[str] = Field(None, alias="altText", description="Alternative text for the image.")
    asset_id: Optional[str] = Field(None, alias="assetId", description="Asset identifier.")
    asset_tags: Optional[str] = Field(None, alias="assetTags", description="Tags associated with the asset.")
    bleed_image: Optional["StoreBleedImageType"] = Field(None, alias="bleedImage")
    call_to_action: Optional[str] = Field(None, alias="callToAction", description="Call to action text.")
    canvas_data: Optional["StoreCanvasData"] = Field(None, alias="canvasData")
    crop_box_data: Optional["StoreCropBoxData"] = Field(None, alias="cropBoxData")
    custom_url: Optional[str] = Field(None, alias="customUrl", description="Custom URL.")
    hide_title: Optional[bool] = Field(None, alias="hideTitle", description="Whether to hide the title.")
    image_height: Optional[float] = Field(None, alias="imageHeight", description="Height of the image.")
    image_key: Optional[str] = Field(None, alias="imageKey", description="Key identifier for the image.")
    image_offset_left: Optional[float] = Field(None, alias="imageOffsetLeft", description="Left offset for image positioning.")
    image_offset_top: Optional[float] = Field(None, alias="imageOffsetTop", description="Top offset for image positioning.")
    image_url: Optional[str] = Field(None, alias="imageUrl", description="URL of the image.")
    image_width: Optional[float] = Field(None, alias="imageWidth", description="Width of the image.")
    is_ai_gen: Optional[bool] = Field(None, alias="isAiGen", description="Whether the image is AI-generated.")
    layout: Optional["StoreImageLayout"] = None
    page_id: Optional[str] = Field(None, alias="pageId", description="Page identifier.")
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="Single ASIN for the image.")
    text: Optional[str] = Field(None, description="Text content.")
    text_align: Optional["StoreImageTextAlign"] = Field(None, alias="textAlign")
    tile_layers: Optional[list[str]] = Field(None, alias="tileLayers", description="Layer configuration for the tile.")
    title: Optional[str] = Field(None, description="Title of the image.")
    vertical_align: Optional["StoreVerticalAlign"] = Field(None, alias="verticalAlign")

    model_config = {'populate_by_name': True}


class StoreImageTile(BaseModel):
    common_properties: "CommonTileProperties" = Field(..., alias="commonProperties")
    content: Optional["StoreImageContent"] = None
    flex_height: Optional[bool] = Field(None, alias="flexHeight", description="Whether the height is flexible.")
    mobile_content: Optional["StoreMobileImageContent"] = Field(None, alias="mobileContent")
    upload_mobile_image: Optional[bool] = Field(None, alias="uploadMobileImage", description="Whether to upload a mobile-specific image.")

    model_config = {'populate_by_name': True}


class StoreImageWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    tiles: list["StoreImageTile"] = Field(..., description="The image tile configuration. Exactly one tile is required.")

    model_config = {'populate_by_name': True}


class StoreTextOptionType(StrEnum):
    NO_TEXT_OVER_VIDEO = "NO_TEXT_OVER_VIDEO"
    TEXT_OVER_VIDEO = "TEXT_OVER_VIDEO"


class StoreVideoContent(BaseModel):
    asset_id: Optional[str] = Field(None, alias="assetId", description="Asset identifier.")
    asset_tags: Optional[str] = Field(None, alias="assetTags", description="Tags associated with the asset.")
    auto_play: Optional[bool] = Field(None, alias="autoPlay", description="Whether video should auto-play.")
    call_to_action: Optional[str] = Field(None, alias="callToAction", description="Call to action text.")
    canvas_data: Optional["StoreCanvasData"] = Field(None, alias="canvasData")
    custom_url: Optional[str] = Field(None, alias="customUrl", description="Custom URL for the content.")
    image_height: Optional[float] = Field(None, alias="imageHeight", description="Height of the image.")
    image_key: Optional[str] = Field(None, alias="imageKey", description="Key for the image asset.")
    image_offset_left: Optional[float] = Field(None, alias="imageOffsetLeft", description="Left offset for image positioning.")
    image_offset_top: Optional[float] = Field(None, alias="imageOffsetTop", description="Top offset for image positioning.")
    image_url: Optional[str] = Field(None, alias="imageUrl", description="URL of the image.")
    image_width: Optional[float] = Field(None, alias="imageWidth", description="Width of the image.")
    mute: Optional[bool] = Field(None, description="Whether video should be muted.")
    page_id: Optional[str] = Field(None, alias="pageId", description="Page identifier")
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="List of product ASINs.")
    render_tile_layers: Optional[bool] = Field(None, alias="renderTileLayers", description="Whether to render tile layers.")
    resource_id: Optional[str] = Field(None, alias="resourceId", description="Resource identifier.")
    text: Optional[str] = Field(None, description="Text content.")
    text_align: Optional[str] = Field(None, alias="textAlign", description="Text alignment.")
    text_option: Optional["StoreTextOptionType"] = Field(None, alias="textOption")
    tile_layers: Optional[list["StoreTileLayer"]] = Field(None, alias="tileLayers", description="Configuration for tile layers.")
    title: Optional[str] = Field(None, description="Title of the content.")
    video_asset_id: Optional[str] = Field(None, alias="videoAssetId", description="Video asset identifier.")
    video_asset_tags: Optional[str] = Field(None, alias="videoAssetTags", description="Tags associated with the video asset.")
    video_description: Optional[str] = Field(None, alias="videoDescription", description="Description of the video.")
    video_key: Optional[str] = Field(None, alias="videoKey", description="Key for the video asset.")
    video_name: Optional[str] = Field(None, alias="videoName", description="Name of the video.")
    video_size: Optional[float] = Field(None, alias="videoSize", description="Size of the video in bytes.")
    video_url: Optional[str] = Field(None, alias="videoUrl", description="URL of the video.")

    model_config = {'populate_by_name': True}


class StoreVideoTile(BaseModel):
    common_properties: "CommonTileProperties" = Field(..., alias="commonProperties")
    content: Optional["StoreVideoContent"] = None

    model_config = {'populate_by_name': True}


class StoreVideoWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    tiles: list["StoreVideoTile"] = Field(..., description="The content configuration for the video widget.")

    model_config = {'populate_by_name': True}


class CTI(BaseModel):
    category: Optional[str] = Field(None, description="Category identifier.")
    item: Optional[str] = Field(None, description="Item identifier.")
    type_: Optional[str] = Field(None, alias="type", description="Type identifier.")

    model_config = {'populate_by_name': True}


class StoreCustomCodeContent(BaseModel):
    auto_dimension: Optional[bool] = Field(None, alias="autoDimension", description="Whether to use automatic dimensioning.")
    available_product_asins: Optional[list[str]] = Field(None, alias="availableProductAsins", description="List of available ASINs, maximum 500 unique items.")
    cti: Optional["CTI"] = None
    embed_code: Optional[str] = Field(None, alias="embedCode", description="Embedded code content.")
    integrity: Optional[str] = Field(None, description="Integrity hash for security.")
    widget_name: Optional[str] = Field(None, alias="widgetName", description="Name of the widget.")
    widget_tag: Optional[str] = Field(None, alias="widgetTag", description="Widget identifier.")

    model_config = {'populate_by_name': True}


class StoreCustomCodeTile(BaseModel):
    common_properties: "CommonTileProperties" = Field(..., alias="commonProperties")
    content: Optional["StoreCustomCodeContent"] = None

    model_config = {'populate_by_name': True}


class StoreEmptyTileContent(BaseModel):
    bond_customer_service_link: Optional[bool] = Field(None, alias="bondCustomerServiceLink", description="Whether to include a customer service link.")
    call_to_action: Optional[str] = Field(None, alias="callToAction", description="Call to action text.")
    text: Optional[str] = Field(None, description="Text content (must be empty).")
    text_align: Optional["StoreTextAlignment"] = Field(None, alias="textAlign")
    title: Optional[str] = Field(None, description="Title of the tile (must be empty).")

    model_config = {'populate_by_name': True}


class StoreEmptyTile(BaseModel):
    common_properties: "CommonTileProperties" = Field(..., alias="commonProperties")
    content: "StoreEmptyTileContent"

    model_config = {'populate_by_name': True}


class StoreLayoutType(StrEnum):
    DEFAULT = "DEFAULT"
    SHOWCASE = "SHOWCASE"


class StoreProductTileContent(BaseModel):
    bleed_image: Optional["StoreBleedImageType"] = Field(None, alias="bleedImage")
    display_out_of_stock_asin: Optional[bool] = Field(None, alias="displayOutOfStockASIN", description="Whether to display out of stock ASIN.")
    layout: Optional["StoreLayoutType"] = None
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="Single ASIN for the product.")
    text: Optional[str] = Field(None, description="Description text for the product.")
    text_align: Optional["StoreTextAlignment"] = Field(None, alias="textAlign")
    title: Optional[str] = Field(None, description="Title of the product.")

    model_config = {'populate_by_name': True}


class StoreProductTile(BaseModel):
    common_properties: "CommonTileProperties" = Field(..., alias="commonProperties")
    content: Optional["StoreProductTileContent"] = None

    model_config = {'populate_by_name': True}


class StoreTile(BaseModel):
    pass


class StoreTileWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    row_height: Optional[int] = Field(None, alias="rowHeight", description="Height of the row in pixels.")
    tiles: list["StoreTile"] = Field(..., description="The tiles for the widget. Minimum 2 and maximum 8 tiles are allowed.")

    model_config = {'populate_by_name': True}


class StoreDealsConfig(BaseModel):
    node: Optional[str] = Field(None, description="Node identifier for deals.")

    model_config = {'populate_by_name': True}


class StoreDealsMode(StrEnum):
    AUTOMATIC = "AUTOMATIC"
    BULK = "BULK"


class StoreDealsContent(BaseModel):
    deals: Optional["StoreDealsConfig"] = None
    deals_mode: Optional["StoreDealsMode"] = Field(None, alias="dealsMode")
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="List of ASINs, maximum 500 unique items.")
    tag: Optional[str] = Field(None, description="Unique tag for the content to track performance.")
    type_: Optional["StoreWidgetSectionType"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class StoreDealsWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    content: Optional["StoreDealsContent"] = None

    model_config = {'populate_by_name': True}


class StoreLiveVideoContent(BaseModel):
    channel: Optional[str] = Field(None, description="Channel of the video.")
    tag: str = Field(..., description="Unique tag for the content.")
    type_: "StoreWidgetType" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class StoreLiveVideoWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    content: "StoreLiveVideoContent"

    model_config = {'populate_by_name': True}


class StoreImageSlide(BaseModel):
    asset_id: Optional[str] = Field(None, alias="assetId", description="Asset identifier.")
    asset_tags: Optional[str] = Field(None, alias="assetTags", description="Tags associated with the asset.")
    canvas_data: Optional["StoreCanvasData"] = Field(None, alias="canvasData")
    image_height: Optional[float] = Field(None, alias="imageHeight", description="Height of the image.")
    image_key: Optional[str] = Field(None, alias="imageKey", description="Key identifier for the image.")
    image_offset_left: Optional[float] = Field(None, alias="imageOffsetLeft", description="Left offset for image positioning.")
    image_offset_top: Optional[float] = Field(None, alias="imageOffsetTop", description="Top offset for image positioning.")
    image_url: Optional[str] = Field(None, alias="imageUrl", description="URL of the image.")
    image_width: Optional[float] = Field(None, alias="imageWidth", description="Width of the image.")
    tag: Optional[str] = Field(None, description="Unique identifier for the slide.")
    type_: Optional["StoreSlideType"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class StoreShopTheLookSlide(BaseModel):
    pass


class StoreShopTheLookSearch(BaseModel):
    include_out_of_stock: Optional[bool] = Field(None, alias="includeOutOfStock", description="Whether to include out of stock items in search.")
    keyword: Optional[str] = Field(None, description="Search keyword.")
    node: Optional[str] = Field(None, description="Node identifier for search.")
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="Single ASIN for search filtering.")

    model_config = {'populate_by_name': True}


class StoreShopTheLookContent(BaseModel):
    bulk: Optional[bool] = Field(None, description="Whether this is a bulk configuration.")
    call_to_action_data: Optional["StoreCallToActionData"] = Field(None, alias="callToActionData")
    include_out_of_stock: Optional[bool] = Field(None, alias="includeOutOfStock", description="Whether to include out of stock items.")
    keyword: Optional[str] = Field(None, description="Keyword for searching.")
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="List of product ASINs, maximum 25 unique items.")
    search: Optional["StoreShopTheLookSearch"] = None
    slides: Optional[list["StoreShopTheLookSlide"]] = Field(None, description="List of slides in the carousel.")
    tag: Optional[str] = Field(None, description="Unique tag for the content.")
    text: Optional[str] = Field(None, description="Text content.")
    title: Optional[str] = Field(None, description="Title of the content.")
    type_: Optional["StoreWidgetSectionType"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class StoreShopTheLookWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    content: Optional["StoreShopTheLookContent"] = None

    model_config = {'populate_by_name': True}


class StoreCallToActionProductData(BaseModel):
    custom_url: Optional[str] = Field(None, alias="customUrl", description="Custom URL for the call to action.")
    product_asin: Optional[str] = Field(None, alias="productAsin", description="Product ASIN for the call to action.")
    text: Optional[str] = Field(None, description="Call to action text.")

    model_config = {'populate_by_name': True}


class StoreProductCarouselSearchType(StrEnum):
    BEST_SELLING = "BEST_SELLING"
    RECOMMENDATION_FOR_YOU = "RECOMMENDATION_FOR_YOU"


class StoreProductCarouselSearch(BaseModel):
    node: Optional[str] = Field(None, description="Node identifier for search")
    type_: Optional["StoreProductCarouselSearchType"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class StoreProductCarouselContent(BaseModel):
    call_to_action_data: Optional["StoreCallToActionProductData"] = Field(None, alias="callToActionData")
    search_content: Optional["StoreProductCarouselSearch"] = Field(None, alias="searchContent")
    tag: str = Field(..., description="Unique tag for the content.")
    type_: "StoreWidgetSectionType" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class StoreProductCarouselWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    content: "StoreProductCarouselContent"

    model_config = {'populate_by_name': True}


class StoreProductCollectionContent(BaseModel):
    collection_tags: Optional[str] = Field(None, alias="collectionTags", description="Tags associated with the collection.")
    product_grid_conversion_timestamp: Optional[float] = Field(None, alias="productGridConversionTimestamp", description="Timestamp of product grid conversion.")
    tag: Optional[str] = Field(None, description="Unique tag for the content.")
    type_: Optional["StoreWidgetType"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class StoreProductCollectionASINGrid(BaseModel):
    bulk: Optional[bool] = Field(None, description="Whether this is a bulk configuration.")
    description: Optional[str] = Field(None, description="Description of the product grid.")
    display_product_grid_header: Optional[bool] = Field(None, alias="displayProductGridHeader", description="Whether to display the product grid header.")
    include_out_of_stock: Optional[bool] = Field(None, alias="includeOutOfStock", description="Whether to include out of stock products.")
    is_automated_product_grid: Optional[bool] = Field(None, alias="isAutomatedProductGrid", description="Whether the product grid is automatically populated")
    keyword: Optional[str] = Field(None, description="Keyword for product filtering.")
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="List of ASINs, maximum 60 unique items.")
    sort: Optional[str] = Field(None, description="Sort order for products.")
    tag: Optional[str] = Field(None, description="Unique tag for the tile to track performance.")
    title: Optional[str] = Field(None, description="Title of the product grid.")
    type_: "StoreWidgetSectionType" = Field(..., alias="type")
    variation: Optional[str] = Field(None, description="Variation of the product grid.")

    model_config = {'populate_by_name': True}


class StoreProductCollectionImageTile(BaseModel):
    common_properties: "CommonTileProperties" = Field(..., alias="commonProperties")
    content: Optional["StoreImageWithTextContent"] = None
    flex_height: Optional[bool] = Field(None, alias="flexHeight", description="Whether the height is flexible.")
    mobile_content: Optional["StoreMobileImageWithTextContent"] = Field(None, alias="mobileContent")
    upload_mobile_image: Optional[bool] = Field(None, alias="uploadMobileImage", description="Whether to upload a mobile-specific image.")
    variation: "StoreImageWithTextTileVariation"

    model_config = {'populate_by_name': True}


class StoreProductCollectionTile(BaseModel):
    pass


class StoreProductCollectionWidget(BaseModel):
    ai_metadata: Optional[list["Tag"]] = Field(None, alias="aiMetadata", description="Metadata about AI generated fields.")
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    content: Optional["StoreProductCollectionContent"] = None
    tiles: list["StoreProductCollectionTile"] = Field(..., description="The tiles for the product collection. Exactly two tiles are required.")

    model_config = {'populate_by_name': True}


class StoreGallerySlide(BaseModel):
    alt: Optional[str] = Field(None, description="Alternative text for the slide.")
    asset_id: Optional[str] = Field(None, alias="assetId", description="Asset identifier for the slide.")
    image_key: Optional[str] = Field(None, alias="imageKey", description="Key identifier for the image.")
    type_: Optional["StoreSlideType"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class StoreMetadataItem(BaseModel):
    alt: Optional[str] = Field(None, description="Alternative text.")
    asset_id: Optional[str] = Field(None, alias="assetId", description="Asset identifier.")
    filename: Optional[str] = Field(None, description="Name of the file.")
    image_key: Optional[str] = Field(None, alias="imageKey", description="Key identifier for the image.")
    image_url: Optional[str] = Field(None, alias="imageUrl", description="The imageUrl of the item.")
    type_: Optional["StoreTileType"] = Field(None, alias="type")
    url: Optional[str] = Field(None, description="URL of the item.")

    model_config = {'populate_by_name': True}


class StoreGalleryContent(BaseModel):
    metadata: Optional[list["StoreMetadataItem"]] = Field(None, description="Metadata associated with the gallery.")
    slides: Optional[list["StoreGallerySlide"]] = Field(None, description="List of slides in the gallery.")
    tag: Optional[str] = Field(None, description="Unique tag for the content.")
    text: Optional[str] = Field(None, description="Text content of the gallery.")
    title: Optional[str] = Field(None, description="Title of the gallery.")
    type_: Optional["StoreWidgetType"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class StoreGalleryWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    content: Optional["StoreGalleryContent"] = None

    model_config = {'populate_by_name': True}


class StoreProductSelectorImageLayout(StrEnum):
    BOTTOM = "BOTTOM"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    TOP = "TOP"


class StoreProductSelectorLayoutConfiguration(BaseModel):
    """Layout configuration for desktop and mobile views"""
    desktop_layout: "StoreProductSelectorImageLayout" = Field(..., alias="desktopLayout")
    mobile_layout: "StoreProductSelectorImageLayout" = Field(..., alias="mobileLayout")

    model_config = {'populate_by_name': True}


class StoreProductSelectorImage(BaseModel):
    """Represents an image used in the product selector introduction"""
    asset_id: str = Field(..., alias="assetId", description="Asset ID of the image")
    file_name: Optional[str] = Field(None, alias="fileName", description="File name of the image")
    image_url: str = Field(..., alias="imageUrl", description="URL of the image")
    layout: Optional["StoreProductSelectorImageLayout"] = None

    model_config = {'populate_by_name': True}


class StoreProductSelectorImageOptions(BaseModel):
    """Image options for the product selector introduction"""
    image: "StoreProductSelectorImage"
    layout_configuration: "StoreProductSelectorLayoutConfiguration" = Field(..., alias="layoutConfiguration")

    model_config = {'populate_by_name': True}


class StoreProductSelectorIntroduction(BaseModel):
    """Introduction section for the product selector widget"""
    button_text: str = Field(..., alias="buttonText", description="Text displayed on the introduction button")
    description: str = Field(..., description="Description text for the introduction section")
    heading: str = Field(..., description="Heading text for the introduction section")
    headline: Optional[str] = Field(None, description="Headline text for the introduction section")
    image_options: "StoreProductSelectorImageOptions" = Field(..., alias="imageOptions")
    is_enabled: bool = Field(..., alias="isEnabled", description="Flag indicating whether the introduction is enabled")

    model_config = {'populate_by_name': True}


class StoreProductSelectorAnswer(BaseModel):
    """Represents a possible answer in the product selector questionnaire"""
    image: Optional["StoreProductSelectorImage"] = None
    next_step: str = Field(..., alias="nextStep", description="Reference to the next question or step in the selection flow")
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="List of ASINs associated with this answer")
    tag: str = Field(..., description="Unique identifier for the answer")
    text: Optional[str] = Field(None, description="Display text for the answer option")

    model_config = {'populate_by_name': True}


class StoreProductSelectorQuestion(BaseModel):
    """Represents a question in the product selector questionnaire"""
    answer_list: Optional[list["StoreProductSelectorAnswer"]] = Field(None, alias="answerList", description="List of possible answers for this question")
    are_images_enabled: Optional[bool] = Field(None, alias="areImagesEnabled", description="Flag indicating whether images are enabled")
    description: Optional[str] = Field(None, description="Additional descriptive text or context for the question")
    has_image: Optional[bool] = Field(None, alias="hasImage", description="Flag indicating whether the question has an image")
    tag: str = Field(..., description="Unique identifier for the question")
    text: Optional[str] = Field(None, description="Main question text displayed to the user")

    model_config = {'populate_by_name': True}


class StoreProductSelectorResults(BaseModel):
    """Configuration for displaying product selector results"""
    button_text: Optional[str] = Field(None, alias="buttonText", description="Text to display on the call-to-action button")
    description: Optional[str] = Field(None, description="Descriptive text explaining the results")
    disclaimer: str = Field(..., description="Legal or additional information text for the results")
    headline: str = Field(..., description="Main heading text for the results section")
    store_url: Optional[str] = Field(None, alias="storeUrl", description="URL to the store page for the selected products")

    model_config = {'populate_by_name': True}


class StoreProductSelectorButtonColor(StrEnum):
    BLACK = "BLACK"
    TRANSPARENT = "TRANSPARENT"
    WHITE = "WHITE"


class StoreProductSelectorDesignOptions(BaseModel):
    """Visual styling options for the product selector widget"""
    background_color: str = Field(..., alias="backgroundColor", description="Background color in hex or named color value")
    background_shape: str = Field(..., alias="backgroundShape", description="Shape of the background container")
    button_color: Optional["StoreProductSelectorButtonColor"] = Field(None, alias="buttonColor")
    button_shape: str = Field(..., alias="buttonShape", description="Shape style for buttons in the selector")
    text_alignment: str = Field(..., alias="textAlignment", description="Alignment of text elements (left, center, right)")
    text_size: str = Field(..., alias="textSize", description="Size of the text elements")
    text_style: str = Field(..., alias="textStyle", description="Font family or style to be used")
    text_weight: str = Field(..., alias="textWeight", description="Font weight for text elements")

    model_config = {'populate_by_name': True}


class StoreProductSelectorWidget(BaseModel):
    """Main widget structure for the product selector feature"""
    design_options: "StoreProductSelectorDesignOptions" = Field(..., alias="designOptions")
    introduction: Optional["StoreProductSelectorIntroduction"] = None
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="Master list of ASINs available in the selector")
    question_list: Optional[list["StoreProductSelectorQuestion"]] = Field(None, alias="questionList", description="Ordered list of questions in the selector flow")
    results: "StoreProductSelectorResults"

    model_config = {'populate_by_name': True}


class StoreVideoRevealVRVideo(BaseModel):
    """Configuration for a single video reveal video asset"""
    asset_id: str = Field(..., alias="assetId", description="Unique identifier for the video asset")
    url: str = Field(..., description="URL of the video content")

    model_config = {'populate_by_name': True}


class StoreVideoRevealVideos(BaseModel):
    """Collection of video assets for different device types"""
    desktop: "StoreVideoRevealVRVideo"
    mobile: "StoreVideoRevealVRVideo"

    model_config = {'populate_by_name': True}


class StoreVideoRevealWidget(BaseModel):
    """Main widget structure for the video reveal feature"""
    background_color: str = Field(..., alias="backgroundColor", description="Background color (CSS property)")
    csm_tag: str = Field(..., alias="csmTag", description="CSM tracking tag for the video reveal")
    fadeout_duration: str = Field(..., alias="fadeoutDuration", description="Fadeout duration (in ms)")
    object_fit: str = Field(..., alias="objectFit", description="Object fit (CSS property)")
    skip_reveal: bool = Field(..., alias="skipReveal", description="Skip reveal (to be used in development only)")
    throttle_limit: str = Field(..., alias="throttleLimit", description="Play video every X minutes")
    videos: "StoreVideoRevealVideos"

    model_config = {'populate_by_name': True}


class BrandedRecipeMedia(BaseModel):
    """Represents media content associated with a recipe"""
    alt_text: Optional[str] = Field(None, alias="altText", description="Alternative text description of the media content")
    asset_library_id: Optional[str] = Field(None, alias="assetLibraryId", description="Identifier for the asset.")
    media_url: Optional[str] = Field(None, alias="mediaUrl", description="URL of the media content")

    model_config = {'populate_by_name': True}


class ReviewStars(BaseModel):
    """Review information for a product"""
    has_half_star: bool = Field(..., alias="hasHalfStar", description="Flag indicating if the product has a half star in the rating")
    review_count: int = Field(..., alias="reviewCount", description="Number of reviews for the product")
    whole_stars: int = Field(..., alias="wholeStars", description="Number of whole stars in the rating")

    model_config = {'populate_by_name': True}


class PriorityAsin(BaseModel):
    """Product information for a priority ASIN"""
    add_to_cart_action_params: str = Field(..., alias="addToCartActionParams", description="Parameters for add to cart action")
    bottle_deposit_fee: Optional[str] = Field(None, alias="bottleDepositFee", description="Bottle deposit fee amount")
    bottle_deposit_fee_string: Optional[str] = Field(None, alias="bottleDepositFeeString", description="Bottle deposit fee as string")
    cart_quantity: float = Field(..., alias="cartQuantity", description="Quantity of this item in the cart")
    catalog_display_price_per_unit_of_measure: Optional[str] = Field(None, alias="catalogDisplayPricePerUnitOfMeasure", description="Price per unit of measure for display")
    fresh_button: Optional[str] = Field(None, alias="freshButton", description="Fresh button information")
    is_alternate_search_result: bool = Field(..., alias="isAlternateSearchResult", description="Flag indicating if this is an alternate search result")
    is_required_quantity_in_cart: bool = Field(..., alias="isRequiredQuantityInCart", description="Flag indicating if a quantity is required in cart")
    is_sold_by_count: bool = Field(..., alias="isSoldByCount", description="Flag indicating if the product is sold by count")
    item_availability: str = Field(..., alias="itemAvailability", description="Status of item availability")
    offer_id: str = Field(..., alias="offerId", description="Unique identifier for the offer")
    offer_name: str = Field(..., alias="offerName", description="Display name of the product offer")
    offer_unit: str = Field(..., alias="offerUnit", description="Unit of the offer (e.g., Fl Oz, lb)")
    product_asin: str = Field(..., alias="productAsin", description="ASIN associated with this product")
    product_details_url: str = Field(..., alias="productDetailsUrl", description="URL to the product details page")
    product_image_url: str = Field(..., alias="productImageUrl", description="URL of the product image")
    promotion_display: Optional[str] = Field(None, alias="promotionDisplay", description="Display text for active promotion")
    promotion_id: Optional[str] = Field(None, alias="promotionId", description="Identifier for active promotion")
    quantity_in_stock: Optional[float] = Field(None, alias="quantityInStock", description="Available quantity in stock")
    required_quantity: float = Field(..., alias="requiredQuantity", description="Required quantity for purchase")
    retail_atc_button: Optional[str] = Field(None, alias="retailATCButton", description="Retail add-to-cart button information")
    review_stars: Optional["ReviewStars"] = Field(None, alias="reviewStars")
    search_term: Optional[str] = Field(None, alias="searchTerm", description="Search term associated with this product")
    subtotal_params: str = Field(..., alias="subtotalParams", description="Subtotal parameters for pricing calculations")
    vuom_display_price: str = Field(..., alias="vuomDisplayPrice", description="Display price for virtual unit of measure")

    model_config = {'populate_by_name': True}


class BrandedRecipeIngredientsMetadata(BaseModel):
    """Contains metadata information for recipe ingredients"""
    priority_asins: Optional[list["PriorityAsin"]] = Field(None, alias="priorityAsins", description="List of priority ASINs for ingredients with detailed product information")
    quantity: Optional[float] = Field(None, description="Quantity amount for the ingredient")
    search_text: Optional[str] = Field(None, alias="searchText", description="Search text for ingredient metadata")
    translated_unit: Optional[str] = Field(None, alias="translatedUnit", description="Translated unit of measurement")

    model_config = {'populate_by_name': True}


class BrandedRecipeQuantityItem(BaseModel):
    """Represents a quantity measurement for a recipe ingredient"""
    amount: float = Field(..., description="Numerical amount of the ingredient")
    unit: str = Field(..., description="Unit of measurement for the ingredient")

    model_config = {'populate_by_name': True}


class BrandedRecipeIngredient(BaseModel):
    """Represents an ingredient in a branded recipe"""
    asin_overrides: Optional[list[str]] = Field(None, alias="asinOverrides", description="List of ASIN overrides for the ingredient")
    brand: str = Field(..., description="Brand name associated with the ingredient")
    display_text: str = Field(..., alias="displayText", description="Formatted text for displaying the ingredient")
    is_asin_restricted: bool = Field(..., alias="isAsinRestricted", description="Flag indicating if ASIN is restricted for this ingredient")
    is_brand_restricted: bool = Field(..., alias="isBrandRestricted", description="Flag indicating if brand is restricted for this ingredient")
    is_exclusive_override: bool = Field(..., alias="isExclusiveOverride", description="Flag indicating if this ingredient has exclusive override")
    name: str = Field(..., description="Name of the ingredient")
    quantity_list: Optional[list["BrandedRecipeQuantityItem"]] = Field(None, alias="quantityList", description="List of quantity measurements for the ingredient")

    model_config = {'populate_by_name': True}


class BrandedRecipeDirection(BaseModel):
    """Represents a single step in a recipe's directions"""
    body: str = Field(..., description="Detailed instruction text for the direction step")
    title: str = Field(..., description="Title or heading for the direction step")

    model_config = {'populate_by_name': True}


class BrandedRecipeWidget(BaseModel):
    """Main widget structure for displaying a branded recipe"""
    available_product_asins: Optional[list[str]] = Field(None, alias="availableProductAsins", description="List of available product ASINs.")
    desktop_media: Optional["BrandedRecipeMedia"] = Field(None, alias="desktopMedia")
    directions: Optional[list["BrandedRecipeDirection"]] = Field(None, description="List of preparation directions for the recipe")
    encoded_ingredient_composition: Optional[str] = Field(None, alias="encodedIngredientComposition", description="Encoded string containing ingredient composition details")
    ingredient_metadata: Optional[list["BrandedRecipeIngredientsMetadata"]] = Field(None, alias="ingredientMetadata", description="Metadata associated with recipe ingredients")
    ingredients: Optional[list["BrandedRecipeIngredient"]] = Field(None, description="List of ingredients required for the recipe")
    is_initial_load: Optional[bool] = Field(None, alias="isInitialLoad", description="Flag indicating if recipe is set to initial load")
    mobile_media: Optional["BrandedRecipeMedia"] = Field(None, alias="mobileMedia")
    preparation_time: str = Field(..., alias="preparationTime", description="Time required to prepare the recipe")
    ref_tag: Optional[str] = Field(None, alias="refTag", description="REF tracking tag for the branded recipe")
    serving_size: float = Field(..., alias="servingSize", description="Number of servings the recipe yields")
    title: Optional[str] = Field(None, description="Title of the recipe")

    model_config = {'populate_by_name': True}


class StoreAWLSTileContent(BaseModel):
    pass


class StoreAWLSTile(BaseModel):
    common_properties: "CommonTileProperties" = Field(..., alias="commonProperties")
    content: Optional["StoreAWLSTileContent"] = None
    external_widget_id: str = Field(..., alias="externalWidgetId", description="External widget identifier.")

    model_config = {'populate_by_name': True}


class StoreAWLSWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    tiles: list["StoreAWLSTile"] = Field(..., description="The AWLS tile configuration. Exactly one tile is required.")
    widget_dependencies: Optional[list[str]] = Field(None, alias="widgetDependencies", description="List of widget dependencies.")

    model_config = {'populate_by_name': True}


class StoreCustomCodeWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    tiles: list["StoreCustomCodeTile"] = Field(..., description="The custom code tile configuration. Exactly one tile is required.")

    model_config = {'populate_by_name': True}


class StoreProductWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    tiles: list["StoreProductTile"] = Field(..., description="The product tile configuration. Exactly one tile is required.")

    model_config = {'populate_by_name': True}


class StoreMobileContent(BaseModel):
    asset_id: Optional[str] = Field(None, alias="assetId", description="Asset identifier for mobile view.")
    asset_tags: Optional[str] = Field(None, alias="assetTags", description="Asset tags for mobile view.")
    canvas_data: Optional["StoreCanvasData"] = Field(None, alias="canvasData")
    image_height: Optional[float] = Field(None, alias="imageHeight", description="Height of the image for mobile view.")
    image_key: Optional[str] = Field(None, alias="imageKey", description="Image key for mobile view.")
    image_offset_left: Optional[float] = Field(None, alias="imageOffsetLeft", description="Left offset of the image for mobile view.")
    image_offset_top: Optional[float] = Field(None, alias="imageOffsetTop", description="Top offset of the image for mobile view.")
    image_url: Optional[str] = Field(None, alias="imageUrl", description="URL of the image for mobile view.")
    image_width: Optional[float] = Field(None, alias="imageWidth", description="Width of the image for mobile view.")
    version: Optional[str] = Field(None, description="Version identifier for mobile content")

    model_config = {'populate_by_name': True}


class StoreHeroContent(BaseModel):
    asset_id: Optional[str] = Field(None, alias="assetId", description="Identifier for the asset.")
    asset_tags: Optional[str] = Field(None, alias="assetTags", description="Tags associated with the asset.")
    canvas_data: Optional["StoreCanvasData"] = Field(None, alias="canvasData")
    description: Optional[str] = Field(None, description="Description of the hero image.")
    image_height: Optional[float] = Field(None, alias="imageHeight", description="Height of the hero image.")
    image_key: Optional[str] = Field(None, alias="imageKey", description="Key identifier for the image.")
    image_offset_left: Optional[float] = Field(None, alias="imageOffsetLeft", description="Left offset of the image.")
    image_offset_top: Optional[float] = Field(None, alias="imageOffsetTop", description="Top offset of the image.")
    image_url: str = Field(..., alias="imageUrl", description="URL of the hero image.")
    image_width: Optional[float] = Field(None, alias="imageWidth", description="Width of the hero image.")
    mobile_content: Optional["StoreMobileContent"] = Field(None, alias="mobileContent")
    tag: Optional[str] = Field(None, description="Unique tag for the content.")
    text_overlay: Optional[str] = Field(None, alias="textOverlay", description="Text overlay displayed on the hero image.")

    model_config = {'populate_by_name': True}


class StoreHeroImageWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    content: Optional["StoreHeroContent"] = None

    model_config = {'populate_by_name': True}


class StoreProductGridSearch(BaseModel):
    brand_id: Optional[str] = Field(None, alias="brandId", description="brand id to search.")
    include_out_of_stock: Optional[bool] = Field(None, alias="includeOutOfStock", description="Whether to include out of stock products in search.")
    keyword: Optional[str] = Field(None, description="Search keyword.")
    node: Optional[str] = Field(None, description="Node identifier for search.")
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="List of product ASINs.")
    sort: Optional[str] = Field(None, description="Sort order for search results.")

    model_config = {'populate_by_name': True}


class StoreProductGridContent(BaseModel):
    bulk: Optional[bool] = Field(None, description="Whether this is a bulk product grid.")
    description: Optional[str] = Field(None, description="Description of the product grid.")
    display_product_grid_header: Optional[bool] = Field(None, alias="displayProductGridHeader", description="Whether to display the grid header.")
    excluded_product_asins: Optional[list[str]] = Field(None, alias="excludedProductAsins", description="List of product ASINs exclude when dynamic.")
    include_out_of_stock: Optional[bool] = Field(None, alias="includeOutOfStock", description="Whether to include out of stock products.")
    is_automated_product_grid: Optional[bool] = Field(None, alias="isAutomatedProductGrid", description="Whether the product grid is automatically populated")
    keyword: Optional[str] = Field(None, description="Keyword for product filtering.")
    pinned_product_asins: Optional[list[str]] = Field(None, alias="pinnedProductAsins", description="List of product ASINs include when dynamic.")
    product_asins: Optional[list[str]] = Field(None, alias="productAsins", description="List of product ASINs.")
    product_type: Optional[str] = Field(None, alias="productType", description="Type of products to display")
    search: Optional["StoreProductGridSearch"] = None
    show_only_markdown: Optional[bool] = Field(None, alias="showOnlyMarkdown", description="Whether to only show products on markdown.")
    sort: Optional[str] = Field(None, description="Sort order for products.")
    tag: Optional[str] = Field(None, description="Unique tag for the content.")
    title: Optional[str] = Field(None, description="Title of the product grid.")
    type_: Optional[str] = Field(None, alias="type", description="Type of the content.")

    model_config = {'populate_by_name': True}


class StoreProductGridWidget(BaseModel):
    common_properties: "CommonWidgetProperties" = Field(..., alias="commonProperties")
    content: "StoreProductGridContent"

    model_config = {'populate_by_name': True}


class StorePageWidget(BaseModel):
    """Union of all possible widget types that can be used on a store page"""
    pass


class StorePageTemplate(StrEnum):
    BLANK = "BLANK"
    HIGHLIGHT = "HIGHLIGHT"
    MARQUEE = "MARQUEE"
    PRODUCT_COLLECTION = "PRODUCT_COLLECTION"
    PRODUCT_GRID = "PRODUCT_GRID"


class StorePageContent(BaseModel):
    """Structure containing the content elements of a store page"""
    description: Optional[str] = Field(None, description="Description of the page")
    template: "StorePageTemplate"
    title: Optional[str] = Field(None, description="For store page, title of the page; for SB landing page, this can be optional")
    widgets: Optional[list["StorePageWidget"]] = Field(None, description="Collection of widgets displayed on the page")

    model_config = {'populate_by_name': True}


class BrandStorePage(BaseModel):
    content: "StorePageContent"
    edition_id: str = Field(..., alias="editionId", description="Reference to the store edition")
    page_id: str = Field(..., alias="pageId", description="Unique identifier for the store page")
    page_type: "StorePageType" = Field(..., alias="pageType")
    store_edition_publish_id: Optional[str] = Field(None, alias="storeEditionPublishId", description="Optional identifier for the published version of this page")
    store_id: str = Field(..., alias="storeId", description="Identifier of the associated store")

    model_config = {'populate_by_name': True}


class BrandStorePageBrandStoreEditionIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class BrandStorePageBrandStoreEditionPublishVersionIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class BrandStorePageBrandStoreIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class BrandStorePagePageIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class BrandStorePageSuccessResponse(BaseModel):
    brand_store_pages: Optional[list["BrandStorePage"]] = Field(None, alias="brandStorePages")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class BrandStoreStoreNameFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class BrandStoreSuccessResponse(BaseModel):
    brand_stores: Optional[list["BrandStore"]] = Field(None, alias="brandStores")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class BrandSuitabilityRiskLevelType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    HIGH = "HIGH"
    HIGH_MEDIUM = "HIGH_MEDIUM"
    HIGH_MEDIUM_LOW = "HIGH_MEDIUM_LOW"


class MarketplaceBudgetAllocation(StrEnum):
    AUTO = "AUTO"
    MANUAL = "MANUAL"


class RolloverStrategy(StrEnum):
    CUMULATIVE_BUDGET_ROLLOVER = "CUMULATIVE_BUDGET_ROLLOVER"
    NO_ROLLOVER = "NO_ROLLOVER"
    PRIOR_BUDGET_ROLLOVER = "PRIOR_BUDGET_ROLLOVER"


class OffAmazonBudgetControlStrategy(StrEnum):
    MAXIMIZE_REACH = "MAXIMIZE_REACH"
    MINIMIZE_SPEND = "MINIMIZE_SPEND"


class BudgetSettings(BaseModel):
    budget_allocation: Optional["BudgetAllocation"] = Field(None, alias="budgetAllocation")
    flight_budget_rollover_strategy: Optional["RolloverStrategy"] = Field(None, alias="flightBudgetRolloverStrategy")
    marketplace_budget_allocation: Optional["MarketplaceBudgetAllocation"] = Field(None, alias="marketplaceBudgetAllocation")
    off_amazon_budget_control_strategy: Optional["OffAmazonBudgetControlStrategy"] = Field(None, alias="offAmazonBudgetControlStrategy")

    model_config = {'populate_by_name': True}


class PrimaryInventoryType(StrEnum):
    AUDIO = "AUDIO"
    DISPLAY = "DISPLAY"
    VIDEO_OLV = "VIDEO_OLV"
    VIDEO_STV = "VIDEO_STV"


class TacticKey(BaseModel):
    """A tactic type paired with its compatible inventory type"""
    primary_inventory_type: "PrimaryInventoryType" = Field(..., alias="primaryInventoryType")
    tactic_type: "AutomatedTargetingTactic" = Field(..., alias="tacticType")

    model_config = {'populate_by_name': True}


class FlightBudget(BaseModel):
    budget_type: "BudgetType" = Field(..., alias="budgetType")
    budget_value: "BudgetValue" = Field(..., alias="budgetValue")

    model_config = {'populate_by_name': True}


class CampaignFlight(BaseModel):
    budget: "FlightBudget"
    end_date_time: str = Field(..., alias="endDateTime", description="The end date of the flight.")
    flight_id: Optional[str] = Field(None, alias="flightId", description="The ID associated with the flight.")
    name: Optional[str] = Field(None, description="The name of the flight.")
    start_date_time: str = Field(..., alias="startDateTime", description="The start date of the flight.")

    model_config = {'populate_by_name': True}


class SiteRestriction(StrEnum):
    AMAZON_BUSINESS = "AMAZON_BUSINESS"
    AMAZON_HAUL = "AMAZON_HAUL"


class Goal(StrEnum):
    AWARENESS = "AWARENESS"
    CONSIDERATION = "CONSIDERATION"
    CONVERSIONS = "CONVERSIONS"


class GoalSettings(BaseModel):
    currency_code: Optional["CurrencyCode"] = Field(None, alias="currencyCode")
    goal: "Goal"
    kpi: "KPI"
    kpi_value: Optional[float] = Field(None, alias="kpiValue", description="The value of the KPI that the campaign is working to optimize.")

    model_config = {'populate_by_name': True}


class CampaignOptimizations(BaseModel):
    bid_settings: Optional["BidSettings"] = Field(None, alias="bidSettings")
    budget_settings: Optional["BudgetSettings"] = Field(None, alias="budgetSettings")
    goal_settings: Optional["GoalSettings"] = Field(None, alias="goalSettings")
    primary_inventory_types: Optional[list["PrimaryInventoryType"]] = Field(None, alias="primaryInventoryTypes", description="Primary inventory type of the campaign for filtering KPIs and recommending tactics.")

    model_config = {'populate_by_name': True}


class IneligibleAutomatedTargetingTacticReasonCode(StrEnum):
    CONVERSION_SELECTIONS_EMPTY = "CONVERSION_SELECTIONS_EMPTY"
    CONVERSION_SELECTIONS_EXCEEDED = "CONVERSION_SELECTIONS_EXCEEDED"
    CONVERSION_SELECTIONS_MINIMUM_NOT_MET = "CONVERSION_SELECTIONS_MINIMUM_NOT_MET"
    NOT_ELIGIBLE_ADVERTISER = "NOT_ELIGIBLE_ADVERTISER"
    NOT_ELIGIBLE_GOAL = "NOT_ELIGIBLE_GOAL"
    NOT_ELIGIBLE_INVENTORY_TYPE = "NOT_ELIGIBLE_INVENTORY_TYPE"
    UNSUPPORTED_COUNTRY = "UNSUPPORTED_COUNTRY"


class IneligibleAutomatedTargetingTacticReason(BaseModel):
    """A single reason for tactic type ineligibility"""
    reason_code: "IneligibleAutomatedTargetingTacticReasonCode" = Field(..., alias="reasonCode")
    reason_message: str = Field(..., alias="reasonMessage", description="Human readable explanation of why this tactic type is ineligible")

    model_config = {'populate_by_name': True}


class IneligibleAutomatedTargetingTactic(BaseModel):
    """Information about an ineligible tactic key and the reasons for ineligibility"""
    reasons: Optional[list["IneligibleAutomatedTargetingTacticReason"]] = Field(None, description="List of reasons why this tactic key is ineligible")
    tactic_key: "TacticKey" = Field(..., alias="tacticKey")

    model_config = {'populate_by_name': True}


class CountryCode(StrEnum):
    AE = "AE"
    AT = "AT"
    AU = "AU"
    BE = "BE"
    BH = "BH"
    BR = "BR"
    CA = "CA"
    CH = "CH"
    DE = "DE"
    DK = "DK"
    EG = "EG"
    ES = "ES"
    FI = "FI"
    FR = "FR"
    GB = "GB"
    IE = "IE"
    IL = "IL"
    IN = "IN"
    IT = "IT"
    JO = "JO"
    JP = "JP"
    KW = "KW"
    LU = "LU"
    MA = "MA"
    MK = "MK"
    MX = "MX"
    NL = "NL"
    NO = "NO"
    NZ = "NZ"
    OM = "OM"
    PL = "PL"
    QA = "QA"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"
    ZA = "ZA"


class SalesChannel(StrEnum):
    AMAZON = "AMAZON"
    OFF_AMAZON = "OFF_AMAZON"


class CostType(StrEnum):
    CPC = "CPC"
    CPM = "CPM"
    FIXED_PRICE = "FIXED_PRICE"
    VCPM = "VCPM"


class CampaignFeeType(StrEnum):
    AGENCY = "AGENCY"


class CampaignFeeValueType(StrEnum):
    PERCENTAGE_OF_BUDGET = "PERCENTAGE_OF_BUDGET"


class CampaignFee(BaseModel):
    fee_type: "CampaignFeeType" = Field(..., alias="feeType")
    fee_value: float = Field(..., alias="feeValue", description="A service fee that is subtracted from the campaign budget as a percent of budget. This setting can’t be changed after an")
    fee_value_type: "CampaignFeeValueType" = Field(..., alias="feeValueType")

    model_config = {'populate_by_name': True}


class MarketplaceCampaignFieldOverrides(BaseModel):
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The end date time for the campaign")
    name: Optional[str] = Field(None, description="The name of the campaign")
    optimizations: Optional["CampaignOptimizations"] = None
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The start date time for the campaign")
    state: Optional["State"] = None
    tags: Optional[list["Tag"]] = Field(None, description="Open ended labels with a key value pair applied to the campaign")

    model_config = {'populate_by_name': True}


class MarketplaceCampaignConfigurations(BaseModel):
    campaign_id: str = Field(..., alias="campaignId", description="Represents marketplace campaign id (Ex: campaignId-US) associated to global campaign (Ex: campaignId-Global)")
    marketplace: "Marketplace"
    overrides: "MarketplaceCampaignFieldOverrides"

    model_config = {'populate_by_name': True}


class Campaign(BaseModel):
    ad_product: "AdProduct" = Field(..., alias="adProduct")
    adomains: Optional[list[str]] = Field(None, description="OpenRTB standard naming meaning: Advertiser domain for block list checking. This can be an array of strings for the case")
    auto_creation_settings: Optional["AutoCreationSettings"] = Field(None, alias="autoCreationSettings")
    auto_scale_global_campaign: Optional["AutoScaleGlobalCampaignSetting"] = Field(None, alias="autoScaleGlobalCampaign")
    brand_id: Optional[str] = Field(None, alias="brandId", description="This is the ID of the brand that the campaign is associated with.")
    budgets: Optional[list["Budget"]] = Field(None, description="The object containing budget details for the campaign (for campaigns that support multiple budgets).")
    campaign_id: str = Field(..., alias="campaignId", description="A unique identifier for a campaign.")
    cost_type: Optional["CostType"] = Field(None, alias="costType")
    countries: Optional[list["CountryCode"]] = Field(None, description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries fiel")
    creation_date_time: str = Field(..., alias="creationDateTime", description="The date time that the campaign was created.")
    eligible_automated_targeting_tactics: Optional[list["TacticKey"]] = Field(None, alias="eligibleAutomatedTargetingTactics", description="List of tactic type and inventory type pairs that are eligible for use with this campaign")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The end date time for the campaign.")
    fees: Optional[list["CampaignFee"]] = Field(None, description="Any fees associated with the campaign.")
    flights: Optional[list["CampaignFlight"]] = Field(None, description="Flight details associated with the campaign.")
    frequencies: Optional[list["Frequency"]] = Field(None, description="Any frequency caps associated with the campaign.")
    global_campaign_id: Optional[str] = Field(None, alias="globalCampaignId", description="The global campaign identifier that manages this marketplace campaign.")
    ineligible_automated_targeting_tactics: Optional[list["IneligibleAutomatedTargetingTactic"]] = Field(None, alias="ineligibleAutomatedTargetingTactics", description="List of tactic type and inventory type pairs that are ineligible for use with this campaign, along with reasons for inel")
    is_multi_ad_groups_enabled: Optional[bool] = Field(None, alias="isMultiAdGroupsEnabled", description="A read-only field that indicates whether a campaign supports multiple adGroups.")
    last_updated_date_time: str = Field(..., alias="lastUpdatedDateTime", description="The date time that the campaign was last updated.")
    marketplace_configurations: Optional[list["MarketplaceCampaignConfigurations"]] = Field(None, alias="marketplaceConfigurations", description="List of marketplace-specific configurations for a global campaign that enables overriding certain attributes at individu")
    marketplace_scope: Optional["MarketplaceScope"] = Field(None, alias="marketplaceScope")
    marketplaces: Optional[list["Marketplace"]] = Field(None, description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an")
    name: str = Field(..., description="The name of the campaign.")
    optimizations: Optional["CampaignOptimizations"] = None
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="The ID of the portfolio associated with the campaign.")
    purchase_order_number: Optional[str] = Field(None, alias="purchaseOrderNumber", description="The purchase order number associated with the campaign.")
    sales_channel: Optional["SalesChannel"] = Field(None, alias="salesChannel")
    site_restrictions: Optional[list["SiteRestriction"]] = Field(None, alias="siteRestrictions", description="Restrict the ad to a particular site")
    skan_app_id: Optional[str] = Field(None, alias="skanAppId", description="StoreKit AdNetwork application ID. Represents iTunes application ID with which SKAN-enabled campaigns are associated.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The start date time for the campaign.")
    state: "State"
    status: Optional["Status"] = None
    tags: Optional[list["Tag"]] = Field(None, description="Open ended labels with a key value pair applied to the campaign")
    targeted_pg_deal_id: Optional[str] = Field(None, alias="targetedPGDealId", description="DealId associated with the campaign.")
    targets_amazon_deal: Optional[bool] = Field(None, alias="targetsAmazonDeal", description="If the campaign is targeting an Amazon deal, the value will be true, and the campaign and ad group(s) will be read-only.")

    model_config = {'populate_by_name': True}


class CampaignAdProductFilter(BaseModel):
    include: list["AdProduct"] = Field(..., description="| AdProduct | Description | | --- | --- | | `SPONSORED_PRODUCTS` | Sponsored Products ad product. | | `SPONSORED_BRANDS`")

    model_config = {'populate_by_name': True}


class CampaignCampaignIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class CreateAutoCreationSettings(BaseModel):
    auto_create_targets: Optional[bool] = Field(None, alias="autoCreateTargets", description="Gives Amazon permission to automatically create targets associated with the campaign based on the products being adverti")
    auto_manage_campaign: Optional[bool] = Field(None, alias="autoManageCampaign", description="Flag that allows Amazon to manage the lifecycle of your Campaign.")

    model_config = {'populate_by_name': True}


class CreateFlightBudget(BaseModel):
    budget_type: "BudgetType" = Field(..., alias="budgetType")
    budget_value: "CreateBudgetValue" = Field(..., alias="budgetValue")

    model_config = {'populate_by_name': True}


class CreateCampaignFlight(BaseModel):
    budget: "CreateFlightBudget"
    end_date_time: str = Field(..., alias="endDateTime", description="The end date of the flight.")
    flight_id: Optional[str] = Field(None, alias="flightId", description="The ID associated with the flight.")
    name: Optional[str] = Field(None, description="The name of the flight.")
    start_date_time: str = Field(..., alias="startDateTime", description="The start date of the flight.")

    model_config = {'populate_by_name': True}


class CreateCampaignFee(BaseModel):
    fee_type: "CampaignFeeType" = Field(..., alias="feeType")
    fee_value: float = Field(..., alias="feeValue", description="A service fee that is subtracted from the campaign budget as a percent of budget. This setting can’t be changed after an")
    fee_value_type: "CampaignFeeValueType" = Field(..., alias="feeValueType")

    model_config = {'populate_by_name': True}


class CreateCreativeBidAdjustment(BaseModel):
    creative_type: Optional["CreativeBidAdjustmentType"] = Field(None, alias="creativeType")
    percentage: int = Field(..., description="The selection of the percentage change associated with the creative type and bid adjustment settings.")

    model_config = {'populate_by_name': True}


class CreateShopperSegmentBidAdjustment(BaseModel):
    pass


class CreateAudienceBidAdjustment(BaseModel):
    audience_id: str = Field(..., alias="audienceId", description="The unique identifier of the Audience to apply bid adjustment.")
    percentage: int = Field(..., description="The selection of the percentage change associated with a given audience and bid adjustment settings.")

    model_config = {'populate_by_name': True}


class CreatePlacementBidAdjustment(BaseModel):
    percentage: int = Field(..., description="The selection of the percentage change associated with a given placement and bid adjustment settings.")
    placement: "Placement"

    model_config = {'populate_by_name': True}


class CreateBidAdjustments(BaseModel):
    audience_bid_adjustments: Optional[list["CreateAudienceBidAdjustment"]] = Field(None, alias="audienceBidAdjustments", description="Bid Adjustments based on the audiences")
    creative_bid_adjustments: Optional[list["CreateCreativeBidAdjustment"]] = Field(None, alias="creativeBidAdjustments", description="Bid Adjustments based on ads being shown as a creative. Range of bid adjustment value would be 0:900")
    placement_bid_adjustments: Optional[list["CreatePlacementBidAdjustment"]] = Field(None, alias="placementBidAdjustments", description="Bid adjustments based on ad placements.")
    shopper_segment_bid_adjustments: Optional[list["CreateShopperSegmentBidAdjustment"]] = Field(None, alias="shopperSegmentBidAdjustments", description="Legacy SB field (marked for deprecation)")

    model_config = {'populate_by_name': True}


class CreateBidSettings(BaseModel):
    bid_adjustments: Optional["CreateBidAdjustments"] = Field(None, alias="bidAdjustments")
    bid_strategy: Optional["BidStrategy"] = Field(None, alias="bidStrategy")

    model_config = {'populate_by_name': True}


class CreateGoalSettings(BaseModel):
    kpi: "KPI"
    kpi_value: Optional[float] = Field(None, alias="kpiValue", description="The value of the KPI that the campaign is working to optimize.")

    model_config = {'populate_by_name': True}


class CreateBudgetSettings(BaseModel):
    budget_allocation: Optional["BudgetAllocation"] = Field(None, alias="budgetAllocation")
    flight_budget_rollover_strategy: Optional["RolloverStrategy"] = Field(None, alias="flightBudgetRolloverStrategy")
    off_amazon_budget_control_strategy: Optional["OffAmazonBudgetControlStrategy"] = Field(None, alias="offAmazonBudgetControlStrategy")

    model_config = {'populate_by_name': True}


class CreateCampaignOptimizations(BaseModel):
    bid_settings: Optional["CreateBidSettings"] = Field(None, alias="bidSettings")
    budget_settings: Optional["CreateBudgetSettings"] = Field(None, alias="budgetSettings")
    goal_settings: Optional["CreateGoalSettings"] = Field(None, alias="goalSettings")
    primary_inventory_types: Optional[list["PrimaryInventoryType"]] = Field(None, alias="primaryInventoryTypes", description="Primary inventory type of the campaign for filtering KPIs and recommending tactics.")

    model_config = {'populate_by_name': True}


class CreateMarketplaceCampaignFieldOverrides(BaseModel):
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The end date time for the campaign")
    name: Optional[str] = Field(None, description="The name of the campaign")
    optimizations: Optional["CreateCampaignOptimizations"] = None
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The start date time for the campaign")
    state: Optional["State"] = None
    tags: Optional[list["CreateTag"]] = Field(None, description="Open ended labels with a key value pair applied to the campaign")

    model_config = {'populate_by_name': True}


class CreateMarketplaceCampaignConfigurations(BaseModel):
    marketplace: "Marketplace"
    overrides: "CreateMarketplaceCampaignFieldOverrides"

    model_config = {'populate_by_name': True}


class CampaignCreate(BaseModel):
    ad_product: "AdProduct" = Field(..., alias="adProduct")
    adomains: Optional[list[str]] = Field(None, description="OpenRTB standard naming meaning: Advertiser domain for block list checking. This can be an array of strings for the case")
    auto_creation_settings: Optional["CreateAutoCreationSettings"] = Field(None, alias="autoCreationSettings")
    brand_id: Optional[str] = Field(None, alias="brandId", description="This is the ID of the brand that the campaign is associated with.")
    budgets: Optional[list["CreateBudget"]] = Field(None, description="The object containing budget details for the campaign (for campaigns that support multiple budgets).")
    cost_type: Optional["CostType"] = Field(None, alias="costType")
    countries: Optional[list["CountryCode"]] = Field(None, description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries fiel")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The end date time for the campaign.")
    fees: Optional[list["CreateCampaignFee"]] = Field(None, description="Any fees associated with the campaign.")
    flights: Optional[list["CreateCampaignFlight"]] = Field(None, description="Flight details associated with the campaign.")
    frequencies: Optional[list["CreateFrequency"]] = Field(None, description="Any frequency caps associated with the campaign.")
    marketplace_configurations: Optional[list["CreateMarketplaceCampaignConfigurations"]] = Field(None, alias="marketplaceConfigurations", description="List of marketplace-specific configurations for a global campaign that enables overriding certain attributes at individu")
    marketplace_scope: Optional["MarketplaceScope"] = Field(None, alias="marketplaceScope")
    marketplaces: Optional[list["Marketplace"]] = Field(None, description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an")
    name: str = Field(..., description="The name of the campaign.")
    optimizations: Optional["CreateCampaignOptimizations"] = None
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="The ID of the portfolio associated with the campaign.")
    purchase_order_number: Optional[str] = Field(None, alias="purchaseOrderNumber", description="The purchase order number associated with the campaign.")
    sales_channel: Optional["SalesChannel"] = Field(None, alias="salesChannel")
    site_restrictions: Optional[list["SiteRestriction"]] = Field(None, alias="siteRestrictions", description="Restrict the ad to a particular site")
    skan_app_id: Optional[str] = Field(None, alias="skanAppId", description="StoreKit AdNetwork application ID. Represents iTunes application ID with which SKAN-enabled campaigns are associated.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The start date time for the campaign.")
    state: "CreateState"
    tags: Optional[list["CreateTag"]] = Field(None, description="Open ended labels with a key value pair applied to the campaign")
    targeted_pg_deal_id: Optional[str] = Field(None, alias="targetedPGDealId", description="DealId associated with the campaign.")

    model_config = {'populate_by_name': True}


class CampaignGoalFilter(BaseModel):
    include: list["Goal"] = Field(..., description="| Goal | Description | | --- | --- | | `AWARENESS` | Indicates a goal of driving awareness. | | `CONSIDERATION` | Indica")

    model_config = {'populate_by_name': True}


class CampaignMarketplaceScopeFilter(BaseModel):
    include: list["MarketplaceScope"] = Field(..., description="| MarketplaceScope | Description | | --- | --- | | `GLOBAL` |  | | `SINGLE_MARKETPLACE` |  |")

    model_config = {'populate_by_name': True}


class CampaignMultiStatusSuccess(BaseModel):
    campaign: "Campaign"
    index: int

    model_config = {'populate_by_name': True}


class CampaignPartialIndex(BaseModel):
    campaign: "Campaign"
    errors: list["Error"]
    index: int

    model_config = {'populate_by_name': True}


class CampaignMultiStatusResponseWithPartialErrors(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    partial_success: Optional[list["CampaignPartialIndex"]] = Field(None, alias="partialSuccess")
    success: Optional[list["CampaignMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class CampaignNameFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class CampaignNameFilter(BaseModel):
    include: list[str]
    query_term_match_type: "CampaignNameFilterType" = Field(..., alias="queryTermMatchType")

    model_config = {'populate_by_name': True}


class CampaignPortfolioIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class CampaignStateFilter(BaseModel):
    include: list["State"] = Field(..., description="| State | Description | | --- | --- | | `ENABLED` | The object is set active by user and eligible for delivery. | | `PAU")

    model_config = {'populate_by_name': True}


class CampaignSuccessResponse(BaseModel):
    campaigns: Optional[list["Campaign"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class UpdateGoalSettings(BaseModel):
    kpi: Optional["KPI"] = None
    kpi_value: Optional[float] = Field(None, alias="kpiValue", description="The value of the KPI that the campaign is working to optimize.")

    model_config = {'populate_by_name': True}


class UpdateBidAdjustments(BaseModel):
    audience_bid_adjustments: Optional[list["CreateAudienceBidAdjustment"]] = Field(None, alias="audienceBidAdjustments", description="Bid Adjustments based on the audiences")
    creative_bid_adjustments: Optional[list["CreateCreativeBidAdjustment"]] = Field(None, alias="creativeBidAdjustments", description="Bid Adjustments based on ads being shown as a creative. Range of bid adjustment value would be 0:900")
    placement_bid_adjustments: Optional[list["CreatePlacementBidAdjustment"]] = Field(None, alias="placementBidAdjustments", description="Bid adjustments based on ad placements.")
    shopper_segment_bid_adjustments: Optional[list["CreateShopperSegmentBidAdjustment"]] = Field(None, alias="shopperSegmentBidAdjustments", description="Legacy SB field (marked for deprecation)")

    model_config = {'populate_by_name': True}


class UpdateBidSettings(BaseModel):
    bid_adjustments: Optional["UpdateBidAdjustments"] = Field(None, alias="bidAdjustments")
    bid_strategy: Optional["BidStrategy"] = Field(None, alias="bidStrategy")

    model_config = {'populate_by_name': True}


class UpdateBudgetSettings(BaseModel):
    budget_allocation: Optional["BudgetAllocation"] = Field(None, alias="budgetAllocation")
    flight_budget_rollover_strategy: Optional["RolloverStrategy"] = Field(None, alias="flightBudgetRolloverStrategy")
    off_amazon_budget_control_strategy: Optional["OffAmazonBudgetControlStrategy"] = Field(None, alias="offAmazonBudgetControlStrategy")

    model_config = {'populate_by_name': True}


class UpdateCampaignOptimizations(BaseModel):
    bid_settings: Optional["UpdateBidSettings"] = Field(None, alias="bidSettings")
    budget_settings: Optional["UpdateBudgetSettings"] = Field(None, alias="budgetSettings")
    goal_settings: Optional["UpdateGoalSettings"] = Field(None, alias="goalSettings")
    primary_inventory_types: Optional[list["PrimaryInventoryType"]] = Field(None, alias="primaryInventoryTypes", description="Primary inventory type of the campaign for filtering KPIs and recommending tactics.")

    model_config = {'populate_by_name': True}


class CampaignUpdate(BaseModel):
    ad_product: Optional["AdProduct"] = Field(None, alias="adProduct")
    adomains: Optional[list[str]] = Field(None, description="OpenRTB standard naming meaning: Advertiser domain for block list checking. This can be an array of strings for the case")
    budgets: Optional[list["CreateBudget"]] = Field(None, description="The object containing budget details for the campaign (for campaigns that support multiple budgets).")
    campaign_id: str = Field(..., alias="campaignId", description="A unique identifier for a campaign.")
    cost_type: Optional["CostType"] = Field(None, alias="costType")
    countries: Optional[list["CountryCode"]] = Field(None, description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries fiel")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The end date time for the campaign.")
    fees: Optional[list["CreateCampaignFee"]] = Field(None, description="Any fees associated with the campaign.")
    flights: Optional[list["CreateCampaignFlight"]] = Field(None, description="Flight details associated with the campaign.")
    frequencies: Optional[list["CreateFrequency"]] = Field(None, description="Any frequency caps associated with the campaign.")
    marketplace_configurations: Optional[list["CreateMarketplaceCampaignConfigurations"]] = Field(None, alias="marketplaceConfigurations", description="List of marketplace-specific configurations for a global campaign that enables overriding certain attributes at individu")
    marketplaces: Optional[list["Marketplace"]] = Field(None, description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an")
    name: Optional[str] = Field(None, description="The name of the campaign.")
    optimizations: Optional["UpdateCampaignOptimizations"] = None
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="The ID of the portfolio associated with the campaign.")
    purchase_order_number: Optional[str] = Field(None, alias="purchaseOrderNumber", description="The purchase order number associated with the campaign.")
    site_restrictions: Optional[list["SiteRestriction"]] = Field(None, alias="siteRestrictions", description="Restrict the ad to a particular site")
    skan_app_id: Optional[str] = Field(None, alias="skanAppId", description="StoreKit AdNetwork application ID. Represents iTunes application ID with which SKAN-enabled campaigns are associated.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The start date time for the campaign.")
    state: Optional["UpdateState"] = None
    tags: Optional[list["CreateTag"]] = Field(None, description="Open ended labels with a key value pair applied to the campaign")
    targeted_pg_deal_id: Optional[str] = Field(None, alias="targetedPGDealId", description="DealId associated with the campaign.")

    model_config = {'populate_by_name': True}


class ConstituentIndexValue(BaseModel):
    """Values for a location index where the indexValue is calculated from the constituents."""
    brand_sales: float = Field(..., alias="brandSales", description="The brand sales value for the postal code.")
    category_sales: float = Field(..., alias="categorySales", description="The category sales value for the postal code.")
    postal_code: str = Field(..., alias="postalCode", description="The postal code for the location index prefixed by country code (i.e. US-10118).")

    model_config = {'populate_by_name': True}


class ConstituentIndexValues(BaseModel):
    values: list["ConstituentIndexValue"] = Field(..., description="List of brand and category sales values.")

    model_config = {'populate_by_name': True}


class ContentCategoryTarget(BaseModel):
    """Target based on the category of content being viewed."""
    content_category_id: str = Field(..., alias="contentCategoryId", description="The content category being targeted.")

    model_config = {'populate_by_name': True}


class ContentGenre(StrEnum):
    ACTION = "ACTION"
    ADVENTURE = "ADVENTURE"
    ALTERNATIVE_ROCK = "ALTERNATIVE_ROCK"
    ANIMATION = "ANIMATION"
    ARTS = "ARTS"
    BIOGRAPHY = "BIOGRAPHY"
    BLUES = "BLUES"
    BUSINESS = "BUSINESS"
    CHILDRENS_MUSIC = "CHILDRENS_MUSIC"
    CHRISTIAN_GOSPEL = "CHRISTIAN_GOSPEL"
    CHRISTMAS_HOLIDAY = "CHRISTMAS_HOLIDAY"
    CLASSICAL = "CLASSICAL"
    CLASSIC_ROCK = "CLASSIC_ROCK"
    COLLEGE_RADIO = "COLLEGE_RADIO"
    COMEDY = "COMEDY"
    COUNTRY = "COUNTRY"
    CRIME = "CRIME"
    DANCE_DJ = "DANCE_DJ"
    DOCUMENTARY = "DOCUMENTARY"
    DRAMA = "DRAMA"
    EASY_LISTENING = "EASY_LISTENING"
    EDUCATION = "EDUCATION"
    EUROPEAN_POP_FOLK = "EUROPEAN_POP_FOLK"
    FAMILY = "FAMILY"
    FANTASY = "FANTASY"
    FICTION = "FICTION"
    FILM_NOIR = "FILM_NOIR"
    FOLK = "FOLK"
    FRENCH_VARIETY = "FRENCH_VARIETY"
    GAME_SHOW = "GAME_SHOW"
    GENRE_NOT_AVAILABLE = "GENRE_NOT_AVAILABLE"
    GERMAN_ROCK_POP = "GERMAN_ROCK_POP"
    GOVERNMENT = "GOVERNMENT"
    HARD_ROCK_METAL = "HARD_ROCK_METAL"
    HEALTH_AND_FITNESS = "HEALTH_AND_FITNESS"
    HISTORY = "HISTORY"
    HORROR = "HORROR"
    INTERNATIONAL = "INTERNATIONAL"
    JAPANESE = "JAPANESE"
    JAZZ = "JAZZ"
    KIDS_AND_FAMILY = "KIDS_AND_FAMILY"
    LATIN_MUSIC = "LATIN_MUSIC"
    LEISURE = "LEISURE"
    MISCELLANEOUS = "MISCELLANEOUS"
    MUSIC = "MUSIC"
    MUSICAL = "MUSICAL"
    MUSICALS_CABARET = "MUSICALS_CABARET"
    MYSTERY = "MYSTERY"
    NEWS = "NEWS"
    NEW_AGE = "NEW_AGE"
    OLDIES_ADULT_STANDARDS = "OLDIES_ADULT_STANDARDS"
    POP = "POP"
    RAP_HIP_HOP = "RAP_HIP_HOP"
    RB = "RB"
    REALITY_TV = "REALITY_TV"
    REGGAE_ISLAND = "REGGAE_ISLAND"
    RELIGION_AND_SPIRITUALITY = "RELIGION_AND_SPIRITUALITY"
    ROCK = "ROCK"
    ROMANCE = "ROMANCE"
    SCIENCE = "SCIENCE"
    SCIENCE_FICTION = "SCIENCE_FICTION"
    SHORT = "SHORT"
    SOCIETY_AND_CULTURE = "SOCIETY_AND_CULTURE"
    SOUNDTRACKS = "SOUNDTRACKS"
    SPORT = "SPORT"
    SUPER_HERO = "SUPER_HERO"
    TALK_SHOW = "TALK_SHOW"
    TECHNOLOGY = "TECHNOLOGY"
    THRILLER = "THRILLER"
    TRUE_CRIME = "TRUE_CRIME"
    TV_AND_FILM = "TV_AND_FILM"
    WAR = "WAR"
    WESTERN = "WESTERN"


class ContentGenreTarget(BaseModel):
    """Target based on the genre of content being viewed."""
    content_genre: "ContentGenre" = Field(..., alias="contentGenre")

    model_config = {'populate_by_name': True}


class ContentInstreamPosition(StrEnum):
    MID_ROLL = "MID_ROLL"
    POST_ROLL = "POST_ROLL"
    PRE_ROLL = "PRE_ROLL"
    UNKNOWN = "UNKNOWN"


class ContentInstreamPositionTarget(BaseModel):
    """Targets ads in the specified content instream position"""
    instream_position: "ContentInstreamPosition" = Field(..., alias="instreamPosition")

    model_config = {'populate_by_name': True}


class ContentOutstreamPosition(StrEnum):
    ACCOMPANYING_CONTENT = "ACCOMPANYING_CONTENT"
    INTERSTITIAL = "INTERSTITIAL"
    STANDALONE = "STANDALONE"
    UNKNOWN = "UNKNOWN"


class ContentOutstreamPositionTarget(BaseModel):
    """Targets ads in the specified content outstream position"""
    outstream_position: "ContentOutstreamPosition" = Field(..., alias="outstreamPosition")

    model_config = {'populate_by_name': True}


class TwitchContentRatingEnum(StrEnum):
    TWITCH_MODERATE = "TWITCH_MODERATE"
    TWITCH_RESTRICTIVE = "TWITCH_RESTRICTIVE"


class TwitchContentRating(BaseModel):
    twitch_content_rating: "TwitchContentRatingEnum" = Field(..., alias="twitchContentRating")

    model_config = {'populate_by_name': True}


class DspContentRatingEnum(StrEnum):
    RATING_NOT_AVAILABLE = "RATING_NOT_AVAILABLE"
    SUITABLE_FOR_ADULTS = "SUITABLE_FOR_ADULTS"
    SUITABLE_FOR_ALL_AUDIENCES = "SUITABLE_FOR_ALL_AUDIENCES"
    SUITABLE_FOR_MATURE_AUDIENCES = "SUITABLE_FOR_MATURE_AUDIENCES"
    SUITABLE_FOR_MOST_AUDIENCES_WITH_PARENTAL_GUIDANCE = "SUITABLE_FOR_MOST_AUDIENCES_WITH_PARENTAL_GUIDANCE"
    SUITABLE_FOR_TEEN_AND_OLDER_AUDIENCES = "SUITABLE_FOR_TEEN_AND_OLDER_AUDIENCES"


class DspContentRating(BaseModel):
    dsp_content_rating: "DspContentRatingEnum" = Field(..., alias="dspContentRating")

    model_config = {'populate_by_name': True}


class ContentRating(BaseModel):
    pass


class ContentRatingTypes(StrEnum):
    DSP_CONTENT_RATING = "DSP_CONTENT_RATING"
    TWITCH_CONTENT_RATING = "TWITCH_CONTENT_RATING"


class ContentRatingTarget(BaseModel):
    """Target based on the rating of content being viewed."""
    content_rating_type: "ContentRatingTypes" = Field(..., alias="contentRatingType")
    content_rating_type_details: "ContentRating" = Field(..., alias="contentRatingTypeDetails")

    model_config = {'populate_by_name': True}


class ContentTooLargeResponseContent(BaseModel):
    code: "ErrorCode"
    message: str

    model_config = {'populate_by_name': True}


class CreateAdAssociationRequest(BaseModel):
    ad_associations: Optional[list["AdAssociationCreate"]] = Field(None, alias="adAssociations")

    model_config = {'populate_by_name': True}


class CreateAdExtensionRequest(BaseModel):
    ad_extensions: Optional[list["AdExtensionCreate"]] = Field(None, alias="adExtensions")

    model_config = {'populate_by_name': True}


class CreateAdGroupRequest(BaseModel):
    ad_groups: Optional[list["AdGroupCreate"]] = Field(None, alias="adGroups")

    model_config = {'populate_by_name': True}


class CreateAdInitiationTarget(BaseModel):
    """Target based on how the video ad will be started."""
    video_initiation_type: "VideoInitiationType" = Field(..., alias="videoInitiationType")

    model_config = {'populate_by_name': True}


class CreateAdPlayerSizeTarget(BaseModel):
    """Target based on the size of the ad player."""
    ad_player_size: "AdPlayerSize" = Field(..., alias="adPlayerSize")

    model_config = {'populate_by_name': True}


class CreateAdRequest(BaseModel):
    ads: Optional[list["AdCreate"]] = None

    model_config = {'populate_by_name': True}


class CreateAdvertiserDomainList(BaseModel):
    """Targets domains based on list inherited from the advertiser."""
    inherit_from_advertiser: bool = Field(..., alias="inheritFromAdvertiser", description="Set to TRUE to inherit domain list from advertiser.")

    model_config = {'populate_by_name': True}


class CreateAppTarget(BaseModel):
    """Target based on user application."""
    app_id: str = Field(..., alias="appId", description="The app identifier being targeted.")
    app_type: "AppType" = Field(..., alias="appType")

    model_config = {'populate_by_name': True}


class CreateMarketplaceStringValue(BaseModel):
    default_value: Optional[str] = Field(None, alias="defaultValue", description="The default value. Either the default value or the marketplace settings should always be specified")

    model_config = {'populate_by_name': True}


class CreateAudienceTarget(BaseModel):
    """Target based on a specified audience ID."""
    across_group_operator: Optional["AcrossGroupOperator"] = Field(None, alias="acrossGroupOperator")
    audience_id: "CreateMarketplaceStringValue" = Field(..., alias="audienceId")
    group_id: Optional[str] = Field(None, alias="groupId", description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences")
    in_group_operator: Optional["InGroupOperator"] = Field(None, alias="inGroupOperator")

    model_config = {'populate_by_name': True}


class CreateBrandSafetyCategoryTarget(BaseModel):
    """Target based on, if any, the classifications of unsuitable contexts that may pose a risk to a brand's reputation of content being viewed."""
    brand_safety_category: "BrandSafetyCategory" = Field(..., alias="brandSafetyCategory")

    model_config = {'populate_by_name': True}


class CreateBrandSafetyTierTarget(BaseModel):
    """Target based on the brand suitability risk levels of content being viewed."""
    brand_safety_tier: "BrandSafetyTier" = Field(..., alias="brandSafetyTier")

    model_config = {'populate_by_name': True}


class CreateCampaignRequest(BaseModel):
    campaigns: Optional[list["CampaignCreate"]] = None

    model_config = {'populate_by_name': True}


class CreateConstituentIndexValue(BaseModel):
    """Values for a location index where the indexValue is calculated from the constituents."""
    brand_sales: float = Field(..., alias="brandSales", description="The brand sales value for the postal code.")
    category_sales: float = Field(..., alias="categorySales", description="The category sales value for the postal code.")
    postal_code: str = Field(..., alias="postalCode", description="The postal code for the location index prefixed by country code (i.e. US-10118).")

    model_config = {'populate_by_name': True}


class CreateConstituentIndexValues(BaseModel):
    values: list["CreateConstituentIndexValue"] = Field(..., description="List of brand and category sales values.")

    model_config = {'populate_by_name': True}


class CreateContentCategoryTarget(BaseModel):
    """Target based on the category of content being viewed."""
    content_category_id: str = Field(..., alias="contentCategoryId", description="The content category being targeted.")

    model_config = {'populate_by_name': True}


class CreateContentGenreTarget(BaseModel):
    """Target based on the genre of content being viewed."""
    content_genre: "ContentGenre" = Field(..., alias="contentGenre")

    model_config = {'populate_by_name': True}


class CreateContentInstreamPositionTarget(BaseModel):
    """Targets ads in the specified content instream position"""
    instream_position: "ContentInstreamPosition" = Field(..., alias="instreamPosition")

    model_config = {'populate_by_name': True}


class CreateContentOutstreamPositionTarget(BaseModel):
    """Targets ads in the specified content outstream position"""
    outstream_position: "ContentOutstreamPosition" = Field(..., alias="outstreamPosition")

    model_config = {'populate_by_name': True}


class CreateTwitchContentRating(BaseModel):
    twitch_content_rating: "TwitchContentRatingEnum" = Field(..., alias="twitchContentRating")

    model_config = {'populate_by_name': True}


class CreateDspContentRating(BaseModel):
    dsp_content_rating: "DspContentRatingEnum" = Field(..., alias="dspContentRating")

    model_config = {'populate_by_name': True}


class CreateContentRating(BaseModel):
    pass


class CreateContentRatingTarget(BaseModel):
    """Target based on the rating of content being viewed."""
    content_rating_type: "ContentRatingTypes" = Field(..., alias="contentRatingType")
    content_rating_type_details: "CreateContentRating" = Field(..., alias="contentRatingTypeDetails")

    model_config = {'populate_by_name': True}


class CreateDVBrandSafetyContentCategoriesWithRiskMap(BaseModel):
    """A map from content categories to risk level to exclude from targeting. Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISAS"""
    key: str = Field(..., description="Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATUR")
    value: "BrandSuitabilityRiskLevelType"

    model_config = {'populate_by_name': True}


class CreateTimeOfDay(BaseModel):
    end_time: str = Field(..., alias="endTime", description="Selected end time")
    start_time: str = Field(..., alias="startTime", description="Selected start time")

    model_config = {'populate_by_name': True}


class DayOfWeek(StrEnum):
    FRIDAY = "FRIDAY"
    MONDAY = "MONDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"
    THURSDAY = "THURSDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"


class CreateDayPartTarget(BaseModel):
    """Target based on time of day."""
    day_of_week: "DayOfWeek" = Field(..., alias="dayOfWeek")
    time_of_day: "CreateTimeOfDay" = Field(..., alias="timeOfDay")

    model_config = {'populate_by_name': True}


class DeviceOrientation(StrEnum):
    LANDSCAPE = "LANDSCAPE"
    PORTRAIT = "PORTRAIT"


class MobileEnvironment(StrEnum):
    APP = "APP"
    WEB = "WEB"


class MobileOs(StrEnum):
    ANDROID = "ANDROID"
    IOS = "IOS"


class DeviceType(StrEnum):
    CONNECTED_DEVICE = "CONNECTED_DEVICE"
    CONNECTED_TV = "CONNECTED_TV"
    DESKTOP = "DESKTOP"
    MOBILE = "MOBILE"


class MobileDevice(StrEnum):
    ANDROID = "ANDROID"
    IPAD = "IPAD"
    IPHONE = "IPHONE"
    KINDLE_FIRE = "KINDLE_FIRE"
    KINDLE_FIRE_HD = "KINDLE_FIRE_HD"


class CreateDeviceTarget(BaseModel):
    """Target based on user device."""
    device_orientation: Optional["DeviceOrientation"] = Field(None, alias="deviceOrientation")
    device_type: "DeviceType" = Field(..., alias="deviceType")
    mobile_device: Optional["MobileDevice"] = Field(None, alias="mobileDevice")
    mobile_environment: Optional["MobileEnvironment"] = Field(None, alias="mobileEnvironment")
    mobile_os: Optional["MobileOs"] = Field(None, alias="mobileOs")

    model_config = {'populate_by_name': True}


class CreateDirectIndexValue(BaseModel):
    """Values for a location index where the indexValue is the pre-calculated index."""
    index_value: float = Field(..., alias="indexValue", description="The pre-calculated index value.")
    postal_code: str = Field(..., alias="postalCode", description="The postal code for the location index prefixed by country code (i.e. US-10118).")

    model_config = {'populate_by_name': True}


class CreateDirectIndexValues(BaseModel):
    values: list["CreateDirectIndexValue"] = Field(..., description="List of direct index values.")

    model_config = {'populate_by_name': True}


class CreateDomainFileTarget(BaseModel):
    """Targets domains based on list provided via file upload."""
    domain_file_key: str = Field(..., alias="domainFileKey", description="The S3 key of the uploaded file which can be obtained from the file upload policy endpoint. A max of 10 files may be ass")
    domain_file_name: str = Field(..., alias="domainFileName", description="The name of the file.")

    model_config = {'populate_by_name': True}


class CreateDomainListTarget(BaseModel):
    """Targets domains based on an existing domain list."""
    domain_list_id: str = Field(..., alias="domainListId", description="The ID of the domain list to target.")

    model_config = {'populate_by_name': True}


class CreateDomainNameTarget(BaseModel):
    """Targets domains based on URL."""
    domain_name: str = Field(..., alias="domainName", description="The URL of the domain to target.")

    model_config = {'populate_by_name': True}


class DomainTargetTypes(StrEnum):
    ADVERTISER_DOMAIN_LIST = "ADVERTISER_DOMAIN_LIST"
    DOMAIN_FILE = "DOMAIN_FILE"
    DOMAIN_LIST = "DOMAIN_LIST"
    DOMAIN_NAME = "DOMAIN_NAME"


class CreateDomainTargetDetails(BaseModel):
    pass


class CreateDomainTarget(BaseModel):
    """Target based on a specified domain."""
    domain_target_details: "CreateDomainTargetDetails" = Field(..., alias="domainTargetDetails")
    domain_target_type: "DomainTargetTypes" = Field(..., alias="domainTargetType")

    model_config = {'populate_by_name': True}


class CreateDoubleVerifyAuthenticAttention(BaseModel):
    universal_attention: bool = Field(..., alias="universalAttention", description="One omni-channel segment that is informed by data from all DV campaigns to help avoid serving ads on generally poor perf")

    model_config = {'populate_by_name': True}


class CreateDoubleVerifyAuthenticBrandSafety(BaseModel):
    double_verify_segment_id: Optional[str] = Field(None, alias="doubleVerifySegmentId")

    model_config = {'populate_by_name': True}


class DVBrandSafetyAppStarRatingType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    APP_STAR_RATING_LT_1_POINT_5_STARS = "APP_STAR_RATING_LT_1_POINT_5_STARS"
    APP_STAR_RATING_LT_2_POINT_5_STARS = "APP_STAR_RATING_LT_2_POINT_5_STARS"
    APP_STAR_RATING_LT_2_STARS = "APP_STAR_RATING_LT_2_STARS"
    APP_STAR_RATING_LT_3_POINT_5_STARS = "APP_STAR_RATING_LT_3_POINT_5_STARS"
    APP_STAR_RATING_LT_3_STARS = "APP_STAR_RATING_LT_3_STARS"
    APP_STAR_RATING_LT_4_POINT_5_STARS = "APP_STAR_RATING_LT_4_POINT_5_STARS"
    APP_STAR_RATING_LT_4_STARS = "APP_STAR_RATING_LT_4_STARS"


class DVBrandSafetyAppAgeRatingType(StrEnum):
    ADULTS_ONLY_18_PLUS = "ADULTS_ONLY_18_PLUS"
    EVERYONE_4_PLUS = "EVERYONE_4_PLUS"
    MATURE_17_PLUS = "MATURE_17_PLUS"
    TEENS_12_PLUS = "TEENS_12_PLUS"
    TWEENS_9_PLUS = "TWEENS_9_PLUS"
    UNKNOWN = "UNKNOWN"


class DVBrandSafetyContentCategoryType(StrEnum):
    AD_SERVER = "AD_SERVER"
    CELEBRITY_GOSSIP = "CELEBRITY_GOSSIP"
    CULTS_SURVIVALISM = "CULTS_SURVIVALISM"
    EXTREME_GRAPHIC = "EXTREME_GRAPHIC"
    GAMBLING = "GAMBLING"
    INCENTIVIZED_MALWARE_CLUTTER = "INCENTIVIZED_MALWARE_CLUTTER"
    INFLAMMATORY_POLITICS_NEWS = "INFLAMMATORY_POLITICS_NEWS"
    NEGATIVE_NEWS_FINANCIAL = "NEGATIVE_NEWS_FINANCIAL"
    NEGATIVE_NEWS_PHARMACEUTICAL = "NEGATIVE_NEWS_PHARMACEUTICAL"
    NON_STANDARD_CONTENT_NON_ENGLISH = "NON_STANDARD_CONTENT_NON_ENGLISH"
    NON_STANDARD_CONTENT_PARKING_PAGE = "NON_STANDARD_CONTENT_PARKING_PAGE"
    OCCULT = "OCCULT"
    PIRACY_COPYRIGHT_INFRINGEMENT = "PIRACY_COPYRIGHT_INFRINGEMENT"
    UNMODERATED_UGC_FORUMS_IMAGES_VIDEO = "UNMODERATED_UGC_FORUMS_IMAGES_VIDEO"


class CreateDoubleVerifyBrandSafety(BaseModel):
    app_age_rating: Optional[list["DVBrandSafetyAppAgeRatingType"]] = Field(None, alias="appAgeRating", description="A list of app age ratings to be used for excluding apps. For example, TEENS_12_PLUS will only exclude apps with content ")
    app_star_rating: Optional["DVBrandSafetyAppStarRatingType"] = Field(None, alias="appStarRating")
    content_categories: Optional[list["DVBrandSafetyContentCategoryType"]] = Field(None, alias="contentCategories", description="A list of content categories to exclude from targeting.")
    content_categories_with_risk: Optional[list["CreateDVBrandSafetyContentCategoriesWithRiskMap"]] = Field(None, alias="contentCategoriesWithRisk")
    exclude_apps_with_insufficient_rating: Optional[bool] = Field(None, alias="excludeAppsWithInsufficientRating", description="Set to true to exclude unofficial apps or apps with insufficient user ratings (<100 lifetime).")
    unknown_content: Optional[bool] = Field(None, alias="unknownContent", description="Set to true to exclude unknown content.")

    model_config = {'populate_by_name': True}


class CreateDoubleVerifyCustomContextualSegmentId(BaseModel):
    double_verify_segment_id: Optional[str] = Field(None, alias="doubleVerifySegmentId")

    model_config = {'populate_by_name': True}


class ExcludeAppsAndSitesType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    FRAUD_TRAFFIC_LEVEL_GTE_02 = "FRAUD_TRAFFIC_LEVEL_GTE_02"
    FRAUD_TRAFFIC_LEVEL_GTE_04 = "FRAUD_TRAFFIC_LEVEL_GTE_04"
    FRAUD_TRAFFIC_LEVEL_GTE_06 = "FRAUD_TRAFFIC_LEVEL_GTE_06"
    FRAUD_TRAFFIC_LEVEL_GTE_08 = "FRAUD_TRAFFIC_LEVEL_GTE_08"
    FRAUD_TRAFFIC_LEVEL_GTE_10 = "FRAUD_TRAFFIC_LEVEL_GTE_10"
    FRAUD_TRAFFIC_LEVEL_GTE_100 = "FRAUD_TRAFFIC_LEVEL_GTE_100"
    FRAUD_TRAFFIC_LEVEL_GTE_25 = "FRAUD_TRAFFIC_LEVEL_GTE_25"
    FRAUD_TRAFFIC_LEVEL_GTE_50 = "FRAUD_TRAFFIC_LEVEL_GTE_50"


class CreateDoubleVerifyFraudInvalidTraffic(BaseModel):
    block_app_and_sites: Optional[bool] = Field(None, alias="blockAppAndSites", description="Set to true to block applications and sites with insufficient historical fraud and invalid traffic statistics. This will")
    exclude_apps_and_sites: Optional["ExcludeAppsAndSitesType"] = Field(None, alias="excludeAppsAndSites")
    exclude_impressions: Optional[bool] = Field(None, alias="excludeImpressions", description="Set to true to exclude impressions delivered to devices identified to be fraudulent or invalid.")

    model_config = {'populate_by_name': True}


class CreateDoubleVerifyStandardDisplayBrandSafety(BaseModel):
    content_categories: Optional[list["DVBrandSafetyContentCategoryType"]] = Field(None, alias="contentCategories", description="A list of content categories to exclude from targeting.")
    content_categories_with_risk: Optional[list["CreateDVBrandSafetyContentCategoriesWithRiskMap"]] = Field(None, alias="contentCategoriesWithRisk")
    unknown_content: Optional[bool] = Field(None, alias="unknownContent", description="Set to true to exclude unknown content.")

    model_config = {'populate_by_name': True}


class MrcViewabilityTargetingType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    MRC_VIEWABILITY_GTE_30 = "MRC_VIEWABILITY_GTE_30"
    MRC_VIEWABILITY_GTE_40 = "MRC_VIEWABILITY_GTE_40"
    MRC_VIEWABILITY_GTE_50 = "MRC_VIEWABILITY_GTE_50"
    MRC_VIEWABILITY_GTE_55 = "MRC_VIEWABILITY_GTE_55"
    MRC_VIEWABILITY_GTE_60 = "MRC_VIEWABILITY_GTE_60"
    MRC_VIEWABILITY_GTE_65 = "MRC_VIEWABILITY_GTE_65"
    MRC_VIEWABILITY_GTE_70 = "MRC_VIEWABILITY_GTE_70"
    MRC_VIEWABILITY_GTE_75 = "MRC_VIEWABILITY_GTE_75"
    MRC_VIEWABILITY_GTE_80 = "MRC_VIEWABILITY_GTE_80"


class CreateDoubleVerifyViewability(BaseModel):
    average_completion_and_fully_viewable_rate_targeting: Optional["AverageCompletionAndFullyViewableRateTargetingType"] = Field(None, alias="averageCompletionAndFullyViewableRateTargeting")
    brand_exposure_viewability_targeting: Optional["BrandExposureViewabilityTargetingType"] = Field(None, alias="brandExposureViewabilityTargeting")
    include_unmeasurable_impressions: Optional[bool] = Field(None, alias="includeUnmeasurableImpressions", description="Set to true to include impressions where impressions can't be measured.")
    mrc_viewability_targeting: Optional["MrcViewabilityTargetingType"] = Field(None, alias="mrcViewabilityTargeting")

    model_config = {'populate_by_name': True}


class FoldPosition(StrEnum):
    ABOVE_THE_FOLD = "ABOVE_THE_FOLD"
    BELOW_THE_FOLD = "BELOW_THE_FOLD"
    UNKNOWN = "UNKNOWN"


class CreateFoldPositionTarget(BaseModel):
    """Targets ads in the specified fold position"""
    fold_position: "FoldPosition" = Field(..., alias="foldPosition")

    model_config = {'populate_by_name': True}


class CreateGeoLocationCoordinates(BaseModel):
    """Coordinates for a point of interest"""
    latitude: float = Field(..., description="Latitude coordinate. Example 47.6157")
    longitude: float = Field(..., description="Longitude coordinate. Example 122.339")

    model_config = {'populate_by_name': True}


class CreateSmartLocation(BaseModel):
    """A smart location targets postal codes based on a sales index."""
    location_index_id: str = Field(..., alias="locationIndexId", description="The ID of the index used for this smart location.")
    max_index_value_percentile: Optional[int] = Field(None, alias="maxIndexValuePercentile", description="Maximum percentile value (0-100). Must be greater than minIndexValuePercentile. Null will be treated as 0.")
    min_index_value_percentile: Optional[int] = Field(None, alias="minIndexValuePercentile", description="Minimum percentile value (0-100). Must be less than maxIndexValuePercentile. Null will be treated as 0.")
    name: str = Field(..., description="Name for the smart location.")

    model_config = {'populate_by_name': True}


class DistanceUnit(StrEnum):
    KILOMETERS = "KILOMETERS"
    MILES = "MILES"


class CreateRadiusLocation(BaseModel):
    """Configuration for a radius-based location. A minimum radius of 0.37 miles (2000 ft, 0.6km) is required."""
    coordinates: Optional["CreateGeoLocationCoordinates"] = None
    point_of_interest_address: Optional[str] = Field(None, alias="pointOfInterestAddress", description="Address. Example '2111 7th Ave, Seattle, WA 98121, United States' or 'Amazon Spheres'")
    point_of_interest_radius: float = Field(..., alias="pointOfInterestRadius", description="Radius of circle in kilometers or miles")
    units: "DistanceUnit"

    model_config = {'populate_by_name': True}


class CreateGeoLocationUnion(BaseModel):
    pass


class GeoLocationCreate(BaseModel):
    location: "CreateGeoLocationUnion"

    model_config = {'populate_by_name': True}


class CreateGeoLocationRequest(BaseModel):
    geo_locations: Optional[list["GeoLocationCreate"]] = Field(None, alias="geoLocations")

    model_config = {'populate_by_name': True}


class CreateIndexValues(BaseModel):
    pass


class IASBrandSafetyLevelType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    BRAND_SAFETY_EXCLUDE_HIGH_AND_MODERATE_RISK = "BRAND_SAFETY_EXCLUDE_HIGH_AND_MODERATE_RISK"
    BRAND_SAFETY_EXCLUDE_HIGH_RISK = "BRAND_SAFETY_EXCLUDE_HIGH_RISK"


class CreateIntegralAdScienceBrandSafety(BaseModel):
    exclude_content: Optional[bool] = Field(None, alias="excludeContent", description="Set to true to exclude content that Integral Ad Science is not able to rate.")
    ias_brand_safety_adult: Optional["IASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyAdult")
    ias_brand_safety_alcohol: Optional["IASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyAlcohol")
    ias_brand_safety_gambling: Optional["IASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyGambling")
    ias_brand_safety_hate_speech: Optional["IASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyHateSpeech")
    ias_brand_safety_illegal_downloads: Optional["IASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyIllegalDownloads")
    ias_brand_safety_illegal_drugs: Optional["IASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyIllegalDrugs")
    ias_brand_safety_offensive_language: Optional["IASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyOffensiveLanguage")
    ias_brand_safety_violence: Optional["IASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyViolence")

    model_config = {'populate_by_name': True}


class CreateIntegralAdScienceContextualAvoidance(BaseModel):
    avoidance_segments: Optional[list[str]] = Field(None, alias="avoidanceSegments", description="The unique identifier of the IAS contextual avoidance segment")

    model_config = {'populate_by_name': True}


class CreateIntegralAdScienceContextualTargeting(BaseModel):
    topical_segments: Optional[list[str]] = Field(None, alias="topicalSegments", description="The unique identifier of the IAS contextual topical targeting segment")
    vertical_segments: Optional[list[str]] = Field(None, alias="verticalSegments", description="The unique identifier of the IAS contextual vertical targeting segment")

    model_config = {'populate_by_name': True}


class IASFraudInvalidTrafficType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_MODERATE_RISK = "FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_MODERATE_RISK"
    FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_RISK = "FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_RISK"


class CreateIntegralAdScienceFraudInvalidTraffic(BaseModel):
    target_setting: Optional["IASFraudInvalidTrafficType"] = Field(None, alias="targetSetting")

    model_config = {'populate_by_name': True}


class CreateIntegralAdScienceQualitySync(BaseModel):
    segment_id: Optional[str] = Field(None, alias="segmentId")

    model_config = {'populate_by_name': True}


class ViewabilityTierType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    VIEWABILITY_TIER_GT_40 = "VIEWABILITY_TIER_GT_40"
    VIEWABILITY_TIER_GT_50 = "VIEWABILITY_TIER_GT_50"
    VIEWABILITY_TIER_GT_60 = "VIEWABILITY_TIER_GT_60"
    VIEWABILITY_TIER_GT_70 = "VIEWABILITY_TIER_GT_70"
    VIEWABILITY_TIER_LT_40 = "VIEWABILITY_TIER_LT_40"


class IASViewabilityStandardType(StrEnum):
    GROUPM = "GROUPM"
    MRC = "MRC"
    NONE = "NONE"
    PUBLICIS = "PUBLICIS"


class CreateIntegralAdScienceViewability(BaseModel):
    """The IAS viewability standard."""
    standard: "IASViewabilityStandardType"
    viewability_targeting: Optional["ViewabilityTierType"] = Field(None, alias="viewabilityTargeting")

    model_config = {'populate_by_name': True}


class InventorySourceType(StrEnum):
    AMAZON = "AMAZON"
    APD = "APD"
    DEAL = "DEAL"
    INVENTORY_GROUP = "INVENTORY_GROUP"
    THIRD_PARTY_EXCHANGE = "THIRD_PARTY_EXCHANGE"


class CreateInventorySourceTarget(BaseModel):
    """Target based on the source of the inventory."""
    inventory_source_id: "CreateMarketplaceStringValue" = Field(..., alias="inventorySourceId")
    inventory_source_type: "InventorySourceType" = Field(..., alias="inventorySourceType")

    model_config = {'populate_by_name': True}


class KeywordMatchType(StrEnum):
    BROAD = "BROAD"
    EXACT = "EXACT"
    PHRASE = "PHRASE"


class CreateKeywordTarget(BaseModel):
    """Targets a specific customer search term."""
    keyword: str = Field(..., description="The customer search term or text to target")
    match_type: "KeywordMatchType" = Field(..., alias="matchType")
    native_language_keyword: Optional[str] = Field(None, alias="nativeLanguageKeyword", description="The unlocalized keyword text in the preferred locale of the advertiser.")
    native_language_locale: Optional["LanguageLocale"] = Field(None, alias="nativeLanguageLocale")

    model_config = {'populate_by_name': True}


class LocationIndexCreate(BaseModel):
    index_data: "CreateIndexValues" = Field(..., alias="indexData")
    index_name: str = Field(..., alias="indexName", description="The name of the location index.")

    model_config = {'populate_by_name': True}


class CreateLocationIndexRequest(BaseModel):
    location_indexes: Optional[list["LocationIndexCreate"]] = Field(None, alias="locationIndexes")

    model_config = {'populate_by_name': True}


class CreateLocationTarget(BaseModel):
    """Target based on geographic location."""
    location_id: str = Field(..., alias="locationId", description="The ID of the geographic location to target.")
    location_id_resolved: Optional[str] = Field(None, alias="locationIdResolved", description="A human-readable location text. It's a read-only field.")

    model_config = {'populate_by_name': True}


class ThemeMatchType(StrEnum):
    INTERESTED_AUDIENCE = "INTERESTED_AUDIENCE"
    KEYWORDS_CLOSE_MATCH = "KEYWORDS_CLOSE_MATCH"
    KEYWORDS_LOOSE_MATCH = "KEYWORDS_LOOSE_MATCH"
    KEYWORDS_RELATED_TO_GIFTS = "KEYWORDS_RELATED_TO_GIFTS"
    KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY = "KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY"
    KEYWORDS_RELATED_TO_PRIME_DAY = "KEYWORDS_RELATED_TO_PRIME_DAY"
    KEYWORDS_RELATED_TO_YOUR_BRAND = "KEYWORDS_RELATED_TO_YOUR_BRAND"
    KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES = "KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES"
    KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY = "KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY"
    PRODUCTS_SIMILAR_TO_ADVERTISED_PRODUCTS = "PRODUCTS_SIMILAR_TO_ADVERTISED_PRODUCTS"
    PRODUCT_COMPLEMENTS = "PRODUCT_COMPLEMENTS"
    PRODUCT_SUBSTITUTES = "PRODUCT_SUBSTITUTES"


class CreateThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""
    match_type: "ThemeMatchType" = Field(..., alias="matchType")

    model_config = {'populate_by_name': True}


class CreateOverridableTargets(BaseModel):
    pass


class CreateMarketplaceTargetFieldOverrides(BaseModel):
    state: Optional["State"] = None
    tags: Optional[list["CreateTag"]] = Field(None, description="Open ended labels with a key value pair applied to the target")
    target_details: Optional["CreateOverridableTargets"] = Field(None, alias="targetDetails")

    model_config = {'populate_by_name': True}


class CreateMarketplaceTargetConfigurations(BaseModel):
    marketplace: "Marketplace"
    overrides: "CreateMarketplaceTargetFieldOverrides"

    model_config = {'populate_by_name': True}


class NativeContentPosition(StrEnum):
    IN_ARTICLE = "IN_ARTICLE"
    IN_FEED = "IN_FEED"
    PERIPHERAL = "PERIPHERAL"
    RECOMMENDATION = "RECOMMENDATION"
    UNKNOWN = "UNKNOWN"


class CreateNativeContentPositionTarget(BaseModel):
    """Targets ads to a specific native content position"""
    native_position: "NativeContentPosition" = Field(..., alias="nativePosition")

    model_config = {'populate_by_name': True}


class NewsGuardBrandGuardMisinformationSafetyType(StrEnum):
    AI_GENERATED_MFA = "AI_GENERATED_MFA"
    BASIC_EXCLUDE = "BASIC_EXCLUDE"
    CLIMATE_MISINFORMATION = "CLIMATE_MISINFORMATION"
    COVID_MISINFORMATION = "COVID_MISINFORMATION"
    ELECTION_MISINFORMATION = "ELECTION_MISINFORMATION"
    HEALTH_MISINFORMATION = "HEALTH_MISINFORMATION"
    HIGH_EXCLUDE = "HIGH_EXCLUDE"
    ISRAEL_HAMAS_MISINFORMATION = "ISRAEL_HAMAS_MISINFORMATION"
    MAX_EXCLUDE = "MAX_EXCLUDE"
    MISINFORMATION_SITES = "MISINFORMATION_SITES"
    OPINIONATED_NEWS = "OPINIONATED_NEWS"
    QANON_MISINFORMATION = "QANON_MISINFORMATION"
    UKRAINE_MISINFORMATION = "UKRAINE_MISINFORMATION"
    VACCINE_MISINFORMATION = "VACCINE_MISINFORMATION"


class CreateNewsGuardBrandGuardMisinformationSafety(BaseModel):
    avoidance_list: Optional[list["NewsGuardBrandGuardMisinformationSafetyType"]] = Field(None, alias="avoidanceList", description="The unique identifiers of misinformation targets")

    model_config = {'populate_by_name': True}


class NewsGuardBrandGuardTrustedNewsTargetingType(StrEnum):
    BASIC_INCLUDE = "BASIC_INCLUDE"
    BUSINESS_INCLUDE = "BUSINESS_INCLUDE"
    COMMUNITY_INCLUDE = "COMMUNITY_INCLUDE"
    HEALTH_INCLUDE = "HEALTH_INCLUDE"
    HIGH_INCLUDE = "HIGH_INCLUDE"
    LIFESTYLE_INCLUDE = "LIFESTYLE_INCLUDE"
    LOCAL_INCLUDE = "LOCAL_INCLUDE"
    MAX_INCLUDE = "MAX_INCLUDE"
    POLITICS_INCLUDE = "POLITICS_INCLUDE"
    TECH_INCLUDE = "TECH_INCLUDE"


class CreateNewsGuardBrandGuardTrustedNewsTargeting(BaseModel):
    """Only applicable for Web supply."""
    targeting_list: Optional[list["NewsGuardBrandGuardTrustedNewsTargetingType"]] = Field(None, alias="targetingList", description="The unique identifiers of trusted news targets")

    model_config = {'populate_by_name': True}


class CreatePixalateFraudInvalidTraffic(BaseModel):
    exclude_apps_and_domains: Optional[bool] = Field(None, alias="excludeAppsAndDomains", description="Set to true to exclude traffic from Apps and Domains identified to be fraudulent or invalid.")
    exclude_ip_address_and_user_agents: Optional[bool] = Field(None, alias="excludeIpAddressAndUserAgents", description="Set to true to exclude traffic from IPV4 and IPV6 addresses and user agents identified to be fraudulent or invalid.")
    exclude_ott_and_mobile_devices: Optional[bool] = Field(None, alias="excludeOttAndMobileDevices", description="Set to true to exclude traffic from OTT and Mobile devices identified to be fraudulent or invalid.")
    exclude_removed_apps_from_app_stores: Optional[bool] = Field(None, alias="excludeRemovedAppsFromAppStores", description="Set to true to exlude traffic from Apps that have been removed from the google play and apple app stores in the last 6 m")

    model_config = {'populate_by_name': True}


class PlacementType(StrEnum):
    REWARDED = "REWARDED"


class CreatePlacementTypeTarget(BaseModel):
    """Target based on the placement type."""
    placement_type: "PlacementType" = Field(..., alias="placementType")

    model_config = {'populate_by_name': True}


class Lookback(StrEnum):
    DAYS_14 = "DAYS_14"
    DAYS_180 = "DAYS_180"
    DAYS_30 = "DAYS_30"
    DAYS_365 = "DAYS_365"
    DAYS_60 = "DAYS_60"
    DAYS_7 = "DAYS_7"
    DAYS_90 = "DAYS_90"


class TargetEvent(StrEnum):
    PURCHASE = "PURCHASE"
    VIEW = "VIEW"


class ProductAudienceMatchType(StrEnum):
    PRODUCT_EXACT = "PRODUCT_EXACT"
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"


class CreateProductAudienceTarget(BaseModel):
    """Target customers who have viewed or purchased a certain product within a specified lookback window."""
    asin: "CreateMarketplaceStringValue"
    event: "TargetEvent"
    lookback: "Lookback"
    match_type: "ProductAudienceMatchType" = Field(..., alias="matchType")

    model_config = {'populate_by_name': True}


class CreateProductCategoryRefinement(BaseModel):
    product_age_range_id: Optional[str] = Field(None, alias="productAgeRangeId", description="The age range ID to target.")
    product_age_range_id_resolved: Optional[str] = Field(None, alias="productAgeRangeIdResolved", description="The resolved age range to target.")
    product_brand_id: Optional[str] = Field(None, alias="productBrandId", description="The brand ID to target.")
    product_brand_id_resolved: Optional[str] = Field(None, alias="productBrandIdResolved", description="The resolved name of the brand.")
    product_category_id: Optional[str] = Field(None, alias="productCategoryId", description="The product category ID to target.")
    product_category_id_resolved: Optional[str] = Field(None, alias="productCategoryIdResolved", description="The resolved product category.")
    product_genre_id: Optional[str] = Field(None, alias="productGenreId", description="The product genre ID to target.")
    product_price_greater_than: Optional[float] = Field(None, alias="productPriceGreaterThan", description="Refinement to target products with a price greater than the value within the product category.")
    product_price_less_than: Optional[float] = Field(None, alias="productPriceLessThan", description="Refinement to target products with a price less than the value within the product category.")
    product_prime_shipping_eligible: Optional[bool] = Field(None, alias="productPrimeShippingEligible", description="Target based on if a product is Prime-shipping eligible.")
    product_rating_greater_than: Optional[float] = Field(None, alias="productRatingGreaterThan", description="Refinement to target products with a rating greater than the value within the product category.")
    product_rating_less_than: Optional[float] = Field(None, alias="productRatingLessThan", description="Refinement to target products with a rating less than the value within the product category.")

    model_config = {'populate_by_name': True}


class CreateProductCategoryRefinementMarketplaceSetting(BaseModel):
    marketplace: "Marketplace"
    product_category_refinement: "CreateProductCategoryRefinement" = Field(..., alias="productCategoryRefinement")

    model_config = {'populate_by_name': True}


class CreateProductCategoryRefinementValue(BaseModel):
    marketplace_settings: Optional[list["CreateProductCategoryRefinementMarketplaceSetting"]] = Field(None, alias="marketplaceSettings", description="Marketplace specific product category refinements. Either the value or the marketplaceSettings should always be specifie")
    product_category_refinement: Optional["CreateProductCategoryRefinement"] = Field(None, alias="productCategoryRefinement")

    model_config = {'populate_by_name': True}


class ProductCategoryMatchType(StrEnum):
    MULTISIGNAL_BROAD = "MULTISIGNAL_BROAD"


class CreateProductGenreRefinement(BaseModel):
    product_genre_id: str = Field(..., alias="productGenreId", description="The product genre ID to target.")

    model_config = {'populate_by_name': True}


class CreateProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""
    match_type: Optional["ProductCategoryMatchType"] = Field(None, alias="matchType")
    product_category_refinement: "CreateProductCategoryRefinementValue" = Field(..., alias="productCategoryRefinement")
    product_genre_refinement: Optional["CreateProductGenreRefinement"] = Field(None, alias="productGenreRefinement")

    model_config = {'populate_by_name': True}


class CreateProductMarketplaceSetting(BaseModel):
    marketplace: "Marketplace"
    product_id: str = Field(..., alias="productId", description="The product id applicable at the specified marketplace.")

    model_config = {'populate_by_name': True}


class CreateProductValue(BaseModel):
    marketplace_settings: Optional[list["CreateProductMarketplaceSetting"]] = Field(None, alias="marketplaceSettings", description="The product ids at specific marketplace level. Either the product id or the marketplace settings should always be specif")
    product_id: Optional[str] = Field(None, alias="productId", description="The product identifier. Either the product id or the marketplace settings should always be specified")

    model_config = {'populate_by_name': True}


class ProductMatchType(StrEnum):
    PRODUCT_COMPLEMENTS = "PRODUCT_COMPLEMENTS"
    PRODUCT_EXACT = "PRODUCT_EXACT"
    PRODUCT_REMARKETING = "PRODUCT_REMARKETING"
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"


class CreateProductTarget(BaseModel):
    """Targets a specific product."""
    match_type: "ProductMatchType" = Field(..., alias="matchType")
    product: "CreateProductValue"
    product_id_type: "ProductIdType" = Field(..., alias="productIdType")

    model_config = {'populate_by_name': True}


class CreateTargetBidMarketplaceSetting(BaseModel):
    bid: Optional[float] = Field(None, description="The maximum bid for a target.")
    currency_code: "CurrencyCode" = Field(..., alias="currencyCode")
    marketplace: "Marketplace"

    model_config = {'populate_by_name': True}


class CreateTargetBid(BaseModel):
    bid: Optional[float] = Field(None, description="The maximum bid for a target.")
    marketplace_settings: Optional[list["CreateTargetBidMarketplaceSetting"]] = Field(None, alias="marketplaceSettings", description="The bid associated with the target at specified marketplace level. Either one of bid or marketplaceSettings should alway")

    model_config = {'populate_by_name': True}


class VideoContentDuration(StrEnum):
    EXTENDED = "EXTENDED"
    LONG = "LONG"
    MEDIUM = "MEDIUM"
    SHORT = "SHORT"
    UNKNOWN = "UNKNOWN"


class CreateVideoContentDurationTarget(BaseModel):
    """Targets ads to a specific video content duration"""
    duration: "VideoContentDuration"

    model_config = {'populate_by_name': True}


class ThirdPartyTargetType(StrEnum):
    DOUBLE_VERIFY_AUTHENTIC_ATTENTION = "DOUBLE_VERIFY_AUTHENTIC_ATTENTION"
    DOUBLE_VERIFY_AUTHENTIC_BRAND_SAFETY = "DOUBLE_VERIFY_AUTHENTIC_BRAND_SAFETY"
    DOUBLE_VERIFY_BRAND_SAFETY = "DOUBLE_VERIFY_BRAND_SAFETY"
    DOUBLE_VERIFY_CUSTOM_CONTEXTUAL_SEGMENT_ID = "DOUBLE_VERIFY_CUSTOM_CONTEXTUAL_SEGMENT_ID"
    DOUBLE_VERIFY_FRAUD_INVALID_TRAFFIC = "DOUBLE_VERIFY_FRAUD_INVALID_TRAFFIC"
    DOUBLE_VERIFY_STANDARD_DISPLAY_BRAND_SAFETY = "DOUBLE_VERIFY_STANDARD_DISPLAY_BRAND_SAFETY"
    DOUBLE_VERIFY_VIEWABILITY = "DOUBLE_VERIFY_VIEWABILITY"
    INTEGRAL_AD_SCIENCE_BRAND_SAFETY = "INTEGRAL_AD_SCIENCE_BRAND_SAFETY"
    INTEGRAL_AD_SCIENCE_CONTEXTUAL_AVOIDANCE = "INTEGRAL_AD_SCIENCE_CONTEXTUAL_AVOIDANCE"
    INTEGRAL_AD_SCIENCE_CONTEXTUAL_TARGETING = "INTEGRAL_AD_SCIENCE_CONTEXTUAL_TARGETING"
    INTEGRAL_AD_SCIENCE_FRAUD_INVALID_TRAFFIC = "INTEGRAL_AD_SCIENCE_FRAUD_INVALID_TRAFFIC"
    INTEGRAL_AD_SCIENCE_QUALITY_SYNC = "INTEGRAL_AD_SCIENCE_QUALITY_SYNC"
    INTEGRAL_AD_SCIENCE_VIEWABILITY = "INTEGRAL_AD_SCIENCE_VIEWABILITY"
    NEWS_GUARD_BRAND_GUARD_MISINFORMATION_SAFETY = "NEWS_GUARD_BRAND_GUARD_MISINFORMATION_SAFETY"
    NEWS_GUARD_BRAND_GUARD_TRUSTED_NEWS_TARGETING = "NEWS_GUARD_BRAND_GUARD_TRUSTED_NEWS_TARGETING"
    PIXALATE_FRAUD_INVALID_TRAFFIC = "PIXALATE_FRAUD_INVALID_TRAFFIC"


class CreateThirdPartyTargetDetails(BaseModel):
    pass


class CreateThirdPartyTarget(BaseModel):
    third_party_target_details: "CreateThirdPartyTargetDetails" = Field(..., alias="thirdPartyTargetDetails")
    third_party_target_type: "ThirdPartyTargetType" = Field(..., alias="thirdPartyTargetType")

    model_config = {'populate_by_name': True}


class VideoAdFormat(StrEnum):
    FULL_EPISODE_PLAYER = "FULL_EPISODE_PLAYER"
    INSTREAM = "INSTREAM"
    OUTSTREAM = "OUTSTREAM"


class CreateVideoAdFormatTarget(BaseModel):
    """Target based on the video ad format."""
    video_ad_format: "VideoAdFormat" = Field(..., alias="videoAdFormat")

    model_config = {'populate_by_name': True}


class CreateTargetDetails(BaseModel):
    pass


class TargetType(StrEnum):
    AD_INITIATION = "AD_INITIATION"
    AD_PLAYER_SIZE = "AD_PLAYER_SIZE"
    APP = "APP"
    AUDIENCE = "AUDIENCE"
    BRAND_SAFETY_CATEGORY = "BRAND_SAFETY_CATEGORY"
    BRAND_SAFETY_TIER = "BRAND_SAFETY_TIER"
    CONTENT_CATEGORY = "CONTENT_CATEGORY"
    CONTENT_GENRE = "CONTENT_GENRE"
    CONTENT_INSTREAM_POSITION = "CONTENT_INSTREAM_POSITION"
    CONTENT_OUTSTREAM_POSITION = "CONTENT_OUTSTREAM_POSITION"
    CONTENT_RATING = "CONTENT_RATING"
    DAYPART = "DAYPART"
    DEVICE = "DEVICE"
    DOMAIN = "DOMAIN"
    FOLD_POSITION = "FOLD_POSITION"
    INVENTORY_SOURCE = "INVENTORY_SOURCE"
    KEYWORD = "KEYWORD"
    LOCATION = "LOCATION"
    NATIVE_CONTENT_POSITION = "NATIVE_CONTENT_POSITION"
    PLACEMENT_TYPE = "PLACEMENT_TYPE"
    PRODUCT = "PRODUCT"
    PRODUCT_AUDIENCE = "PRODUCT_AUDIENCE"
    PRODUCT_CATEGORY = "PRODUCT_CATEGORY"
    THEME = "THEME"
    THIRD_PARTY = "THIRD_PARTY"
    VIDEO_AD_FORMAT = "VIDEO_AD_FORMAT"
    VIDEO_CONTENT_DURATION = "VIDEO_CONTENT_DURATION"


class TargetCreate(BaseModel):
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.")
    ad_product: "AdProduct" = Field(..., alias="adProduct")
    bid: Optional["CreateTargetBid"] = None
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.")
    marketplace_configurations: Optional[list["CreateMarketplaceTargetConfigurations"]] = Field(None, alias="marketplaceConfigurations", description="List of marketplace-specific configurations for a global target that enables overriding certain attributes at individual")
    marketplace_scope: Optional["MarketplaceScope"] = Field(None, alias="marketplaceScope")
    marketplaces: Optional[list["Marketplace"]] = Field(None, description="The list of marketplace in which the global target is applicable. The marketplaces included should either be same as or ")
    negative: bool = Field(..., description="Indicates whether the target is negative or not.")
    state: "CreateState"
    tags: Optional[list["CreateTag"]] = Field(None, description="Open ended labels with a key value pair applied to the target")
    target_details: "CreateTargetDetails" = Field(..., alias="targetDetails")
    target_type: "TargetType" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class CreateTargetRequest(BaseModel):
    targets: Optional[list["TargetCreate"]] = None

    model_config = {'populate_by_name': True}


class DSPAcrossGroupOperator(StrEnum):
    ALL = "ALL"
    ANY = "ANY"


class DSPCurrencyCode(StrEnum):
    AED = "AED"
    ARS = "ARS"
    AUD = "AUD"
    BGN = "BGN"
    BHD = "BHD"
    BOB = "BOB"
    BRL = "BRL"
    CAD = "CAD"
    CHF = "CHF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    CRC = "CRC"
    CZK = "CZK"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EUR = "EUR"
    GBP = "GBP"
    GTQ = "GTQ"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    JMD = "JMD"
    JPY = "JPY"
    KRW = "KRW"
    KWD = "KWD"
    MAD = "MAD"
    MXN = "MXN"
    MYR = "MYR"
    NOK = "NOK"
    NZD = "NZD"
    PAB = "PAB"
    PEN = "PEN"
    PHP = "PHP"
    PKR = "PKR"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    THB = "THB"
    TND = "TND"
    TRY = "TRY"
    TWD = "TWD"
    UAH = "UAH"
    USD = "USD"
    UYU = "UYU"
    VND = "VND"


class DSPAdGroupBid(BaseModel):
    base_bid: Optional[float] = Field(None, alias="baseBid", description="The lower bound bid used for the ads in the ad group.")
    currency_code: "DSPCurrencyCode" = Field(..., alias="currencyCode")
    max_average_bid: Optional[float] = Field(None, alias="maxAverageBid", description="The max average bid that will be targeted on the ad group across all of the bids (a single bid could be lower or higher ")

    model_config = {'populate_by_name': True}


class DSPBudgetAllocation(StrEnum):
    AUTO = "AUTO"
    MANUAL = "MANUAL"


class DSPAdGroupBudgetSettings(BaseModel):
    budget_allocation: Optional["DSPBudgetAllocation"] = Field(None, alias="budgetAllocation")
    daily_min_spend_value: Optional[float] = Field(None, alias="dailyMinSpendValue", description="Denotes the daily minimum spend on the ad group in local currency.")

    model_config = {'populate_by_name': True}


class DSPVideoInitiationType(StrEnum):
    AUTOPLAY = "AUTOPLAY"
    UNKNOWN = "UNKNOWN"
    USER_INITIATED = "USER_INITIATED"


class DSPAdInitiationTarget(BaseModel):
    """Target based on how the video ad will be started."""
    video_initiation_type: "DSPVideoInitiationType" = Field(..., alias="videoInitiationType")

    model_config = {'populate_by_name': True}


class DSPAdPlayerSize(StrEnum):
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    SMALL = "SMALL"
    UNKNOWN = "UNKNOWN"


class DSPAdPlayerSizeTarget(BaseModel):
    """Target based on the size of the ad player."""
    ad_player_size: "DSPAdPlayerSize" = Field(..., alias="adPlayerSize")

    model_config = {'populate_by_name': True}


class DSPAdProduct(StrEnum):
    AMAZON_DSP = "AMAZON_DSP"


class DSPAdvertiserDomainList(BaseModel):
    """Targets domains based on list inherited from the advertiser."""
    inherit_from_advertiser: bool = Field(..., alias="inheritFromAdvertiser", description="Set to TRUE to inherit domain list from advertiser.")

    model_config = {'populate_by_name': True}


class DSPViewabilityTier(StrEnum):
    ALL_TIERS = "ALL_TIERS"
    GREATER_THAN_40_PERCENT = "GREATER_THAN_40_PERCENT"
    GREATER_THAN_50_PERCENT = "GREATER_THAN_50_PERCENT"
    GREATER_THAN_60_PERCENT = "GREATER_THAN_60_PERCENT"
    GREATER_THAN_70_PERCENT = "GREATER_THAN_70_PERCENT"
    LESS_THAN_40_PERCENT = "LESS_THAN_40_PERCENT"


class DSPAmazonViewability(BaseModel):
    include_unmeasurable_impressions: bool = Field(..., alias="includeUnmeasurableImpressions", description="Must be false if viewabilityTier is set to ALL_TIERS. You can set to true to include impressions that can not be measure")
    viewability_tier: "DSPViewabilityTier" = Field(..., alias="viewabilityTier")

    model_config = {'populate_by_name': True}


class DSPAppType(StrEnum):
    MOBILE = "MOBILE"
    STREAMING_TV = "STREAMING_TV"


class DSPAppTarget(BaseModel):
    """Target based on user application."""
    app_id: str = Field(..., alias="appId", description="The app identifier being targeted.")
    app_type: "DSPAppType" = Field(..., alias="appType")

    model_config = {'populate_by_name': True}


class DSPMarketplaceStringValue(BaseModel):
    default_value: Optional[str] = Field(None, alias="defaultValue", description="The default value. Either the default value or the marketplace settings should always be specified")

    model_config = {'populate_by_name': True}


class DSPInGroupOperator(StrEnum):
    ALL = "ALL"
    ANY = "ANY"


class DSPAudienceTarget(BaseModel):
    """Target based on a specified audience ID."""
    across_group_operator: Optional["DSPAcrossGroupOperator"] = Field(None, alias="acrossGroupOperator")
    audience_id: "DSPMarketplaceStringValue" = Field(..., alias="audienceId")
    group_id: Optional[str] = Field(None, alias="groupId", description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences")
    in_group_operator: Optional["DSPInGroupOperator"] = Field(None, alias="inGroupOperator")

    model_config = {'populate_by_name': True}


class DSPAutoCreationSettings(BaseModel):
    pass


class DSPAutomatedTargetingTactic(StrEnum):
    AWARENESS = "AWARENESS"
    CUSTOMER_ACQUISITION = "CUSTOMER_ACQUISITION"
    MAXIMIZE_PERFORMANCE = "MAXIMIZE_PERFORMANCE"
    PROSPECTING = "PROSPECTING"
    REMARKETING = "REMARKETING"
    RETENTION = "RETENTION"
    SEARCH = "SEARCH"


class DSPAverageCompletionAndFullyViewableRateTargetingType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_10 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_10"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_20 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_20"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_25 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_25"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_30 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_30"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_35 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_35"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_40 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_40"


class DSPBidStrategy(StrEnum):
    PRIORITIZE_KPI_TARGET = "PRIORITIZE_KPI_TARGET"
    SPEND_BUDGET_IN_FULL = "SPEND_BUDGET_IN_FULL"
    USE_CAMPAIGN_STRATEGY = "USE_CAMPAIGN_STRATEGY"


class DSPBidSettings(BaseModel):
    bid_strategy: Optional["DSPBidStrategy"] = Field(None, alias="bidStrategy")

    model_config = {'populate_by_name': True}


class DSPBrandExposureViewabilityTargetingType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    BRAND_EXPOSURE_VIEWABILITY_GTE_10_SEC_AVG_DURATION = "BRAND_EXPOSURE_VIEWABILITY_GTE_10_SEC_AVG_DURATION"
    BRAND_EXPOSURE_VIEWABILITY_GTE_15_SEC_AVG_DURATION = "BRAND_EXPOSURE_VIEWABILITY_GTE_15_SEC_AVG_DURATION"
    BRAND_EXPOSURE_VIEWABILITY_GTE_5_SEC_AVG_DURATION = "BRAND_EXPOSURE_VIEWABILITY_GTE_5_SEC_AVG_DURATION"


class DSPBrandSafetyCategory(StrEnum):
    ACCIDENTS_DISASTERS_AND_TRAGEDIES = "ACCIDENTS_DISASTERS_AND_TRAGEDIES"
    ALCOHOL_AND_RELATED_PRODUCTS = "ALCOHOL_AND_RELATED_PRODUCTS"
    BLOOD_GORE_VIOLENCE = "BLOOD_GORE_VIOLENCE"
    CRIME = "CRIME"
    DRUG_REFERENCES_OR_USE = "DRUG_REFERENCES_OR_USE"
    GAMBLING = "GAMBLING"
    HIGHLY_DEBATED_SOCIAL_ISSUES = "HIGHLY_DEBATED_SOCIAL_ISSUES"
    POLITICS = "POLITICS"
    PROFANITY = "PROFANITY"
    RELIGIOUS_CONTENT = "RELIGIOUS_CONTENT"
    SEXUAL_REFERENCES_AND_SUGGESTIVE = "SEXUAL_REFERENCES_AND_SUGGESTIVE"
    SHOCK_AND_HORROR = "SHOCK_AND_HORROR"
    TOBACCO_AND_RELATED_PRODUCTS = "TOBACCO_AND_RELATED_PRODUCTS"
    UNRATED_MEDIA_CONTENT = "UNRATED_MEDIA_CONTENT"
    WEAPONS = "WEAPONS"


class DSPBrandSafetyCategoryTarget(BaseModel):
    """Target based on, if any, the classifications of unsuitable contexts that may pose a risk to a brand's reputation of content being viewed."""
    brand_safety_category: "DSPBrandSafetyCategory" = Field(..., alias="brandSafetyCategory")

    model_config = {'populate_by_name': True}


class DSPBrandSafetyTier(StrEnum):
    EXPANDED = "EXPANDED"
    RESTRICTIVE = "RESTRICTIVE"
    STANDARD = "STANDARD"


class DSPBrandSafetyTierTarget(BaseModel):
    """Target based on the brand suitability risk levels of content being viewed."""
    brand_safety_tier: "DSPBrandSafetyTier" = Field(..., alias="brandSafetyTier")

    model_config = {'populate_by_name': True}


class DSPBrandSuitabilityRiskLevelType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    HIGH = "HIGH"
    HIGH_MEDIUM = "HIGH_MEDIUM"
    HIGH_MEDIUM_LOW = "HIGH_MEDIUM_LOW"


class DSPRecurrence(StrEnum):
    DAILY = "DAILY"
    LIFETIME = "LIFETIME"
    MONTHLY = "MONTHLY"


class DSPMonetaryBudget(BaseModel):
    currency_code: "DSPCurrencyCode" = Field(..., alias="currencyCode")
    value: float = Field(..., description="The monetary amount of the budget cap in the given currency.")

    model_config = {'populate_by_name': True}


class DSPMonetaryBudgetValue(BaseModel):
    monetary_budget: Optional["DSPMonetaryBudget"] = Field(None, alias="monetaryBudget")

    model_config = {'populate_by_name': True}


class DSPBudgetValue(BaseModel):
    pass


class DSPBudgetType(StrEnum):
    MONETARY = "MONETARY"


class DSPBudget(BaseModel):
    budget_type: "DSPBudgetType" = Field(..., alias="budgetType")
    budget_value: "DSPBudgetValue" = Field(..., alias="budgetValue")
    recurrence_time_period: "DSPRecurrence" = Field(..., alias="recurrenceTimePeriod")

    model_config = {'populate_by_name': True}


class DSPRolloverStrategy(StrEnum):
    CUMULATIVE_BUDGET_ROLLOVER = "CUMULATIVE_BUDGET_ROLLOVER"
    NO_ROLLOVER = "NO_ROLLOVER"
    PRIOR_BUDGET_ROLLOVER = "PRIOR_BUDGET_ROLLOVER"


class DSPBudgetSettings(BaseModel):
    budget_allocation: Optional["DSPBudgetAllocation"] = Field(None, alias="budgetAllocation")
    flight_budget_rollover_strategy: Optional["DSPRolloverStrategy"] = Field(None, alias="flightBudgetRolloverStrategy")

    model_config = {'populate_by_name': True}


class DSPCampaignFeeType(StrEnum):
    AGENCY = "AGENCY"


class DSPCampaignFeeValueType(StrEnum):
    PERCENTAGE_OF_BUDGET = "PERCENTAGE_OF_BUDGET"


class DSPCampaignFee(BaseModel):
    fee_type: "DSPCampaignFeeType" = Field(..., alias="feeType")
    fee_value: float = Field(..., alias="feeValue", description="A service fee that is subtracted from the campaign budget as a percent of budget. This setting can’t be changed after an")
    fee_value_type: "DSPCampaignFeeValueType" = Field(..., alias="feeValueType")

    model_config = {'populate_by_name': True}


class DSPFlightBudget(BaseModel):
    budget_type: "DSPBudgetType" = Field(..., alias="budgetType")
    budget_value: "DSPBudgetValue" = Field(..., alias="budgetValue")

    model_config = {'populate_by_name': True}


class DSPCampaignFlight(BaseModel):
    budget: "DSPFlightBudget"
    end_date_time: str = Field(..., alias="endDateTime")
    flight_id: Optional[str] = Field(None, alias="flightId", description="The ID associated with the flight.")
    name: Optional[str] = Field(None, description="The name of the flight.")
    start_date_time: str = Field(..., alias="startDateTime", description="The start date of the flight.")

    model_config = {'populate_by_name': True}


class DSPForecastFlight(BaseModel):
    budget: "DSPBudget"
    end_date_time: str = Field(..., alias="endDateTime")
    flight_id: Optional[str] = Field(None, alias="flightId", description="The ID associated with the flight.")
    start_date_time: str = Field(..., alias="startDateTime", description="The start date of the flight.")

    model_config = {'populate_by_name': True}


class DSPDeliverInFullConfidenceLevel(StrEnum):
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    UNAVAILABLE = "UNAVAILABLE"


class DSPDeliverInFullConfidence(BaseModel):
    """Description of how confident we delivery 100% of the ads for the specific metric."""
    value: "DSPDeliverInFullConfidenceLevel"

    model_config = {'populate_by_name': True}


class DSPForecastPeriodicity(StrEnum):
    DAILY = "DAILY"
    LIFETIME = "LIFETIME"
    MONTHLY = "MONTHLY"
    WEEKLY = "WEEKLY"


class DSPForecastValue(BaseModel):
    high: float
    low: float
    mean: float

    model_config = {'populate_by_name': True}


class DSPPointLabel(StrEnum):
    AIMP = "AIMP"
    AREA = "AREA"
    BID = "BID"
    CAS = "CAS"
    CPA = "CPA"
    CPC = "CPC"
    CPM = "CPM"
    DC = "DC"
    EIMP = "EIMP"
    EREA = "EREA"
    ROAS = "ROAS"
    SPEND = "SPEND"
    TAS = "TAS"


class DSPYPoint(BaseModel):
    """The label and value on Y axis of the curve."""
    label: "DSPPointLabel"
    value: "DSPForecastValue"

    model_config = {'populate_by_name': True}


class DSPXPoint(BaseModel):
    """The label and value on X axis of the curve."""
    label: "DSPPointLabel"
    value: float

    model_config = {'populate_by_name': True}


class DSPPoint(BaseModel):
    point_type: Optional[str] = Field(None, alias="pointType")
    x: "DSPXPoint"
    y: Optional[list["DSPYPoint"]] = None

    model_config = {'populate_by_name': True}


class DSPCurve(BaseModel):
    """The forecast curve of Bid/Spend vs the metric type based on periodicity."""
    focus_point: Optional[list["DSPPoint"]] = Field(None, alias="focusPoint")
    periodicity: Optional["DSPForecastPeriodicity"] = None
    points: Optional[list["DSPPoint"]] = None

    model_config = {'populate_by_name': True}


class DSPRecommendedObjectType(StrEnum):
    ADGROUP = "ADGROUP"
    CAMPAIGN = "CAMPAIGN"


class DSPInsightFeature(StrEnum):
    CAMPAIGN_FREQUENCY_CAP = "CAMPAIGN_FREQUENCY_CAP"
    LINE_ITEM_APPBLOCKING_TARGETING = "LINE_ITEM_APPBLOCKING_TARGETING"
    LINE_ITEM_COLD_START_DEALS = "LINE_ITEM_COLD_START_DEALS"
    LINE_ITEM_COLD_START_SEGMENTS = "LINE_ITEM_COLD_START_SEGMENTS"
    LINE_ITEM_CONTEXTUAL_TARGETING = "LINE_ITEM_CONTEXTUAL_TARGETING"
    LINE_ITEM_DOMAINLIST_TARGETING = "LINE_ITEM_DOMAINLIST_TARGETING"
    LINE_ITEM_FREQUENCY_CAP = "LINE_ITEM_FREQUENCY_CAP"
    LINE_ITEM_GEO_TARGETING = "LINE_ITEM_GEO_TARGETING"
    LINE_ITEM_LARGE_TARGETING = "LINE_ITEM_LARGE_TARGETING"
    LINE_ITEM_MAX_BID = "LINE_ITEM_MAX_BID"
    LINE_ITEM_MOBILE_DEVICES_TARGETING = "LINE_ITEM_MOBILE_DEVICES_TARGETING"
    LINE_ITEM_NARROW_SEGMENTS = "LINE_ITEM_NARROW_SEGMENTS"
    LINE_ITEM_SIMILAR_AUDIENCES = "LINE_ITEM_SIMILAR_AUDIENCES"
    LINE_ITEM_TOO_FAR_IN_FUTURE = "LINE_ITEM_TOO_FAR_IN_FUTURE"
    LINE_ITEM_UNSUPPORTED_CONTEXTUAL_TARGETING = "LINE_ITEM_UNSUPPORTED_CONTEXTUAL_TARGETING"
    LINE_ITEM_UNSUPPORTED_KEYWORD_TARGETING = "LINE_ITEM_UNSUPPORTED_KEYWORD_TARGETING"


class DSPForecastInsightsGroup(BaseModel):
    """Insights for leading drivers of forecast results for a specific entity, e.g. campaign frequency cap, line item max bid."""
    cold_start_deal_names: Optional[list[str]] = Field(None, alias="coldStartDealNames", description="The names of audience deals attached to the entity, that are newly created and may not be accurately incorporated into t")
    cold_start_segment_names: Optional[list[str]] = Field(None, alias="coldStartSegmentNames", description="The names of audience segments attached to the entity, that are newly created and may not be accurately incorporated int")
    display_name: str = Field(..., alias="displayName", description="The display name for the entity this insight is for, e.g. campaign/line item display name.")
    group_type: "DSPRecommendedObjectType" = Field(..., alias="groupType")
    insights_features: list["DSPInsightFeature"] = Field(..., alias="insightsFeatures", description="The features corresponding to this group of insights, e.g. array of line item max bid, campaign frequency cap, etc.")
    tag: str = Field(..., description="The unique identifier for the entity this group of insights refers to, e.g. line item ID, campaign ID, etc.")

    model_config = {'populate_by_name': True}


class DSPFlightForecastInsights(BaseModel):
    """Collection of insights for a particular flight forecast."""
    forecast_explainability_insights: Optional[list["DSPForecastInsightsGroup"]] = Field(None, alias="forecastExplainabilityInsights", description="Detailed insights explaining leading drivers of the flight forecast results, per entity (e.g. campaign or its line items")
    top_explainability_factors: Optional[list["DSPInsightFeature"]] = Field(None, alias="topExplainabilityFactors", description="Top factors affecting the forecast results, e.g. max bid, frequency cap, etc.")

    model_config = {'populate_by_name': True}


class DSPSelectedForecastMetric(StrEnum):
    AIMP = "AIMP"
    AREA = "AREA"
    CAS = "CAS"
    CPA = "CPA"
    CPC = "CPC"
    CPM = "CPM"
    DC = "DC"
    EIMP = "EIMP"
    EREA = "EREA"
    IREA = "IREA"
    ROAS = "ROAS"
    TAS = "TAS"


class DSPForecastMetric(BaseModel):
    """The forecast based on metric and periodicity."""
    metric: "DSPSelectedForecastMetric"
    periodicity: Optional["DSPForecastPeriodicity"] = None
    value: "DSPForecastValue"

    model_config = {'populate_by_name': True}


class DSPReplanning(BaseModel):
    """Recommendation for replanning."""
    content: str
    curves: Optional[list["DSPCurve"]] = None
    deliver_in_full_confidence: Optional["DSPDeliverInFullConfidence"] = Field(None, alias="deliverInFullConfidence")
    metrics: Optional[list["DSPForecastMetric"]] = None
    scenario_flight: Optional["DSPForecastFlight"] = Field(None, alias="scenarioFlight")
    scenario_type: Optional[str] = Field(None, alias="scenarioType")
    selected_metrics: Optional[list["DSPSelectedForecastMetric"]] = Field(None, alias="selectedMetrics", description="| SelectedForecastMetric | Description | | --- | --- | | `DC` | Delivery confidence. | | `TAS` | Total available spend. ")
    title: str

    model_config = {'populate_by_name': True}


class DSPWarning(BaseModel):
    """The warning message of a forecast."""
    ad_group_ids: Optional[list[str]] = Field(None, alias="adGroupIds")
    code: str
    message: str
    message_parameters: Optional[list[str]] = Field(None, alias="messageParameters")
    warning_level: Optional[int] = Field(None, alias="warningLevel")

    model_config = {'populate_by_name': True}


class DSPFlightForecast(BaseModel):
    """The forecast result of a specific flight."""
    curves: Optional[list["DSPCurve"]] = Field(None, description="The forecasting curves of a flight based on different periodicities.")
    deliver_in_full_confidence: Optional["DSPDeliverInFullConfidence"] = Field(None, alias="deliverInFullConfidence")
    flight_id: str = Field(..., alias="flightId", description="The flightId of the flight.")
    forecast_end_date_time: str = Field(..., alias="forecastEndDateTime", description="The endtime of the flight for forecasting.")
    forecast_start_date_time: str = Field(..., alias="forecastStartDateTime", description="The starttime of the flight for forecasting.")
    insights: Optional["DSPFlightForecastInsights"] = None
    metrics: Optional[list["DSPForecastMetric"]] = Field(None, description="The different metrics to measure the performance of the flight.")
    replanning: Optional[list["DSPReplanning"]] = Field(None, description="The recommendation for replanning.")
    spend: Optional[float] = Field(None, description="The amount of money spend for this flight.")
    total_budget: Optional["DSPMonetaryBudget"] = Field(None, alias="totalBudget")
    warnings: Optional[list["DSPWarning"]] = Field(None, description="Warnings of the campaign forecast.")

    model_config = {'populate_by_name': True}


class DSPState(StrEnum):
    ARCHIVED = "ARCHIVED"
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


class DSPDeliveryProfile(StrEnum):
    ASAP = "ASAP"
    EVEN = "EVEN"
    PACE_AHEAD = "PACE_AHEAD"


class DSPPacing(BaseModel):
    delivery_profile: Optional["DSPDeliveryProfile"] = Field(None, alias="deliveryProfile")

    model_config = {'populate_by_name': True}


class DSPDeliveryStatus(StrEnum):
    DELIVERING = "DELIVERING"
    LIMITED = "LIMITED"
    NOT_DELIVERING = "NOT_DELIVERING"
    UNAVAILABLE = "UNAVAILABLE"


class DSPDeliveryReason(StrEnum):
    AD_CREATIVES_NOT_RUNNING = "AD_CREATIVES_NOT_RUNNING"
    AD_GROUPS_NOT_RUNNING = "AD_GROUPS_NOT_RUNNING"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_ENDED = "AD_GROUP_ENDED"
    AD_GROUP_INELIGIBLE_GOAL_KPI = "AD_GROUP_INELIGIBLE_GOAL_KPI"
    AD_GROUP_MISSING_CONVERSION_TRACKING_SELECTIONS = "AD_GROUP_MISSING_CONVERSION_TRACKING_SELECTIONS"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_PENDING_START_DATE = "AD_GROUP_PENDING_START_DATE"
    AD_GROUP_POLICING_SUSPENDED = "AD_GROUP_POLICING_SUSPENDED"
    AD_GROUP_TOO_FEW_CONVERSION_TRACKING_SELECTIONS = "AD_GROUP_TOO_FEW_CONVERSION_TRACKING_SELECTIONS"
    AD_GROUP_TOO_MANY_CONVERSION_TRACKING_SELECTIONS = "AD_GROUP_TOO_MANY_CONVERSION_TRACKING_SELECTIONS"
    AD_NOT_APPROVED_FOR_ALL_AD_GROUPS = "AD_NOT_APPROVED_FOR_ALL_AD_GROUPS"
    AD_NOT_ASSOCIATED_WITH_AD_GROUP = "AD_NOT_ASSOCIATED_WITH_AD_GROUP"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    AD_POLICING_SUSPENDED = "AD_POLICING_SUSPENDED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_END_DATE_REACHED = "CAMPAIGN_END_DATE_REACHED"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_PENDING_START_DATE = "CAMPAIGN_PENDING_START_DATE"
    CAMPAIGN_POLICING_SUSPENDED = "CAMPAIGN_POLICING_SUSPENDED"
    OTHER = "OTHER"


class DSPStatus(BaseModel):
    delivery_reasons: Optional[list["DSPDeliveryReason"]] = Field(None, alias="deliveryReasons", description="This is the list of reasons behind the delivery status.")
    delivery_status: "DSPDeliveryStatus" = Field(..., alias="deliveryStatus")

    model_config = {'populate_by_name': True}


class DSPMarketplaceAdGroupConfigurations(BaseModel):
    pass


class DSPMarketplaceScope(StrEnum):
    SINGLE_MARKETPLACE = "SINGLE_MARKETPLACE"


class DSPOptimization(BaseModel):
    bid_strategy: Optional["DSPBidStrategy"] = Field(None, alias="bidStrategy")
    budget_settings: Optional["DSPAdGroupBudgetSettings"] = Field(None, alias="budgetSettings")

    model_config = {'populate_by_name': True}


class DSPTimeZoneType(StrEnum):
    ADVERTISER_REGION = "ADVERTISER_REGION"
    VIEWER = "VIEWER"


class DSPUserLocationSignal(StrEnum):
    CURRENT = "CURRENT"
    MULTIPLE_SIGNALS = "MULTIPLE_SIGNALS"


class DSPVideoCompletionTier(StrEnum):
    ALL_TIERS = "ALL_TIERS"
    GREATER_THAN_10_PERCENT = "GREATER_THAN_10_PERCENT"
    GREATER_THAN_20_PERCENT = "GREATER_THAN_20_PERCENT"
    GREATER_THAN_30_PERCENT = "GREATER_THAN_30_PERCENT"
    GREATER_THAN_40_PERCENT = "GREATER_THAN_40_PERCENT"
    GREATER_THAN_50_PERCENT = "GREATER_THAN_50_PERCENT"
    GREATER_THAN_60_PERCENT = "GREATER_THAN_60_PERCENT"
    GREATER_THAN_70_PERCENT = "GREATER_THAN_70_PERCENT"
    GREATER_THAN_80_PERCENT = "GREATER_THAN_80_PERCENT"
    GREATER_THAN_90_PERCENT = "GREATER_THAN_90_PERCENT"


class DSPTacticsConvertersExclusionType(StrEnum):
    NO_EXCLUSION = "NO_EXCLUSION"
    RECENT_CONVERTERS = "RECENT_CONVERTERS"


class DSPSiteLanguage(StrEnum):
    AR = "AR"
    BN = "BN"
    CS = "CS"
    DA = "DA"
    DE = "DE"
    EN = "EN"
    ES = "ES"
    FI = "FI"
    FR = "FR"
    GU = "GU"
    HI = "HI"
    IT = "IT"
    JA = "JA"
    KN = "KN"
    ML = "ML"
    MR = "MR"
    NL = "NL"
    NO = "NO"
    OTHER = "OTHER"
    PA = "PA"
    PL = "PL"
    PT = "PT"
    SV = "SV"
    TA = "TA"
    TE = "TE"
    TR = "TR"
    ZH = "ZH"


class DSPDefaultAudienceTargetingMatchType(StrEnum):
    EXACT = "EXACT"
    SIMILAR = "SIMILAR"


class DSPTargetingSettings(BaseModel):
    amazon_viewability: Optional["DSPAmazonViewability"] = Field(None, alias="amazonViewability")
    automated_targeting_tactic: Optional["DSPAutomatedTargetingTactic"] = Field(None, alias="automatedTargetingTactic")
    default_audience_targeting_match_type: Optional["DSPDefaultAudienceTargetingMatchType"] = Field(None, alias="defaultAudienceTargetingMatchType")
    enable_language_targeting: Optional[bool] = Field(None, alias="enableLanguageTargeting", description="If set to true, creatives will only target supply where the content language matches the creative language.")
    site_language: Optional["DSPSiteLanguage"] = Field(None, alias="siteLanguage")
    tactics_converters_exclusion_type: Optional["DSPTacticsConvertersExclusionType"] = Field(None, alias="tacticsConvertersExclusionType")
    targeted_pg_deal_id: Optional[str] = Field(None, alias="targetedPGDealId", description="DealId to be targeted by the Ad Group being created. If you are creating an ad group targeting a programmatic guaranteed")
    time_zone_type: Optional["DSPTimeZoneType"] = Field(None, alias="timeZoneType")
    user_location_signal: Optional["DSPUserLocationSignal"] = Field(None, alias="userLocationSignal")
    video_completion_tier: Optional["DSPVideoCompletionTier"] = Field(None, alias="videoCompletionTier")

    model_config = {'populate_by_name': True}


class DSPFeesThirdPartyProvider(StrEnum):
    COM_SCORE = "COM_SCORE"
    CPM_1 = "CPM_1"
    CPM_2 = "CPM_2"
    CPM_3 = "CPM_3"
    DOUBLE_CLICK_CAMPAIGN_MANAGER = "DOUBLE_CLICK_CAMPAIGN_MANAGER"
    DOUBLE_VERIFY = "DOUBLE_VERIFY"
    INTEGRAL_AD_SCIENCE = "INTEGRAL_AD_SCIENCE"


class DSPFeeType(StrEnum):
    AMAZON_AUDIENCE = "AMAZON_AUDIENCE"
    AMAZON_DSP = "AMAZON_DSP"
    MANAGED_SERVICE_FEE = "MANAGED_SERVICE_FEE"
    OMNICHANNEL_METRICS = "OMNICHANNEL_METRICS"
    THIRD_PARTY_APPLIED = "THIRD_PARTY_APPLIED"
    THIRD_PARTY_AUDIENCE = "THIRD_PARTY_AUDIENCE"
    THIRD_PARTY_TARGETING = "THIRD_PARTY_TARGETING"


class DSPFeeValueType(StrEnum):
    FIXED_CPM = "FIXED_CPM"
    PERCENTAGE_OF_BUDGET = "PERCENTAGE_OF_BUDGET"
    PERCENTAGE_OF_SUPPLY_COST = "PERCENTAGE_OF_SUPPLY_COST"


class DSPFee(BaseModel):
    add_to_budget_spent_amount: Optional[bool] = Field(None, alias="addToBudgetSpentAmount", description="Applies only to THIRD_PARTY_APPLIED_FEE. When set to true, third-party applied fees are are added on top of the total ad")
    currency_code: "DSPCurrencyCode" = Field(..., alias="currencyCode")
    fee_type: "DSPFeeType" = Field(..., alias="feeType")
    fee_value: float = Field(..., alias="feeValue", description="The fee amount expressed as the feeValueType. AMAZON_AUDIENCE_FEE AND THIRD_PARTY_AUDIENCE_FEE is in the currency of the")
    fee_value_type: "DSPFeeValueType" = Field(..., alias="feeValueType")
    third_party_provider: Optional["DSPFeesThirdPartyProvider"] = Field(None, alias="thirdPartyProvider")

    model_config = {'populate_by_name': True}


class DSPTag(BaseModel):
    key: str = Field(..., description="A custom key value pair entered by the advertiser.")
    value: str = Field(..., description="A custom key value pair entered by the advertiser.")

    model_config = {'populate_by_name': True}


class DSPCreativeRotationType(StrEnum):
    RANDOM = "RANDOM"
    WEIGHTED = "WEIGHTED"


class DSPMarketplace(StrEnum):
    AE = "AE"
    AU = "AU"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    SA = "SA"
    SE = "SE"
    TR = "TR"
    US = "US"


class DSPInventoryType(StrEnum):
    AAP_MOBILE_APP = "AAP_MOBILE_APP"
    AMAZON_MOBILE_DISPLAY = "AMAZON_MOBILE_DISPLAY"
    AUDIO = "AUDIO"
    AUDIO_AMAZON_DEAL = "AUDIO_AMAZON_DEAL"
    DISPLAY = "DISPLAY"
    LIVE_EVENTS = "LIVE_EVENTS"
    ONLINE_VIDEO = "ONLINE_VIDEO"
    PODCAST = "PODCAST"
    STANDARD_DISPLAY = "STANDARD_DISPLAY"
    STREAMING_TV = "STREAMING_TV"
    STREAMING_TV_AMAZON_DEAL = "STREAMING_TV_AMAZON_DEAL"
    VIDEO = "VIDEO"


class DSPFrequencyTargetingSetting(StrEnum):
    HOUSEHOLD = "HOUSEHOLD"
    USER = "USER"


class DSPTimeUnit(StrEnum):
    DAYS = "DAYS"
    HOURS = "HOURS"
    MINUTES = "MINUTES"


class DSPFrequency(BaseModel):
    event_max_count: int = Field(..., alias="eventMaxCount", description="The maximum number of times an EventType is served per user. For ADSP ad group, maximum supported value is 500.")
    frequency_targeting_setting: "DSPFrequencyTargetingSetting" = Field(..., alias="frequencyTargetingSetting")
    time_count: Optional[int] = Field(None, alias="timeCount", description="The value associated with the time and unit of time for this frequency cap.")
    time_unit: Optional["DSPTimeUnit"] = Field(None, alias="timeUnit")

    model_config = {'populate_by_name': True}


class DSPForecastAdGroup(BaseModel):
    """Ad group domain model"""
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="The unique identifier of the ad group.")
    ad_product: Optional["DSPAdProduct"] = Field(None, alias="adProduct")
    advertised_product_category_ids: Optional[list[str]] = Field(None, alias="advertisedProductCategoryIds", description="The array of identifiers of product categories associated with the ad group. For VIDEO ad group type only one parent pro")
    bid: Optional["DSPAdGroupBid"] = None
    budgets: Optional[list["DSPBudget"]] = Field(None, description="An object containing budget details for the ad group.")
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="The unique identifier of the campaign the ad group belongs to.")
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="The date time that the ad group was created.")
    creative_rotation_type: Optional["DSPCreativeRotationType"] = Field(None, alias="creativeRotationType")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The end date time for the ad group.")
    fees: Optional[list["DSPFee"]] = Field(None, description="The fees associated with the ad group.")
    frequencies: Optional[list["DSPFrequency"]] = Field(None, description="An object containing frequency details for the ad group.")
    global_ad_group_id: Optional[str] = Field(None, alias="globalAdGroupId", description="The global adGroup identifier that manages this marketplace adGroup.")
    inventory_type: Optional["DSPInventoryType"] = Field(None, alias="inventoryType")
    last_updated_date_time: Optional[str] = Field(None, alias="lastUpdatedDateTime", description="The date time that the ad group was last updated.")
    marketplace_configurations: Optional[list["DSPMarketplaceAdGroupConfigurations"]] = Field(None, alias="marketplaceConfigurations", description="List of marketplace-specific configurations for a global ad group that enables overriding certain attributes at individu")
    marketplace_scope: Optional["DSPMarketplaceScope"] = Field(None, alias="marketplaceScope")
    marketplaces: Optional[list["DSPMarketplace"]] = Field(None, description="A list of country codes representing Amazon marketplaces | Marketplace | Description | | --- | --- | | `AE` |  | | `AU` ")
    name: Optional[str] = Field(None, description="The name of the ad group.")
    optimization: Optional["DSPOptimization"] = None
    pacing: Optional["DSPPacing"] = None
    purchase_order_number: Optional[str] = Field(None, alias="purchaseOrderNumber", description="The purchase order number associated with the ad group.")
    retailer_id: Optional[str] = Field(None, alias="retailerId", description="Identifier for retailer associated with this ad group.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The start date time for the ad group.")
    state: Optional["DSPState"] = None
    status: Optional["DSPStatus"] = None
    tags: Optional[list["DSPTag"]] = Field(None, description="Open ended labels with a key value pair applied to the ad group")
    targeting_settings: Optional["DSPTargetingSettings"] = Field(None, alias="targetingSettings")

    model_config = {'populate_by_name': True}


class DSPIneligibleAutomatedTargetingTactic(BaseModel):
    """Information about an ineligible tactic key and the reasons for ineligibility"""
    pass


class DSPPrimaryInventoryType(StrEnum):
    AUDIO = "AUDIO"
    DISPLAY = "DISPLAY"
    VIDEO_OLV = "VIDEO_OLV"
    VIDEO_STV = "VIDEO_STV"


class DSPGoal(StrEnum):
    AWARENESS = "AWARENESS"
    CONSIDERATION = "CONSIDERATION"
    CONVERSIONS = "CONVERSIONS"


class DSPKPI(StrEnum):
    CLICK_THROUGH_RATE = "CLICK_THROUGH_RATE"
    COMBINED_RETURN_ON_AD_SPEND = "COMBINED_RETURN_ON_AD_SPEND"
    COST_PER_ACTION = "COST_PER_ACTION"
    COST_PER_CLICK = "COST_PER_CLICK"
    COST_PER_CONVERSION_OFF_AMAZON = "COST_PER_CONVERSION_OFF_AMAZON"
    COST_PER_DETAIL_PAGE_VIEW = "COST_PER_DETAIL_PAGE_VIEW"
    COST_PER_FIRST_APP_OPEN = "COST_PER_FIRST_APP_OPEN"
    COST_PER_INSTALL = "COST_PER_INSTALL"
    COST_PER_SIGN_UP = "COST_PER_SIGN_UP"
    COST_PER_VIDEO_COMPLETION = "COST_PER_VIDEO_COMPLETION"
    DETAIL_PAGE_VIEW_RATE = "DETAIL_PAGE_VIEW_RATE"
    FREQUENCY_AVERAGE = "FREQUENCY_AVERAGE"
    REACH = "REACH"
    RETURN_ON_AD_SPEND = "RETURN_ON_AD_SPEND"
    ROAS = "ROAS"
    ROAS_COMBINED = "ROAS_COMBINED"
    ROAS_PROMOTED = "ROAS_PROMOTED"
    TOTAL_RETURN_ON_AD_SPEND = "TOTAL_RETURN_ON_AD_SPEND"
    VIDEO_COMPLETION_RATE = "VIDEO_COMPLETION_RATE"


class DSPGoalSettings(BaseModel):
    currency_code: Optional["DSPCurrencyCode"] = Field(None, alias="currencyCode")
    goal: "DSPGoal"
    kpi: Optional["DSPKPI"] = None
    kpi_value: Optional[float] = Field(None, alias="kpiValue", description="The value of the KPI that the campaign is working to optimize.")

    model_config = {'populate_by_name': True}


class DSPCampaignOptimizations(BaseModel):
    bid_settings: Optional["DSPBidSettings"] = Field(None, alias="bidSettings")
    budget_settings: Optional["DSPBudgetSettings"] = Field(None, alias="budgetSettings")
    goal_settings: Optional["DSPGoalSettings"] = Field(None, alias="goalSettings")
    primary_inventory_types: Optional[list["DSPPrimaryInventoryType"]] = Field(None, alias="primaryInventoryTypes", description="Primary inventory type of the campaign for filtering KPIs and recommending tactics.")

    model_config = {'populate_by_name': True}


class DSPCountryCode(StrEnum):
    AE = "AE"
    AT = "AT"
    AU = "AU"
    BE = "BE"
    BH = "BH"
    BR = "BR"
    CA = "CA"
    CH = "CH"
    DE = "DE"
    DK = "DK"
    EG = "EG"
    ES = "ES"
    FI = "FI"
    FR = "FR"
    GB = "GB"
    IE = "IE"
    IL = "IL"
    IN = "IN"
    IT = "IT"
    JO = "JO"
    JP = "JP"
    KW = "KW"
    LU = "LU"
    MA = "MA"
    MX = "MX"
    NL = "NL"
    NO = "NO"
    NZ = "NZ"
    OM = "OM"
    QA = "QA"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"


class DSPTacticKey(BaseModel):
    """A tactic type paired with its compatible inventory type"""
    pass


class DSPMarketplaceCampaignConfigurations(BaseModel):
    pass


class DSPForecastCampaign(BaseModel):
    """Campaign domain model"""
    ad_product: Optional["DSPAdProduct"] = Field(None, alias="adProduct")
    adomains: Optional[list[str]] = Field(None, description="OpenRTB standard naming meaning: Advertiser domain for block list checking. This can be an array of strings for the case")
    auto_creation_settings: Optional["DSPAutoCreationSettings"] = Field(None, alias="autoCreationSettings")
    brand_id: Optional[str] = Field(None, alias="brandId", description="This is the ID of the brand that the campaign is associated with.")
    budgets: Optional[list["DSPBudget"]] = Field(None, description="The object containing budget details for the campaign (for campaigns that support multiple budgets).")
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="A unique identifier for a campaign.")
    campaign_preset_id: Optional[str] = Field(None, alias="campaignPresetId", description="This is the ID of the originally generated campaign preset that the campaign is associated with.")
    countries: Optional[list["DSPCountryCode"]] = Field(None, description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries fiel")
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="The date time that the campaign was created.")
    eligible_automated_targeting_tactics: Optional[list["DSPTacticKey"]] = Field(None, alias="eligibleAutomatedTargetingTactics", description="List of tactic type and inventory type pairs that are eligible for use with this campaign")
    end_date: Optional[str] = Field(None, alias="endDate", description="The end date of the campaign.")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The end date time for the campaign.")
    fees: Optional[list["DSPCampaignFee"]] = Field(None, description="Any fees associated with the campaign.")
    flights: Optional[list["DSPCampaignFlight"]] = Field(None, description="Flight details associated with the campaign.")
    frequencies: Optional[list["DSPFrequency"]] = Field(None, description="Any frequency caps associated with the campaign.")
    global_campaign_id: Optional[str] = Field(None, alias="globalCampaignId", description="The global campaign identifier that manages this marketplace campaign.")
    ineligible_automated_targeting_tactics: Optional[list["DSPIneligibleAutomatedTargetingTactic"]] = Field(None, alias="ineligibleAutomatedTargetingTactics", description="List of tactic type and inventory type pairs that are ineligible for use with this campaign, along with reasons for inel")
    last_updated_date_time: Optional[str] = Field(None, alias="lastUpdatedDateTime", description="The date time that the campaign was last updated.")
    marketplace_configurations: Optional[list["DSPMarketplaceCampaignConfigurations"]] = Field(None, alias="marketplaceConfigurations", description="List of marketplace-specific configurations for a global campaign that enables overriding certain attributes at individu")
    marketplace_scope: Optional["DSPMarketplaceScope"] = Field(None, alias="marketplaceScope")
    marketplaces: Optional[list["DSPMarketplace"]] = Field(None, description="A list of country codes representing Amazon marketplaces | Marketplace | Description | | --- | --- | | `AE` |  | | `AU` ")
    name: Optional[str] = Field(None, description="The name of the campaign.")
    optimizations: Optional["DSPCampaignOptimizations"] = None
    portfolio_id: Optional[str] = Field(None, alias="portfolioId", description="The ID of the portfolio associated with the campaign.")
    product_category_id: Optional[str] = Field(None, alias="productCategoryId", description="This is the ID of the product category that the campaign is associated with.")
    purchase_order_number: Optional[str] = Field(None, alias="purchaseOrderNumber", description="The purchase order number associated with the campaign.")
    skan_app_id: Optional[str] = Field(None, alias="skanAppId", description="StoreKit AdNetwork application ID. Represents iTunes application ID with which SKAN-enabled campaigns are associated.")
    start_date: Optional[str] = Field(None, alias="startDate", description="The start date of the campaign.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The start date time for the campaign.")
    state: Optional["DSPState"] = None
    status: Optional["DSPStatus"] = None
    tags: Optional[list["DSPTag"]] = Field(None, description="Open ended labels with a key value pair applied to the campaign")
    targeted_pg_deal_id: Optional[str] = Field(None, alias="targetedPGDealId", description="DealId associated with the campaign.")
    targets_amazon_deal: Optional[bool] = Field(None, alias="targetsAmazonDeal", description="If the campaign is targeting an Amazon deal, the value will be true, and the campaign and ad group(s) will be read-only.")

    model_config = {'populate_by_name': True}


class DSPMarketplaceTargetConfigurations(BaseModel):
    pass


class DSPThemeMatchType(StrEnum):
    PRODUCTS_SIMILAR_TO_ADVERTISED_PRODUCTS = "PRODUCTS_SIMILAR_TO_ADVERTISED_PRODUCTS"


class DSPThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""
    match_type: "DSPThemeMatchType" = Field(..., alias="matchType")

    model_config = {'populate_by_name': True}


class DSPProductMatchType(StrEnum):
    PRODUCT_EXACT = "PRODUCT_EXACT"


class DSPProductIdType(StrEnum):
    ASIN = "ASIN"


class DSPProductMarketplaceSetting(BaseModel):
    marketplace: "DSPMarketplace"
    product_id: str = Field(..., alias="productId", description="The product id applicable at the specified marketplace.")

    model_config = {'populate_by_name': True}


class DSPProductValue(BaseModel):
    marketplace_settings: Optional[list["DSPProductMarketplaceSetting"]] = Field(None, alias="marketplaceSettings", description="The product ids at specific marketplace level. Either the product id or the marketplace settings should always be specif")
    product_id: Optional[str] = Field(None, alias="productId", description="The product identifier. Either the product id or the marketplace settings should always be specified")

    model_config = {'populate_by_name': True}


class DSPProductTarget(BaseModel):
    """Targets a specific product."""
    match_type: "DSPProductMatchType" = Field(..., alias="matchType")
    product: "DSPProductValue"
    product_id_type: "DSPProductIdType" = Field(..., alias="productIdType")

    model_config = {'populate_by_name': True}


class DSPContentCategoryTarget(BaseModel):
    """Target based on the category of content being viewed."""
    content_category_id: str = Field(..., alias="contentCategoryId", description="The content category being targeted.")

    model_config = {'populate_by_name': True}


class DSPKeywordMatchType(StrEnum):
    BROAD = "BROAD"


class DSPKeywordTarget(BaseModel):
    """Targets a specific customer search term."""
    keyword: str = Field(..., description="The customer search term or text to target")
    match_type: "DSPKeywordMatchType" = Field(..., alias="matchType")

    model_config = {'populate_by_name': True}


class DSPLocationTarget(BaseModel):
    """Target based on geographic location."""
    location_id: str = Field(..., alias="locationId", description="The ID of the geographic location to target.")

    model_config = {'populate_by_name': True}


class DSPMobileEnvironment(StrEnum):
    APP = "APP"
    WEB = "WEB"


class DSPDeviceOrientation(StrEnum):
    LANDSCAPE = "LANDSCAPE"
    PORTRAIT = "PORTRAIT"


class DSPMobileOs(StrEnum):
    ANDROID = "ANDROID"
    IOS = "IOS"


class DSPMobileDevice(StrEnum):
    ANDROID = "ANDROID"
    IPAD = "IPAD"
    IPHONE = "IPHONE"
    KINDLE_FIRE = "KINDLE_FIRE"
    KINDLE_FIRE_HD = "KINDLE_FIRE_HD"


class DSPDeviceType(StrEnum):
    CONNECTED_DEVICE = "CONNECTED_DEVICE"
    CONNECTED_TV = "CONNECTED_TV"
    DESKTOP = "DESKTOP"
    MOBILE = "MOBILE"


class DSPDeviceTarget(BaseModel):
    """Target based on user device."""
    device_orientation: Optional["DSPDeviceOrientation"] = Field(None, alias="deviceOrientation")
    device_type: "DSPDeviceType" = Field(..., alias="deviceType")
    mobile_device: Optional["DSPMobileDevice"] = Field(None, alias="mobileDevice")
    mobile_environment: Optional["DSPMobileEnvironment"] = Field(None, alias="mobileEnvironment")
    mobile_os: Optional["DSPMobileOs"] = Field(None, alias="mobileOs")

    model_config = {'populate_by_name': True}


class DSPNativeContentPosition(StrEnum):
    IN_ARTICLE = "IN_ARTICLE"
    IN_FEED = "IN_FEED"
    PERIPHERAL = "PERIPHERAL"
    RECOMMENDATION = "RECOMMENDATION"
    UNKNOWN = "UNKNOWN"


class DSPNativeContentPositionTarget(BaseModel):
    """Targets ads to a specific native content position"""
    native_position: "DSPNativeContentPosition" = Field(..., alias="nativePosition")

    model_config = {'populate_by_name': True}


class DSPPlacementType(StrEnum):
    REWARDED = "REWARDED"


class DSPPlacementTypeTarget(BaseModel):
    """Target based on the placement type."""
    placement_type: "DSPPlacementType" = Field(..., alias="placementType")

    model_config = {'populate_by_name': True}


class DSPThirdPartyTargetType(StrEnum):
    DOUBLE_VERIFY_AUTHENTIC_ATTENTION = "DOUBLE_VERIFY_AUTHENTIC_ATTENTION"
    DOUBLE_VERIFY_AUTHENTIC_BRAND_SAFETY = "DOUBLE_VERIFY_AUTHENTIC_BRAND_SAFETY"
    DOUBLE_VERIFY_BRAND_SAFETY = "DOUBLE_VERIFY_BRAND_SAFETY"
    DOUBLE_VERIFY_CUSTOM_CONTEXTUAL_SEGMENT_ID = "DOUBLE_VERIFY_CUSTOM_CONTEXTUAL_SEGMENT_ID"
    DOUBLE_VERIFY_FRAUD_INVALID_TRAFFIC = "DOUBLE_VERIFY_FRAUD_INVALID_TRAFFIC"
    DOUBLE_VERIFY_STANDARD_DISPLAY_BRAND_SAFETY = "DOUBLE_VERIFY_STANDARD_DISPLAY_BRAND_SAFETY"
    DOUBLE_VERIFY_VIEWABILITY = "DOUBLE_VERIFY_VIEWABILITY"
    INTEGRAL_AD_SCIENCE_BRAND_SAFETY = "INTEGRAL_AD_SCIENCE_BRAND_SAFETY"
    INTEGRAL_AD_SCIENCE_CONTEXTUAL_AVOIDANCE = "INTEGRAL_AD_SCIENCE_CONTEXTUAL_AVOIDANCE"
    INTEGRAL_AD_SCIENCE_CONTEXTUAL_TARGETING = "INTEGRAL_AD_SCIENCE_CONTEXTUAL_TARGETING"
    INTEGRAL_AD_SCIENCE_FRAUD_INVALID_TRAFFIC = "INTEGRAL_AD_SCIENCE_FRAUD_INVALID_TRAFFIC"
    INTEGRAL_AD_SCIENCE_QUALITY_SYNC = "INTEGRAL_AD_SCIENCE_QUALITY_SYNC"
    INTEGRAL_AD_SCIENCE_VIEWABILITY = "INTEGRAL_AD_SCIENCE_VIEWABILITY"
    NEWS_GUARD_BRAND_GUARD_MISINFORMATION_SAFETY = "NEWS_GUARD_BRAND_GUARD_MISINFORMATION_SAFETY"
    NEWS_GUARD_BRAND_GUARD_TRUSTED_NEWS_TARGETING = "NEWS_GUARD_BRAND_GUARD_TRUSTED_NEWS_TARGETING"
    PIXALATE_FRAUD_INVALID_TRAFFIC = "PIXALATE_FRAUD_INVALID_TRAFFIC"


class DSPIntegralAdScienceContextualAvoidance(BaseModel):
    avoidance_segments: Optional[list[str]] = Field(None, alias="avoidanceSegments", description="The unique identifier of the IAS contextual avoidance segment")

    model_config = {'populate_by_name': True}


class DSPIASFraudInvalidTrafficType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_MODERATE_RISK = "FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_MODERATE_RISK"
    FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_RISK = "FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_RISK"


class DSPIntegralAdScienceFraudInvalidTraffic(BaseModel):
    target_setting: Optional["DSPIASFraudInvalidTrafficType"] = Field(None, alias="targetSetting")

    model_config = {'populate_by_name': True}


class DSPDoubleVerifyCustomContextualSegmentId(BaseModel):
    double_verify_segment_id: Optional[str] = Field(None, alias="doubleVerifySegmentId")

    model_config = {'populate_by_name': True}


class DSPViewabilityTierType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    VIEWABILITY_TIER_GT_40 = "VIEWABILITY_TIER_GT_40"
    VIEWABILITY_TIER_GT_50 = "VIEWABILITY_TIER_GT_50"
    VIEWABILITY_TIER_GT_60 = "VIEWABILITY_TIER_GT_60"
    VIEWABILITY_TIER_GT_70 = "VIEWABILITY_TIER_GT_70"
    VIEWABILITY_TIER_LT_40 = "VIEWABILITY_TIER_LT_40"


class DSPIASViewabilityStandardType(StrEnum):
    GROUPM = "GROUPM"
    MRC = "MRC"
    NONE = "NONE"
    PUBLICIS = "PUBLICIS"


class DSPIntegralAdScienceViewability(BaseModel):
    """The IAS viewability standard."""
    standard: "DSPIASViewabilityStandardType"
    viewability_targeting: Optional["DSPViewabilityTierType"] = Field(None, alias="viewabilityTargeting")

    model_config = {'populate_by_name': True}


class DSPIntegralAdScienceQualitySync(BaseModel):
    segment_id: Optional[str] = Field(None, alias="segmentId")

    model_config = {'populate_by_name': True}


class DSPDoubleVerifyAuthenticBrandSafety(BaseModel):
    double_verify_segment_id: Optional[str] = Field(None, alias="doubleVerifySegmentId")

    model_config = {'populate_by_name': True}


class DSPExcludeAppsAndSitesType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    FRAUD_TRAFFIC_LEVEL_GTE_02 = "FRAUD_TRAFFIC_LEVEL_GTE_02"
    FRAUD_TRAFFIC_LEVEL_GTE_04 = "FRAUD_TRAFFIC_LEVEL_GTE_04"
    FRAUD_TRAFFIC_LEVEL_GTE_06 = "FRAUD_TRAFFIC_LEVEL_GTE_06"
    FRAUD_TRAFFIC_LEVEL_GTE_08 = "FRAUD_TRAFFIC_LEVEL_GTE_08"
    FRAUD_TRAFFIC_LEVEL_GTE_10 = "FRAUD_TRAFFIC_LEVEL_GTE_10"
    FRAUD_TRAFFIC_LEVEL_GTE_100 = "FRAUD_TRAFFIC_LEVEL_GTE_100"
    FRAUD_TRAFFIC_LEVEL_GTE_25 = "FRAUD_TRAFFIC_LEVEL_GTE_25"
    FRAUD_TRAFFIC_LEVEL_GTE_50 = "FRAUD_TRAFFIC_LEVEL_GTE_50"


class DSPDoubleVerifyFraudInvalidTraffic(BaseModel):
    block_app_and_sites: Optional[bool] = Field(None, alias="blockAppAndSites", description="Set to true to block applications and sites with insufficient historical fraud and invalid traffic statistics. This will")
    exclude_apps_and_sites: Optional["DSPExcludeAppsAndSitesType"] = Field(None, alias="excludeAppsAndSites")
    exclude_impressions: Optional[bool] = Field(None, alias="excludeImpressions", description="Set to true to exclude impressions delivered to devices identified to be fraudulent or invalid.")

    model_config = {'populate_by_name': True}


class DSPIntegralAdScienceContextualTargeting(BaseModel):
    topical_segments: Optional[list[str]] = Field(None, alias="topicalSegments", description="The unique identifier of the IAS contextual topical targeting segment")
    vertical_segments: Optional[list[str]] = Field(None, alias="verticalSegments", description="The unique identifier of the IAS contextual vertical targeting segment")

    model_config = {'populate_by_name': True}


class DSPDVBrandSafetyAppStarRatingType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    APP_STAR_RATING_LT_1_POINT_5_STARS = "APP_STAR_RATING_LT_1_POINT_5_STARS"
    APP_STAR_RATING_LT_2_POINT_5_STARS = "APP_STAR_RATING_LT_2_POINT_5_STARS"
    APP_STAR_RATING_LT_2_STARS = "APP_STAR_RATING_LT_2_STARS"
    APP_STAR_RATING_LT_3_POINT_5_STARS = "APP_STAR_RATING_LT_3_POINT_5_STARS"
    APP_STAR_RATING_LT_3_STARS = "APP_STAR_RATING_LT_3_STARS"
    APP_STAR_RATING_LT_4_POINT_5_STARS = "APP_STAR_RATING_LT_4_POINT_5_STARS"
    APP_STAR_RATING_LT_4_STARS = "APP_STAR_RATING_LT_4_STARS"


class DSPDVBrandSafetyContentCategoriesWithRiskMap(BaseModel):
    """A map from content categories to risk level to exclude from targeting. Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISAS"""
    key: str = Field(..., description="Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATUR")
    value: "DSPBrandSuitabilityRiskLevelType"

    model_config = {'populate_by_name': True}


class DSPDVBrandSafetyContentCategoryType(StrEnum):
    AD_SERVER = "AD_SERVER"
    CELEBRITY_GOSSIP = "CELEBRITY_GOSSIP"
    CULTS_SURVIVALISM = "CULTS_SURVIVALISM"
    EXTREME_GRAPHIC = "EXTREME_GRAPHIC"
    GAMBLING = "GAMBLING"
    INCENTIVIZED_MALWARE_CLUTTER = "INCENTIVIZED_MALWARE_CLUTTER"
    INFLAMMATORY_POLITICS_NEWS = "INFLAMMATORY_POLITICS_NEWS"
    NEGATIVE_NEWS_FINANCIAL = "NEGATIVE_NEWS_FINANCIAL"
    NEGATIVE_NEWS_PHARMACEUTICAL = "NEGATIVE_NEWS_PHARMACEUTICAL"
    NON_STANDARD_CONTENT_NON_ENGLISH = "NON_STANDARD_CONTENT_NON_ENGLISH"
    NON_STANDARD_CONTENT_PARKING_PAGE = "NON_STANDARD_CONTENT_PARKING_PAGE"
    OCCULT = "OCCULT"
    PIRACY_COPYRIGHT_INFRINGEMENT = "PIRACY_COPYRIGHT_INFRINGEMENT"
    UNMODERATED_UGC_FORUMS_IMAGES_VIDEO = "UNMODERATED_UGC_FORUMS_IMAGES_VIDEO"


class DSPDVBrandSafetyAppAgeRatingType(StrEnum):
    ADULTS_ONLY_18_PLUS = "ADULTS_ONLY_18_PLUS"
    EVERYONE_4_PLUS = "EVERYONE_4_PLUS"
    MATURE_17_PLUS = "MATURE_17_PLUS"
    TEENS_12_PLUS = "TEENS_12_PLUS"
    TWEENS_9_PLUS = "TWEENS_9_PLUS"
    UNKNOWN = "UNKNOWN"


class DSPDoubleVerifyBrandSafety(BaseModel):
    app_age_rating: Optional[list["DSPDVBrandSafetyAppAgeRatingType"]] = Field(None, alias="appAgeRating", description="A list of app age ratings to be used for excluding apps. For example, TEENS_12_PLUS will only exclude apps with content ")
    app_star_rating: Optional["DSPDVBrandSafetyAppStarRatingType"] = Field(None, alias="appStarRating")
    content_categories: Optional[list["DSPDVBrandSafetyContentCategoryType"]] = Field(None, alias="contentCategories", description="A list of content categories to exclude from targeting.")
    content_categories_with_risk: Optional[list["DSPDVBrandSafetyContentCategoriesWithRiskMap"]] = Field(None, alias="contentCategoriesWithRisk")
    exclude_apps_with_insufficient_rating: Optional[bool] = Field(None, alias="excludeAppsWithInsufficientRating", description="Set to true to exclude unofficial apps or apps with insufficient user ratings (<100 lifetime).")
    unknown_content: Optional[bool] = Field(None, alias="unknownContent", description="Set to true to exclude unknown content.")

    model_config = {'populate_by_name': True}


class DSPPixalateFraudInvalidTraffic(BaseModel):
    exclude_apps_and_domains: Optional[bool] = Field(None, alias="excludeAppsAndDomains", description="Set to true to exclude traffic from Apps and Domains identified to be fraudulent or invalid.")
    exclude_ip_address_and_user_agents: Optional[bool] = Field(None, alias="excludeIpAddressAndUserAgents", description="Set to true to exclude traffic from IPV4 and IPV6 addresses and user agents identified to be fraudulent or invalid.")
    exclude_ott_and_mobile_devices: Optional[bool] = Field(None, alias="excludeOttAndMobileDevices", description="Set to true to exclude traffic from OTT and Mobile devices identified to be fraudulent or invalid.")
    exclude_removed_apps_from_app_stores: Optional[bool] = Field(None, alias="excludeRemovedAppsFromAppStores", description="Set to true to exlude traffic from Apps that have been removed from the google play and apple app stores in the last 6 m")

    model_config = {'populate_by_name': True}


class DSPNewsGuardBrandGuardTrustedNewsTargetingType(StrEnum):
    BASIC_INCLUDE = "BASIC_INCLUDE"
    BUSINESS_INCLUDE = "BUSINESS_INCLUDE"
    COMMUNITY_INCLUDE = "COMMUNITY_INCLUDE"
    HEALTH_INCLUDE = "HEALTH_INCLUDE"
    HIGH_INCLUDE = "HIGH_INCLUDE"
    LIFESTYLE_INCLUDE = "LIFESTYLE_INCLUDE"
    LOCAL_INCLUDE = "LOCAL_INCLUDE"
    MAX_INCLUDE = "MAX_INCLUDE"
    POLITICS_INCLUDE = "POLITICS_INCLUDE"
    TECH_INCLUDE = "TECH_INCLUDE"


class DSPNewsGuardBrandGuardTrustedNewsTargeting(BaseModel):
    """Only applicable for Web supply."""
    targeting_list: Optional[list["DSPNewsGuardBrandGuardTrustedNewsTargetingType"]] = Field(None, alias="targetingList", description="The unique identifiers of trusted news targets")

    model_config = {'populate_by_name': True}


class DSPDoubleVerifyStandardDisplayBrandSafety(BaseModel):
    content_categories: Optional[list["DSPDVBrandSafetyContentCategoryType"]] = Field(None, alias="contentCategories", description="A list of content categories to exclude from targeting.")
    content_categories_with_risk: Optional[list["DSPDVBrandSafetyContentCategoriesWithRiskMap"]] = Field(None, alias="contentCategoriesWithRisk")
    unknown_content: Optional[bool] = Field(None, alias="unknownContent", description="Set to true to exclude unknown content.")

    model_config = {'populate_by_name': True}


class DSPIASBrandSafetyLevelType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    BRAND_SAFETY_EXCLUDE_HIGH_AND_MODERATE_RISK = "BRAND_SAFETY_EXCLUDE_HIGH_AND_MODERATE_RISK"
    BRAND_SAFETY_EXCLUDE_HIGH_RISK = "BRAND_SAFETY_EXCLUDE_HIGH_RISK"


class DSPIntegralAdScienceBrandSafety(BaseModel):
    exclude_content: Optional[bool] = Field(None, alias="excludeContent", description="Set to true to exclude content that Integral Ad Science is not able to rate.")
    ias_brand_safety_adult: Optional["DSPIASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyAdult")
    ias_brand_safety_alcohol: Optional["DSPIASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyAlcohol")
    ias_brand_safety_gambling: Optional["DSPIASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyGambling")
    ias_brand_safety_hate_speech: Optional["DSPIASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyHateSpeech")
    ias_brand_safety_illegal_downloads: Optional["DSPIASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyIllegalDownloads")
    ias_brand_safety_illegal_drugs: Optional["DSPIASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyIllegalDrugs")
    ias_brand_safety_offensive_language: Optional["DSPIASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyOffensiveLanguage")
    ias_brand_safety_violence: Optional["DSPIASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyViolence")

    model_config = {'populate_by_name': True}


class DSPDoubleVerifyAuthenticAttention(BaseModel):
    universal_attention: bool = Field(..., alias="universalAttention", description="One omni-channel segment that is informed by data from all DV campaigns to help avoid serving ads on generally poor perf")

    model_config = {'populate_by_name': True}


class DSPNewsGuardBrandGuardMisinformationSafetyType(StrEnum):
    AI_GENERATED_MFA = "AI_GENERATED_MFA"
    BASIC_EXCLUDE = "BASIC_EXCLUDE"
    CLIMATE_MISINFORMATION = "CLIMATE_MISINFORMATION"
    COVID_MISINFORMATION = "COVID_MISINFORMATION"
    ELECTION_MISINFORMATION = "ELECTION_MISINFORMATION"
    HEALTH_MISINFORMATION = "HEALTH_MISINFORMATION"
    HIGH_EXCLUDE = "HIGH_EXCLUDE"
    ISRAEL_HAMAS_MISINFORMATION = "ISRAEL_HAMAS_MISINFORMATION"
    MAX_EXCLUDE = "MAX_EXCLUDE"
    MISINFORMATION_SITES = "MISINFORMATION_SITES"
    OPINIONATED_NEWS = "OPINIONATED_NEWS"
    QANON_MISINFORMATION = "QANON_MISINFORMATION"
    UKRAINE_MISINFORMATION = "UKRAINE_MISINFORMATION"
    VACCINE_MISINFORMATION = "VACCINE_MISINFORMATION"


class DSPNewsGuardBrandGuardMisinformationSafety(BaseModel):
    avoidance_list: Optional[list["DSPNewsGuardBrandGuardMisinformationSafetyType"]] = Field(None, alias="avoidanceList", description="The unique identifiers of misinformation targets")

    model_config = {'populate_by_name': True}


class DSPMrcViewabilityTargetingType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    MRC_VIEWABILITY_GTE_30 = "MRC_VIEWABILITY_GTE_30"
    MRC_VIEWABILITY_GTE_40 = "MRC_VIEWABILITY_GTE_40"
    MRC_VIEWABILITY_GTE_50 = "MRC_VIEWABILITY_GTE_50"
    MRC_VIEWABILITY_GTE_55 = "MRC_VIEWABILITY_GTE_55"
    MRC_VIEWABILITY_GTE_60 = "MRC_VIEWABILITY_GTE_60"
    MRC_VIEWABILITY_GTE_65 = "MRC_VIEWABILITY_GTE_65"
    MRC_VIEWABILITY_GTE_70 = "MRC_VIEWABILITY_GTE_70"
    MRC_VIEWABILITY_GTE_75 = "MRC_VIEWABILITY_GTE_75"
    MRC_VIEWABILITY_GTE_80 = "MRC_VIEWABILITY_GTE_80"


class DSPDoubleVerifyViewability(BaseModel):
    average_completion_and_fully_viewable_rate_targeting: Optional["DSPAverageCompletionAndFullyViewableRateTargetingType"] = Field(None, alias="averageCompletionAndFullyViewableRateTargeting")
    brand_exposure_viewability_targeting: Optional["DSPBrandExposureViewabilityTargetingType"] = Field(None, alias="brandExposureViewabilityTargeting")
    include_unmeasurable_impressions: Optional[bool] = Field(None, alias="includeUnmeasurableImpressions", description="Set to true to include impressions where impressions can't be measured.")
    mrc_viewability_targeting: Optional["DSPMrcViewabilityTargetingType"] = Field(None, alias="mrcViewabilityTargeting")

    model_config = {'populate_by_name': True}


class DSPThirdPartyTargetDetails(BaseModel):
    pass


class DSPThirdPartyTarget(BaseModel):
    third_party_target_details: "DSPThirdPartyTargetDetails" = Field(..., alias="thirdPartyTargetDetails")
    third_party_target_type: "DSPThirdPartyTargetType" = Field(..., alias="thirdPartyTargetType")

    model_config = {'populate_by_name': True}


class DSPInventorySourceType(StrEnum):
    AMAZON = "AMAZON"
    APD = "APD"
    DEAL = "DEAL"
    INVENTORY_GROUP = "INVENTORY_GROUP"
    THIRD_PARTY_EXCHANGE = "THIRD_PARTY_EXCHANGE"


class DSPInventorySourceTarget(BaseModel):
    """Target based on the source of the inventory."""
    inventory_source_id: "DSPMarketplaceStringValue" = Field(..., alias="inventorySourceId")
    inventory_source_type: "DSPInventorySourceType" = Field(..., alias="inventorySourceType")

    model_config = {'populate_by_name': True}


class DSPContentGenre(StrEnum):
    ACTION = "ACTION"
    ADVENTURE = "ADVENTURE"
    ALTERNATIVE_ROCK = "ALTERNATIVE_ROCK"
    ANIMATION = "ANIMATION"
    ARTS = "ARTS"
    BIOGRAPHY = "BIOGRAPHY"
    BLUES = "BLUES"
    BUSINESS = "BUSINESS"
    CHILDRENS_MUSIC = "CHILDRENS_MUSIC"
    CHRISTIAN_GOSPEL = "CHRISTIAN_GOSPEL"
    CHRISTMAS_HOLIDAY = "CHRISTMAS_HOLIDAY"
    CLASSICAL = "CLASSICAL"
    CLASSIC_ROCK = "CLASSIC_ROCK"
    COLLEGE_RADIO = "COLLEGE_RADIO"
    COMEDY = "COMEDY"
    COUNTRY = "COUNTRY"
    CRIME = "CRIME"
    DANCE_DJ = "DANCE_DJ"
    DOCUMENTARY = "DOCUMENTARY"
    DRAMA = "DRAMA"
    EASY_LISTENING = "EASY_LISTENING"
    EDUCATION = "EDUCATION"
    EUROPEAN_POP_FOLK = "EUROPEAN_POP_FOLK"
    FAMILY = "FAMILY"
    FANTASY = "FANTASY"
    FICTION = "FICTION"
    FILM_NOIR = "FILM_NOIR"
    FOLK = "FOLK"
    FRENCH_VARIETY = "FRENCH_VARIETY"
    GAME_SHOW = "GAME_SHOW"
    GENRE_NOT_AVAILABLE = "GENRE_NOT_AVAILABLE"
    GERMAN_ROCK_POP = "GERMAN_ROCK_POP"
    GOVERNMENT = "GOVERNMENT"
    HARD_ROCK_METAL = "HARD_ROCK_METAL"
    HEALTH_AND_FITNESS = "HEALTH_AND_FITNESS"
    HISTORY = "HISTORY"
    HORROR = "HORROR"
    INTERNATIONAL = "INTERNATIONAL"
    JAPANESE = "JAPANESE"
    JAZZ = "JAZZ"
    KIDS_AND_FAMILY = "KIDS_AND_FAMILY"
    LATIN_MUSIC = "LATIN_MUSIC"
    LEISURE = "LEISURE"
    MISCELLANEOUS = "MISCELLANEOUS"
    MUSIC = "MUSIC"
    MUSICAL = "MUSICAL"
    MUSICALS_CABARET = "MUSICALS_CABARET"
    MYSTERY = "MYSTERY"
    NEWS = "NEWS"
    NEW_AGE = "NEW_AGE"
    OLDIES_ADULT_STANDARDS = "OLDIES_ADULT_STANDARDS"
    POP = "POP"
    RAP_HIP_HOP = "RAP_HIP_HOP"
    RB = "RB"
    REALITY_TV = "REALITY_TV"
    REGGAE_ISLAND = "REGGAE_ISLAND"
    RELIGION_AND_SPIRITUALITY = "RELIGION_AND_SPIRITUALITY"
    ROCK = "ROCK"
    ROMANCE = "ROMANCE"
    SCIENCE = "SCIENCE"
    SCIENCE_FICTION = "SCIENCE_FICTION"
    SHORT = "SHORT"
    SOCIETY_AND_CULTURE = "SOCIETY_AND_CULTURE"
    SOUNDTRACKS = "SOUNDTRACKS"
    SPORT = "SPORT"
    SUPER_HERO = "SUPER_HERO"
    TALK_SHOW = "TALK_SHOW"
    TECHNOLOGY = "TECHNOLOGY"
    THRILLER = "THRILLER"
    TRUE_CRIME = "TRUE_CRIME"
    TV_AND_FILM = "TV_AND_FILM"
    WAR = "WAR"
    WESTERN = "WESTERN"


class DSPContentGenreTarget(BaseModel):
    """Target based on the genre of content being viewed."""
    content_genre: "DSPContentGenre" = Field(..., alias="contentGenre")

    model_config = {'populate_by_name': True}


class DSPVideoContentDuration(StrEnum):
    EXTENDED = "EXTENDED"
    LONG = "LONG"
    MEDIUM = "MEDIUM"
    SHORT = "SHORT"
    UNKNOWN = "UNKNOWN"


class DSPVideoContentDurationTarget(BaseModel):
    """Targets ads to a specific video content duration"""
    duration: "DSPVideoContentDuration"

    model_config = {'populate_by_name': True}


class DSPContentOutstreamPosition(StrEnum):
    ACCOMPANYING_CONTENT = "ACCOMPANYING_CONTENT"
    INTERSTITIAL = "INTERSTITIAL"
    STANDALONE = "STANDALONE"
    UNKNOWN = "UNKNOWN"


class DSPContentOutstreamPositionTarget(BaseModel):
    """Targets ads in the specified content outstream position"""
    outstream_position: "DSPContentOutstreamPosition" = Field(..., alias="outstreamPosition")

    model_config = {'populate_by_name': True}


class DSPFoldPosition(StrEnum):
    ABOVE_THE_FOLD = "ABOVE_THE_FOLD"
    BELOW_THE_FOLD = "BELOW_THE_FOLD"
    UNKNOWN = "UNKNOWN"


class DSPFoldPositionTarget(BaseModel):
    """Targets ads in the specified fold position"""
    fold_position: "DSPFoldPosition" = Field(..., alias="foldPosition")

    model_config = {'populate_by_name': True}


class DSPVideoAdFormat(StrEnum):
    FULL_EPISODE_PLAYER = "FULL_EPISODE_PLAYER"
    INSTREAM = "INSTREAM"
    OUTSTREAM = "OUTSTREAM"


class DSPVideoAdFormatTarget(BaseModel):
    """Target based on the video ad format."""
    video_ad_format: "DSPVideoAdFormat" = Field(..., alias="videoAdFormat")

    model_config = {'populate_by_name': True}


class DSPContentRatingTypes(StrEnum):
    DSP_CONTENT_RATING = "DSP_CONTENT_RATING"
    TWITCH_CONTENT_RATING = "TWITCH_CONTENT_RATING"


class DSPDspContentRatingEnum(StrEnum):
    RATING_NOT_AVAILABLE = "RATING_NOT_AVAILABLE"
    SUITABLE_FOR_ADULTS = "SUITABLE_FOR_ADULTS"
    SUITABLE_FOR_ALL_AUDIENCES = "SUITABLE_FOR_ALL_AUDIENCES"
    SUITABLE_FOR_MATURE_AUDIENCES = "SUITABLE_FOR_MATURE_AUDIENCES"
    SUITABLE_FOR_MOST_AUDIENCES_WITH_PARENTAL_GUIDANCE = "SUITABLE_FOR_MOST_AUDIENCES_WITH_PARENTAL_GUIDANCE"
    SUITABLE_FOR_TEEN_AND_OLDER_AUDIENCES = "SUITABLE_FOR_TEEN_AND_OLDER_AUDIENCES"


class DSPDspContentRating(BaseModel):
    dsp_content_rating: "DSPDspContentRatingEnum" = Field(..., alias="dspContentRating")

    model_config = {'populate_by_name': True}


class DSPTwitchContentRatingEnum(StrEnum):
    TWITCH_MODERATE = "TWITCH_MODERATE"
    TWITCH_RESTRICTIVE = "TWITCH_RESTRICTIVE"


class DSPTwitchContentRating(BaseModel):
    twitch_content_rating: "DSPTwitchContentRatingEnum" = Field(..., alias="twitchContentRating")

    model_config = {'populate_by_name': True}


class DSPContentRating(BaseModel):
    pass


class DSPContentRatingTarget(BaseModel):
    """Target based on the rating of content being viewed."""
    content_rating_type: "DSPContentRatingTypes" = Field(..., alias="contentRatingType")
    content_rating_type_details: "DSPContentRating" = Field(..., alias="contentRatingTypeDetails")

    model_config = {'populate_by_name': True}


class DSPContentInstreamPosition(StrEnum):
    MID_ROLL = "MID_ROLL"
    POST_ROLL = "POST_ROLL"
    PRE_ROLL = "PRE_ROLL"
    UNKNOWN = "UNKNOWN"


class DSPContentInstreamPositionTarget(BaseModel):
    """Targets ads in the specified content instream position"""
    instream_position: "DSPContentInstreamPosition" = Field(..., alias="instreamPosition")

    model_config = {'populate_by_name': True}


class DSPDayOfWeek(StrEnum):
    FRIDAY = "FRIDAY"
    MONDAY = "MONDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"
    THURSDAY = "THURSDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"


class DSPTimeOfDay(BaseModel):
    end_time: str = Field(..., alias="endTime", description="Selected end time")
    start_time: str = Field(..., alias="startTime", description="Selected start time")

    model_config = {'populate_by_name': True}


class DSPDayPartTarget(BaseModel):
    """Target based on time of day."""
    day_of_week: "DSPDayOfWeek" = Field(..., alias="dayOfWeek")
    time_of_day: "DSPTimeOfDay" = Field(..., alias="timeOfDay")

    model_config = {'populate_by_name': True}


class DSPDomainNameTarget(BaseModel):
    """Targets domains based on URL."""
    domain_name: str = Field(..., alias="domainName", description="The URL of the domain to target.")

    model_config = {'populate_by_name': True}


class DSPDomainListTarget(BaseModel):
    """Targets domains based on an existing domain list."""
    domain_list_id: str = Field(..., alias="domainListId", description="The ID of the domain list to target.")

    model_config = {'populate_by_name': True}


class DSPDomainFileTarget(BaseModel):
    """Targets domains based on list provided via file upload."""
    domain_file_id: Optional[str] = Field(None, alias="domainFileId", description="The ID associated to the domain file to target. Read-only and created based on the inputted domainFileKey.")
    domain_file_key: Optional[str] = Field(None, alias="domainFileKey", description="The S3 key of the uploaded file which can be obtained from the file upload policy endpoint. A max of 10 files may be ass")
    domain_file_name: Optional[str] = Field(None, alias="domainFileName", description="The name of the file.")
    domain_file_url: Optional[str] = Field(None, alias="domainFileUrl", description="The file containing the domains uploaded. It expires in one hour.")

    model_config = {'populate_by_name': True}


class DSPDomainTargetDetails(BaseModel):
    pass


class DSPDomainTargetTypes(StrEnum):
    ADVERTISER_DOMAIN_LIST = "ADVERTISER_DOMAIN_LIST"
    DOMAIN_FILE = "DOMAIN_FILE"
    DOMAIN_LIST = "DOMAIN_LIST"
    DOMAIN_NAME = "DOMAIN_NAME"


class DSPDomainTarget(BaseModel):
    """Target based on a specified domain."""
    domain_target_details: "DSPDomainTargetDetails" = Field(..., alias="domainTargetDetails")
    domain_target_type: "DSPDomainTargetTypes" = Field(..., alias="domainTargetType")

    model_config = {'populate_by_name': True}


class DSPProductCategoryRefinement(BaseModel):
    product_category_id: Optional[str] = Field(None, alias="productCategoryId", description="The product category ID to target.")

    model_config = {'populate_by_name': True}


class DSPProductCategoryRefinementValue(BaseModel):
    product_category_refinement: Optional["DSPProductCategoryRefinement"] = Field(None, alias="productCategoryRefinement")

    model_config = {'populate_by_name': True}


class DSPProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""
    product_category_refinement: "DSPProductCategoryRefinementValue" = Field(..., alias="productCategoryRefinement")

    model_config = {'populate_by_name': True}


class DSPTargetDetails(BaseModel):
    pass


class DSPTargetLevel(StrEnum):
    AD_GROUP = "AD_GROUP"


class DSPTargetType(StrEnum):
    AD_INITIATION = "AD_INITIATION"
    AD_PLAYER_SIZE = "AD_PLAYER_SIZE"
    APP = "APP"
    AUDIENCE = "AUDIENCE"
    BRAND_SAFETY_CATEGORY = "BRAND_SAFETY_CATEGORY"
    BRAND_SAFETY_TIER = "BRAND_SAFETY_TIER"
    CONTENT_CATEGORY = "CONTENT_CATEGORY"
    CONTENT_GENRE = "CONTENT_GENRE"
    CONTENT_INSTREAM_POSITION = "CONTENT_INSTREAM_POSITION"
    CONTENT_OUTSTREAM_POSITION = "CONTENT_OUTSTREAM_POSITION"
    CONTENT_RATING = "CONTENT_RATING"
    DAYPART = "DAYPART"
    DEVICE = "DEVICE"
    DOMAIN = "DOMAIN"
    FOLD_POSITION = "FOLD_POSITION"
    INVENTORY_SOURCE = "INVENTORY_SOURCE"
    KEYWORD = "KEYWORD"
    LOCATION = "LOCATION"
    NATIVE_CONTENT_POSITION = "NATIVE_CONTENT_POSITION"
    PLACEMENT_TYPE = "PLACEMENT_TYPE"
    PRODUCT = "PRODUCT"
    PRODUCT_CATEGORY = "PRODUCT_CATEGORY"
    THEME = "THEME"
    THIRD_PARTY = "THIRD_PARTY"
    VIDEO_AD_FORMAT = "VIDEO_AD_FORMAT"
    VIDEO_CONTENT_DURATION = "VIDEO_CONTENT_DURATION"


class DSPTargetBid(BaseModel):
    pass


class DSPForecastTarget(BaseModel):
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.")
    ad_product: Optional["DSPAdProduct"] = Field(None, alias="adProduct")
    bid: Optional["DSPTargetBid"] = None
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.")
    creation_date_time: Optional[str] = Field(None, alias="creationDateTime", description="The date time the target was created.")
    global_target_id: Optional[str] = Field(None, alias="globalTargetId", description="The global target identifier that manages this marketplace target.")
    last_updated_date_time: Optional[str] = Field(None, alias="lastUpdatedDateTime", description="The date time the target was last updated.")
    marketplace_configurations: Optional[list["DSPMarketplaceTargetConfigurations"]] = Field(None, alias="marketplaceConfigurations", description="List of marketplace-specific configurations for a global target that enables overriding certain attributes at individual")
    marketplace_scope: Optional["DSPMarketplaceScope"] = Field(None, alias="marketplaceScope")
    marketplaces: Optional[list["DSPMarketplace"]] = Field(None, description="A list of country codes representing Amazon marketplaces | Marketplace | Description | | --- | --- | | `AE` |  | | `AU` ")
    negative: Optional[bool] = Field(None, description="Indicates whether the target is negative or not.")
    state: Optional["DSPState"] = None
    status: Optional["DSPStatus"] = None
    tags: Optional[list["DSPTag"]] = Field(None, description="Open ended labels with a key value pair applied to the target")
    target_details: Optional["DSPTargetDetails"] = Field(None, alias="targetDetails")
    target_id: Optional[str] = Field(None, alias="targetId", description="A unique identifier for the target.")
    target_level: Optional["DSPTargetLevel"] = Field(None, alias="targetLevel")
    target_type: Optional["DSPTargetType"] = Field(None, alias="targetType")

    model_config = {'populate_by_name': True}


class DSPReplanningSettings(BaseModel):
    """Forecast request of a campaign, adGroups, flights, and targets with adjusted settings."""
    ad_groups: Optional[list["DSPForecastAdGroup"]] = Field(None, alias="adGroups")
    campaign: Optional["DSPForecastCampaign"] = None
    flights: Optional[list["DSPForecastFlight"]] = None
    targets: Optional[list["DSPForecastTarget"]] = None

    model_config = {'populate_by_name': True}


class DSPForecastMetricsDescription(BaseModel):
    """Describe how user select to see all metrics or selected ones."""
    all_metrics: bool = Field(..., alias="allMetrics", description="If it is true, all the supported metrics would return.")
    selected_metrics: Optional[list["DSPSelectedForecastMetric"]] = Field(None, alias="selectedMetrics", description="The list of selected metrics in order.")

    model_config = {'populate_by_name': True}


class DSPEnabledFeaturesInCampaignForecast(BaseModel):
    """For the user to specify which features to enable in the forecast result."""
    campaign_settings_cache: Optional[bool] = Field(None, alias="campaignSettingsCache", description="Describe if the forecast will use cached settings of a campaign.")
    curve: Optional[bool] = Field(None, description="Describe if the user want to see curve or not.")
    insights: Optional[bool] = Field(None, description="Describe if the user want to see detailed insights for leading drivers of forecast results.")
    metrics: Optional["DSPForecastMetricsDescription"] = None
    replanning: Optional[bool] = Field(None, description="Describe if the forecast will show replanning recommendation.")

    model_config = {'populate_by_name': True}


class DSPCampaignForecastDescription(BaseModel):
    """The description of which campaign and what features are enabled for a forecast."""
    campaign_id: str = Field(..., alias="campaignId", description="The unique identifier of the campaign.")
    enabled_features: Optional["DSPEnabledFeaturesInCampaignForecast"] = Field(None, alias="enabledFeatures")
    flight_ids: Optional[list[str]] = Field(None, alias="flightIds", description="The unique identifier of the flight.")
    replanning_settings: Optional["DSPReplanningSettings"] = Field(None, alias="replanningSettings")

    model_config = {'populate_by_name': True}


class DSPCampaignForecast(BaseModel):
    available_forecast_flights: Optional[list["DSPForecastFlight"]] = Field(None, alias="availableForecastFlights", description="The combination of existing flight settings and proposed flight settings based on forecasting.")
    campaign_display_name: str = Field(..., alias="campaignDisplayName", description="The display name of the campaign used for the forecast.")
    campaign_forecast_description: "DSPCampaignForecastDescription" = Field(..., alias="campaignForecastDescription")
    creation_date_time: str = Field(..., alias="creationDateTime", description="The creation date of the campaign forecast.")
    flight_forecasts: Optional[list["DSPFlightForecast"]] = Field(None, alias="flightForecasts", description="The forecast results of multiple flights of the campaign.")
    has_existing_guidance: Optional[bool] = Field(None, alias="hasExistingGuidance", description="Indicates whether there are existing recommendations/guidance available for the campaign from the Noble ListGuidance API")

    model_config = {'populate_by_name': True}


class DSPCampaignForecastMultiStatusSuccess(BaseModel):
    campaign_forecast: "DSPCampaignForecast" = Field(..., alias="campaignForecast")
    index: int

    model_config = {'populate_by_name': True}


class DSPCampaignForecastMultiStatusResponse(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    success: Optional[list["DSPCampaignForecastMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class DSPSpendCalculationMode(StrEnum):
    ADVERTISER_ACCOUNT = "ADVERTISER_ACCOUNT"
    CAMPAIGN = "CAMPAIGN"
    MANAGER_ACCOUNT = "MANAGER_ACCOUNT"


class DSPFulfillmentLevel(StrEnum):
    LEVEL_0 = "LEVEL_0"
    LEVEL_5 = "LEVEL_5"


class DSPCommitment(BaseModel):
    advertiser_ids: Optional[list[str]] = Field(None, alias="advertiserIds", description="Advertiser IDs associated with the commitment.")
    campaign_ids: Optional[list[str]] = Field(None, alias="campaignIds", description="Campaign IDs associated with the commitment.")
    commitment_id: str = Field(..., alias="commitmentId", description="A unique identifier for the commitment.")
    commitment_name: str = Field(..., alias="commitmentName", description="The name of the commitment.")
    committed_spend: float = Field(..., alias="committedSpend", description="The total committed spend for the commitment.")
    currency_code: "DSPCurrencyCode" = Field(..., alias="currencyCode")
    deal_ids: Optional[list[str]] = Field(None, alias="dealIds", description="Deal IDs associated with the commitment.")
    end_date_time: str = Field(..., alias="endDateTime", description="The end date and time of the commitment.")
    fulfillment_level: "DSPFulfillmentLevel" = Field(..., alias="fulfillmentLevel")
    spend_calculation_mode: "DSPSpendCalculationMode" = Field(..., alias="spendCalculationMode")
    start_date_time: str = Field(..., alias="startDateTime", description="The start date and time of the commitment.")

    model_config = {'populate_by_name': True}


class DSPCommitmentCreate(BaseModel):
    advertiser_ids: Optional[list[str]] = Field(None, alias="advertiserIds", description="Advertiser IDs associated with the commitment.")
    campaign_ids: Optional[list[str]] = Field(None, alias="campaignIds", description="Campaign IDs associated with the commitment.")
    commitment_name: str = Field(..., alias="commitmentName", description="The name of the commitment.")
    committed_spend: float = Field(..., alias="committedSpend", description="The total committed spend for the commitment.")
    currency_code: "DSPCurrencyCode" = Field(..., alias="currencyCode")
    deal_ids: Optional[list[str]] = Field(None, alias="dealIds", description="Deal IDs associated with the commitment.")
    end_date_time: str = Field(..., alias="endDateTime", description="The end date and time of the commitment.")
    fulfillment_level: "DSPFulfillmentLevel" = Field(..., alias="fulfillmentLevel")
    spend_calculation_mode: "DSPSpendCalculationMode" = Field(..., alias="spendCalculationMode")
    start_date_time: str = Field(..., alias="startDateTime", description="The start date and time of the commitment.")

    model_config = {'populate_by_name': True}


class DSPCommitmentMultiStatusSuccess(BaseModel):
    commitment: "DSPCommitment"
    index: int

    model_config = {'populate_by_name': True}


class DSPCommitmentMultiStatusResponse(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    success: Optional[list["DSPCommitmentMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class DSPSpendDimensionType(StrEnum):
    ADVERTISER = "ADVERTISER"
    CAMPAIGN = "CAMPAIGN"
    COMMITMENT = "COMMITMENT"
    DEAL = "DEAL"


class DSPSpendDimension(BaseModel):
    """| SpendDimension | Description | | --- | --- | | `advertiserAccountId` | Identifier for an advertising account. | | `campaignId` | Identifier for campaign entity | | `dealId` | Identifier for deal ent"""
    pass


class DSPCommitmentSpendIdentifier(BaseModel):
    commitment_id: str = Field(..., alias="commitmentId", description="Commitment ID associated with the commitment.")
    spend_dimension: Optional["DSPSpendDimension"] = Field(None, alias="spendDimension")

    model_config = {'populate_by_name': True}


class DSPCommitmentSpend(BaseModel):
    accrued_spend_value: Optional[float] = Field(None, alias="accruedSpendValue", description="Actual accrual spend amount in commitment currency.")
    accrued_to_date_time: str = Field(..., alias="accruedToDateTime", description="Timestamp for accrual spend.")
    commitment_id: "DSPCommitmentSpendIdentifier" = Field(..., alias="commitmentId")
    currency_code: "DSPCurrencyCode" = Field(..., alias="currencyCode")
    projected_spend_value: Optional[float] = Field(None, alias="projectedSpendValue", description="Projected spend amount in commitment currency.")
    spend_at_risk_value: Optional[float] = Field(None, alias="spendAtRiskValue", description="Spend at risk amount in commitment currency.")
    spend_dimension_type: "DSPSpendDimensionType" = Field(..., alias="spendDimensionType")

    model_config = {'populate_by_name': True}


class DSPCommitmentSpendMultiStatusSuccess(BaseModel):
    commitment_spend: "DSPCommitmentSpend" = Field(..., alias="commitmentSpend")
    index: int

    model_config = {'populate_by_name': True}


class DSPCommitmentSpendMultiStatusResponse(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    success: Optional[list["DSPCommitmentSpendMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class DSPCommitmentSuccessResponse(BaseModel):
    commitments: Optional[list["DSPCommitment"]] = None
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class DSPCommitmentUpdate(BaseModel):
    advertiser_ids: Optional[list[str]] = Field(None, alias="advertiserIds", description="Advertiser IDs associated with the commitment.")
    campaign_ids: Optional[list[str]] = Field(None, alias="campaignIds", description="Campaign IDs associated with the commitment.")
    commitment_id: str = Field(..., alias="commitmentId", description="A unique identifier for the commitment.")
    commitment_name: Optional[str] = Field(None, alias="commitmentName", description="The name of the commitment.")
    committed_spend: Optional[float] = Field(None, alias="committedSpend", description="The total committed spend for the commitment.")
    currency_code: Optional["DSPCurrencyCode"] = Field(None, alias="currencyCode")
    deal_ids: Optional[list[str]] = Field(None, alias="dealIds", description="Deal IDs associated with the commitment.")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The end date and time of the commitment.")
    fulfillment_level: Optional["DSPFulfillmentLevel"] = Field(None, alias="fulfillmentLevel")
    spend_calculation_mode: Optional["DSPSpendCalculationMode"] = Field(None, alias="spendCalculationMode")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The start date and time of the commitment.")

    model_config = {'populate_by_name': True}


class DSPCreateCommitmentRequest(BaseModel):
    commitments: Optional[list["DSPCommitmentCreate"]] = None

    model_config = {'populate_by_name': True}


class DSPRetrieveCampaignForecastRequest(BaseModel):
    campaign_forecast_descriptions: Optional[list["DSPCampaignForecastDescription"]] = Field(None, alias="campaignForecastDescriptions")

    model_config = {'populate_by_name': True}


class DSPRetrieveCommitmentRequest(BaseModel):
    commitment_ids: Optional[list[str]] = Field(None, alias="commitmentIds")

    model_config = {'populate_by_name': True}


class DSPRetrieveCommitmentSpendRequest(BaseModel):
    commitment_ids: Optional[list["DSPCommitmentSpendIdentifier"]] = Field(None, alias="commitmentIds")

    model_config = {'populate_by_name': True}


class DSPUpdateCommitmentRequest(BaseModel):
    commitments: Optional[list["DSPCommitmentUpdate"]] = None

    model_config = {'populate_by_name': True}


class DVBrandSafetyContentCategoriesWithRiskMap(BaseModel):
    """A map from content categories to risk level to exclude from targeting. Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISAS"""
    key: str = Field(..., description="Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATUR")
    value: "BrandSuitabilityRiskLevelType"

    model_config = {'populate_by_name': True}


class TimeOfDay(BaseModel):
    end_time: str = Field(..., alias="endTime", description="Selected end time")
    start_time: str = Field(..., alias="startTime", description="Selected start time")

    model_config = {'populate_by_name': True}


class DayPartTarget(BaseModel):
    """Target based on time of day."""
    day_of_week: "DayOfWeek" = Field(..., alias="dayOfWeek")
    time_of_day: "TimeOfDay" = Field(..., alias="timeOfDay")

    model_config = {'populate_by_name': True}


class DeleteAdAssociationRequest(BaseModel):
    ad_association_ids: Optional[list[str]] = Field(None, alias="adAssociationIds")

    model_config = {'populate_by_name': True}


class DeleteAdGroupRequest(BaseModel):
    ad_group_ids: Optional[list[str]] = Field(None, alias="adGroupIds")

    model_config = {'populate_by_name': True}


class DeleteAdRequest(BaseModel):
    ad_ids: Optional[list[str]] = Field(None, alias="adIds")

    model_config = {'populate_by_name': True}


class DeleteCampaignRequest(BaseModel):
    campaign_ids: Optional[list[str]] = Field(None, alias="campaignIds")

    model_config = {'populate_by_name': True}


class DeleteTargetRequest(BaseModel):
    target_ids: Optional[list[str]] = Field(None, alias="targetIds")

    model_config = {'populate_by_name': True}


class DeviceTarget(BaseModel):
    """Target based on user device."""
    device_orientation: Optional["DeviceOrientation"] = Field(None, alias="deviceOrientation")
    device_type: "DeviceType" = Field(..., alias="deviceType")
    mobile_device: Optional["MobileDevice"] = Field(None, alias="mobileDevice")
    mobile_environment: Optional["MobileEnvironment"] = Field(None, alias="mobileEnvironment")
    mobile_os: Optional["MobileOs"] = Field(None, alias="mobileOs")

    model_config = {'populate_by_name': True}


class DirectIndexValue(BaseModel):
    """Values for a location index where the indexValue is the pre-calculated index."""
    index_value: float = Field(..., alias="indexValue", description="The pre-calculated index value.")
    postal_code: str = Field(..., alias="postalCode", description="The postal code for the location index prefixed by country code (i.e. US-10118).")

    model_config = {'populate_by_name': True}


class DirectIndexValues(BaseModel):
    values: list["DirectIndexValue"] = Field(..., description="List of direct index values.")

    model_config = {'populate_by_name': True}


class DomainFileTarget(BaseModel):
    """Targets domains based on list provided via file upload."""
    domain_file_id: Optional[str] = Field(None, alias="domainFileId", description="The ID associated to the domain file to target. Read-only and created based on the inputted domainFileKey.")
    domain_file_key: str = Field(..., alias="domainFileKey", description="The S3 key of the uploaded file which can be obtained from the file upload policy endpoint. A max of 10 files may be ass")
    domain_file_name: str = Field(..., alias="domainFileName", description="The name of the file.")
    domain_file_url: Optional[str] = Field(None, alias="domainFileUrl", description="The file containing the domains uploaded. It expires in one hour.")

    model_config = {'populate_by_name': True}


class DomainListTarget(BaseModel):
    """Targets domains based on an existing domain list."""
    domain_list_id: str = Field(..., alias="domainListId", description="The ID of the domain list to target.")

    model_config = {'populate_by_name': True}


class DomainNameTarget(BaseModel):
    """Targets domains based on URL."""
    domain_name: str = Field(..., alias="domainName", description="The URL of the domain to target.")

    model_config = {'populate_by_name': True}


class DomainTargetDetails(BaseModel):
    pass


class DomainTarget(BaseModel):
    """Target based on a specified domain."""
    domain_target_details: "DomainTargetDetails" = Field(..., alias="domainTargetDetails")
    domain_target_type: "DomainTargetTypes" = Field(..., alias="domainTargetType")

    model_config = {'populate_by_name': True}


class DoubleVerifyAuthenticAttention(BaseModel):
    universal_attention: bool = Field(..., alias="universalAttention", description="One omni-channel segment that is informed by data from all DV campaigns to help avoid serving ads on generally poor perf")

    model_config = {'populate_by_name': True}


class DoubleVerifyAuthenticBrandSafety(BaseModel):
    double_verify_segment_id: Optional[str] = Field(None, alias="doubleVerifySegmentId")

    model_config = {'populate_by_name': True}


class DoubleVerifyBrandSafety(BaseModel):
    app_age_rating: Optional[list["DVBrandSafetyAppAgeRatingType"]] = Field(None, alias="appAgeRating", description="A list of app age ratings to be used for excluding apps. For example, TEENS_12_PLUS will only exclude apps with content ")
    app_star_rating: Optional["DVBrandSafetyAppStarRatingType"] = Field(None, alias="appStarRating")
    content_categories: Optional[list["DVBrandSafetyContentCategoryType"]] = Field(None, alias="contentCategories", description="A list of content categories to exclude from targeting.")
    content_categories_with_risk: Optional[list["DVBrandSafetyContentCategoriesWithRiskMap"]] = Field(None, alias="contentCategoriesWithRisk")
    exclude_apps_with_insufficient_rating: Optional[bool] = Field(None, alias="excludeAppsWithInsufficientRating", description="Set to true to exclude unofficial apps or apps with insufficient user ratings (<100 lifetime).")
    unknown_content: Optional[bool] = Field(None, alias="unknownContent", description="Set to true to exclude unknown content.")

    model_config = {'populate_by_name': True}


class DoubleVerifyCustomContextualSegmentId(BaseModel):
    double_verify_segment_id: Optional[str] = Field(None, alias="doubleVerifySegmentId")

    model_config = {'populate_by_name': True}


class DoubleVerifyFraudInvalidTraffic(BaseModel):
    block_app_and_sites: Optional[bool] = Field(None, alias="blockAppAndSites", description="Set to true to block applications and sites with insufficient historical fraud and invalid traffic statistics. This will")
    exclude_apps_and_sites: Optional["ExcludeAppsAndSitesType"] = Field(None, alias="excludeAppsAndSites")
    exclude_impressions: Optional[bool] = Field(None, alias="excludeImpressions", description="Set to true to exclude impressions delivered to devices identified to be fraudulent or invalid.")

    model_config = {'populate_by_name': True}


class DoubleVerifyStandardDisplayBrandSafety(BaseModel):
    content_categories: Optional[list["DVBrandSafetyContentCategoryType"]] = Field(None, alias="contentCategories", description="A list of content categories to exclude from targeting.")
    content_categories_with_risk: Optional[list["DVBrandSafetyContentCategoriesWithRiskMap"]] = Field(None, alias="contentCategoriesWithRisk")
    unknown_content: Optional[bool] = Field(None, alias="unknownContent", description="Set to true to exclude unknown content.")

    model_config = {'populate_by_name': True}


class DoubleVerifyViewability(BaseModel):
    average_completion_and_fully_viewable_rate_targeting: Optional["AverageCompletionAndFullyViewableRateTargetingType"] = Field(None, alias="averageCompletionAndFullyViewableRateTargeting")
    brand_exposure_viewability_targeting: Optional["BrandExposureViewabilityTargetingType"] = Field(None, alias="brandExposureViewabilityTargeting")
    include_unmeasurable_impressions: Optional[bool] = Field(None, alias="includeUnmeasurableImpressions", description="Set to true to include impressions where impressions can't be measured.")
    mrc_viewability_targeting: Optional["MrcViewabilityTargetingType"] = Field(None, alias="mrcViewabilityTargeting")

    model_config = {'populate_by_name': True}


class FoldPositionTarget(BaseModel):
    """Targets ads in the specified fold position"""
    fold_position: "FoldPosition" = Field(..., alias="foldPosition")

    model_config = {'populate_by_name': True}


class ForbiddenResponseContent(BaseModel):
    code: "ErrorCode"
    message: str

    model_config = {'populate_by_name': True}


class GatewayTimeoutResponseContent(BaseModel):
    code: str
    message: str

    model_config = {'populate_by_name': True}


class GeoLocationCoordinates(BaseModel):
    """Coordinates for a point of interest"""
    latitude: float = Field(..., description="Latitude coordinate. Example 47.6157")
    longitude: float = Field(..., description="Longitude coordinate. Example 122.339")

    model_config = {'populate_by_name': True}


class RadiusLocation(BaseModel):
    """Configuration for a radius-based location. A minimum radius of 0.37 miles (2000 ft, 0.6km) is required."""
    coordinates: Optional["GeoLocationCoordinates"] = None
    point_of_interest_address: Optional[str] = Field(None, alias="pointOfInterestAddress", description="Address. Example '2111 7th Ave, Seattle, WA 98121, United States' or 'Amazon Spheres'")
    point_of_interest_radius: float = Field(..., alias="pointOfInterestRadius", description="Radius of circle in kilometers or miles")
    units: "DistanceUnit"

    model_config = {'populate_by_name': True}


class SmartLocation(BaseModel):
    """A smart location targets postal codes based on a sales index."""
    location_index_id: str = Field(..., alias="locationIndexId", description="The ID of the index used for this smart location.")
    max_index_value_percentile: Optional[int] = Field(None, alias="maxIndexValuePercentile", description="Maximum percentile value (0-100). Must be greater than minIndexValuePercentile. Null will be treated as 0.")
    min_index_value_percentile: Optional[int] = Field(None, alias="minIndexValuePercentile", description="Minimum percentile value (0-100). Must be less than maxIndexValuePercentile. Null will be treated as 0.")
    name: str = Field(..., description="Name for the smart location.")

    model_config = {'populate_by_name': True}


class GeoLocationUnion(BaseModel):
    pass


class GeoLocation(BaseModel):
    geo_location_id: str = Field(..., alias="geoLocationId", description="The identifier of the geo location.")
    location: "GeoLocationUnion"

    model_config = {'populate_by_name': True}


class GeoLocationMultiStatusSuccess(BaseModel):
    geo_location: "GeoLocation" = Field(..., alias="geoLocation")
    index: int

    model_config = {'populate_by_name': True}


class GeoLocationMultiStatusResponse(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    success: Optional[list["GeoLocationMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class IndexStatus(StrEnum):
    ENABLED = "ENABLED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    UPDATE_FAILED = "UPDATE_FAILED"


class IndexValues(BaseModel):
    pass


class IntegralAdScienceBrandSafety(BaseModel):
    exclude_content: Optional[bool] = Field(None, alias="excludeContent", description="Set to true to exclude content that Integral Ad Science is not able to rate.")
    ias_brand_safety_adult: Optional["IASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyAdult")
    ias_brand_safety_alcohol: Optional["IASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyAlcohol")
    ias_brand_safety_gambling: Optional["IASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyGambling")
    ias_brand_safety_hate_speech: Optional["IASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyHateSpeech")
    ias_brand_safety_illegal_downloads: Optional["IASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyIllegalDownloads")
    ias_brand_safety_illegal_drugs: Optional["IASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyIllegalDrugs")
    ias_brand_safety_offensive_language: Optional["IASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyOffensiveLanguage")
    ias_brand_safety_violence: Optional["IASBrandSafetyLevelType"] = Field(None, alias="iasBrandSafetyViolence")

    model_config = {'populate_by_name': True}


class IntegralAdScienceContextualAvoidance(BaseModel):
    avoidance_segments: Optional[list[str]] = Field(None, alias="avoidanceSegments", description="The unique identifier of the IAS contextual avoidance segment")

    model_config = {'populate_by_name': True}


class IntegralAdScienceContextualTargeting(BaseModel):
    topical_segments: Optional[list[str]] = Field(None, alias="topicalSegments", description="The unique identifier of the IAS contextual topical targeting segment")
    vertical_segments: Optional[list[str]] = Field(None, alias="verticalSegments", description="The unique identifier of the IAS contextual vertical targeting segment")

    model_config = {'populate_by_name': True}


class IntegralAdScienceFraudInvalidTraffic(BaseModel):
    target_setting: Optional["IASFraudInvalidTrafficType"] = Field(None, alias="targetSetting")

    model_config = {'populate_by_name': True}


class IntegralAdScienceQualitySync(BaseModel):
    segment_id: Optional[str] = Field(None, alias="segmentId")

    model_config = {'populate_by_name': True}


class IntegralAdScienceViewability(BaseModel):
    """The IAS viewability standard."""
    standard: "IASViewabilityStandardType"
    viewability_targeting: Optional["ViewabilityTierType"] = Field(None, alias="viewabilityTargeting")

    model_config = {'populate_by_name': True}


class InternalServerErrorResponseContent(BaseModel):
    code: str
    message: str

    model_config = {'populate_by_name': True}


class InventorySourceTarget(BaseModel):
    """Target based on the source of the inventory."""
    inventory_source_id: "MarketplaceStringValue" = Field(..., alias="inventorySourceId")
    inventory_source_type: "InventorySourceType" = Field(..., alias="inventorySourceType")

    model_config = {'populate_by_name': True}


class KeywordTarget(BaseModel):
    """Targets a specific customer search term."""
    keyword: str = Field(..., description="The customer search term or text to target")
    match_type: "KeywordMatchType" = Field(..., alias="matchType")
    native_language_keyword: Optional[str] = Field(None, alias="nativeLanguageKeyword", description="The unlocalized keyword text in the preferred locale of the advertiser.")
    native_language_locale: Optional["LanguageLocale"] = Field(None, alias="nativeLanguageLocale")

    model_config = {'populate_by_name': True}


class LocationIndex(BaseModel):
    creation_date_time: str = Field(..., alias="creationDateTime", description="The date time the location index was created.")
    index_data: "IndexValues" = Field(..., alias="indexData")
    index_id: str = Field(..., alias="indexId", description="The identifier of the location index.")
    index_name: str = Field(..., alias="indexName", description="The name of the location index.")
    last_updated_date_time: str = Field(..., alias="lastUpdatedDateTime", description="The date time the location index was last updated successfully.")
    status: "IndexStatus"

    model_config = {'populate_by_name': True}


class LocationIndexMultiStatusSuccess(BaseModel):
    index: int
    location_index: "LocationIndex" = Field(..., alias="locationIndex")

    model_config = {'populate_by_name': True}


class LocationIndexMultiStatusResponse(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    success: Optional[list["LocationIndexMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class LocationIndexSuccessResponse(BaseModel):
    location_indexes: Optional[list["LocationIndex"]] = Field(None, alias="locationIndexes")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class UpdateDirectIndexValues(BaseModel):
    values: Optional[list["CreateDirectIndexValue"]] = Field(None, description="List of direct index values.")

    model_config = {'populate_by_name': True}


class UpdateConstituentIndexValues(BaseModel):
    values: Optional[list["CreateConstituentIndexValue"]] = Field(None, description="List of brand and category sales values.")

    model_config = {'populate_by_name': True}


class UpdateIndexValues(BaseModel):
    pass


class LocationIndexUpdate(BaseModel):
    index_data: Optional["UpdateIndexValues"] = Field(None, alias="indexData")
    index_id: str = Field(..., alias="indexId", description="The identifier of the location index.")

    model_config = {'populate_by_name': True}


class LocationTarget(BaseModel):
    """Target based on geographic location."""
    location_id: str = Field(..., alias="locationId", description="The ID of the geographic location to target.")
    location_id_resolved: Optional[str] = Field(None, alias="locationIdResolved", description="A human-readable location text. It's a read-only field.")

    model_config = {'populate_by_name': True}


class ThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""
    match_type: "ThemeMatchType" = Field(..., alias="matchType")

    model_config = {'populate_by_name': True}


class OverridableTargets(BaseModel):
    pass


class MarketplaceTargetFieldOverrides(BaseModel):
    state: Optional["State"] = None
    tags: Optional[list["Tag"]] = Field(None, description="Open ended labels with a key value pair applied to the target")
    target_details: Optional["OverridableTargets"] = Field(None, alias="targetDetails")

    model_config = {'populate_by_name': True}


class MarketplaceTargetConfigurations(BaseModel):
    marketplace: "Marketplace"
    overrides: "MarketplaceTargetFieldOverrides"
    target_id: str = Field(..., alias="targetId", description="Represents marketplace target id (Ex: targetId-US) associated to global target (Ex: targetId-Global)")

    model_config = {'populate_by_name': True}


class MatchType(StrEnum):
    BROAD = "BROAD"
    EXACT = "EXACT"
    INTERESTED_AUDIENCE = "INTERESTED_AUDIENCE"
    KEYWORDS_CLOSE_MATCH = "KEYWORDS_CLOSE_MATCH"
    KEYWORDS_LOOSE_MATCH = "KEYWORDS_LOOSE_MATCH"
    KEYWORDS_RELATED_TO_GIFTS = "KEYWORDS_RELATED_TO_GIFTS"
    KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY = "KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY"
    KEYWORDS_RELATED_TO_PRIME_DAY = "KEYWORDS_RELATED_TO_PRIME_DAY"
    KEYWORDS_RELATED_TO_YOUR_BRAND = "KEYWORDS_RELATED_TO_YOUR_BRAND"
    KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES = "KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES"
    KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY = "KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY"
    PHRASE = "PHRASE"
    PRODUCTS_SIMILAR_TO_ADVERTISED_PRODUCTS = "PRODUCTS_SIMILAR_TO_ADVERTISED_PRODUCTS"
    PRODUCT_COMPLEMENTS = "PRODUCT_COMPLEMENTS"
    PRODUCT_EXACT = "PRODUCT_EXACT"
    PRODUCT_REMARKETING = "PRODUCT_REMARKETING"
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"
    PRODUCT_SUBSTITUTES = "PRODUCT_SUBSTITUTES"


class NativeContentPositionTarget(BaseModel):
    """Targets ads to a specific native content position"""
    native_position: "NativeContentPosition" = Field(..., alias="nativePosition")

    model_config = {'populate_by_name': True}


class NewsGuardBrandGuardMisinformationSafety(BaseModel):
    avoidance_list: Optional[list["NewsGuardBrandGuardMisinformationSafetyType"]] = Field(None, alias="avoidanceList", description="The unique identifiers of misinformation targets")

    model_config = {'populate_by_name': True}


class NewsGuardBrandGuardTrustedNewsTargeting(BaseModel):
    """Only applicable for Web supply."""
    targeting_list: Optional[list["NewsGuardBrandGuardTrustedNewsTargetingType"]] = Field(None, alias="targetingList", description="The unique identifiers of trusted news targets")

    model_config = {'populate_by_name': True}


class NotFoundResponseContent(BaseModel):
    code: "ErrorCode"
    message: str

    model_config = {'populate_by_name': True}


class PixalateFraudInvalidTraffic(BaseModel):
    exclude_apps_and_domains: Optional[bool] = Field(None, alias="excludeAppsAndDomains", description="Set to true to exclude traffic from Apps and Domains identified to be fraudulent or invalid.")
    exclude_ip_address_and_user_agents: Optional[bool] = Field(None, alias="excludeIpAddressAndUserAgents", description="Set to true to exclude traffic from IPV4 and IPV6 addresses and user agents identified to be fraudulent or invalid.")
    exclude_ott_and_mobile_devices: Optional[bool] = Field(None, alias="excludeOttAndMobileDevices", description="Set to true to exclude traffic from OTT and Mobile devices identified to be fraudulent or invalid.")
    exclude_removed_apps_from_app_stores: Optional[bool] = Field(None, alias="excludeRemovedAppsFromAppStores", description="Set to true to exlude traffic from Apps that have been removed from the google play and apple app stores in the last 6 m")

    model_config = {'populate_by_name': True}


class PlacementTypeTarget(BaseModel):
    """Target based on the placement type."""
    placement_type: "PlacementType" = Field(..., alias="placementType")

    model_config = {'populate_by_name': True}


class ProductAudienceTarget(BaseModel):
    """Target customers who have viewed or purchased a certain product within a specified lookback window."""
    asin: "MarketplaceStringValue"
    event: "TargetEvent"
    lookback: "Lookback"
    match_type: "ProductAudienceMatchType" = Field(..., alias="matchType")

    model_config = {'populate_by_name': True}


class ProductCategoryRefinement(BaseModel):
    product_age_range_id: Optional[str] = Field(None, alias="productAgeRangeId", description="The age range ID to target.")
    product_age_range_id_resolved: Optional[str] = Field(None, alias="productAgeRangeIdResolved", description="The resolved age range to target.")
    product_brand_id: Optional[str] = Field(None, alias="productBrandId", description="The brand ID to target.")
    product_brand_id_resolved: Optional[str] = Field(None, alias="productBrandIdResolved", description="The resolved name of the brand.")
    product_category_id: Optional[str] = Field(None, alias="productCategoryId", description="The product category ID to target.")
    product_category_id_resolved: Optional[str] = Field(None, alias="productCategoryIdResolved", description="The resolved product category.")
    product_genre_id: Optional[str] = Field(None, alias="productGenreId", description="The product genre ID to target.")
    product_genre_id_resolved: Optional[str] = Field(None, alias="productGenreIdResolved", description="The resolved product genre to target.")
    product_price_greater_than: Optional[float] = Field(None, alias="productPriceGreaterThan", description="Refinement to target products with a price greater than the value within the product category.")
    product_price_less_than: Optional[float] = Field(None, alias="productPriceLessThan", description="Refinement to target products with a price less than the value within the product category.")
    product_prime_shipping_eligible: Optional[bool] = Field(None, alias="productPrimeShippingEligible", description="Target based on if a product is Prime-shipping eligible.")
    product_rating_greater_than: Optional[float] = Field(None, alias="productRatingGreaterThan", description="Refinement to target products with a rating greater than the value within the product category.")
    product_rating_less_than: Optional[float] = Field(None, alias="productRatingLessThan", description="Refinement to target products with a rating less than the value within the product category.")

    model_config = {'populate_by_name': True}


class ProductCategoryRefinementMarketplaceSetting(BaseModel):
    marketplace: "Marketplace"
    product_category_refinement: "ProductCategoryRefinement" = Field(..., alias="productCategoryRefinement")

    model_config = {'populate_by_name': True}


class ProductCategoryRefinementValue(BaseModel):
    marketplace_settings: Optional[list["ProductCategoryRefinementMarketplaceSetting"]] = Field(None, alias="marketplaceSettings", description="Marketplace specific product category refinements. Either the value or the marketplaceSettings should always be specifie")
    product_category_refinement: Optional["ProductCategoryRefinement"] = Field(None, alias="productCategoryRefinement")

    model_config = {'populate_by_name': True}


class ProductGenreRefinement(BaseModel):
    product_genre_id: str = Field(..., alias="productGenreId", description="The product genre ID to target.")
    product_genre_id_resolved: Optional[str] = Field(None, alias="productGenreIdResolved", description="The resolved product genre to target.")

    model_config = {'populate_by_name': True}


class ProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""
    match_type: Optional["ProductCategoryMatchType"] = Field(None, alias="matchType")
    product_category_refinement: "ProductCategoryRefinementValue" = Field(..., alias="productCategoryRefinement")
    product_genre_refinement: Optional["ProductGenreRefinement"] = Field(None, alias="productGenreRefinement")

    model_config = {'populate_by_name': True}


class ProductMarketplaceSetting(BaseModel):
    marketplace: "Marketplace"
    product_id: str = Field(..., alias="productId", description="The product id applicable at the specified marketplace.")

    model_config = {'populate_by_name': True}


class ProductValue(BaseModel):
    marketplace_settings: Optional[list["ProductMarketplaceSetting"]] = Field(None, alias="marketplaceSettings", description="The product ids at specific marketplace level. Either the product id or the marketplace settings should always be specif")
    product_id: Optional[str] = Field(None, alias="productId", description="The product identifier. Either the product id or the marketplace settings should always be specified")

    model_config = {'populate_by_name': True}


class ProductTarget(BaseModel):
    """Targets a specific product."""
    match_type: "ProductMatchType" = Field(..., alias="matchType")
    product: "ProductValue"
    product_id_type: "ProductIdType" = Field(..., alias="productIdType")

    model_config = {'populate_by_name': True}


class QueryAdAssociationRequest(BaseModel):
    ad_association_id_filter: Optional["AdAssociationAdAssociationIdFilter"] = Field(None, alias="adAssociationIdFilter")
    ad_group_id_filter: Optional["AdAssociationAdGroupIdFilter"] = Field(None, alias="adGroupIdFilter")
    ad_id_filter: Optional["AdAssociationAdIdFilter"] = Field(None, alias="adIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class QueryAdExtensionRequest(BaseModel):
    ad_extension_id_filter: Optional["AdExtensionAdExtensionIdFilter"] = Field(None, alias="adExtensionIdFilter")
    ad_extension_status_filter: Optional["AdExtensionAdExtensionStatusFilter"] = Field(None, alias="adExtensionStatusFilter")
    ad_extension_type_filter: Optional["AdExtensionAdExtensionTypeFilter"] = Field(None, alias="adExtensionTypeFilter")
    ad_group_id_filter: Optional["AdExtensionAdGroupIdFilter"] = Field(None, alias="adGroupIdFilter")
    ad_id_filter: Optional["AdExtensionAdIdFilter"] = Field(None, alias="adIdFilter")
    ad_product_filter: Optional["AdExtensionAdProductFilter"] = Field(None, alias="adProductFilter")
    max_results: Optional[int] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken")
    state_filter: Optional["AdExtensionStateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class QueryAdGroupRequest(BaseModel):
    ad_group_id_filter: Optional["AdGroupAdGroupIdFilter"] = Field(None, alias="adGroupIdFilter")
    ad_product_filter: "AdGroupAdProductFilter" = Field(..., alias="adProductFilter")
    campaign_id_filter: Optional["AdGroupCampaignIdFilter"] = Field(None, alias="campaignIdFilter")
    marketplace_scope_filter: Optional["AdGroupMarketplaceScopeFilter"] = Field(None, alias="marketplaceScopeFilter")
    max_results: Optional[int] = Field(None, alias="maxResults")
    name_filter: Optional["AdGroupNameFilter"] = Field(None, alias="nameFilter")
    next_token: Optional[str] = Field(None, alias="nextToken")
    state_filter: Optional["AdGroupStateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class QueryAdRequest(BaseModel):
    ad_group_id_filter: Optional["AdAdGroupIdFilter"] = Field(None, alias="adGroupIdFilter")
    ad_id_filter: Optional["AdAdIdFilter"] = Field(None, alias="adIdFilter")
    ad_product_filter: "AdAdProductFilter" = Field(..., alias="adProductFilter")
    campaign_id_filter: Optional["AdCampaignIdFilter"] = Field(None, alias="campaignIdFilter")
    marketplace_scope_filter: Optional["AdMarketplaceScopeFilter"] = Field(None, alias="marketplaceScopeFilter")
    max_results: Optional[int] = Field(None, alias="maxResults")
    name_filter: Optional["AdNameFilter"] = Field(None, alias="nameFilter")
    next_token: Optional[str] = Field(None, alias="nextToken")
    state_filter: Optional["AdStateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class QueryBrandStoreEditionPublishVersionRequest(BaseModel):
    edition_id_filter: "BrandStoreEditionPublishVersionBrandStoreEditionIdFilter" = Field(..., alias="editionIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken")
    publish_status_filter: "BrandStoreEditionPublishVersionStorePublishStatusFilter" = Field(..., alias="publishStatusFilter")
    store_id_filter: "BrandStoreEditionPublishVersionBrandStoreIdFilter" = Field(..., alias="storeIdFilter")

    model_config = {'populate_by_name': True}


class QueryBrandStorePageRequest(BaseModel):
    edition_id_filter: "BrandStorePageBrandStoreEditionIdFilter" = Field(..., alias="editionIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken")
    page_id_filter: "BrandStorePagePageIdFilter" = Field(..., alias="pageIdFilter")
    store_edition_publish_id_filter: Optional["BrandStorePageBrandStoreEditionPublishVersionIdFilter"] = Field(None, alias="storeEditionPublishIdFilter")
    store_id_filter: "BrandStorePageBrandStoreIdFilter" = Field(..., alias="storeIdFilter")

    model_config = {'populate_by_name': True}


class QueryBrandStoreRequest(BaseModel):
    max_results: Optional[int] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken")
    store_name_filter: "BrandStoreStoreNameFilter" = Field(..., alias="storeNameFilter")

    model_config = {'populate_by_name': True}


class QueryCampaignRequest(BaseModel):
    ad_product_filter: "CampaignAdProductFilter" = Field(..., alias="adProductFilter")
    campaign_id_filter: Optional["CampaignCampaignIdFilter"] = Field(None, alias="campaignIdFilter")
    goal_filter: Optional["CampaignGoalFilter"] = Field(None, alias="goalFilter")
    marketplace_scope_filter: Optional["CampaignMarketplaceScopeFilter"] = Field(None, alias="marketplaceScopeFilter")
    max_results: Optional[int] = Field(None, alias="maxResults")
    name_filter: Optional["CampaignNameFilter"] = Field(None, alias="nameFilter")
    next_token: Optional[str] = Field(None, alias="nextToken")
    portfolio_id_filter: Optional["CampaignPortfolioIdFilter"] = Field(None, alias="portfolioIdFilter")
    state_filter: Optional["CampaignStateFilter"] = Field(None, alias="stateFilter")

    model_config = {'populate_by_name': True}


class TargetLanguageLocaleFilter(BaseModel):
    include: list["LanguageLocale"] = Field(..., description="| NativeLanguageLocale | Description | | --- | --- | | `ak_GH` | Akan (Ghana). | | `am_ET` | Amharic (Ethiopia). | | `an")

    model_config = {'populate_by_name': True}


class TargetStateFilter(BaseModel):
    include: list["State"] = Field(..., description="| State | Description | | --- | --- | | `ENABLED` | The object is set active by user and eligible for delivery. | | `PAU")

    model_config = {'populate_by_name': True}


class TargetProductIdFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class TargetProductIdFilter(BaseModel):
    include: list[str]
    query_term_match_type: "TargetProductIdFilterType" = Field(..., alias="queryTermMatchType")

    model_config = {'populate_by_name': True}


class TargetTargetIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class TargetAdProductFilter(BaseModel):
    include: list["AdProduct"] = Field(..., description="| AdProduct | Description | | --- | --- | | `SPONSORED_PRODUCTS` | Sponsored Products ad product. | | `SPONSORED_BRANDS`")

    model_config = {'populate_by_name': True}


class TargetAdGroupIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class TargetMarketplaceScopeFilter(BaseModel):
    include: list["MarketplaceScope"] = Field(..., description="| MarketplaceScope | Description | | --- | --- | | `GLOBAL` |  | | `SINGLE_MARKETPLACE` |  |")

    model_config = {'populate_by_name': True}


class TargetTargetTypeFilter(BaseModel):
    include: list["TargetType"] = Field(..., description="| TargetType | Description | | --- | --- | | `KEYWORD` | Target based on customer search terms. | | `PRODUCT` | Target b")

    model_config = {'populate_by_name': True}


class TargetKeywordFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class TargetKeywordFilter(BaseModel):
    include: list[str]
    query_term_match_type: "TargetKeywordFilterType" = Field(..., alias="queryTermMatchType")

    model_config = {'populate_by_name': True}


class TargetInventorySourceTypeFilter(BaseModel):
    include: list["InventorySourceType"] = Field(..., description="| InventorySourceType | Description | | --- | --- | | `AMAZON` | Amazon-owned inventory. | | `APD` | Amazon Publisher Di")

    model_config = {'populate_by_name': True}


class TargetNegativeFilter(BaseModel):
    include: list[bool]

    model_config = {'populate_by_name': True}


class TargetCampaignIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class TargetMatchTypeFilter(BaseModel):
    include: list["MatchType"] = Field(..., description="| MatchType | Description | | --- | --- | | `KEYWORDS_RELATED_TO_GIFTS` | Search terms related to gifts. | | `KEYWORDS_R")

    model_config = {'populate_by_name': True}


class TargetMarketplaceStringValueFilter(BaseModel):
    include: list["MarketplaceStringValue"]

    model_config = {'populate_by_name': True}


class QueryTargetRequest(BaseModel):
    ad_group_id_filter: Optional["TargetAdGroupIdFilter"] = Field(None, alias="adGroupIdFilter")
    ad_product_filter: "TargetAdProductFilter" = Field(..., alias="adProductFilter")
    campaign_id_filter: Optional["TargetCampaignIdFilter"] = Field(None, alias="campaignIdFilter")
    inventory_source_id_filter: Optional["TargetMarketplaceStringValueFilter"] = Field(None, alias="inventorySourceIdFilter")
    inventory_source_type_filter: Optional["TargetInventorySourceTypeFilter"] = Field(None, alias="inventorySourceTypeFilter")
    keyword_filter: Optional["TargetKeywordFilter"] = Field(None, alias="keywordFilter")
    marketplace_scope_filter: Optional["TargetMarketplaceScopeFilter"] = Field(None, alias="marketplaceScopeFilter")
    match_type_filter: Optional["TargetMatchTypeFilter"] = Field(None, alias="matchTypeFilter")
    max_results: Optional[int] = Field(None, alias="maxResults")
    native_language_locale_filter: Optional["TargetLanguageLocaleFilter"] = Field(None, alias="nativeLanguageLocaleFilter")
    negative_filter: Optional["TargetNegativeFilter"] = Field(None, alias="negativeFilter")
    next_token: Optional[str] = Field(None, alias="nextToken")
    product_id_filter: Optional["TargetProductIdFilter"] = Field(None, alias="productIdFilter")
    state_filter: Optional["TargetStateFilter"] = Field(None, alias="stateFilter")
    target_id_filter: Optional["TargetTargetIdFilter"] = Field(None, alias="targetIdFilter")
    target_type_filter: Optional["TargetTargetTypeFilter"] = Field(None, alias="targetTypeFilter")

    model_config = {'populate_by_name': True}


class RetrieveLocationIndexRequest(BaseModel):
    index_ids: Optional[list[str]] = Field(None, alias="indexIds")

    model_config = {'populate_by_name': True}


class SBCurrencyCode(StrEnum):
    AED = "AED"
    AUD = "AUD"
    BRL = "BRL"
    CAD = "CAD"
    CHF = "CHF"
    CNY = "CNY"
    DKK = "DKK"
    EGP = "EGP"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"
    JPY = "JPY"
    MXN = "MXN"
    MXP = "MXP"
    NGN = "NGN"
    NOK = "NOK"
    NZD = "NZD"
    PLN = "PLN"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    TRY = "TRY"
    USD = "USD"
    ZAR = "ZAR"


class SBAdvertisingDealPriceType(StrEnum):
    FIXED_PRICE = "FIXED_PRICE"


class SBAdvertisingDealPrice(BaseModel):
    currency_code: "SBCurrencyCode" = Field(..., alias="currencyCode")
    price_type: "SBAdvertisingDealPriceType" = Field(..., alias="priceType")
    value: float = Field(..., description="The monetary amount of the price in the given currency.")

    model_config = {'populate_by_name': True}


class SBAdvertisingDealStatusEnum(StrEnum):
    DRAFT = "DRAFT"
    MODERATION_APPROVED = "MODERATION_APPROVED"
    PROPOSED = "PROPOSED"


class SBAdvertisingDealStatus(BaseModel):
    status: "SBAdvertisingDealStatusEnum"

    model_config = {'populate_by_name': True}


class SBAdvertisingDealState(StrEnum):
    DRAFT = "DRAFT"
    PROPOSED = "PROPOSED"


class SBAdvertisingDeal(BaseModel):
    advertising_deal_id: str = Field(..., alias="advertisingDealId", description="A unique identifier for a deal.")
    end_date_time: str = Field(..., alias="endDateTime", description="The end date time for the deal.")
    name: str = Field(..., description="The name of the deal.")
    price: Optional["SBAdvertisingDealPrice"] = None
    replacing_deal_id: Optional[str] = Field(None, alias="replacingDealId", description="The ID of an advertising deal that this deal intends to replace.")
    start_date_time: str = Field(..., alias="startDateTime", description="The start date time for the deal.")
    state: Optional["SBAdvertisingDealState"] = None
    status: "SBAdvertisingDealStatus"

    model_config = {'populate_by_name': True}


class SBAdvertisingDealAdvertisingDealIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class SBAdvertisingDealBrandedKeywordTargetDetails(BaseModel):
    """The detail of a BRANDED_KEYWORD target."""
    branded_keyword: str = Field(..., alias="brandedKeyword", description="The branded keyword that is an exact match to the shoppers' search term.")

    model_config = {'populate_by_name': True}


class SBCreateAdvertisingDealPrice(BaseModel):
    price_type: "SBAdvertisingDealPriceType" = Field(..., alias="priceType")
    value: float = Field(..., description="The monetary amount of the price in the given currency.")

    model_config = {'populate_by_name': True}


class SBAdvertisingDealCreate(BaseModel):
    end_date_time: str = Field(..., alias="endDateTime", description="The end date time for the deal.")
    name: str = Field(..., description="The name of the deal.")
    price: Optional["SBCreateAdvertisingDealPrice"] = None
    replacing_deal_id: Optional[str] = Field(None, alias="replacingDealId", description="The ID of an advertising deal that this deal intends to replace.")
    start_date_time: str = Field(..., alias="startDateTime", description="The start date time for the deal.")
    state: Optional["SBAdvertisingDealState"] = None

    model_config = {'populate_by_name': True}


class SBAdvertisingDealMultiStatusSuccess(BaseModel):
    advertising_deal: "SBAdvertisingDeal" = Field(..., alias="advertisingDeal")
    index: int

    model_config = {'populate_by_name': True}


class SBAdvertisingDealMultiStatusResponse(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    success: Optional[list["SBAdvertisingDealMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class SBAdvertisingDealNameFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SBAdvertisingDealNameFilter(BaseModel):
    include: list[str]
    query_term_match_type: "SBAdvertisingDealNameFilterType" = Field(..., alias="queryTermMatchType")

    model_config = {'populate_by_name': True}


class SBAdvertisingDealSuccessResponse(BaseModel):
    advertising_deals: Optional[list["SBAdvertisingDeal"]] = Field(None, alias="advertisingDeals")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class SBAdvertisingDealTargetType(StrEnum):
    BRANDED_KEYWORD = "BRANDED_KEYWORD"


class SBAdvertisingDealTargetDetails(BaseModel):
    pass


class SBAdvertisingDealTarget(BaseModel):
    advertising_deal_id: str = Field(..., alias="advertisingDealId", description="A unique identifier for the deal associated with the target.")
    advertising_deal_target_id: str = Field(..., alias="advertisingDealTargetId", description="A unique identifier for a deal target.")
    target_details: "SBAdvertisingDealTargetDetails" = Field(..., alias="targetDetails")
    target_type: "SBAdvertisingDealTargetType" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class SBAdvertisingDealTargetAdvertisingDealIdFilter(BaseModel):
    include: list[str]

    model_config = {'populate_by_name': True}


class SBCreateAdvertisingDealBrandedKeywordTargetDetails(BaseModel):
    """The detail of a BRANDED_KEYWORD target."""
    branded_keyword: str = Field(..., alias="brandedKeyword", description="The branded keyword that is an exact match to the shoppers' search term.")

    model_config = {'populate_by_name': True}


class SBCreateAdvertisingDealTargetDetails(BaseModel):
    pass


class SBAdvertisingDealTargetCreate(BaseModel):
    advertising_deal_id: str = Field(..., alias="advertisingDealId", description="A unique identifier for the deal associated with the target.")
    target_details: "SBCreateAdvertisingDealTargetDetails" = Field(..., alias="targetDetails")
    target_type: "SBAdvertisingDealTargetType" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class SBAdvertisingDealTargetMultiStatusSuccess(BaseModel):
    advertising_deal_target: "SBAdvertisingDealTarget" = Field(..., alias="advertisingDealTarget")
    index: int

    model_config = {'populate_by_name': True}


class SBAdvertisingDealTargetMultiStatusResponse(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    success: Optional[list["SBAdvertisingDealTargetMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class SBAdvertisingDealTargetSuccessResponse(BaseModel):
    advertising_deal_targets: Optional[list["SBAdvertisingDealTarget"]] = Field(None, alias="advertisingDealTargets")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class SBUpdateAdvertisingDealPrice(BaseModel):
    price_type: Optional["SBAdvertisingDealPriceType"] = Field(None, alias="priceType")
    value: Optional[float] = Field(None, description="The monetary amount of the price in the given currency.")

    model_config = {'populate_by_name': True}


class SBAdvertisingDealUpdate(BaseModel):
    advertising_deal_id: str = Field(..., alias="advertisingDealId", description="A unique identifier for a deal.")
    end_date_time: Optional[str] = Field(None, alias="endDateTime", description="The end date time for the deal.")
    name: Optional[str] = Field(None, description="The name of the deal.")
    price: Optional["SBUpdateAdvertisingDealPrice"] = None
    replacing_deal_id: Optional[str] = Field(None, alias="replacingDealId", description="The ID of an advertising deal that this deal intends to replace.")
    start_date_time: Optional[str] = Field(None, alias="startDateTime", description="The start date time for the deal.")
    state: Optional["SBAdvertisingDealState"] = None

    model_config = {'populate_by_name': True}


class SBAlternateBrandIdType(StrEnum):
    BRAND_REGISTRY = "BRAND_REGISTRY"


class SBBrandAlternateId(BaseModel):
    """Other types of brand identifiers for a brand that are used with other operations."""
    alternate_brand_id: str = Field(..., alias="alternateBrandId", description="The alternative brand identifier for the brandId.")
    alternate_brand_id_type: "SBAlternateBrandIdType" = Field(..., alias="alternateBrandIdType")

    model_config = {'populate_by_name': True}


class SBBrandedKeyword(BaseModel):
    brand_alternate_id: "SBBrandAlternateId" = Field(..., alias="brandAlternateId")
    keyword: str = Field(..., description="Branded keyword")

    model_config = {'populate_by_name': True}


class SBBrandedKeywordList(BaseModel):
    associated_brand_ids: Optional[list[str]] = Field(None, alias="associatedBrandIds", description="Brand IDs associated with the branded keyword list")
    branded_keyword: Optional[list["SBBrandedKeyword"]] = Field(None, alias="brandedKeyword", description="Branded keywords are specific words or phrases that include a company's brand name or a registered trademark of a brand")

    model_config = {'populate_by_name': True}


class SBBrandedKeywordRecommendationTypeDetails(BaseModel):
    brand_alternate_id: list["SBBrandAlternateId"] = Field(..., alias="brandAlternateId")
    brand_ids: Optional[list[str]] = Field(None, alias="brandIds", description="The brand ID to scope branded keyword recommendations for")

    model_config = {'populate_by_name': True}


class SBKeywordsPricing(BaseModel):
    """The detail of keywords pricing."""
    price: "SBAdvertisingDealPrice"
    valid_keywords: list[str] = Field(..., alias="validKeywords", description="List of valid keywords.")

    model_config = {'populate_by_name': True}


class SBRejectedKeyword(BaseModel):
    """The detail of a rejected keyword."""
    keyword: str = Field(..., description="The keyword that has been rejected.")
    reason: str = Field(..., description="The reason keyword has been rejected for this advertiser.")

    model_config = {'populate_by_name': True}


class SBBrandedKeywordsPricing(BaseModel):
    advertising_deal_id: Optional[str] = Field(None, alias="advertisingDealId", description="Identifier of the existing deal to price. Omit when pricing a new deal.")
    branded_keywords_pricing_id: str = Field(..., alias="brandedKeywordsPricingId", description="A unique identifier for the branded keywords pricing.")
    end_date_time: str = Field(..., alias="endDateTime", description="The end date time for the deal.")
    keywords: list[str] = Field(..., description="The list of branded keywords advertiser wants to reserve.")
    keywords_pricing: Optional["SBKeywordsPricing"] = Field(None, alias="keywordsPricing")
    rejected_keywords: Optional[list["SBRejectedKeyword"]] = Field(None, alias="rejectedKeywords", description="The list of branded keywords rejected for reservation by this advertiser.")
    start_date_time: str = Field(..., alias="startDateTime", description="The start date time for the deal.")

    model_config = {'populate_by_name': True}


class SBBrandedKeywordsPricingCreate(BaseModel):
    advertising_deal_id: Optional[str] = Field(None, alias="advertisingDealId", description="Identifier of the existing deal to price. Omit when pricing a new deal.")
    end_date_time: str = Field(..., alias="endDateTime", description="The end date time for the deal.")
    keywords: list[str] = Field(..., description="The list of branded keywords advertiser wants to reserve.")
    start_date_time: str = Field(..., alias="startDateTime", description="The start date time for the deal.")

    model_config = {'populate_by_name': True}


class SBBrandedKeywordsPricingMultiStatusSuccess(BaseModel):
    branded_keywords_pricing: "SBBrandedKeywordsPricing" = Field(..., alias="brandedKeywordsPricing")
    index: int

    model_config = {'populate_by_name': True}


class SBBrandedKeywordsPricingMultiStatusResponse(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    success: Optional[list["SBBrandedKeywordsPricingMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class SBCreateAdvertisingDealRequest(BaseModel):
    advertising_deals: Optional[list["SBAdvertisingDealCreate"]] = Field(None, alias="advertisingDeals")

    model_config = {'populate_by_name': True}


class SBCreateAdvertisingDealTargetRequest(BaseModel):
    advertising_deal_targets: Optional[list["SBAdvertisingDealTargetCreate"]] = Field(None, alias="advertisingDealTargets")

    model_config = {'populate_by_name': True}


class SBCreateBrandAlternateId(BaseModel):
    """Other types of brand identifiers for a brand that are used with other operations."""
    alternate_brand_id: str = Field(..., alias="alternateBrandId", description="The alternative brand identifier for the brandId.")
    alternate_brand_id_type: "SBAlternateBrandIdType" = Field(..., alias="alternateBrandIdType")

    model_config = {'populate_by_name': True}


class SBCreateBrandedKeywordRecommendationTypeDetails(BaseModel):
    brand_alternate_id: list["SBCreateBrandAlternateId"] = Field(..., alias="brandAlternateId")
    brand_ids: Optional[list[str]] = Field(None, alias="brandIds", description="The brand ID to scope branded keyword recommendations for")

    model_config = {'populate_by_name': True}


class SBCreateBrandedKeywordsPricingRequest(BaseModel):
    branded_keywords_pricings: Optional[list["SBBrandedKeywordsPricingCreate"]] = Field(None, alias="brandedKeywordsPricings")

    model_config = {'populate_by_name': True}


class SBKeywordReservationValidationCreate(BaseModel):
    keyword: str = Field(..., description="Keyword to be validated.")

    model_config = {'populate_by_name': True}


class SBCreateKeywordReservationValidationRequest(BaseModel):
    keyword_reservation_validations: Optional[list["SBKeywordReservationValidationCreate"]] = Field(None, alias="keywordReservationValidations")

    model_config = {'populate_by_name': True}


class SBCreateRecommendationTypeDetails(BaseModel):
    pass


class SBRecommendationCreate(BaseModel):
    recommendation_type: str = Field(..., alias="recommendationType", description="A unique value to indicate similar recommendations, used for internal purposes only")
    recommendation_type_details: Optional["SBCreateRecommendationTypeDetails"] = Field(None, alias="recommendationTypeDetails")

    model_config = {'populate_by_name': True}


class SBCreateRecommendationRequest(BaseModel):
    recommendations: Optional[list["SBRecommendationCreate"]] = None

    model_config = {'populate_by_name': True}


class SBDeleteAdvertisingDealRequest(BaseModel):
    advertising_deal_ids: Optional[list[str]] = Field(None, alias="advertisingDealIds")

    model_config = {'populate_by_name': True}


class SBDeleteAdvertisingDealTargetRequest(BaseModel):
    advertising_deal_target_ids: Optional[list[str]] = Field(None, alias="advertisingDealTargetIds")

    model_config = {'populate_by_name': True}


class SBKeywordReservationValidation(BaseModel):
    is_reservable: bool = Field(..., alias="isReservable", description="Whether the keyword can be reserved or not.")
    keyword: str = Field(..., description="Keyword to be validated.")
    keyword_reservation_validation_id: str = Field(..., alias="keywordReservationValidationId", description="The identifier of the KeywordReservationValidation.")
    reservation_rejected_reason: Optional[str] = Field(None, alias="reservationRejectedReason", description="Reason why the keyword cannot be reserved. It is present only when isReservable is false.")

    model_config = {'populate_by_name': True}


class SBKeywordReservationValidationMultiStatusSuccess(BaseModel):
    index: int
    keyword_reservation_validation: "SBKeywordReservationValidation" = Field(..., alias="keywordReservationValidation")

    model_config = {'populate_by_name': True}


class SBKeywordReservationValidationMultiStatusResponse(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    success: Optional[list["SBKeywordReservationValidationMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class SBObjectSettings(BaseModel):
    pass


class SBQueryAdvertisingDealRequest(BaseModel):
    advertising_deal_id_filter: Optional["SBAdvertisingDealAdvertisingDealIdFilter"] = Field(None, alias="advertisingDealIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults")
    name_filter: Optional["SBAdvertisingDealNameFilter"] = Field(None, alias="nameFilter")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class SBQueryAdvertisingDealTargetRequest(BaseModel):
    advertising_deal_id_filter: "SBAdvertisingDealTargetAdvertisingDealIdFilter" = Field(..., alias="advertisingDealIdFilter")
    max_results: Optional[int] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class SBQueryRecommendationTypeRequest(BaseModel):
    max_results: Optional[int] = Field(None, alias="maxResults")
    next_token: Optional[str] = Field(None, alias="nextToken")

    model_config = {'populate_by_name': True}


class SBRecommendedObject(BaseModel):
    """Details of the recommended object"""
    recommended_object_settings: Optional["SBObjectSettings"] = Field(None, alias="recommendedObjectSettings")

    model_config = {'populate_by_name': True}


class SBRecommendationTypeDetails(BaseModel):
    pass


class SBRecommendation(BaseModel):
    recommendation_id: str = Field(..., alias="recommendationId", description="The identifier of the recommendation")
    recommendation_type: str = Field(..., alias="recommendationType", description="A unique value to indicate similar recommendations, used for internal purposes only")
    recommendation_type_details: Optional["SBRecommendationTypeDetails"] = Field(None, alias="recommendationTypeDetails")
    recommended_objects: list["SBRecommendedObject"] = Field(..., alias="recommendedObjects", description="The target objects of the recommendation")

    model_config = {'populate_by_name': True}


class SBRecommendationMultiStatusSuccess(BaseModel):
    index: int
    recommendation: "SBRecommendation"

    model_config = {'populate_by_name': True}


class SBRecommendationMultiStatusResponse(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    success: Optional[list["SBRecommendationMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class SBRecommendationType(BaseModel):
    recommendation_type_id: str = Field(..., alias="recommendationTypeId", description="The ID of the recommendation type. Format: Either a UUID or a unique descriptive string identifier")
    recommendation_type_title: str = Field(..., alias="recommendationTypeTitle", description="Titles or short descriptions of the recommendation")

    model_config = {'populate_by_name': True}


class SBRecommendationTypeEnum(StrEnum):
    BRANDED_KEYWORD = "BRANDED_KEYWORD"


class SBRecommendationTypeSuccessResponse(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken")
    recommendation_types: Optional[list["SBRecommendationType"]] = Field(None, alias="recommendationTypes")

    model_config = {'populate_by_name': True}


class SBUpdateAdvertisingDealRequest(BaseModel):
    advertising_deals: Optional[list["SBAdvertisingDealUpdate"]] = Field(None, alias="advertisingDeals")

    model_config = {'populate_by_name': True}


class ServiceUnavailableErrorResponseContent(BaseModel):
    code: str
    message: str

    model_config = {'populate_by_name': True}


class TargetLevel(StrEnum):
    AD_GROUP = "AD_GROUP"
    CAMPAIGN = "CAMPAIGN"


class TargetBidMarketplaceSetting(BaseModel):
    bid: Optional[float] = Field(None, description="The maximum bid for a target.")
    currency_code: "CurrencyCode" = Field(..., alias="currencyCode")
    marketplace: "Marketplace"

    model_config = {'populate_by_name': True}


class TargetBid(BaseModel):
    bid: Optional[float] = Field(None, description="The maximum bid for a target.")
    currency_code: Optional["CurrencyCode"] = Field(None, alias="currencyCode")
    marketplace_settings: Optional[list["TargetBidMarketplaceSetting"]] = Field(None, alias="marketplaceSettings", description="The bid associated with the target at specified marketplace level. Either one of bid or marketplaceSettings should alway")

    model_config = {'populate_by_name': True}


class VideoContentDurationTarget(BaseModel):
    """Targets ads to a specific video content duration"""
    duration: "VideoContentDuration"

    model_config = {'populate_by_name': True}


class VideoAdFormatTarget(BaseModel):
    """Target based on the video ad format."""
    video_ad_format: "VideoAdFormat" = Field(..., alias="videoAdFormat")

    model_config = {'populate_by_name': True}


class ThirdPartyTargetDetails(BaseModel):
    pass


class ThirdPartyTarget(BaseModel):
    third_party_target_details: "ThirdPartyTargetDetails" = Field(..., alias="thirdPartyTargetDetails")
    third_party_target_type: "ThirdPartyTargetType" = Field(..., alias="thirdPartyTargetType")

    model_config = {'populate_by_name': True}


class TargetDetails(BaseModel):
    pass


class Target(BaseModel):
    ad_group_id: Optional[str] = Field(None, alias="adGroupId", description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.")
    ad_product: "AdProduct" = Field(..., alias="adProduct")
    bid: Optional["TargetBid"] = None
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.")
    creation_date_time: str = Field(..., alias="creationDateTime", description="The date time the target was created.")
    global_target_id: Optional[str] = Field(None, alias="globalTargetId", description="The global target identifier that manages this marketplace target.")
    last_updated_date_time: str = Field(..., alias="lastUpdatedDateTime", description="The date time the target was last updated.")
    marketplace_configurations: Optional[list["MarketplaceTargetConfigurations"]] = Field(None, alias="marketplaceConfigurations", description="List of marketplace-specific configurations for a global target that enables overriding certain attributes at individual")
    marketplace_scope: Optional["MarketplaceScope"] = Field(None, alias="marketplaceScope")
    marketplaces: Optional[list["Marketplace"]] = Field(None, description="The list of marketplace in which the global target is applicable. The marketplaces included should either be same as or ")
    negative: bool = Field(..., description="Indicates whether the target is negative or not.")
    state: "State"
    status: Optional["Status"] = None
    tags: Optional[list["Tag"]] = Field(None, description="Open ended labels with a key value pair applied to the target")
    target_details: "TargetDetails" = Field(..., alias="targetDetails")
    target_id: str = Field(..., alias="targetId", description="A unique identifier for the target.")
    target_level: Optional["TargetLevel"] = Field(None, alias="targetLevel")
    target_type: "TargetType" = Field(..., alias="targetType")

    model_config = {'populate_by_name': True}


class TargetPartialIndex(BaseModel):
    errors: list["Error"]
    index: int
    target: "Target"

    model_config = {'populate_by_name': True}


class TargetMultiStatusSuccess(BaseModel):
    index: int
    target: "Target"

    model_config = {'populate_by_name': True}


class TargetMultiStatusResponseWithPartialErrors(BaseModel):
    error: Optional[list["ErrorsIndex"]] = None
    partial_success: Optional[list["TargetPartialIndex"]] = Field(None, alias="partialSuccess")
    success: Optional[list["TargetMultiStatusSuccess"]] = None

    model_config = {'populate_by_name': True}


class TargetSuccessResponse(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken")
    targets: Optional[list["Target"]] = None
    total_results: Optional[int] = Field(None, alias="totalResults")

    model_config = {'populate_by_name': True}


class UpdateTargetBid(BaseModel):
    bid: Optional[float] = Field(None, description="The maximum bid for a target.")
    marketplace_settings: Optional[list["CreateTargetBidMarketplaceSetting"]] = Field(None, alias="marketplaceSettings", description="The bid associated with the target at specified marketplace level. Either one of bid or marketplaceSettings should alway")

    model_config = {'populate_by_name': True}


class TargetUpdate(BaseModel):
    bid: Optional["UpdateTargetBid"] = None
    campaign_id: Optional[str] = Field(None, alias="campaignId", description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.")
    marketplace_configurations: Optional[list["CreateMarketplaceTargetConfigurations"]] = Field(None, alias="marketplaceConfigurations", description="List of marketplace-specific configurations for a global target that enables overriding certain attributes at individual")
    marketplace_scope: Optional["MarketplaceScope"] = Field(None, alias="marketplaceScope")
    marketplaces: Optional[list["Marketplace"]] = Field(None, description="The list of marketplace in which the global target is applicable. The marketplaces included should either be same as or ")
    state: Optional["UpdateState"] = None
    tags: Optional[list["CreateTag"]] = Field(None, description="Open ended labels with a key value pair applied to the target")
    target_id: str = Field(..., alias="targetId", description="A unique identifier for the target.")

    model_config = {'populate_by_name': True}


class TooManyRequestsResponseContent(BaseModel):
    code: "ErrorCode"
    message: str

    model_config = {'populate_by_name': True}


class UnauthorizedResponseContent(BaseModel):
    code: "ErrorCode"
    message: str

    model_config = {'populate_by_name': True}


class UpdateAdAssociationRequest(BaseModel):
    ad_associations: Optional[list["AdAssociationUpdate"]] = Field(None, alias="adAssociations")

    model_config = {'populate_by_name': True}


class UpdateAdExtensionRequest(BaseModel):
    ad_extensions: Optional[list["AdExtensionUpdate"]] = Field(None, alias="adExtensions")

    model_config = {'populate_by_name': True}


class UpdateAdGroupRequest(BaseModel):
    ad_groups: Optional[list["AdGroupUpdate"]] = Field(None, alias="adGroups")

    model_config = {'populate_by_name': True}


class UpdateAdRequest(BaseModel):
    ads: Optional[list["AdUpdate"]] = None

    model_config = {'populate_by_name': True}


class UpdateBrandStoreEditionPublishVersionRequest(BaseModel):
    brand_store_edition_publish_versions: Optional[list["BrandStoreEditionPublishVersionUpdate"]] = Field(None, alias="brandStoreEditionPublishVersions")

    model_config = {'populate_by_name': True}


class UpdateCampaignRequest(BaseModel):
    campaigns: Optional[list["CampaignUpdate"]] = None

    model_config = {'populate_by_name': True}


class UpdateLocationIndexRequest(BaseModel):
    location_indexes: Optional[list["LocationIndexUpdate"]] = Field(None, alias="locationIndexes")

    model_config = {'populate_by_name': True}


class UpdateTargetRequest(BaseModel):
    targets: Optional[list["TargetUpdate"]] = None

    model_config = {'populate_by_name': True}

