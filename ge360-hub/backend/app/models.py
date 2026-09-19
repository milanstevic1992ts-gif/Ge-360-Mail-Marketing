from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, Index, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .db import Base


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def new_ge360_id() -> str:
    return f"CNT-{uuid4().hex[:12].upper()}"


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True)
    ge360_id: Mapped[str] = mapped_column(String(32), unique=True, index=True, default=new_ge360_id)
    contact_type: Mapped[str] = mapped_column(String(64), default="professional", index=True)

    first_name: Mapped[str | None] = mapped_column(String(120), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(120), nullable=True)
    company: Mapped[str | None] = mapped_column(String(200), nullable=True, index=True)
    email: Mapped[str | None] = mapped_column(String(320), nullable=True, index=True)
    phone: Mapped[str | None] = mapped_column(String(64), nullable=True)
    website: Mapped[str | None] = mapped_column(String(500), nullable=True)

    city: Mapped[str | None] = mapped_column(String(120), nullable=True, index=True)
    province: Mapped[str | None] = mapped_column(String(120), nullable=True)
    country: Mapped[str] = mapped_column(String(2), default="IT")

    source: Mapped[str | None] = mapped_column(String(120), nullable=True, index=True)
    source_url: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    status: Mapped[str] = mapped_column(String(64), default="new", index=True)

    marketing_status: Mapped[str] = mapped_column(String(64), default="unknown", index=True)
    do_not_contact: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, onupdate=utcnow)

    external_identities: Mapped[list[ExternalIdentity]] = relationship(
        back_populates="contact",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        Index("ix_contacts_name_company", "last_name", "company"),
    )


class ExternalIdentity(Base):
    __tablename__ = "external_identities"

    id: Mapped[int] = mapped_column(primary_key=True)
    contact_id: Mapped[int] = mapped_column(ForeignKey("contacts.id", ondelete="CASCADE"), index=True)
    engine: Mapped[str] = mapped_column(String(32), index=True)
    external_id: Mapped[str] = mapped_column(String(255))
    last_synced_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    contact: Mapped[Contact] = relationship(back_populates="external_identities")

    __table_args__ = (
        UniqueConstraint("engine", "external_id", name="uq_external_identity_engine_id"),
        UniqueConstraint("contact_id", "engine", name="uq_contact_engine"),
    )
