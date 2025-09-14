"""Orchestrates the ETL workflow."""

from . import normalizer, scorer, publisher
from .sources import hkpf_scameter, hkma_alerts, sfc_alerts


def run() -> None:
    records: list[dict] = []
    for src in (hkpf_scameter, hkma_alerts, sfc_alerts):
        records.extend(src.fetch())
    records = normalizer.normalize(records)
    records = scorer.score(records)
    publisher.publish(records)


if __name__ == "__main__":
    run()
