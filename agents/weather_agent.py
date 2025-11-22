import requests
from utils.geocode import geocode_city

def get_weather(city_name: str):
    geo = geocode_city(city_name)
    if geo is None:
        return None

    lat = geo["lat"]
    lon = geo["lon"]

    # Open-Meteo endpoint
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": "precipitation_probability"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        current_weather = data.get("current_weather", {})
        temperature = current_weather.get("temperature", "N/A")

        # Take first value from hourly probability list
        rain_prob_list = data.get("hourly", {}).get("precipitation_probability", [0])
        rain_prob = rain_prob_list[0] if rain_prob_list else 0

        best_time = "morning 🌅" if temperature < 32 else "evening 🌆"

        return {
            "city": geo["name"],
            "temperature": temperature,
            "rain_prob": rain_prob,
            "best_time": best_time
        }

    except:
        return None
