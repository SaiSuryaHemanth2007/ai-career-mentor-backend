from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import re

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------
load_dotenv()

# --------------------------------------------------
# FastAPI App
# --------------------------------------------------
app = FastAPI(
    title="AI Career Mentor API",
    description="Backend API for AI Career Mentor",
    version="3.3.0",
)

# --------------------------------------------------
# CORS
# --------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Request Model
# --------------------------------------------------
class CareerRequest(BaseModel):
    interest: str
    education_level: str

# --------------------------------------------------
# Input Cleanup Layer (SPELL FIX)
# --------------------------------------------------
COMMON_FIXES = {
    "dipolma": "Diploma",
    "btech": "BTech",
    "cybersecutiy": "Cybersecurity",
    "cyber security": "Cybersecurity",
}

def clean_text(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"\s+", " ", text)
    return COMMON_FIXES.get(text, text.title())

# --------------------------------------------------
# Health Check
# --------------------------------------------------
@app.get("/")
def health_check():
    return {
        "status": "AI Career Mentor backend running",
        "ai_provider": "fallback",
        "version": "3.3.0",
    }

# --------------------------------------------------
# Dynamic Fallback Generator (CLEAN OUTPUT)
# --------------------------------------------------
def generate_fallback(interest: str, level: str, duration: int = 2):
    summary = (
        f"This is a {duration}-year structured career roadmap designed for a "
        f"{level} student aiming to build strong fundamentals and job-ready skills "
        f"in {interest}."
    )

    title = f"📘 {duration}-Year {interest} Career Roadmap"

    detailed = f"""
{title}

🎓 Profile
• Education Level: {level}
• Interest: {interest}

━━━━━━━━━━━━━━━━━━
📅 Year 1 – Foundations
━━━━━━━━━━━━━━━━━━
• Core fundamentals of {interest}
• Python programming
• Data Structures & Algorithms
• Git & GitHub
• Cloud fundamentals

━━━━━━━━━━━━━━━━━━
📅 Year 2 – Specialization
━━━━━━━━━━━━━━━━━━
• Advanced {interest} concepts
• Backend development (FastAPI)
• Cloud deployment
• Capstone project

━━━━━━━━━━━━━━━━━━
🎯 Outcomes
━━━━━━━━━━━━━━━━━━
• Strong portfolio
• Industry-ready skills
• Internship & placement readiness
""".strip()

    return summary, detailed

# --------------------------------------------------
# Career Advice API
# --------------------------------------------------
@app.post("/api/career-advice")
def career_advice(data: CareerRequest):
    interest = clean_text(data.interest)
    level = clean_text(data.education_level)

    summary, detailed = generate_fallback(
        interest,
        level,
        duration=2
    )

    return {
        "summary": summary,
        "detailed": detailed,
        "ai_provider": "fallback",
    }
