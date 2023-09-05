from evaluation import Eval
from multisim import MultiSim
import statistics
import random
import time


class Genetic:
    def __init__(self, initial_evaluator: Eval, depth: int, iters: int, player_number: int) -> None:
        self.timestamp = int(time.time())
        
        self.current_eval = initial_evaluator
        self.best_eval = initial_evaluator
        self.best_val = 12
        self.depth = depth
        self.iters = iters
        self.player_number = player_number
        self.reports = ""
        
        self.performances = {}
        
        # self.run()
        
        
    def run(self) -> None:
        for generation in range(self.depth):
            print(generation)
            report = ""
            report += "\n"
            report += f"---------------------GEN {generation}-------------------------\n"
            report += f"CONFIRMED WEIGHT: {self.best_eval.all_confirmed} -> {self.current_eval.all_confirmed}\n"
            report += f"LOW WEIGHT: {self.best_eval.low_weight} -> {self.current_eval.low_weight}\n"
            report += f"SHOW WEIGHTS: {self.best_eval.show_set_weights} -> {self.current_eval.show_set_weights}\n"
            report += "\n"
        
            sim = MultiSim(self.iters, self.player_number, self.current_eval)
            report += sim.get_report()
            
            avg = statistics.mean(sim.turns)
            # stdev = statistics.stdev(sim.turns)
            # val = avg * stdev
            val = avg
            
            report += "\n"
            report += f"GENETIC SCORE: {val}\n"
            
            report += "-----------------------------------------------------\n"
            report += "\n"
            
            # self.add_performance(sim)
            
            with open(f"report{self.timestamp}.txt", "a") as file:
                file.write(report)
            
            if val < self.best_val:
                print("new best")
                self.best_val = val
                self.best_eval = self.current_eval
            
            self.current_eval = Eval(self.best_eval.all_confirmed, self.best_eval.low_weight, self.best_eval.show_set_weights)
                        
            self.mutate()
            
    
    def add_performance(self, sim: MultiSim):
        self.performances[sim.evaluator] = statistics.mean(sim.turns)

    
    def mutate(self) -> None:
        all = ((random.randint(0, 200) / 100 - 1) / 100 + 1) * self.current_eval.all_confirmed
        low = ((random.randint(0, 200) / 100 - 1) / 100 + 1) * self.current_eval.low_weight
        three = ((random.randint(0, 200) / 100 - 1) / 100 + 1) * self.current_eval.show_set_weights[3]
        two = ((random.randint(0, 200) / 100 - 1) / 100 + 1) * self.current_eval.show_set_weights[2]
        
        self.current_eval = Eval(all, low, {3: three, 2: two})
        
        