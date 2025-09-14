"""Score records to indicate confidence."""


def score(records: list[dict]) -> list[dict]:
    for rec in records:
        rec.setdefault("score", 0)
    return records
