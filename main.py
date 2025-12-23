from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils import CareerRequest, analyze_career

app = FastAPI(
    title="AI Career Mentor API",
    description="Backend API for Imagine Cup AI Career Mentor MVP",
    version="1.0.0"
)

# Enable CORS (for frontend later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "AI Career Mentor API is running 🚀"
    }

# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

# Career analysis endpoint
@app.post("/analyze-career")
async def analyze(data: CareerRequest):
    result = analyze_career(data)
    return result
import os

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )
