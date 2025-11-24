import os
import openai

openai.api_key = os.getenv("API_KEY")

def generate_animation(script_text):
    prompt = f"""
    Convert this script into a 10-second short AI animation description:
    {script_text}

    Output format:
    1. Scene visuals
    2. Camera movement
    3. Character actions
    4. Background style
    5. Lighting
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"]
