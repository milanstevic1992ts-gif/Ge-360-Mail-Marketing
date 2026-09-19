import re

from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session, selectinload

from app.models import Contact


def normalize_email(value: str | None) -> str | None:
    if not value:
        return None
    normalized = value.strip().lower()
    return normalized or None


def normalize_phone(value: str | None) -> str | None:
    if not value:
        return None
    digits = re.sub(r"\D+", "", value)
    return digits if len(digits) >= 7 else None


def find_duplicate_candidates(
    db: Session,
    *,
    email: str | None = None,
    phone: str | None = None,
    company: str | None = None,
    city: str | None = None,
    limit: int = 20,
) -> list[Contact]:
    clauses = []

    normalized_email = normalize_email(email)
    if normalized_email:
        clauses.append(func.lower(func.trim(Contact.email)) == normalized_email)

    normalized_phone = normalize_phone(phone)
    if normalized_phone:
        # Portable fallback for v0.1. Stronger normalized-phone storage is planned
        # before high-volume imports.
        clauses.append(Contact.phone == phone.strip())

    if company and company.strip():
        company_clause = func.lower(func.trim(Contact.company)) == company.strip().lower()
        if city and city.strip():
            company_clause = company_clause & (
                func.lower(func.trim(Contact.city)) == city.strip().lower()
            )
        clauses.append(company_clause)

    if not clauses:
        return []

    stmt = (
        select(Contact)
        .options(selectinload(Contact.external_identities))
        .where(or_(*clauses))
        .order_by(Contact.updated_at.desc())
        .limit(limit)
    )
    return list(db.scalars(stmt).all())
