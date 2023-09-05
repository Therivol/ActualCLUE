from card import Card


class Trio:
    def __init__(self, room: Card, character: Card, weapon: Card) -> None:
        self.room = room
        self.character = character
        self.weapon = weapon
        self.hash = self.room.id + (self.character.id << 4) + (self.weapon.id << 8)
        self.set = {self.room, self.character, self.weapon}
        
    def __hash__(self) -> int:
        return self.hash
    
    def __repr__(self) -> str:
        return f"({self.room}, {self.character}, {self.weapon})"
    
    def __eq__(self, __value: object) -> bool:
        return __value.hash == self.hash
    
    def __iter__(self):
        yield self.room
        yield self.character
        yield self.weapon
        
    def __contains__(self, __value: object) -> bool:
        return __value in self.set
    
    def __set__(self) -> set:
        return self.set
    
    
    @staticmethod
    def hash_non_trio(room: Card, character: Card, weapon: Card):
        return room.id + (character.id << 4) + (weapon.id << 8)