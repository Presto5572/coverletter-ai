# ✔ All prompting now lives in a template
# ✔ Variables are passed cleanly
# ✔ No more giant strings in the Python file
# ✔ Easy to add tone modes, new templates, etc.

# --------------------------------------------
from openai import OpenAI # Import OpenAI client
from app.config import OPENAI_API_KEY # Ensure API key is imported from config
import os # Import os for file path handling
from app.prompts.utils import load_prompt, fill_template
# client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
client = OpenAI(api_key=OPENAI_API_KEY) # Initialize OpenAI client with API key

def generate_cover_letter(request): # Function to generate cover letter
    try:
        # 1. Load base template
        template = load_prompt("cover_letter_template.txt")

        # 2. Load tone-specific template
        tone_path = f"tone/{request.tone.lower()}.txt"
        tone_text = load_prompt(tone_path)

        # 3. Build variables dictionary
        variables = {
            "name": request.name,
            "role": request.role,
            "company": request.company,
            "experience": request.experience or "N/A",
            "skills": request.skills or "N/A",
            "tone": tone_text,
        }

        # 4. Merge variables into template
        prompt = fill_template(template, variables)

        # 5. Call OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # adjust if upgrading
            messages=[
                {"role": "system", "content": "You are an expert career writer specializing in professional cover letters."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,
            temperature=0.5
        )

        cover_letter = response.choices[0].message.content
        return cover_letter

    except Exception as e:
        return f"Error generating cover letter: {str(e)}"
