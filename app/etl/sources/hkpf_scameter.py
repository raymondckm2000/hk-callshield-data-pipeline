"""Fetch scam phone numbers from the Hong Kong Police Force Scameter."""

from __future__ import annotations

import httpx
from bs4 import BeautifulSoup

from app.utils.phone import to_e164


# TODO: replace with the actual Scameter source URL once available.
BASE_URL = "https://example-hkpf-scameter/list"


def fetch() -> list[dict]:
    """Fetch Scameter data and convert phone numbers to E.164.

    The endpoint currently serves an HTML table where the first column
    contains phone numbers.  Each row is parsed and normalised with
    :func:`app.utils.phone.to_e164`.
    """

    with httpx.Client(timeout=30) as client:
        resp = client.get(BASE_URL)
        resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "lxml")
    items: list[dict] = []
    for row in soup.select("table tr"):
        cols = [td.get_text(strip=True) for td in row.select("td")]
        if not cols:
            continue
        raw = cols[0]
        norm = to_e164(raw)
        if not norm:
            continue
        e164, is_overseas = norm
        items.append(
            {
                "e164": e164,
                "is_overseas": is_overseas,
                "label": "scam",
                # TODO: extract a relevant snippet from the row for context.
                "snippet": "HKPF listing",
                "url": BASE_URL,
                "source": "HKPF",
            }
        )
    return items

