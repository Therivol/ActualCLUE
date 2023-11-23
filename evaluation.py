

class Eval:
    
    def __init__(self, all_confirmed: int, low_weight: int, show_set_weights: dict, num_players: int) -> None:
        # self.all_confirmed = all_confirmed
        self.all_confirmed = 21 * num_players - 18
        # self.low_weight = low_weight
        self.low_weight = 1
        self.show_set_weights = show_set_weights
        self.show_set_weights = {3: num_players / 3, 2: num_players / 2}
        
        
    def __hash__(self) -> int:
        return hash(self.all_confirmed, self.low_weight, self.show_set_weights)
    
    
3000
30
{3: 10, 2: 15}