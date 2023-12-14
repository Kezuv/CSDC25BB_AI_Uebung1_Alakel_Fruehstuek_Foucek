import aStar
from heuristic import Manhatten
import puzzle

init_puzzle = puzzle.Puzzle(puzzle.Puzzle.generate_random_puzzle())
heuristic = Manhatten()
a_star = aStar.AStar()
a_star.start(init_puzzle, heuristic)
