import aStar
from heuristic import Manhattan
from heuristic import Hamingway
from puzzle import Puzzle

init_puzzle = Puzzle.generate_random_puzzle()
#init_puzzle = Puzzle([[1,2,3],[4,0,6],[7,5,8]])
#init_puzzle = Puzzle.generate_goal_puzzle()
init_puzzle.display()
goal_puzzle = Puzzle.generate_goal_puzzle()
goal_puzzle.display()
heuristic_Hamming = Hamingway(goal_puzzle)
heuristic_Manhattan = Manhattan(goal_puzzle)

a_star = aStar.AStar()
print(a_star.start(init_puzzle, heuristic_Manhattan))
