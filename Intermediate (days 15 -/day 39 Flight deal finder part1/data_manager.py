import os
import requests

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEET_ENPONT = os.environ.get("SHEET_ENPONT")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}",
        }
        response = requests.get(url=SHEET_ENPONT, headers=headers)
        response.raise_for_status()

        self.destination_data = response.json()["prices"]

    def get_destination_data(self):
        return self.destination_data