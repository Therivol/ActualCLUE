from position import Position
from cards import Cards
from guess import Guess
from tempposition import TempPosition
from trio import Trio
from collections import defaultdict
import time


class NextGuess:
    def __init__(self) -> None:
        self.tp = TempPosition()
    
    def get_next_guesses(self, position: Position):
        # start_time = time.time()
        base_eval = position.evaluate()
        next_guesses = {}
        self.tp.set_anchor(position)
        
        for trio in Cards.all_trios():
            outcomes = self.get_outcomes(position, trio)
            next_guesses[trio] = (sum(outcomes) / len(outcomes)) - base_eval

        sorted_guesses = dict(sorted(next_guesses.items(), key=lambda item: item[1], reverse=True))
        
        # print(time.time() - start_time)
        return sorted_guesses
    
    def get_next_predictive(self, position: Position):
        pred = position.predictions
        predictions = {}
        for card, weights in pred.items():
            summation = sum(weights)
            length = len(weights)
            predictions[card] = [val * length/ summation for val in weights]
        # start_time = time.time()
        base_eval = position.evaluate()
        next_guesses = {}
        
        self.tp.set_anchor(position)
        
        for trio in Cards.all_trios():
            outcomes = self.get_predictive_outcomes(position, trio, predictions)
            next_guesses[trio] = (sum(outcomes) / len(outcomes)) - base_eval
            
        sorted_guesses = dict(sorted(next_guesses.items(), key=lambda item: item[1], reverse=True))
        
        # print(time.time() - start_time)
        return sorted_guesses
    
    def sort_trios(self, position: Position) -> dict:
        non_zeroes = []
        unique = {}
        for trio in Cards.all_trios():
            total_info_count = 0
            total_card_info = {}
            trio_known = set(trio)
            for card in trio:
                if card in position.players[0].known_cards:
                    trio_known.remove(card)
            
            if not len(trio_known) == 0:
                
                for player in position.players[1 :]:
                    
                    has_possible = False
                    has_known = False
                    
                    info_count = 0
                    
                    card_info = defaultdict(int)
                    for card in trio_known:
                        if card in player.possible_cards:
                            has_possible = True
                            card_info[card] += 1
                            info_count += 1
                        if card in player.known_cards:
                            has_known = True
                    
                    if has_known:
                        break
                    elif has_possible:
                        total_info_count += info_count
                        total_card_info = total_card_info | card_info
                        

            # if total_info_count != 0:
                # non_zeroes.append(trio)
            
            key = frozenset(total_card_info.items())
            if key in unique:
                unique[key].append(trio)
            else:
                unique[key] = [trio]
        for val in unique.keys():
            print(val, unique[val])
            print(val, len(unique[val]))
            print()
            
        
        # return non_zeroes
        return unique
    

    def get_predictive_outcomes(self, position: Position, trio: Trio, predictions: dict):
        outcomes = []
        for player_idx, player in enumerate(position.players[1:]):
            player_outcomes = []
            for card in trio:
                if card in player.known_cards:
                    outcomes.append(self.tp.run(position, Guess(0, player_idx + 1, trio, card)))
                    return outcomes
                
                if card in player.possible_cards:
                    player_outcomes.append(self.tp.run(position, Guess(0, player_idx + 1, trio, card)) * predictions[card][player_idx + 1])
            
            outcomes += player_outcomes
        
        outcomes.append(self.tp.run(position, Guess(0, -1, trio, Cards.none)))
        
        return outcomes
    

            
    
    def get_outcomes(self, position: Position, trio: Trio):
        outcomes = []
        for player_idx, player in enumerate(position.players[1:]):
            player_outcomes = []
            for card in trio:
                if card in player.known_cards:
                    outcomes.append(self.tp.run(position, Guess(0, player_idx + 1, trio, card)))
                    return outcomes
                
                if card in player.possible_cards:
                    player_outcomes.append(self.tp.run(position, Guess(0, player_idx + 1, trio, card)))
            
            outcomes += player_outcomes
        
        outcomes.append(self.tp.run(position, Guess(0, -1, trio, Cards.none)))
        
        return outcomes
    
    
