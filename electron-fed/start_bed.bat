@echo off
cd server
call .venv\Scripts\activate

@REM python -m src.fastapi_bed.app
python -m uvicorn src.fastapi_bed.app:app --port 8866 --host 0.0.0.0
