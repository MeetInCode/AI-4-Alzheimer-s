@echo off
REM Backend startup script for Windows
echo Starting GemmARIA Backend...
cd /d %~dp0
call venv\Scripts\activate.bat
python -m uvicorn back.back:app --host 0.0.0.0 --port 8000 --reload
pause


