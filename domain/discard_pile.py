class DiscardPile:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def take_card(self, how_many = 1):
        return [self.cards.pop]
