"""Publish processed records."""

from pathlib import Path
import json


def publish(records: list[dict], output_dir: str = "app/public/snapshots") -> Path:
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    outfile = path / "latest.json"
    with outfile.open("w", encoding="utf-8") as fh:
        json.dump(records, fh, ensure_ascii=False, indent=2)
    return outfile
