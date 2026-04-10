"""Auto-generated Pydantic models. Do not edit manually.

Source: AdvertisingUserPermissionsManagement_prod_3p.json
Title:  Advertising User Permissions Management
"""

from __future__ import annotations

from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field



class AccessScope(StrEnum):
    ALL = "ALL"
    DIRECT = "DIRECT"
    EFFECTIVE = "EFFECTIVE"
    INDIRECT = "INDIRECT"


class AccessScopeFilter(BaseModel):
    include: Optional[list["AccessScope"]] = None

    model_config = {'populate_by_name': True}


class BadRequestExceptionResponseContent(BaseModel):
    code: Optional[str] = None
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class CountryCode(StrEnum):
    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    CL = "CL"
    CO = "CO"
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
    NG = "NG"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"
    ZA = "ZA"


class CountryCodesFilter(BaseModel):
    include: Optional[list["CountryCode"]] = None

    model_config = {'populate_by_name': True}


class DeleteUserPermissionsError(BaseModel):
    code: Optional[str] = None
    countries: Optional[list["CountryCode"]] = None
    message: Optional[str] = None
    user_id: Optional[str] = Field(None, alias="userId", description="User ID of the user that had an error when their permissions were deleted")

    model_config = {'populate_by_name': True}


class UserId(BaseModel):
    user_id: Optional[str] = Field(None, alias="userId")

    model_config = {'populate_by_name': True}


class DeleteUserPermissionsRequestContent(BaseModel):
    users: Optional[list["UserId"]] = None

    model_config = {'populate_by_name': True}


class DeleteUserPermissionsSuccess(BaseModel):
    user_id: Optional[str] = Field(None, alias="userId", description="User ID of the user having their permissions deleted")

    model_config = {'populate_by_name': True}


class DeleteUserPermissionsResponseContent(BaseModel):
    errors: Optional[list["DeleteUserPermissionsError"]] = None
    successes: Optional[list["DeleteUserPermissionsSuccess"]] = None

    model_config = {'populate_by_name': True}


class ForbiddenExceptionResponseContent(BaseModel):
    code: Optional[str] = None
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class ListUsersRequestContent(BaseModel):
    access_scope_filter: Optional["AccessScopeFilter"] = Field(None, alias="accessScopeFilter")
    country_codes_filter: Optional["CountryCodesFilter"] = Field(None, alias="countryCodesFilter")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Max results for pagination")
    next_token: Optional[str] = Field(None, alias="nextToken", description="The pagination token that is required to go to the next page")

    model_config = {'populate_by_name': True}


class User(BaseModel):
    country_codes: Optional[list["CountryCode"]] = Field(None, alias="countryCodes")
    email_address: str = Field(..., alias="emailAddress")
    user_id: str = Field(..., alias="userId")

    model_config = {'populate_by_name': True}


class ListUsersResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    users: Optional[list["User"]] = None

    model_config = {'populate_by_name': True}


class NotFoundExceptionResponseContent(BaseModel):
    code: Optional[str] = None
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class Permission(BaseModel):
    access_level: Optional[str] = Field(None, alias="accessLevel")
    country_codes: Optional[list["CountryCode"]] = Field(None, alias="countryCodes")
    id_: Optional[str] = Field(None, alias="id")
    resource_type: Optional[str] = Field(None, alias="resourceType")

    model_config = {'populate_by_name': True}


class PermissionId(BaseModel):
    name: Optional[str] = None

    model_config = {'populate_by_name': True}


class Role(StrEnum):
    ADMIN = "ADMIN"
    EDITOR = "EDITOR"
    VIEWER = "VIEWER"


class Type(StrEnum):
    CUSTOM_PERMISSION_SET = "CUSTOM_PERMISSION_SET"
    ROLE = "ROLE"


