"""Normalize source records."""

from ..utils.phone import normalize_phone


def normalize(records: list[dict]) -> list[dict]:
    """Ensure each record has an E.164 phone number.

    The original sources may provide either a ``number`` field containing
    arbitrary characters or an ``e164`` field.  For our test fixtures we only
    supply ``e164`` so the normaliser simply preserves it, but if ``number`` is
    provided we strip non-digit characters and prefix it with a ``+`` to
    resemble an E.164 value.
    """

    for rec in records:
        if "number" in rec and "e164" not in rec:
            rec["e164"] = "+" + normalize_phone(rec["number"])
    return records
