from typing import Any

from .base import BaseConnector


class OpenCRMConnector(BaseConnector):
    name = "opencrm"
    capabilities = ("sales_ai", "pipeline")

    async def pull_contacts(self) -> list[dict[str, Any]]:
        raise NotImplementedError("OpenCRM API mapping is scheduled for roadmap v0.4")

    async def push_contact(self, contact: dict[str, Any]) -> str:
        raise NotImplementedError("OpenCRM API mapping is scheduled for roadmap v0.4")
