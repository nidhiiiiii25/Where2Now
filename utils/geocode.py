import requests

def geocode_city(city_name: str):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city_name,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "Where2Now-App"  # Required or API rejects request
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        if len(data) == 0:
            return None  # Place not found

        return {
            "name": data[0].get("display_name"),
            "lat": float(data[0]["lat"]),
            "lon": float(data[0]["lon"])
        }

    except Exception as e:
        print("Geocoding error:", e)
        return None
