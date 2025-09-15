"""Publish processed records."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from ..config import IOS_CHUNK_SIZE, PUBLISH_DIR


def publish(records: list[dict], output_dir: str | None = None) -> Path:
    """Write records to a JSON file under the publish directory."""
    base = Path(output_dir or PUBLISH_DIR) / "snapshots"
    base.mkdir(parents=True, exist_ok=True)
    outfile = base / "latest.json"
    with outfile.open("w", encoding="utf-8") as fh:
        json.dump(records, fh, ensure_ascii=False, indent=2)
    return outfile


def publish_delta(records: list[dict], output_dir: str | None = None) -> Path:
    """Write delta and iOS blocklist artifacts.

    This simplified implementation treats all provided records as additions and
    emits chunked blocklists for iOS clients as well as a ``latest.json`` index
    file describing the generated artefacts.
    """

    base = Path(output_dir or PUBLISH_DIR)
    delta_dir = base / "delta"
    ios_dir = base / "ios"
    delta_dir.mkdir(parents=True, exist_ok=True)
    ios_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    additions = delta_dir / f"additions_{ts}.json"
    removals = delta_dir / f"removals_{ts}.json"
    with additions.open("w", encoding="utf-8") as fh:
        json.dump(records, fh, ensure_ascii=False, indent=2)
    with removals.open("w", encoding="utf-8") as fh:
        json.dump([], fh, ensure_ascii=False, indent=2)

    chunk_paths: list[str] = []
    for i in range(0, len(records), IOS_CHUNK_SIZE):
        chunk = records[i : i + IOS_CHUNK_SIZE]
        outfile = ios_dir / f"blocklist_chunk_{(i // IOS_CHUNK_SIZE) + 1}.json"
        with outfile.open("w", encoding="utf-8") as fh:
            json.dump([r["e164"] for r in chunk], fh, ensure_ascii=False, indent=2)
        chunk_paths.append(str(outfile.relative_to(base)))

    latest = {
        "generated_at": ts,
        "additions": [str(additions.relative_to(base))],
        "removals": [str(removals.relative_to(base))],
        "ios_chunks": chunk_paths,
    }
    latest_path = base / "latest.json"
    with latest_path.open("w", encoding="utf-8") as fh:
        json.dump(latest, fh, ensure_ascii=False, indent=2)
    return latest_path
