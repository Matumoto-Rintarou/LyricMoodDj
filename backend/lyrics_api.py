import requests
import os

GENIUS_TOKEN = os.getenv("GENIUS_API_TOKEN")

def get_lyrics(query):
    base_url = "https://api.genius.com/search"
    headers = {"Authorization": f"Bearer {GENIUS_TOKEN}"}
    params = {"q": query}
    response = requests.get(base_url, headers=headers, params=params).json()
    hits = response["response"]["hits"]
    if hits:
        return hits[0]["result"]["title"] + " - " + hits[0]["result"]["primary_artist"]["name"]
    return "Not found"
