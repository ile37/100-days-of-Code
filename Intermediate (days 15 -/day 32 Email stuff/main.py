import datetime as dt
import random
import smtplib

now = dt.datetime.now()
print(now.weekday())

if now.weekday() == 10:
    with open("quotes.txt") as data:
        quote = data.readlines()[random.randint(0, 101)]
        person = quote.split("-")[1].strip()
        quote = quote.split("-")[0].strip()

    message = f"Subject:From {person}\n\n{quote}"

    my_email = "your_email@gmil.com"
    app_password = "#################"

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(user=my_email, password=app_password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs="to_this_email", 
                            msg=message)
