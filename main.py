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
    allow_origins=["*"],  # Restrict later if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# Root test
# --------------------
@app.get("/")
def root():
    return {"status": "AI Career Mentor backend running successfully"}

# --------------------
# Career Advice Endpoint (IMAGINE CUP VERSION)
# --------------------
@app.post("/api/career-advice")
def career_advice(data: CareerRequest):
    interest = data.interest
    level = data.education_level

    # --------------------
    # Short Chat-Friendly Summary (UI response)
    # --------------------
    summary = (
        f"You're a {level} interested in {interest}. "
        "Focus first on Python, DSA, Git/GitHub, and Azure fundamentals. "
        "Build 2–3 strong projects in Year 1, then move to AI, FastAPI, "
        "and Azure AI services in Year 2. I can share a detailed roadmap anytime."
    )

    # --------------------
    # Detailed Roadmap (Deep guidance)
    # --------------------
    detailed_roadmap = f"""
🎓 Personalized 2-Year Career Roadmap

📌 Your Profile
• Education Level: {level}
• Interest: {interest}

━━━━━━━━━━━━━━━━━━
📅 YEAR 1 – Foundations
━━━━━━━━━━━━━━━━━━
🔹 Skills
• Python (Core + OOP)
• Data Structures & Algorithms
• Git & GitHub
• Cloud Fundamentals (Azure)

🔹 Projects
• Resume Analyzer (Python)
• Student Management System
• Cloud-hosted Static Website (Azure)

━━━━━━━━━━━━━━━━━━
📅 YEAR 2 – Specialization
━━━━━━━━━━━━━━━━━━
🔹 Skills
• Machine Learning Basics
• AI APIs & Prompt Engineering
• FastAPI & Backend Development
• Azure AI Services

🔹 Projects
• AI Career Mentor (this MVP)
• AI-powered Chatbot
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
✔ Strong GitHub portfolio  
✔ Real-world AI & Cloud projects  
✔ Industry-recognized certifications  
✔ Internship & placement readiness
"""

    return {
        "summary": summary,
        "detailed": detailed_roadmap
    }
