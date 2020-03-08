from domain.hand import Hand

class Player:
    def __init__(self, screen_name: str):
        self.screen_name = screen_name
        self.hand = []