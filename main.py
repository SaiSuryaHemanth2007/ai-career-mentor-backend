from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

<<<<<<< HEAD
from utils import CareerRequest, analyze_career

# Create FastAPI app
=======
>>>>>>> 7efecce (Clean requirements and stabilize backend)
app = FastAPI(
    title="AI Career Mentor API",
    description="Backend API for Imagine Cup AI Career Mentor MVP",
    version="1.0.0"
)

<<<<<<< HEAD
# Enable CORS (for frontend connection later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for now
=======
# ✅ Allow frontend (Azure Static Web Apps)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # OK for MVP / demo
>>>>>>> 7efecce (Clean requirements and stabilize backend)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ REQUEST MODEL — MUST MATCH FRONTEND
class CareerRequest(BaseModel):
    interest: str
    education_level: str


@app.get("/")
def root():
<<<<<<< HEAD
    return {
        "message": "AI Career Mentor Backend is running",
        "status": "success"
    }
=======
    return {"status": "AI Career Mentor Backend Running"}

>>>>>>> 7efecce (Clean requirements and stabilize backend)

@app.get("/health")
def health():
<<<<<<< HEAD
    return {"health": "ok"}

# Main career analysis endpoint
@app.post("/api/career-advice")
def career_advice(request: CareerRequest):
    """
    Accepts user interest + background and returns AI-based career advice
    """
    result = analyze_career(request)
    return result
=======
    return {"status": "healthy"}


@app.post("/api/career-advice")
def career_advice(req: CareerRequest):
    advice = f"""
You are a {req.education_level} interested in {req.interest}.

🎯 Suggested Career Roadmap:

1️⃣ Strengthen Python fundamentals  
2️⃣ Learn Data Structures & Algorithms  
3️⃣ Understand Machine Learning basics  
4️⃣ Explore Cloud Computing (Azure / AWS)  
5️⃣ Build real-world AI + Cloud projects  
6️⃣ Participate in hackathons like Imagine Cup  
7️⃣ Create a strong GitHub & LinkedIn profile  

🚀 You are on the right path — keep building consistently!
"""

    return {
        "advice": advice.strip()
    }
>>>>>>> 7efecce (Clean requirements and stabilize backend)
