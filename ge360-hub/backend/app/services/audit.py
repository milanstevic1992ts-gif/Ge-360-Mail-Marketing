from sqlalchemy.orm import Session

from app.models import AuditEvent


def record_event(
    db: Session,
    *,
    entity_type: str,
    entity_id: str,
    action: str,
    actor: str = "ge360-core",
    source_engine: str | None = None,
    detail: str | None = None,
) -> AuditEvent:
    event = AuditEvent(
        entity_type=entity_type,
        entity_id=entity_id,
        action=action,
        actor=actor,
        source_engine=source_engine,
        detail=detail,
    )
    db.add(event)
    return event
