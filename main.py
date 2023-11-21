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
# gen = Genetic(Eval(3107.3818917440735, 30.496847727020274, {3: 9.986162913392482, 2: 14.802851343708411}), 1, 10000, 3)
# gen.run()


players = [Player("Zander", 4), Player("Kerry", 4), Player("Cal", 4), Player("Mother", 3), Player("Father", 3)]
eval = Eval(3000, 30, {3: 10, 2: 15, 0: 0})
game = Game(players, {Cards.candlestick, Cards.lead_pipe, Cards.lounge, Cards.study}, eval)

# Zander: 0
# Kerry: 1
# Cal: 2
# Mother: 3
# Father: 4

# kerry does not have scarlet, lounge, or pipe
# K has ballroom or mrs white
# we can get more info from cards revealed to other players and how they change their guesses

game.add_guess(Guess(3, 0, Trio(Cards.lounge, Cards.miss_scarlet, Cards.lead_pipe), Cards.none)) # showed lounge to Mother
game.add_guess(Guess(0, 1, Trio(Cards.study, Cards.mr_green, Cards.knife), Cards.knife))
game.add_guess(Guess(1, 0, Trio(Cards.lounge, Cards.col_mustard, Cards.candlestick), Cards.none)) # showed lounge to Kerry
# game.add_guess(Guess(3, 4, Trio(Cards.conservatory, Cards.miss_scarlet, Cards.candlestick), Cards.none)) # showed candle to Mother
game.add_guess(Guess(0, 1, Trio(Cards.kitchen, Cards.mr_green, Cards.rope), Cards.kitchen))
game.add_guess(Guess(1, 2, Trio(Cards.conservatory, Cards.miss_scarlet, Cards.revolver), Cards.none))
game.add_guess(Guess(4, 1, Trio(Cards.ball_room, Cards.mrs_white, Cards.knife), Cards.none))
game.add_guess(Guess(2, 3, Trio(Cards.ball_room, Cards.col_mustard, Cards.lead_pipe), Cards.none))
game.add_guess(Guess(0, 3, Trio(Cards.ball_room, Cards.mr_green, Cards.rope), Cards.ball_room))
game.add_guess(Guess(1, 3, Trio(Cards.ball_room, Cards.mr_green, Cards.revolver), Cards.none))
game.add_guess(Guess(4, 1, Trio(Cards.billiard_room, Cards.mr_green, Cards.knife), Cards.none))
game.add_guess(Guess(1, 2, Trio(Cards.conservatory, Cards.prof_plum, Cards.lead_pipe), Cards.none))

# game.add_guess(Guess(0, 1, Trio(Cards.conservatory, Cards.mrs_white, Cards.knife), Cards.mrs_white)) # THIS ONE IS UNSURE
game.add_guess(Guess(2, 4, Trio(Cards.kitchen, Cards.mr_green, Cards.lead_pipe), Cards.none))
game.add_guess(Guess(0, 1, Trio(Cards.lounge, Cards.mrs_peacock, Cards.wrench), Cards.mrs_peacock))
game.add_guess(Guess(2, 0, Trio(Cards.lounge, Cards.mrs_peacock, Cards.lead_pipe), Cards.none)) # showed lounge to Cal
game.add_guess(Guess(3, 1, Trio(Cards.kitchen, Cards.miss_scarlet, Cards.knife), Cards.none))
game.add_guess(Guess(0, 2, Trio(Cards.dining_room, Cards.col_mustard, Cards.rope), Cards.dining_room))
game.add_guess(Guess(1, 2, Trio(Cards.billiard_room, Cards.col_mustard, Cards.lead_pipe), Cards.none))
game.add_guess(Guess(2, 0, Trio(Cards.conservatory, Cards.col_mustard, Cards.lead_pipe), Cards.none))
game.add_guess(Guess(3, 0, Trio(Cards.study, Cards.miss_scarlet, Cards.rope), Cards.none))
game.add_guess(Guess(4, 3, Trio(Cards.library, Cards.mrs_white, Cards.wrench), Cards.none))
game.add_guess(Guess(0, 3, Trio(Cards.lounge, Cards.prof_plum, Cards.revolver), Cards.prof_plum))

game.add_guess(Guess(0, 1, Trio(Cards.hall, Cards.mr_green, Cards.lead_pipe), Cards.hall)) # unsure
game.add_guess(Guess(0, 2, Trio(Cards.ball_room, Cards.miss_scarlet, Cards.lead_pipe), Cards.miss_scarlet)) # unsure but both sure together

# game.add_guess(Guess(1, 4, Trio(Cards.lounge, Cards.mrs_white, Cards.rope), Cards.none))
# game.add_guess(Guess(3, 1, Trio(Cards.hall, Cards.miss_scarlet, Cards.wrench), Cards.none))
# game.add_guess(Guess(4, 0, Trio(Cards.lounge, Cards.mr_green, Cards.rope), Cards.none))

# game.current_position.add_command(game.current_position.players[4].reveal_card, [Cards.revolver])
game.current_position.update()

print(game.current_position.known_cards)


game.current_position.print_info()

ng = NextGuess()
guesses = ng.get_next_guesses(game.current_position)
for guess in guesses:
    if guesses[guess] != 0:
        print(guess, guesses[guess])

quit()


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
