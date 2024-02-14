import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

movie_tags = soup.find_all(name="h3", class_="title")
movie_titles = [movie_tag.getText() for movie_tag in movie_tags]

with open("movies.txt", mode="w") as file:
    for title in reversed(movie_titles):
        file.write(f"{title}\n")
