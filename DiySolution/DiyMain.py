from DiySolution.DiyHeuristic import Manhattan, Hamingway, Hamingway_WithBlank
from DiySolution.DiyPuzzle import Puzzle
from DiySolution.DiyAStar import AStar


# goal_puzzle.display()

def start(seed, puzzle_count):
    goal_puzzle = Puzzle.generate_goal_puzzle()

    list_init_puzzles = Puzzle.generate_random_puzzle(seed, puzzle_count)


    manhattan_time = 0
    for init_puzzle in list_init_puzzles:
        a_star = AStar()
        manhattan_time += a_star.start(init_puzzle, Manhattan(goal_puzzle))[1]
        print(str(puzzle_count) + ' -- ' + 'Manhattan:')
        #print("{} -- Manhattan: {}".format(puzzle_count,init_puzzle))

    hamming_time = 0
    for init_puzzle in list_init_puzzles:
        a_star = AStar()
        hamming_time += a_star.start(init_puzzle, Hamingway(goal_puzzle))[1]
        print(str(puzzle_count) + ' -- ' + 'Heming: ')

    hamming_withBlank_time = 0
    for init_puzzle in list_init_puzzles:
        a_star = AStar()
        hamming_time += a_star.start(init_puzzle, Hamingway_WithBlank(goal_puzzle))[1]
        puzzle_count += 1
        print(str(puzzle_count) + ' -- ' + 'Hamingway_WithBlank: ')

    print("Average Manhattan time: " + str(manhattan_time/puzzle_count))
    print("Average Heming time: " + str(hamming_time/puzzle_count))
    print("Average Hamingway_WithBlank time: " + str(hamming_withBlank_time/puzzle_count))
