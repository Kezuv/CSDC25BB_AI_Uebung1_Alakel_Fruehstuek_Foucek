import time
from puzzle import Puzzle
from aStar import AStar
from heuristic import HammingDistance, ManhattanDistance, EuclideanDistance
from tqdm import tqdm


def main():
    num_puzzles = 100
    goal_puzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    heuristics = {
        "Hamming": HammingDistance(),
        "Manhattan": ManhattanDistance(),
        "Euclidean": EuclideanDistance()
    }

    for name, heuristic in heuristics.items():
        total_time = 0
        total_steps = 0

        with tqdm(total=num_puzzles, desc=f"Heuristic {name}") as pbar:
            for i in range(num_puzzles):
                initial_puzzle = Puzzle.generate_random_puzzle()
                solver = AStar(heuristic)

                start_time = time.time()
                solution_path = solver.solve(initial_puzzle, goal_puzzle)
                end_time = time.time()

                total_time += end_time - start_time
                total_steps += len(solution_path) if solution_path else 0
                pbar.update(1)

            average_time = total_time / num_puzzles
            average_steps = total_steps / num_puzzles

            print(f"{name} Heuristic - Average Time: {average_time:.4f} seconds, Average Steps: {average_steps}")


if __name__ == "__main__":
    main()
