import os
import openai

openai.api_key = os.getenv("API_KEY")

def generate_voice(script_text):
    prompt = f"Convert this script into a natural sounding YouTube short voiceover: {script_text}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    # normally here you'd call a TTS model
    return response.choices[0].message["content"]
