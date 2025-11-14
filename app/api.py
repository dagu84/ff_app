import requests as re

def get_user(username: str):
    url = f"https://api.sleeper.app/v1/user/{username}"
    response = re.get(url)
    response.raise_for_status()
    return response.json()

def get_leagues(user_id: str, season: int):
    url = f"https://api.sleeper.app/v1/user/{user_id}/leagues/nfl/{season}"
    response = re.get(url)
    response.raise_for_status()
    return response.json()

def get_specfic_league(league_id: str):
    url = f"https://api.sleeper.app/v1/league/{league_id}"
    response = re.get(url)
    response.raise_for_status()
    return response.json()

def get_rosters(league_id: str):
    url = f"https://api.sleeper.app/v1/league/{league_id}/rosters"
    response = re.get(url)
    response.raise_for_status()
    return response.json()
