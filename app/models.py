from datetime import datetime
from pydantic import BaseModel


class PhoneRecord(BaseModel):
    number: str
    source: str
    score: int | None = None
    created_at: datetime | None = None
