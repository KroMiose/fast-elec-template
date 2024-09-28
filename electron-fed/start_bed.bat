@echo off
cd server
call .venv\Scripts\activate
python -m src.fastapi_bed.app
