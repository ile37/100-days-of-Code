import os
import requests

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEET_ENPONT = os.environ.get("SHEET_ENPONT")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}",
        }
        response_prices = requests.get(url=f"{SHEET_ENPONT}/prices", headers=self.headers)
        response_prices.raise_for_status()

        response_users = requests.get(url=f"{SHEET_ENPONT}/users", headers=self.headers)
        response_users.raise_for_status()

        self.destination_data = response_prices.json()["prices"]
        self.users_data = response_users.json()["users"]

    def get_destination_data(self):
        return self.destination_data
    
    def get_users_data(self):
        return self.users_data
    
    def add_user(self, name, email):

        json = {
            "user": {
                "name": name,
                "email": email
            }
        }

        response = requests.post(url=f"{SHEET_ENPONT}/users", json=json, headers=self.headers)
        response.raise_for_status()

        response_users = requests.get(url=f"{SHEET_ENPONT}/users", headers=self.headers)
        response_users.raise_for_status()

        self.users_data = response_users.json()["users"]