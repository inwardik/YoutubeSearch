import requests
import json

def get_coords(phone):
    url = "http://127.0.0.1:5000/api/v1/get_coord"
    payload = {
        'phone': phone
    }
    response = requests.get(url, params=payload)
    return json.loads(response.text)
