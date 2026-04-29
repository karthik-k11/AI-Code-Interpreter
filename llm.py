import os
from groq import Groq
from dotenv import load_dotenv

##Load env variables
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_llm_response(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that writes Python code."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"