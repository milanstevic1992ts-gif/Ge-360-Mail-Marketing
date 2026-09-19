#!/usr/bin/env bash
set -euo pipefail

API_URL="${GE360_API_URL:-http://127.0.0.1:8789}"

echo "GE360 Mail Marketing doctor"
echo "==========================="

if ! command -v docker >/dev/null 2>&1; then
  echo "[FAIL] docker non trovato"
  exit 1
fi

if ! docker compose version >/dev/null 2>&1; then
  echo "[FAIL] docker compose plugin non trovato"
  exit 1
fi

echo "[OK] Docker"
docker compose ps

echo
if command -v curl >/dev/null 2>&1; then
  if curl -fsS "${API_URL}/api/health"; then
    echo
    echo "[OK] Core API"
  else
    echo
    echo "[FAIL] Core API non raggiungibile: ${API_URL}"
    exit 1
  fi
else
  echo "[WARN] curl non installato: salto test HTTP"
fi
