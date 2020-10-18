"""interfaces for an 18xx game"""
import requests

def download_game(game_id):
    url = f"https://www.18xx.games/api/game/{game_id}"
    return requests.get(url).json()

class Game:
    def __init__(self, game_id):
        self.game_id = game_id
        self.game_info = download_game(self.game_id)