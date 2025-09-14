# hk-callshield-data-pipeline

A modular pipeline for collecting Hong Kong scam and nuisance phone numbers. The project:

- Scrapes official sources for suspicious phone numbers.
- Cleans and normalises records.
- Scores and publishes delta lists for downstream use.
- Exposes minimal FastAPI endpoints for query and download.
- Provides output formats for iOS (segmented lists) and Android (SQLite/JSONL).
- Uses GitHub Actions for scheduled runs and releases.

## Development

```bash
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Docker Compose

An example `docker-compose.yml` is provided to start both the API and a local Postgres database:

```bash
docker-compose up
```

The database is exposed on `localhost:5432` with the user, password and database name all set to `callshield`.
