import os
import requests
import time

KIWI_API_KEY = os.environ.get("KIWI_API_KEY")
KIWI_ENPOINT = "https://api.tequila.kiwi.com/v2/search"

DEPARTURE_CITY_IATA = "LON"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, destination_data):

        self.flights_data = []

        kiwi_headers = {
            "apikey": KIWI_API_KEY,
        }
        date_from = time.strftime("%d/%m/%Y")
        # searches flights from now to 30 days from now
        date_to = time.strftime("%d/%m/%Y", time.localtime(time.time() + 86400 * 30))


        for destination in destination_data:

            kiwi_body = {
                "fly_from": DEPARTURE_CITY_IATA,
                "fly_to": destination["iataCode"],
                "date_from": date_from,
                "date_to": date_to,
                "one_for_city": "1",
                "one_per_date": "1",
                "price_to": int(destination["lowestPrice"]),
                "curr": "EUR",
            }
            response = requests.get(url=KIWI_ENPOINT, headers=kiwi_headers, params=kiwi_body)
            response.raise_for_status()

            for flight in response.json()["data"]:
                flight_dict = {
                    "price": flight["price"],
                    "cityFrom": flight["cityFrom"],
                    "cityTo": flight["cityTo"],
                    "departureDate": flight["route"][0]["local_departure"].split("T")[0],
                }
                self.flights_data.append(flight_dict)

    def get_flights_data(self):
        return self.flights_data


        