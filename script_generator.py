import openai
import os

openai.api_key = os.getenv("API_KEY")

def generate_script():
    prompt = """
    Create a 10-second emotional AI animated YouTube short script.
    Format:
    1. Hook line
    2. Scene description
    3. Character action
    4. Twist ending
    Also give title + hashtags.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"]
