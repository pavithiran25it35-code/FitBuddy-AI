# FitBuddy – AI Fitness Plan Generator

Complete FastAPI + SQLite + Gemini fitness planner.

## One-click Windows setup

1. Install Python 3.11+.
2. Extract this ZIP.
3. Open the extracted folder.
4. Double-click `run.bat`.
5. Open http://127.0.0.1:8000
6. Register first, then complete your fitness profile.
7. Click Generate 7-Day Plan.

For real Gemini generation, copy `.env.example` to `.env` and add your Gemini API key.
Without a key, the app still runs using a built-in demo planner.

## Manual start

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Then visit http://127.0.0.1:8000

## API
POST /api/register
POST /api/login
GET /api/me
POST /api/profile
POST /api/plan
POST /api/plan/regenerate
GET /api/plans
GET /api/health

Fitness plans are informational and do not replace professional medical advice.
