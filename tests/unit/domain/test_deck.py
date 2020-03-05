import unittest

from domain.deck import Deck
from domain.card import Card


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.deck.add_card(Card(1, "Clubs"))

    def test_add_card(self):
        self.assertEqual(len(self.deck.cards), 1)


class TestDeckMultileCards(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.deck.add_card(Card(1, "Clubs"))
        self.deck.add_card(Card(7, "Hearts"))

    def test_add_card(self):
        self.assertEqual(len(self.deck.cards), 2)


if __name__ == '__main__':
    unittest.main()
