import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint


def fetch_billboard_page(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None


def extract_song_titles(page_content):
    soup = BeautifulSoup(page_content, "html.parser")
    # Correct the CSS selector
    song_names_spans = soup.select("div.o-chart-results-list-row-container ul li ul li h3#title-of-a-story")
    return [song.getText().strip() for song in song_names_spans]


def get_billboard_top_100(desired_date):
    base_url = "https://www.billboard.com/charts/hot-100/"
    billboard_url = base_url + desired_date
    headers = {'User-Agent': 'Mozilla/5.0'}

    page_content = fetch_billboard_page(billboard_url, headers)
    if page_content:
        return extract_song_titles(page_content)


def authenticate_spotify(client_id, client_secret, redirect_uri, scope, username):
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope,
            show_dialog=True,
            cache_path="token.txt",
            username=username,
        )
    )
    return sp


def get_spotify_uris(song_names, sp):
    uris = []
    for song_name in song_names:
        result = sp.search(q=song_name, limit=1)
        tracks = result['tracks']['items']
        if tracks:
            uris.append(tracks[0]['uri'])
        else:
            print(f"No results for {song_name}")
    return uris


def create_billboard_playlist(sp, desired_date, uris):
    playlist_name = f"{desired_date} Billboard 100"
    playlist_description = f"Top 100 songs from Billboard on {desired_date}"
    playlist = sp.user_playlist_create(username, playlist_name, public=False, description=playlist_description)
    playlist_id = playlist['id']
    sp.playlist_add_items(playlist_id, uris)
    print(f"Playlist created: {playlist['external_urls']['spotify']}")


if __name__ == "__main__":
    desired_date = input("Enter the date you would like to travel to in YYYY-MM-DD format: ")
    song_names = get_billboard_top_100(desired_date)
    if song_names:
        client_id = 'f942e82a6a7440ef88d0cd2b995e7fe2'
        client_secret = '496542177659411ea5ac550f4a06fc40'
        redirect_uri = 'http://example.com'
        scope = 'playlist-modify-private'
        username = 'dor12'

        sp = authenticate_spotify(client_id, client_secret, redirect_uri, scope, username)
        uris = get_spotify_uris(song_names, sp)
        pprint(uris)
        if uris:
            create_billboard_playlist(sp, desired_date, uris)
        else:
            print("Failed to retrieve song URIs.")
    else:
        print("Failed to retrieve song names.")



