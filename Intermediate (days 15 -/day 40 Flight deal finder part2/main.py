import data_manager as dm
import flight_search as fs
import notification_manager as nm

print("Welcome to the Flight Club. We find the best flight deals and email you")
username = input("What is your name? ")
email = input("What is your email? ")

data_manager = dm.DataManager()

if username != "" or email != "":
    data_manager.add_user(username, email)
    print("username and email added to the database")
    print("Thank you! You will now get the best flight deals to your email")

destination_data = data_manager.get_destination_data()

flight_search = fs.FlightSearch(destination_data)
notifications = nm.NotificationManager(data_manager=data_manager)

flights_data = flight_search.get_flights_data()
notifications.send_emails(flights_data)

print(f"{len(flights_data)} fligths send to registered emails.")
    