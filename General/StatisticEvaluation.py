from GptSolution import GptMain
from DiySolution import DiyMain
# for each heuristic:
# step counter for each puzzle
# average step counter
# depth for each puzzle
# average depth
# time for each puzzle
# average time
def main():
    seed = 11
    puzzle_count = 5

    start_one_heuristic(seed, puzzle_count, "Manhattan")
    start_one_heuristic(seed, puzzle_count, "Hamming")
    start_one_heuristic(seed, puzzle_count, "Euclidean")

def start_one_heuristic(seed, puzzle_count, heuristic_function):
    print("==========================================================")
    print("               GPT", heuristic_function)
    print("==========================================================")
    (step_counter_for_each_puzzle,
     average_step_counter,
     depth_for_each_puzzle,
     average_depth,
     time_for_each_puzzle,
     average_time) = GptMain.start(seed, puzzle_count, heuristic_function)

    print(heuristic_function, " GPT steps for each puzzle:", step_counter_for_each_puzzle)
    print(heuristic_function, " GPT average steps", average_step_counter)
    print(heuristic_function, " GPT depth for each puzzle:", depth_for_each_puzzle)
    print(heuristic_function, " GPT average depth:", average_depth)
    print(heuristic_function, " GPT time for each puzzle:", time_for_each_puzzle)
    print(heuristic_function, " GPT average time:", average_time)

    print("==========================================================")
    print("                DIY", heuristic_function)
    print("==========================================================")
    (step_counter_for_each_puzzle,
     average_step_counter,
     depth_for_each_puzzle,
     average_depth,
     time_for_each_puzzle,
     average_time) = DiyMain.start(seed, puzzle_count, heuristic_function)

    print(heuristic_function, " DIY steps for each puzzle:", step_counter_for_each_puzzle)
    print(heuristic_function, " DIY average steps", average_step_counter)
    print(heuristic_function, " DIY depth for each puzzle:", depth_for_each_puzzle)
    print(heuristic_function, " DIY average depth:", average_depth)
    print(heuristic_function, " DIY time for each puzzle:", time_for_each_puzzle)
    print(heuristic_function, " DIY average time:", average_time)


if __name__ == "__main__":
    main()