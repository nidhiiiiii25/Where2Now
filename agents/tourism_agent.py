from .intent_classifier import wants_weather, wants_places
from .city_extractor import extract_city
from utils.geocode import geocode_city

from .places_agent import get_places

from .weather_agent import get_weather
from agents.places_agent import get_place_info, is_open_now


# Dummy fake data (will replace later with API results)
FAKE_WEATHER = "24°C with only 10% chance of rain ☀️"
FAKE_PLACES = [
    "Lalbagh Botanical Garden 🌸",
    "Cubbon Park 🌳",
    "Bangalore Palace 👑",
    "Bannerghatta National Park 🐅",
    "Visvesvaraya Science Museum 🧠"
]

def tourism_agent(user_input: str) -> str:
    city = extract_city(user_input)
    if not city:
        return "Hmm… I’m not sure which place that is 🤔\nTry mentioning a known city!"

    geo = geocode_city(city)
    if geo is None:
        return f"I tried finding **{city}**, but it doesn’t seem to exist on the map 😅"


    wants_w = wants_weather(user_input)
    wants_p = wants_places(user_input)

    response = f"**{city}? Awesome choice! Here’s your travel scoop 🌍👇**\n\n"

    if wants_w:
        weather = get_weather(city)
        if weather:
            response += (
                f"Weather rn: **{weather['temperature']}°C** 🌡️\n"
                f"Rain chance: **{weather['rain_prob']}%** 🌧️\n"
                f"Best vibe: **{weather['best_time']}** 😌\n\n"
            )
        else:
            response += "Couldn't fetch weather info rn 😅\n\n"


    if wants_p:
        places = get_places(city)
        if places:
            response += "**Spots worth checking:**\n"
            for p in places:
                emoji, desc = get_place_info(p["type"])
                status = is_open_now()
                response += (
                    f"- **{p['name']}** {emoji}\n"
                    f"  • {p['distance']} km away\n"
                    f"  • {desc}\n"
                    f"  • {status}\n\n"
                )
        else:
            response += "Couldn't fetch places right now 😅\n\n"


    if not wants_w and not wants_p:
        response += "Tell me if you want weather ☁️ or places to visit 🏛️!"

    return response
