import requests

path = "https://us1.locationiq.com/v1/search.php"

LOCATIONIQ_API_KEY = "pk.4761b1257d9b016dd5034da988fa4aeb"

query_params = {
    "key": LOCATIONIQ_API_KEY,
    "q": "Great Wall of China",
    "format": "json"
}

response = requests.get(path, params=query_params)

print("The value of response is", response)
print("The value of response.text, which contains a text description of the request, is", response.text)