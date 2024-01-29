import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")


url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHAVANTAGE_API_KEY}"
r = requests.get(url)
data = r.json()["Time Series (Daily)"]

last_two_days_closing = []
for i, day in enumerate(data.items()):
    last_two_days_closing.append(float(day[1]["4. close"]))
    if i == 1:
        break

difference = last_two_days_closing[0] - last_two_days_closing[1]
percentage = (difference / last_two_days_closing[0]) * 100

if abs(percentage) >= 5:
    print("Get News")

    url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}"
    r = requests.get(url)
    data = r.json()["articles"][:3]

    for article in data:
        print("-----")
        print(article["title"])
        print(article["description"])
        print("-----")

#TODO: Send news articles to email / sms