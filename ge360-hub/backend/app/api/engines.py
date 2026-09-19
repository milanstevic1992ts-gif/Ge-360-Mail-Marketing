from fastapi import APIRouter

from connectors import connector_registry

router = APIRouter(prefix="/engines", tags=["engines"])


@router.get("")
def list_engines() -> dict:
    return {
        name: {
            "enabled": connector.enabled,
            "configured": connector.configured,
            "capabilities": list(connector.capabilities),
        }
        for name, connector in connector_registry.items()
    }
