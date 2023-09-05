from guess import Guess
from player import Player
from card import Card
from cards import Cards
from evaluation import Eval


class Position:
    def __init__(self, players: list[Player], guesses: list[Guess], evaluator: Eval) -> None:
        self.players = players
        self.num_players = len(players)
        self.evaluator = evaluator
        self.guesses = guesses
        self.cur_queue = []
        self.next_queue = []
        self.possible_cards = {card: 0 for card in Cards.all()}
        self.confirmed = {}
                
    def run(self) -> None:
        for guess in self.guesses:
            self.add_guess(guess)
    
    def add_guess(self, guess: Guess) -> None:
        if guess.reveal_id == -1:
            for player in self.players:
                for card in guess.cards:
                    self.add_command(player.remove_card, [card])
        
        else:
            if guess.reveal_id < guess.guess_id:
                end = guess.reveal_id + self.num_players
            else:
                end = guess.reveal_id
            
            for idx in range(guess.guess_id + 1, end):
                player_index = idx % self.num_players
                for card in guess.cards:
                    self.add_command(self.players[player_index].remove_card, [card])
                    
            if guess.revealed != Cards.none:
                self.add_command(self.players[guess.reveal_id].reveal_card, [guess.revealed])
            else:
                self.add_command(self.players[guess.reveal_id].add_show_set, [guess.cards])                
                    
        self.update()
                
    def add_command(self, command: callable, args: list) -> None:
        self.next_queue.append([command, args])
            
    def update(self) -> None:
        for cmd in self.cur_queue:
            cmd[0](*cmd[1])
        
        if self.next_queue:
            self.cur_queue = self.next_queue.copy()
            self.next_queue.clear()
            self.update()
            
        else:
            self.cur_queue.clear()

    def remove_from_all(self, card: Card) -> None:
        for player in self.players:
            player.remove_card(card)
            
    def print_info(self) -> None:
        print("---------------------------------------")
        print(f"Evaluation: {self.evaluate()}")
        print(f"Possible Cards({len(self.possible_cards)}): {self.possible_cards}")
        print(f"Confirmed Cards({len(self.confirmed)}): {self.confirmed}")
        print("Player Info:")
        for player_idx, player in enumerate(self.players):
            print(f"\t{player.name}({player_idx}):")
            print(f"\t\tKnown Cards({len(player.known_cards)}): {player.known_cards}")
            print(f"\t\tPossible Cards({len(player.possible_cards)}): {player.possible_cards}")
            print(f"\t\tShow Sets({len(player.show_sets)}): {player.show_sets}")
        print("---------------------------------------")

    def increase_possible(self, card: Card) -> None:
        self.possible_cards[card] += 1
        if self.possible_cards[card] == self.num_players:
            self.confirmed[card.type] = card
    
    def evaluate(self) -> int:
        evaluation = 0
        
        if len(self.confirmed) == 3:
            return self.evaluator.all_confirmed
        # evaluation += len(self.confirmed) * self.evaluator.confirmed
        
        evaluation += self.evaluator.low_weight * sum(self.possible_cards.values())
        evaluation += sum(self.evaluator.show_set_weights[len(show_set)] for player in self.players for show_set in player.show_sets)
        
        return evaluation
    