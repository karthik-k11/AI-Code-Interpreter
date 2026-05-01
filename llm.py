import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_llm_response(prompt: str, file_path: str = None) -> str:

    system_prompt = """
You are a Python code generator.

Rules:
- Only generate Python code
- If a CSV file is mentioned, use pandas to read it
- Always print output
"""

    if file_path:
        prompt = f"{prompt}\nThe file path is: {file_path}"

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"