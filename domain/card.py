from .suit import Suit

class Card:
    RANK_MAP = {1: "Ace", 14: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

    def __init__(self, rank: int, suit: Suit):
        self.rank = rank
        self.suit = suit

    def display_name(self) -> str:
        return f"{self.__rank_name()} of {self.suit.name}"

    def points(self) -> int:
        if self.rank == 1 or self.rank == 14:
            return 15

        if self.rank > 9:
            return 10

        return 5

    def __rank_name(self) -> str:
        return Card.RANK_MAP.get(self.rank, str(self.rank))
