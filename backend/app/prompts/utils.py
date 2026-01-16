import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def load_prompt(filename: str) -> str:
    """
    Loads a prompt file from /app/prompts.
    """
    filepath = os.path.join(BASE_PATH, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Prompt file not found: {filepath}")

    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def fill_template(template: str, variables: dict) -> str:
    """
    Replaces {{variable}} placeholders with actual values.
    """
    for key, value in variables.items():
        template = template.replace(f"{{{{{key}}}}}", value)
    return template
