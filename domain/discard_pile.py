from .card import Card

class DiscardPile:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def take_card(self, how_many = 1) -> Card:
        return [self.cards.pop]