class PermissionSet(BaseModel):
    custom_permission_set: Optional[list["PermissionId"]] = Field(None, alias="customPermissionSet", description="If type = CUSTOM_PERMISSION_SET, indicates the permissions of the invitation. Different permissions are supported for di")
    role: Optional["Role"] = None
    type_: "Type" = Field(..., alias="type")

    model_config = {'populate_by_name': True}


class QueryUserPermissionsRequestContent(BaseModel):
    access_scope_filter: Optional["AccessScopeFilter"] = Field(None, alias="accessScopeFilter")
    country_codes_filter: Optional["CountryCodesFilter"] = Field(None, alias="countryCodesFilter")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Max results for pagination")
    next_token: Optional[str] = Field(None, alias="nextToken", description="The pagination token that is required to go to the next page")
    user_id: str = Field(..., alias="userId", description="User ID for the request")

    model_config = {'populate_by_name': True}


class QueryUserPermissionsResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    permissions: Optional[list["Permission"]] = None

    model_config = {'populate_by_name': True}


class QueryUserRolesRequestContent(BaseModel):
    country_codes_filter: Optional["CountryCodesFilter"] = Field(None, alias="countryCodesFilter")
    max_results: Optional[float] = Field(None, alias="maxResults", description="Max results for pagination")
    next_token: Optional[str] = Field(None, alias="nextToken", description="The pagination token that is required to go to the next page")
    user_id: str = Field(..., alias="userId", description="This represents the userId of the target of the QueryUserRoles call")

    model_config = {'populate_by_name': True}


class RoleForCountries(BaseModel):
    country_codes: Optional[list["CountryCode"]] = Field(None, alias="countryCodes", description="The roles for an account are associated to a specific country/countries These roles may differ per countries")
    role: Optional["Role"] = None
    type_: Optional["Type"] = Field(None, alias="type")

    model_config = {'populate_by_name': True}


class QueryUserRolesResponseContent(BaseModel):
    next_token: Optional[str] = Field(None, alias="nextToken", description="token value allowing to navigate to the next response page")
    roles: Optional[list["RoleForCountries"]] = None

    model_config = {'populate_by_name': True}


class RateLimitExceededExceptionResponseContent(BaseModel):
    code: Optional[str] = None
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class ServiceExceptionResponseContent(BaseModel):
    code: Optional[str] = None
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class UnauthorizedExceptionResponseContent(BaseModel):
    code: Optional[str] = None
    message: Optional[str] = None

    model_config = {'populate_by_name': True}


class UpdateUserPermissionsError(BaseModel):
    code: Optional[str] = None
    message: Optional[str] = None
    user_id: Optional[str] = Field(None, alias="userId", description="User ID of the user having their permissions updated")

    model_config = {'populate_by_name': True}


class UserPermission(BaseModel):
    country_codes: Optional[list["CountryCode"]] = Field(None, alias="countryCodes", description="List of two-letter ISO 3166 country codes that the user is having permissions edited for. Only valid for updates to glob")
    permission_set: Optional["PermissionSet"] = Field(None, alias="permissionSet")
    user_id: Optional[str] = Field(None, alias="userId", description="User ID of the user having their permissions updated")

    model_config = {'populate_by_name': True}


class UpdateUserPermissionsRequestContent(BaseModel):
    user_permissions: Optional[list["UserPermission"]] = Field(None, alias="userPermissions")

    model_config = {'populate_by_name': True}


class UpdateUserPermissionsSuccess(BaseModel):
    user_id: Optional[str] = Field(None, alias="userId", description="User ID of the user having their permissions updated")

    model_config = {'populate_by_name': True}


class UpdateUserPermissionsResponseContent(BaseModel):
    errors: Optional[list["UpdateUserPermissionsError"]] = None
    successes: Optional[list["UpdateUserPermissionsSuccess"]] = None

    model_config = {'populate_by_name': True}


class UserCannotBeRemovedExceptionResponseContent(BaseModel):
    code: Optional[str] = None
    countries: Optional[list["CountryCode"]] = None
    message: Optional[str] = None

    model_config = {'populate_by_name': True}

