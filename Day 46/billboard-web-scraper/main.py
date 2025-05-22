import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

target_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{target_date}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

song_info = soup.select("li h3#title-of-a-story")
song_titles = [item.get_text(strip=True) for item in song_info]
artist_info = soup.select("li span.a-no-trucate")
artists = [artist.get_text(strip=True) for artist in artist_info]

search_queries = [f"{title} {artist}" for title, artist in zip(song_titles, artists)]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('SPOTIFY_ID'),
    client_secret=os.getenv('SPOTIFY_SECRET'),
    redirect_uri=os.getenv('SPOTIFY_REDIRECT'),
    scope="playlist-modify-public playlist-modify-private"
))

user_id = sp.current_user()['id']
playlist_name = f"Top 100 from {target_date}"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=f"Billboard Top 100 for {target_date}")
print(f"Created playlist: {playlist_name}")

track_ids = []
for query in search_queries:
    results = sp.search(q=query, type='track', limit=1)
    tracks = results['tracks']['items']
    if tracks:
        track_ids.append(tracks[0]['id'])
    else:
        print(f"Could not find track: {query}")

for i in range(0, len(track_ids), 100):
    sp.playlist_add_items(playlist_id=playlist['id'], items=track_ids[i:i+100])

print(f"Added {len(track_ids)} tracks to the playlist!")
