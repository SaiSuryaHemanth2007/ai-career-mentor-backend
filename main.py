from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re

# --------------------------------------------------
# FastAPI App
# --------------------------------------------------
app = FastAPI(
    title="AI Career Mentor API",
    description="Backend API for AI Career Mentor",
    version="4.0.0",
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
# Input Cleanup & Normalization Layer
# (Honest, deterministic, production-safe)
# --------------------------------------------------
COMMON_FIXES = {
    "dipolma": "Diploma",
    "btech": "BTech",
    "cybersecutiy": "Cybersecurity",
    "cybersectutiiiy": "Cybersecurity",
    "ai and cloud": "AI and Cloud Computing",
    "cloud ai": "AI and Cloud Computing",
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
        "ai_provider": "rule-based (AI-ready)",
        "version": "4.0.0",
    }

# --------------------------------------------------
# Roadmap Generator (FINAL LOGIC)
# --------------------------------------------------
def generate_roadmap(interest: str, level: str, duration: int = 2):
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
• Career Interest: {interest}

━━━━━━━━━━━━━━━━━━
📅 Year 1 – Foundations
━━━━━━━━━━━━━━━━━━
• Core fundamentals of {interest}
• Python programming basics
• Data Structures & Algorithms
• Git & GitHub
• Cloud fundamentals
• Mini projects and hands-on practice

━━━━━━━━━━━━━━━━━━
📅 Year 2 – Specialization
━━━━━━━━━━━━━━━━━━
• Advanced {interest} concepts
• Backend development using FastAPI
• Cloud deployment and services
• End-to-end capstone project
• Real-world problem solving

━━━━━━━━━━━━━━━━━━
🎯 Outcomes
━━━━━━━━━━━━━━━━━━
• Industry-ready skills
• Strong GitHub portfolio
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

    summary, detailed = generate_roadmap(
        interest=interest,
        level=level,
        duration=2
    )

    return {
        "summary": summary,
        "detailed": detailed,
        "ai_provider": "fallback (Azure OpenAI ready)",
    }
