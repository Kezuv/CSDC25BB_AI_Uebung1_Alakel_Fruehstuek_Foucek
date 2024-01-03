import time

from GptSolution.GptAStar import AStar
from GptSolution.GptHeuristic import HammingDistance, ManhattanDistance, EuclideanDistance
from GptSolution.GptPuzzle import Puzzle
from GptSolution.GptHeuristic import Heuristic


def start(seed, puzzle_count, heuristic_function_name):
    """Entrypoint for solving puzzles
    :param seed: the seed used for generating random puzzles
    :type seed: int
    :param puzzle_count: the count of puzzles to be solved
    :type puzzle_count: int
    :param heuristic_function_name: the heuristic name to be used
    :type heuristic_function_name: str
    :returns: step_counter_for_each_puzzle,average_step_counter,depth_for_each_puzzle,average_depth,time_for_each_puzzle,average_time
    :rtype: (int[], int, int[], int, float[], float)
    """
    # initialize attributes for statistic evaluation
    step_counter_for_each_puzzle = []
    average_step_counter = 0
    depth_for_each_puzzle = []
    average_depth = 0
    time_for_each_puzzle = []
    average_time = 0.0

    goal_puzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    # set the heuristic function based on the function name
    if heuristic_function_name == "Hamming":
        heuristic_function = HammingDistance()
    if heuristic_function_name == "Manhattan":
        heuristic_function = ManhattanDistance()
    if heuristic_function_name == "Euclidean":
        heuristic_function = EuclideanDistance()

    # generate a set of solveable puzzles
    list_init_puzzles = Puzzle.generate_random_puzzle(seed, puzzle_count)

    # loop through all puzzle
    for i in range(puzzle_count):
        # initialize the solver with the chosen heuristic function
        solver = AStar(heuristic_function)

        # start the astar algorithm
        start_time = time.time()
        current_step, current_depth = solver.solve(list_init_puzzles.__getitem__(i), goal_puzzle)
        end_time = time.time()

        # calculate statistic values
        process_time = end_time - start_time
        time_for_each_puzzle.append(process_time)
        average_time += process_time

        step_counter_for_each_puzzle.append(current_step)
        average_step_counter += current_step

        depth_for_each_puzzle.append(current_depth)
        average_depth += current_depth

    # calculate avarage values for statistic evaluation
    average_time /= len(list_init_puzzles)
    average_step_counter /= len(list_init_puzzles)
    average_depth /= len(list_init_puzzles)

    return (step_counter_for_each_puzzle,
            average_step_counter,
            depth_for_each_puzzle,
            average_depth,
            time_for_each_puzzle,
            average_time)
