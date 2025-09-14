#!/usr/bin/env bash
set -e

python -m pip install -r requirements.txt
if [ ! -f .env ]; then
  cp .env.example .env
fi
