from typing import Any

from .base import BaseConnector


class MauticConnector(BaseConnector):
    name = "mautic"
    capabilities = ("segments", "campaigns", "email_events")

    async def pull_contacts(self) -> list[dict[str, Any]]:
        raise NotImplementedError("Mautic API mapping is scheduled for roadmap v0.3")

    async def push_contact(self, contact: dict[str, Any]) -> str:
        raise NotImplementedError("Mautic API mapping is scheduled for roadmap v0.3")
