from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.db import get_db
from app.models import Contact
from app.schemas import ContactCreate, ContactRead

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.post("", response_model=ContactRead, status_code=status.HTTP_201_CREATED)
def create_contact(payload: ContactCreate, db: Session = Depends(get_db)) -> Contact:
    contact = Contact(**payload.model_dump())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


@router.get("", response_model=list[ContactRead])
def list_contacts(
    limit: int = Query(default=50, ge=1, le=250),
    offset: int = Query(default=0, ge=0),
    contact_status: str | None = Query(default=None, alias="status"),
    city: str | None = None,
    db: Session = Depends(get_db),
) -> list[Contact]:
    stmt = (
        select(Contact)
        .options(selectinload(Contact.external_identities))
        .order_by(Contact.created_at.desc())
        .limit(limit)
        .offset(offset)
    )

    if contact_status:
        stmt = stmt.where(Contact.status == contact_status)
    if city:
        stmt = stmt.where(Contact.city == city)

    return list(db.scalars(stmt).all())


@router.get("/{ge360_id}", response_model=ContactRead)
def get_contact(ge360_id: str, db: Session = Depends(get_db)) -> Contact:
    stmt = (
        select(Contact)
        .options(selectinload(Contact.external_identities))
        .where(Contact.ge360_id == ge360_id)
    )
    contact = db.scalar(stmt)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact
