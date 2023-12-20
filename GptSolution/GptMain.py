import time
from GptSolution.GptPuzzle import Puzzle
from GptSolution.GptAStar import AStar
from GptSolution.GptHeuristic import HammingDistance, ManhattanDistance, EuclideanDistance
from tqdm import tqdm


def start(seed, puzzle_count):
    goal_puzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    heuristics = {
        "Hamming": HammingDistance(),
        "Manhattan": ManhattanDistance(),
        "Euclidean": EuclideanDistance()
    }

    list_init_puzzles = Puzzle.generate_random_puzzle(seed, puzzle_count)

    for name, heuristic in heuristics.items():
        total_time = 0
        total_steps = 0

        with tqdm(total=puzzle_count, desc=f"Heuristic {name}") as pbar:
            for i in range(puzzle_count):
                solver = AStar(heuristic)

                start_time = time.time()
                solution_path = solver.solve(list_init_puzzles.__getitem__(i), goal_puzzle)
                end_time = time.time()

                total_time += end_time - start_time
                total_steps += len(solution_path) if solution_path else 0
                pbar.update(1)

            average_time = total_time / puzzle_count
            average_steps = total_steps / puzzle_count

            print(f"{name} Heuristic - Average Time: {average_time:.4f} seconds, Average Steps: {average_steps}")
