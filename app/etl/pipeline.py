"""Orchestrates the ETL workflow."""

import asyncio

from . import normalizer, scorer, publisher
from .sources._fixtures import fake_items


async def run() -> None:
    records = fake_items()
    records = normalizer.normalize(records)
    records = scorer.score(records)
    publisher.publish_delta(records)


if __name__ == "__main__":
    asyncio.run(run())
