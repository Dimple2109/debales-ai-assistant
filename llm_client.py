from google import genai
from config import GOOGLE_KEY

client = genai.Client(api_key=GOOGLE_KEY)

def generate_answer(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text