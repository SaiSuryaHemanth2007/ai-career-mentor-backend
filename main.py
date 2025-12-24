from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# --------------------
# Request Model
# --------------------
class CareerRequest(BaseModel):
    interest: str
    education_level: str

# --------------------
# FastAPI App
# --------------------
app = FastAPI(
    title="AI Career Mentor API",
    description="Backend API for Imagine Cup AI Career Mentor MVP",
    version="1.0.0"
)

# --------------------
# CORS (allow frontend)
# --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later you can restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# Root test
# --------------------
@app.get("/")
def root():
    return {"status": "AI Career Mentor backend running"}

# --------------------
# Career Advice Endpoint
# --------------------
@app.post("/api/career-advice")
def career_advice(request: CareerRequest):
    interest = request.interest
    education = request.education_level

    advice = (
        f"Based on your interest in {interest} and your education level "
        f"as a {education}, focus on Python, cloud fundamentals, "
        f"machine learning basics, and building real-world projects."
    )

    return {"advice": advice}
