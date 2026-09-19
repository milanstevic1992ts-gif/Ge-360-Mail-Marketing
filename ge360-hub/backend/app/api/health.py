from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.config import get_settings
from app.db import get_db

router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
def health(db: Session = Depends(get_db)) -> dict:
    db.execute(text("SELECT 1"))
    settings = get_settings()

    return {
        "status": "ok",
        "service": "ge360-mail-marketing-core",
        "engines": {
            "prospex": {"enabled": settings.prospex_enabled, "configured": bool(settings.prospex_base_url)},
            "twenty": {"enabled": settings.twenty_enabled, "configured": bool(settings.twenty_base_url)},
            "mautic": {"enabled": settings.mautic_enabled, "configured": bool(settings.mautic_base_url)},
            "opencrm": {"enabled": settings.opencrm_enabled, "configured": bool(settings.opencrm_base_url)},
        },
    }
