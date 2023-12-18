import aStar
from heuristic import Manhattan
from heuristic import Hamingway
from puzzle import Puzzle

solved_puzzles = 0
goal_puzzle = Puzzle.generate_goal_puzzle()
# goal_puzzle.display()

list_init_puzzles = []
while list_init_puzzles.__len__() < 10:
    new_puzzle = Puzzle.generate_random_puzzle()
    if new_puzzle.is_solvable():
        list_init_puzzles.append(new_puzzle)


for init_puzzle in list_init_puzzles:
    # init_puzzle.display()
    a_star = aStar.AStar()
    print('Manhattan: ' + str(a_star.start(init_puzzle, Manhattan(goal_puzzle))))

for init_puzzle in list_init_puzzles:
    # init_puzzle.display()
    a_star = aStar.AStar()
    print('Heming: ' + str(a_star.start(init_puzzle, Hamingway(goal_puzzle))))
