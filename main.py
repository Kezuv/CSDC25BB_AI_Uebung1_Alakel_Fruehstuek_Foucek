import aStar
from heuristic import Manhattan
from heuristic import Hamingway
from puzzle import Puzzle

solved_puzzles = 0
goal_puzzle = Puzzle.generate_goal_puzzle()
# goal_puzzle.display()
heuristic_Hamingway = Hamingway(goal_puzzle)
heuristic_Manhattan = Manhattan(goal_puzzle)

while solved_puzzles <= 100:

    init_puzzle = Puzzle.generate_random_puzzle()
    if init_puzzle.is_solvable():
        init_puzzle.display()
        a_star = aStar.AStar()
        print(a_star.start(init_puzzle, heuristic_Manhattan))
        solved_puzzles += 1

