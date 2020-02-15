import collections

from domain.card import Card
from domain.deck import Deck

deck1 = Deck()

deck1.add_card(Card(1, "Clubs"))
deck1.add_card(Card(4, "Clubs"))
deck1.add_card(Card(2, "Clubs"))
deck1.add_card(Card(3, "Clubs"))

print(deck1.is_run())

deck2 = Deck()

deck2.add_card(Card(1, "Clubs"))
deck2.add_card(Card(13, "Clubs"))
deck2.add_card(Card(12, "Clubs"))

print(deck2.is_run())



