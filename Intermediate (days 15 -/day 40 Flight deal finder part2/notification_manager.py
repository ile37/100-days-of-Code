import smtplib
import os

FROM_EMAIL = "test@gmail.com"
APP_PASSWORD = os.environ.get("APP_PASSWORD")

class NotificationManager:
    #This class is responsible for sending notifications with deal flight details.
    def __init__(self, data_manager):

        self.users = data_manager.get_users_data()


    def send_emails(self, flights_data):
        for user in self.users:
            for flight in flights_data:
                message = f"Subject: Low price alert!\n\nOnly {flight['price']}€ to fly from 
                {flight['cityFrom']}-{flight['cityTo']}, on {flight['departureDate']}."
                print(message)
                # with smtplib.SMTP("smtp.gmail.com") as connection:
                #     connection.starttls()
                #     connection.login(user="