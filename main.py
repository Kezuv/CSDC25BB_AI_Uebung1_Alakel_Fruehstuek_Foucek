import aStar
from heuristic import Manhattan, Hamingway, Hamingway_WithBlank
from puzzle import Puzzle

puzzleCnt = 50
solved_puzzles = 0
goal_puzzle = Puzzle.generate_goal_puzzle()
# goal_puzzle.display()


list_init_puzzles = []
while list_init_puzzles.__len__() < puzzleCnt:
    new_puzzle = Puzzle.generate_random_puzzle()
    if new_puzzle.is_solvable():
        list_init_puzzles.append(new_puzzle)


puzzle_count = 0
manhattan_time = 0
for init_puzzle in list_init_puzzles:
    # init_puzzle.display()
    a_star = aStar.AStar()
    puzzle_count += 1
    manhattan_time += a_star.start(init_puzzle, Manhattan(goal_puzzle))[1]
    print(str(puzzle_count) + ' -- ' + 'Manhattan: ' + str(manhattan_time))
    #print("{} -- Manhattan: {}".format(puzzle_count,init_puzzle))

puzzle_count = 0
hamming_time = 0
for init_puzzle in list_init_puzzles:
    # init_puzzle.display()
    a_star = aStar.AStar()
    hamming_time += a_star.start(init_puzzle, Hamingway(goal_puzzle))[1]
    puzzle_count += 1
    print(str(puzzle_count) + ' -- ' + 'Heming: ' + str(a_star.start(init_puzzle, Hamingway(goal_puzzle))))

puzzle_count = 0
hamming_withBlank_time = 0
for init_puzzle in list_init_puzzles:
    # init_puzzle.display()
    a_star = aStar.AStar()
    hamming_time += a_star.start(init_puzzle, Hamingway_WithBlank(goal_puzzle))[1]
    puzzle_count += 1
    print(str(puzzle_count) + ' -- ' + 'Hamingway_WithBlank: ' + str(a_star.start(init_puzzle, Hamingway_WithBlank(goal_puzzle))))

print("Average Manhattan time: " + str(manhattan_time/puzzleCnt))
print("Average Heming time: " + str(hamming_time/puzzleCnt))
print("Average Hamingway_WithBlank time: " + str(hamming_withBlank_time/puzzleCnt))
