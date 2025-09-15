.PHONY: dev db schema run api etl publish all

dev:
	python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

db:
	docker compose up -d db

schema:
	psql $$DATABASE_URL -f app/schema.sql

run: api

api:
	uvicorn app.main:app --host $${API_HOST:-0.0.0.0} --port $${API_PORT:-8080}

etl:
	python -m app.etl.pipeline

publish:
	python -m app.etl.publisher

all: etl publish
