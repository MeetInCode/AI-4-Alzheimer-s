#!/bin/bash
# Backend startup script for Linux/Mac
echo "Starting GemmARIA Backend..."
cd "$(dirname "$0")"
source venv/bin/activate
python -m uvicorn back.back:app --host 0.0.0.0 --port 8000 --reload


