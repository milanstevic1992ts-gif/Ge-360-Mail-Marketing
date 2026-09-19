from typing import Any

from .base import BaseConnector


class TwentyConnector(BaseConnector):
    name = "twenty"
    capabilities = ("crm", "contacts", "opportunities")

    async def pull_contacts(self) -> list[dict[str, Any]]:
        raise NotImplementedError("Twenty API mapping is scheduled for roadmap v0.2")

    async def push_contact(self, contact: dict[str, Any]) -> str:
        raise NotImplementedError("Twenty API mapping is scheduled for roadmap v0.2")
