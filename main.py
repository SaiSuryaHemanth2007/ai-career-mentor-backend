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
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# Root health check
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

    summary = f"""
🎓 2-Year AI + Cloud Career Roadmap

Focus on Python, Azure Cloud, Machine Learning basics,
real-world projects, and certifications for strong placements.
"""

    detailed = f"""
🎓 Personalized 2-Year Career Roadmap

📌 Your Profile
• Education Level: {level}
• Interest: {interest}

━━━━━━━━━━━━━━━━━━
📅 YEAR 1 — Foundations
━━━━━━━━━━━━━━━━━━
🔹 Skills
• Python (core + OOP)
• Data Structures & Algorithms
• Git & GitHub
• Cloud Fundamentals (Azure)

🔹 Projects
• Resume Analyzer (Python)
• Student Management System
• Cloud-hosted Static Website

━━━━━━━━━━━━━━━━━━
📅 YEAR 2 — Specialization
━━━━━━━━━━━━━━━━━━
🔹 Skills
• Machine Learning Basics
• AI APIs & Prompt Engineering
• FastAPI & Backend Development
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
• (Optional) Google ML Crash Course

━━━━━━━━━━━━━━━━━━
🎯 Final Outcome
━━━━━━━━━━━━━━━━━━
✔ Real-world AI + Cloud projects  
✔ Strong GitHub portfolio  
✔ Industry-recognized certifications  
✔ Internship & placement readiness
"""

    return {
    "summary": f"""2-Year AI + Cloud Career Roadmap

Focus on Python, Azure Cloud, Machine Learning basics,
real-world projects, and certifications for strong placements.""",

    "detailed": advice
}

