import collections

from domain.card import Card
from domain.deck import Deck

deck = Deck()

deck.add_card(Card(1, "Clubs"))
deck.add_card(Card(4, "Clubs"))
deck.add_card(Card(2, "Clubs"))
deck.add_card(Card(3, "Clubs"))

print(deck.is_run())

