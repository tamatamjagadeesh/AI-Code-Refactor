import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=api_key)

# Use stable model
model = genai.GenerativeModel("gemini-2.5-flash-lite")

def refactor_code(code):
    prompt = f"""
Refactor the following Python code to improve readability.
Do NOT change the functionality.
Avoid nested if statements if possible.

Code:
{code}
"""
    response = model.generate_content(prompt)
    cleaned = clean_code_output(response.text)
    return cleaned

def clean_code_output(text):
    if text.startswith("```"):
        lines = text.splitlines()
        lines = [line for line in lines if not line.startswith("```")]
        return "\n".join(lines)
    return text