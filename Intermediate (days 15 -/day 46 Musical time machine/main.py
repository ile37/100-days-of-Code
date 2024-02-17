from bs4 import BeautifulSoup
import requests


date = input("Witch date do you want to travel to? (YYYY-MM-DD): ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

song_titles = [song.getText().strip() for song in soup.select("li ul li h3")] 
print(song_titles)
