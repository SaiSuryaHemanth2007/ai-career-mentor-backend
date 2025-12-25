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
# CORS
# --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# Health Check
# --------------------
@app.get("/")
def root():
    return {
        "status": "AI Career Mentor backend running",
        "version": "1.0.0"
    }

# --------------------
# Career Advice Endpoint
# --------------------
@app.post("/api/career-advice")
def career_advice(data: CareerRequest):
    interest = data.interest
    level = data.education_level

    # ✅ SUMMARY (NO EMOJIS – PROFESSIONAL)
    summary = f"""
2-Year AI and Cloud Career Roadmap

This roadmap is designed for a {level.lower()} interested in {interest.lower()}.
It focuses on building strong programming fundamentals, cloud expertise,
applied machine learning skills, and real-world project experience to prepare
for internships and full-time roles.
""".strip()

    # ✅ DETAILED ROADMAP (EMOJIS ONLY HERE)
    detailed = f"""
🎓 Personalized 2-Year Career Roadmap

📌 Profile
• Education Level: {level}
• Interest: {interest}

━━━━━━━━━━━━━━━━━━
📅 Year 1 – Foundations
━━━━━━━━━━━━━━━━━━
🔹 Skills
• Python (core and object-oriented programming)
• Data Structures and Algorithms
• Git and GitHub
• Cloud Fundamentals (Azure)

🔹 Projects
• Resume Analyzer (Python)
• Student Management System
• Cloud-hosted Static Website

━━━━━━━━━━━━━━━━━━
📅 Year 2 – Specialization
━━━━━━━━━━━━━━━━━━
🔹 Skills
• Machine Learning Basics
• AI APIs and Prompt Engineering
• FastAPI and Backend Development
• Azure AI Services

🔹 Projects
• AI Career Mentor (this project)
• AI Chatbot using APIs
• Cloud-based AI Application

━━━━━━━━━━━━━━━━━━
🎓 Certifications
━━━━━━━━━━━━━━━━━━
• Microsoft Azure AI Fundamentals
• Microsoft Azure Developer Associate
• Optional: Google Machine Learning Crash Course

━━━━━━━━━━━━━━━━━━
🎯 Outcome
━━━━━━━━━━━━━━━━━━
• Real-world AI and cloud projects
• Strong GitHub portfolio
• Internship and placement readiness
""".strip()

    return {
        "summary": summary,
        "detailed": detailed
    }
