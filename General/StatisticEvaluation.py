import csv
import datetime
import os

from DiySolution import DiyMain
from GptSolution import GptMain


def main():
    start_statistic_evaluation(1, 100)


def start_statistic_evaluation(seed, puzzle_count):
    output_directory = f"statisticsOutputs/Seed_{seed}_PuzzleCount_{puzzle_count}"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    each_puzzle_data = "eachPuzzleData.csv"
    average_data = "averageData.csv"

    each_puzzle_data_path = os.path.join(output_directory, each_puzzle_data)
    average_data_path = os.path.join(output_directory, average_data)

    with open(each_puzzle_data_path, "w", newline="") as each_puzzle_data, open(average_data_path, "w",
                                                                                newline="") as average_data:
        each_puzzle_writer = csv.writer(each_puzzle_data)
        each_puzzle_writer.writerow(["Heuristic", "Puzzle Number", "GPT Steps", "DIY Steps",
                                     "GPT Depth", "DIY Depth", "GPT Time", "DIY Time"])

        average_data_writer = csv.writer(average_data)

        average_data_writer.writerow(["Heuristic", "GPT Average Steps", "DIY Average Steps",
                                      "GPT Average Depth", "DIY Average Steps", "GPT Average Time", "DIY Average Time"])


        print("Seednumber: " + str(seed))
        print("Puzzle count: " + str(puzzle_count))
        print("___________________________________________________________________________________\n")
        print("Startzeit:", datetime.datetime.now())

        run_astars(seed, puzzle_count, "Hamming", each_puzzle_writer, average_data_writer)
        run_astars(seed, puzzle_count, "Euclidean", each_puzzle_writer, average_data_writer)
        run_astars(seed, puzzle_count, "Manhattan", each_puzzle_writer, average_data_writer)

        print("Endzeit:", datetime.datetime.now())


def run_astars(seed, puzzle_count, heuristic_function, each_puzzle_writer, average_data_writer):
    (gpt_step_counter_for_each_puzzle,
     gpt_average_step_counter,
     gpt_depth_for_each_puzzle,
     gpt_average_depth,
     gpt_time_for_each_puzzle,
     gpt_average_time) = start_one_heuristic(seed, puzzle_count, "GPT", heuristic_function)

    (diy_step_counter_for_each_puzzle,
     diy_average_step_counter,
     diy_depth_for_each_puzzle,
     diy_average_depth,
     diy_time_for_each_puzzle,
     diy_average_time) = start_one_heuristic(seed, puzzle_count, "DIY", heuristic_function)

    for i in range(len(gpt_step_counter_for_each_puzzle)):
        # each_puzzle_writer.writerow(["Heuristic", "Puzzle Number", "GPT Steps", "DIY Steps",
        #                                      "GPT Depth", "DIY Depth", "GPT Time", "DIY Time"])
        each_puzzle_writer.writerow([heuristic_function, i + 1,
                                     gpt_step_counter_for_each_puzzle[i],
                                     diy_step_counter_for_each_puzzle[i],
                                     gpt_depth_for_each_puzzle[i],
                                     diy_depth_for_each_puzzle[i],
                                     time_formatter(gpt_time_for_each_puzzle[i]),
                                     time_formatter(diy_time_for_each_puzzle[i])
                                     ])

    # average_data_writer.writerow(["Heuristic", "GPT Average Steps", "DIY Average Steps",
    #                                       "GPT Average Depth", "DIY Average Steps",
    #                                       "GPT Average Time", "DIY Average Time"])
    average_data_writer.writerow([heuristic_function,
                                  int(round(gpt_average_step_counter)),
                                  int(round(diy_average_step_counter)),
                                  int(round(gpt_average_depth)),
                                  int(round(diy_average_depth)),
                                  time_formatter(gpt_average_time),
                                  time_formatter(diy_average_time)
                                  ])


def time_formatter(time):
    time *=1000
    formatted_time = int(round(time, 0))
    return formatted_time


def start_one_heuristic(seed, puzzle_count, solution_type, heuristic_function):
    print("==========================================================")
    print(f"               {solution_type} / {heuristic_function}")
    print("==========================================================")
    (step_counter_for_each_puzzle,
     average_step_counter,
     depth_for_each_puzzle,
     average_depth,
     time_for_each_puzzle,
     average_time) = DiyMain.start(seed, puzzle_count, heuristic_function) if solution_type == "DIY" \
        else GptMain.start(seed, puzzle_count, heuristic_function)

    print(f"{solution_type} / {heuristic_function} steps for each puzzle: {step_counter_for_each_puzzle}")
    print(f"{solution_type} / {heuristic_function} depth for each puzzle: {depth_for_each_puzzle}")
    print(f"{solution_type} / {heuristic_function} time each puzzle: {time_for_each_puzzle}")

    print(f"{solution_type} / {heuristic_function} average steps: {average_step_counter}")
    print(f"{solution_type} / {heuristic_function} average depth: {average_depth}")
    print(f"{solution_type} / {heuristic_function} average time: {average_step_counter}")

    print("\n")

    return (step_counter_for_each_puzzle,
            average_step_counter,
            depth_for_each_puzzle,
            average_depth,
            time_for_each_puzzle,
            average_time)


if __name__ == "__main__":
    main()
