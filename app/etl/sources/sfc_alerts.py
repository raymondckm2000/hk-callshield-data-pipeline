"""Fetch phone numbers from Securities and Futures Commission alerts."""

from __future__ import annotations

import re

import httpx
from bs4 import BeautifulSoup

from app.utils.phone import to_e164

# The SFC publishes an alert list of suspicious entities.  This is the English
# page which contains phone numbers that we can scrape.
BASE_URL = "https://www.sfc.hk/en/alert-list"

# Loose pattern to identify phone numbers embedded in the alert text.
PHONE_RE = re.compile(r"\+?\d[\d\s-]{5,}\d")


def fetch() -> list[dict]:
    """Fetch SFC alert list and extract phone numbers.

    The alert list is an HTML page.  We scan common elements that might contain
    phone numbers, normalise them to E.164 and return a record for each number
    discovered.
    """

    with httpx.Client(timeout=30) as client:
        resp = client.get(BASE_URL)
        resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "lxml")
    items: list[dict] = []

    # Table rows, list items and paragraphs cover the majority of page layouts.
    for element in soup.select("table tr, ul li, p"):
        text = element.get_text(" ", strip=True)
        for raw in PHONE_RE.findall(text):
            norm = to_e164(raw)
            if not norm:
                continue
            e164, is_overseas = norm
            items.append(
                {
                    "e164": e164,
                    "is_overseas": is_overseas,
                    "label": "scam",
                    "snippet": text,
                    "url": BASE_URL,
                    "source": "SFC",
                }
            )

    return items
