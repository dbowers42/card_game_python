import random

class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def points(self):
        total = 0
        
        for card in self.cards:
            total += card.points()

    def is_book(self):
        if len(self.cards) < 3:
            return False

        return all([card.rank == self.cards[0].rank for card in self.cards])

    def is_run(self):
        if len(self.cards) < 3:
            return False

        if any([card.suit != self.cards[0].suit for card in self.cards]):
            return False

        sorted_cards = sorted(self.cards, key = lambda c: c.rank)

        for card in sorted_cards:
            print(card.display_name())

        rank = sorted_cards.pop(0).rank
        
        for card in sorted_cards:
            rank += 1

            print(rank)

            if card.rank != rank:
                return False
        
        return True
        