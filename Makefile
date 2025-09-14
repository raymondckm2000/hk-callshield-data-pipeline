.PHONY: install run test lint

install:
python -m pip install -r requirements.txt

run:
uvicorn app.main:app --reload

test:
pytest
