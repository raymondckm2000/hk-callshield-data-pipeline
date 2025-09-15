from __future__ import annotations


def fake_items() -> list[dict]:
    return [
        {"e164": "+85261234567", "label": "scam", "snippet": "測試號碼 A", "url": "https://example/a", "source": "HKPF"},
        {"e164": "+85251234567", "label": "telemarketing", "snippet": "測試號碼 B", "url": "https://example/b", "source": "HKMA"},
        {"e164": "+81312345678", "label": "scam", "snippet": "日本號測試", "url": "https://example/c", "source": "SFC"},
    ]
