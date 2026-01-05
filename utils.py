from pydantic import BaseModel
from typing import List

class CareerRequest(BaseModel):
    skills: List[str]
    interests: List[str]
    education: str

def analyze_career(data: CareerRequest):
    return {
        "recommended_role": "AI Engineer",
        "next_steps": [
            "Learn Machine Learning",
            "Build AI projects",
            "Practice DSA",
            "Apply for internships"
        ],
        "based_on": data
    }
