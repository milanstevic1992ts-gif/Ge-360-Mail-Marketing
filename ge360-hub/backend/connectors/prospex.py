from typing import Any

from .base import BaseConnector


class ProspexConnector(BaseConnector):
    name = "prospex"
    capabilities = ("lead_discovery", "enrichment")

    async def pull_contacts(self) -> list[dict[str, Any]]:
        raise NotImplementedError("Prospex API mapping is scheduled for roadmap v0.2")

    async def push_contact(self, contact: dict[str, Any]) -> str:
        raise NotImplementedError("Prospex API mapping is scheduled for roadmap v0.2")
