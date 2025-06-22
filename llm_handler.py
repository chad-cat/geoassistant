import os
from dotenv import load_dotenv

load_dotenv()

llm_provider = os.getenv("LLM_PROVIDER", "gemini").lower()

if llm_provider == "openai":
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")

elif llm_provider == "gemini":
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    gemini_text = genai.GenerativeModel("models/gemini-pro")
    gemini_vision = genai.GenerativeModel("models/gemini-pro-vision")

else:
    raise ValueError("Unsupported LLM_PROVIDER in .env file")


def ask_text_query(prompt):
    if llm_provider == "openai":
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"]

    elif llm_provider == "gemini":
        response = gemini_text.generate_content(prompt)
        return response.text


def ask_image_query(prompt, image):
    if llm_provider == "gemini":
        response = gemini_vision.generate_content([prompt, image])
        return response.text
    else:
        return " Image input only supported for Gemini right now."

