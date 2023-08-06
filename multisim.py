import time
import statistics
import threading
from gamesim import GameSim


class MultiSim:
    def __init__(self, num_games: int, player_num: int) -> None:
        self.player_number = player_num
        self.start_time = time.time()
        self.times = []
        self.turns = []
        self.threads = []
        x = threading.Thread(target=self.run, args=[int(num_games)])
        # y = threading.Thread(target=self.run, args=[int(num_games)])
        
        self.threads.append(x)
        # self.threads.append(y)
        for thread in self.threads:
            thread.start()
            
        
    def run(self, num_games: int):
        times = []
        turns = []
        for _ in range(num_games):
            start = time.time()
            game_sim = GameSim(self.player_number)
            times.append(time.time() - start)
            turns.append(game_sim.turns)
        
        self.times += times
        self.turns += turns
        self.thread_done()
        
    def thread_done(self) -> None:
        for thread in self.threads:
            if threading.current_thread() != thread:
                if thread.is_alive():
                    return
        
        self.finish()
        
    def finish(self) -> None:
        print("AVG RUNTIME:", statistics.mean(self.times))
        print("AVG GUESSES:", statistics.mean(self.turns))
        print("STANDARD DEVIATION:", statistics.stdev(self.turns))
        print("MAX GUESSES:", max(self.turns))
        print("MIN GUESSES:", min(self.turns))
        print("ELAPSED:", time.time() - self.start_time)
