from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.contacts import router as contacts_router
from app.api.health import router as health_router
from app.db import Base, engine
from app import models  # noqa: F401


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Bootstrap only. Alembic migrations will replace create_all before production releases.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="GE360 Mail Marketing Core",
    version="0.1.0-dev",
    description="Orchestrator API for contacts, external engines, campaigns and opportunities.",
    lifespan=lifespan,
)

app.include_router(health_router, prefix="/api")
app.include_router(contacts_router, prefix="/api")


@app.get("/")
def root() -> dict[str, str]:
    return {
        "service": "GE360 Mail Marketing",
        "status": "running",
        "docs": "/docs",
        "health": "/api/health",
    }
