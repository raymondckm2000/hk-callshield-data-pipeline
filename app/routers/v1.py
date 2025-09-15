from fastapi import APIRouter, HTTPException

from ..db import get_db
from ..models import PhoneRecord

router = APIRouter()


@router.get("/numbers/{phone}", response_model=PhoneRecord)
def get_phone(phone: str) -> PhoneRecord:
    with get_db() as db:
        with db.cursor() as cur:
            cur.execute(
                "SELECT number, source, score, created_at FROM phones WHERE number = %s",
                (phone,),
            )
            row = cur.fetchone()
    if row:
        return PhoneRecord(**row)
    raise HTTPException(status_code=404, detail="number not found")
