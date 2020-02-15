from domain.board import Board
from domain.draw_pile import DrawPile
from domain.discard_pile import DiscardPile
from domain.hand import Hand

class Game:
    def __init__(self, board, draw_pile, discard_pile, players):
        self.board = board
        self.draw_pile = draw_pile
        self.discard_pile = discard_pile
        self.players = players

    def deal(self):
        for player in self.players:
            player.hand = Hand(self.draw_pile.draw_cards(7))