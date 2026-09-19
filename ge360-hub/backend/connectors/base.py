from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ConnectorState:
    name: str
    enabled: bool
    configured: bool
    capabilities: tuple[str, ...]


class BaseConnector(ABC):
    name: str
    capabilities: tuple[str, ...] = ()

    def __init__(self, *, enabled: bool, base_url: str) -> None:
        self.enabled = enabled
        self.base_url = base_url.rstrip("/")

    @property
    def configured(self) -> bool:
        return bool(self.base_url)

    def state(self) -> ConnectorState:
        return ConnectorState(
            name=self.name,
            enabled=self.enabled,
            configured=self.configured,
            capabilities=self.capabilities,
        )

    @abstractmethod
    async def pull_contacts(self) -> list[dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    async def push_contact(self, contact: dict[str, Any]) -> str:
        raise NotImplementedError
