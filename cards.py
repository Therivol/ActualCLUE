from card import Card
import random
from itertools import product


class Cards:
    
    # Card Types
    room = 0
    character = 1
    weapon = 2
    
    # Cards
    study = Card("STUDY", 0)
    hall = Card("HALL", 0)
    lounge = Card("LOUNGE", 0)
    library = Card("LIBRARY", 0)
    dining_room = Card("DINING ROOM", 0)
    billiard_room = Card("BILLIARD ROOM", 0)
    conservatory = Card("CONSERVATORY", 0)
    ball_room = Card("BALLROOM", 0)
    kitchen = Card("KITCHEN", 0)
    
    miss_scarlet = Card("MISS SCARLET", 1)
    mr_green = Card("MR GREEN", 1)
    prof_plum = Card("PROFESSOR PLUM", 1)
    col_mustard = Card("COLONEL MUSTARD", 1)
    mrs_white = Card("MRS WHITE", 1)
    mrs_peacock = Card("MRS PEACOCK", 1)
    
    candlestick = Card("CANDLESTICK", 2)
    knife = Card("KNIFE", 2)
    rope = Card("ROPE", 2)
    revolver = Card("REVOLVER", 2)
    lead_pipe = Card("LEAD PIPE", 2)
    wrench = Card("WRENCH", 2)
    
    # Groups
    
    _rooms = {study, hall, lounge, library, dining_room, billiard_room, conservatory, ball_room, kitchen}
    _characters = {miss_scarlet, mr_green, prof_plum, col_mustard, mrs_white, mrs_peacock}
    _weapons = {candlestick, knife, rope, revolver, wrench, lead_pipe}
    _all = _rooms | _characters | _weapons
    
    _rooms_list = list(_rooms)
    _characters_list = list(_characters)
    _weapons_list = list(_weapons)
    _all_list = list(_all)
    
    _all_combinations = [frozenset(combo) for combo in product(_rooms_list, _characters_list, _weapons_list)]
    
    # Methods
    @staticmethod
    def rooms() -> set:
        return Cards._rooms.copy()

    @staticmethod
    def characters() -> set:
        return Cards._characters.copy()
    
    @staticmethod
    def weapons() -> set:
        return Cards._weapons.copy()
    
    @staticmethod
    def all() -> set:
        return Cards._all.copy()
    
    @staticmethod
    def case_file() -> set:
        return {0: random.choice(Cards._rooms_list), 1: random.choice(Cards._characters_list), 2: random.choice(Cards._weapons_list)}
    
    @staticmethod
    def all_combinations() -> list:
        return Cards._all_combinations