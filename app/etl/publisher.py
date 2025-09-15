"""Publish processed records."""

from pathlib import Path
import json

from ..config import PUBLISH_DIR


def publish(records: list[dict], output_dir: str | None = None) -> Path:
    """Write records to a JSON file under the publish directory."""
    base = Path(output_dir or PUBLISH_DIR) / "snapshots"
    base.mkdir(parents=True, exist_ok=True)
    outfile = base / "latest.json"
    with outfile.open("w", encoding="utf-8") as fh:
        json.dump(records, fh, ensure_ascii=False, indent=2)
    return outfile
