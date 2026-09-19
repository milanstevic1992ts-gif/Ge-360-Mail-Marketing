from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ExternalIdentityRead(BaseModel):
    engine: str
    external_id: str
    last_synced_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class ContactCreate(BaseModel):
    contact_type: str = "professional"
    first_name: str | None = None
    last_name: str | None = None
    company: str | None = None
    email: str | None = None
    phone: str | None = None
    website: str | None = None
    city: str | None = None
    province: str | None = None
    country: str = Field(default="IT", min_length=2, max_length=2)
    source: str | None = None
    source_url: str | None = None
    status: str = "new"
    marketing_status: str = "unknown"
    do_not_contact: bool = False
    notes: str | None = None


class ContactRead(ContactCreate):
    ge360_id: str
    created_at: datetime
    updated_at: datetime
    external_identities: list[ExternalIdentityRead] = []

    model_config = ConfigDict(from_attributes=True)
