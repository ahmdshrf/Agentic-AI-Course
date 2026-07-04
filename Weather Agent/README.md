# Agentic AI Course

This repository contains code and materials for the course:
**Building Autonomous Agentic Systems**

Course Link: https://learning.oreilly.com/course/building-autonomous-agentic/9781807609818/

---

## 🌤️ Weather Agent

An intelligent weather agent that combines **Google Gemini AI** with the **OpenWeatherMap API** to provide natural language weather queries.

### Features

- 🤖 **Natural Language Processing**: Uses Google Gemini 2.5 Flash to understand weather queries and extract city names
- 🌍 **Smart Location Detection**: Extracts city names from user questions, even when asking about countries (returns capital cities)
- 🌡️ **Real-time Weather Data**: Fetches current weather from OpenWeatherMap
- 📊 **Comprehensive Data**: Temperature, humidity, wind speed, pressure, cloudiness, and more
- ✨ **Beautiful Output**: Formatted console output with emoji indicators

### Prerequisites

- Python 3.8+
- `requests` library
- `python-dotenv` library
- `google-generativeai` library

### Installation

1. Install required dependencies:
```bash
pip install requests python-dotenv google-generativeai
```

2. Create a `.env` file in the project root with your API keys:
```
GEMINI_KEY=your_google_gemini_api_key
OWM_KEY=your_openweathermap_api_key
```

### Getting API Keys

- **Google Gemini API**: Get a free API key from [Google AI Studio](https://aistudio.google.com/)
- **OpenWeatherMap API**: Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)

### Usage

Run the script:
```bash
python weather_agent.py
```

Example queries:
- "What's the weather in London?"
- "How's the weather in France?" (returns capital city: Paris)
- "Tell me the weather for Tokyo"

### Output Example

```
User: What's the weather in New York?

Fetching weather for New York...

📍 Location: New York, US
🌡️ Temperature: 22.5°C (feels like 21.8°C)
📊 Min/Max: 20.1°C / 24.3°C
💧 Humidity: 65%
💨 Wind Speed: 5.2 m/s
☁️ Cloudiness: 40%
📝 Description: Partly cloudy
```

### Functions

#### `extract_city_from_user_question(user_question: str) -> str`
Extracts city name from natural language user input using Gemini AI.

- **Parameters**: `user_question` - The user's weather-related question
- **Returns**: City name or "none" if not weather-related

#### `fetch_weather_from_openweathermap(city: str) -> dict`
Fetches weather data from OpenWeatherMap API.

- **Parameters**: `city` - City name to fetch weather for
- **Returns**: Dictionary containing:
  - `city`: City name
  - `country`: Country code
  - `temperature`: Current temperature (°C)
  - `feels_like`: Feels-like temperature
  - `temp_min/max`: Min/max temperatures
  - `humidity`: Humidity percentage
  - `pressure`: Atmospheric pressure
  - `description`: Weather description
  - `wind_speed`: Wind speed (m/s)
  - `cloudiness`: Cloud coverage percentage

### Configuration

To change temperature unit from Celsius to Fahrenheit, modify the `units` parameter in `fetch_weather_from_openweathermap()`:
```python
params = {
    "q": city,
    "appid": OWM_KEY,
    "units": "imperial"  # Use "imperial" for Fahrenheit
}
```

### Error Handling

The agent gracefully handles:
- Missing or invalid API keys
- Network errors
- Invalid city names
- Non-weather related queries
