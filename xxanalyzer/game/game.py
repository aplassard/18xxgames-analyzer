"""interfaces for an 18xx game"""

def download_game(game_id):
    pass

class Game:
    def __init__(self, game_id):
        self.game_id
        self.game_info = download_game(self.game_id)