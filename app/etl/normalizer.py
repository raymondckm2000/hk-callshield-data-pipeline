"""Normalize source records."""

from .sources import hkpf_scameter, hkma_alerts, sfc_alerts  # noqa: F401
from ..utils.phone import normalize_phone


def normalize(records: list[dict]) -> list[dict]:
    for rec in records:
        rec["number"] = normalize_phone(rec["number"])
    return records
