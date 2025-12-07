"""
Amazon DSP API 模块

官方文档: https://advertising.amazon.com/API/docs/en-us/dsp
"""

from .audiences import DSPAudiencesAPI
from .advertisers import DSPAdvertisersAPI
from .orders import DSPOrdersAPI
from .line_items import DSPLineItemsAPI
from .creatives import DSPCreativesAPI
from .inventory import DSPInventoryAPI
from .measurement import DSPMeasurementAPI
from .conversions import DSPConversionsAPI
from .target_kpi import DSPTargetKPIAPI

__all__ = [
    "DSPAudiencesAPI",
    "DSPAdvertisersAPI",
    "DSPOrdersAPI",
    "DSPLineItemsAPI",
    "DSPCreativesAPI",
    "DSPInventoryAPI",
    "DSPMeasurementAPI",
    "DSPConversionsAPI",
    "DSPTargetKPIAPI",
]
