import time

from DiySolution.DiyAStar import AStar
from DiySolution.DiyHeuristic import Manhattan, Hamming, Euclidean
from DiySolution.DiyPuzzle import Puzzle


def start(seed, puzzle_count, heuristic_function_name):
    """Declares the parameters for the puzzle analysis and runs the solving method"""
    step_counter_for_each_puzzle = []
    average_step_counter = 0
    depth_for_each_puzzle = []
    average_depth = 0
    time_for_each_puzzle = []
    average_time = 0.0

    goal_puzzle = Puzzle.generate_goal_puzzle()

    list_init_puzzles = Puzzle.generate_random_puzzle(seed, puzzle_count)

    if heuristic_function_name == "Hamming":
        heuristic_function = Hamming(goal_puzzle)
    if heuristic_function_name == "Manhattan":
        heuristic_function = Manhattan(goal_puzzle)
    if heuristic_function_name == "Euclidean":
        heuristic_function = Euclidean(goal_puzzle)

    for init_puzzle in list_init_puzzles:
        a_star = AStar()

        start_time = time.time()
        current_step, current_depth = a_star.solve(init_puzzle, heuristic_function)
        end_time = time.time()

        process_time = end_time - start_time
        time_for_each_puzzle.append(process_time)
        average_time += process_time

        step_counter_for_each_puzzle.append(current_step)
        average_step_counter += current_step

        depth_for_each_puzzle.append(current_depth)
        average_depth += current_depth

    average_time /= len(list_init_puzzles)
    average_step_counter /= len(list_init_puzzles)
    average_depth /= len(list_init_puzzles)

    return (step_counter_for_each_puzzle,
            average_step_counter,
            depth_for_each_puzzle,
            average_depth,
            time_for_each_puzzle,
            average_time)
