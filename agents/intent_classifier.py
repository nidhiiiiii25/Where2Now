def wants_weather(text: str) -> bool:
    text = text.lower()
    weather_keywords = ["weather", "temperature", "climate", "rain"]
    return any(word in text for word in weather_keywords)

def wants_places(text: str) -> bool:
    text = text.lower()
    place_keywords = ["places", "visit", "tour", "plan my trip", "go"]
    return any(word in text for word in place_keywords)
