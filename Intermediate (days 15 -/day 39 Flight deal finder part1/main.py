#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager as dm
import flight_search as fs


data_manager = dm.DataManager()

destination_data = data_manager.get_destination_data()

flight_search = fs.FlightSearch(destination_data)

# TODO: send information via email or sms to the user
for flight in flight_search.get_flights_data():
    print(flight)