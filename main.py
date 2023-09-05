from game import Game
from player import Player
from cards import Cards
from guess import Guess
from nextguess import NextGuess
from multisim import MultiSim
from trio import Trio
from genetic import Genetic
from evaluation import Eval
import cProfile

import pstats


# cProfile.run("MultiSim(10, 3)")
# sim = MultiSim(1000, 3, Eval(5000, 30, {3: 10, 2: 15}))
# sim.print_info()
# print(hash(Guess(0, -1, Trio(Cards.study, Cards.col_mustard, Cards.revolver), Cards.none)))
# print(hash(Guess(0, 3, Trio(Cards.study, Cards.col_mustard, Cards.revolver), Cards.revolver)))

# Genetic(Eval(3000, 30, {3: 10, 2: 15}), 10, 20, 3)
# gen = Genetic(Eval(3002.29605, 30.0117825, {3: 9.917079200000002, 2: 14.76095865}), 1, 10000, 3)
gen = Genetic(Eval(3107.3818917440735, 30.496847727020274, {3: 9.986162913392482, 2: 14.802851343708411}), 1, 10000, 3)
gen.run()
quit()

players = [Player("Zander", 5), Player("Father", 5), Player("Cal", 4), Player("Mother", 4)]
game = Game(players, {Cards.mrs_peacock, Cards.miss_scarlet, Cards.billiard_room, Cards.kitchen, Cards.hall})


game.add_guess(Guess(0, 1, Trio(Cards.study, Cards.col_mustard, Cards.revolver), Cards.study))

game.add_guess(Guess(0, 2, Trio(Cards.lounge, Cards.mrs_peacock, Cards.revolver), Cards.revolver))
game.add_guess(Guess(0, 1, Trio(Cards.lounge, Cards.mr_green, Cards.candlestick), Cards.candlestick))
game.add_guess(Guess(0, 3, Trio(Cards.lounge, Cards.mr_green, Cards.knife), Cards.lounge))

game.current_position.print_info()


ng = NextGuess()


sorted_trios = ng.sort_trios(game.current_position)
print("_______________________________")

# quit()

next = ng.get_next_guesses(game.current_position)
unique = {val: [] for val in next.values()}
for trio, val in next.items():
    unique[val].append(trio)
print(len(unique))
for val in unique.keys():
    print(val, unique[val])
    print(val, len(unique[val]))
    print()
    
next_trios = set([frozenset(val) for val in unique.values()])
print(next_trios == sorted_trios)
# quit()

print(list(ng.get_next_guesses(game.current_position).keys())[0])
