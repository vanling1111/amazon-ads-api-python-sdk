"""Auto-generated Pydantic models. Do not edit manually.

Source: Advertisers_prod_3p.json
Title:  Advertisers
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class AccountBudgetFeatureFlagsErrorCode(StrEnum):
    ENTRY_NOT_FOUND = "ENTRY_NOT_FOUND"
    INVALID_PARAMETER_VALUE = "INVALID_PARAMETER_VALUE"
    OK = "OK"


class AccountBudgetFeatureFlagsError(BaseModel):
    """The Error Response Object."""
    code: Optional[AccountBudgetFeatureFlagsErrorCode] = Field(None, description="An enumerated code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}


class FeatureFlags(BaseModel):
    """Feature flags for account budget, which denotes that advertiser Opted In/Out from specific budget feature."""
    is_opted_out_for_average_daily_budget_increase: Optional[bool] = Field(None, alias="isOptedOutForAverageDailyBudgetIncrease", description="Denotes the opt in/out decision for AverageDailyBudgetIncrease feature. If the entity spends less than your daily budget")

    model_config = {'populate_by_name': True}


class GetAccountBudgetFeatureFlagsResponse(BaseModel):
    """Response to get account budget feature flags information."""
    feature_flags: Optional["FeatureFlags"] = Field(None, alias="featureFlags")

    model_config = {'populate_by_name': True}


class UpdateAccountBudgetFeatureFlagsRequest(BaseModel):
    """Request to update account budget feature flags information."""
    feature_flags: "FeatureFlags" = Field(..., alias="featureFlags")

    model_config = {'populate_by_name': True}


class UpdateAccountBudgetFeatureFlagsResponseCode(StrEnum):
    ENTRY_NOT_FOUND = "ENTRY_NOT_FOUND"
    INVALID_PARAMETER_VALUE = "INVALID_PARAMETER_VALUE"
    OK = "OK"


class UpdateAccountBudgetFeatureFlagsResponse(BaseModel):
    """Response for update account budget feature flags information."""
    code: Optional[UpdateAccountBudgetFeatureFlagsResponseCode] = Field(None, description="An enumerated code for machine use.")
    details: Optional[str] = Field(None, description="A human-readable description of the response.")

    model_config = {'populate_by_name': True}

