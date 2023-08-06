from player import Player
from guess import Guess
from position import Position
from cards import Cards
from card import Card


class Game:
    def __init__(self, players: list[Player], your_hand: set[Card]) -> None:
        self.players = players
        self.player_num = len(players)
        self.your_hand = your_hand
        
        self.guesses = []
        self.current_position = Position(self.players, self.guesses)
        
        self.start()
        
    def start(self) -> None:
        for player in self.players:
            player.set_position(self.current_position)
        
        for card in self.your_hand:
            self.current_position.add_command(self.players[0].reveal_card, [card])
        
        self.current_position.update()
    
    def add_guess(self, guess: Guess) -> None:
        self.guesses.append(guess)
        self.current_position.add_guess(guess)
        
    def check_confirmed(self) -> bool:
        return len(self.current_position.confirmed) == 3
        