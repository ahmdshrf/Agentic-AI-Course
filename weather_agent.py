import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_KEY")
OWM_KEY = os.getenv("OWM_KEY")

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


def fetch_weather_from_openweathermap(city: str) :
    """
    Fetch weather data from OpenWeatherMap API for a given city.
    
    Args:
        city (str): City name
        
    Returns:
        dict: Weather data including temperature, description, humidity, etc.
    """
    if not OWM_KEY:
        return {"error": "OWM_KEY not found in environment variables"}
    
    url = f"https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": OWM_KEY,
        "units": "metric"  # Use Celsius, change to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        
        weather_data = response.json()
        
        # Extract relevant information
        return {
            "city": weather_data.get("name"),
            "country": weather_data.get("sys", {}).get("country"),
            "temperature": weather_data.get("main", {}).get("temp"),
            "feels_like": weather_data.get("main", {}).get("feels_like"),
            "temp_min": weather_data.get("main", {}).get("temp_min"),
            "temp_max": weather_data.get("main", {}).get("temp_max"),
            "humidity": weather_data.get("main", {}).get("humidity"),
            "pressure": weather_data.get("main", {}).get("pressure"),
            "description": weather_data.get("weather", [{}])[0].get("description"),
            "wind_speed": weather_data.get("wind", {}).get("speed"),
            "cloudiness": weather_data.get("clouds", {}).get("all"),
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch weather data: {str(e)}"}
    except ValueError:
        return {"error": "Invalid response from OpenWeatherMap API"}


user_message = input("User: ")

city = extract_city_from_user_question(user_message)

if city and city.lower() != "none":
    print(f"\nFetching weather for {city}...")
    weather = fetch_weather_from_openweathermap(city)
    
    if "error" not in weather:
        print(f"\n📍 Location: {weather['city']}, {weather['country']}")
        print(f"🌡️ Temperature: {weather['temperature']}°C (feels like {weather['feels_like']}°C)")
        print(f"📊 Min/Max: {weather['temp_min']}°C / {weather['temp_max']}°C")
        print(f"💧 Humidity: {weather['humidity']}%")
        print(f"💨 Wind Speed: {weather['wind_speed']} m/s")
        print(f"☁️ Cloudiness: {weather['cloudiness']}%")
        print(f"📝 Description: {weather['description'].capitalize()}")
    else:
        print(f"❌ {weather['error']}")
else:
    print("❌ Could not extract a city name or it's not weather-related")