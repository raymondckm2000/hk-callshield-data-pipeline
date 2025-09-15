"""Utility functions for phone numbers."""

import re
import phonenumbers

HK_REGION = "HK"
NON_DIGITS = re.compile(r"\D")


def normalize_phone(number: str) -> str:
    return NON_DIGITS.sub("", number)


def to_e164(raw: str) -> tuple[str, bool] | None:
    try:
        num = phonenumbers.parse(raw, HK_REGION)
        if not phonenumbers.is_valid_number(num):
            return None
        e164 = phonenumbers.format_number(
            num, phonenumbers.PhoneNumberFormat.E164
        )
        is_overseas = num.country_code != 852
        return e164, is_overseas
    except Exception:
        return None
