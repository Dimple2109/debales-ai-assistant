import os
from google import genai

# API key load
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def generate_answer(prompt):
    try:
        # available models fetch
        models = client.models.list()

        # allowed models list
        allowed = [
            "gemini-2.5-flash",
            "gemini-2.0-flash",
            "gemini-1.5-flash"
        ]

        selected_model = None

        # choose first available allowed model
        for m in models:
            name = m.name.replace("models/", "")
            if name in allowed:
                selected_model = m.name
                break

        # fallback (always safe)
        if not selected_model:
            selected_model = "models/gemini-1.5-flash"

        # generate response
        response = client.models.generate_content(
            model=selected_model,
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"