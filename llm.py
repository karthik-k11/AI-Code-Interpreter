import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_llm_response(prompt: str, file_path: str = None) -> str:
    """
    Improved prompt for cleaner, minimal Python code
    """

    system_prompt = """
You are a Python code generator.

STRICT RULES:
- ONLY return Python code (no explanation, no markdown)
- DO NOT use input()
- DO NOT define unnecessary functions
- Write minimal, direct code
- Always print final result clearly

IF CSV:
- Use pandas
- Use given file_path variable (DO NOT hardcode path)
- Show:
  1. First few rows
  2. Summary statistics
"""

    if file_path:
        prompt = f"""
{prompt}

IMPORTANT:
Use variable 'file_path' (already provided).
DO NOT write file_path = '...'
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"