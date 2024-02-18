from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

billboard_top_100_url = "https://www.billboard.com/charts/hot-100/"

client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.environ.get("SPOTIFY_REDIRECT_URI")

date = input("Witch date do you want to travel to? (YYYY-MM-DD): ")

response = requests.get(f"{billboard_top_100_url}{date}")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

song_titles = [song.getText().strip() for song in soup.select("li ul li h3")] 

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="playlist-modify-private"))

user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"Top 100 from {date}", public=False)
print("Playlist created successfully:", playlist["name"], "-", playlist["id"])

for song in song_titles:
    result = sp.search(q=f"track:{song} year:{date.split('-')[0]}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        sp.playlist_add_items(playlist_id=playlist["id"], items=[uri])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print("songs added successfully!")