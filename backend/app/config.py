import os
from dotenv import load_dotenv

load_dotenv()  # loads .env from backend/

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
