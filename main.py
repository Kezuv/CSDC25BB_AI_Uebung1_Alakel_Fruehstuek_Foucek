import aStar
from heuristic import Manhatten
import puzzle

init_puzzle = puzzle.Puzzle(puzzle.Puzzle.generate_random_puzzle())
init_puzzle.display()
goal_puzzle = puzzle.Puzzle.generate_goal_puzzle()
goal_puzzle.display()
heuristic = Manhatten(goal_puzzle)

a_star = aStar.AStar()
a_star.start(init_puzzle, heuristic)
