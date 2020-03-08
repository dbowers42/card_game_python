from .deck import Deck

class Board:
    def __init__(self):
        self.decks = []

    def add_deck(self, deck: Deck):
        self.decks.append(deck)
