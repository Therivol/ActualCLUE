from game import Game
from player import Player
from cards import Cards
from nextguess import NextGuess
from guess import Guess
import random


class GameSim:
    def __init__(self, num_players, evaluator) -> None:
        self.evaluator = evaluator
        self.next_guess = NextGuess()
        self.case_file = Cards.case_file()
        self.your_player = 0
        self.player_hands = [set() for _ in range(num_players)]
        self.num_players = num_players
        self.distribute()
        self.players = self.get_players()
        self.game = Game(self.players, self.player_hands[0], evaluator)
        self.turns = 0
        self.run()
        
    def distribute(self) -> None:
        all_cards = Cards._all_list.copy()
        player_idx = 0
        while len(all_cards) > 0:
            rand_card = random.choice(all_cards)
            all_cards.remove(rand_card)
            if rand_card == self.case_file[rand_card.type]:
                continue
            else:
                self.player_hands[player_idx].add(rand_card)
            
            player_idx = (player_idx + 1) % self.num_players
        
        
    def get_players(self) -> list[Player]:
        players = []
        for idx in range(self.num_players):
            player = Player(str(idx), len(self.player_hands[idx]))
            players.append(player)
            
        return players
            
    def run(self) -> None:
        while not self.game.check_confirmed():
            self.turns += 1
            next_guess = list(self.next_guess.get_next_guesses(self.game.current_position).keys())[0]
            break_outside = False
            for idx, hand in enumerate(self.player_hands[1:]):
                for card in next_guess:
                    if card in hand:
                        reveal_id = idx + 1
                        revealed = card
                        break_outside = True
                        break
                if break_outside:
                    break
            else:
                reveal_id = -1
                revealed = Cards.none
                
            self.game.add_guess(Guess(0, reveal_id, next_guess, revealed))
            
        if self.game.current_position.confirmed != self.case_file:
            print(self.game.current_position.confirmed != self.case_file)
            