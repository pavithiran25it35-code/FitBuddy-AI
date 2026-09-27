import json
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Header
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from .database import get_db, init_db
from .auth import hash_password, verify_password, make_token, read_token
from .ai import generate_plan

load_dotenv()
init_db()
BASE = Path(__file__).resolve().parent.parent
app = FastAPI(title="FitBuddy API", version="1.0.0")

class RegisterIn(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    email: str
    password: str = Field(min_length=6, max_length=128)

class LoginIn(BaseModel):
    email: str
    password: str

class ProfileIn(BaseModel):
    age: int = Field(ge=13, le=100)
    gender: str = "Prefer not to say"
    height_cm: float = Field(gt=80, lt=250)
    weight_kg: float = Field(gt=25, lt=400)
    goal: str
    activity_level: str = "moderate"
    experience: str = "beginner"
    equipment: str = "bodyweight"
    dietary_preference: str = "balanced"
    workout_minutes: int = Field(default=30, ge=10, le=180)

class PlanIn(BaseModel):
    feedback: str = Field(default="", max_length=2000)

def current_user(authorization):
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(401, "Please log in.")
    uid = read_token(authorization.split(" ", 1)[1])
    if not uid:
        raise HTTPException(401, "Invalid session.")
    conn = get_db()
    row = conn.execute("SELECT id,name,email FROM users WHERE id=?", (uid,)).fetchone()
    conn.close()
    if not row:
        raise HTTPException(401, "User not found.")
    return dict(row)

def get_profile(uid):
    conn = get_db()
    row = conn.execute("SELECT * FROM profiles WHERE user_id=?", (uid,)).fetchone()
    conn.close()
    return dict(row) if row else None

@app.get("/")
def home():
    return FileResponse(BASE / "web" / "index.html")

@app.get("/app.js")
def js():
    return FileResponse(BASE / "web" / "app.js", media_type="application/javascript")

@app.get("/styles.css")
def css():
    return FileResponse(BASE / "web" / "styles.css", media_type="text/css")

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "FitBuddy"}

@app.post("/api/register")
def register(data: RegisterIn):
    email = data.email.strip().lower()
    conn = get_db()
    if conn.execute("SELECT id FROM users WHERE email=?", (email,)).fetchone():
        conn.close()
        raise HTTPException(400, "Email already registered.")
    cur = conn.execute(
        "INSERT INTO users(name,email,password_hash) VALUES(?,?,?)",
        (data.name.strip(), email, hash_password(data.password))
    )
    conn.commit()
    uid = cur.lastrowid
    conn.close()
    return {"token": make_token(uid), "user": {"id": uid, "name": data.name.strip(), "email": email}}

@app.post("/api/login")
def login(data: LoginIn):
    email = data.email.strip().lower()
    conn = get_db()
    row = conn.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
    conn.close()
    if not row or not verify_password(data.password, row["password_hash"]):
        raise HTTPException(401, "Incorrect email or password.")
    return {"token": make_token(row["id"]), "user": {"id": row["id"], "name": row["name"], "email": row["email"]}}

@app.get("/api/me")
def me(authorization: str | None = Header(default=None)):
    user = current_user(authorization)
    return {"user": user, "profile": get_profile(user["id"])}

@app.post("/api/profile")
def save_profile(data: ProfileIn, authorization: str | None = Header(default=None)):
    user = current_user(authorization)
    conn = get_db()
    conn.execute(
        '''INSERT INTO profiles
        (user_id,age,gender,height_cm,weight_kg,goal,activity_level,experience,equipment,dietary_preference,workout_minutes)
        VALUES(?,?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT(user_id) DO UPDATE SET
        age=excluded.age, gender=excluded.gender, height_cm=excluded.height_cm,
        weight_kg=excluded.weight_kg, goal=excluded.goal, activity_level=excluded.activity_level,
        experience=excluded.experience, equipment=excluded.equipment,
        dietary_preference=excluded.dietary_preference, workout_minutes=excluded.workout_minutes''',
        (user["id"], data.age, data.gender, data.height_cm, data.weight_kg, data.goal,
         data.activity_level, data.experience, data.equipment, data.dietary_preference, data.workout_minutes)
    )
    conn.commit()
    conn.close()
    return {"message": "Profile saved.", "profile": get_profile(user["id"])}

@app.post("/api/plan")
def create_plan(data: PlanIn, authorization: str | None = Header(default=None)):
    user = current_user(authorization)
    profile = get_profile(user["id"])
    if not profile:
        raise HTTPException(400, "Complete your fitness profile first.")
    plan, mode = generate_plan(profile, data.feedback)
    conn = get_db()
    conn.execute("INSERT INTO plans(user_id,plan_json,feedback) VALUES(?,?,?)",
                 (user["id"], json.dumps(plan), data.feedback))
    conn.commit()
    conn.close()
    return {"plan": plan, "mode": mode}

@app.post("/api/plan/regenerate")
def regenerate(data: PlanIn, authorization: str | None = Header(default=None)):
    return create_plan(data, authorization)

@app.get("/api/plans")
def plans(authorization: str | None = Header(default=None)):
    user = current_user(authorization)
    conn = get_db()
    rows = conn.execute(
        "SELECT id,plan_json,feedback,created_at FROM plans WHERE user_id=? ORDER BY id DESC LIMIT 10",
        (user["id"],)
    ).fetchall()
    conn.close()
    return {"plans": [{"id": r["id"], "plan": json.loads(r["plan_json"]), "feedback": r["feedback"], "created_at": r["created_at"]} for r in rows]}
