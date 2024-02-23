import requests
from bs4 import BeautifulSoup
import smtplib
import os


TRESHOLD_PRICE = 59.99
USER_AGENT =  "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0" # os.environ.get('USER_AGENT')

# bech power supply
product_to_track_url = "https://www.amazon.com/Jesverty-Adjustable-Switching-Encoder-Knob/dp/B0CBM2D3DW/ref=sr_1_9?crid=3QHAIEOCTU0MV&dib=eyJ2IjoiMSJ9.RCZpnlCWNZMdqXloK16JBXOAciqmPWoggW9lWB86wNEAT1qcXo_jnxhuFU_oywM6PVeM-s7JRe58j5dPmJXZwfMiqjXq7GnKpHct9aWGDjifEAIkq2BWhbzRo1S9WY7ugPDtUzR698jLuPd2fBt7b_pczcEgOyt4MZFyGN1mYa5NV8WIahEnZnJW6LQjDQOelV1JS7St9g4HAqDdkP1E5Ng6bLpcW7eVDPa3yVQxqYo.T9VQq4C4VVrA4h3l1dxKHohe2Y_KsDMoSUAuu6gQFSk&dib_tag=se&keywords=bench+power+supply&qid=1708717238&sprefix=bech+power+%2Caps%2C218&sr=8-9"

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(product_to_track_url, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

price_whole = float(soup.find(name="span", class_="a-price-whole").getText())
price_fraction = float(soup.find(name="span", class_="a-price-fraction").getText()) / 100
price = price_whole + price_fraction

if price < TRESHOLD_PRICE:

    product_name = soup.find(name="span", id="productTitle").getText().strip()

    print(f"Subject:Amazon Price Alert!\n\n{product_name} is now ${price}! Buy now: {product_to_track_url}")

    email = os.environ.get('EMAIL')
    password = os.environ.get('EMAIL_PASSWORD')

    # send email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Amazon Price Alert!\n\n{product_name} is now ${price}! Buy now: {product_to_track_url}"
        )