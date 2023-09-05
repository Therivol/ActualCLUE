from position import Position
from guess import Guess
import copy


class TempPosition:
    def __init__(self) -> None:
        self.player_data: list
        self.possible_cards: dict
        self.confirmed: dict
    
    def set_anchor(self, position: Position):
        self.player_data = [[player.known_cards.copy(), player.possible_cards.copy(), player.show_sets] for player in position.players]
        self.possible_cards = position.possible_cards.copy()
        self.confirmed = position.confirmed.copy()
    
    def run(self, position: Position, guess: Guess) -> int:
        
        position.add_guess(guess)        
        eval = position.evaluate()
        self.reset(position)
                
        return eval
    
    def reset(self, position: Position):
        for player_idx, player in enumerate(position.players):
            player.known_cards = self.player_data[player_idx][0].copy()
            player.possible_cards = self.player_data[player_idx][1].copy()
            player.show_sets = [set(s) for s in self.player_data[player_idx][2]]
            
        position.possible_cards = self.possible_cards.copy()
        position.confirmed = self.confirmed.copy()