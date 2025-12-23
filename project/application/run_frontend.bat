@echo off
REM Frontend startup script for Windows
echo Starting GemmARIA Frontend...
cd /d %~dp0front
npm run dev
pause


