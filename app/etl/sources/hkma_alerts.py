"""Fetch data from Hong Kong Monetary Authority (HKMA) alerts.

This module scrapes the HKMA security alerts page and extracts phone numbers
that appear in each alert item.  Numbers are normalised to E.164 using
``app.utils.phone.to_e164`` and returned together with a short description of
the alert for context.
"""

from __future__ import annotations

import re

import httpx
from bs4 import BeautifulSoup

from app.utils.phone import to_e164


# The English HKMA security alerts page.  Each list item may contain one or
# more phone numbers and a short description.
BASE_URL = "https://www.hkma.gov.hk/eng/security-alerts/"

# Loose pattern to identify phone numbers within the alert text.
PHONE_RE = re.compile(r"\+?\d[\d\s-]{5,}\d")


def fetch() -> list[dict]:
    """Fetch HKMA security alerts and extract phone numbers.

    The HKMA page is mostly HTML lists and tables.  We search through common
    elements that may contain phone numbers, normalise them and build a record
    for each one found.
    """

    with httpx.Client(timeout=30) as client:
        resp = client.get(BASE_URL)
        resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "lxml")
    items: list[dict] = []

    # Iterate over table rows and list items; these cover the current layouts of
    # the alerts page.  Any text containing a phone number is captured.
    for element in soup.select("table tr, ul li"):
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
                    "source": "HKMA",
                }
            )

    return items
