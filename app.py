import collections
import domain

players = [
    domain.Player("Fred"),
    domain.Player("Bob"),
    domain.Player("Jim")
]

game = domain.Game(
    board=domain.Board(), 
    draw_pile=domain.DrawPile(), 
    discard_pile=domain.DiscardPile(), 
    players=players)

game.deal()

for player in game.players:
    print(f"== {player.screen_name} ==")
    for card in player.hand.cards:
       print(card.display_name())