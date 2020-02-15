import collections

from domain.card import Card
from domain.deck import Deck
from domain.draw_pile import DrawPile
from domain.discard_pile import DiscardPile
from domain.game import Game
from domain.player import Player
from domain.board import Board

players = [
    Player("Fred"),
    Player("Bob"),
    Player("Jim")
]

game = Game(board=Board(), draw_pile=DrawPile(), discard_pile=DiscardPile(), players=players)

