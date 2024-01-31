import requests
import time
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

SHEET_ENPONT = os.environ.get("SHEET_ENPONT")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

parameters = {
    "query": input("Tell me which exercises you did: "),
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()

# add row to sheet
headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
}

data_body = {
    "workout": {
        "date": time.strftime("%x"),
        "time": time.strftime("%X"),
        "exercise": response.json()["exercises"][0]["name"].title(),
        "duration": response.json()["exercises"][0]["duration_min"],
        "calories": response.json()["exercises"][0]["nf_calories"],
    }
}

add_response = requests.post(url=SHEET_ENPONT, json=data_body, headers=headers)
add_response.raise_for_status()

print(data_body)
print("added to sheet successfully!")