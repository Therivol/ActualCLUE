from player import Player
from game import Game
from cards import Cards
from card import Card

class TryAgain:
    def __init__(self, game: Game) -> None:
        self.players = game.players
        self.player_num = game.player_num
        
        self.cur_queue = []
        self.next_queue = []
        
        self.room_locs = {room: {id for id in range(self.player_num + 1)} for room in Cards.rooms()}
        self.character_locs = {character: {id for id in range(self.player_num + 1)} for character in Cards.characters()}
        self.weapon_locs = {weapon: {id for id in range(self.player_num + 1)} for weapon in Cards.weapons()}
        self.card_locs = [self.room_locs, self.character_locs, self.weapon_locs]
        
        self.player_hands = [[] for id in range(self.player_num)]
        
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
        
    def remove_from(self, card: Card, id: int) -> None:
        directory = self.card_locs[card.type][card]
        directory.remove(id)
        if len(directory) == 1:
            self.add_command()
            
    def reveal_for(self, card: )