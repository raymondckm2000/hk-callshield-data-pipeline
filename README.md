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
