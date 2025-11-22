import requests
import math
from utils.geocode import geocode_city
from datetime import datetime

def is_open_now():
    hour = datetime.now().hour
    if 9 <= hour <= 19:
        return "🟢 Open now"
    return "🔴 Probably closed now"


# Map place types to emoji + description
TYPE_INFO = {
    "park": ("🌳", "Green space & chill vibes"),
    "museum": ("🏛️", "Learn and explore"),
    "historic": ("🏰", "Cultural & heritage spot"),
    "temple": ("🕍", "Peaceful spiritual spot"),
    "attraction": ("📍", "Tourist hotspot"),
}

def get_place_info(place_type: str):
    for key in TYPE_INFO:
        if key in place_type:
            return TYPE_INFO[key]
    return ("📍", "Popular spot")


# Simple function to calculate distance between two GPS points (Haversine formula)
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in KM
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = (math.sin(dlat/2)**2 
         + math.cos(math.radians(lat1)) 
         * math.cos(math.radians(lat2)) 
         * math.sin(dlon/2)**2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 1)


def get_places(city_name: str):
    geo = geocode_city(city_name)
    if geo is None:
        return None

    lat = geo["lat"]
    lon = geo["lon"]

    query = f"""
    [out:json][timeout:25];
    (
      node(around:10000,{lat},{lon})["tourism"];
      node(around:10000,{lat},{lon})["historic"];
      node(around:10000,{lat},{lon})["amenity"="museum"];
      node(around:10000,{lat},{lon})["leisure"="park"];
    );
    out center;
    """


    try:
        response = requests.post("https://overpass-api.de/api/interpreter", data=query)
        data = response.json()

        places = []
        for element in data.get("elements", []):
            name = element.get("tags", {}).get("name")
            if not name: 
                continue  # skip unnamed places

            # type of place (park, museum, temple etc.)
            tags = element.get("tags", {})
            place_type = tags.get("tourism", "")

            place_lat = element.get("lat")
            place_lon = element.get("lon")

            distance = calculate_distance(lat, lon, place_lat, place_lon)

            places.append({
                "name": name,
                "distance": distance,
                "type": place_type
            })

            if len(places) >= 5:
                break
        places = sorted(places, key=lambda x: x["distance"])
        places = places[:5]

        return places

    except Exception as e:
        print("Places API Error:", e)
        return None
