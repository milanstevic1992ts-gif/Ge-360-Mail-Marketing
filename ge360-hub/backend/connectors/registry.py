from app.config import get_settings

from .mautic import MauticConnector
from .opencrm import OpenCRMConnector
from .prospex import ProspexConnector
from .twenty import TwentyConnector


def build_registry():
    settings = get_settings()
    return {
        "prospex": ProspexConnector(
            enabled=settings.prospex_enabled,
            base_url=settings.prospex_base_url,
        ),
        "twenty": TwentyConnector(
            enabled=settings.twenty_enabled,
            base_url=settings.twenty_base_url,
        ),
        "mautic": MauticConnector(
            enabled=settings.mautic_enabled,
            base_url=settings.mautic_base_url,
        ),
        "opencrm": OpenCRMConnector(
            enabled=settings.opencrm_enabled,
            base_url=settings.opencrm_base_url,
        ),
    }


connector_registry = build_registry()
