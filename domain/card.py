class Card:
    RANK_MAP = {1: "Ace", 14: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def rank_name(self):
        return Card.RANK_MAP.get(self.rank, str(self.rank))

    def display_name(self):
        return f"{self.rank_name()} of {self.suit}"

    def points(self):
        if self.rank == 1 or self.rank == 14:
            return 15

        if self.rank > 9:
            return 10

        return 5
