import random
from domain.card import Card

class DrawPile:
    def __init__(self):
        self.cards = []

        for rank in range(1, 14):
            self.cards.append(Card(rank, "Clubs"))
            self.cards.append(Card(rank, "Hearts"))
            self.cards.append(Card(rank, "Spades"))
            self.cards.append(Card(rank, "Diamonds"))

        random.shuffle(self.cards)

    def draw_cards(self, how_many = 1):
        return self.cards.pop()       
    