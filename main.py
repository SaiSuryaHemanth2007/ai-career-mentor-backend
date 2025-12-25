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
    interest_lower = interest.lower()

    # --------------------
    # SUMMARY (NO EMOJIS)
    # --------------------
    if "project" in interest_lower:
        summary = """
Building strong, resume-ready projects is essential for demonstrating
practical AI and Cloud skills. Focus on end-to-end applications that
showcase problem-solving, backend development, and cloud deployment.
""".strip()

    elif "certification" in interest_lower:
        summary = """
Professional certifications help validate your AI and Cloud knowledge.
Start with foundational certifications and gradually move to role-based
certifications to strengthen your placement readiness.
""".strip()

    elif "internship" in interest_lower:
        summary = """
Securing AI and Cloud internships requires hands-on projects, a strong
GitHub profile, and basic cloud deployment experience. Practical skills
and consistent applications are key to success.
""".strip()

    else:
        summary = f"""
2-Year AI and Cloud Career Roadmap

This roadmap is designed for a {level.lower()} interested in {interest_lower}.
It focuses on strong programming fundamentals, cloud expertise, applied
machine learning skills, and real-world project experience.
""".strip()

    # --------------------
    # DETAILED ROADMAP (EMOJIS ONLY HERE)
    # --------------------
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
