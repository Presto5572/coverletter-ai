from fastapi import FastAPI
from pydantic import BaseModel
from app.ai import generate_cover_letter
from app.models import CoverLetterRequest
from app.config import OPENAI_API_KEY

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# This tells FastAPI to allow requests from your React dev server.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# class CoverLetterRequest(BaseModel):
#     name: str
#     role: str
#     company: str
#     job_description: str
#     resume_highlights: str
#     tone: str = "corporate"  # default if none provided


@app.post("/generate-cover-letter")
def generate(request: CoverLetterRequest):
    cover_letter = generate_cover_letter(request)
    return {
        "status": "success",
        "cover_letter": cover_letter
    }

@app.get("/")
def read_root():
    return {"message": "Welcome to the Cover Letter AI API. Visit /docs for API documentation."}
