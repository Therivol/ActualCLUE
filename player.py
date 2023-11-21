from card import Card
from cards import Cards


class Player:
    def __init__(self, name: str, hand_size: int) -> None:
        self.name = name
        self.hand_size = hand_size
        self.position = None
        self.known_cards = set()
        self.possible_cards = Cards.all()
        self.show_sets: list[set] = []
        
    def __repr__(self) -> str:
        return self.name
        
    def set_position(self, position: any) -> None:
        self.position = position
        
    def reveal_card(self, card: Card) -> None:
        # should probably change this to .remove but then it gets an error. not sure why
        self.possible_cards.discard(card)
        self.known_cards.add(card)
        if len(self.known_cards) == self.hand_size:
            for possible_card in self.possible_cards:
                self.position.increase_possible(possible_card)
            self.possible_cards.clear()
            
        self.show_sets = [show_set for show_set in self.show_sets if card not in show_set]
        self.position.add_known(card)
        
        self.position.add_command(self.position.remove_from_all, [card])
        
    def add_show_set(self, show_set: set[Card]):
        new_set = set()
        for card in show_set:
            if card in self.known_cards:
                return
            if card in self.possible_cards:
                new_set.add(card)
        
        len_set = len(new_set)
        if len_set > 1:
            self.show_sets.append(new_set)
        elif len_set == 1:
            self.position.add_command(self.reveal_card, [new_set.pop()])
            
                    
    def remove_card(self, card: Card) -> None:
        if card in self.possible_cards:
            self.possible_cards.remove(card)
            self.position.increase_possible(card)
            if len(self.possible_cards) + len(self.known_cards) == self.hand_size:
                for card in self.possible_cards:
                    self.position.add_command(self.reveal_card, [card])
        
        show_set_updated = []
        for show_set in self.show_sets:
            if card in show_set:
                show_set.remove(card)
                if len(show_set) == 1:
                    self.position.add_command(self.reveal_card, [show_set.pop()])
                    continue
                
            show_set_updated.append(show_set)
        
        self.show_sets = show_set_updated