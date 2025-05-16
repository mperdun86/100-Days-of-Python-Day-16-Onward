import requests
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all(name="h3", class_="title")

movie_titles = [tag.get_text() for tag in titles]

mt_correct_order = movie_titles[::-1]

print(mt_correct_order)

with open("movie_list.txt", "w", encoding="utf-8") as movie_list:
    for movie in mt_correct_order:
        movie_list.write(movie + "\n")



