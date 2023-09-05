from dataclasses import dataclass
from card import Card
from trio import Trio


class Guess:
    
    def __init__(self, guess_id: int, reveal_id: int, cards: Trio, revealed: Card) -> None:
        self.guess_id = guess_id
        self.reveal_id = reveal_id
        self.cards = cards
        self.revealed = revealed
    
    def __repr__(self) -> str:
        return f"{self.guess_id}-{self.reveal_id}-{self.cards}-{self.revealed}"

    

    