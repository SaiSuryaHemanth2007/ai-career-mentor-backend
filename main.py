from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils import CareerRequest, analyze_career

# Create FastAPI app
app = FastAPI(
    title="AI Career Mentor API",
    description="Backend API for Imagine Cup AI Career Mentor MVP",
    version="1.0.0"
)

# Enable CORS (for frontend connection later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "AI Career Mentor Backend is running",
        "status": "success"
    }

# Health check endpoint
@app.get("/health")
def health():
    return {"health": "ok"}

# Main career analysis endpoint
@app.post("/api/career-advice")
def career_advice(request: CareerRequest):
    """
    Accepts user interest + background and returns AI-based career advice
    """
    result = analyze_career(request)
    return result
