#!/bin/bash
# Start the server

echo "Starting server..."

.venv/bin/python -m src.fastapi_bed.app
