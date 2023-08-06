from dataclasses import dataclass
from card import Card


@dataclass
class Guess:
    guess_id: int
    reveal_id: int
    cards: frozenset
    revealed: Card=None
    
    def __repr__(self) -> str:
        return f"{self.guess_id}-{self.reveal_id}-{self.cards}-{self.revealed}"
    