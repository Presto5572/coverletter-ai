from pydantic import BaseModel

# This defines what data your endpoint expects.

class CoverLetterRequest(BaseModel):
    name: str
    role: str
    company: str
    experience: str | None = ""
    skills: str | None = ""
    tone: str = "formal"  # default
