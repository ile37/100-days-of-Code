import os
import requests
from twilio.rest import Client


TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


# Helsinki
LAT = 60.169857
LON = 24.938379

WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

# url = f"http://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}"
api_endpoint = "http://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": WEATHER_API_KEY,
    "cnt": 4,
}

response = requests.get(api_endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json().get("list")

for data in weather_data:
    if data.get("weather")[0].get("id") < 700:
        print("Bring an umbrella")
        twilio_client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = twilio_client.messages.create(
            body="It's going to rain today. Remember to bring an umbrella ☔",
            from_="#########",
            to="########",
        )
        print(message.status)
        break
