from game import Game
from player import Player
from cards import Cards
from guess import Guess
from nextguess import NextGuess
from multisim import MultiSim
import cProfile

import pstats


# SHOW SETS NOT WORKING CORRECTLY
# some of the guess predictions go down in score (by 15), meaning it lost a show_set of len 2 without gaining a possible card increment or something
# cross ref code with original program?

# Changing the order of the combos changes the top score???? (uh oh)

cProfile.run("MultiSim(500, 3)")

quit()

players = [Player("Zander", 5), Player("Father", 5), Player("Cal", 4), Player("Mother", 4)]
game = Game(players, {Cards.mrs_peacock, Cards.miss_scarlet, Cards.billiard_room, Cards.kitchen, Cards.ball_room, Cards.hall})

game.add_guess(Guess(0, 1, {Cards.study, Cards.col_mustard, Cards.revolver}, Cards.study))
game.add_guess(Guess(0, 2, {Cards.lounge, Cards.mrs_peacock, Cards.revolver}, Cards.lounge))

game.current_position.print_info()

ng = NextGuess()
# print(ng.get_next_guesses(game.current_position))
print(ng.get_next_guesses(game.current_position)[frozenset([Cards.hall, Cards.mrs_peacock, Cards.knife])])
