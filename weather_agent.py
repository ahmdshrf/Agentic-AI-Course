import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_KEY")

genai.configure(api_key=GEMINI_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# prompt = "Hey Google, how are you ?"

# response = model.generate_content(prompt)

# print(response.text)

def extract_city_from_user_question(user_question:str) ->str:
    prompt = f""" 
User said : "{user_question}"

Your job: exctract only the city name if only the user is asking weather.
if the user is asking weather of a country -> Return the capital city of this country with No punctuation, no extra text.
if not weather related OR city is not mentioned -> return none.
Return only a city name. No punctuation, no extra text
"""
    respone = model.generate_content(prompt)
    city = respone.text.strip()

    print(city)
    return city


user_message = input("User: ")

extract_city_from_user_question(user_message)