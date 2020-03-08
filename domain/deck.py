import random
from domain.card import Card


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def points(self) -> int:
        total = 0

        for card in self.cards:
            total += card.points()

    def is_book(self) -> bool:
        if len(self.cards) < 3:
            return False

        return all([card.rank == self.cards[0].rank for card in self.cards])

    def is_run(self) -> bool:
        if len(self.cards) < 3:
            return False

        if any([card.suit != self.cards[0].suit for card in self.cards]):
            return False

        return self.is_sequential(ace_high=False) or self.is_sequential(ace_high=True)

    def is_sequential(self, ace_high=False) -> bool:
        cards = []

        if ace_high:
            for card in self.cards:
                if card.rank == 1:
                    cards.append(Card(14, card.suit))
                else:
                    cards.append(card)
        else:
            cards = self.cards[:]

        sorted_cards = sorted(cards, key=lambda c: c.rank)

        rank = sorted_cards.pop(0).rank

        for card in sorted_cards:
            rank += 1

            if card.rank != rank:
                return False

        return True
