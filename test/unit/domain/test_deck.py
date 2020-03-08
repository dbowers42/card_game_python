import unittest

from parameterized import parameterized
from domain.deck import Deck
from domain.card import Card
from domain.suit import Suit


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.deck.add_card(Card(1, Suit.Clubs))

    def test_add_card(self):
        self.assertEqual(len(self.deck.cards), 1)


class TestDeckMultileCards(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        # TODO: clearing should not be needed
        self.deck.cards.clear()
        self.deck.add_card(Card(1, Suit.Clubs))
        self.deck.add_card(Card(7, Suit.Hearts))

    def test_add_card(self):
        self.assertEqual(len(self.deck.cards), 2)


class TestDeckPoints(unittest.TestCase):
    @parameterized.expand([
        (Deck([]), 0),
        (Deck([Card(1, Suit.Clubs)]), 15),
        (Deck([Card(14, Suit.Clubs)]), 15),
        (Deck([Card(1, Suit.Clubs), Card(2, Suit.Clubs), Card(3, Suit.Clubs)]), 25),
        (Deck([Card(1, Suit.Clubs), Card(9, Suit.Clubs), Card(10, Suit.Clubs)]), 30),
        (Deck([Card(10, Suit.Clubs), Card(11, Suit.Clubs), Card(12, Suit.Clubs)]), 30),
        (Deck([Card(2, Suit.Clubs), Card(3, Suit.Clubs), Card(4, Suit.Clubs)]), 15),
        (Deck([Card(2, Suit.Clubs), Card(3, Suit.Clubs), Card(13, Suit.Clubs)]), 20)
    ])
    def test_points(self, deck: Deck, points: int):
        self.assertEqual(deck.points(), points)


if __name__ == '__main__':
    unittest.main()
