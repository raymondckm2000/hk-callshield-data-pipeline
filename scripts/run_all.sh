#!/usr/bin/env bash
set -euo pipefail
source .venv/bin/activate || true
export $(grep -v '^#' .env | xargs)
make db
sleep 3
make schema || true
make all
make api
