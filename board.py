from queue import SimpleQueue




class Board:
    
    MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
]
    
    ROOMS = {
        "KITCHEN": [(4, 7)], 
        "BALLROOM": [(7, 5), (9, 8), (14, 8), (16, 5)], 
        "CONSERVATORY": [(18, 5)], 
        "DINING_ROOM": [(8, 12), (6, 16)], 
        "BILLIARD_ROOM": [(17, 9)], 
        "LIBRARY": [(20, 13), (16, 16)], 
        "LOUNGE": [(6, 18)], 
        "HALL": [(11, 17), (12, 17), (15, 20)], 
        "STUDY": [(17, 20)]
    }
    
    def __init__(self, tokens: list) -> None:
        self.tokens = tokens
        self.map = Board.MAP
        self.update_map()
        
    def update_map(self):
        self.map = Board.MAP
        for token in self.tokens:
            if token.room is None:
                self.map[token.pos[1]][token.pos[0]] = 1
                
    def room_dists(self, start: tuple):
        turns = {}
        for room, entrances in Board.ROOMS.items():
            shortest = min([self.shortest_path(start, entrance) for entrance in entrances])
            turns[room] = (shortest + 1) / 3.5
        
        if turns["STUDY"] > turns["KITCHEN"] + 1:
            turns["STUDY"] = turns["KITCHEN"] + 1
            
        elif turns["KITCHEN"] > turns["STUDY"] + 1:
            turns["KITCHEN"] = turns["STUDY"] + 1
            
        if turns["CONSERVATORY"] > turns["LOUNGE"] + 1:
            turns["CONSERVATORY"] = turns["LOUNGE"] + 1
            
        if turns["LOUNGE"] > turns["CONSERVATORY"] + 1:
            turns["LOUNGE"] = turns["CONSERVATORY"] + 1
            
        for room, length in turns.items():
            print(room, round(length, 3))
            
        return turns
        
    def shortest_path(self, start: tuple, end: tuple) -> int:
        
        rows, cols = len(self.map), len(self.map[0])
        visited = [[False] * cols for _ in range(rows)]

        queue = SimpleQueue()
        queue.put((start[0], start[1], 0))

        # THIS WHILE STATEMENT IS ALWAYS GONNA BE TRUE -- FIX
        while not queue.empty():
            x, y, distance = queue.get()

            if (x, y) == end:
                return distance

            # Check neighboring cells
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy

                if 0 <= ny < rows and 0 <= nx < cols and self.map[ny][nx] == 0 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.put((nx, ny, distance + 1))

        return -1  # No path found
            
        
        
class Token:
    def __init__(self, name: str, pos: tuple) -> None:
        self.name = name
        self.room = None
        self.pos = pos
        
b = Board([])
print(b.room_dists((9, 0)))
# Token("Test", (7, 1))