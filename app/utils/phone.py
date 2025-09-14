"""Utility functions for phone numbers."""

import re

NON_DIGITS = re.compile(r"\D")


def normalize_phone(number: str) -> str:
    return NON_DIGITS.sub("", number)
