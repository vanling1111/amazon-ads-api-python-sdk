"""Auto-generated Pydantic models. Do not edit manually.

Source: HashedRecords_prod_3p.json
Title:  Hashed Records
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field



class Sha256String(BaseModel):
    pass


class HashedRecord(BaseModel):
    address: Optional["Sha256String"] = Field(None, description="The street address normalized and hashed [according to the documentation](https://advertising.amazon.com/help/GCCXMZYCK4")
    city: Optional["Sha256String"] = Field(None, description="The city normalized and hashed [according to the documentation](https://advertising.amazon.com/help/GCCXMZYCK4RXWS6C).")
    email: Optional["Sha256String"] = Field(None, description="The email address normalized and hashed [according to the documentation](https://advertising.amazon.com/help/GCCXMZYCK4R")
    first_name: Optional["Sha256String"] = Field(None, alias="firstName", description="The first name normalized and hashed [according to the documentation](https://advertising.amazon.com/help/GCCXMZYCK4RXWS")
    last_name: Optional["Sha256String"] = Field(None, alias="lastName", description="The last name normalized and hashed [according to the documentation](https://advertising.amazon.com/help/GCCXMZYCK4RXWS6")
    phone: Optional["Sha256String"] = Field(None, description="The phone number normalized and hashed [according to the documentation](https://advertising.amazon.com/help/GCCXMZYCK4RX")
    postal_code: Optional["Sha256String"] = Field(None, alias="postalCode", description="The postal code normalized and hashed [according to the documentation](https://advertising.amazon.com/help/GCCXMZYCK4RXW")
    state: Optional["Sha256String"] = Field(None, description="The state or province normalized and hashed [according to the documentation](https://advertising.amazon.com/help/GCCXMZY")

    model_config = {'populate_by_name': True}


class IngestionRecord(BaseModel):
    external_id: str = Field(..., alias="externalId", description="The external identifier for this record.  This can be any ID unique to the record in the caller's own identity space, an")
    hashed_records: list["HashedRecord"] = Field(..., alias="hashedRecords", description="list of hashed records data")

    model_config = {'populate_by_name': True}


class IngestionRecordsList(BaseModel):
    """The list of hashed records."""
    pass

