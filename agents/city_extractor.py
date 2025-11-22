# TEMPORARY SIMPLE VERSION
# Later we will replace this with Nominatim API result

CITIES = [
    "bangalore", "bengaluru",
    "mysore", "mumbai", "delhi",
    "hyderabad", "chennai", "kolkata",
    "pune", "jaipur", "goa",
    "ahmedabad", "kochi", "coimbatore"
]

def extract_city(text: str) -> str | None:
    text = text.lower()
    for city in CITIES:
        if city in text:
            return city.capitalize()
    return None
