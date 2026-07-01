import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_KEY")

genai.configure(api_key=GEMINI_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

prompt = "Hey Google, how are you ?"

response = model.generate_content(prompt)

print(response.text)