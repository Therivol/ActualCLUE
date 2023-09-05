import time
import statistics
import threading
from gamesim import GameSim
from evaluation import Eval



class MultiSim:
    def __init__(self, num_games: int, player_num: int, evaluator: Eval) -> None:
        self.num_games = num_games
        self.player_num = player_num
        self.evaluator = evaluator
        
        self.start_time = time.time()
        
        self.times = []
        self.turns = []
        
        self.run()
        
    def run(self) -> None:
        for _ in range(self.num_games):
            start = time.time()
            game_sim = GameSim(self.player_num, self.evaluator)
            self.times.append(time.time() - start)
            self.turns.append(game_sim.turns)
    
    def get_report(self) -> str:
        report = ""
        report += f"AVG RUNTIME: {statistics.mean(self.times)}\n"
        report += f"AVG GUESSES: {statistics.mean(self.turns)}\n"
        report += f"STANDARD DEVIATION: {statistics.stdev(self.turns)}\n"
        report += f"MAX GUESSES: {max(self.turns)}\n"
        report += f"MIN GUESSES: {min(self.turns)}\n"
        report += f"ELAPSED: {time.time() - self.start_time}\n"
        return report

