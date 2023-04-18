import requests, json
import time

def get_lat_lon(locations):
    PATH = "https://us1.locationiq.com/v1/search.php"
    LOCATIONIQ_API_KEY = "pk.4761b1257d9b016dd5034da988fa4aeb"
    coordinates = {}
    for location in locations:
        query_params = {
            "key": LOCATIONIQ_API_KEY,
            "q": location,
            "format": "json"
        }
        time.sleep(.25)
        response = requests.get(PATH, params=query_params)
        time.sleep(.25)
        print(f"***RESPONSE FOR {location.upper()}***", json.dumps(response.json(), indent=4, sort_keys=True))
        body = response.json()[0]
        location_coords = {
            "latitude": body["lat"],
            "longitude": body["lon"]
        }
        coordinates[location] = location_coords
    return coordinates


wonders = ["Great Wall of China", "Petra", "Colosseum", "Chichen Itza", "Machu Picchu", "Taj Mahal", "Christ the Redeemer"]

print(get_lat_lon(wonders))

# print(get_lat_lon(["Christ the Redeemer"]))