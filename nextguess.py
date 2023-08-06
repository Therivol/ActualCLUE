from position import Position
from cards import Cards
from guess import Guess
from tempposition import TempPosition
import time


class NextGuess:
    def __init__(self) -> None:
        self.tp = TempPosition()
    
    def get_next_guesses(self, position: Position):
        start_time = time.time()
        base_eval = position.evaluate()
        next_guesses = {}
        
        self.tp.set_anchor(position)
        
        for combo in Cards.all_combinations():
            outcomes = self.get_outcomes(position, combo)
            next_guesses[combo] = (sum(outcomes) / len(outcomes)) - base_eval
            
        sorted_guesses = dict(sorted(next_guesses.items(), key=lambda item: item[1], reverse=True))
        
        # print(time.time() - start_time)
        return sorted_guesses
            
    
    def get_outcomes(self, position: Position, combo: set):
        outcomes = []
        for player_idx, player in enumerate(position.players[1:]):
            player_outcomes = []
            for card in combo:
                if card in player.known_cards:
                    outcomes.append(self.tp.run(position, Guess(0, player_idx + 1, combo, card)))
                    return outcomes
                
                if card in player.possible_cards:
                    player_outcomes.append(self.tp.run(position, Guess(0, player_idx + 1, combo, card)))
            
            outcomes += player_outcomes
        
        outcomes.append(self.tp.run(position, Guess(0, -1, combo)))
        
        return outcomes
    
    
