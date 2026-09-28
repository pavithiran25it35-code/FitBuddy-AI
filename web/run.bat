@echo off
title FitBuddy AI
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Creating Python virtual environment...
  py -m venv .venv
  if errorlevel 1 (
    echo Python was not found. Install Python 3.11+ and enable Add Python to PATH.
    pause
    exit /b 1
  )
)
echo Installing dependencies...
.venv\Scripts\python.exe -m pip install -r requirements.txt
echo Starting FitBuddy...
start "" http://127.0.0.1:8000
.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000
pause
