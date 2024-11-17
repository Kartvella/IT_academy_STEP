import requests
import json

URL = 'https://rickandmortyapi.com/api'

def fetch_characters():
    characters = {}
    next_url = f"{URL}/character"
    while next_url:
        response = requests.get(next_url).json()
        for character in response['results']:
            characters[character['name']] = character['episode']
        next_url = response['info']['next']
    return characters

def fetch_all_episodes():
    episodes = {}
    next_url = f"{URL}/episode"
    while next_url:
        response = requests.get(next_url).json()
        for episode in response['results']:
            episodes[episode['url']] = episode['name']
        next_url = response['info']['next']
    return episodes

def map_characters_to_episodes():
    characters = fetch_characters()
    episodes = fetch_all_episodes()
    return {name: [episodes[url] for url in urls] for name, urls in characters.items()}

def save_to_file(data):
    with open("Lecture 20 - APIs/character_episodes.json", "w") as file:
        json.dump(data, file, indent=4)

character_episodes = map_characters_to_episodes()
save_to_file(character_episodes)

print("data saved to 'character_episodes.json'")
