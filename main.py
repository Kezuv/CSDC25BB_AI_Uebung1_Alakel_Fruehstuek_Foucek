# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
"""
from PuzzleSolver import PuzzleSolver
from StateGenerator import StateGenerator
import numpy as np
import time

def main():
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    num_puzzles = 100
    heuristics = ['hamming', 'manhattan', 'euclidean']

    for heuristic in heuristics:
        total_time = 0
        total_steps = 0

        for _ in range(num_puzzles):
            initial_state = StateGenerator.generate_state(seed=None)  # None for random seeding each time
            solver = PuzzleSolver(initial_state, goal_state)

            start_time = time.time()
            solution = solver.solve(heuristic)
            end_time = time.time()

            total_time += end_time - start_time

            # Count the number of steps in the solution
            steps = 0
            while solution and solution.parent:
                steps += 1
                solution = solution.parent

            total_steps += steps

        average_time = total_time / num_puzzles
        average_steps = total_steps / num_puzzles

        print(f"{heuristic} heuristic: Average Time = {average_time} seconds, Average Steps = {average_steps}")

if __name__ == "__main__":
    main()
"""
