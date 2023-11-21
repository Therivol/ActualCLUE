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
        self.possible_cards = {card: names.copy() for card, names in position.possible_cards.items()}
        self.confirmed = position.confirmed.copy()
        self.known_cards = [position.known_cards[0].copy(), position.known_cards[1].copy(), position.known_cards[2].copy()]
        self.predictions = position.predictions.copy()
    
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
            
        position.possible_cards = {card: names.copy() for card, names in self.possible_cards.items()}
        position.confirmed = self.confirmed.copy()
        position.known_cards = [self.known_cards[0].copy(), self.known_cards[1].copy(), self.known_cards[2].copy()]
        position.predictions = self.predictions.copy()